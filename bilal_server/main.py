from fastapi import FastAPI
from bilal_server.routers import add_routes


def _initialize():
    app = FastAPI(
        title='Bilal Server',
        description='Backend server for Athan App',
    )
    add_routes(app)
    return app


app = _initialize()


@app.on_event("startup")
async def startup_event():
    pass


@app.on_event("shutdown")
async def shutdown_event():
    pass
