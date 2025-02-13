import uvicorn
from fastapi import FastAPI
from app.routers.html_router import router as html_router
from app.routers.api_router import router as api_router

app = FastAPI(
    title="API web-приложения 'CI/CD utils'",
    description="""
            Обрабатывает клиентские запросы на стек CI/CD.
            Реализует основную логику взаимодействия с сервером web-приложением.
            """,
    version="1.0.0",
)

app.include_router(html_router)
app.include_router(api_router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
