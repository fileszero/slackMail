import pickle
import os.path
import re
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

class GooglePeople:
    # If modifying these scopes, delete the file token.pickle.
    SCOPES = ['https://www.googleapis.com/auth/contacts.readonly']
    _Contacts = None
    def __init__(self):
        """Shows basic usage of the People API.
        Prints the name of the first 10 connections.
        """
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', self.SCOPES)
                creds = flow.run_console()
                # creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        self.service = build('people', 'v1', credentials=creds)

    # https://1upnoob.blogspot.com/2020/06/google-people-api-python-1.html?_sm_au_=iHVSF4qS7P48k8n5N4s4kKHFLKVG2
    def getContacts(self):
        # check cache
        if self._Contacts:
            return self._Contacts

        self._Contacts=[]
        next_page_token  = ''
        while True:
            if not (next_page_token is None):
                # Call the People API
                results = self.service.people().connections().list(
                        resourceName = 'people/me',
                        pageSize     = 500,
                        personFields = 'names,emailAddresses,phoneNumbers',
                        pageToken    = next_page_token
                        ).execute()
                self._Contacts = self._Contacts + results.get('connections', [])
                next_page_token  = results.get('nextPageToken')
            else:
                break
        return self._Contacts

    def getContactByPhoneNumber(self, num):
        searchNum = re.sub(r'[^\d]', '',num)

        # Call the People API
        contacts = self.getContacts()
        for contact in contacts:
            phoneNumbers=contact.get("phoneNumbers")
            if not phoneNumbers:
                continue
            for phonenum in phoneNumbers:
                pnum=re.sub(r'[^\d]', '',phonenum.get("value"))
                # print(pnum)
                if(pnum==searchNum):
                    return contact

if __name__ == '__main__':
    api=GooglePeople()
    contact=api.getContactByPhoneNumber("0120-914-557")
    print(contact)
    name="/".join(map(lambda name: name.get("displayName"),contact.get("names")))
    print(name)

    contact=api.getContactByPhoneNumber("1234-567-890")
    print(contact)
