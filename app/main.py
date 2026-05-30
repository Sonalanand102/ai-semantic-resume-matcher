from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.job_routes import router as job_router
from app.routes.match_routes import router as match_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(job_router)
app.include_router(match_router)

@app.get("/")
def root():
    return {"message": "AI Job Matcher Running"}