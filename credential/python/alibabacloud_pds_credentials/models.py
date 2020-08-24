# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class Config(TeaModel):
    def __init__(self, endpoint=None, domain_id=None, client_id=None, refresh_token=None, client_secret=None,
                 access_token=None, expire_time=None):
        self.endpoint = endpoint  # type: str
        self.domain_id = domain_id  # type: str
        self.client_id = client_id  # type: str
        self.refresh_token = refresh_token  # type: str
        self.client_secret = client_secret  # type: str
        self.access_token = access_token  # type: str
        self.expire_time = expire_time  # type: str

    def validate(self):
        self.validate_required(self.domain_id, 'domain_id')

    def to_map(self):
        result = {}
        result['endpoint'] = self.endpoint
        result['domainId'] = self.domain_id
        result['clientId'] = self.client_id
        result['refreshToken'] = self.refresh_token
        result['clientSecret'] = self.client_secret
        result['accessToken'] = self.access_token
        result['expireTime'] = self.expire_time
        return result

    def from_map(self, map={}):
        self.endpoint = map.get('endpoint')
        self.domain_id = map.get('domainId')
        self.client_id = map.get('clientId')
        self.refresh_token = map.get('refreshToken')
        self.client_secret = map.get('clientSecret')
        self.access_token = map.get('accessToken')
        self.expire_time = map.get('expireTime')
        return self
