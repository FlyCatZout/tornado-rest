#!/usr/bin/env python
#
# Copyright 2013 Rodrigo Ancavil del Pino
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

# -*- coding: utf-8 -*-

import tornado.ioloop
import pyrestful.rest
import asyncio

from pyrestful import mediatypes
from pyrestful.rest import get

class AsyncService(pyrestful.rest.RestHandler):
    @get('/async/{time}',{'format':'json'},_catch_fire=True)
    async def get_async(self, time):
        if not str(time).isnumeric(): 
            return {'status' : 'is not a valid integer'}

        await asyncio.sleep(int(time))
        return {'status' : 'Ok', 'after' : '{}s'.format(int(time))}

if __name__ == '__main__':
    try:
        print("Start the service")
        app = pyrestful.rest.RestService([AsyncService])
        http_server = tornado.httpserver.HTTPServer(app)
        http_server.listen(8080)
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        print("\nStop the service")
