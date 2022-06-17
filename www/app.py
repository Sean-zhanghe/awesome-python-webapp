# -*- coding:utf-8 -*-
import logging
logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime
from aiohttp import web
import orm
from models import User, Blog, Comment


def index(request):
    return web.Response(body=b'<h1>Awesome</h1>', headers={'content-type':'text/html'})


async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    await site.start()

    # srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    # logging.info('server started at http://127.0.0.1:9000...')
    # return srv


async def test(loop):
    await orm.create_pool(loop=loop, user='root', password='123456', db='awesome')
    u = User(name='Test', email='test@example.com', password='1234567890', image='about:blank')
    await u.save()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # loop.run_until_complete(init(loop))
    loop.run_until_complete(test(loop))
    # loop.run_forever()
