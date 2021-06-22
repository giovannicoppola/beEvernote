# beEvernoteZero (deprecated)
Inbox Zero for Evernote using Beeminder

**Update 2020: deprecated as Evernote abandoned developer access**

The goal of this script is to count the notes in an Evernote notebook and to post that number onto a Beeminder goal. 

You will need to install the following:
1. Evernote SDK (https://dev.evernote.com/doc)
2. Python packages (requests, json) #json not needed for this particular script

Variables to replace in the script: 
1. Evernote developer token (https://dev.evernote.com/doc/articles/dev_tokens.php)
2. GUID of the Evernote notebook you want to count notes in, which can be obtained from the URL in the web interface (see https://discussion.evernote.com/topic/37081-archived-how-to-find-notebook_guid) or using the code commented out at the bottom of the script
3. a personal auth token from your Beeminder account (http://api.beeminder.com/#auth)
4. your Beeminder username
5. your Beeminder goal name
