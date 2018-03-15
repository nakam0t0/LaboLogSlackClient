# -*- coding: utf-8 -*-

import requests, re
from slackbot.bot import listen_to, respond_to

@listen_to('今(.*)')
def getIndex(message, something):
    param = "{}".format(something)
    if re.match(".*[誰人].*", param):
        msg = ''

        # 日付のセット
        if re.match("^日", param):
            query = 'today'
            msg = '今日研究室にいた人は\n'
        else:
            query = 'now'
            msg = '今研究室にいる人は\n'

        url = 'http://serene-tundra-42600.herokuapp.com/search?query=' + query
        headers = {"content-type": "application/json"}
        r = requests.get(url, headers=headers)
        data = r.json()
        if data:
            for i in data:
                msg = msg + i + 'さん\n' 
        else:
            msg = msg + 'いない'

        message.send(msg)
    else:
        message.send('ねむい')
