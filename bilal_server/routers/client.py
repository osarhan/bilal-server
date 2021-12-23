from fastapi import APIRouter

bilal_server = APIRouter(
    prefix='/api/bilal-server',
    responses={200: {'description': 'success'},
               500: {'description': 'failure'}},
)


@bilal_server.get('/prayer-times')
async def get_prayer_times():
    return {'hello world'}
