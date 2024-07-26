from os import path
import pickle
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Update SCOPES to include Google Tasks
SCOPES = ['https://www.googleapis.com/auth/calendar.events',
                   'https://www.googleapis.com/auth/calendar','https://www.googleapis.com/auth/tasks']

def get_credentials_google():
    flow = InstalledAppFlow.from_client_secrets_file("creds.json", SCOPES)
    print("Getting credentials", flow)
    creds = flow.run_local_server()

    # Save the credentials for the next run
    pickle.dump(creds, open("token.txt", "wb"))
    return creds

def get_calendar_service():
    creds = None
    if path.exists("token.txt"):
        creds = pickle.load(open("token.txt", "rb"))
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            creds = get_credentials_google()
    service = build("calendar", "v3", credentials=creds)
    return service

def get_tasks_service():
    creds = None
    if path.exists("token.txt"):
        creds = pickle.load(open("token.txt", "rb"))
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            creds = get_credentials_google()
    service = build("tasks", "v1", credentials=creds)
    return service
