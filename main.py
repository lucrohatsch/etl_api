from fastapi import FastAPI, HTTPException
from api.config.settings import VERSION
from fastapi.middleware.cors import CORSMiddleware
from api.routes.reports_router import reports_router


description = ""

app = FastAPI(
    title="RD_APP_REPORTS",
    description=description,
    version=VERSION
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(reports_router, prefix=("/reports"), tags=["Reports"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
