from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import logging
import os

from qa_generator import generate_qa_pairs, save_qa_to_docx

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

temp_results = {}

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "results": None}
    )

@app.post("/", response_class=HTMLResponse)
async def generate(request: Request, summary: str = Form(...)):

    try:
        results = generate_qa_pairs(summary)

        session_id = str(abs(hash(summary)))[:10]
        temp_results[session_id] = results

        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "results": results,
                "summary": summary,
                "session_id": session_id
            }
        )

    except Exception as e:
        logger.error(str(e))
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "results": [],
                "error": f"Error: {str(e)}",
                "summary": summary
            }
        )

@app.get("/download/{session_id}")
async def download_docx(session_id: str):

    if session_id not in temp_results:
        return HTMLResponse("Session expired. Please regenerate.", status_code=404)

    results = temp_results[session_id]
    output_path = f"questions_{session_id}.docx"

    save_qa_to_docx(results, output_path)

    return FileResponse(
        path=output_path,
        filename="Generated_Questions.docx",
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )

@app.on_event("shutdown")
async def cleanup():
    for file in os.listdir("."):
        if file.startswith("questions_") and file.endswith(".docx"):
            try:
                os.remove(file)
            except:
                pass
