import os

from dotenv import load_dotenv
from memory.chat_memory import add_message, get_history
from openai import OpenAI
from rag.retriever import search_documents
from tickets.ticket_service import create_ticket, needs_escalation

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def ask_rag(user_id, question):

    if needs_escalation(question):
        ticket = create_ticket(user_id=user_id, issue=question)

        return {
            "answer": f"Support ticket created. Ticket ID: {ticket.id} | Status: {ticket.status}",
            "sources": [],
        }

    docs = search_documents(question)
    history = get_history(user_id)

    history_text = "\n".join(
        [f"{msg['role']}: {msg['content']}" for msg in history[-10:]]
    )

    # Build context
    context = "\n\n".join([doc.page_content for doc in docs])

    # Collect source files
    sources = []

    for doc in docs:
        source = doc.metadata.get("source")

        if source:
            sources.append(source)

    prompt = f"""
You are a customer support assistant.

Conversation History:
{history_text}

Knowledge Base Context:
{context}

Current Question:
{question}

Instructions:
- Use Conversation History when the user asks about previous messages.
- Use Knowledge Base Context for company/product questions.
- If the user's name appears in the conversation history, answer using that information.
- Only say "I could not find that information." if it is not available in either place.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini", messages=[{"role": "user", "content": prompt}]
    )

    answer = response.choices[0].message.content

    add_message(user_id, "user", question)

    add_message(user_id, "assistant", answer)
    return {"answer": answer, "sources": list(set(sources))}
