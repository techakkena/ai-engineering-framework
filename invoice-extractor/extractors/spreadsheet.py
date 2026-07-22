import io

import pandas as pd
from fastapi import HTTPException


def extract(data: bytes, extension: str) -> dict:
    try:
        if extension == "csv":
            df = pd.read_csv(io.BytesIO(data))
        else:
            df = pd.read_excel(io.BytesIO(data))
    except Exception as exc:
        raise HTTPException(status_code=400, detail="Could not parse the uploaded spreadsheet.") from exc

    return {"kind": "text", "text": df.to_csv(index=False)}
