from sanic import Sanic
from sanic.response import HTTPResponse

import asyncio
import os

CURRENT_PATH = os.path.dirname(__file__)
JSON_PAYLOAD_PATH = os.path.join(CURRENT_PATH, 'payload.json')
f = open(JSON_PAYLOAD_PATH, 'r')
data = f.read()
f.close()


app = Sanic()
@app.route('/')
async def json(request):
    await asyncio.sleep(10)

    return HTTPResponse(
        data,
        headers=None,
        status=200,
        content_type="application/json",
    )
