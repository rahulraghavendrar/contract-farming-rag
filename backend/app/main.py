from fastapi import (
    FastAPI,
    UploadFile,
    File
)

from app.services.rag_service import (
    process_pdf,
    retrieve_context
)

from app.services.gemini_service import (
    generate_answer
)

from app.schemas.chat import (
    ChatRequest
)

import shutil

app=FastAPI()


@app.get("/")
def home():

    return {
        "message":"Contract Farming RAG Running"
    }


@app.post("/upload")

async def upload_pdf(
    file:UploadFile=File(...)
):

    pdf_path=f"app/uploads/{file.filename}"

    with open(
        pdf_path,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    process_pdf(
        pdf_path
    )

    return {
        "message":"PDF Uploaded Successfully"
    }


@app.post("/chat")

async def chat(
    request:ChatRequest
):

    context=retrieve_context(
        request.question
    )

    answer=generate_answer(
        context,
        request.question
    )

    return {
        "answer":answer
    }