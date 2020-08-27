# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import time
import datetime
import json
import calendar

from Tea.exceptions import TeaException
from Tea.request import TeaRequest
from Tea.core import TeaCore


class Client(object):
    def __init__(self, config):
        self._endpoint = config.endpoint
        self._domain_id = config.domain_id
        self._client_id = config.client_id
        self._refresh_token = config.refresh_token
        self._client_secret = config.client_secret
        self._access_token = config.access_token
        self._expire_time = config.expire_time

    def set_expire_time(self, expire_time):
        self._expire_time = expire_time

    def get_expire_time(self):
        return self._expire_time

    def get_refresh_token(self):
        return self._refresh_token

    def set_refresh_token(self, refresh_token):
        self._refresh_token = refresh_token

    def set_access_token(self, access_token):
        self._access_token = access_token

    def get_access_token(self):
        if self._access_token is None:
            raise TeaException('access token is None')

        if self.should_refresh():
            self.refresh_access_token()

        return self._access_token

    def should_refresh(self):
        if not self._expire_time or not self._refresh_token:
            return False
        expire_time_str = self._expire_time.replace('T', ' ').replace('Z', '')
        time_array = time.strptime(expire_time_str, "%Y-%m-%d %H:%M:%S")
        time_stamp = calendar.timegm(time_array)
        return int(time.mktime(time.localtime())) >= (time_stamp - 180)

    def refresh_access_token(self):
        tea_request = TeaRequest()
        tea_request.method = "POST"
        tea_request.pathname = "/v2/oauth/token"
        headers = {
            "host": self._endpoint if self._endpoint else self._domain_id + ".api.aliyunpds.com",
            "content-type": "application/x-www-form-urlencoded; charset=utf-8",
            "date": datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT'),
            "accept": "application/json",
            "x-acs-signature-method": "HMAC-SHA1",
            "x-acs-signature-version": "1.0"
        }
        tea_request.headers = headers
        body_str = "grant_type=refresh_token&refresh_token={0}&client_id={1}&client_secret={2}".format(
            self._refresh_token, self._client_id, self._client_secret)
        tea_request.body = bytes(body_str, encoding="utf-8")
        response = TeaCore.do_action(tea_request)
        dic = json.loads(str(response.body, encoding="utf-8"))
        if response.status_code == 200:
            self._expire_time = dic.get("expire_time")
            self._access_token = dic.get("access_token")
            self._refresh_token = dic.get("refresh_token")
        else:
            raise TeaException(dic)
