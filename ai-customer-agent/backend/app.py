import shutil

from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel

"""from ai_service import ask_ai"""
from ai_service import ask_rag
from database.db import SessionLocal
from database.models import Ticket
from fastapi.middleware.cors import CORSMiddleware
from integrations.google_drive import sync_google_drive
from rag.process_pdf import process_pdf
from tickets.ticket_service import (
    get_all_tickets,
    update_ticket_status,
)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "AI Customer Support Agent Running"}


class ChatRequest(BaseModel):
    user_id: str
    message: str


@app.post("/chat")
def chat(data: ChatRequest):

    result = ask_rag(data.user_id, data.message)

    return result


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    chunk_count = process_pdf(file_path)

    return {"message": "PDF processed", "chunks": chunk_count}


@app.get("/tickets")
def tickets():

    return get_all_tickets()


@app.get("/tickets/{ticket_id}")
def get_ticket(ticket_id: int):

    db = SessionLocal()

    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()

    db.close()

    if not ticket:
        return {"message": "Ticket not found"}

    return {
        "id": ticket.id,
        "user_id": ticket.user_id,
        "issue": ticket.issue,
        "priority": ticket.priority,
        "status": ticket.status,
    }


@app.put("/tickets/{ticket_id}")
def update_ticket(ticket_id: int, status: str):

    ticket = update_ticket_status(ticket_id, status)

    if not ticket:
        return {"message": "Ticket not found"}

    return {"message": "updated", "ticket_id": ticket.id, "status": ticket.status}


@app.post("/sync-drive")
def sync_drive():

    count = sync_google_drive()

    return {"message": f"{count} files synced"}


process_document()
