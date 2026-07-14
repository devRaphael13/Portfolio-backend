from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination
from routers import build_notes, case_studies, experiences, messages, services, stats, users, auth, file_handler

app = FastAPI(
    title="Portfolio API",
    description="This is a portfolio API built with FastAPI.",
    version="1.0.0"
)


app.include_router(build_notes.router)
app.include_router(file_handler.router)
app.include_router(case_studies.router)
app.include_router(experiences.router)
app.include_router(messages.router)
app.include_router(users.router)
app.include_router(services.router)
app.include_router(stats.router)
app.include_router(auth.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

add_pagination(app)

@app.get("/")
def root():
    return {"message": "Welcome to the Portfolio API!"}

