from fastapi import APIRouter, UploadFile, File, HTTPException,status
from starlette.concurrency import run_in_threadpool
import cloudinary.uploader
from schemas.file_handler import FileUploadResponse

router = APIRouter(prefix="/file", tags=["File handling"])

MAX_SIZE = 10 * 1024 * 1024 # 10MB

def validate_file(file: UploadFile, contents: bytes):
    if len(contents) > MAX_SIZE:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="File exceeds 10MB limit")
    

@router.post("/upload", response_model=FileUploadResponse ,status_code=status.HTTP_201_CREATED)
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    validate_file(file, contents)

    result = await run_in_threadpool(
        cloudinary.uploader.upload,
        contents,
        folder="portfolio",
        resource_type="auto"
    )

    return {
        "url": result["secure_url"],
        "public_id": result["public_id"]
    }

@router.delete("/{public_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_file(public_id: str):
    result = await run_in_threadpool(
        cloudinary.uploader.destroy,
        public_id
    )

    if result.get("result") not in ("ok", "not found"):
        raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, detail="Failed to delete from Cloudinary")
    return