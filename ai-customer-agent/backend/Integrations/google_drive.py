import sys
import os
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)
sys.path.insert(0, BASE_DIR)

print("BASE_DIR =", BASE_DIR)
print("FILES IN BASE_DIR =", os.listdir(BASE_DIR))
from rag.process_pdf import process_pdf
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
import io


def download_file(file_id, file_name):

    request = drive_service.files().get_media(
        fileId=file_id
    )

    os.makedirs("uploads", exist_ok=True)

    file_path = os.path.join(
        "uploads",
        file_name
    )

    with open(file_path, "wb") as fh:

        downloader = MediaIoBaseDownload(
            fh,
            request
        )

        done = False

        while not done:
            status, done = (
                downloader.next_chunk()
            )

    return file_path

SCOPES = [
    "https://www.googleapis.com/auth/drive.readonly"
]

SERVICE_ACCOUNT_FILE = (
    "credentials/service-account.json"
)

FOLDER_ID = "1-pgHyoTjD5-S02gG_tslE2THYsyw6ede"

credentials = (
    service_account.Credentials
    .from_service_account_file(
        SERVICE_ACCOUNT_FILE,  
        scopes=SCOPES
    )
)

drive_service = build(
    "drive",
    "v3",
    credentials=credentials
)

def get_drive_files():

    results = (
        drive_service.files()
        .list(
            pageSize=100,
            fields="files(id,name,mimeType)"
        )
        .execute()
    )

    files = results.get("files", [])

    for file in files:
        print(
            file["name"],
            file["mimeType"]
        )

    return files

if __name__ == "__main__":

    files = get_drive_files()

    print("\nFILES FOUND:")
    print(files)

    for file in files:

        if file["mimeType"] == "application/pdf":
            path = download_file(
                file["id"],
                file["name"]
            )

            print(
                "Downloaded:",
                path
            )

    print(
        "\nService Account Email:",
        credentials.service_account_email
    )
def sync_google_drive():

    files = get_drive_files()

    for file in files:

        name = file["name"].lower()

        # Skip folders
        if file["mimeType"] == "application/vnd.google-apps.folder":
            continue

        path = download_file(
            file["id"],
            file["name"]
        )

        if name.endswith(".pdf"):

            process_pdf(path)

        elif name.endswith(".xlsx"):

            process_excel(path)

        elif name.endswith(".csv"):

            process_csv(path)

        elif name.endswith(".docx"):

            process_docx(path)

        print(
            f"Processed: {file['name']}"
        )

    return len(files)

def process_document(path):

    if path.endswith(".pdf"):
        process_pdf(path)

    elif path.endswith(".xlsx"):
        process_excel(path)

    elif path.endswith(".docx"):
        process_docx(path)

    elif path.endswith(".csv"):
        process_csv(path)
    

