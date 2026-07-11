from database.db import SessionLocal
from database.models import Ticket

ESCALATION_KEYWORDS = [
    "refund",
    "complaint",
    "damaged",
    "broken",
    "cancel",
    "return",
    "support",
]


def needs_escalation(message):

    text = message.lower()

    for word in ESCALATION_KEYWORDS:
        if word in text:
            return True

    return False


def detect_priority(issue):

    text = issue.lower()

    if any(word in text for word in ["urgent", "critical", "emergency"]):
        return "Critical"

    if any(word in text for word in ["refund", "broken", "damaged"]):
        return "High"

    return "Medium"


def create_ticket(user_id, issue, priority="Medium"):

    db = SessionLocal()

    ticket = Ticket(user_id=user_id, issue=issue, priority=priority, status="Open")

    db.add(ticket)
    db.commit()
    db.refresh(ticket)
    db.close()

    return ticket


def get_all_tickets():

    db = SessionLocal()

    tickets = db.query(Ticket).all()

    db.close()

    return tickets


def update_ticket_status(ticket_id, status):

    db = SessionLocal()

    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()

    if ticket:
        ticket.status = status
        db.commit()
        db.refresh(ticket)

    db.close()

    return ticket
