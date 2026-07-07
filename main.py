from fastapi import FastAPI
from routers import build_notes, case_studies, experience, messages, services, stats, users

app = FastAPI(
    title="Portfolio API",
    description="This is a portfolio API built with FastAPI.",
    version="1.0.0"
)

# app.include_router(build_notes.router)
# app.include_router(case_studies.router)
# app.include_router(experience.router)
# app.include_router(messages.router)
# app.include_router(profile.router)
# app.include_router(services.router)
# app.include_router(stats.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Portfolio API!"}

