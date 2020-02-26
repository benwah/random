from sanic import Sanic
from sanic.response import HTTPResponse

import asyncio
import os

CURRENT_PATH = os.path.dirname(__file__)
JSON_PAYLOAD_PATH = os.path.join(CURRENT_PATH, 'payload.json')
f = open(JSON_PAYLOAD_PATH, 'r')
data = f.read()
f.close()

class Config(object):
    REQUEST_BUFFER_QUEUE_SIZE = 1024 * 100
    REQUEST_TIMEOUT = 60 * 10
    RESPONSE_TIMEOUT = 60 * 10
    KEEP_ALIVE_TIMEOUT = 60


app = Sanic()
app.config.from_object(Config)

@app.route('/')
async def json(request):
    await asyncio.sleep(10)

    return HTTPResponse(
        data,
        headers=None,
        status=200,
        content_type="application/json",
    )
