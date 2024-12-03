import os
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# Scopes for accessing YouTube Data API
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']

def authenticate_youtube():
    """
    Authenticate with YouTube Data API using OAuth2.
    Returns the YouTube API service object.
    """
    creds = None
    # Check if a token file exists
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    
    # Authenticate if credentials are missing or invalid
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # Use client_secrets.json to authenticate
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secrets.json', SCOPES)
            creds = flow.run_local_server(port=8080)
        
        # Save credentials for future use
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    
    return build('youtube', 'v3', credentials=creds)

def fetch_comments(youtube):
    """
    Fetch all comments made by the authenticated user.
    Returns a list of comments.
    """
    comments = []
    
    # Get the authenticated user's channel information
    request = youtube.channels().list(
        part="contentDetails",
        mine=True
    )
    response = request.execute()
    
    # Extract the channel ID
    channel_id = response["items"][0]["id"]
    
    # Fetch the comment threads from the authenticated user's channel
    request = youtube.commentThreads().list(
        part="snippet",
        allThreadsRelatedToChannelId=channel_id,
        maxResults=50  # Adjust this number based on your needs
    )
    
    # Keep fetching comments while there are more pages
    while request:
        response = request.execute()
        comments.extend(response.get('items', []))  # Add comments to the list
        
        # If there's a next page, make another request
        request = youtube.commentThreads().list_next(request, response)
    
    return comments

def main():
    # Authenticate and create the YouTube API service object
    youtube = authenticate_youtube()
    
    # Fetch user comments
    print("Fetching your comments...")
    comments = fetch_comments(youtube)
    
    if not comments:
        print("No comments found!")
        return
    
    # Extract and sort comments by like count
    print("Sorting comments by likes...")
    sorted_comments = sorted(
        comments, 
        key=lambda x: int(x['snippet']['topLevelComment']['snippet']['likeCount']), 
        reverse=True
    )
    
    # Display the sorted comments
    print("\nYour comments sorted by likes:")
    for comment in sorted_comments:
        text = comment['snippet']['topLevelComment']['snippet']['textDisplay']
        likes = comment['snippet']['topLevelComment']['snippet']['likeCount']
        print(f"Likes: {likes} | Comment: {text}")

if __name__ == "__main__":
    main()
