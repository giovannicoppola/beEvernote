# Wednesday August 30, 2017, 12:53 PM
# Super simple script to retrieve the number of notes in a particular Evernote notebook and update a Beeminder goal

import hashlib
import binascii
import evernote.edam.userstore.constants as UserStoreConstants
import evernote.edam.type.ttypes as Types
import datetime
import requests
import json


from evernote.api.client import EvernoteClient
from evernote.edam.notestore.ttypes import NoteFilter, NotesMetadataResultSpec


#PRODUCTION VERSION TOKEN
#Get dev_token from https://www.evernote.com/api/DeveloperToken.action
dev_token = "YOUR-DEV-TOKEN-GOES-HERE"
client = EvernoteClient(token=dev_token, sandbox=False)
user_store = client.get_user_store()
note_store = client.get_note_store()

#checking Evernote API version
version_ok = user_store.checkVersion(
    "Evernote EDAMTest (Python)",
    UserStoreConstants.EDAM_VERSION_MAJOR,
    UserStoreConstants.EDAM_VERSION_MINOR
)

if not version_ok:
  print "outdated API!"
  exit(1)


beEverLog = open('beEverLogFile.txt', 'a+') #opening log file

#a function to parse the notebook count (probably there is a better way to either obtain the count, or to parse the count output)
def ParseCount (myText):
	myStart = ': '
	myEnd = '}'
	s = myText
	return((s.split(myStart))[1].split(myEnd)[0])


myfilter = NoteFilter(notebookGuid='YOUR-NOTEBOOK-GUID-GOES-HERE')
myCount = note_store.findNoteCounts(dev_token,myfilter,False)
myCountString= str(myCount.notebookCounts)
currentNoteCount =  ParseCount(myCountString)


# Posting datapoint onto Beeminder goal

data = [
  ('auth_token', 'YOUR-BEEMINDER-AUTH-TOKEN-GOES-HERE'),
  ('value', currentNoteCount),
  ('comment', 'from EvernoteScript!'),
]

requests.post('https://www.beeminder.com/api/v1/users/YOUR-BEEMINDER-USERNAME/goals/YOUR-BEEMINDER-GOAL/datapoints.json', data=data)

#print myJsonQuery	
print>>beEverLog,('{:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now())+ ' -- ok')
print "script executed!"



###########################
## Retrieving Evernote notebook GUIDs. 
## To list all of the notebooks in the user's account:

#notebooks = note_store.listNotebooks()
#print "Found ", len(notebooks), " notebooks:"
#for notebook in notebooks:
	#print "  * ", notebook.name
	#print "  * ", notebook.guid
##########################


