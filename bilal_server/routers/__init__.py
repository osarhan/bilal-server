from bilal_server.routers import client


def add_routes(app):
    app.include_router(client.bilal_server, tags=['athan tag'])
