import json
import os

FILE_PATH = "metadata/documents.json"


def save_document(filename, chunks):

    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, "w") as f:
            json.dump([], f)

    with open(FILE_PATH, "r") as f:
        data = json.load(f)

    data.append({"filename": filename, "chunks": chunks})

    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=4)
