def extract(data: bytes) -> dict:
    return {"kind": "text", "text": data.decode("utf-8", errors="ignore")}
