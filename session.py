from typing import Any

from aiogram.client.session.aiohttp import AiohttpSession
from ujson import loads, dumps


class Session(AiohttpSession):

    def __init__(self, **kwargs: Any):
        super().__init__(**kwargs)


session = Session(json_dumps=dumps, json_loads=loads)
