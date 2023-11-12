import uvicorn
from fastapi import FastAPI

from src.routes.route1 import route_one
from src.routes.route2 import route_two

app = FastAPI(
    title="MyApp",
    description="""
                That's really it!
                """,
    version="1.0.0",
)

app.include_router(route_one, prefix="/route_one", tags=["route_one"])

app.include_router(route_two, prefix="/route_two", tags=["route_two"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
