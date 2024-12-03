For this program to work, you need a few prerequisites. 

 	,_     _
	 |\\_,-~/
	 / _  _ |    ,--.
	(  @  @ )   / ,-'
	 \  _T_/-._( (
	 /         `. \
	|         _  \ |
	 \ \ ,  /      |
	  || |-_\__   /
	 ((_/`(____,-'



Make sure you have BOTH python, AND google installed. You can do this with other browsers too, but its fastest and easiest with google. 
This script only runs on Python version 3.7 and higher, for installing python on linux:

	https://docs.python-guide.org/starting/install3/linux/
	sudo apt install python3-venv
 
	pip install google-api-python-client google-auth google-auth-oauthlib google-auth-httplib2
	import googleapiclient.discovery
	import google.auth
	import google_auth_oauthlib.flow
 
You also need to authenticate your Google account, so the script can take the information, log in, and see the comments you left.
1.	Create a Project in Google Cloud Console

  Go to the Google Cloud Console.
  Log in with your Google account.
  Click on "Select a Project" in the top navigation bar, then click "New Project".
  Give your project a name (e.g., "YouTube Comment Sorter") and click "Create".

2. Enable the YouTube Data API

    After your project is created, go to the APIs & Services > Library in the Cloud Console.
    Search for "YouTube Data API v3" and click on it.
    Click Enable to activate the API for your project.

3. Create OAuth Credentials

    Go to APIs & Services > Credentials.
    Click on Create Credentials > OAuth client ID.
    If prompted to configure a consent screen, follow the instructions:
        Set the User Type to "External" and click Create.
        Fill in the basic information (App Name, User Support Email, etc.).
        Save the consent screen configuration.
    Under Application Type, select Desktop App.
    Enter a name for the credentials (e.g., "YouTube API Desktop Credentials") and click Create.
    A dialog will appear with your Client ID and Client Secret. Click Download JSON to download the credentials file.
    Save the file as client_secrets.json in the same directory as your script.




If you run into the same issues on Linux as I have where pip cannot run the command, you have a few extra steps to run in bash:

	python3 -m venv myenv
	source myenv/bin/activate
	cd ~/Desktop/youtube\ comment\ sorter/ (if you already dont have it set to your location, this is what it was for me)

actually run the script using:

	python youtubecommentsorter.py


If you have any extra questions, ask chatgpt, the allmightly holder of knowledge :P
Have fun!
