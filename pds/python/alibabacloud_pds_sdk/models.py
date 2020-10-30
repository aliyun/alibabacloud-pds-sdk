# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
try:
    from typing import Dict, List
except ImportError:
    pass


class RuntimeOptions(TeaModel):
    def __init__(self, autoretry=None, ignore_ssl=None, max_attempts=None, backoff_policy=None, backoff_period=None,
                 read_timeout=None, connect_timeout=None, http_proxy=None, https_proxy=None, no_proxy=None, max_idle_conns=None,
                 local_addr=None, socks_5proxy=None, socks_5net_work=None):
        # whether to try again
        self.autoretry = autoretry      # type: bool
        # ignore SSL validation
        self.ignore_ssl = ignore_ssl    # type: bool
        # maximum number of retries
        self.max_attempts = max_attempts  # type: int
        # backoff policy
        self.backoff_policy = backoff_policy  # type: str
        # backoff period
        self.backoff_period = backoff_period  # type: int
        # read timeout
        self.read_timeout = read_timeout  # type: int
        # connect timeout
        self.connect_timeout = connect_timeout  # type: int
        # http proxy url
        self.http_proxy = http_proxy    # type: str
        # https Proxy url
        self.https_proxy = https_proxy  # type: str
        # agent blacklist
        self.no_proxy = no_proxy        # type: str
        # maximum number of connections
        self.max_idle_conns = max_idle_conns  # type: int
        # local addr
        self.local_addr = local_addr    # type: str
        # SOCKS5 proxy
        self.socks_5proxy = socks_5proxy  # type: str
        # SOCKS5 netWork
        self.socks_5net_work = socks_5net_work  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.autoretry is not None:
            result['autoretry'] = self.autoretry
        if self.ignore_ssl is not None:
            result['ignoreSSL'] = self.ignore_ssl
        if self.max_attempts is not None:
            result['maxAttempts'] = self.max_attempts
        if self.backoff_policy is not None:
            result['backoffPolicy'] = self.backoff_policy
        if self.backoff_period is not None:
            result['backoffPeriod'] = self.backoff_period
        if self.read_timeout is not None:
            result['readTimeout'] = self.read_timeout
        if self.connect_timeout is not None:
            result['connectTimeout'] = self.connect_timeout
        if self.http_proxy is not None:
            result['httpProxy'] = self.http_proxy
        if self.https_proxy is not None:
            result['httpsProxy'] = self.https_proxy
        if self.no_proxy is not None:
            result['noProxy'] = self.no_proxy
        if self.max_idle_conns is not None:
            result['maxIdleConns'] = self.max_idle_conns
        if self.local_addr is not None:
            result['localAddr'] = self.local_addr
        if self.socks_5proxy is not None:
            result['socks5Proxy'] = self.socks_5proxy
        if self.socks_5net_work is not None:
            result['socks5NetWork'] = self.socks_5net_work
        return result

    def from_map(self, map={}):
        if map.get('autoretry') is not None:
            self.autoretry = map.get('autoretry')
        if map.get('ignoreSSL') is not None:
            self.ignore_ssl = map.get('ignoreSSL')
        if map.get('maxAttempts') is not None:
            self.max_attempts = map.get('maxAttempts')
        if map.get('backoffPolicy') is not None:
            self.backoff_policy = map.get('backoffPolicy')
        if map.get('backoffPeriod') is not None:
            self.backoff_period = map.get('backoffPeriod')
        if map.get('readTimeout') is not None:
            self.read_timeout = map.get('readTimeout')
        if map.get('connectTimeout') is not None:
            self.connect_timeout = map.get('connectTimeout')
        if map.get('httpProxy') is not None:
            self.http_proxy = map.get('httpProxy')
        if map.get('httpsProxy') is not None:
            self.https_proxy = map.get('httpsProxy')
        if map.get('noProxy') is not None:
            self.no_proxy = map.get('noProxy')
        if map.get('maxIdleConns') is not None:
            self.max_idle_conns = map.get('maxIdleConns')
        if map.get('localAddr') is not None:
            self.local_addr = map.get('localAddr')
        if map.get('socks5Proxy') is not None:
            self.socks_5proxy = map.get('socks5Proxy')
        if map.get('socks5NetWork') is not None:
            self.socks_5net_work = map.get('socks5NetWork')
        return self


class Config(TeaModel):
    def __init__(self, endpoint=None, domain_id=None, client_id=None, refresh_token=None, client_secret=None,
                 access_token=None, expire_time=None, protocol=None, type=None, security_token=None, access_key_id=None,
                 access_key_secret=None, nickname=None, user_agent=None):
        self.endpoint = endpoint        # type: str
        self.domain_id = domain_id      # type: str
        self.client_id = client_id      # type: str
        self.refresh_token = refresh_token  # type: str
        self.client_secret = client_secret  # type: str
        self.access_token = access_token  # type: str
        self.expire_time = expire_time  # type: str
        self.protocol = protocol        # type: str
        self.type = type                # type: str
        self.security_token = security_token  # type: str
        self.access_key_id = access_key_id  # type: str
        self.access_key_secret = access_key_secret  # type: str
        self.nickname = nickname        # type: str
        self.user_agent = user_agent    # type: str

    def validate(self):
        if self.domain_id is not None:
            self.validate_pattern(self.domain_id, 'domain_id', '^[a-zA-Z0-9_-]+$')

    def to_map(self):
        result = {}
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.domain_id is not None:
            result['domainId'] = self.domain_id
        if self.client_id is not None:
            result['clientId'] = self.client_id
        if self.refresh_token is not None:
            result['refreshToken'] = self.refresh_token
        if self.client_secret is not None:
            result['clientSecret'] = self.client_secret
        if self.access_token is not None:
            result['accessToken'] = self.access_token
        if self.expire_time is not None:
            result['expireTime'] = self.expire_time
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.type is not None:
            result['type'] = self.type
        if self.security_token is not None:
            result['securityToken'] = self.security_token
        if self.access_key_id is not None:
            result['accessKeyId'] = self.access_key_id
        if self.access_key_secret is not None:
            result['accessKeySecret'] = self.access_key_secret
        if self.nickname is not None:
            result['nickname'] = self.nickname
        if self.user_agent is not None:
            result['userAgent'] = self.user_agent
        return result

    def from_map(self, map={}):
        if map.get('endpoint') is not None:
            self.endpoint = map.get('endpoint')
        if map.get('domainId') is not None:
            self.domain_id = map.get('domainId')
        if map.get('clientId') is not None:
            self.client_id = map.get('clientId')
        if map.get('refreshToken') is not None:
            self.refresh_token = map.get('refreshToken')
        if map.get('clientSecret') is not None:
            self.client_secret = map.get('clientSecret')
        if map.get('accessToken') is not None:
            self.access_token = map.get('accessToken')
        if map.get('expireTime') is not None:
            self.expire_time = map.get('expireTime')
        if map.get('protocol') is not None:
            self.protocol = map.get('protocol')
        if map.get('type') is not None:
            self.type = map.get('type')
        if map.get('securityToken') is not None:
            self.security_token = map.get('securityToken')
        if map.get('accessKeyId') is not None:
            self.access_key_id = map.get('accessKeyId')
        if map.get('accessKeySecret') is not None:
            self.access_key_secret = map.get('accessKeySecret')
        if map.get('nickname') is not None:
            self.nickname = map.get('nickname')
        if map.get('userAgent') is not None:
            self.user_agent = map.get('userAgent')
        return self


class CancelLinkModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: AccountAccessTokenResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = AccountAccessTokenResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class ConfirmLinkModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: AccountAccessTokenResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = AccountAccessTokenResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class ChangePasswordModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: AccountAccessTokenResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = AccountAccessTokenResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class SetPasswordModel(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        return self


class VerifyCodeModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: VerifyCodeResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = VerifyCodeResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class GetAccessTokenByLinkInfoModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: AccountAccessTokenResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = AccountAccessTokenResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class GetCaptchaModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: Captcha

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = Captcha()
            self.body = temp_model.from_map(map['body'])
        return self


class GetLinkInfoModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: LinkInfoResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = LinkInfoResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class GetLinkInfoByUserIdModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: LinkInfoListResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = LinkInfoListResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class GetPublicKeyModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: GetAppPublicKeyResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetAppPublicKeyResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class LinkModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: AccountAccessTokenResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = AccountAccessTokenResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class CheckExistModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: MobileCheckExistResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = MobileCheckExistResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class LoginModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: AccountAccessTokenResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = AccountAccessTokenResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class RegisterModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: AccountAccessTokenResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = AccountAccessTokenResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class MobileSendSmsCodeModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: MobileSendSmsCodeResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = MobileSendSmsCodeResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class AccountRevokeModel(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        return self


class AccountTokenModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: AccountAccessTokenResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = AccountAccessTokenResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class AccessTokenResponse(TeaModel):
    """
    *
    """
    def __init__(self, access_token=None, default_drive_id=None, expire_time=None, expires_in=None,
                 refresh_token=None, role=None, token_type=None, user_id=None):
        # 用于调用业务接口的accessToken
        self.access_token = access_token  # type: str
        # Default Drive ID
        self.default_drive_id = default_drive_id  # type: str
        # accessToken过期时间，ISO时间
        self.expire_time = expire_time  # type: str
        # accessToken过期时间，单位秒
        self.expires_in = expires_in    # type: int
        # 用于刷新accessToken
        self.refresh_token = refresh_token  # type: str
        # 当前用户角色
        self.role = role                # type: str
        # accessToken类型，Bearer
        self.token_type = token_type    # type: str
        # 当前用户ID
        self.user_id = user_id          # type: str

    def validate(self):
        self.validate_required(self.access_token, 'access_token')
        self.validate_required(self.default_drive_id, 'default_drive_id')
        self.validate_required(self.expire_time, 'expire_time')
        self.validate_required(self.expires_in, 'expires_in')
        self.validate_required(self.refresh_token, 'refresh_token')
        self.validate_required(self.role, 'role')
        self.validate_required(self.token_type, 'token_type')
        self.validate_required(self.user_id, 'user_id')

    def to_map(self):
        result = {}
        if self.access_token is not None:
            result['access_token'] = self.access_token
        if self.default_drive_id is not None:
            result['default_drive_id'] = self.default_drive_id
        if self.expire_time is not None:
            result['expire_time'] = self.expire_time
        if self.expires_in is not None:
            result['expires_in'] = self.expires_in
        if self.refresh_token is not None:
            result['refresh_token'] = self.refresh_token
        if self.role is not None:
            result['role'] = self.role
        if self.token_type is not None:
            result['token_type'] = self.token_type
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, map={}):
        if map.get('access_token') is not None:
            self.access_token = map.get('access_token')
        if map.get('default_drive_id') is not None:
            self.default_drive_id = map.get('default_drive_id')
        if map.get('expire_time') is not None:
            self.expire_time = map.get('expire_time')
        if map.get('expires_in') is not None:
            self.expires_in = map.get('expires_in')
        if map.get('refresh_token') is not None:
            self.refresh_token = map.get('refresh_token')
        if map.get('role') is not None:
            self.role = map.get('role')
        if map.get('token_type') is not None:
            self.token_type = map.get('token_type')
        if map.get('user_id') is not None:
            self.user_id = map.get('user_id')
        return self


class AccountAccessTokenResponse(TeaModel):
    """
    *
    """
    def __init__(self, access_token=None, avatar=None, data_pin_saved=None, data_pin_setup=None,
                 default_drive_id=None, exist_link=None, expire_time=None, expires_in=None, is_first_login=None, need_link=None,
                 nick_name=None, refresh_token=None, role=None, state=None, token_type=None, user_data=None, user_id=None,
                 user_name=None):
        # 用于调用业务接口的accessToken
        self.access_token = access_token  # type: str
        # 当前用户头像
        self.avatar = avatar            # type: str
        # 用户的数据密码是否保存服务端
        self.data_pin_saved = data_pin_saved  # type: bool
        # 用户的数据密码是否设置过
        self.data_pin_setup = data_pin_setup  # type: bool
        # Default Drive ID
        self.default_drive_id = default_drive_id  # type: str
        # 当前用户已存在的登录方式
        self.exist_link = exist_link    # type: List[LinkInfo]
        # accessToken过期时间，ISO时间
        self.expire_time = expire_time  # type: str
        # accessToken过期时间，单位秒
        self.expires_in = expires_in    # type: int
        # 用户是否为第一次登录
        self.is_first_login = is_first_login  # type: bool
        # 是否需要绑定
        self.need_link = need_link      # type: bool
        # 当前用户昵称
        self.nick_name = nick_name      # type: str
        # 用于刷新accessToken
        self.refresh_token = refresh_token  # type: str
        # 当前用户角色
        self.role = role                # type: str
        # 临时权限，用于登录成功后设置密码
        self.state = state              # type: str
        # accessToken类型，Bearer
        self.token_type = token_type    # type: str
        # 用户自定义数据，格式为json，可用于配置项、少量临时数据等存储，不超过1K
        self.user_data = user_data      # type: dict
        # 当前用户ID
        self.user_id = user_id          # type: str
        # 当前用户名
        self.user_name = user_name      # type: str

    def validate(self):
        self.validate_required(self.access_token, 'access_token')
        if self.exist_link:
            for k in self.exist_link:
                if k:
                    k.validate()
        self.validate_required(self.need_link, 'need_link')

    def to_map(self):
        result = {}
        if self.access_token is not None:
            result['access_token'] = self.access_token
        if self.avatar is not None:
            result['avatar'] = self.avatar
        if self.data_pin_saved is not None:
            result['data_pin_saved'] = self.data_pin_saved
        if self.data_pin_setup is not None:
            result['data_pin_setup'] = self.data_pin_setup
        if self.default_drive_id is not None:
            result['default_drive_id'] = self.default_drive_id
        result['exist_link'] = []
        if self.exist_link is not None:
            for k in self.exist_link:
                result['exist_link'].append(k.to_map() if k else None)
        if self.expire_time is not None:
            result['expire_time'] = self.expire_time
        if self.expires_in is not None:
            result['expires_in'] = self.expires_in
        if self.is_first_login is not None:
            result['is_first_login'] = self.is_first_login
        if self.need_link is not None:
            result['need_link'] = self.need_link
        if self.nick_name is not None:
            result['nick_name'] = self.nick_name
        if self.refresh_token is not None:
            result['refresh_token'] = self.refresh_token
        if self.role is not None:
            result['role'] = self.role
        if self.state is not None:
            result['state'] = self.state
        if self.token_type is not None:
            result['token_type'] = self.token_type
        if self.user_data is not None:
            result['user_data'] = self.user_data
        if self.user_id is not None:
            result['user_id'] = self.user_id
        if self.user_name is not None:
            result['user_name'] = self.user_name
        return result

    def from_map(self, map={}):
        if map.get('access_token') is not None:
            self.access_token = map.get('access_token')
        if map.get('avatar') is not None:
            self.avatar = map.get('avatar')
        if map.get('data_pin_saved') is not None:
            self.data_pin_saved = map.get('data_pin_saved')
        if map.get('data_pin_setup') is not None:
            self.data_pin_setup = map.get('data_pin_setup')
        if map.get('default_drive_id') is not None:
            self.default_drive_id = map.get('default_drive_id')
        self.exist_link = []
        if map.get('exist_link') is not None:
            for k in map.get('exist_link'):
                temp_model = LinkInfo()
                self.exist_link.append(temp_model.from_map(k))
        if map.get('expire_time') is not None:
            self.expire_time = map.get('expire_time')
        if map.get('expires_in') is not None:
            self.expires_in = map.get('expires_in')
        if map.get('is_first_login') is not None:
            self.is_first_login = map.get('is_first_login')
        if map.get('need_link') is not None:
            self.need_link = map.get('need_link')
        if map.get('nick_name') is not None:
            self.nick_name = map.get('nick_name')
        if map.get('refresh_token') is not None:
            self.refresh_token = map.get('refresh_token')
        if map.get('role') is not None:
            self.role = map.get('role')
        if map.get('state') is not None:
            self.state = map.get('state')
        if map.get('token_type') is not None:
            self.token_type = map.get('token_type')
        if map.get('user_data') is not None:
            self.user_data = map.get('user_data')
        if map.get('user_id') is not None:
            self.user_id = map.get('user_id')
        if map.get('user_name') is not None:
            self.user_name = map.get('user_name')
        return self


class AccountLinkRequest(TeaModel):
    """
    *
    """
    def __init__(self, headers=None, detail=None, extra=None, identity=None, status=None, type=None, user_id=None):
        self.headers = headers          # type: Dict[str, str]
        # 账号信息
        self.detail = detail            # type: str
        # 额外的信息，比如type为mobile时，此字段为国家编号，不填默认86
        self.extra = extra              # type: str
        # 唯一身份标识
        self.identity = identity        # type: str
        # 状态
        self.status = status            # type: str
        # 认证类型
        self.type = type                # type: str
        # 绑定的user_id
        self.user_id = user_id          # type: str

    def validate(self):
        self.validate_required(self.identity, 'identity')
        self.validate_required(self.type, 'type')
        self.validate_required(self.user_id, 'user_id')

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.detail is not None:
            result['detail'] = self.detail
        if self.extra is not None:
            result['extra'] = self.extra
        if self.identity is not None:
            result['identity'] = self.identity
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('detail') is not None:
            self.detail = map.get('detail')
        if map.get('extra') is not None:
            self.extra = map.get('extra')
        if map.get('identity') is not None:
            self.identity = map.get('identity')
        if map.get('status') is not None:
            self.status = map.get('status')
        if map.get('type') is not None:
            self.type = map.get('type')
        if map.get('user_id') is not None:
            self.user_id = map.get('user_id')
        return self


class AuthorizeRequest(TeaModel):
    """
    *
    """
    def __init__(self, client_id=None, login_type=None, redirect_uri=None, response_type=None, scope=None,
                 state=None):
        # Client ID, 此处填写创建App时返回的AppID
        self.client_id = client_id      # type: str
        # 鉴权方式，目前支持ding,ram鉴权
        self.login_type = login_type    # type: str
        # 回调地址, 此处填写创建App时填写的回调地址
        self.redirect_uri = redirect_uri  # type: str
        # 返回类型, 只能填写code
        self.response_type = response_type  # type: str
        # 申请的权限列表, 默认为所有权限
        self.scope = scope              # type: List[str]
        # 用户自定义字段，会在鉴权成功后的callback带回
        self.state = state              # type: str

    def validate(self):
        self.validate_required(self.client_id, 'client_id')
        self.validate_required(self.redirect_uri, 'redirect_uri')
        self.validate_required(self.response_type, 'response_type')

    def to_map(self):
        result = {}
        if self.client_id is not None:
            result['ClientID'] = self.client_id
        if self.login_type is not None:
            result['LoginType'] = self.login_type
        if self.redirect_uri is not None:
            result['RedirectUri'] = self.redirect_uri
        if self.response_type is not None:
            result['ResponseType'] = self.response_type
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, map={}):
        if map.get('ClientID') is not None:
            self.client_id = map.get('ClientID')
        if map.get('LoginType') is not None:
            self.login_type = map.get('LoginType')
        if map.get('RedirectUri') is not None:
            self.redirect_uri = map.get('RedirectUri')
        if map.get('ResponseType') is not None:
            self.response_type = map.get('ResponseType')
        if map.get('Scope') is not None:
            self.scope = map.get('Scope')
        if map.get('State') is not None:
            self.state = map.get('State')
        return self


class BaseDriveResponse(TeaModel):
    """
    Base drive response
    """
    def __init__(self, creator=None, description=None, domain_id=None, drive_id=None, drive_name=None,
                 drive_type=None, encrypt_data_access=None, encrypt_mode=None, owner=None, relative_path=None, status=None,
                 store_id=None, total_size=None, used_size=None):
        # Drive 创建者
        self.creator = creator          # type: str
        # Drive 备注信息
        self.description = description  # type: str
        # Domain ID
        self.domain_id = domain_id      # type: str
        # Drive ID
        self.drive_id = drive_id        # type: str
        # Drive 名称
        self.drive_name = drive_name    # type: str
        # Drive 类型
        self.drive_type = drive_type    # type: str
        self.encrypt_data_access = encrypt_data_access  # type: bool
        self.encrypt_mode = encrypt_mode  # type: str
        # Drive 所有者
        self.owner = owner              # type: str
        # Drive存储基于store的相对路径，domain的PathType为OSSPath时返回
        self.relative_path = relative_path  # type: str
        # Drive 状态
        self.status = status            # type: str
        # 存储 ID, domain的PathType为OSSPath时返回
        self.store_id = store_id        # type: str
        # Drive 空间总量
        self.total_size = total_size    # type: int
        # Drive 空间已使用量
        self.used_size = used_size      # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.creator is not None:
            result['creator'] = self.creator
        if self.description is not None:
            result['description'] = self.description
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.drive_name is not None:
            result['drive_name'] = self.drive_name
        if self.drive_type is not None:
            result['drive_type'] = self.drive_type
        if self.encrypt_data_access is not None:
            result['encrypt_data_access'] = self.encrypt_data_access
        if self.encrypt_mode is not None:
            result['encrypt_mode'] = self.encrypt_mode
        if self.owner is not None:
            result['owner'] = self.owner
        if self.relative_path is not None:
            result['relative_path'] = self.relative_path
        if self.status is not None:
            result['status'] = self.status
        if self.store_id is not None:
            result['store_id'] = self.store_id
        if self.total_size is not None:
            result['total_size'] = self.total_size
        if self.used_size is not None:
            result['used_size'] = self.used_size
        return result

    def from_map(self, map={}):
        if map.get('creator') is not None:
            self.creator = map.get('creator')
        if map.get('description') is not None:
            self.description = map.get('description')
        if map.get('domain_id') is not None:
            self.domain_id = map.get('domain_id')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('drive_name') is not None:
            self.drive_name = map.get('drive_name')
        if map.get('drive_type') is not None:
            self.drive_type = map.get('drive_type')
        if map.get('encrypt_data_access') is not None:
            self.encrypt_data_access = map.get('encrypt_data_access')
        if map.get('encrypt_mode') is not None:
            self.encrypt_mode = map.get('encrypt_mode')
        if map.get('owner') is not None:
            self.owner = map.get('owner')
        if map.get('relative_path') is not None:
            self.relative_path = map.get('relative_path')
        if map.get('status') is not None:
            self.status = map.get('status')
        if map.get('store_id') is not None:
            self.store_id = map.get('store_id')
        if map.get('total_size') is not None:
            self.total_size = map.get('total_size')
        if map.get('used_size') is not None:
            self.used_size = map.get('used_size')
        return self


class BaseFileAnonymousResponse(TeaModel):
    """
    list_file_by_anonymous base response
    """
    def __init__(self, file_id=None, name=None, size=None, thumbnail=None, type=None, updated_at=None):
        # file_id
        self.file_id = file_id          # type: str
        # name
        self.name = name                # type: str
        # size, type=file时才有效
        self.size = size                # type: int
        # thumbnail
        self.thumbnail = thumbnail      # type: str
        # type
        self.type = type                # type: str
        # updated_at
        self.updated_at = updated_at    # type: str

    def validate(self):
        if self.file_id is not None:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9]{1,50}')
        if self.name is not None:
            self.validate_pattern(self.name, 'name', '[a-zA-Z0-9.-]{1,1000}')
        if self.size is not None:
            self.validate_maximum(self.size, 'size', 53687091200)
            self.validate_minimum(self.size, 'size', 0)

    def to_map(self):
        result = {}
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.name is not None:
            result['name'] = self.name
        if self.size is not None:
            result['size'] = self.size
        if self.thumbnail is not None:
            result['thumbnail'] = self.thumbnail
        if self.type is not None:
            result['type'] = self.type
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        return result

    def from_map(self, map={}):
        if map.get('file_id') is not None:
            self.file_id = map.get('file_id')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('size') is not None:
            self.size = map.get('size')
        if map.get('thumbnail') is not None:
            self.thumbnail = map.get('thumbnail')
        if map.get('type') is not None:
            self.type = map.get('type')
        if map.get('updated_at') is not None:
            self.updated_at = map.get('updated_at')
        return self


class BaseFileResponse(TeaModel):
    """
    Base file response
    """
    def __init__(self, category=None, content_hash=None, content_hash_name=None, content_type=None, crc_64hash=None,
                 created_at=None, description=None, domain_id=None, download_url=None, drive_id=None, encrypt_mode=None,
                 file_extension=None, file_id=None, hidden=None, image_media_metadata=None, labels=None, meta=None, name=None,
                 parent_file_id=None, punish_flag=None, size=None, starred=None, status=None, streams_info=None, thumbnail=None,
                 trashed_at=None, type=None, updated_at=None, upload_id=None, url=None, user_meta=None,
                 video_media_metadata=None, video_preview_metadata=None):
        # category
        self.category = category        # type: str
        # Content Hash
        self.content_hash = content_hash  # type: str
        # content_hash_name
        self.content_hash_name = content_hash_name  # type: str
        # content_type
        self.content_type = content_type  # type: str
        # crc64_hash
        self.crc_64hash = crc_64hash    # type: str
        # created_at
        self.created_at = created_at    # type: str
        # description
        self.description = description  # type: str
        # DomainID
        self.domain_id = domain_id      # type: str
        # download_url
        self.download_url = download_url  # type: str
        # drive_id
        self.drive_id = drive_id        # type: str
        # encrypt_mode
        self.encrypt_mode = encrypt_mode  # type: str
        # file_extension
        self.file_extension = file_extension  # type: str
        # file_id
        self.file_id = file_id          # type: str
        # Hidden
        # type: boolean
        self.hidden = hidden            # type: bool
        self.image_media_metadata = image_media_metadata  # type: ImageMediaResponse
        # labels
        self.labels = labels            # type: List[str]
        self.meta = meta                # type: str
        # name
        self.name = name                # type: str
        # parent_file_id
        self.parent_file_id = parent_file_id  # type: str
        self.punish_flag = punish_flag  # type: int
        # Size
        self.size = size                # type: int
        # starred
        # type: boolean
        self.starred = starred          # type: bool
        # status
        self.status = status            # type: str
        # @Deprecated streams url info
        self.streams_info = streams_info  # type: dict
        # thumbnail
        self.thumbnail = thumbnail      # type: str
        # trashed_at
        self.trashed_at = trashed_at    # type: str
        # type
        self.type = type                # type: str
        # updated_at
        self.updated_at = updated_at    # type: str
        # upload_id
        self.upload_id = upload_id      # type: str
        # url
        self.url = url                  # type: str
        # user_meta
        self.user_meta = user_meta      # type: str
        self.video_media_metadata = video_media_metadata  # type: VideoMediaResponse
        self.video_preview_metadata = video_preview_metadata  # type: VideoPreviewResponse

    def validate(self):
        if self.domain_id is not None:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z]+')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.file_id is not None:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9]{1,50}')
        if self.image_media_metadata:
            self.image_media_metadata.validate()
        self.validate_required(self.name, 'name')
        if self.name is not None:
            self.validate_pattern(self.name, 'name', '[a-zA-Z0-9.-]{1,1000}')
        if self.parent_file_id is not None:
            self.validate_max_length(self.parent_file_id, 'parent_file_id', 50)
            self.validate_pattern(self.parent_file_id, 'parent_file_id', '[a-z0-9]{1,50}')
        if self.size is not None:
            self.validate_maximum(self.size, 'size', 53687091200)
            self.validate_minimum(self.size, 'size', 0)
        if self.video_media_metadata:
            self.video_media_metadata.validate()
        if self.video_preview_metadata:
            self.video_preview_metadata.validate()

    def to_map(self):
        result = {}
        if self.category is not None:
            result['category'] = self.category
        if self.content_hash is not None:
            result['content_hash'] = self.content_hash
        if self.content_hash_name is not None:
            result['content_hash_name'] = self.content_hash_name
        if self.content_type is not None:
            result['content_type'] = self.content_type
        if self.crc_64hash is not None:
            result['crc64_hash'] = self.crc_64hash
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.download_url is not None:
            result['download_url'] = self.download_url
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.encrypt_mode is not None:
            result['encrypt_mode'] = self.encrypt_mode
        if self.file_extension is not None:
            result['file_extension'] = self.file_extension
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.hidden is not None:
            result['hidden'] = self.hidden
        if self.image_media_metadata is not None:
            result['image_media_metadata'] = self.image_media_metadata.to_map()
        if self.labels is not None:
            result['labels'] = self.labels
        if self.meta is not None:
            result['meta'] = self.meta
        if self.name is not None:
            result['name'] = self.name
        if self.parent_file_id is not None:
            result['parent_file_id'] = self.parent_file_id
        if self.punish_flag is not None:
            result['punish_flag'] = self.punish_flag
        if self.size is not None:
            result['size'] = self.size
        if self.starred is not None:
            result['starred'] = self.starred
        if self.status is not None:
            result['status'] = self.status
        if self.streams_info is not None:
            result['streams_info'] = self.streams_info
        if self.thumbnail is not None:
            result['thumbnail'] = self.thumbnail
        if self.trashed_at is not None:
            result['trashed_at'] = self.trashed_at
        if self.type is not None:
            result['type'] = self.type
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        if self.upload_id is not None:
            result['upload_id'] = self.upload_id
        if self.url is not None:
            result['url'] = self.url
        if self.user_meta is not None:
            result['user_meta'] = self.user_meta
        if self.video_media_metadata is not None:
            result['video_media_metadata'] = self.video_media_metadata.to_map()
        if self.video_preview_metadata is not None:
            result['video_preview_metadata'] = self.video_preview_metadata.to_map()
        return result

    def from_map(self, map={}):
        if map.get('category') is not None:
            self.category = map.get('category')
        if map.get('content_hash') is not None:
            self.content_hash = map.get('content_hash')
        if map.get('content_hash_name') is not None:
            self.content_hash_name = map.get('content_hash_name')
        if map.get('content_type') is not None:
            self.content_type = map.get('content_type')
        if map.get('crc64_hash') is not None:
            self.crc_64hash = map.get('crc64_hash')
        if map.get('created_at') is not None:
            self.created_at = map.get('created_at')
        if map.get('description') is not None:
            self.description = map.get('description')
        if map.get('domain_id') is not None:
            self.domain_id = map.get('domain_id')
        if map.get('download_url') is not None:
            self.download_url = map.get('download_url')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('encrypt_mode') is not None:
            self.encrypt_mode = map.get('encrypt_mode')
        if map.get('file_extension') is not None:
            self.file_extension = map.get('file_extension')
        if map.get('file_id') is not None:
            self.file_id = map.get('file_id')
        if map.get('hidden') is not None:
            self.hidden = map.get('hidden')
        if map.get('image_media_metadata') is not None:
            temp_model = ImageMediaResponse()
            self.image_media_metadata = temp_model.from_map(map['image_media_metadata'])
        if map.get('labels') is not None:
            self.labels = map.get('labels')
        if map.get('meta') is not None:
            self.meta = map.get('meta')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('parent_file_id') is not None:
            self.parent_file_id = map.get('parent_file_id')
        if map.get('punish_flag') is not None:
            self.punish_flag = map.get('punish_flag')
        if map.get('size') is not None:
            self.size = map.get('size')
        if map.get('starred') is not None:
            self.starred = map.get('starred')
        if map.get('status') is not None:
            self.status = map.get('status')
        if map.get('streams_info') is not None:
            self.streams_info = map.get('streams_info')
        if map.get('thumbnail') is not None:
            self.thumbnail = map.get('thumbnail')
        if map.get('trashed_at') is not None:
            self.trashed_at = map.get('trashed_at')
        if map.get('type') is not None:
            self.type = map.get('type')
        if map.get('updated_at') is not None:
            self.updated_at = map.get('updated_at')
        if map.get('upload_id') is not None:
            self.upload_id = map.get('upload_id')
        if map.get('url') is not None:
            self.url = map.get('url')
        if map.get('user_meta') is not None:
            self.user_meta = map.get('user_meta')
        if map.get('video_media_metadata') is not None:
            temp_model = VideoMediaResponse()
            self.video_media_metadata = temp_model.from_map(map['video_media_metadata'])
        if map.get('video_preview_metadata') is not None:
            temp_model = VideoPreviewResponse()
            self.video_preview_metadata = temp_model.from_map(map['video_preview_metadata'])
        return self


class BaseMediaResponse(TeaModel):
    """
    *
    """
    def __init__(self, address_line=None, city=None, country=None, district=None, height=None, location=None,
                 province=None, time=None, township=None, width=None):
        # address_line
        self.address_line = address_line  # type: str
        # city
        self.city = city                # type: str
        # country
        self.country = country          # type: str
        # district
        self.district = district        # type: str
        # height
        self.height = height            # type: int
        # location
        self.location = location        # type: str
        # province
        self.province = province        # type: str
        # time
        self.time = time                # type: str
        # township
        self.township = township        # type: str
        # width
        self.width = width              # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.address_line is not None:
            result['address_line'] = self.address_line
        if self.city is not None:
            result['city'] = self.city
        if self.country is not None:
            result['country'] = self.country
        if self.district is not None:
            result['district'] = self.district
        if self.height is not None:
            result['height'] = self.height
        if self.location is not None:
            result['location'] = self.location
        if self.province is not None:
            result['province'] = self.province
        if self.time is not None:
            result['time'] = self.time
        if self.township is not None:
            result['township'] = self.township
        if self.width is not None:
            result['width'] = self.width
        return result

    def from_map(self, map={}):
        if map.get('address_line') is not None:
            self.address_line = map.get('address_line')
        if map.get('city') is not None:
            self.city = map.get('city')
        if map.get('country') is not None:
            self.country = map.get('country')
        if map.get('district') is not None:
            self.district = map.get('district')
        if map.get('height') is not None:
            self.height = map.get('height')
        if map.get('location') is not None:
            self.location = map.get('location')
        if map.get('province') is not None:
            self.province = map.get('province')
        if map.get('time') is not None:
            self.time = map.get('time')
        if map.get('township') is not None:
            self.township = map.get('township')
        if map.get('width') is not None:
            self.width = map.get('width')
        return self


class BaseOSSFileResponse(TeaModel):
    """
    Base file response
    """
    def __init__(self, content_hash=None, content_hash_name=None, content_type=None, crc_64hash=None,
                 created_at=None, description=None, domain_id=None, download_url=None, drive_id=None, file_extension=None,
                 file_path=None, name=None, parent_file_path=None, share_id=None, size=None, status=None, thumbnail=None,
                 trashed_at=None, type=None, updated_at=None, upload_id=None, url=None):
        # Content Hash
        self.content_hash = content_hash  # type: str
        # content_hash_name
        self.content_hash_name = content_hash_name  # type: str
        # content_type
        self.content_type = content_type  # type: str
        # crc64_hash
        self.crc_64hash = crc_64hash    # type: str
        # created_at
        self.created_at = created_at    # type: str
        # description
        self.description = description  # type: str
        # domain_id
        self.domain_id = domain_id      # type: str
        # download_url
        self.download_url = download_url  # type: str
        # drive_id
        self.drive_id = drive_id        # type: str
        # file_extension
        self.file_extension = file_extension  # type: str
        # file_path
        self.file_path = file_path      # type: str
        # name
        self.name = name                # type: str
        # parent_file_id
        self.parent_file_path = parent_file_path  # type: str
        # share_id
        self.share_id = share_id        # type: str
        # Size
        self.size = size                # type: int
        # status
        self.status = status            # type: str
        # thumbnail
        self.thumbnail = thumbnail      # type: str
        # trashed_at
        self.trashed_at = trashed_at    # type: str
        # type
        self.type = type                # type: str
        # updated_at
        self.updated_at = updated_at    # type: str
        # upload_id
        self.upload_id = upload_id      # type: str
        # url
        self.url = url                  # type: str

    def validate(self):
        if self.domain_id is not None:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z]+')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.name, 'name')
        if self.name is not None:
            self.validate_pattern(self.name, 'name', '[a-zA-Z0-9.-]{1,1000}')
        if self.parent_file_path is not None:
            self.validate_max_length(self.parent_file_path, 'parent_file_path', 50)
            self.validate_pattern(self.parent_file_path, 'parent_file_path', '[a-z0-9]{1,50}')
        if self.share_id is not None:
            self.validate_pattern(self.share_id, 'share_id', '[0-9]+')
        if self.size is not None:
            self.validate_maximum(self.size, 'size', 53687091200)
            self.validate_minimum(self.size, 'size', 0)

    def to_map(self):
        result = {}
        if self.content_hash is not None:
            result['content_hash'] = self.content_hash
        if self.content_hash_name is not None:
            result['content_hash_name'] = self.content_hash_name
        if self.content_type is not None:
            result['content_type'] = self.content_type
        if self.crc_64hash is not None:
            result['crc64_hash'] = self.crc_64hash
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.download_url is not None:
            result['download_url'] = self.download_url
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_extension is not None:
            result['file_extension'] = self.file_extension
        if self.file_path is not None:
            result['file_path'] = self.file_path
        if self.name is not None:
            result['name'] = self.name
        if self.parent_file_path is not None:
            result['parent_file_path'] = self.parent_file_path
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.size is not None:
            result['size'] = self.size
        if self.status is not None:
            result['status'] = self.status
        if self.thumbnail is not None:
            result['thumbnail'] = self.thumbnail
        if self.trashed_at is not None:
            result['trashed_at'] = self.trashed_at
        if self.type is not None:
            result['type'] = self.type
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        if self.upload_id is not None:
            result['upload_id'] = self.upload_id
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, map={}):
        if map.get('content_hash') is not None:
            self.content_hash = map.get('content_hash')
        if map.get('content_hash_name') is not None:
            self.content_hash_name = map.get('content_hash_name')
        if map.get('content_type') is not None:
            self.content_type = map.get('content_type')
        if map.get('crc64_hash') is not None:
            self.crc_64hash = map.get('crc64_hash')
        if map.get('created_at') is not None:
            self.created_at = map.get('created_at')
        if map.get('description') is not None:
            self.description = map.get('description')
        if map.get('domain_id') is not None:
            self.domain_id = map.get('domain_id')
        if map.get('download_url') is not None:
            self.download_url = map.get('download_url')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('file_extension') is not None:
            self.file_extension = map.get('file_extension')
        if map.get('file_path') is not None:
            self.file_path = map.get('file_path')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('parent_file_path') is not None:
            self.parent_file_path = map.get('parent_file_path')
        if map.get('share_id') is not None:
            self.share_id = map.get('share_id')
        if map.get('size') is not None:
            self.size = map.get('size')
        if map.get('status') is not None:
            self.status = map.get('status')
        if map.get('thumbnail') is not None:
            self.thumbnail = map.get('thumbnail')
        if map.get('trashed_at') is not None:
            self.trashed_at = map.get('trashed_at')
        if map.get('type') is not None:
            self.type = map.get('type')
        if map.get('updated_at') is not None:
            self.updated_at = map.get('updated_at')
        if map.get('upload_id') is not None:
            self.upload_id = map.get('upload_id')
        if map.get('url') is not None:
            self.url = map.get('url')
        return self


class BaseShareLinkResponse(TeaModel):
    """
    list_share_link response
    """
    def __init__(self, created_at=None, download_count=None, drive_id=None, expiration=None, expired=None,
                 file_id=None, preview_count=None, save_count=None, share_id=None, share_msg=None, share_policy=None,
                 share_pwd=None, share_url=None, updated_at=None):
        # created_at
        self.created_at = created_at    # type: str
        # 下载次数
        self.download_count = download_count  # type: int
        # drive_id
        self.drive_id = drive_id        # type: str
        # expiration
        self.expiration = expiration    # type: str
        # expired
        self.expired = expired          # type: bool
        # file_id
        self.file_id = file_id          # type: str
        # preview_count
        self.preview_count = preview_count  # type: int
        # 转存次数
        self.save_count = save_count    # type: int
        # share_id
        self.share_id = share_id        # type: str
        # share_msg
        self.share_msg = share_msg      # type: str
        # share_policy
        self.share_policy = share_policy  # type: str
        # share_pwd
        self.share_pwd = share_pwd      # type: str
        # share_url
        self.share_url = share_url      # type: str
        # updated_at
        self.updated_at = updated_at    # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.download_count is not None:
            result['download_count'] = self.download_count
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.expiration is not None:
            result['expiration'] = self.expiration
        if self.expired is not None:
            result['expired'] = self.expired
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.preview_count is not None:
            result['preview_count'] = self.preview_count
        if self.save_count is not None:
            result['save_count'] = self.save_count
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.share_msg is not None:
            result['share_msg'] = self.share_msg
        if self.share_policy is not None:
            result['share_policy'] = self.share_policy
        if self.share_pwd is not None:
            result['share_pwd'] = self.share_pwd
        if self.share_url is not None:
            result['share_url'] = self.share_url
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        return result

    def from_map(self, map={}):
        if map.get('created_at') is not None:
            self.created_at = map.get('created_at')
        if map.get('download_count') is not None:
            self.download_count = map.get('download_count')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('expiration') is not None:
            self.expiration = map.get('expiration')
        if map.get('expired') is not None:
            self.expired = map.get('expired')
        if map.get('file_id') is not None:
            self.file_id = map.get('file_id')
        if map.get('preview_count') is not None:
            self.preview_count = map.get('preview_count')
        if map.get('save_count') is not None:
            self.save_count = map.get('save_count')
        if map.get('share_id') is not None:
            self.share_id = map.get('share_id')
        if map.get('share_msg') is not None:
            self.share_msg = map.get('share_msg')
        if map.get('share_policy') is not None:
            self.share_policy = map.get('share_policy')
        if map.get('share_pwd') is not None:
            self.share_pwd = map.get('share_pwd')
        if map.get('share_url') is not None:
            self.share_url = map.get('share_url')
        if map.get('updated_at') is not None:
            self.updated_at = map.get('updated_at')
        return self


class BaseShareResponse(TeaModel):
    """
    List share response
    """
    def __init__(self, created_at=None, creator=None, description=None, domain_id=None, drive_id=None,
                 expiration=None, expired=None, owner=None, permissions=None, share_file_path=None, share_id=None,
                 share_name=None, share_policy=None, status=None, updated_at=None):
        # created_at
        self.created_at = created_at    # type: str
        # creator
        self.creator = creator          # type: str
        # description
        self.description = description  # type: str
        # domain_id
        self.domain_id = domain_id      # type: str
        # drive_id
        self.drive_id = drive_id        # type: str
        # expiration
        self.expiration = expiration    # type: str
        # expired
        self.expired = expired          # type: bool
        # owner
        self.owner = owner              # type: str
        # permissions
        self.permissions = permissions  # type: List[str]
        # share_path
        self.share_file_path = share_file_path  # type: str
        # share_id
        self.share_id = share_id        # type: str
        # share_name
        self.share_name = share_name    # type: str
        self.share_policy = share_policy  # type: List[SharePermissionPolicy]
        # status
        self.status = status            # type: str
        # updated_at
        self.updated_at = updated_at    # type: str

    def validate(self):
        if self.share_policy:
            for k in self.share_policy:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.creator is not None:
            result['creator'] = self.creator
        if self.description is not None:
            result['description'] = self.description
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.expiration is not None:
            result['expiration'] = self.expiration
        if self.expired is not None:
            result['expired'] = self.expired
        if self.owner is not None:
            result['owner'] = self.owner
        if self.permissions is not None:
            result['permissions'] = self.permissions
        if self.share_file_path is not None:
            result['share_file_path'] = self.share_file_path
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.share_name is not None:
            result['share_name'] = self.share_name
        result['share_policy'] = []
        if self.share_policy is not None:
            for k in self.share_policy:
                result['share_policy'].append(k.to_map() if k else None)
        if self.status is not None:
            result['status'] = self.status
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        return result

    def from_map(self, map={}):
        if map.get('created_at') is not None:
            self.created_at = map.get('created_at')
        if map.get('creator') is not None:
            self.creator = map.get('creator')
        if map.get('description') is not None:
            self.description = map.get('description')
        if map.get('domain_id') is not None:
            self.domain_id = map.get('domain_id')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('expiration') is not None:
            self.expiration = map.get('expiration')
        if map.get('expired') is not None:
            self.expired = map.get('expired')
        if map.get('owner') is not None:
            self.owner = map.get('owner')
        if map.get('permissions') is not None:
            self.permissions = map.get('permissions')
        if map.get('share_file_path') is not None:
            self.share_file_path = map.get('share_file_path')
        if map.get('share_id') is not None:
            self.share_id = map.get('share_id')
        if map.get('share_name') is not None:
            self.share_name = map.get('share_name')
        self.share_policy = []
        if map.get('share_policy') is not None:
            for k in map.get('share_policy'):
                temp_model = SharePermissionPolicy()
                self.share_policy.append(temp_model.from_map(k))
        if map.get('status') is not None:
            self.status = map.get('status')
        if map.get('updated_at') is not None:
            self.updated_at = map.get('updated_at')
        return self


class BatchResponse(TeaModel):
    """
    batch operation response
    """
    def __init__(self, responses=None):
        # responses 返回结果合集
        self.responses = responses      # type: List[BatchSubResponse]

    def validate(self):
        if self.responses:
            for k in self.responses:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['responses'] = []
        if self.responses is not None:
            for k in self.responses:
                result['responses'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        self.responses = []
        if map.get('responses') is not None:
            for k in map.get('responses'):
                temp_model = BatchSubResponse()
                self.responses.append(temp_model.from_map(k))
        return self


class BatchSubResponse(TeaModel):
    """
    *
    """
    def __init__(self, body=None, id=None, status=None):
        # body 子请求的返回结果，可参考对于子请求文档 json 字符串
        self.body = body                # type: dict
        # id 请求带过来的id, 可以跟 request 进行关联
        self.id = id                    # type: str
        # status 子请求的返回状态码，可参考对于子请求文档
        self.status = status            # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.body is not None:
            result['body'] = self.body
        if self.id is not None:
            result['id'] = self.id
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, map={}):
        if map.get('body') is not None:
            self.body = map.get('body')
        if map.get('id') is not None:
            self.id = map.get('id')
        if map.get('status') is not None:
            self.status = map.get('status')
        return self


class CancelLinkRequest(TeaModel):
    """
    *
    """
    def __init__(self, headers=None, temporary_token=None):
        self.headers = headers          # type: Dict[str, str]
        # 待绑定的临时token，此token只能访问绑定、取消绑定接口
        self.temporary_token = temporary_token  # type: str

    def validate(self):
        self.validate_required(self.temporary_token, 'temporary_token')

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.temporary_token is not None:
            result['temporary_token'] = self.temporary_token
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('temporary_token') is not None:
            self.temporary_token = map.get('temporary_token')
        return self


class Captcha(TeaModel):
    """
    *
    """
    def __init__(self, captcha=None, captcha_format=None, captcha_id=None):
        # 图片验证码，base64格式
        self.captcha = captcha          # type: str
        # 图片格式
        self.captcha_format = captcha_format  # type: str
        # 图片验证码ID
        self.captcha_id = captcha_id    # type: str

    def validate(self):
        self.validate_required(self.captcha, 'captcha')
        self.validate_required(self.captcha_format, 'captcha_format')
        self.validate_required(self.captcha_id, 'captcha_id')

    def to_map(self):
        result = {}
        if self.captcha is not None:
            result['captcha'] = self.captcha
        if self.captcha_format is not None:
            result['captcha_format'] = self.captcha_format
        if self.captcha_id is not None:
            result['captcha_id'] = self.captcha_id
        return result

    def from_map(self, map={}):
        if map.get('captcha') is not None:
            self.captcha = map.get('captcha')
        if map.get('captcha_format') is not None:
            self.captcha_format = map.get('captcha_format')
        if map.get('captcha_id') is not None:
            self.captcha_id = map.get('captcha_id')
        return self


class CompleteFileResponse(TeaModel):
    """
    complete file response
    """
    def __init__(self, category=None, content_hash=None, content_hash_name=None, content_type=None, crc_64hash=None,
                 created_at=None, description=None, domain_id=None, download_url=None, drive_id=None, encrypt_mode=None,
                 file_extension=None, file_id=None, hidden=None, image_media_metadata=None, labels=None, meta=None, name=None,
                 parent_file_id=None, punish_flag=None, size=None, starred=None, status=None, streams_info=None, thumbnail=None,
                 trashed_at=None, type=None, updated_at=None, upload_id=None, url=None, user_meta=None,
                 video_media_metadata=None, video_preview_metadata=None):
        # category
        self.category = category        # type: str
        # Content Hash
        self.content_hash = content_hash  # type: str
        # content_hash_name
        self.content_hash_name = content_hash_name  # type: str
        # content_type
        self.content_type = content_type  # type: str
        # crc64_hash
        self.crc_64hash = crc_64hash    # type: str
        # created_at
        self.created_at = created_at    # type: str
        # description
        self.description = description  # type: str
        # DomainID
        self.domain_id = domain_id      # type: str
        # download_url
        self.download_url = download_url  # type: str
        # drive_id
        self.drive_id = drive_id        # type: str
        # encrypt_mode
        self.encrypt_mode = encrypt_mode  # type: str
        # file_extension
        self.file_extension = file_extension  # type: str
        # file_id
        self.file_id = file_id          # type: str
        # Hidden
        # type: boolean
        self.hidden = hidden            # type: bool
        self.image_media_metadata = image_media_metadata  # type: ImageMediaResponse
        # labels
        self.labels = labels            # type: List[str]
        self.meta = meta                # type: str
        # name
        self.name = name                # type: str
        # parent_file_id
        self.parent_file_id = parent_file_id  # type: str
        self.punish_flag = punish_flag  # type: int
        # Size
        self.size = size                # type: int
        # starred
        # type: boolean
        self.starred = starred          # type: bool
        # status
        self.status = status            # type: str
        # @Deprecated streams url info
        self.streams_info = streams_info  # type: dict
        # thumbnail
        self.thumbnail = thumbnail      # type: str
        # trashed_at
        self.trashed_at = trashed_at    # type: str
        # type
        self.type = type                # type: str
        # updated_at
        self.updated_at = updated_at    # type: str
        # upload_id
        self.upload_id = upload_id      # type: str
        # url
        self.url = url                  # type: str
        # user_meta
        self.user_meta = user_meta      # type: str
        self.video_media_metadata = video_media_metadata  # type: VideoMediaResponse
        self.video_preview_metadata = video_preview_metadata  # type: VideoPreviewResponse

    def validate(self):
        if self.domain_id is not None:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z]+')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.file_id is not None:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9]{1,50}')
        if self.image_media_metadata:
            self.image_media_metadata.validate()
        self.validate_required(self.name, 'name')
        if self.name is not None:
            self.validate_pattern(self.name, 'name', '[a-zA-Z0-9.-]{1,1000}')
        if self.parent_file_id is not None:
            self.validate_max_length(self.parent_file_id, 'parent_file_id', 50)
            self.validate_pattern(self.parent_file_id, 'parent_file_id', '[a-z0-9]{1,50}')
        if self.size is not None:
            self.validate_maximum(self.size, 'size', 53687091200)
            self.validate_minimum(self.size, 'size', 0)
        if self.video_media_metadata:
            self.video_media_metadata.validate()
        if self.video_preview_metadata:
            self.video_preview_metadata.validate()

    def to_map(self):
        result = {}
        if self.category is not None:
            result['category'] = self.category
        if self.content_hash is not None:
            result['content_hash'] = self.content_hash
        if self.content_hash_name is not None:
            result['content_hash_name'] = self.content_hash_name
        if self.content_type is not None:
            result['content_type'] = self.content_type
        if self.crc_64hash is not None:
            result['crc64_hash'] = self.crc_64hash
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.download_url is not None:
            result['download_url'] = self.download_url
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.encrypt_mode is not None:
            result['encrypt_mode'] = self.encrypt_mode
        if self.file_extension is not None:
            result['file_extension'] = self.file_extension
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.hidden is not None:
            result['hidden'] = self.hidden
        if self.image_media_metadata is not None:
            result['image_media_metadata'] = self.image_media_metadata.to_map()
        if self.labels is not None:
            result['labels'] = self.labels
        if self.meta is not None:
            result['meta'] = self.meta
        if self.name is not None:
            result['name'] = self.name
        if self.parent_file_id is not None:
            result['parent_file_id'] = self.parent_file_id
        if self.punish_flag is not None:
            result['punish_flag'] = self.punish_flag
        if self.size is not None:
            result['size'] = self.size
        if self.starred is not None:
            result['starred'] = self.starred
        if self.status is not None:
            result['status'] = self.status
        if self.streams_info is not None:
            result['streams_info'] = self.streams_info
        if self.thumbnail is not None:
            result['thumbnail'] = self.thumbnail
        if self.trashed_at is not None:
            result['trashed_at'] = self.trashed_at
        if self.type is not None:
            result['type'] = self.type
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        if self.upload_id is not None:
            result['upload_id'] = self.upload_id
        if self.url is not None:
            result['url'] = self.url
        if self.user_meta is not None:
            result['user_meta'] = self.user_meta
        if self.video_media_metadata is not None:
            result['video_media_metadata'] = self.video_media_metadata.to_map()
        if self.video_preview_metadata is not None:
            result['video_preview_metadata'] = self.video_preview_metadata.to_map()
        return result

    def from_map(self, map={}):
        if map.get('category') is not None:
            self.category = map.get('category')
        if map.get('content_hash') is not None:
            self.content_hash = map.get('content_hash')
        if map.get('content_hash_name') is not None:
            self.content_hash_name = map.get('content_hash_name')
        if map.get('content_type') is not None:
            self.content_type = map.get('content_type')
        if map.get('crc64_hash') is not None:
            self.crc_64hash = map.get('crc64_hash')
        if map.get('created_at') is not None:
            self.created_at = map.get('created_at')
        if map.get('description') is not None:
            self.description = map.get('description')
        if map.get('domain_id') is not None:
            self.domain_id = map.get('domain_id')
        if map.get('download_url') is not None:
            self.download_url = map.get('download_url')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('encrypt_mode') is not None:
            self.encrypt_mode = map.get('encrypt_mode')
        if map.get('file_extension') is not None:
            self.file_extension = map.get('file_extension')
        if map.get('file_id') is not None:
            self.file_id = map.get('file_id')
        if map.get('hidden') is not None:
            self.hidden = map.get('hidden')
        if map.get('image_media_metadata') is not None:
            temp_model = ImageMediaResponse()
            self.image_media_metadata = temp_model.from_map(map['image_media_metadata'])
        if map.get('labels') is not None:
            self.labels = map.get('labels')
        if map.get('meta') is not None:
            self.meta = map.get('meta')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('parent_file_id') is not None:
            self.parent_file_id = map.get('parent_file_id')
        if map.get('punish_flag') is not None:
            self.punish_flag = map.get('punish_flag')
        if map.get('size') is not None:
            self.size = map.get('size')
        if map.get('starred') is not None:
            self.starred = map.get('starred')
        if map.get('status') is not None:
            self.status = map.get('status')
        if map.get('streams_info') is not None:
            self.streams_info = map.get('streams_info')
        if map.get('thumbnail') is not None:
            self.thumbnail = map.get('thumbnail')
        if map.get('trashed_at') is not None:
            self.trashed_at = map.get('trashed_at')
        if map.get('type') is not None:
            self.type = map.get('type')
        if map.get('updated_at') is not None:
            self.updated_at = map.get('updated_at')
        if map.get('upload_id') is not None:
            self.upload_id = map.get('upload_id')
        if map.get('url') is not None:
            self.url = map.get('url')
        if map.get('user_meta') is not None:
            self.user_meta = map.get('user_meta')
        if map.get('video_media_metadata') is not None:
            temp_model = VideoMediaResponse()
            self.video_media_metadata = temp_model.from_map(map['video_media_metadata'])
        if map.get('video_preview_metadata') is not None:
            temp_model = VideoPreviewResponse()
            self.video_preview_metadata = temp_model.from_map(map['video_preview_metadata'])
        return self


class ConfirmLinkRequest(TeaModel):
    """
    *
    """
    def __init__(self, headers=None, temporary_token=None):
        self.headers = headers          # type: Dict[str, str]
        # 待绑定的临时token，此token只能访问绑定、取消绑定接口
        self.temporary_token = temporary_token  # type: str

    def validate(self):
        self.validate_required(self.temporary_token, 'temporary_token')

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.temporary_token is not None:
            result['temporary_token'] = self.temporary_token
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('temporary_token') is not None:
            self.temporary_token = map.get('temporary_token')
        return self


class CopyFileResponse(TeaModel):
    """
    文件拷贝 response
    """
    def __init__(self, async_task_id=None, domain_id=None, drive_id=None, file_id=None):
        # async_task_id
        self.async_task_id = async_task_id  # type: str
        # DomainID
        self.domain_id = domain_id      # type: str
        # drive_id
        self.drive_id = drive_id        # type: str
        # file_id
        self.file_id = file_id          # type: str

    def validate(self):
        if self.domain_id is not None:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z]+')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.file_id is not None:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9]{1,50}')

    def to_map(self):
        result = {}
        if self.async_task_id is not None:
            result['async_task_id'] = self.async_task_id
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        return result

    def from_map(self, map={}):
        if map.get('async_task_id') is not None:
            self.async_task_id = map.get('async_task_id')
        if map.get('domain_id') is not None:
            self.domain_id = map.get('domain_id')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('file_id') is not None:
            self.file_id = map.get('file_id')
        return self


class CorsRule(TeaModel):
    """
    *
    """
    def __init__(self, allowed_header=None, allowed_method=None, allowed_origin=None, expose_header=None,
                 max_age_seconds=None):
        # AllowedHeader
        self.allowed_header = allowed_header  # type: List[str]
        # AllowedMethod
        self.allowed_method = allowed_method  # type: List[str]
        # AllowedOrigin
        self.allowed_origin = allowed_origin  # type: List[str]
        # ExposeHeader
        self.expose_header = expose_header  # type: List[str]
        # MaxAgeSeconds
        self.max_age_seconds = max_age_seconds  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.allowed_header is not None:
            result['allowed_header'] = self.allowed_header
        if self.allowed_method is not None:
            result['allowed_method'] = self.allowed_method
        if self.allowed_origin is not None:
            result['allowed_origin'] = self.allowed_origin
        if self.expose_header is not None:
            result['expose_header'] = self.expose_header
        if self.max_age_seconds is not None:
            result['max_age_seconds'] = self.max_age_seconds
        return result

    def from_map(self, map={}):
        if map.get('allowed_header') is not None:
            self.allowed_header = map.get('allowed_header')
        if map.get('allowed_method') is not None:
            self.allowed_method = map.get('allowed_method')
        if map.get('allowed_origin') is not None:
            self.allowed_origin = map.get('allowed_origin')
        if map.get('expose_header') is not None:
            self.expose_header = map.get('expose_header')
        if map.get('max_age_seconds') is not None:
            self.max_age_seconds = map.get('max_age_seconds')
        return self


class CreateDriveResponse(TeaModel):
    """
    Create drive response
    """
    def __init__(self, domain_id=None, drive_id=None):
        # Domain ID
        self.domain_id = domain_id      # type: str
        # Drive ID
        self.drive_id = drive_id        # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        return result

    def from_map(self, map={}):
        if map.get('domain_id') is not None:
            self.domain_id = map.get('domain_id')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        return self


class CreateFileResponse(TeaModel):
    """
    Create file response
    """
    def __init__(self, domain_id=None, drive_id=None, encrypt_mode=None, exist=None, file_id=None, file_name=None,
                 parent_file_id=None, part_info_list=None, rapid_upload=None, status=None, streams_upload_info=None, type=None,
                 upload_id=None):
        # domain_id
        self.domain_id = domain_id      # type: str
        # drive_id
        self.drive_id = drive_id        # type: str
        # encrypt_mode
        self.encrypt_mode = encrypt_mode  # type: str
        # exist
        # type: boolean
        self.exist = exist              # type: bool
        # file_id
        self.file_id = file_id          # type: str
        # file_name
        self.file_name = file_name      # type: str
        # parent_file_id
        self.parent_file_id = parent_file_id  # type: str
        # part_info_list
        self.part_info_list = part_info_list  # type: List[UploadPartInfo]
        # rapid_upload
        # type: boolean
        self.rapid_upload = rapid_upload  # type: bool
        # status
        self.status = status            # type: str
        # streams_upload_info
        self.streams_upload_info = streams_upload_info  # type: dict
        # type
        self.type = type                # type: str
        # upload_id
        self.upload_id = upload_id      # type: str

    def validate(self):
        if self.domain_id is not None:
            self.validate_max_length(self.domain_id, 'domain_id', 50)
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9]{1,50}')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.file_id is not None:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9]{1,50}')
        if self.file_name is not None:
            self.validate_max_length(self.file_name, 'file_name', 255)
        if self.parent_file_id is not None:
            self.validate_max_length(self.parent_file_id, 'parent_file_id', 50)
            self.validate_pattern(self.parent_file_id, 'parent_file_id', '[a-z0-9]{1,50}')
        if self.part_info_list:
            for k in self.part_info_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.encrypt_mode is not None:
            result['encrypt_mode'] = self.encrypt_mode
        if self.exist is not None:
            result['exist'] = self.exist
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.file_name is not None:
            result['file_name'] = self.file_name
        if self.parent_file_id is not None:
            result['parent_file_id'] = self.parent_file_id
        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k in self.part_info_list:
                result['part_info_list'].append(k.to_map() if k else None)
        if self.rapid_upload is not None:
            result['rapid_upload'] = self.rapid_upload
        if self.status is not None:
            result['status'] = self.status
        if self.streams_upload_info is not None:
            result['streams_upload_info'] = self.streams_upload_info
        if self.type is not None:
            result['type'] = self.type
        if self.upload_id is not None:
            result['upload_id'] = self.upload_id
        return result

    def from_map(self, map={}):
        if map.get('domain_id') is not None:
            self.domain_id = map.get('domain_id')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('encrypt_mode') is not None:
            self.encrypt_mode = map.get('encrypt_mode')
        if map.get('exist') is not None:
            self.exist = map.get('exist')
        if map.get('file_id') is not None:
            self.file_id = map.get('file_id')
        if map.get('file_name') is not None:
            self.file_name = map.get('file_name')
        if map.get('parent_file_id') is not None:
            self.parent_file_id = map.get('parent_file_id')
        self.part_info_list = []
        if map.get('part_info_list') is not None:
            for k in map.get('part_info_list'):
                temp_model = UploadPartInfo()
                self.part_info_list.append(temp_model.from_map(k))
        if map.get('rapid_upload') is not None:
            self.rapid_upload = map.get('rapid_upload')
        if map.get('status') is not None:
            self.status = map.get('status')
        if map.get('streams_upload_info') is not None:
            self.streams_upload_info = map.get('streams_upload_info')
        if map.get('type') is not None:
            self.type = map.get('type')
        if map.get('upload_id') is not None:
            self.upload_id = map.get('upload_id')
        return self


class CreateShareLinkResponse(TeaModel):
    """
    create_share_link response
    """
    def __init__(self, share_id=None, share_msg=None, share_policy=None, share_pwd=None, share_url=None):
        # share_id
        self.share_id = share_id        # type: str
        # share_msg
        self.share_msg = share_msg      # type: str
        # share_policy
        self.share_policy = share_policy  # type: str
        # share_pwd
        self.share_pwd = share_pwd      # type: str
        # share_url
        self.share_url = share_url      # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.share_msg is not None:
            result['share_msg'] = self.share_msg
        if self.share_policy is not None:
            result['share_policy'] = self.share_policy
        if self.share_pwd is not None:
            result['share_pwd'] = self.share_pwd
        if self.share_url is not None:
            result['share_url'] = self.share_url
        return result

    def from_map(self, map={}):
        if map.get('share_id') is not None:
            self.share_id = map.get('share_id')
        if map.get('share_msg') is not None:
            self.share_msg = map.get('share_msg')
        if map.get('share_policy') is not None:
            self.share_policy = map.get('share_policy')
        if map.get('share_pwd') is not None:
            self.share_pwd = map.get('share_pwd')
        if map.get('share_url') is not None:
            self.share_url = map.get('share_url')
        return self


class CreateShareResponse(TeaModel):
    """
    Create share response
    """
    def __init__(self, domain_id=None, share_id=None):
        # domain_id
        self.domain_id = domain_id      # type: str
        # share_id
        self.share_id = share_id        # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.share_id is not None:
            result['share_id'] = self.share_id
        return result

    def from_map(self, map={}):
        if map.get('domain_id') is not None:
            self.domain_id = map.get('domain_id')
        if map.get('share_id') is not None:
            self.share_id = map.get('share_id')
        return self


class CroppingBoundary(TeaModel):
    """
    *
    """
    def __init__(self, height=None, left=None, top=None, width=None):
        self.height = height            # type: int
        self.left = left                # type: int
        self.top = top                  # type: int
        self.width = width              # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.height is not None:
            result['height'] = self.height
        if self.left is not None:
            result['left'] = self.left
        if self.top is not None:
            result['top'] = self.top
        if self.width is not None:
            result['width'] = self.width
        return result

    def from_map(self, map={}):
        if map.get('height') is not None:
            self.height = map.get('height')
        if map.get('left') is not None:
            self.left = map.get('left')
        if map.get('top') is not None:
            self.top = map.get('top')
        if map.get('width') is not None:
            self.width = map.get('width')
        return self


class CroppingSuggestionItem(TeaModel):
    """
    *
    """
    def __init__(self, aspect_ratio=None, cropping_boundary=None, score=None):
        self.aspect_ratio = aspect_ratio  # type: str
        self.cropping_boundary = cropping_boundary  # type: CroppingBoundary
        self.score = score              # type: float

    def validate(self):
        if self.cropping_boundary:
            self.cropping_boundary.validate()

    def to_map(self):
        result = {}
        if self.aspect_ratio is not None:
            result['aspect_ratio'] = self.aspect_ratio
        if self.cropping_boundary is not None:
            result['cropping_boundary'] = self.cropping_boundary.to_map()
        if self.score is not None:
            result['score'] = self.score
        return result

    def from_map(self, map={}):
        if map.get('aspect_ratio') is not None:
            self.aspect_ratio = map.get('aspect_ratio')
        if map.get('cropping_boundary') is not None:
            temp_model = CroppingBoundary()
            self.cropping_boundary = temp_model.from_map(map['cropping_boundary'])
        if map.get('score') is not None:
            self.score = map.get('score')
        return self


class DefaultChangePasswordRequest(TeaModel):
    """
    *
    """
    def __init__(self, headers=None, app_id=None, encrypted_key=None, new_password=None, phone_number=None,
                 phone_region=None, state=None):
        self.headers = headers          # type: Dict[str, str]
        # App ID, 当前访问的App
        self.app_id = app_id            # type: str
        # AES-256对称加密密钥，通过App公钥加密后传输
        self.encrypted_key = encrypted_key  # type: str
        # 新密码，必须包含数字和字母，长度8-20个字符
        self.new_password = new_password  # type: str
        # 手机号
        self.phone_number = phone_number  # type: str
        # 国家编号，默认86，不需要填+号，直接填数字
        self.phone_region = phone_region  # type: str
        # 修改密码的临时授权码
        self.state = state              # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.encrypted_key, 'encrypted_key')
        self.validate_required(self.new_password, 'new_password')
        self.validate_required(self.phone_number, 'phone_number')
        self.validate_required(self.state, 'state')

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.app_id is not None:
            result['app_id'] = self.app_id
        if self.encrypted_key is not None:
            result['encrypted_key'] = self.encrypted_key
        if self.new_password is not None:
            result['new_password'] = self.new_password
        if self.phone_number is not None:
            result['phone_number'] = self.phone_number
        if self.phone_region is not None:
            result['phone_region'] = self.phone_region
        if self.state is not None:
            result['state'] = self.state
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('app_id') is not None:
            self.app_id = map.get('app_id')
        if map.get('encrypted_key') is not None:
            self.encrypted_key = map.get('encrypted_key')
        if map.get('new_password') is not None:
            self.new_password = map.get('new_password')
        if map.get('phone_number') is not None:
            self.phone_number = map.get('phone_number')
        if map.get('phone_region') is not None:
            self.phone_region = map.get('phone_region')
        if map.get('state') is not None:
            self.state = map.get('state')
        return self


class DefaultSetPasswordRequest(TeaModel):
    """
    *
    """
    def __init__(self, headers=None, app_id=None, encrypted_key=None, new_password=None, state=None):
        self.headers = headers          # type: Dict[str, str]
        # App ID, 当前访问的App
        self.app_id = app_id            # type: str
        # AES-256对称加密密钥，通过App公钥加密后传输
        self.encrypted_key = encrypted_key  # type: str
        # 新密码，必须包含数字和字母，长度8-20个字符，使用AES-256对称加密后传输（CBC模式, 填充算法为PKCS7Padding，生成base64字符串）
        self.new_password = new_password  # type: str
        # 修改密码的临时授权码
        self.state = state              # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.encrypted_key, 'encrypted_key')
        self.validate_required(self.new_password, 'new_password')
        self.validate_required(self.state, 'state')

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.app_id is not None:
            result['app_id'] = self.app_id
        if self.encrypted_key is not None:
            result['encrypted_key'] = self.encrypted_key
        if self.new_password is not None:
            result['new_password'] = self.new_password
        if self.state is not None:
            result['state'] = self.state
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('app_id') is not None:
            self.app_id = map.get('app_id')
        if map.get('encrypted_key') is not None:
            self.encrypted_key = map.get('encrypted_key')
        if map.get('new_password') is not None:
            self.new_password = map.get('new_password')
        if map.get('state') is not None:
            self.state = map.get('state')
        return self


class DeleteDriveResponse(TeaModel):
    """
    delete drive response
    """
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = {}
        return result

    def from_map(self, map={}):
        return self


class DeleteFileResponse(TeaModel):
    """
    删除文件 response
    """
    def __init__(self, async_task_id=None, domain_id=None, drive_id=None, file_id=None):
        # async_task_id
        self.async_task_id = async_task_id  # type: str
        # domain_id
        self.domain_id = domain_id      # type: str
        # drive_id
        self.drive_id = drive_id        # type: str
        # file_id
        self.file_id = file_id          # type: str

    def validate(self):
        if self.domain_id is not None:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z]+')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.file_id is not None:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9]{1,50}')

    def to_map(self):
        result = {}
        if self.async_task_id is not None:
            result['async_task_id'] = self.async_task_id
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        return result

    def from_map(self, map={}):
        if map.get('async_task_id') is not None:
            self.async_task_id = map.get('async_task_id')
        if map.get('domain_id') is not None:
            self.domain_id = map.get('domain_id')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('file_id') is not None:
            self.file_id = map.get('file_id')
        return self


class DeleteFilesResponse(TeaModel):
    """
    批量删除文件 response
    """
    def __init__(self, deleted_file_id_list=None, domain_id=None, drive_id=None):
        # deleted_file_id_list
        self.deleted_file_id_list = deleted_file_id_list  # type: List[str]
        # domain_id
        self.domain_id = domain_id      # type: str
        # drive_id
        self.drive_id = drive_id        # type: str

    def validate(self):
        if self.domain_id is not None:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z]+')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')

    def to_map(self):
        result = {}
        if self.deleted_file_id_list is not None:
            result['deleted_file_id_list'] = self.deleted_file_id_list
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        return result

    def from_map(self, map={}):
        if map.get('deleted_file_id_list') is not None:
            self.deleted_file_id_list = map.get('deleted_file_id_list')
        if map.get('domain_id') is not None:
            self.domain_id = map.get('domain_id')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        return self


class DeviceAuthorizeRequest(TeaModel):
    """
    *
    """
    def __init__(self, client_id=None, device_info=None, device_name=None, login_type=None, scope=None):
        # Client ID, 此处填写创建App时返回的AppID
        self.client_id = client_id      # type: str
        # 设备信息，用于用户识别设备
        self.device_info = device_info  # type: str
        # 设备名，实现方需保证不同设备的设备名不重复（推荐用硬件名称+硬件型号作为设备名）
        self.device_name = device_name  # type: str
        # 鉴权方式，目前支持ding,ram鉴权
        self.login_type = login_type    # type: str
        # 申请的权限列表, 默认为所有权限
        self.scope = scope              # type: List[str]

    def validate(self):
        self.validate_required(self.client_id, 'client_id')
        self.validate_required(self.device_name, 'device_name')

    def to_map(self):
        result = {}
        if self.client_id is not None:
            result['ClientID'] = self.client_id
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.login_type is not None:
            result['LoginType'] = self.login_type
        if self.scope is not None:
            result['Scope'] = self.scope
        return result

    def from_map(self, map={}):
        if map.get('ClientID') is not None:
            self.client_id = map.get('ClientID')
        if map.get('DeviceInfo') is not None:
            self.device_info = map.get('DeviceInfo')
        if map.get('DeviceName') is not None:
            self.device_name = map.get('DeviceName')
        if map.get('LoginType') is not None:
            self.login_type = map.get('LoginType')
        if map.get('Scope') is not None:
            self.scope = map.get('Scope')
        return self


class FileDeltaResponse(TeaModel):
    """
    the file op info
    """
    def __init__(self, current_category=None, file=None, file_id=None, op=None):
        self.current_category = current_category  # type: str
        self.file = file                # type: BaseFileResponse
        self.file_id = file_id          # type: str
        self.op = op                    # type: str

    def validate(self):
        if self.file:
            self.file.validate()

    def to_map(self):
        result = {}
        if self.current_category is not None:
            result['current_category'] = self.current_category
        if self.file is not None:
            result['file'] = self.file.to_map()
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.op is not None:
            result['op'] = self.op
        return result

    def from_map(self, map={}):
        if map.get('current_category') is not None:
            self.current_category = map.get('current_category')
        if map.get('file') is not None:
            temp_model = BaseFileResponse()
            self.file = temp_model.from_map(map['file'])
        if map.get('file_id') is not None:
            self.file_id = map.get('file_id')
        if map.get('op') is not None:
            self.op = map.get('op')
        return self


class GetAccessTokenByLinkInfoRequest(TeaModel):
    """
    *
    """
    def __init__(self, headers=None, extra=None, identity=None, type=None):
        self.headers = headers          # type: Dict[str, str]
        # 额外的信息，比如type为mobile时，此字段为国家编号，不填默认86
        self.extra = extra              # type: str
        # 唯一身份标识
        self.identity = identity        # type: str
        # 认证类型
        self.type = type                # type: str

    def validate(self):
        self.validate_required(self.identity, 'identity')
        self.validate_required(self.type, 'type')

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.extra is not None:
            result['extra'] = self.extra
        if self.identity is not None:
            result['identity'] = self.identity
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('extra') is not None:
            self.extra = map.get('extra')
        if map.get('identity') is not None:
            self.identity = map.get('identity')
        if map.get('type') is not None:
            self.type = map.get('type')
        return self


class GetAppPublicKeyRequest(TeaModel):
    """
    *
    """
    def __init__(self, headers=None, app_id=None):
        self.headers = headers          # type: Dict[str, str]
        # App ID
        self.app_id = app_id            # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.app_id is not None:
            result['app_id'] = self.app_id
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('app_id') is not None:
            self.app_id = map.get('app_id')
        return self


class GetAsyncTaskResponse(TeaModel):
    """
    Get AsyncTask Response
    """
    def __init__(self, async_task_id=None, message=None, state=None):
        # async_task_id
        # type:string
        self.async_task_id = async_task_id  # type: str
        # message
        self.message = message          # type: str
        # state
        self.state = state              # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.async_task_id is not None:
            result['async_task_id'] = self.async_task_id
        if self.message is not None:
            result['message'] = self.message
        if self.state is not None:
            result['state'] = self.state
        return result

    def from_map(self, map={}):
        if map.get('async_task_id') is not None:
            self.async_task_id = map.get('async_task_id')
        if map.get('message') is not None:
            self.message = map.get('message')
        if map.get('state') is not None:
            self.state = map.get('state')
        return self


class GetByLinkInfoRequest(TeaModel):
    """
    *
    """
    def __init__(self, headers=None, extra=None, identity=None, type=None):
        self.headers = headers          # type: Dict[str, str]
        # 额外的信息，比如type为mobile时，此字段为国家编号，不填默认86
        self.extra = extra              # type: str
        # 唯一身份标识
        self.identity = identity        # type: str
        # 认证类型
        self.type = type                # type: str

    def validate(self):
        self.validate_required(self.identity, 'identity')
        self.validate_required(self.type, 'type')

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.extra is not None:
            result['extra'] = self.extra
        if self.identity is not None:
            result['identity'] = self.identity
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('extra') is not None:
            self.extra = map.get('extra')
        if map.get('identity') is not None:
            self.identity = map.get('identity')
        if map.get('type') is not None:
            self.type = map.get('type')
        return self


class GetCaptchaRequest(TeaModel):
    """
    *
    """
    def __init__(self, headers=None, app_id=None):
        self.headers = headers          # type: Dict[str, str]
        # App ID, 当前访问的App
        self.app_id = app_id            # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.app_id is not None:
            result['app_id'] = self.app_id
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('app_id') is not None:
            self.app_id = map.get('app_id')
        return self


class GetDownloadUrlResponse(TeaModel):
    """
    获取download url response
    """
    def __init__(self, expiration=None, method=None, ratelimit=None, size=None, streams_url=None, url=None):
        # expiration
        self.expiration = expiration    # type: str
        # method
        self.method = method            # type: str
        self.ratelimit = ratelimit      # type: RateLimit
        # size
        self.size = size                # type: int
        # streams url info
        self.streams_url = streams_url  # type: dict
        # url
        self.url = url                  # type: str

    def validate(self):
        if self.ratelimit:
            self.ratelimit.validate()

    def to_map(self):
        result = {}
        if self.expiration is not None:
            result['expiration'] = self.expiration
        if self.method is not None:
            result['method'] = self.method
        if self.ratelimit is not None:
            result['ratelimit'] = self.ratelimit.to_map()
        if self.size is not None:
            result['size'] = self.size
        if self.streams_url is not None:
            result['streams_url'] = self.streams_url
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, map={}):
        if map.get('expiration') is not None:
            self.expiration = map.get('expiration')
        if map.get('method') is not None:
            self.method = map.get('method')
        if map.get('ratelimit') is not None:
            temp_model = RateLimit()
            self.ratelimit = temp_model.from_map(map['ratelimit'])
        if map.get('size') is not None:
            self.size = map.get('size')
        if map.get('streams_url') is not None:
            self.streams_url = map.get('streams_url')
        if map.get('url') is not None:
            self.url = map.get('url')
        return self


class GetDriveResponse(TeaModel):
    """
    Get drive response
    """
    def __init__(self, creator=None, description=None, domain_id=None, drive_id=None, drive_name=None,
                 drive_type=None, encrypt_data_access=None, encrypt_mode=None, owner=None, relative_path=None, status=None,
                 store_id=None, total_size=None, used_size=None):
        # Drive 创建者
        self.creator = creator          # type: str
        # Drive 备注信息
        self.description = description  # type: str
        # Domain ID
        self.domain_id = domain_id      # type: str
        # Drive ID
        self.drive_id = drive_id        # type: str
        # Drive 名称
        self.drive_name = drive_name    # type: str
        # Drive 类型
        self.drive_type = drive_type    # type: str
        self.encrypt_data_access = encrypt_data_access  # type: bool
        self.encrypt_mode = encrypt_mode  # type: str
        # Drive 所有者
        self.owner = owner              # type: str
        # Drive存储基于store的相对路径，domain的PathType为OSSPath时返回
        self.relative_path = relative_path  # type: str
        # Drive 状态
        self.status = status            # type: str
        # 存储 ID, domain的PathType为OSSPath时返回
        self.store_id = store_id        # type: str
        # Drive 空间总量
        self.total_size = total_size    # type: int
        # Drive 空间已使用量
        self.used_size = used_size      # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.creator is not None:
            result['creator'] = self.creator
        if self.description is not None:
            result['description'] = self.description
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.drive_name is not None:
            result['drive_name'] = self.drive_name
        if self.drive_type is not None:
            result['drive_type'] = self.drive_type
        if self.encrypt_data_access is not None:
            result['encrypt_data_access'] = self.encrypt_data_access
        if self.encrypt_mode is not None:
            result['encrypt_mode'] = self.encrypt_mode
        if self.owner is not None:
            result['owner'] = self.owner
        if self.relative_path is not None:
            result['relative_path'] = self.relative_path
        if self.status is not None:
            result['status'] = self.status
        if self.store_id is not None:
            result['store_id'] = self.store_id
        if self.total_size is not None:
            result['total_size'] = self.total_size
        if self.used_size is not None:
            result['used_size'] = self.used_size
        return result

    def from_map(self, map={}):
        if map.get('creator') is not None:
            self.creator = map.get('creator')
        if map.get('description') is not None:
            self.description = map.get('description')
        if map.get('domain_id') is not None:
            self.domain_id = map.get('domain_id')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('drive_name') is not None:
            self.drive_name = map.get('drive_name')
        if map.get('drive_type') is not None:
            self.drive_type = map.get('drive_type')
        if map.get('encrypt_data_access') is not None:
            self.encrypt_data_access = map.get('encrypt_data_access')
        if map.get('encrypt_mode') is not None:
            self.encrypt_mode = map.get('encrypt_mode')
        if map.get('owner') is not None:
            self.owner = map.get('owner')
        if map.get('relative_path') is not None:
            self.relative_path = map.get('relative_path')
        if map.get('status') is not None:
            self.status = map.get('status')
        if map.get('store_id') is not None:
            self.store_id = map.get('store_id')
        if map.get('total_size') is not None:
            self.total_size = map.get('total_size')
        if map.get('used_size') is not None:
            self.used_size = map.get('used_size')
        return self


class GetFileByPathResponse(TeaModel):
    """
    根据路径获取文件元数据response
    """
    def __init__(self, category=None, content_hash=None, content_hash_name=None, content_type=None, crc_64hash=None,
                 created_at=None, description=None, domain_id=None, download_url=None, drive_id=None, encrypt_mode=None,
                 file_extension=None, file_id=None, hidden=None, image_media_metadata=None, labels=None, meta=None, name=None,
                 parent_file_id=None, punish_flag=None, size=None, starred=None, status=None, streams_info=None, thumbnail=None,
                 trashed_at=None, type=None, updated_at=None, upload_id=None, url=None, user_meta=None,
                 video_media_metadata=None, video_preview_metadata=None):
        # category
        self.category = category        # type: str
        # Content Hash
        self.content_hash = content_hash  # type: str
        # content_hash_name
        self.content_hash_name = content_hash_name  # type: str
        # content_type
        self.content_type = content_type  # type: str
        # crc64_hash
        self.crc_64hash = crc_64hash    # type: str
        # created_at
        self.created_at = created_at    # type: str
        # description
        self.description = description  # type: str
        # DomainID
        self.domain_id = domain_id      # type: str
        # download_url
        self.download_url = download_url  # type: str
        # drive_id
        self.drive_id = drive_id        # type: str
        # encrypt_mode
        self.encrypt_mode = encrypt_mode  # type: str
        # file_extension
        self.file_extension = file_extension  # type: str
        # file_id
        self.file_id = file_id          # type: str
        # Hidden
        # type: boolean
        self.hidden = hidden            # type: bool
        self.image_media_metadata = image_media_metadata  # type: ImageMediaResponse
        # labels
        self.labels = labels            # type: List[str]
        self.meta = meta                # type: str
        # name
        self.name = name                # type: str
        # parent_file_id
        self.parent_file_id = parent_file_id  # type: str
        self.punish_flag = punish_flag  # type: int
        # Size
        self.size = size                # type: int
        # starred
        # type: boolean
        self.starred = starred          # type: bool
        # status
        self.status = status            # type: str
        # @Deprecated streams url info
        self.streams_info = streams_info  # type: dict
        # thumbnail
        self.thumbnail = thumbnail      # type: str
        # trashed_at
        self.trashed_at = trashed_at    # type: str
        # type
        self.type = type                # type: str
        # updated_at
        self.updated_at = updated_at    # type: str
        # upload_id
        self.upload_id = upload_id      # type: str
        # url
        self.url = url                  # type: str
        # user_meta
        self.user_meta = user_meta      # type: str
        self.video_media_metadata = video_media_metadata  # type: VideoMediaResponse
        self.video_preview_metadata = video_preview_metadata  # type: VideoPreviewResponse

    def validate(self):
        if self.domain_id is not None:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z]+')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.file_id is not None:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9]{1,50}')
        if self.image_media_metadata:
            self.image_media_metadata.validate()
        self.validate_required(self.name, 'name')
        if self.name is not None:
            self.validate_pattern(self.name, 'name', '[a-zA-Z0-9.-]{1,1000}')
        if self.parent_file_id is not None:
            self.validate_max_length(self.parent_file_id, 'parent_file_id', 50)
            self.validate_pattern(self.parent_file_id, 'parent_file_id', '[a-z0-9]{1,50}')
        if self.size is not None:
            self.validate_maximum(self.size, 'size', 53687091200)
            self.validate_minimum(self.size, 'size', 0)
        if self.video_media_metadata:
            self.video_media_metadata.validate()
        if self.video_preview_metadata:
            self.video_preview_metadata.validate()

    def to_map(self):
        result = {}
        if self.category is not None:
            result['category'] = self.category
        if self.content_hash is not None:
            result['content_hash'] = self.content_hash
        if self.content_hash_name is not None:
            result['content_hash_name'] = self.content_hash_name
        if self.content_type is not None:
            result['content_type'] = self.content_type
        if self.crc_64hash is not None:
            result['crc64_hash'] = self.crc_64hash
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.download_url is not None:
            result['download_url'] = self.download_url
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.encrypt_mode is not None:
            result['encrypt_mode'] = self.encrypt_mode
        if self.file_extension is not None:
            result['file_extension'] = self.file_extension
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.hidden is not None:
            result['hidden'] = self.hidden
        if self.image_media_metadata is not None:
            result['image_media_metadata'] = self.image_media_metadata.to_map()
        if self.labels is not None:
            result['labels'] = self.labels
        if self.meta is not None:
            result['meta'] = self.meta
        if self.name is not None:
            result['name'] = self.name
        if self.parent_file_id is not None:
            result['parent_file_id'] = self.parent_file_id
        if self.punish_flag is not None:
            result['punish_flag'] = self.punish_flag
        if self.size is not None:
            result['size'] = self.size
        if self.starred is not None:
            result['starred'] = self.starred
        if self.status is not None:
            result['status'] = self.status
        if self.streams_info is not None:
            result['streams_info'] = self.streams_info
        if self.thumbnail is not None:
            result['thumbnail'] = self.thumbnail
        if self.trashed_at is not None:
            result['trashed_at'] = self.trashed_at
        if self.type is not None:
            result['type'] = self.type
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        if self.upload_id is not None:
            result['upload_id'] = self.upload_id
        if self.url is not None:
            result['url'] = self.url
        if self.user_meta is not None:
            result['user_meta'] = self.user_meta
        if self.video_media_metadata is not None:
            result['video_media_metadata'] = self.video_media_metadata.to_map()
        if self.video_preview_metadata is not None:
            result['video_preview_metadata'] = self.video_preview_metadata.to_map()
        return result

    def from_map(self, map={}):
        if map.get('category') is not None:
            self.category = map.get('category')
        if map.get('content_hash') is not None:
            self.content_hash = map.get('content_hash')
        if map.get('content_hash_name') is not None:
            self.content_hash_name = map.get('content_hash_name')
        if map.get('content_type') is not None:
            self.content_type = map.get('content_type')
        if map.get('crc64_hash') is not None:
            self.crc_64hash = map.get('crc64_hash')
        if map.get('created_at') is not None:
            self.created_at = map.get('created_at')
        if map.get('description') is not None:
            self.description = map.get('description')
        if map.get('domain_id') is not None:
            self.domain_id = map.get('domain_id')
        if map.get('download_url') is not None:
            self.download_url = map.get('download_url')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('encrypt_mode') is not None:
            self.encrypt_mode = map.get('encrypt_mode')
        if map.get('file_extension') is not None:
            self.file_extension = map.get('file_extension')
        if map.get('file_id') is not None:
            self.file_id = map.get('file_id')
        if map.get('hidden') is not None:
            self.hidden = map.get('hidden')
        if map.get('image_media_metadata') is not None:
            temp_model = ImageMediaResponse()
            self.image_media_metadata = temp_model.from_map(map['image_media_metadata'])
        if map.get('labels') is not None:
            self.labels = map.get('labels')
        if map.get('meta') is not None:
            self.meta = map.get('meta')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('parent_file_id') is not None:
            self.parent_file_id = map.get('parent_file_id')
        if map.get('punish_flag') is not None:
            self.punish_flag = map.get('punish_flag')
        if map.get('size') is not None:
            self.size = map.get('size')
        if map.get('starred') is not None:
            self.starred = map.get('starred')
        if map.get('status') is not None:
            self.status = map.get('status')
        if map.get('streams_info') is not None:
            self.streams_info = map.get('streams_info')
        if map.get('thumbnail') is not None:
            self.thumbnail = map.get('thumbnail')
        if map.get('trashed_at') is not None:
            self.trashed_at = map.get('trashed_at')
        if map.get('type') is not None:
            self.type = map.get('type')
        if map.get('updated_at') is not None:
            self.updated_at = map.get('updated_at')
        if map.get('upload_id') is not None:
            self.upload_id = map.get('upload_id')
        if map.get('url') is not None:
            self.url = map.get('url')
        if map.get('user_meta') is not None:
            self.user_meta = map.get('user_meta')
        if map.get('video_media_metadata') is not None:
            temp_model = VideoMediaResponse()
            self.video_media_metadata = temp_model.from_map(map['video_media_metadata'])
        if map.get('video_preview_metadata') is not None:
            temp_model = VideoPreviewResponse()
            self.video_preview_metadata = temp_model.from_map(map['video_preview_metadata'])
        return self


class GetFileResponse(TeaModel):
    """
    获取文件元数据response
    """
    def __init__(self, category=None, content_hash=None, content_hash_name=None, content_type=None, crc_64hash=None,
                 created_at=None, description=None, domain_id=None, download_url=None, drive_id=None, encrypt_mode=None,
                 file_extension=None, file_id=None, hidden=None, image_media_metadata=None, labels=None, meta=None, name=None,
                 parent_file_id=None, punish_flag=None, size=None, starred=None, status=None, streams_info=None, thumbnail=None,
                 trashed_at=None, type=None, updated_at=None, upload_id=None, url=None, user_meta=None,
                 video_media_metadata=None, video_preview_metadata=None):
        # category
        self.category = category        # type: str
        # Content Hash
        self.content_hash = content_hash  # type: str
        # content_hash_name
        self.content_hash_name = content_hash_name  # type: str
        # content_type
        self.content_type = content_type  # type: str
        # crc64_hash
        self.crc_64hash = crc_64hash    # type: str
        # created_at
        self.created_at = created_at    # type: str
        # description
        self.description = description  # type: str
        # DomainID
        self.domain_id = domain_id      # type: str
        # download_url
        self.download_url = download_url  # type: str
        # drive_id
        self.drive_id = drive_id        # type: str
        # encrypt_mode
        self.encrypt_mode = encrypt_mode  # type: str
        # file_extension
        self.file_extension = file_extension  # type: str
        # file_id
        self.file_id = file_id          # type: str
        # Hidden
        # type: boolean
        self.hidden = hidden            # type: bool
        self.image_media_metadata = image_media_metadata  # type: ImageMediaResponse
        # labels
        self.labels = labels            # type: List[str]
        self.meta = meta                # type: str
        # name
        self.name = name                # type: str
        # parent_file_id
        self.parent_file_id = parent_file_id  # type: str
        self.punish_flag = punish_flag  # type: int
        # Size
        self.size = size                # type: int
        # starred
        # type: boolean
        self.starred = starred          # type: bool
        # status
        self.status = status            # type: str
        # @Deprecated streams url info
        self.streams_info = streams_info  # type: dict
        # thumbnail
        self.thumbnail = thumbnail      # type: str
        # trashed_at
        self.trashed_at = trashed_at    # type: str
        # type
        self.type = type                # type: str
        # updated_at
        self.updated_at = updated_at    # type: str
        # upload_id
        self.upload_id = upload_id      # type: str
        # url
        self.url = url                  # type: str
        # user_meta
        self.user_meta = user_meta      # type: str
        self.video_media_metadata = video_media_metadata  # type: VideoMediaResponse
        self.video_preview_metadata = video_preview_metadata  # type: VideoPreviewResponse

    def validate(self):
        if self.domain_id is not None:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z]+')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.file_id is not None:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9]{1,50}')
        if self.image_media_metadata:
            self.image_media_metadata.validate()
        self.validate_required(self.name, 'name')
        if self.name is not None:
            self.validate_pattern(self.name, 'name', '[a-zA-Z0-9.-]{1,1000}')
        if self.parent_file_id is not None:
            self.validate_max_length(self.parent_file_id, 'parent_file_id', 50)
            self.validate_pattern(self.parent_file_id, 'parent_file_id', '[a-z0-9]{1,50}')
        if self.size is not None:
            self.validate_maximum(self.size, 'size', 53687091200)
            self.validate_minimum(self.size, 'size', 0)
        if self.video_media_metadata:
            self.video_media_metadata.validate()
        if self.video_preview_metadata:
            self.video_preview_metadata.validate()

    def to_map(self):
        result = {}
        if self.category is not None:
            result['category'] = self.category
        if self.content_hash is not None:
            result['content_hash'] = self.content_hash
        if self.content_hash_name is not None:
            result['content_hash_name'] = self.content_hash_name
        if self.content_type is not None:
            result['content_type'] = self.content_type
        if self.crc_64hash is not None:
            result['crc64_hash'] = self.crc_64hash
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.download_url is not None:
            result['download_url'] = self.download_url
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.encrypt_mode is not None:
            result['encrypt_mode'] = self.encrypt_mode
        if self.file_extension is not None:
            result['file_extension'] = self.file_extension
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.hidden is not None:
            result['hidden'] = self.hidden
        if self.image_media_metadata is not None:
            result['image_media_metadata'] = self.image_media_metadata.to_map()
        if self.labels is not None:
            result['labels'] = self.labels
        if self.meta is not None:
            result['meta'] = self.meta
        if self.name is not None:
            result['name'] = self.name
        if self.parent_file_id is not None:
            result['parent_file_id'] = self.parent_file_id
        if self.punish_flag is not None:
            result['punish_flag'] = self.punish_flag
        if self.size is not None:
            result['size'] = self.size
        if self.starred is not None:
            result['starred'] = self.starred
        if self.status is not None:
            result['status'] = self.status
        if self.streams_info is not None:
            result['streams_info'] = self.streams_info
        if self.thumbnail is not None:
            result['thumbnail'] = self.thumbnail
        if self.trashed_at is not None:
            result['trashed_at'] = self.trashed_at
        if self.type is not None:
            result['type'] = self.type
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        if self.upload_id is not None:
            result['upload_id'] = self.upload_id
        if self.url is not None:
            result['url'] = self.url
        if self.user_meta is not None:
            result['user_meta'] = self.user_meta
        if self.video_media_metadata is not None:
            result['video_media_metadata'] = self.video_media_metadata.to_map()
        if self.video_preview_metadata is not None:
            result['video_preview_metadata'] = self.video_preview_metadata.to_map()
        return result

    def from_map(self, map={}):
        if map.get('category') is not None:
            self.category = map.get('category')
        if map.get('content_hash') is not None:
            self.content_hash = map.get('content_hash')
        if map.get('content_hash_name') is not None:
            self.content_hash_name = map.get('content_hash_name')
        if map.get('content_type') is not None:
            self.content_type = map.get('content_type')
        if map.get('crc64_hash') is not None:
            self.crc_64hash = map.get('crc64_hash')
        if map.get('created_at') is not None:
            self.created_at = map.get('created_at')
        if map.get('description') is not None:
            self.description = map.get('description')
        if map.get('domain_id') is not None:
            self.domain_id = map.get('domain_id')
        if map.get('download_url') is not None:
            self.download_url = map.get('download_url')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('encrypt_mode') is not None:
            self.encrypt_mode = map.get('encrypt_mode')
        if map.get('file_extension') is not None:
            self.file_extension = map.get('file_extension')
        if map.get('file_id') is not None:
            self.file_id = map.get('file_id')
        if map.get('hidden') is not None:
            self.hidden = map.get('hidden')
        if map.get('image_media_metadata') is not None:
            temp_model = ImageMediaResponse()
            self.image_media_metadata = temp_model.from_map(map['image_media_metadata'])
        if map.get('labels') is not None:
            self.labels = map.get('labels')
        if map.get('meta') is not None:
            self.meta = map.get('meta')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('parent_file_id') is not None:
            self.parent_file_id = map.get('parent_file_id')
        if map.get('punish_flag') is not None:
            self.punish_flag = map.get('punish_flag')
        if map.get('size') is not None:
            self.size = map.get('size')
        if map.get('starred') is not None:
            self.starred = map.get('starred')
        if map.get('status') is not None:
            self.status = map.get('status')
        if map.get('streams_info') is not None:
            self.streams_info = map.get('streams_info')
        if map.get('thumbnail') is not None:
            self.thumbnail = map.get('thumbnail')
        if map.get('trashed_at') is not None:
            self.trashed_at = map.get('trashed_at')
        if map.get('type') is not None:
            self.type = map.get('type')
        if map.get('updated_at') is not None:
            self.updated_at = map.get('updated_at')
        if map.get('upload_id') is not None:
            self.upload_id = map.get('upload_id')
        if map.get('url') is not None:
            self.url = map.get('url')
        if map.get('user_meta') is not None:
            self.user_meta = map.get('user_meta')
        if map.get('video_media_metadata') is not None:
            temp_model = VideoMediaResponse()
            self.video_media_metadata = temp_model.from_map(map['video_media_metadata'])
        if map.get('video_preview_metadata') is not None:
            temp_model = VideoPreviewResponse()
            self.video_preview_metadata = temp_model.from_map(map['video_preview_metadata'])
        return self


class GetLastCursorResponse(TeaModel):
    """
    get last file op cursor response
    """
    def __init__(self, cursor=None):
        self.cursor = cursor            # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.cursor is not None:
            result['cursor'] = self.cursor
        return result

    def from_map(self, map={}):
        if map.get('cursor') is not None:
            self.cursor = map.get('cursor')
        return self


class GetLinkInfoByUserIDRequest(TeaModel):
    """
    *
    """
    def __init__(self, headers=None, user_id=None):
        self.headers = headers          # type: Dict[str, str]
        # user ID
        self.user_id = user_id          # type: str

    def validate(self):
        self.validate_required(self.user_id, 'user_id')

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('user_id') is not None:
            self.user_id = map.get('user_id')
        return self


class GetMediaPlayURLResponse(TeaModel):
    """
    get_media_play_url response
    """
    def __init__(self, url=None):
        # url
        self.url = url                  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, map={}):
        if map.get('url') is not None:
            self.url = map.get('url')
        return self


class GetOfficePreviewUrlResponse(TeaModel):
    """
    获取文档预览地址 response
    """
    def __init__(self, access_token=None, preview_url=None):
        # AccessToken
        self.access_token = access_token  # type: str
        # preview_url
        self.preview_url = preview_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.access_token is not None:
            result['access_token'] = self.access_token
        if self.preview_url is not None:
            result['preview_url'] = self.preview_url
        return result

    def from_map(self, map={}):
        if map.get('access_token') is not None:
            self.access_token = map.get('access_token')
        if map.get('preview_url') is not None:
            self.preview_url = map.get('preview_url')
        return self


class GetPublicKeyResponse(TeaModel):
    """
    *
    """
    def __init__(self, app_id=None, key_pair_id=None, public_key=None):
        # App ID
        self.app_id = app_id            # type: str
        self.key_pair_id = key_pair_id  # type: str
        # RSA加密算法的公钥, PEM格式
        self.public_key = public_key    # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.public_key, 'public_key')

    def to_map(self):
        result = {}
        if self.app_id is not None:
            result['app_id'] = self.app_id
        if self.key_pair_id is not None:
            result['key_pair_id'] = self.key_pair_id
        if self.public_key is not None:
            result['public_key'] = self.public_key
        return result

    def from_map(self, map={}):
        if map.get('app_id') is not None:
            self.app_id = map.get('app_id')
        if map.get('key_pair_id') is not None:
            self.key_pair_id = map.get('key_pair_id')
        if map.get('public_key') is not None:
            self.public_key = map.get('public_key')
        return self


class GetShareLinkByAnonymousResponse(TeaModel):
    """
    get_share_link_by_anonymous response
    """
    def __init__(self, creator_id=None, creator_name=None, expiration=None, updated_at=None):
        # creator_id
        self.creator_id = creator_id    # type: str
        # creator_name
        self.creator_name = creator_name  # type: str
        # expiration
        self.expiration = expiration    # type: str
        # updated_at
        self.updated_at = updated_at    # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.creator_id is not None:
            result['creator_id'] = self.creator_id
        if self.creator_name is not None:
            result['creator_name'] = self.creator_name
        if self.expiration is not None:
            result['expiration'] = self.expiration
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        return result

    def from_map(self, map={}):
        if map.get('creator_id') is not None:
            self.creator_id = map.get('creator_id')
        if map.get('creator_name') is not None:
            self.creator_name = map.get('creator_name')
        if map.get('expiration') is not None:
            self.expiration = map.get('expiration')
        if map.get('updated_at') is not None:
            self.updated_at = map.get('updated_at')
        return self


class GetShareLinkIDResponse(TeaModel):
    """
    get_share_id response
    """
    def __init__(self, share_id=None, share_pwd=None):
        # share_id
        self.share_id = share_id        # type: str
        # share_pwd
        self.share_pwd = share_pwd      # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.share_pwd is not None:
            result['share_pwd'] = self.share_pwd
        return result

    def from_map(self, map={}):
        if map.get('share_id') is not None:
            self.share_id = map.get('share_id')
        if map.get('share_pwd') is not None:
            self.share_pwd = map.get('share_pwd')
        return self


class GetShareLinkTokenResponse(TeaModel):
    """
    get_share_token response
    """
    def __init__(self, expire_time=None, expires_in=None, share_token=None):
        # expire_time
        self.expire_time = expire_time  # type: str
        # expires_in
        self.expires_in = expires_in    # type: int
        # share_token
        self.share_token = share_token  # type: str

    def validate(self):
        self.validate_required(self.expire_time, 'expire_time')
        self.validate_required(self.expires_in, 'expires_in')
        self.validate_required(self.share_token, 'share_token')

    def to_map(self):
        result = {}
        if self.expire_time is not None:
            result['expire_time'] = self.expire_time
        if self.expires_in is not None:
            result['expires_in'] = self.expires_in
        if self.share_token is not None:
            result['share_token'] = self.share_token
        return result

    def from_map(self, map={}):
        if map.get('expire_time') is not None:
            self.expire_time = map.get('expire_time')
        if map.get('expires_in') is not None:
            self.expires_in = map.get('expires_in')
        if map.get('share_token') is not None:
            self.share_token = map.get('share_token')
        return self


class GetShareResponse(TeaModel):
    """
    Get share response
    """
    def __init__(self, created_at=None, creator=None, description=None, domain_id=None, drive_id=None,
                 expiration=None, expired=None, owner=None, permissions=None, share_file_path=None, share_id=None,
                 share_name=None, share_policy=None, status=None, updated_at=None):
        # created_at
        self.created_at = created_at    # type: str
        # creator
        self.creator = creator          # type: str
        # description
        self.description = description  # type: str
        # domain_id
        self.domain_id = domain_id      # type: str
        # drive_id
        self.drive_id = drive_id        # type: str
        # expiration
        self.expiration = expiration    # type: str
        # expired
        self.expired = expired          # type: bool
        # owner
        self.owner = owner              # type: str
        # permissions
        self.permissions = permissions  # type: List[str]
        # share_path
        self.share_file_path = share_file_path  # type: str
        # share_id
        self.share_id = share_id        # type: str
        # share_name
        self.share_name = share_name    # type: str
        self.share_policy = share_policy  # type: List[SharePermissionPolicy]
        # status
        self.status = status            # type: str
        # updated_at
        self.updated_at = updated_at    # type: str

    def validate(self):
        if self.share_policy:
            for k in self.share_policy:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.creator is not None:
            result['creator'] = self.creator
        if self.description is not None:
            result['description'] = self.description
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.expiration is not None:
            result['expiration'] = self.expiration
        if self.expired is not None:
            result['expired'] = self.expired
        if self.owner is not None:
            result['owner'] = self.owner
        if self.permissions is not None:
            result['permissions'] = self.permissions
        if self.share_file_path is not None:
            result['share_file_path'] = self.share_file_path
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.share_name is not None:
            result['share_name'] = self.share_name
        result['share_policy'] = []
        if self.share_policy is not None:
            for k in self.share_policy:
                result['share_policy'].append(k.to_map() if k else None)
        if self.status is not None:
            result['status'] = self.status
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        return result

    def from_map(self, map={}):
        if map.get('created_at') is not None:
            self.created_at = map.get('created_at')
        if map.get('creator') is not None:
            self.creator = map.get('creator')
        if map.get('description') is not None:
            self.description = map.get('description')
        if map.get('domain_id') is not None:
            self.domain_id = map.get('domain_id')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('expiration') is not None:
            self.expiration = map.get('expiration')
        if map.get('expired') is not None:
            self.expired = map.get('expired')
        if map.get('owner') is not None:
            self.owner = map.get('owner')
        if map.get('permissions') is not None:
            self.permissions = map.get('permissions')
        if map.get('share_file_path') is not None:
            self.share_file_path = map.get('share_file_path')
        if map.get('share_id') is not None:
            self.share_id = map.get('share_id')
        if map.get('share_name') is not None:
            self.share_name = map.get('share_name')
        self.share_policy = []
        if map.get('share_policy') is not None:
            for k in map.get('share_policy'):
                temp_model = SharePermissionPolicy()
                self.share_policy.append(temp_model.from_map(k))
        if map.get('status') is not None:
            self.status = map.get('status')
        if map.get('updated_at') is not None:
            self.updated_at = map.get('updated_at')
        return self


class GetUploadUrlResponse(TeaModel):
    """
    Get UploadUrl Response
    """
    def __init__(self, create_at=None, domain_id=None, drive_id=None, file_id=None, part_info_list=None,
                 upload_id=None):
        # created_at
        self.create_at = create_at      # type: str
        # domain_id
        self.domain_id = domain_id      # type: str
        # drive_id
        self.drive_id = drive_id        # type: str
        # file_id
        self.file_id = file_id          # type: str
        # part_info_list
        self.part_info_list = part_info_list  # type: List[UploadPartInfo]
        # upload_id
        self.upload_id = upload_id      # type: str

    def validate(self):
        if self.domain_id is not None:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z]+')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.file_id is not None:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9]{1,50}')
        if self.part_info_list:
            for k in self.part_info_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.create_at is not None:
            result['create_at'] = self.create_at
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k in self.part_info_list:
                result['part_info_list'].append(k.to_map() if k else None)
        if self.upload_id is not None:
            result['upload_id'] = self.upload_id
        return result

    def from_map(self, map={}):
        if map.get('create_at') is not None:
            self.create_at = map.get('create_at')
        if map.get('domain_id') is not None:
            self.domain_id = map.get('domain_id')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('file_id') is not None:
            self.file_id = map.get('file_id')
        self.part_info_list = []
        if map.get('part_info_list') is not None:
            for k in map.get('part_info_list'):
                temp_model = UploadPartInfo()
                self.part_info_list.append(temp_model.from_map(k))
        if map.get('upload_id') is not None:
            self.upload_id = map.get('upload_id')
        return self


class GetVideoPreviewSpriteURLResponse(TeaModel):
    """
    获取视频雪碧图地址 url response
    """
    def __init__(self, col=None, count=None, frame_count=None, frame_height=None, frame_width=None, row=None,
                 sprite_url_list=None):
        # col
        self.col = col                  # type: int
        # count
        self.count = count              # type: int
        # frame_count
        self.frame_count = frame_count  # type: int
        # frame_height
        self.frame_height = frame_height  # type: int
        # frame_width
        self.frame_width = frame_width  # type: int
        # row
        self.row = row                  # type: int
        # sprite_url_list
        self.sprite_url_list = sprite_url_list  # type: List[str]

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.col is not None:
            result['col'] = self.col
        if self.count is not None:
            result['count'] = self.count
        if self.frame_count is not None:
            result['frame_count'] = self.frame_count
        if self.frame_height is not None:
            result['frame_height'] = self.frame_height
        if self.frame_width is not None:
            result['frame_width'] = self.frame_width
        if self.row is not None:
            result['row'] = self.row
        if self.sprite_url_list is not None:
            result['sprite_url_list'] = self.sprite_url_list
        return result

    def from_map(self, map={}):
        if map.get('col') is not None:
            self.col = map.get('col')
        if map.get('count') is not None:
            self.count = map.get('count')
        if map.get('frame_count') is not None:
            self.frame_count = map.get('frame_count')
        if map.get('frame_height') is not None:
            self.frame_height = map.get('frame_height')
        if map.get('frame_width') is not None:
            self.frame_width = map.get('frame_width')
        if map.get('row') is not None:
            self.row = map.get('row')
        if map.get('sprite_url_list') is not None:
            self.sprite_url_list = map.get('sprite_url_list')
        return self


class GetVideoPreviewURLResponse(TeaModel):
    """
    获取视频文件播放 url response
    """
    def __init__(self, preview_url=None):
        # preview_url
        self.preview_url = preview_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.preview_url is not None:
            result['preview_url'] = self.preview_url
        return result

    def from_map(self, map={}):
        if map.get('preview_url') is not None:
            self.preview_url = map.get('preview_url')
        return self


class ImageMediaResponse(TeaModel):
    """
    *
    """
    def __init__(self, address_line=None, city=None, country=None, cropping_suggestion=None, district=None,
                 exif=None, faces=None, height=None, image_quality=None, image_tags=None, location=None, province=None,
                 story_image_score=None, time=None, township=None, width=None):
        # address_line
        self.address_line = address_line  # type: str
        # city
        self.city = city                # type: str
        # country
        self.country = country          # type: str
        # cropping_suggestion
        self.cropping_suggestion = cropping_suggestion  # type: List[CroppingSuggestionItem]
        # district
        self.district = district        # type: str
        # exif json string
        self.exif = exif                # type: str
        # faces json string
        self.faces = faces              # type: str
        # height
        self.height = height            # type: int
        self.image_quality = image_quality  # type: ImageQuality
        # system_tags
        self.image_tags = image_tags    # type: List[SystemTag]
        # location
        self.location = location        # type: str
        # province
        self.province = province        # type: str
        # story_image_score
        self.story_image_score = story_image_score  # type: float
        # time
        self.time = time                # type: str
        # township
        self.township = township        # type: str
        # width
        self.width = width              # type: int

    def validate(self):
        if self.cropping_suggestion:
            for k in self.cropping_suggestion:
                if k:
                    k.validate()
        if self.image_quality:
            self.image_quality.validate()
        if self.image_tags:
            for k in self.image_tags:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.address_line is not None:
            result['address_line'] = self.address_line
        if self.city is not None:
            result['city'] = self.city
        if self.country is not None:
            result['country'] = self.country
        result['cropping_suggestion'] = []
        if self.cropping_suggestion is not None:
            for k in self.cropping_suggestion:
                result['cropping_suggestion'].append(k.to_map() if k else None)
        if self.district is not None:
            result['district'] = self.district
        if self.exif is not None:
            result['exif'] = self.exif
        if self.faces is not None:
            result['faces'] = self.faces
        if self.height is not None:
            result['height'] = self.height
        if self.image_quality is not None:
            result['image_quality'] = self.image_quality.to_map()
        result['image_tags'] = []
        if self.image_tags is not None:
            for k in self.image_tags:
                result['image_tags'].append(k.to_map() if k else None)
        if self.location is not None:
            result['location'] = self.location
        if self.province is not None:
            result['province'] = self.province
        if self.story_image_score is not None:
            result['story_image_score'] = self.story_image_score
        if self.time is not None:
            result['time'] = self.time
        if self.township is not None:
            result['township'] = self.township
        if self.width is not None:
            result['width'] = self.width
        return result

    def from_map(self, map={}):
        if map.get('address_line') is not None:
            self.address_line = map.get('address_line')
        if map.get('city') is not None:
            self.city = map.get('city')
        if map.get('country') is not None:
            self.country = map.get('country')
        self.cropping_suggestion = []
        if map.get('cropping_suggestion') is not None:
            for k in map.get('cropping_suggestion'):
                temp_model = CroppingSuggestionItem()
                self.cropping_suggestion.append(temp_model.from_map(k))
        if map.get('district') is not None:
            self.district = map.get('district')
        if map.get('exif') is not None:
            self.exif = map.get('exif')
        if map.get('faces') is not None:
            self.faces = map.get('faces')
        if map.get('height') is not None:
            self.height = map.get('height')
        if map.get('image_quality') is not None:
            temp_model = ImageQuality()
            self.image_quality = temp_model.from_map(map['image_quality'])
        self.image_tags = []
        if map.get('image_tags') is not None:
            for k in map.get('image_tags'):
                temp_model = SystemTag()
                self.image_tags.append(temp_model.from_map(k))
        if map.get('location') is not None:
            self.location = map.get('location')
        if map.get('province') is not None:
            self.province = map.get('province')
        if map.get('story_image_score') is not None:
            self.story_image_score = map.get('story_image_score')
        if map.get('time') is not None:
            self.time = map.get('time')
        if map.get('township') is not None:
            self.township = map.get('township')
        if map.get('width') is not None:
            self.width = map.get('width')
        return self


class ImageQuality(TeaModel):
    """
    *
    """
    def __init__(self, clarity=None, clarity_score=None, color=None, color_score=None, composition_score=None,
                 contrast=None, contrast_score=None, exposure=None, exposure_score=None, overall_score=None):
        self.clarity = clarity          # type: float
        self.clarity_score = clarity_score  # type: float
        self.color = color              # type: float
        self.color_score = color_score  # type: float
        self.composition_score = composition_score  # type: float
        self.contrast = contrast        # type: float
        self.contrast_score = contrast_score  # type: float
        self.exposure = exposure        # type: float
        self.exposure_score = exposure_score  # type: float
        self.overall_score = overall_score  # type: float

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.clarity is not None:
            result['clarity'] = self.clarity
        if self.clarity_score is not None:
            result['clarity_score'] = self.clarity_score
        if self.color is not None:
            result['color'] = self.color
        if self.color_score is not None:
            result['color_score'] = self.color_score
        if self.composition_score is not None:
            result['composition_score'] = self.composition_score
        if self.contrast is not None:
            result['contrast'] = self.contrast
        if self.contrast_score is not None:
            result['contrast_score'] = self.contrast_score
        if self.exposure is not None:
            result['exposure'] = self.exposure
        if self.exposure_score is not None:
            result['exposure_score'] = self.exposure_score
        if self.overall_score is not None:
            result['overall_score'] = self.overall_score
        return result

    def from_map(self, map={}):
        if map.get('clarity') is not None:
            self.clarity = map.get('clarity')
        if map.get('clarity_score') is not None:
            self.clarity_score = map.get('clarity_score')
        if map.get('color') is not None:
            self.color = map.get('color')
        if map.get('color_score') is not None:
            self.color_score = map.get('color_score')
        if map.get('composition_score') is not None:
            self.composition_score = map.get('composition_score')
        if map.get('contrast') is not None:
            self.contrast = map.get('contrast')
        if map.get('contrast_score') is not None:
            self.contrast_score = map.get('contrast_score')
        if map.get('exposure') is not None:
            self.exposure = map.get('exposure')
        if map.get('exposure_score') is not None:
            self.exposure_score = map.get('exposure_score')
        if map.get('overall_score') is not None:
            self.overall_score = map.get('overall_score')
        return self


class LinkInfo(TeaModel):
    """
    *
    """
    def __init__(self, extra=None, identity=None, type=None):
        # 额外的信息，比如type为mobile时，此字段为国家编号，不填默认86
        self.extra = extra              # type: str
        # 当前用户已存在的登录标识
        self.identity = identity        # type: str
        # 当前用户已存在的登录方式
        self.type = type                # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.extra is not None:
            result['extra'] = self.extra
        if self.identity is not None:
            result['identity'] = self.identity
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, map={}):
        if map.get('extra') is not None:
            self.extra = map.get('extra')
        if map.get('identity') is not None:
            self.identity = map.get('identity')
        if map.get('type') is not None:
            self.type = map.get('type')
        return self


class LinkInfoListResponse(TeaModel):
    """
    *
    """
    def __init__(self, items=None):
        # items
        self.items = items              # type: List[LinkInfoResponse]

    def validate(self):
        self.validate_required(self.items, 'items')
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = LinkInfoResponse()
                self.items.append(temp_model.from_map(k))
        return self


class LinkInfoResponse(TeaModel):
    """
    *
    """
    def __init__(self, authentication_type=None, created_at=None, domain_id=None, extra=None, identity=None,
                 last_login_time=None, status=None, user_id=None):
        # 认证类型
        self.authentication_type = authentication_type  # type: str
        # 创建时间
        self.created_at = created_at    # type: int
        # Domain ID
        self.domain_id = domain_id      # type: str
        # 额外的信息，比如type为mobile时，此字段为国家编号，不填默认86
        self.extra = extra              # type: str
        # 唯一身份标识
        self.identity = identity        # type: str
        # 最后登录时间
        self.last_login_time = last_login_time  # type: int
        # 状态
        self.status = status            # type: str
        # 用户ID
        self.user_id = user_id          # type: str

    def validate(self):
        self.validate_required(self.authentication_type, 'authentication_type')
        self.validate_required(self.created_at, 'created_at')
        self.validate_required(self.domain_id, 'domain_id')
        self.validate_required(self.identity, 'identity')
        self.validate_required(self.last_login_time, 'last_login_time')
        self.validate_required(self.status, 'status')
        self.validate_required(self.user_id, 'user_id')

    def to_map(self):
        result = {}
        if self.authentication_type is not None:
            result['authentication_type'] = self.authentication_type
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.extra is not None:
            result['extra'] = self.extra
        if self.identity is not None:
            result['identity'] = self.identity
        if self.last_login_time is not None:
            result['last_login_time'] = self.last_login_time
        if self.status is not None:
            result['status'] = self.status
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, map={}):
        if map.get('authentication_type') is not None:
            self.authentication_type = map.get('authentication_type')
        if map.get('created_at') is not None:
            self.created_at = map.get('created_at')
        if map.get('domain_id') is not None:
            self.domain_id = map.get('domain_id')
        if map.get('extra') is not None:
            self.extra = map.get('extra')
        if map.get('identity') is not None:
            self.identity = map.get('identity')
        if map.get('last_login_time') is not None:
            self.last_login_time = map.get('last_login_time')
        if map.get('status') is not None:
            self.status = map.get('status')
        if map.get('user_id') is not None:
            self.user_id = map.get('user_id')
        return self


class ListByAnonymousResponse(TeaModel):
    """
    list_file_by_anonymous response
    """
    def __init__(self, items=None, next_marker=None):
        # items
        self.items = items              # type: List[BaseFileAnonymousResponse]
        # next_marker
        self.next_marker = next_marker  # type: str

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, map={}):
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = BaseFileAnonymousResponse()
                self.items.append(temp_model.from_map(k))
        if map.get('next_marker') is not None:
            self.next_marker = map.get('next_marker')
        return self


class ListDriveResponse(TeaModel):
    """
    list drive response
    """
    def __init__(self, items=None, next_marker=None):
        # Drive 列表
        self.items = items              # type: List[BaseDriveResponse]
        # 翻页标记
        self.next_marker = next_marker  # type: str

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, map={}):
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = BaseDriveResponse()
                self.items.append(temp_model.from_map(k))
        if map.get('next_marker') is not None:
            self.next_marker = map.get('next_marker')
        return self


class ListFileDeltaResponse(TeaModel):
    """
    list file op response
    """
    def __init__(self, cursor=None, has_more=None, items=None):
        # cursor
        self.cursor = cursor            # type: str
        # has_more
        self.has_more = has_more        # type: bool
        # items
        self.items = items              # type: List[FileDeltaResponse]

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.cursor is not None:
            result['cursor'] = self.cursor
        if self.has_more is not None:
            result['has_more'] = self.has_more
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('cursor') is not None:
            self.cursor = map.get('cursor')
        if map.get('has_more') is not None:
            self.has_more = map.get('has_more')
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = FileDeltaResponse()
                self.items.append(temp_model.from_map(k))
        return self


class ListFileResponse(TeaModel):
    """
    List file response
    """
    def __init__(self, items=None, next_marker=None):
        # items
        self.items = items              # type: List[BaseFileResponse]
        # next_marker
        self.next_marker = next_marker  # type: str

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, map={}):
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = BaseFileResponse()
                self.items.append(temp_model.from_map(k))
        if map.get('next_marker') is not None:
            self.next_marker = map.get('next_marker')
        return self


class ListShareLinkResponse(TeaModel):
    """
    list_share_link response
    """
    def __init__(self, items=None, next_marker=None):
        # items
        self.items = items              # type: List[BaseShareLinkResponse]
        # next_marker
        self.next_marker = next_marker  # type: str

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, map={}):
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = BaseShareLinkResponse()
                self.items.append(temp_model.from_map(k))
        if map.get('next_marker') is not None:
            self.next_marker = map.get('next_marker')
        return self


class ListShareResponse(TeaModel):
    """
    List share response
    """
    def __init__(self, items=None, next_marker=None):
        # items
        self.items = items              # type: List[BaseShareResponse]
        # next_marker
        self.next_marker = next_marker  # type: str

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, map={}):
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = BaseShareResponse()
                self.items.append(temp_model.from_map(k))
        if map.get('next_marker') is not None:
            self.next_marker = map.get('next_marker')
        return self


class ListStoreFileResponse(TeaModel):
    """
    List storage file
    """
    def __init__(self, items=None, next_marker=None):
        # items
        # file list
        self.items = items              # type: List[StoreFile]
        self.next_marker = next_marker  # type: str

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, map={}):
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = StoreFile()
                self.items.append(temp_model.from_map(k))
        if map.get('next_marker') is not None:
            self.next_marker = map.get('next_marker')
        return self


class ListStoreResponse(TeaModel):
    """
    List storage
    """
    def __init__(self, items=None):
        # items
        self.items = items              # type: List[StoreItemResponse]

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = StoreItemResponse()
                self.items.append(temp_model.from_map(k))
        return self


class ListUploadedPartResponse(TeaModel):
    """
    获取签名 response
    """
    def __init__(self, file_id=None, next_part_number_marker=None, upload_id=None, uploaded_parts=None):
        # file_id
        self.file_id = file_id          # type: str
        # next_part_number_marker
        self.next_part_number_marker = next_part_number_marker  # type: str
        # upload_id
        self.upload_id = upload_id      # type: str
        # uploaded_parts
        self.uploaded_parts = uploaded_parts  # type: List[UploadPartInfo]

    def validate(self):
        if self.file_id is not None:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9]{1,50}')
        if self.uploaded_parts:
            for k in self.uploaded_parts:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.next_part_number_marker is not None:
            result['next_part_number_marker'] = self.next_part_number_marker
        if self.upload_id is not None:
            result['upload_id'] = self.upload_id
        result['uploaded_parts'] = []
        if self.uploaded_parts is not None:
            for k in self.uploaded_parts:
                result['uploaded_parts'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('file_id') is not None:
            self.file_id = map.get('file_id')
        if map.get('next_part_number_marker') is not None:
            self.next_part_number_marker = map.get('next_part_number_marker')
        if map.get('upload_id') is not None:
            self.upload_id = map.get('upload_id')
        self.uploaded_parts = []
        if map.get('uploaded_parts') is not None:
            for k in map.get('uploaded_parts'):
                temp_model = UploadPartInfo()
                self.uploaded_parts.append(temp_model.from_map(k))
        return self


class LoginByCodeRequest(TeaModel):
    """
    *
    """
    def __init__(self, access_token=None, app_id=None, auth_code=None, type=None):
        # 鉴权后返回的accessToken，淘宝登录需要此字段
        self.access_token = access_token  # type: str
        # App ID, 当前访问的App
        self.app_id = app_id            # type: str
        # 鉴权后返回的AuthCode，支付宝登录需要此字段
        self.auth_code = auth_code      # type: str
        # 鉴权类型，淘宝、支付宝
        self.type = type                # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.type, 'type')

    def to_map(self):
        result = {}
        if self.access_token is not None:
            result['access_token'] = self.access_token
        if self.app_id is not None:
            result['app_id'] = self.app_id
        if self.auth_code is not None:
            result['auth_code'] = self.auth_code
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, map={}):
        if map.get('access_token') is not None:
            self.access_token = map.get('access_token')
        if map.get('app_id') is not None:
            self.app_id = map.get('app_id')
        if map.get('auth_code') is not None:
            self.auth_code = map.get('auth_code')
        if map.get('type') is not None:
            self.type = map.get('type')
        return self


class MobileCheckExistRequest(TeaModel):
    """
    *
    """
    def __init__(self, headers=None, app_id=None, phone_number=None, phone_region=None):
        self.headers = headers          # type: Dict[str, str]
        # App ID, 当前访问的App
        self.app_id = app_id            # type: str
        # 待查询的手机号
        self.phone_number = phone_number  # type: str
        # 国家编号，默认86，不需要填+号，直接填数字
        self.phone_region = phone_region  # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.phone_number, 'phone_number')

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.app_id is not None:
            result['app_id'] = self.app_id
        if self.phone_number is not None:
            result['phone_number'] = self.phone_number
        if self.phone_region is not None:
            result['phone_region'] = self.phone_region
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('app_id') is not None:
            self.app_id = map.get('app_id')
        if map.get('phone_number') is not None:
            self.phone_number = map.get('phone_number')
        if map.get('phone_region') is not None:
            self.phone_region = map.get('phone_region')
        return self


class MobileCheckExistResponse(TeaModel):
    """
    *
    """
    def __init__(self, is_exist=None, phone_number=None, phone_region=None):
        # 当前手机号是否存在
        self.is_exist = is_exist        # type: bool
        # 待查询的手机号
        self.phone_number = phone_number  # type: str
        # 国家编号，默认86，不需要填+号，直接填数字
        self.phone_region = phone_region  # type: str

    def validate(self):
        self.validate_required(self.is_exist, 'is_exist')
        self.validate_required(self.phone_number, 'phone_number')

    def to_map(self):
        result = {}
        if self.is_exist is not None:
            result['is_exist'] = self.is_exist
        if self.phone_number is not None:
            result['phone_number'] = self.phone_number
        if self.phone_region is not None:
            result['phone_region'] = self.phone_region
        return result

    def from_map(self, map={}):
        if map.get('is_exist') is not None:
            self.is_exist = map.get('is_exist')
        if map.get('phone_number') is not None:
            self.phone_number = map.get('phone_number')
        if map.get('phone_region') is not None:
            self.phone_region = map.get('phone_region')
        return self


class MobileLoginRequest(TeaModel):
    """
    *
    """
    def __init__(self, headers=None, app_id=None, auto_register=None, captcha_id=None, captcha_text=None,
                 encrypted_key=None, password=None, phone_number=None, phone_region=None, sms_code=None, sms_code_id=None):
        self.headers = headers          # type: Dict[str, str]
        # App ID, 当前访问的App
        self.app_id = app_id            # type: str
        # 是否自动注册用户，使用密码登录此参数不生效
        self.auto_register = auto_register  # type: bool
        # 图片验证码ID, 密码登录需要此参数
        self.captcha_id = captcha_id    # type: str
        # 用户输入的验证码值, 密码登录需要此参数
        self.captcha_text = captcha_text  # type: str
        # AES-256对称加密密钥，通过App公钥加密后传输
        self.encrypted_key = encrypted_key  # type: str
        # 登录密码, 传入此参数则忽略短信验证码，不传此参数则默认使用短信登录。
        self.password = password        # type: str
        # 待查询的手机号
        self.phone_number = phone_number  # type: str
        # 国家编号，默认86，不需要填+号，直接填数字
        self.phone_region = phone_region  # type: str
        # 短信验证码内容，使用密码登录此参数不生效
        self.sms_code = sms_code        # type: str
        # 短信验证码ID，使用密码登录此参数不生效
        self.sms_code_id = sms_code_id  # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.phone_number, 'phone_number')

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.app_id is not None:
            result['app_id'] = self.app_id
        if self.auto_register is not None:
            result['auto_register'] = self.auto_register
        if self.captcha_id is not None:
            result['captcha_id'] = self.captcha_id
        if self.captcha_text is not None:
            result['captcha_text'] = self.captcha_text
        if self.encrypted_key is not None:
            result['encrypted_key'] = self.encrypted_key
        if self.password is not None:
            result['password'] = self.password
        if self.phone_number is not None:
            result['phone_number'] = self.phone_number
        if self.phone_region is not None:
            result['phone_region'] = self.phone_region
        if self.sms_code is not None:
            result['sms_code'] = self.sms_code
        if self.sms_code_id is not None:
            result['sms_code_id'] = self.sms_code_id
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('app_id') is not None:
            self.app_id = map.get('app_id')
        if map.get('auto_register') is not None:
            self.auto_register = map.get('auto_register')
        if map.get('captcha_id') is not None:
            self.captcha_id = map.get('captcha_id')
        if map.get('captcha_text') is not None:
            self.captcha_text = map.get('captcha_text')
        if map.get('encrypted_key') is not None:
            self.encrypted_key = map.get('encrypted_key')
        if map.get('password') is not None:
            self.password = map.get('password')
        if map.get('phone_number') is not None:
            self.phone_number = map.get('phone_number')
        if map.get('phone_region') is not None:
            self.phone_region = map.get('phone_region')
        if map.get('sms_code') is not None:
            self.sms_code = map.get('sms_code')
        if map.get('sms_code_id') is not None:
            self.sms_code_id = map.get('sms_code_id')
        return self


class MobileRegisterRequest(TeaModel):
    """
    *
    """
    def __init__(self, headers=None, app_id=None, phone_number=None, phone_region=None, sms_code=None,
                 sms_code_id=None):
        self.headers = headers          # type: Dict[str, str]
        # App ID, 当前访问的App
        self.app_id = app_id            # type: str
        # 待查询的手机号
        self.phone_number = phone_number  # type: str
        # 国家编号，默认86，不需要填+号，直接填数字
        self.phone_region = phone_region  # type: str
        # 短信验证码内容
        self.sms_code = sms_code        # type: str
        # 短信验证码ID
        self.sms_code_id = sms_code_id  # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.phone_number, 'phone_number')
        self.validate_required(self.sms_code, 'sms_code')
        self.validate_required(self.sms_code_id, 'sms_code_id')

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.app_id is not None:
            result['app_id'] = self.app_id
        if self.phone_number is not None:
            result['phone_number'] = self.phone_number
        if self.phone_region is not None:
            result['phone_region'] = self.phone_region
        if self.sms_code is not None:
            result['sms_code'] = self.sms_code
        if self.sms_code_id is not None:
            result['sms_code_id'] = self.sms_code_id
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('app_id') is not None:
            self.app_id = map.get('app_id')
        if map.get('phone_number') is not None:
            self.phone_number = map.get('phone_number')
        if map.get('phone_region') is not None:
            self.phone_region = map.get('phone_region')
        if map.get('sms_code') is not None:
            self.sms_code = map.get('sms_code')
        if map.get('sms_code_id') is not None:
            self.sms_code_id = map.get('sms_code_id')
        return self


class MobileSendSmsCodeRequest(TeaModel):
    """
    *
    """
    def __init__(self, headers=None, app_id=None, captcha_id=None, captcha_text=None, phone_number=None,
                 phone_region=None, type=None):
        self.headers = headers          # type: Dict[str, str]
        # App ID, 当前访问的App
        self.app_id = app_id            # type: str
        # 图片验证码ID
        self.captcha_id = captcha_id    # type: str
        # 用户输入的验证码值
        self.captcha_text = captcha_text  # type: str
        # 待发送验证短信的手机号
        self.phone_number = phone_number  # type: str
        # 国家编号，默认86，不需要填+号，直接填数字
        self.phone_region = phone_region  # type: str
        # 验证码用途, 可下发: login、register、change_password
        self.type = type                # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.phone_number, 'phone_number')
        self.validate_required(self.type, 'type')

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.app_id is not None:
            result['app_id'] = self.app_id
        if self.captcha_id is not None:
            result['captcha_id'] = self.captcha_id
        if self.captcha_text is not None:
            result['captcha_text'] = self.captcha_text
        if self.phone_number is not None:
            result['phone_number'] = self.phone_number
        if self.phone_region is not None:
            result['phone_region'] = self.phone_region
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('app_id') is not None:
            self.app_id = map.get('app_id')
        if map.get('captcha_id') is not None:
            self.captcha_id = map.get('captcha_id')
        if map.get('captcha_text') is not None:
            self.captcha_text = map.get('captcha_text')
        if map.get('phone_number') is not None:
            self.phone_number = map.get('phone_number')
        if map.get('phone_region') is not None:
            self.phone_region = map.get('phone_region')
        if map.get('type') is not None:
            self.type = map.get('type')
        return self


class MobileSendSmsCodeResponse(TeaModel):
    """
    *
    """
    def __init__(self, sms_code_id=None):
        # 短信验证码ID
        self.sms_code_id = sms_code_id  # type: str

    def validate(self):
        self.validate_required(self.sms_code_id, 'sms_code_id')

    def to_map(self):
        result = {}
        if self.sms_code_id is not None:
            result['sms_code_id'] = self.sms_code_id
        return result

    def from_map(self, map={}):
        if map.get('sms_code_id') is not None:
            self.sms_code_id = map.get('sms_code_id')
        return self


class MoveFileResponse(TeaModel):
    """
    文件移动 response
    """
    def __init__(self, async_task_id=None, domain_id=None, drive_id=None, file_id=None):
        # async_task_id
        self.async_task_id = async_task_id  # type: str
        # DomainID
        self.domain_id = domain_id      # type: str
        # drive_id
        self.drive_id = drive_id        # type: str
        # file_id
        self.file_id = file_id          # type: str

    def validate(self):
        if self.domain_id is not None:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z]+')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.file_id is not None:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9]{1,50}')

    def to_map(self):
        result = {}
        if self.async_task_id is not None:
            result['async_task_id'] = self.async_task_id
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        return result

    def from_map(self, map={}):
        if map.get('async_task_id') is not None:
            self.async_task_id = map.get('async_task_id')
        if map.get('domain_id') is not None:
            self.domain_id = map.get('domain_id')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('file_id') is not None:
            self.file_id = map.get('file_id')
        return self


class OSSCompleteFileResponse(TeaModel):
    """
    complete file response
    """
    def __init__(self, content_hash=None, content_hash_name=None, content_type=None, crc=None, crc_64hash=None,
                 created_at=None, description=None, domain_id=None, download_url=None, drive_id=None, file_extension=None,
                 file_path=None, name=None, parent_file_path=None, share_id=None, size=None, status=None, thumbnail=None,
                 trashed_at=None, type=None, updated_at=None, upload_id=None, url=None):
        # Content Hash
        self.content_hash = content_hash  # type: str
        # content_hash_name
        self.content_hash_name = content_hash_name  # type: str
        # content_type
        self.content_type = content_type  # type: str
        # crc
        self.crc = crc                  # type: str
        # crc64_hash
        self.crc_64hash = crc_64hash    # type: str
        # created_at
        self.created_at = created_at    # type: str
        # description
        self.description = description  # type: str
        # domain_id
        self.domain_id = domain_id      # type: str
        # download_url
        self.download_url = download_url  # type: str
        # drive_id
        self.drive_id = drive_id        # type: str
        # file_extension
        self.file_extension = file_extension  # type: str
        # file_path
        self.file_path = file_path      # type: str
        # name
        self.name = name                # type: str
        # parent_file_id
        self.parent_file_path = parent_file_path  # type: str
        # share_id
        self.share_id = share_id        # type: str
        # Size
        self.size = size                # type: int
        # status
        self.status = status            # type: str
        # thumbnail
        self.thumbnail = thumbnail      # type: str
        # trashed_at
        self.trashed_at = trashed_at    # type: str
        # type
        self.type = type                # type: str
        # updated_at
        self.updated_at = updated_at    # type: str
        # upload_id
        self.upload_id = upload_id      # type: str
        # url
        self.url = url                  # type: str

    def validate(self):
        if self.domain_id is not None:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z]+')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.name, 'name')
        if self.name is not None:
            self.validate_pattern(self.name, 'name', '[a-zA-Z0-9.-]{1,1000}')
        if self.parent_file_path is not None:
            self.validate_max_length(self.parent_file_path, 'parent_file_path', 50)
            self.validate_pattern(self.parent_file_path, 'parent_file_path', '[a-z0-9]{1,50}')
        if self.share_id is not None:
            self.validate_pattern(self.share_id, 'share_id', '[0-9]+')
        if self.size is not None:
            self.validate_maximum(self.size, 'size', 53687091200)
            self.validate_minimum(self.size, 'size', 0)

    def to_map(self):
        result = {}
        if self.content_hash is not None:
            result['content_hash'] = self.content_hash
        if self.content_hash_name is not None:
            result['content_hash_name'] = self.content_hash_name
        if self.content_type is not None:
            result['content_type'] = self.content_type
        if self.crc is not None:
            result['crc'] = self.crc
        if self.crc_64hash is not None:
            result['crc64_hash'] = self.crc_64hash
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.download_url is not None:
            result['download_url'] = self.download_url
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_extension is not None:
            result['file_extension'] = self.file_extension
        if self.file_path is not None:
            result['file_path'] = self.file_path
        if self.name is not None:
            result['name'] = self.name
        if self.parent_file_path is not None:
            result['parent_file_path'] = self.parent_file_path
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.size is not None:
            result['size'] = self.size
        if self.status is not None:
            result['status'] = self.status
        if self.thumbnail is not None:
            result['thumbnail'] = self.thumbnail
        if self.trashed_at is not None:
            result['trashed_at'] = self.trashed_at
        if self.type is not None:
            result['type'] = self.type
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        if self.upload_id is not None:
            result['upload_id'] = self.upload_id
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, map={}):
        if map.get('content_hash') is not None:
            self.content_hash = map.get('content_hash')
        if map.get('content_hash_name') is not None:
            self.content_hash_name = map.get('content_hash_name')
        if map.get('content_type') is not None:
            self.content_type = map.get('content_type')
        if map.get('crc') is not None:
            self.crc = map.get('crc')
        if map.get('crc64_hash') is not None:
            self.crc_64hash = map.get('crc64_hash')
        if map.get('created_at') is not None:
            self.created_at = map.get('created_at')
        if map.get('description') is not None:
            self.description = map.get('description')
        if map.get('domain_id') is not None:
            self.domain_id = map.get('domain_id')
        if map.get('download_url') is not None:
            self.download_url = map.get('download_url')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('file_extension') is not None:
            self.file_extension = map.get('file_extension')
        if map.get('file_path') is not None:
            self.file_path = map.get('file_path')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('parent_file_path') is not None:
            self.parent_file_path = map.get('parent_file_path')
        if map.get('share_id') is not None:
            self.share_id = map.get('share_id')
        if map.get('size') is not None:
            self.size = map.get('size')
        if map.get('status') is not None:
            self.status = map.get('status')
        if map.get('thumbnail') is not None:
            self.thumbnail = map.get('thumbnail')
        if map.get('trashed_at') is not None:
            self.trashed_at = map.get('trashed_at')
        if map.get('type') is not None:
            self.type = map.get('type')
        if map.get('updated_at') is not None:
            self.updated_at = map.get('updated_at')
        if map.get('upload_id') is not None:
            self.upload_id = map.get('upload_id')
        if map.get('url') is not None:
            self.url = map.get('url')
        return self


class OSSCopyFileResponse(TeaModel):
    """
    文件拷贝 response
    """
    def __init__(self, async_task_id=None, domain_id=None, drive_id=None, file_path=None, share_id=None):
        # async_task_id
        self.async_task_id = async_task_id  # type: str
        # domain_id
        self.domain_id = domain_id      # type: str
        # drive_id
        self.drive_id = drive_id        # type: str
        # file_path
        self.file_path = file_path      # type: str
        # drive_id
        self.share_id = share_id        # type: str

    def validate(self):
        if self.domain_id is not None:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z-]+')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.share_id is not None:
            self.validate_pattern(self.share_id, 'share_id', '[a-z0-9A-Z]+')

    def to_map(self):
        result = {}
        if self.async_task_id is not None:
            result['async_task_id'] = self.async_task_id
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_path is not None:
            result['file_path'] = self.file_path
        if self.share_id is not None:
            result['share_id'] = self.share_id
        return result

    def from_map(self, map={}):
        if map.get('async_task_id') is not None:
            self.async_task_id = map.get('async_task_id')
        if map.get('domain_id') is not None:
            self.domain_id = map.get('domain_id')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('file_path') is not None:
            self.file_path = map.get('file_path')
        if map.get('share_id') is not None:
            self.share_id = map.get('share_id')
        return self


class OSSCreateFileResponse(TeaModel):
    """
    Create file response
    """
    def __init__(self, domain_id=None, drive_id=None, file_path=None, part_info_list=None, share_id=None, type=None,
                 upload_id=None):
        # domain_id
        self.domain_id = domain_id      # type: str
        # drive_id
        self.drive_id = drive_id        # type: str
        # file_path
        self.file_path = file_path      # type: str
        # part_info_list
        self.part_info_list = part_info_list  # type: List[UploadPartInfo]
        # share_id
        self.share_id = share_id        # type: str
        # type
        self.type = type                # type: str
        # upload_id
        self.upload_id = upload_id      # type: str

    def validate(self):
        if self.domain_id is not None:
            self.validate_max_length(self.domain_id, 'domain_id', 50)
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9]{1,50}')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.part_info_list:
            for k in self.part_info_list:
                if k:
                    k.validate()
        if self.share_id is not None:
            self.validate_pattern(self.share_id, 'share_id', '[0-9]+')

    def to_map(self):
        result = {}
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_path is not None:
            result['file_path'] = self.file_path
        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k in self.part_info_list:
                result['part_info_list'].append(k.to_map() if k else None)
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.type is not None:
            result['type'] = self.type
        if self.upload_id is not None:
            result['upload_id'] = self.upload_id
        return result

    def from_map(self, map={}):
        if map.get('domain_id') is not None:
            self.domain_id = map.get('domain_id')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('file_path') is not None:
            self.file_path = map.get('file_path')
        self.part_info_list = []
        if map.get('part_info_list') is not None:
            for k in map.get('part_info_list'):
                temp_model = UploadPartInfo()
                self.part_info_list.append(temp_model.from_map(k))
        if map.get('share_id') is not None:
            self.share_id = map.get('share_id')
        if map.get('type') is not None:
            self.type = map.get('type')
        if map.get('upload_id') is not None:
            self.upload_id = map.get('upload_id')
        return self


class OSSDeleteFileResponse(TeaModel):
    """
    删除文件 response
    """
    def __init__(self, async_task_id=None, domain_id=None, drive_id=None, file_path=None, share_id=None):
        # async_task_id
        self.async_task_id = async_task_id  # type: str
        # domain_id
        self.domain_id = domain_id      # type: str
        # drive_id
        self.drive_id = drive_id        # type: str
        # file_path
        self.file_path = file_path      # type: str
        # share_id
        self.share_id = share_id        # type: str

    def validate(self):
        if self.domain_id is not None:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z]+')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.share_id is not None:
            self.validate_pattern(self.share_id, 'share_id', '[a-z0-9A-Z]+')

    def to_map(self):
        result = {}
        if self.async_task_id is not None:
            result['async_task_id'] = self.async_task_id
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_path is not None:
            result['file_path'] = self.file_path
        if self.share_id is not None:
            result['share_id'] = self.share_id
        return result

    def from_map(self, map={}):
        if map.get('async_task_id') is not None:
            self.async_task_id = map.get('async_task_id')
        if map.get('domain_id') is not None:
            self.domain_id = map.get('domain_id')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('file_path') is not None:
            self.file_path = map.get('file_path')
        if map.get('share_id') is not None:
            self.share_id = map.get('share_id')
        return self


class OSSDeleteFilesResponse(TeaModel):
    """
    批量删除文件 response
    """
    def __init__(self, deleted_file_id_list=None, domain_id=None, drive_id=None, share_id=None):
        # deleted_file_id_list
        self.deleted_file_id_list = deleted_file_id_list  # type: List[str]
        # domain_id
        self.domain_id = domain_id      # type: str
        # drive_id
        self.drive_id = drive_id        # type: str
        # share_id
        self.share_id = share_id        # type: str

    def validate(self):
        if self.domain_id is not None:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z]+')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.share_id is not None:
            self.validate_pattern(self.share_id, 'share_id', '[0-9]+')

    def to_map(self):
        result = {}
        if self.deleted_file_id_list is not None:
            result['deleted_file_id_list'] = self.deleted_file_id_list
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.share_id is not None:
            result['share_id'] = self.share_id
        return result

    def from_map(self, map={}):
        if map.get('deleted_file_id_list') is not None:
            self.deleted_file_id_list = map.get('deleted_file_id_list')
        if map.get('domain_id') is not None:
            self.domain_id = map.get('domain_id')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('share_id') is not None:
            self.share_id = map.get('share_id')
        return self


class OSSGetDownloadUrlResponse(TeaModel):
    """
    获取download url response
    """
    def __init__(self, expiration=None, method=None, url=None):
        # expiration
        self.expiration = expiration    # type: str
        # method
        self.method = method            # type: str
        # url
        self.url = url                  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.expiration is not None:
            result['expiration'] = self.expiration
        if self.method is not None:
            result['method'] = self.method
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, map={}):
        if map.get('expiration') is not None:
            self.expiration = map.get('expiration')
        if map.get('method') is not None:
            self.method = map.get('method')
        if map.get('url') is not None:
            self.url = map.get('url')
        return self


class OSSGetFileResponse(TeaModel):
    """
    获取文件元数据response
    """
    def __init__(self, content_hash=None, content_hash_name=None, content_type=None, crc_64hash=None,
                 created_at=None, description=None, domain_id=None, download_url=None, drive_id=None, file_extension=None,
                 file_path=None, name=None, parent_file_path=None, share_id=None, size=None, status=None, thumbnail=None,
                 trashed_at=None, type=None, updated_at=None, upload_id=None, url=None):
        # Content Hash
        self.content_hash = content_hash  # type: str
        # content_hash_name
        self.content_hash_name = content_hash_name  # type: str
        # content_type
        self.content_type = content_type  # type: str
        # crc64_hash
        self.crc_64hash = crc_64hash    # type: str
        # created_at
        self.created_at = created_at    # type: str
        # description
        self.description = description  # type: str
        # domain_id
        self.domain_id = domain_id      # type: str
        # download_url
        self.download_url = download_url  # type: str
        # drive_id
        self.drive_id = drive_id        # type: str
        # file_extension
        self.file_extension = file_extension  # type: str
        # file_path
        self.file_path = file_path      # type: str
        # name
        self.name = name                # type: str
        # parent_file_id
        self.parent_file_path = parent_file_path  # type: str
        # share_id
        self.share_id = share_id        # type: str
        # Size
        self.size = size                # type: int
        # status
        self.status = status            # type: str
        # thumbnail
        self.thumbnail = thumbnail      # type: str
        # trashed_at
        self.trashed_at = trashed_at    # type: str
        # type
        self.type = type                # type: str
        # updated_at
        self.updated_at = updated_at    # type: str
        # upload_id
        self.upload_id = upload_id      # type: str
        # url
        self.url = url                  # type: str

    def validate(self):
        if self.domain_id is not None:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z]+')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.name, 'name')
        if self.name is not None:
            self.validate_pattern(self.name, 'name', '[a-zA-Z0-9.-]{1,1000}')
        if self.parent_file_path is not None:
            self.validate_max_length(self.parent_file_path, 'parent_file_path', 50)
            self.validate_pattern(self.parent_file_path, 'parent_file_path', '[a-z0-9]{1,50}')
        if self.share_id is not None:
            self.validate_pattern(self.share_id, 'share_id', '[0-9]+')
        if self.size is not None:
            self.validate_maximum(self.size, 'size', 53687091200)
            self.validate_minimum(self.size, 'size', 0)

    def to_map(self):
        result = {}
        if self.content_hash is not None:
            result['content_hash'] = self.content_hash
        if self.content_hash_name is not None:
            result['content_hash_name'] = self.content_hash_name
        if self.content_type is not None:
            result['content_type'] = self.content_type
        if self.crc_64hash is not None:
            result['crc64_hash'] = self.crc_64hash
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.download_url is not None:
            result['download_url'] = self.download_url
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_extension is not None:
            result['file_extension'] = self.file_extension
        if self.file_path is not None:
            result['file_path'] = self.file_path
        if self.name is not None:
            result['name'] = self.name
        if self.parent_file_path is not None:
            result['parent_file_path'] = self.parent_file_path
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.size is not None:
            result['size'] = self.size
        if self.status is not None:
            result['status'] = self.status
        if self.thumbnail is not None:
            result['thumbnail'] = self.thumbnail
        if self.trashed_at is not None:
            result['trashed_at'] = self.trashed_at
        if self.type is not None:
            result['type'] = self.type
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        if self.upload_id is not None:
            result['upload_id'] = self.upload_id
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, map={}):
        if map.get('content_hash') is not None:
            self.content_hash = map.get('content_hash')
        if map.get('content_hash_name') is not None:
            self.content_hash_name = map.get('content_hash_name')
        if map.get('content_type') is not None:
            self.content_type = map.get('content_type')
        if map.get('crc64_hash') is not None:
            self.crc_64hash = map.get('crc64_hash')
        if map.get('created_at') is not None:
            self.created_at = map.get('created_at')
        if map.get('description') is not None:
            self.description = map.get('description')
        if map.get('domain_id') is not None:
            self.domain_id = map.get('domain_id')
        if map.get('download_url') is not None:
            self.download_url = map.get('download_url')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('file_extension') is not None:
            self.file_extension = map.get('file_extension')
        if map.get('file_path') is not None:
            self.file_path = map.get('file_path')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('parent_file_path') is not None:
            self.parent_file_path = map.get('parent_file_path')
        if map.get('share_id') is not None:
            self.share_id = map.get('share_id')
        if map.get('size') is not None:
            self.size = map.get('size')
        if map.get('status') is not None:
            self.status = map.get('status')
        if map.get('thumbnail') is not None:
            self.thumbnail = map.get('thumbnail')
        if map.get('trashed_at') is not None:
            self.trashed_at = map.get('trashed_at')
        if map.get('type') is not None:
            self.type = map.get('type')
        if map.get('updated_at') is not None:
            self.updated_at = map.get('updated_at')
        if map.get('upload_id') is not None:
            self.upload_id = map.get('upload_id')
        if map.get('url') is not None:
            self.url = map.get('url')
        return self


class OSSGetSecureUrlResponse(TeaModel):
    """
    获取secure url response
    """
    def __init__(self, expiration=None, url=None):
        # expiration
        self.expiration = expiration    # type: str
        # url
        self.url = url                  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.expiration is not None:
            result['expiration'] = self.expiration
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, map={}):
        if map.get('expiration') is not None:
            self.expiration = map.get('expiration')
        if map.get('url') is not None:
            self.url = map.get('url')
        return self


class OSSGetUploadUrlResponse(TeaModel):
    """
    Get UploadUrl Response
    """
    def __init__(self, create_at=None, domain_id=None, drive_id=None, file_path=None, part_info_list=None,
                 upload_id=None):
        # created_at
        self.create_at = create_at      # type: str
        # domain_id
        self.domain_id = domain_id      # type: str
        # drive_id
        self.drive_id = drive_id        # type: str
        # file_path
        self.file_path = file_path      # type: str
        # part_info_list
        self.part_info_list = part_info_list  # type: List[UploadPartInfo]
        # upload_id
        self.upload_id = upload_id      # type: str

    def validate(self):
        if self.domain_id is not None:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z]+')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.part_info_list:
            for k in self.part_info_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.create_at is not None:
            result['create_at'] = self.create_at
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_path is not None:
            result['file_path'] = self.file_path
        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k in self.part_info_list:
                result['part_info_list'].append(k.to_map() if k else None)
        if self.upload_id is not None:
            result['upload_id'] = self.upload_id
        return result

    def from_map(self, map={}):
        if map.get('create_at') is not None:
            self.create_at = map.get('create_at')
        if map.get('domain_id') is not None:
            self.domain_id = map.get('domain_id')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('file_path') is not None:
            self.file_path = map.get('file_path')
        self.part_info_list = []
        if map.get('part_info_list') is not None:
            for k in map.get('part_info_list'):
                temp_model = UploadPartInfo()
                self.part_info_list.append(temp_model.from_map(k))
        if map.get('upload_id') is not None:
            self.upload_id = map.get('upload_id')
        return self


class OSSListFileResponse(TeaModel):
    """
    List file response
    """
    def __init__(self, items=None, next_marker=None):
        # items
        self.items = items              # type: List[BaseOSSFileResponse]
        # next_marker
        self.next_marker = next_marker  # type: str

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, map={}):
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = BaseOSSFileResponse()
                self.items.append(temp_model.from_map(k))
        if map.get('next_marker') is not None:
            self.next_marker = map.get('next_marker')
        return self


class OSSListUploadedPartResponse(TeaModel):
    """
    获取签名 response
    """
    def __init__(self, file_path=None, next_part_number_marker=None, upload_id=None, uploaded_parts=None):
        # file_path
        self.file_path = file_path      # type: str
        # next_part_number_marker
        self.next_part_number_marker = next_part_number_marker  # type: str
        # upload_id
        self.upload_id = upload_id      # type: str
        # uploaded_parts
        self.uploaded_parts = uploaded_parts  # type: List[UploadPartInfo]

    def validate(self):
        if self.uploaded_parts:
            for k in self.uploaded_parts:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.file_path is not None:
            result['file_path'] = self.file_path
        if self.next_part_number_marker is not None:
            result['next_part_number_marker'] = self.next_part_number_marker
        if self.upload_id is not None:
            result['upload_id'] = self.upload_id
        result['uploaded_parts'] = []
        if self.uploaded_parts is not None:
            for k in self.uploaded_parts:
                result['uploaded_parts'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('file_path') is not None:
            self.file_path = map.get('file_path')
        if map.get('next_part_number_marker') is not None:
            self.next_part_number_marker = map.get('next_part_number_marker')
        if map.get('upload_id') is not None:
            self.upload_id = map.get('upload_id')
        self.uploaded_parts = []
        if map.get('uploaded_parts') is not None:
            for k in map.get('uploaded_parts'):
                temp_model = UploadPartInfo()
                self.uploaded_parts.append(temp_model.from_map(k))
        return self


class OSSMoveFileResponse(TeaModel):
    """
    文件移动 response
    """
    def __init__(self, async_task_id=None, domain_id=None, drive_id=None, file_path=None, share_id=None):
        # async_task_id
        self.async_task_id = async_task_id  # type: str
        # domain_id
        self.domain_id = domain_id      # type: str
        # drive_id
        self.drive_id = drive_id        # type: str
        # file_path
        self.file_path = file_path      # type: str
        # drive_id
        self.share_id = share_id        # type: str

    def validate(self):
        if self.domain_id is not None:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z-]+')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.share_id is not None:
            self.validate_pattern(self.share_id, 'share_id', '[a-z0-9A-Z]+')

    def to_map(self):
        result = {}
        if self.async_task_id is not None:
            result['async_task_id'] = self.async_task_id
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_path is not None:
            result['file_path'] = self.file_path
        if self.share_id is not None:
            result['share_id'] = self.share_id
        return result

    def from_map(self, map={}):
        if map.get('async_task_id') is not None:
            self.async_task_id = map.get('async_task_id')
        if map.get('domain_id') is not None:
            self.domain_id = map.get('domain_id')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('file_path') is not None:
            self.file_path = map.get('file_path')
        if map.get('share_id') is not None:
            self.share_id = map.get('share_id')
        return self


class OSSSearchFileResponse(TeaModel):
    """
    search file response
    """
    def __init__(self, items=None, next_marker=None):
        # items
        self.items = items              # type: List[BaseOSSFileResponse]
        # next_marker
        self.next_marker = next_marker  # type: str

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, map={}):
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = BaseOSSFileResponse()
                self.items.append(temp_model.from_map(k))
        if map.get('next_marker') is not None:
            self.next_marker = map.get('next_marker')
        return self


class OSSUpdateFileMetaResponse(TeaModel):
    """
    更新文件元数据 response
    """
    def __init__(self, content_hash=None, content_hash_name=None, content_type=None, crc_64hash=None,
                 created_at=None, description=None, domain_id=None, download_url=None, drive_id=None, file_extension=None,
                 file_path=None, name=None, parent_file_path=None, share_id=None, size=None, status=None, thumbnail=None,
                 trashed_at=None, type=None, updated_at=None, upload_id=None, url=None):
        # Content Hash
        self.content_hash = content_hash  # type: str
        # content_hash_name
        self.content_hash_name = content_hash_name  # type: str
        # content_type
        self.content_type = content_type  # type: str
        # crc64_hash
        self.crc_64hash = crc_64hash    # type: str
        # created_at
        self.created_at = created_at    # type: str
        # description
        self.description = description  # type: str
        # domain_id
        self.domain_id = domain_id      # type: str
        # download_url
        self.download_url = download_url  # type: str
        # drive_id
        self.drive_id = drive_id        # type: str
        # file_extension
        self.file_extension = file_extension  # type: str
        # file_path
        self.file_path = file_path      # type: str
        # name
        self.name = name                # type: str
        # parent_file_id
        self.parent_file_path = parent_file_path  # type: str
        # share_id
        self.share_id = share_id        # type: str
        # Size
        self.size = size                # type: int
        # status
        self.status = status            # type: str
        # thumbnail
        self.thumbnail = thumbnail      # type: str
        # trashed_at
        self.trashed_at = trashed_at    # type: str
        # type
        self.type = type                # type: str
        # updated_at
        self.updated_at = updated_at    # type: str
        # upload_id
        self.upload_id = upload_id      # type: str
        # url
        self.url = url                  # type: str

    def validate(self):
        if self.domain_id is not None:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z]+')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.name, 'name')
        if self.name is not None:
            self.validate_pattern(self.name, 'name', '[a-zA-Z0-9.-]{1,1000}')
        if self.parent_file_path is not None:
            self.validate_max_length(self.parent_file_path, 'parent_file_path', 50)
            self.validate_pattern(self.parent_file_path, 'parent_file_path', '[a-z0-9]{1,50}')
        if self.share_id is not None:
            self.validate_pattern(self.share_id, 'share_id', '[0-9]+')
        if self.size is not None:
            self.validate_maximum(self.size, 'size', 53687091200)
            self.validate_minimum(self.size, 'size', 0)

    def to_map(self):
        result = {}
        if self.content_hash is not None:
            result['content_hash'] = self.content_hash
        if self.content_hash_name is not None:
            result['content_hash_name'] = self.content_hash_name
        if self.content_type is not None:
            result['content_type'] = self.content_type
        if self.crc_64hash is not None:
            result['crc64_hash'] = self.crc_64hash
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.download_url is not None:
            result['download_url'] = self.download_url
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_extension is not None:
            result['file_extension'] = self.file_extension
        if self.file_path is not None:
            result['file_path'] = self.file_path
        if self.name is not None:
            result['name'] = self.name
        if self.parent_file_path is not None:
            result['parent_file_path'] = self.parent_file_path
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.size is not None:
            result['size'] = self.size
        if self.status is not None:
            result['status'] = self.status
        if self.thumbnail is not None:
            result['thumbnail'] = self.thumbnail
        if self.trashed_at is not None:
            result['trashed_at'] = self.trashed_at
        if self.type is not None:
            result['type'] = self.type
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        if self.upload_id is not None:
            result['upload_id'] = self.upload_id
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, map={}):
        if map.get('content_hash') is not None:
            self.content_hash = map.get('content_hash')
        if map.get('content_hash_name') is not None:
            self.content_hash_name = map.get('content_hash_name')
        if map.get('content_type') is not None:
            self.content_type = map.get('content_type')
        if map.get('crc64_hash') is not None:
            self.crc_64hash = map.get('crc64_hash')
        if map.get('created_at') is not None:
            self.created_at = map.get('created_at')
        if map.get('description') is not None:
            self.description = map.get('description')
        if map.get('domain_id') is not None:
            self.domain_id = map.get('domain_id')
        if map.get('download_url') is not None:
            self.download_url = map.get('download_url')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('file_extension') is not None:
            self.file_extension = map.get('file_extension')
        if map.get('file_path') is not None:
            self.file_path = map.get('file_path')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('parent_file_path') is not None:
            self.parent_file_path = map.get('parent_file_path')
        if map.get('share_id') is not None:
            self.share_id = map.get('share_id')
        if map.get('size') is not None:
            self.size = map.get('size')
        if map.get('status') is not None:
            self.status = map.get('status')
        if map.get('thumbnail') is not None:
            self.thumbnail = map.get('thumbnail')
        if map.get('trashed_at') is not None:
            self.trashed_at = map.get('trashed_at')
        if map.get('type') is not None:
            self.type = map.get('type')
        if map.get('updated_at') is not None:
            self.updated_at = map.get('updated_at')
        if map.get('upload_id') is not None:
            self.upload_id = map.get('upload_id')
        if map.get('url') is not None:
            self.url = map.get('url')
        return self


class OSSVideoDRMLicenseResponse(TeaModel):
    """
    DRM License response
    """
    def __init__(self, data=None, states=None):
        # drm_data
        self.data = data                # type: str
        # states
        self.states = states            # type: int

    def validate(self):
        self.validate_required(self.data, 'data')
        self.validate_required(self.states, 'states')

    def to_map(self):
        result = {}
        if self.data is not None:
            result['data'] = self.data
        if self.states is not None:
            result['states'] = self.states
        return result

    def from_map(self, map={}):
        if map.get('data') is not None:
            self.data = map.get('data')
        if map.get('states') is not None:
            self.states = map.get('states')
        return self


class OSSVideoDefinitionResponse(TeaModel):
    """
    转码接口response
    """
    def __init__(self, definition_list=None, frame_rate=None):
        # definition_list
        self.definition_list = definition_list  # type: List[str]
        # frame_rate
        self.frame_rate = frame_rate    # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.definition_list is not None:
            result['definition_list'] = self.definition_list
        if self.frame_rate is not None:
            result['frame_rate'] = self.frame_rate
        return result

    def from_map(self, map={}):
        if map.get('definition_list') is not None:
            self.definition_list = map.get('definition_list')
        if map.get('frame_rate') is not None:
            self.frame_rate = map.get('frame_rate')
        return self


class OSSVideoTranscodeResponse(TeaModel):
    """
    转码接口response
    """
    def __init__(self, definition_list=None, duration=None, hls_time=None):
        # definition_list
        self.definition_list = definition_list  # type: List[str]
        # duration
        self.duration = duration        # type: int
        # hls_time
        self.hls_time = hls_time        # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.definition_list is not None:
            result['definition_list'] = self.definition_list
        if self.duration is not None:
            result['duration'] = self.duration
        if self.hls_time is not None:
            result['hls_time'] = self.hls_time
        return result

    def from_map(self, map={}):
        if map.get('definition_list') is not None:
            self.definition_list = map.get('definition_list')
        if map.get('duration') is not None:
            self.duration = map.get('duration')
        if map.get('hls_time') is not None:
            self.hls_time = map.get('hls_time')
        return self


class PreHashCheckSuccessResponse(TeaModel):
    """
    Pre hash check Response
    """
    def __init__(self, code=None, file_name=None, message=None, parent_file_id=None, pre_hash=None):
        # code
        self.code = code                # type: str
        # file_name
        self.file_name = file_name      # type: str
        # message
        self.message = message          # type: str
        # parent_file_id
        self.parent_file_id = parent_file_id  # type: str
        # pre_hash
        self.pre_hash = pre_hash        # type: str

    def validate(self):
        self.validate_required(self.parent_file_id, 'parent_file_id')
        if self.parent_file_id is not None:
            self.validate_max_length(self.parent_file_id, 'parent_file_id', 50)
            self.validate_pattern(self.parent_file_id, 'parent_file_id', '[a-z0-9]{1,50}')

    def to_map(self):
        result = {}
        if self.code is not None:
            result['code'] = self.code
        if self.file_name is not None:
            result['file_name'] = self.file_name
        if self.message is not None:
            result['message'] = self.message
        if self.parent_file_id is not None:
            result['parent_file_id'] = self.parent_file_id
        if self.pre_hash is not None:
            result['pre_hash'] = self.pre_hash
        return result

    def from_map(self, map={}):
        if map.get('code') is not None:
            self.code = map.get('code')
        if map.get('file_name') is not None:
            self.file_name = map.get('file_name')
        if map.get('message') is not None:
            self.message = map.get('message')
        if map.get('parent_file_id') is not None:
            self.parent_file_id = map.get('parent_file_id')
        if map.get('pre_hash') is not None:
            self.pre_hash = map.get('pre_hash')
        return self


class RateLimit(TeaModel):
    """
    下载限速配置
    """
    def __init__(self, part_size=None, part_speed=None):
        self.part_size = part_size      # type: int
        self.part_speed = part_speed    # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.part_size is not None:
            result['part_size'] = self.part_size
        if self.part_speed is not None:
            result['part_speed'] = self.part_speed
        return result

    def from_map(self, map={}):
        if map.get('part_size') is not None:
            self.part_size = map.get('part_size')
        if map.get('part_speed') is not None:
            self.part_speed = map.get('part_speed')
        return self


class RevokeRequest(TeaModel):
    """
    *
    """
    def __init__(self, headers=None, app_id=None, refresh_token=None):
        self.headers = headers          # type: Dict[str, str]
        # App ID, 当前访问的App
        self.app_id = app_id            # type: str
        # refresh token, 登录时返回的
        self.refresh_token = refresh_token  # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.refresh_token, 'refresh_token')

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.app_id is not None:
            result['app_id'] = self.app_id
        if self.refresh_token is not None:
            result['refresh_token'] = self.refresh_token
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('app_id') is not None:
            self.app_id = map.get('app_id')
        if map.get('refresh_token') is not None:
            self.refresh_token = map.get('refresh_token')
        return self


class ScanFileMetaResponse(TeaModel):
    """
    scan file meta response
    """
    def __init__(self, items=None, next_marker=None):
        # items
        self.items = items              # type: List[BaseFileResponse]
        # next_marker
        self.next_marker = next_marker  # type: str

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, map={}):
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = BaseFileResponse()
                self.items.append(temp_model.from_map(k))
        if map.get('next_marker') is not None:
            self.next_marker = map.get('next_marker')
        return self


class SearchFileResponse(TeaModel):
    """
    search file response
    """
    def __init__(self, items=None, next_marker=None):
        # items
        self.items = items              # type: List[BaseFileResponse]
        # next_marker
        self.next_marker = next_marker  # type: str

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, map={}):
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = BaseFileResponse()
                self.items.append(temp_model.from_map(k))
        if map.get('next_marker') is not None:
            self.next_marker = map.get('next_marker')
        return self


class SharePermissionPolicy(TeaModel):
    """
    *
    """
    def __init__(self, file_path=None, permission_inheritable=None, permission_list=None, permission_type=None):
        self.file_path = file_path      # type: str
        self.permission_inheritable = permission_inheritable  # type: bool
        self.permission_list = permission_list  # type: List[str]
        self.permission_type = permission_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.file_path is not None:
            result['file_path'] = self.file_path
        if self.permission_inheritable is not None:
            result['permission_inheritable'] = self.permission_inheritable
        if self.permission_list is not None:
            result['permission_list'] = self.permission_list
        if self.permission_type is not None:
            result['permission_type'] = self.permission_type
        return result

    def from_map(self, map={}):
        if map.get('file_path') is not None:
            self.file_path = map.get('file_path')
        if map.get('permission_inheritable') is not None:
            self.permission_inheritable = map.get('permission_inheritable')
        if map.get('permission_list') is not None:
            self.permission_list = map.get('permission_list')
        if map.get('permission_type') is not None:
            self.permission_type = map.get('permission_type')
        return self


class StoreFile(TeaModel):
    """
    *
    """
    def __init__(self, domain_id=None, name=None, parent_file_path=None, store_id=None, type=None):
        self.domain_id = domain_id      # type: str
        self.name = name                # type: str
        self.parent_file_path = parent_file_path  # type: str
        self.store_id = store_id        # type: str
        self.type = type                # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.name is not None:
            result['name'] = self.name
        if self.parent_file_path is not None:
            result['parent_file_path'] = self.parent_file_path
        if self.store_id is not None:
            result['store_id'] = self.store_id
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, map={}):
        if map.get('domain_id') is not None:
            self.domain_id = map.get('domain_id')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('parent_file_path') is not None:
            self.parent_file_path = map.get('parent_file_path')
        if map.get('store_id') is not None:
            self.store_id = map.get('store_id')
        if map.get('type') is not None:
            self.type = map.get('type')
        return self


class StoreItemResponse(TeaModel):
    """
    *
    """
    def __init__(self, accelerate_endpoint=None, base_path=None, bucket=None, cdn_endpoint=None,
                 customized_accelerate_endpoint=None, customized_cdn_endpoint=None, customized_endpoint=None, customized_internal_endpoint=None,
                 domain_id=None, endpoint=None, internal_endpoint=None, location=None, ownership=None, policy=None,
                 role_arn=None, store_id=None, type=None):
        # 全球加速地址
        self.accelerate_endpoint = accelerate_endpoint  # type: str
        # 存储公共前缀
        self.base_path = base_path      # type: str
        # bucket名称
        self.bucket = bucket            # type: str
        # 内容分发地址
        self.cdn_endpoint = cdn_endpoint  # type: str
        # 自定义全球加速地址
        self.customized_accelerate_endpoint = customized_accelerate_endpoint  # type: str
        # 自定义内容分发地址
        self.customized_cdn_endpoint = customized_cdn_endpoint  # type: str
        # 自定义Public访问地址
        self.customized_endpoint = customized_endpoint  # type: str
        # 自定义vpc访问地址
        self.customized_internal_endpoint = customized_internal_endpoint  # type: str
        self.domain_id = domain_id      # type: str
        # Public访问地址
        self.endpoint = endpoint        # type: str
        # vpc访问地址
        self.internal_endpoint = internal_endpoint  # type: str
        # 地点
        self.location = location        # type: str
        # 存储归属，system表示系统提供，custom表示使用自己的存储
        self.ownership = ownership      # type: str
        # Policy授权,system类型store会将bucket权限授予当前云账号
        self.policy = policy            # type: str
        # 访问Bucket的角色ARN
        self.role_arn = role_arn        # type: str
        # store ID
        self.store_id = store_id        # type: str
        # 存储类型，当前只支持oss
        self.type = type                # type: str

    def validate(self):
        self.validate_required(self.bucket, 'bucket')
        self.validate_required(self.endpoint, 'endpoint')
        self.validate_required(self.ownership, 'ownership')
        self.validate_required(self.policy, 'policy')
        self.validate_required(self.store_id, 'store_id')
        self.validate_required(self.type, 'type')

    def to_map(self):
        result = {}
        if self.accelerate_endpoint is not None:
            result['accelerate_endpoint'] = self.accelerate_endpoint
        if self.base_path is not None:
            result['base_path'] = self.base_path
        if self.bucket is not None:
            result['bucket'] = self.bucket
        if self.cdn_endpoint is not None:
            result['cdn_endpoint'] = self.cdn_endpoint
        if self.customized_accelerate_endpoint is not None:
            result['customized_accelerate_endpoint'] = self.customized_accelerate_endpoint
        if self.customized_cdn_endpoint is not None:
            result['customized_cdn_endpoint'] = self.customized_cdn_endpoint
        if self.customized_endpoint is not None:
            result['customized_endpoint'] = self.customized_endpoint
        if self.customized_internal_endpoint is not None:
            result['customized_internal_endpoint'] = self.customized_internal_endpoint
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.internal_endpoint is not None:
            result['internal_endpoint'] = self.internal_endpoint
        if self.location is not None:
            result['location'] = self.location
        if self.ownership is not None:
            result['ownership'] = self.ownership
        if self.policy is not None:
            result['policy'] = self.policy
        if self.role_arn is not None:
            result['role_arn'] = self.role_arn
        if self.store_id is not None:
            result['store_id'] = self.store_id
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, map={}):
        if map.get('accelerate_endpoint') is not None:
            self.accelerate_endpoint = map.get('accelerate_endpoint')
        if map.get('base_path') is not None:
            self.base_path = map.get('base_path')
        if map.get('bucket') is not None:
            self.bucket = map.get('bucket')
        if map.get('cdn_endpoint') is not None:
            self.cdn_endpoint = map.get('cdn_endpoint')
        if map.get('customized_accelerate_endpoint') is not None:
            self.customized_accelerate_endpoint = map.get('customized_accelerate_endpoint')
        if map.get('customized_cdn_endpoint') is not None:
            self.customized_cdn_endpoint = map.get('customized_cdn_endpoint')
        if map.get('customized_endpoint') is not None:
            self.customized_endpoint = map.get('customized_endpoint')
        if map.get('customized_internal_endpoint') is not None:
            self.customized_internal_endpoint = map.get('customized_internal_endpoint')
        if map.get('domain_id') is not None:
            self.domain_id = map.get('domain_id')
        if map.get('endpoint') is not None:
            self.endpoint = map.get('endpoint')
        if map.get('internal_endpoint') is not None:
            self.internal_endpoint = map.get('internal_endpoint')
        if map.get('location') is not None:
            self.location = map.get('location')
        if map.get('ownership') is not None:
            self.ownership = map.get('ownership')
        if map.get('policy') is not None:
            self.policy = map.get('policy')
        if map.get('role_arn') is not None:
            self.role_arn = map.get('role_arn')
        if map.get('store_id') is not None:
            self.store_id = map.get('store_id')
        if map.get('type') is not None:
            self.type = map.get('type')
        return self


class StreamInfo(TeaModel):
    """
    *
    """
    def __init__(self, crc_64hash=None, download_url=None, thumbnail=None, url=None):
        # crc64_hash
        self.crc_64hash = crc_64hash    # type: str
        # download_url
        self.download_url = download_url  # type: str
        # thumbnail
        self.thumbnail = thumbnail      # type: str
        # url
        self.url = url                  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.crc_64hash is not None:
            result['crc64_hash'] = self.crc_64hash
        if self.download_url is not None:
            result['download_url'] = self.download_url
        if self.thumbnail is not None:
            result['thumbnail'] = self.thumbnail
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, map={}):
        if map.get('crc64_hash') is not None:
            self.crc_64hash = map.get('crc64_hash')
        if map.get('download_url') is not None:
            self.download_url = map.get('download_url')
        if map.get('thumbnail') is not None:
            self.thumbnail = map.get('thumbnail')
        if map.get('url') is not None:
            self.url = map.get('url')
        return self


class StreamUploadInfo(TeaModel):
    """
    *
    """
    def __init__(self, part_info_list=None, pre_rapid_upload=None, rapid_upload=None, upload_id=None):
        # part_info_list
        self.part_info_list = part_info_list  # type: List[UploadPartInfo]
        # pre_rapid_upload
        # type: boolean
        self.pre_rapid_upload = pre_rapid_upload  # type: bool
        # rapid_upload
        # type: boolean
        self.rapid_upload = rapid_upload  # type: bool
        # upload_id
        self.upload_id = upload_id      # type: str

    def validate(self):
        if self.part_info_list:
            for k in self.part_info_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k in self.part_info_list:
                result['part_info_list'].append(k.to_map() if k else None)
        if self.pre_rapid_upload is not None:
            result['pre_rapid_upload'] = self.pre_rapid_upload
        if self.rapid_upload is not None:
            result['rapid_upload'] = self.rapid_upload
        if self.upload_id is not None:
            result['upload_id'] = self.upload_id
        return result

    def from_map(self, map={}):
        self.part_info_list = []
        if map.get('part_info_list') is not None:
            for k in map.get('part_info_list'):
                temp_model = UploadPartInfo()
                self.part_info_list.append(temp_model.from_map(k))
        if map.get('pre_rapid_upload') is not None:
            self.pre_rapid_upload = map.get('pre_rapid_upload')
        if map.get('rapid_upload') is not None:
            self.rapid_upload = map.get('rapid_upload')
        if map.get('upload_id') is not None:
            self.upload_id = map.get('upload_id')
        return self


class SystemTag(TeaModel):
    """
    *
    """
    def __init__(self, confidence=None, en_name=None, name=None, parent_en_name=None, parent_name=None,
                 selected=None, tag_level=None):
        self.confidence = confidence    # type: float
        self.en_name = en_name          # type: str
        self.name = name                # type: str
        self.parent_en_name = parent_en_name  # type: str
        self.parent_name = parent_name  # type: str
        self.selected = selected        # type: bool
        self.tag_level = tag_level      # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.confidence is not None:
            result['confidence'] = self.confidence
        if self.en_name is not None:
            result['en_name'] = self.en_name
        if self.name is not None:
            result['name'] = self.name
        if self.parent_en_name is not None:
            result['parent_en_name'] = self.parent_en_name
        if self.parent_name is not None:
            result['parent_name'] = self.parent_name
        if self.selected is not None:
            result['selected'] = self.selected
        if self.tag_level is not None:
            result['tag_level'] = self.tag_level
        return result

    def from_map(self, map={}):
        if map.get('confidence') is not None:
            self.confidence = map.get('confidence')
        if map.get('en_name') is not None:
            self.en_name = map.get('en_name')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('parent_en_name') is not None:
            self.parent_en_name = map.get('parent_en_name')
        if map.get('parent_name') is not None:
            self.parent_name = map.get('parent_name')
        if map.get('selected') is not None:
            self.selected = map.get('selected')
        if map.get('tag_level') is not None:
            self.tag_level = map.get('tag_level')
        return self


class TokenRequest(TeaModel):
    """
    *
    """
    def __init__(self, headers=None, addition_data=None, app_id=None, grant_type=None, refresh_token=None):
        self.headers = headers          # type: Dict[str, str]
        # addition_data
        self.addition_data = addition_data  # type: dict
        # App ID, 当前访问的App
        self.app_id = app_id            # type: str
        # 只能填refresh_token
        self.grant_type = grant_type    # type: str
        # refresh token, 登录时返回的
        self.refresh_token = refresh_token  # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.grant_type, 'grant_type')
        self.validate_required(self.refresh_token, 'refresh_token')

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.addition_data is not None:
            result['addition_data'] = self.addition_data
        if self.app_id is not None:
            result['app_id'] = self.app_id
        if self.grant_type is not None:
            result['grant_type'] = self.grant_type
        if self.refresh_token is not None:
            result['refresh_token'] = self.refresh_token
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('addition_data') is not None:
            self.addition_data = map.get('addition_data')
        if map.get('app_id') is not None:
            self.app_id = map.get('app_id')
        if map.get('grant_type') is not None:
            self.grant_type = map.get('grant_type')
        if map.get('refresh_token') is not None:
            self.refresh_token = map.get('refresh_token')
        return self


class UpdateDriveResponse(TeaModel):
    """
    Update drive response
    """
    def __init__(self, creator=None, description=None, domain_id=None, drive_id=None, drive_name=None,
                 drive_type=None, encrypt_data_access=None, encrypt_mode=None, owner=None, relative_path=None, status=None,
                 store_id=None, total_size=None, used_size=None):
        # Drive 创建者
        self.creator = creator          # type: str
        # Drive 备注信息
        self.description = description  # type: str
        # Domain ID
        self.domain_id = domain_id      # type: str
        # Drive ID
        self.drive_id = drive_id        # type: str
        # Drive 名称
        self.drive_name = drive_name    # type: str
        # Drive 类型
        self.drive_type = drive_type    # type: str
        self.encrypt_data_access = encrypt_data_access  # type: bool
        self.encrypt_mode = encrypt_mode  # type: str
        # Drive 所有者
        self.owner = owner              # type: str
        # Drive存储基于store的相对路径，domain的PathType为OSSPath时返回
        self.relative_path = relative_path  # type: str
        # Drive 状态
        self.status = status            # type: str
        # 存储 ID, domain的PathType为OSSPath时返回
        self.store_id = store_id        # type: str
        # Drive 空间总量
        self.total_size = total_size    # type: int
        # Drive 空间已使用量
        self.used_size = used_size      # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.creator is not None:
            result['creator'] = self.creator
        if self.description is not None:
            result['description'] = self.description
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.drive_name is not None:
            result['drive_name'] = self.drive_name
        if self.drive_type is not None:
            result['drive_type'] = self.drive_type
        if self.encrypt_data_access is not None:
            result['encrypt_data_access'] = self.encrypt_data_access
        if self.encrypt_mode is not None:
            result['encrypt_mode'] = self.encrypt_mode
        if self.owner is not None:
            result['owner'] = self.owner
        if self.relative_path is not None:
            result['relative_path'] = self.relative_path
        if self.status is not None:
            result['status'] = self.status
        if self.store_id is not None:
            result['store_id'] = self.store_id
        if self.total_size is not None:
            result['total_size'] = self.total_size
        if self.used_size is not None:
            result['used_size'] = self.used_size
        return result

    def from_map(self, map={}):
        if map.get('creator') is not None:
            self.creator = map.get('creator')
        if map.get('description') is not None:
            self.description = map.get('description')
        if map.get('domain_id') is not None:
            self.domain_id = map.get('domain_id')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('drive_name') is not None:
            self.drive_name = map.get('drive_name')
        if map.get('drive_type') is not None:
            self.drive_type = map.get('drive_type')
        if map.get('encrypt_data_access') is not None:
            self.encrypt_data_access = map.get('encrypt_data_access')
        if map.get('encrypt_mode') is not None:
            self.encrypt_mode = map.get('encrypt_mode')
        if map.get('owner') is not None:
            self.owner = map.get('owner')
        if map.get('relative_path') is not None:
            self.relative_path = map.get('relative_path')
        if map.get('status') is not None:
            self.status = map.get('status')
        if map.get('store_id') is not None:
            self.store_id = map.get('store_id')
        if map.get('total_size') is not None:
            self.total_size = map.get('total_size')
        if map.get('used_size') is not None:
            self.used_size = map.get('used_size')
        return self


class UpdateFileMetaResponse(TeaModel):
    """
    更新文件元数据 response
    """
    def __init__(self, category=None, content_hash=None, content_hash_name=None, content_type=None, crc_64hash=None,
                 created_at=None, description=None, domain_id=None, download_url=None, drive_id=None, encrypt_mode=None,
                 file_extension=None, file_id=None, hidden=None, image_media_metadata=None, labels=None, meta=None, name=None,
                 parent_file_id=None, punish_flag=None, size=None, starred=None, status=None, streams_info=None, thumbnail=None,
                 trashed_at=None, type=None, updated_at=None, upload_id=None, url=None, user_meta=None,
                 video_media_metadata=None, video_preview_metadata=None):
        # category
        self.category = category        # type: str
        # Content Hash
        self.content_hash = content_hash  # type: str
        # content_hash_name
        self.content_hash_name = content_hash_name  # type: str
        # content_type
        self.content_type = content_type  # type: str
        # crc64_hash
        self.crc_64hash = crc_64hash    # type: str
        # created_at
        self.created_at = created_at    # type: str
        # description
        self.description = description  # type: str
        # DomainID
        self.domain_id = domain_id      # type: str
        # download_url
        self.download_url = download_url  # type: str
        # drive_id
        self.drive_id = drive_id        # type: str
        # encrypt_mode
        self.encrypt_mode = encrypt_mode  # type: str
        # file_extension
        self.file_extension = file_extension  # type: str
        # file_id
        self.file_id = file_id          # type: str
        # Hidden
        # type: boolean
        self.hidden = hidden            # type: bool
        self.image_media_metadata = image_media_metadata  # type: ImageMediaResponse
        # labels
        self.labels = labels            # type: List[str]
        self.meta = meta                # type: str
        # name
        self.name = name                # type: str
        # parent_file_id
        self.parent_file_id = parent_file_id  # type: str
        self.punish_flag = punish_flag  # type: int
        # Size
        self.size = size                # type: int
        # starred
        # type: boolean
        self.starred = starred          # type: bool
        # status
        self.status = status            # type: str
        # @Deprecated streams url info
        self.streams_info = streams_info  # type: dict
        # thumbnail
        self.thumbnail = thumbnail      # type: str
        # trashed_at
        self.trashed_at = trashed_at    # type: str
        # type
        self.type = type                # type: str
        # updated_at
        self.updated_at = updated_at    # type: str
        # upload_id
        self.upload_id = upload_id      # type: str
        # url
        self.url = url                  # type: str
        # user_meta
        self.user_meta = user_meta      # type: str
        self.video_media_metadata = video_media_metadata  # type: VideoMediaResponse
        self.video_preview_metadata = video_preview_metadata  # type: VideoPreviewResponse

    def validate(self):
        if self.domain_id is not None:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z]+')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.file_id is not None:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9]{1,50}')
        if self.image_media_metadata:
            self.image_media_metadata.validate()
        self.validate_required(self.name, 'name')
        if self.name is not None:
            self.validate_pattern(self.name, 'name', '[a-zA-Z0-9.-]{1,1000}')
        if self.parent_file_id is not None:
            self.validate_max_length(self.parent_file_id, 'parent_file_id', 50)
            self.validate_pattern(self.parent_file_id, 'parent_file_id', '[a-z0-9]{1,50}')
        if self.size is not None:
            self.validate_maximum(self.size, 'size', 53687091200)
            self.validate_minimum(self.size, 'size', 0)
        if self.video_media_metadata:
            self.video_media_metadata.validate()
        if self.video_preview_metadata:
            self.video_preview_metadata.validate()

    def to_map(self):
        result = {}
        if self.category is not None:
            result['category'] = self.category
        if self.content_hash is not None:
            result['content_hash'] = self.content_hash
        if self.content_hash_name is not None:
            result['content_hash_name'] = self.content_hash_name
        if self.content_type is not None:
            result['content_type'] = self.content_type
        if self.crc_64hash is not None:
            result['crc64_hash'] = self.crc_64hash
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.download_url is not None:
            result['download_url'] = self.download_url
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.encrypt_mode is not None:
            result['encrypt_mode'] = self.encrypt_mode
        if self.file_extension is not None:
            result['file_extension'] = self.file_extension
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.hidden is not None:
            result['hidden'] = self.hidden
        if self.image_media_metadata is not None:
            result['image_media_metadata'] = self.image_media_metadata.to_map()
        if self.labels is not None:
            result['labels'] = self.labels
        if self.meta is not None:
            result['meta'] = self.meta
        if self.name is not None:
            result['name'] = self.name
        if self.parent_file_id is not None:
            result['parent_file_id'] = self.parent_file_id
        if self.punish_flag is not None:
            result['punish_flag'] = self.punish_flag
        if self.size is not None:
            result['size'] = self.size
        if self.starred is not None:
            result['starred'] = self.starred
        if self.status is not None:
            result['status'] = self.status
        if self.streams_info is not None:
            result['streams_info'] = self.streams_info
        if self.thumbnail is not None:
            result['thumbnail'] = self.thumbnail
        if self.trashed_at is not None:
            result['trashed_at'] = self.trashed_at
        if self.type is not None:
            result['type'] = self.type
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        if self.upload_id is not None:
            result['upload_id'] = self.upload_id
        if self.url is not None:
            result['url'] = self.url
        if self.user_meta is not None:
            result['user_meta'] = self.user_meta
        if self.video_media_metadata is not None:
            result['video_media_metadata'] = self.video_media_metadata.to_map()
        if self.video_preview_metadata is not None:
            result['video_preview_metadata'] = self.video_preview_metadata.to_map()
        return result

    def from_map(self, map={}):
        if map.get('category') is not None:
            self.category = map.get('category')
        if map.get('content_hash') is not None:
            self.content_hash = map.get('content_hash')
        if map.get('content_hash_name') is not None:
            self.content_hash_name = map.get('content_hash_name')
        if map.get('content_type') is not None:
            self.content_type = map.get('content_type')
        if map.get('crc64_hash') is not None:
            self.crc_64hash = map.get('crc64_hash')
        if map.get('created_at') is not None:
            self.created_at = map.get('created_at')
        if map.get('description') is not None:
            self.description = map.get('description')
        if map.get('domain_id') is not None:
            self.domain_id = map.get('domain_id')
        if map.get('download_url') is not None:
            self.download_url = map.get('download_url')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('encrypt_mode') is not None:
            self.encrypt_mode = map.get('encrypt_mode')
        if map.get('file_extension') is not None:
            self.file_extension = map.get('file_extension')
        if map.get('file_id') is not None:
            self.file_id = map.get('file_id')
        if map.get('hidden') is not None:
            self.hidden = map.get('hidden')
        if map.get('image_media_metadata') is not None:
            temp_model = ImageMediaResponse()
            self.image_media_metadata = temp_model.from_map(map['image_media_metadata'])
        if map.get('labels') is not None:
            self.labels = map.get('labels')
        if map.get('meta') is not None:
            self.meta = map.get('meta')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('parent_file_id') is not None:
            self.parent_file_id = map.get('parent_file_id')
        if map.get('punish_flag') is not None:
            self.punish_flag = map.get('punish_flag')
        if map.get('size') is not None:
            self.size = map.get('size')
        if map.get('starred') is not None:
            self.starred = map.get('starred')
        if map.get('status') is not None:
            self.status = map.get('status')
        if map.get('streams_info') is not None:
            self.streams_info = map.get('streams_info')
        if map.get('thumbnail') is not None:
            self.thumbnail = map.get('thumbnail')
        if map.get('trashed_at') is not None:
            self.trashed_at = map.get('trashed_at')
        if map.get('type') is not None:
            self.type = map.get('type')
        if map.get('updated_at') is not None:
            self.updated_at = map.get('updated_at')
        if map.get('upload_id') is not None:
            self.upload_id = map.get('upload_id')
        if map.get('url') is not None:
            self.url = map.get('url')
        if map.get('user_meta') is not None:
            self.user_meta = map.get('user_meta')
        if map.get('video_media_metadata') is not None:
            temp_model = VideoMediaResponse()
            self.video_media_metadata = temp_model.from_map(map['video_media_metadata'])
        if map.get('video_preview_metadata') is not None:
            temp_model = VideoPreviewResponse()
            self.video_preview_metadata = temp_model.from_map(map['video_preview_metadata'])
        return self


class UpdateShareResponse(TeaModel):
    """
    Update share response
    """
    def __init__(self, created_at=None, creator=None, description=None, domain_id=None, drive_id=None,
                 expiration=None, expired=None, owner=None, permissions=None, share_file_path=None, share_id=None,
                 share_name=None, share_policy=None, status=None, updated_at=None):
        # created_at
        self.created_at = created_at    # type: str
        # creator
        self.creator = creator          # type: str
        # description
        self.description = description  # type: str
        # domain_id
        self.domain_id = domain_id      # type: str
        # drive_id
        self.drive_id = drive_id        # type: str
        # expiration
        self.expiration = expiration    # type: str
        # expired
        self.expired = expired          # type: bool
        # owner
        self.owner = owner              # type: str
        # permissions
        self.permissions = permissions  # type: List[str]
        # share_path
        self.share_file_path = share_file_path  # type: str
        # share_id
        self.share_id = share_id        # type: str
        # share_name
        self.share_name = share_name    # type: str
        self.share_policy = share_policy  # type: List[SharePermissionPolicy]
        # status
        self.status = status            # type: str
        # updated_at
        self.updated_at = updated_at    # type: str

    def validate(self):
        if self.share_policy:
            for k in self.share_policy:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.creator is not None:
            result['creator'] = self.creator
        if self.description is not None:
            result['description'] = self.description
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.expiration is not None:
            result['expiration'] = self.expiration
        if self.expired is not None:
            result['expired'] = self.expired
        if self.owner is not None:
            result['owner'] = self.owner
        if self.permissions is not None:
            result['permissions'] = self.permissions
        if self.share_file_path is not None:
            result['share_file_path'] = self.share_file_path
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.share_name is not None:
            result['share_name'] = self.share_name
        result['share_policy'] = []
        if self.share_policy is not None:
            for k in self.share_policy:
                result['share_policy'].append(k.to_map() if k else None)
        if self.status is not None:
            result['status'] = self.status
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        return result

    def from_map(self, map={}):
        if map.get('created_at') is not None:
            self.created_at = map.get('created_at')
        if map.get('creator') is not None:
            self.creator = map.get('creator')
        if map.get('description') is not None:
            self.description = map.get('description')
        if map.get('domain_id') is not None:
            self.domain_id = map.get('domain_id')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('expiration') is not None:
            self.expiration = map.get('expiration')
        if map.get('expired') is not None:
            self.expired = map.get('expired')
        if map.get('owner') is not None:
            self.owner = map.get('owner')
        if map.get('permissions') is not None:
            self.permissions = map.get('permissions')
        if map.get('share_file_path') is not None:
            self.share_file_path = map.get('share_file_path')
        if map.get('share_id') is not None:
            self.share_id = map.get('share_id')
        if map.get('share_name') is not None:
            self.share_name = map.get('share_name')
        self.share_policy = []
        if map.get('share_policy') is not None:
            for k in map.get('share_policy'):
                temp_model = SharePermissionPolicy()
                self.share_policy.append(temp_model.from_map(k))
        if map.get('status') is not None:
            self.status = map.get('status')
        if map.get('updated_at') is not None:
            self.updated_at = map.get('updated_at')
        return self


class UploadPartInfo(TeaModel):
    """
    *
    """
    def __init__(self, etag=None, part_number=None, part_size=None, upload_url=None):
        # etag
        self.etag = etag                # type: str
        # PartNumber
        self.part_number = part_number  # type: int
        # PartSize：
        self.part_size = part_size      # type: int
        # upload_url
        self.upload_url = upload_url    # type: str

    def validate(self):
        if self.part_number is not None:
            self.validate_pattern(self.part_number, 'part_number', '[0-9]+')
            self.validate_maximum(self.part_number, 'part_number', 10000)
            self.validate_minimum(self.part_number, 'part_number', 1)
        if self.part_size is not None:
            self.validate_maximum(self.part_size, 'part_size', 5368709120)
            self.validate_minimum(self.part_size, 'part_size', 102400)

    def to_map(self):
        result = {}
        if self.etag is not None:
            result['etag'] = self.etag
        if self.part_number is not None:
            result['part_number'] = self.part_number
        if self.part_size is not None:
            result['part_size'] = self.part_size
        if self.upload_url is not None:
            result['upload_url'] = self.upload_url
        return result

    def from_map(self, map={}):
        if map.get('etag') is not None:
            self.etag = map.get('etag')
        if map.get('part_number') is not None:
            self.part_number = map.get('part_number')
        if map.get('part_size') is not None:
            self.part_size = map.get('part_size')
        if map.get('upload_url') is not None:
            self.upload_url = map.get('upload_url')
        return self


class UrlInfo(TeaModel):
    """
    *
    """
    def __init__(self, download_url=None, thumbnail=None, url=None):
        # download_url
        self.download_url = download_url  # type: str
        # thumbnail
        self.thumbnail = thumbnail      # type: str
        # url
        self.url = url                  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.download_url is not None:
            result['download_url'] = self.download_url
        if self.thumbnail is not None:
            result['thumbnail'] = self.thumbnail
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, map={}):
        if map.get('download_url') is not None:
            self.download_url = map.get('download_url')
        if map.get('thumbnail') is not None:
            self.thumbnail = map.get('thumbnail')
        if map.get('url') is not None:
            self.url = map.get('url')
        return self


class UserAuthentication(TeaModel):
    """
    *
    """
    def __init__(self, authentication_type=None, created_at=None, detail=None, domain_id=None, identity=None,
                 last_login_time=None, status=None, user_id=None, extra=None):
        # 认证类型
        self.authentication_type = authentication_type  # type: str
        # 创建时间
        self.created_at = created_at    # type: int
        # 详情
        self.detail = detail            # type: str
        # Domain ID
        self.domain_id = domain_id      # type: str
        # 唯一身份标识
        self.identity = identity        # type: str
        # 最后登录时间
        self.last_login_time = last_login_time  # type: int
        # 状态
        self.status = status            # type: str
        # 用户ID
        self.user_id = user_id          # type: str
        # 额外的信息，比如type为mobile时，此字段为国家编号，不填默认86
        self.extra = extra              # type: str

    def validate(self):
        self.validate_required(self.authentication_type, 'authentication_type')
        self.validate_required(self.created_at, 'created_at')
        self.validate_required(self.detail, 'detail')
        self.validate_required(self.domain_id, 'domain_id')
        self.validate_required(self.identity, 'identity')
        self.validate_required(self.last_login_time, 'last_login_time')
        self.validate_required(self.status, 'status')
        self.validate_required(self.user_id, 'user_id')

    def to_map(self):
        result = {}
        if self.authentication_type is not None:
            result['AuthenticationType'] = self.authentication_type
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.domain_id is not None:
            result['DomainID'] = self.domain_id
        if self.identity is not None:
            result['Identity'] = self.identity
        if self.last_login_time is not None:
            result['LastLoginTime'] = self.last_login_time
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserID'] = self.user_id
        if self.extra is not None:
            result['extra'] = self.extra
        return result

    def from_map(self, map={}):
        if map.get('AuthenticationType') is not None:
            self.authentication_type = map.get('AuthenticationType')
        if map.get('CreatedAt') is not None:
            self.created_at = map.get('CreatedAt')
        if map.get('Detail') is not None:
            self.detail = map.get('Detail')
        if map.get('DomainID') is not None:
            self.domain_id = map.get('DomainID')
        if map.get('Identity') is not None:
            self.identity = map.get('Identity')
        if map.get('LastLoginTime') is not None:
            self.last_login_time = map.get('LastLoginTime')
        if map.get('Status') is not None:
            self.status = map.get('Status')
        if map.get('UserID') is not None:
            self.user_id = map.get('UserID')
        if map.get('extra') is not None:
            self.extra = map.get('extra')
        return self


class VerifyCodeRequest(TeaModel):
    """
    *
    """
    def __init__(self, headers=None, app_id=None, phone_number=None, phone_region=None, sms_code=None,
                 sms_code_id=None, verify_type=None):
        self.headers = headers          # type: Dict[str, str]
        # App ID, 当前访问的App
        self.app_id = app_id            # type: str
        # 手机号
        self.phone_number = phone_number  # type: str
        # 国家编号，默认86，不需要填+号，直接填数字
        self.phone_region = phone_region  # type: str
        # 短信验证码内容
        self.sms_code = sms_code        # type: str
        # 短信验证码ID
        self.sms_code_id = sms_code_id  # type: str
        # 需要被校验内容的类型
        self.verify_type = verify_type  # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.phone_number, 'phone_number')
        self.validate_required(self.sms_code, 'sms_code')
        self.validate_required(self.sms_code_id, 'sms_code_id')

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.app_id is not None:
            result['app_id'] = self.app_id
        if self.phone_number is not None:
            result['phone_number'] = self.phone_number
        if self.phone_region is not None:
            result['phone_region'] = self.phone_region
        if self.sms_code is not None:
            result['sms_code'] = self.sms_code
        if self.sms_code_id is not None:
            result['sms_code_id'] = self.sms_code_id
        if self.verify_type is not None:
            result['verify_type'] = self.verify_type
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('app_id') is not None:
            self.app_id = map.get('app_id')
        if map.get('phone_number') is not None:
            self.phone_number = map.get('phone_number')
        if map.get('phone_region') is not None:
            self.phone_region = map.get('phone_region')
        if map.get('sms_code') is not None:
            self.sms_code = map.get('sms_code')
        if map.get('sms_code_id') is not None:
            self.sms_code_id = map.get('sms_code_id')
        if map.get('verify_type') is not None:
            self.verify_type = map.get('verify_type')
        return self


class VerifyCodeResponse(TeaModel):
    """
    *
    """
    def __init__(self, state=None):
        # 修改密码的临时授权码
        self.state = state              # type: str

    def validate(self):
        self.validate_required(self.state, 'state')

    def to_map(self):
        result = {}
        if self.state is not None:
            result['state'] = self.state
        return result

    def from_map(self, map={}):
        if map.get('state') is not None:
            self.state = map.get('state')
        return self


class VideoMediaAudioStream(TeaModel):
    """
    *
    """
    def __init__(self, bit_rate=None, channel_layout=None, channels=None, code_name=None, duration=None,
                 sample_rate=None):
        # bit_rate 音频比特率 单位：bps
        self.bit_rate = bit_rate        # type: str
        # channel_layout 声道布局
        self.channel_layout = channel_layout  # type: str
        # channels 音频数/声道数
        self.channels = channels        # type: int
        # code_name 音频编码模式
        self.code_name = code_name      # type: str
        # duration 单位 秒
        self.duration = duration        # type: str
        # sample_rate 音频采样率
        self.sample_rate = sample_rate  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.bit_rate is not None:
            result['bit_rate'] = self.bit_rate
        if self.channel_layout is not None:
            result['channel_layout'] = self.channel_layout
        if self.channels is not None:
            result['channels'] = self.channels
        if self.code_name is not None:
            result['code_name'] = self.code_name
        if self.duration is not None:
            result['duration'] = self.duration
        if self.sample_rate is not None:
            result['sample_rate'] = self.sample_rate
        return result

    def from_map(self, map={}):
        if map.get('bit_rate') is not None:
            self.bit_rate = map.get('bit_rate')
        if map.get('channel_layout') is not None:
            self.channel_layout = map.get('channel_layout')
        if map.get('channels') is not None:
            self.channels = map.get('channels')
        if map.get('code_name') is not None:
            self.code_name = map.get('code_name')
        if map.get('duration') is not None:
            self.duration = map.get('duration')
        if map.get('sample_rate') is not None:
            self.sample_rate = map.get('sample_rate')
        return self


class VideoMediaResponse(TeaModel):
    """
    *
    """
    def __init__(self, address_line=None, city=None, country=None, district=None, duration=None, height=None,
                 location=None, province=None, time=None, township=None, video_media_audio_stream=None,
                 video_media_video_stream=None, width=None):
        # address_line
        self.address_line = address_line  # type: str
        # city
        self.city = city                # type: str
        # country
        self.country = country          # type: str
        # district
        self.district = district        # type: str
        # duration 单位 秒
        self.duration = duration        # type: str
        # height
        self.height = height            # type: int
        # location
        self.location = location        # type: str
        # province
        self.province = province        # type: str
        # time
        self.time = time                # type: str
        # township
        self.township = township        # type: str
        self.video_media_audio_stream = video_media_audio_stream  # type: List[VideoMediaAudioStream]
        self.video_media_video_stream = video_media_video_stream  # type: List[VideoMediaVideoStream]
        # width
        self.width = width              # type: int

    def validate(self):
        if self.video_media_audio_stream:
            for k in self.video_media_audio_stream:
                if k:
                    k.validate()
        if self.video_media_video_stream:
            for k in self.video_media_video_stream:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.address_line is not None:
            result['address_line'] = self.address_line
        if self.city is not None:
            result['city'] = self.city
        if self.country is not None:
            result['country'] = self.country
        if self.district is not None:
            result['district'] = self.district
        if self.duration is not None:
            result['duration'] = self.duration
        if self.height is not None:
            result['height'] = self.height
        if self.location is not None:
            result['location'] = self.location
        if self.province is not None:
            result['province'] = self.province
        if self.time is not None:
            result['time'] = self.time
        if self.township is not None:
            result['township'] = self.township
        result['video_media_audio_stream'] = []
        if self.video_media_audio_stream is not None:
            for k in self.video_media_audio_stream:
                result['video_media_audio_stream'].append(k.to_map() if k else None)
        result['video_media_video_stream'] = []
        if self.video_media_video_stream is not None:
            for k in self.video_media_video_stream:
                result['video_media_video_stream'].append(k.to_map() if k else None)
        if self.width is not None:
            result['width'] = self.width
        return result

    def from_map(self, map={}):
        if map.get('address_line') is not None:
            self.address_line = map.get('address_line')
        if map.get('city') is not None:
            self.city = map.get('city')
        if map.get('country') is not None:
            self.country = map.get('country')
        if map.get('district') is not None:
            self.district = map.get('district')
        if map.get('duration') is not None:
            self.duration = map.get('duration')
        if map.get('height') is not None:
            self.height = map.get('height')
        if map.get('location') is not None:
            self.location = map.get('location')
        if map.get('province') is not None:
            self.province = map.get('province')
        if map.get('time') is not None:
            self.time = map.get('time')
        if map.get('township') is not None:
            self.township = map.get('township')
        self.video_media_audio_stream = []
        if map.get('video_media_audio_stream') is not None:
            for k in map.get('video_media_audio_stream'):
                temp_model = VideoMediaAudioStream()
                self.video_media_audio_stream.append(temp_model.from_map(k))
        self.video_media_video_stream = []
        if map.get('video_media_video_stream') is not None:
            for k in map.get('video_media_video_stream'):
                temp_model = VideoMediaVideoStream()
                self.video_media_video_stream.append(temp_model.from_map(k))
        if map.get('width') is not None:
            self.width = map.get('width')
        return self


class VideoMediaVideoStream(TeaModel):
    """
    *
    """
    def __init__(self, bitrate=None, clarity=None, code_name=None, duration=None, fps=None):
        # bitrate 视频比特率 单位：bps
        self.bitrate = bitrate          # type: str
        # clarity 清晰度（扫描）
        self.clarity = clarity          # type: str
        # code_name 视频编码模式
        self.code_name = code_name      # type: str
        # duration 单位 秒
        self.duration = duration        # type: str
        # fps 视频平均帧率
        self.fps = fps                  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.bitrate is not None:
            result['bitrate'] = self.bitrate
        if self.clarity is not None:
            result['clarity'] = self.clarity
        if self.code_name is not None:
            result['code_name'] = self.code_name
        if self.duration is not None:
            result['duration'] = self.duration
        if self.fps is not None:
            result['fps'] = self.fps
        return result

    def from_map(self, map={}):
        if map.get('bitrate') is not None:
            self.bitrate = map.get('bitrate')
        if map.get('clarity') is not None:
            self.clarity = map.get('clarity')
        if map.get('code_name') is not None:
            self.code_name = map.get('code_name')
        if map.get('duration') is not None:
            self.duration = map.get('duration')
        if map.get('fps') is not None:
            self.fps = map.get('fps')
        return self


class VideoPreviewResponse(TeaModel):
    """
    *
    """
    def __init__(self, audio_format=None, bitrate=None, duration=None, frame_rate=None, height=None,
                 sprite_info=None, template_list=None, thumbnail=None, video_format=None, width=None):
        # audio_format
        self.audio_format = audio_format  # type: str
        # bitrate
        self.bitrate = bitrate          # type: str
        # duration
        self.duration = duration        # type: str
        # frame_rate
        self.frame_rate = frame_rate    # type: str
        # height
        self.height = height            # type: int
        self.sprite_info = sprite_info  # type: VideoPreviewSprite
        # template_list
        self.template_list = template_list  # type: List[VideoPreviewTranscode]
        # thumbnail
        self.thumbnail = thumbnail      # type: str
        # video_format
        self.video_format = video_format  # type: str
        # width
        self.width = width              # type: int

    def validate(self):
        if self.sprite_info:
            self.sprite_info.validate()
        if self.template_list:
            for k in self.template_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.audio_format is not None:
            result['audio_format'] = self.audio_format
        if self.bitrate is not None:
            result['bitrate'] = self.bitrate
        if self.duration is not None:
            result['duration'] = self.duration
        if self.frame_rate is not None:
            result['frame_rate'] = self.frame_rate
        if self.height is not None:
            result['height'] = self.height
        if self.sprite_info is not None:
            result['sprite_info'] = self.sprite_info.to_map()
        result['template_list'] = []
        if self.template_list is not None:
            for k in self.template_list:
                result['template_list'].append(k.to_map() if k else None)
        if self.thumbnail is not None:
            result['thumbnail'] = self.thumbnail
        if self.video_format is not None:
            result['video_format'] = self.video_format
        if self.width is not None:
            result['width'] = self.width
        return result

    def from_map(self, map={}):
        if map.get('audio_format') is not None:
            self.audio_format = map.get('audio_format')
        if map.get('bitrate') is not None:
            self.bitrate = map.get('bitrate')
        if map.get('duration') is not None:
            self.duration = map.get('duration')
        if map.get('frame_rate') is not None:
            self.frame_rate = map.get('frame_rate')
        if map.get('height') is not None:
            self.height = map.get('height')
        if map.get('sprite_info') is not None:
            temp_model = VideoPreviewSprite()
            self.sprite_info = temp_model.from_map(map['sprite_info'])
        self.template_list = []
        if map.get('template_list') is not None:
            for k in map.get('template_list'):
                temp_model = VideoPreviewTranscode()
                self.template_list.append(temp_model.from_map(k))
        if map.get('thumbnail') is not None:
            self.thumbnail = map.get('thumbnail')
        if map.get('video_format') is not None:
            self.video_format = map.get('video_format')
        if map.get('width') is not None:
            self.width = map.get('width')
        return self


class VideoPreviewSprite(TeaModel):
    """
    *
    """
    def __init__(self, col=None, count=None, frame_count=None, frame_height=None, frame_width=None, row=None,
                 status=None):
        # col
        self.col = col                  # type: int
        # count
        self.count = count              # type: int
        # frame_count
        self.frame_count = frame_count  # type: int
        # frame_height
        self.frame_height = frame_height  # type: int
        # frame_width
        self.frame_width = frame_width  # type: int
        # row
        self.row = row                  # type: int
        # status
        self.status = status            # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.col is not None:
            result['col'] = self.col
        if self.count is not None:
            result['count'] = self.count
        if self.frame_count is not None:
            result['frame_count'] = self.frame_count
        if self.frame_height is not None:
            result['frame_height'] = self.frame_height
        if self.frame_width is not None:
            result['frame_width'] = self.frame_width
        if self.row is not None:
            result['row'] = self.row
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, map={}):
        if map.get('col') is not None:
            self.col = map.get('col')
        if map.get('count') is not None:
            self.count = map.get('count')
        if map.get('frame_count') is not None:
            self.frame_count = map.get('frame_count')
        if map.get('frame_height') is not None:
            self.frame_height = map.get('frame_height')
        if map.get('frame_width') is not None:
            self.frame_width = map.get('frame_width')
        if map.get('row') is not None:
            self.row = map.get('row')
        if map.get('status') is not None:
            self.status = map.get('status')
        return self


class VideoPreviewTranscode(TeaModel):
    """
    *
    """
    def __init__(self, status=None, template_id=None):
        # status
        self.status = status            # type: str
        # template_id
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.status is not None:
            result['status'] = self.status
        if self.template_id is not None:
            result['template_id'] = self.template_id
        return result

    def from_map(self, map={}):
        if map.get('status') is not None:
            self.status = map.get('status')
        if map.get('template_id') is not None:
            self.template_id = map.get('template_id')
        return self


class AdminListStoresModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: ListStoresResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = ListStoresResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class GetUserAccessTokenModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: AccessTokenResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = AccessTokenResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class AddStoreResponse(TeaModel):
    """
    *
    """
    def __init__(self, accelerate_endpoint=None, base_path=None, bucket=None, cdn_endpoint=None,
                 customized_accelerate_endpoint=None, customized_cdn_endpoint=None, customized_endpoint=None, customized_internal_endpoint=None,
                 domain_id=None, endpoint=None, internal_endpoint=None, location=None, ownership=None, policy=None,
                 role_arn=None, store_id=None, type=None):
        # 全球加速地址
        self.accelerate_endpoint = accelerate_endpoint  # type: str
        # 存储公共前缀
        self.base_path = base_path      # type: str
        # bucket名称
        self.bucket = bucket            # type: str
        # 内容分发地址
        self.cdn_endpoint = cdn_endpoint  # type: str
        # 自定义全球加速地址
        self.customized_accelerate_endpoint = customized_accelerate_endpoint  # type: str
        # 自定义内容分发地址
        self.customized_cdn_endpoint = customized_cdn_endpoint  # type: str
        # 自定义Public访问地址
        self.customized_endpoint = customized_endpoint  # type: str
        # 自定义vpc访问地址
        self.customized_internal_endpoint = customized_internal_endpoint  # type: str
        # domain ID
        self.domain_id = domain_id      # type: str
        # Public访问地址
        self.endpoint = endpoint        # type: str
        # vpc访问地址
        self.internal_endpoint = internal_endpoint  # type: str
        # 地点
        self.location = location        # type: str
        # 存储归属，system表示系统提供，custom表示使用自己的存储
        self.ownership = ownership      # type: str
        # Policy授权,system类型store会将bucket权限授予当前云账号
        self.policy = policy            # type: str
        # 访问Bucket的角色ARN
        self.role_arn = role_arn        # type: str
        # store ID
        self.store_id = store_id        # type: str
        # 存储类型，当前只支持oss
        self.type = type                # type: str

    def validate(self):
        self.validate_required(self.bucket, 'bucket')
        self.validate_required(self.domain_id, 'domain_id')
        self.validate_required(self.endpoint, 'endpoint')
        self.validate_required(self.ownership, 'ownership')
        self.validate_required(self.policy, 'policy')
        self.validate_required(self.store_id, 'store_id')
        self.validate_required(self.type, 'type')

    def to_map(self):
        result = {}
        if self.accelerate_endpoint is not None:
            result['accelerate_endpoint'] = self.accelerate_endpoint
        if self.base_path is not None:
            result['base_path'] = self.base_path
        if self.bucket is not None:
            result['bucket'] = self.bucket
        if self.cdn_endpoint is not None:
            result['cdn_endpoint'] = self.cdn_endpoint
        if self.customized_accelerate_endpoint is not None:
            result['customized_accelerate_endpoint'] = self.customized_accelerate_endpoint
        if self.customized_cdn_endpoint is not None:
            result['customized_cdn_endpoint'] = self.customized_cdn_endpoint
        if self.customized_endpoint is not None:
            result['customized_endpoint'] = self.customized_endpoint
        if self.customized_internal_endpoint is not None:
            result['customized_internal_endpoint'] = self.customized_internal_endpoint
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.internal_endpoint is not None:
            result['internal_endpoint'] = self.internal_endpoint
        if self.location is not None:
            result['location'] = self.location
        if self.ownership is not None:
            result['ownership'] = self.ownership
        if self.policy is not None:
            result['policy'] = self.policy
        if self.role_arn is not None:
            result['role_arn'] = self.role_arn
        if self.store_id is not None:
            result['store_id'] = self.store_id
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, map={}):
        if map.get('accelerate_endpoint') is not None:
            self.accelerate_endpoint = map.get('accelerate_endpoint')
        if map.get('base_path') is not None:
            self.base_path = map.get('base_path')
        if map.get('bucket') is not None:
            self.bucket = map.get('bucket')
        if map.get('cdn_endpoint') is not None:
            self.cdn_endpoint = map.get('cdn_endpoint')
        if map.get('customized_accelerate_endpoint') is not None:
            self.customized_accelerate_endpoint = map.get('customized_accelerate_endpoint')
        if map.get('customized_cdn_endpoint') is not None:
            self.customized_cdn_endpoint = map.get('customized_cdn_endpoint')
        if map.get('customized_endpoint') is not None:
            self.customized_endpoint = map.get('customized_endpoint')
        if map.get('customized_internal_endpoint') is not None:
            self.customized_internal_endpoint = map.get('customized_internal_endpoint')
        if map.get('domain_id') is not None:
            self.domain_id = map.get('domain_id')
        if map.get('endpoint') is not None:
            self.endpoint = map.get('endpoint')
        if map.get('internal_endpoint') is not None:
            self.internal_endpoint = map.get('internal_endpoint')
        if map.get('location') is not None:
            self.location = map.get('location')
        if map.get('ownership') is not None:
            self.ownership = map.get('ownership')
        if map.get('policy') is not None:
            self.policy = map.get('policy')
        if map.get('role_arn') is not None:
            self.role_arn = map.get('role_arn')
        if map.get('store_id') is not None:
            self.store_id = map.get('store_id')
        if map.get('type') is not None:
            self.type = map.get('type')
        return self


class AdminListStoresRequest(TeaModel):
    """
    *
    """
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        return self


class AppAccessStrategy(TeaModel):
    """
    *
    """
    def __init__(self, effect=None, except_app_id_list=None):
        self.effect = effect            # type: str
        self.except_app_id_list = except_app_id_list  # type: List[str]

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.effect is not None:
            result['effect'] = self.effect
        if self.except_app_id_list is not None:
            result['except_app_id_list'] = self.except_app_id_list
        return result

    def from_map(self, map={}):
        if map.get('effect') is not None:
            self.effect = map.get('effect')
        if map.get('except_app_id_list') is not None:
            self.except_app_id_list = map.get('except_app_id_list')
        return self


class AuthConfig(TeaModel):
    """
    *
    """
    def __init__(self, app_id=None, app_secret=None, callback_security=None, enable=None, endpoint=None,
                 enterprise_id=None, login_page_headers=None, login_page_template=None, login_page_vars=None):
        self.app_id = app_id            # type: str
        self.app_secret = app_secret    # type: str
        self.callback_security = callback_security  # type: bool
        self.enable = enable            # type: bool
        self.endpoint = endpoint        # type: str
        self.enterprise_id = enterprise_id  # type: str
        self.login_page_headers = login_page_headers  # type: dict
        self.login_page_template = login_page_template  # type: str
        self.login_page_vars = login_page_vars  # type: dict

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.app_id is not None:
            result['app_id'] = self.app_id
        if self.app_secret is not None:
            result['app_secret'] = self.app_secret
        if self.callback_security is not None:
            result['callback_security'] = self.callback_security
        if self.enable is not None:
            result['enable'] = self.enable
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.enterprise_id is not None:
            result['enterprise_id'] = self.enterprise_id
        if self.login_page_headers is not None:
            result['login_page_headers'] = self.login_page_headers
        if self.login_page_template is not None:
            result['login_page_template'] = self.login_page_template
        if self.login_page_vars is not None:
            result['login_page_vars'] = self.login_page_vars
        return result

    def from_map(self, map={}):
        if map.get('app_id') is not None:
            self.app_id = map.get('app_id')
        if map.get('app_secret') is not None:
            self.app_secret = map.get('app_secret')
        if map.get('callback_security') is not None:
            self.callback_security = map.get('callback_security')
        if map.get('enable') is not None:
            self.enable = map.get('enable')
        if map.get('endpoint') is not None:
            self.endpoint = map.get('endpoint')
        if map.get('enterprise_id') is not None:
            self.enterprise_id = map.get('enterprise_id')
        if map.get('login_page_headers') is not None:
            self.login_page_headers = map.get('login_page_headers')
        if map.get('login_page_template') is not None:
            self.login_page_template = map.get('login_page_template')
        if map.get('login_page_vars') is not None:
            self.login_page_vars = map.get('login_page_vars')
        return self


class BaseDomainResponse(TeaModel):
    """
    base domain response
    """
    def __init__(self, api_cname=None, auth_alipay_app_id=None, auth_alipay_enable=None,
                 auth_alipay_private_key=None, auth_config=None, auth_dingding_app_id=None, auth_dingding_app_secret=None,
                 auth_dingding_enable=None, auth_endpoint_enable=None, auth_ram_app_id=None, auth_ram_app_secret=None,
                 auth_ram_enable=None, created_at=None, data_hash_name=None, description=None, domain_id=None, domain_name=None,
                 event_filename_matches=None, event_mns_endpoint=None, event_mns_topic=None, event_names=None, event_role_arn=None,
                 init_drive_enable=None, init_drive_size=None, init_drive_store_id=None, mode=None, path_type=None,
                 published_app_access_strategy=None, sharable=None, store_level=None, store_region_list=None, updated_at=None):
        # Domain CName
        self.api_cname = api_cname      # type: str
        # 支付宝 App Id
        self.auth_alipay_app_id = auth_alipay_app_id  # type: str
        # 是否开启了支付宝认证
        self.auth_alipay_enable = auth_alipay_enable  # type: bool
        # 支付宝 App Secret
        self.auth_alipay_private_key = auth_alipay_private_key  # type: str
        # 登录相关信息
        self.auth_config = auth_config  # type: dict
        # 钉钉 App Id
        self.auth_dingding_app_id = auth_dingding_app_id  # type: str
        # 钉钉 App Secret
        self.auth_dingding_app_secret = auth_dingding_app_secret  # type: str
        # 是否开启了钉钉认证
        self.auth_dingding_enable = auth_dingding_enable  # type: bool
        self.auth_endpoint_enable = auth_endpoint_enable  # type: bool
        # RAM App Id
        self.auth_ram_app_id = auth_ram_app_id  # type: str
        # RAM App Secret
        self.auth_ram_app_secret = auth_ram_app_secret  # type: str
        # 是否开启了 RAM 认证
        self.auth_ram_enable = auth_ram_enable  # type: bool
        # Domain 创建时间
        self.created_at = created_at    # type: str
        # 数据 Hash 算法
        self.data_hash_name = data_hash_name  # type: str
        # Domain 描述
        self.description = description  # type: str
        # Domain ID
        self.domain_id = domain_id      # type: str
        # Domain 描述
        self.domain_name = domain_name  # type: str
        # 事件通知 MNS 匹配文件名
        self.event_filename_matches = event_filename_matches  # type: str
        # 事件通知 MNS Endpoint
        self.event_mns_endpoint = event_mns_endpoint  # type: str
        # 事件通知 MNS Topic
        self.event_mns_topic = event_mns_topic  # type: str
        # 事件名列表
        self.event_names = event_names  # type: List[str]
        # 事件通知 Role Arn
        self.event_role_arn = event_role_arn  # type: str
        # 是否开启了自动初始化 Drive
        self.init_drive_enable = init_drive_enable  # type: bool
        # 自动初始化 Drive 大小
        self.init_drive_size = init_drive_size  # type: int
        # 自动初始化 Drive 所用 Store ID
        self.init_drive_store_id = init_drive_store_id  # type: str
        # Domain 类型
        self.mode = mode                # type: str
        # Domain 类型
        self.path_type = path_type      # type: str
        self.published_app_access_strategy = published_app_access_strategy  # type: AppAccessStrategy
        # 是否开启了分享
        self.sharable = sharable        # type: bool
        # 存储级别
        self.store_level = store_level  # type: str
        # 存储 Region 列表
        self.store_region_list = store_region_list  # type: List[str]
        # Domain 更新时间
        self.updated_at = updated_at    # type: str

    def validate(self):
        if self.published_app_access_strategy:
            self.published_app_access_strategy.validate()

    def to_map(self):
        result = {}
        if self.api_cname is not None:
            result['api_cname'] = self.api_cname
        if self.auth_alipay_app_id is not None:
            result['auth_alipay_app_id'] = self.auth_alipay_app_id
        if self.auth_alipay_enable is not None:
            result['auth_alipay_enable'] = self.auth_alipay_enable
        if self.auth_alipay_private_key is not None:
            result['auth_alipay_private_key'] = self.auth_alipay_private_key
        if self.auth_config is not None:
            result['auth_config'] = self.auth_config
        if self.auth_dingding_app_id is not None:
            result['auth_dingding_app_id'] = self.auth_dingding_app_id
        if self.auth_dingding_app_secret is not None:
            result['auth_dingding_app_secret'] = self.auth_dingding_app_secret
        if self.auth_dingding_enable is not None:
            result['auth_dingding_enable'] = self.auth_dingding_enable
        if self.auth_endpoint_enable is not None:
            result['auth_endpoint_enable'] = self.auth_endpoint_enable
        if self.auth_ram_app_id is not None:
            result['auth_ram_app_id'] = self.auth_ram_app_id
        if self.auth_ram_app_secret is not None:
            result['auth_ram_app_secret'] = self.auth_ram_app_secret
        if self.auth_ram_enable is not None:
            result['auth_ram_enable'] = self.auth_ram_enable
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.data_hash_name is not None:
            result['data_hash_name'] = self.data_hash_name
        if self.description is not None:
            result['description'] = self.description
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.domain_name is not None:
            result['domain_name'] = self.domain_name
        if self.event_filename_matches is not None:
            result['event_filename_matches'] = self.event_filename_matches
        if self.event_mns_endpoint is not None:
            result['event_mns_endpoint'] = self.event_mns_endpoint
        if self.event_mns_topic is not None:
            result['event_mns_topic'] = self.event_mns_topic
        if self.event_names is not None:
            result['event_names'] = self.event_names
        if self.event_role_arn is not None:
            result['event_role_arn'] = self.event_role_arn
        if self.init_drive_enable is not None:
            result['init_drive_enable'] = self.init_drive_enable
        if self.init_drive_size is not None:
            result['init_drive_size'] = self.init_drive_size
        if self.init_drive_store_id is not None:
            result['init_drive_store_id'] = self.init_drive_store_id
        if self.mode is not None:
            result['mode'] = self.mode
        if self.path_type is not None:
            result['path_type'] = self.path_type
        if self.published_app_access_strategy is not None:
            result['published_app_access_strategy'] = self.published_app_access_strategy.to_map()
        if self.sharable is not None:
            result['sharable'] = self.sharable
        if self.store_level is not None:
            result['store_level'] = self.store_level
        if self.store_region_list is not None:
            result['store_region_list'] = self.store_region_list
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        return result

    def from_map(self, map={}):
        if map.get('api_cname') is not None:
            self.api_cname = map.get('api_cname')
        if map.get('auth_alipay_app_id') is not None:
            self.auth_alipay_app_id = map.get('auth_alipay_app_id')
        if map.get('auth_alipay_enable') is not None:
            self.auth_alipay_enable = map.get('auth_alipay_enable')
        if map.get('auth_alipay_private_key') is not None:
            self.auth_alipay_private_key = map.get('auth_alipay_private_key')
        if map.get('auth_config') is not None:
            self.auth_config = map.get('auth_config')
        if map.get('auth_dingding_app_id') is not None:
            self.auth_dingding_app_id = map.get('auth_dingding_app_id')
        if map.get('auth_dingding_app_secret') is not None:
            self.auth_dingding_app_secret = map.get('auth_dingding_app_secret')
        if map.get('auth_dingding_enable') is not None:
            self.auth_dingding_enable = map.get('auth_dingding_enable')
        if map.get('auth_endpoint_enable') is not None:
            self.auth_endpoint_enable = map.get('auth_endpoint_enable')
        if map.get('auth_ram_app_id') is not None:
            self.auth_ram_app_id = map.get('auth_ram_app_id')
        if map.get('auth_ram_app_secret') is not None:
            self.auth_ram_app_secret = map.get('auth_ram_app_secret')
        if map.get('auth_ram_enable') is not None:
            self.auth_ram_enable = map.get('auth_ram_enable')
        if map.get('created_at') is not None:
            self.created_at = map.get('created_at')
        if map.get('data_hash_name') is not None:
            self.data_hash_name = map.get('data_hash_name')
        if map.get('description') is not None:
            self.description = map.get('description')
        if map.get('domain_id') is not None:
            self.domain_id = map.get('domain_id')
        if map.get('domain_name') is not None:
            self.domain_name = map.get('domain_name')
        if map.get('event_filename_matches') is not None:
            self.event_filename_matches = map.get('event_filename_matches')
        if map.get('event_mns_endpoint') is not None:
            self.event_mns_endpoint = map.get('event_mns_endpoint')
        if map.get('event_mns_topic') is not None:
            self.event_mns_topic = map.get('event_mns_topic')
        if map.get('event_names') is not None:
            self.event_names = map.get('event_names')
        if map.get('event_role_arn') is not None:
            self.event_role_arn = map.get('event_role_arn')
        if map.get('init_drive_enable') is not None:
            self.init_drive_enable = map.get('init_drive_enable')
        if map.get('init_drive_size') is not None:
            self.init_drive_size = map.get('init_drive_size')
        if map.get('init_drive_store_id') is not None:
            self.init_drive_store_id = map.get('init_drive_store_id')
        if map.get('mode') is not None:
            self.mode = map.get('mode')
        if map.get('path_type') is not None:
            self.path_type = map.get('path_type')
        if map.get('published_app_access_strategy') is not None:
            temp_model = AppAccessStrategy()
            self.published_app_access_strategy = temp_model.from_map(map['published_app_access_strategy'])
        if map.get('sharable') is not None:
            self.sharable = map.get('sharable')
        if map.get('store_level') is not None:
            self.store_level = map.get('store_level')
        if map.get('store_region_list') is not None:
            self.store_region_list = map.get('store_region_list')
        if map.get('updated_at') is not None:
            self.updated_at = map.get('updated_at')
        return self


class CNameStatus(TeaModel):
    """
    *
    """
    def __init__(self, bingding_state=None, legal_state=None, remark=None):
        # binding state
        self.bingding_state = bingding_state  # type: str
        # legal state
        self.legal_state = legal_state  # type: str
        # remark
        self.remark = remark            # type: str

    def validate(self):
        self.validate_required(self.bingding_state, 'bingding_state')
        self.validate_required(self.legal_state, 'legal_state')
        self.validate_required(self.remark, 'remark')

    def to_map(self):
        result = {}
        if self.bingding_state is not None:
            result['bingding_state'] = self.bingding_state
        if self.legal_state is not None:
            result['legal_state'] = self.legal_state
        if self.remark is not None:
            result['remark'] = self.remark
        return result

    def from_map(self, map={}):
        if map.get('bingding_state') is not None:
            self.bingding_state = map.get('bingding_state')
        if map.get('legal_state') is not None:
            self.legal_state = map.get('legal_state')
        if map.get('remark') is not None:
            self.remark = map.get('remark')
        return self


class CreateDomainResponse(TeaModel):
    """
    create domain response
    """
    def __init__(self, api_cname=None, auth_alipay_app_id=None, auth_alipay_enable=None,
                 auth_alipay_private_key=None, auth_config=None, auth_dingding_app_id=None, auth_dingding_app_secret=None,
                 auth_dingding_enable=None, auth_endpoint_enable=None, auth_ram_app_id=None, auth_ram_app_secret=None,
                 auth_ram_enable=None, created_at=None, data_hash_name=None, description=None, domain_id=None, domain_name=None,
                 event_filename_matches=None, event_mns_endpoint=None, event_mns_topic=None, event_names=None, event_role_arn=None,
                 init_drive_enable=None, init_drive_size=None, init_drive_store_id=None, mode=None, path_type=None,
                 published_app_access_strategy=None, sharable=None, store_level=None, store_region_list=None, updated_at=None):
        # Domain CName
        self.api_cname = api_cname      # type: str
        # 支付宝 App Id
        self.auth_alipay_app_id = auth_alipay_app_id  # type: str
        # 是否开启了支付宝认证
        self.auth_alipay_enable = auth_alipay_enable  # type: bool
        # 支付宝 App Secret
        self.auth_alipay_private_key = auth_alipay_private_key  # type: str
        # 登录相关信息
        self.auth_config = auth_config  # type: dict
        # 钉钉 App Id
        self.auth_dingding_app_id = auth_dingding_app_id  # type: str
        # 钉钉 App Secret
        self.auth_dingding_app_secret = auth_dingding_app_secret  # type: str
        # 是否开启了钉钉认证
        self.auth_dingding_enable = auth_dingding_enable  # type: bool
        self.auth_endpoint_enable = auth_endpoint_enable  # type: bool
        # RAM App Id
        self.auth_ram_app_id = auth_ram_app_id  # type: str
        # RAM App Secret
        self.auth_ram_app_secret = auth_ram_app_secret  # type: str
        # 是否开启了 RAM 认证
        self.auth_ram_enable = auth_ram_enable  # type: bool
        # Domain 创建时间
        self.created_at = created_at    # type: str
        # 数据 Hash 算法
        self.data_hash_name = data_hash_name  # type: str
        # Domain 描述
        self.description = description  # type: str
        # Domain ID
        self.domain_id = domain_id      # type: str
        # Domain 描述
        self.domain_name = domain_name  # type: str
        # 事件通知 MNS 匹配文件名
        self.event_filename_matches = event_filename_matches  # type: str
        # 事件通知 MNS Endpoint
        self.event_mns_endpoint = event_mns_endpoint  # type: str
        # 事件通知 MNS Topic
        self.event_mns_topic = event_mns_topic  # type: str
        # 事件名列表
        self.event_names = event_names  # type: List[str]
        # 事件通知 Role Arn
        self.event_role_arn = event_role_arn  # type: str
        # 是否开启了自动初始化 Drive
        self.init_drive_enable = init_drive_enable  # type: bool
        # 自动初始化 Drive 大小
        self.init_drive_size = init_drive_size  # type: int
        # 自动初始化 Drive 所用 Store ID
        self.init_drive_store_id = init_drive_store_id  # type: str
        # Domain 类型
        self.mode = mode                # type: str
        # Domain 类型
        self.path_type = path_type      # type: str
        self.published_app_access_strategy = published_app_access_strategy  # type: AppAccessStrategy
        # 是否开启了分享
        self.sharable = sharable        # type: bool
        # 存储级别
        self.store_level = store_level  # type: str
        # 存储 Region 列表
        self.store_region_list = store_region_list  # type: List[str]
        # Domain 更新时间
        self.updated_at = updated_at    # type: str

    def validate(self):
        if self.published_app_access_strategy:
            self.published_app_access_strategy.validate()

    def to_map(self):
        result = {}
        if self.api_cname is not None:
            result['api_cname'] = self.api_cname
        if self.auth_alipay_app_id is not None:
            result['auth_alipay_app_id'] = self.auth_alipay_app_id
        if self.auth_alipay_enable is not None:
            result['auth_alipay_enable'] = self.auth_alipay_enable
        if self.auth_alipay_private_key is not None:
            result['auth_alipay_private_key'] = self.auth_alipay_private_key
        if self.auth_config is not None:
            result['auth_config'] = self.auth_config
        if self.auth_dingding_app_id is not None:
            result['auth_dingding_app_id'] = self.auth_dingding_app_id
        if self.auth_dingding_app_secret is not None:
            result['auth_dingding_app_secret'] = self.auth_dingding_app_secret
        if self.auth_dingding_enable is not None:
            result['auth_dingding_enable'] = self.auth_dingding_enable
        if self.auth_endpoint_enable is not None:
            result['auth_endpoint_enable'] = self.auth_endpoint_enable
        if self.auth_ram_app_id is not None:
            result['auth_ram_app_id'] = self.auth_ram_app_id
        if self.auth_ram_app_secret is not None:
            result['auth_ram_app_secret'] = self.auth_ram_app_secret
        if self.auth_ram_enable is not None:
            result['auth_ram_enable'] = self.auth_ram_enable
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.data_hash_name is not None:
            result['data_hash_name'] = self.data_hash_name
        if self.description is not None:
            result['description'] = self.description
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.domain_name is not None:
            result['domain_name'] = self.domain_name
        if self.event_filename_matches is not None:
            result['event_filename_matches'] = self.event_filename_matches
        if self.event_mns_endpoint is not None:
            result['event_mns_endpoint'] = self.event_mns_endpoint
        if self.event_mns_topic is not None:
            result['event_mns_topic'] = self.event_mns_topic
        if self.event_names is not None:
            result['event_names'] = self.event_names
        if self.event_role_arn is not None:
            result['event_role_arn'] = self.event_role_arn
        if self.init_drive_enable is not None:
            result['init_drive_enable'] = self.init_drive_enable
        if self.init_drive_size is not None:
            result['init_drive_size'] = self.init_drive_size
        if self.init_drive_store_id is not None:
            result['init_drive_store_id'] = self.init_drive_store_id
        if self.mode is not None:
            result['mode'] = self.mode
        if self.path_type is not None:
            result['path_type'] = self.path_type
        if self.published_app_access_strategy is not None:
            result['published_app_access_strategy'] = self.published_app_access_strategy.to_map()
        if self.sharable is not None:
            result['sharable'] = self.sharable
        if self.store_level is not None:
            result['store_level'] = self.store_level
        if self.store_region_list is not None:
            result['store_region_list'] = self.store_region_list
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        return result

    def from_map(self, map={}):
        if map.get('api_cname') is not None:
            self.api_cname = map.get('api_cname')
        if map.get('auth_alipay_app_id') is not None:
            self.auth_alipay_app_id = map.get('auth_alipay_app_id')
        if map.get('auth_alipay_enable') is not None:
            self.auth_alipay_enable = map.get('auth_alipay_enable')
        if map.get('auth_alipay_private_key') is not None:
            self.auth_alipay_private_key = map.get('auth_alipay_private_key')
        if map.get('auth_config') is not None:
            self.auth_config = map.get('auth_config')
        if map.get('auth_dingding_app_id') is not None:
            self.auth_dingding_app_id = map.get('auth_dingding_app_id')
        if map.get('auth_dingding_app_secret') is not None:
            self.auth_dingding_app_secret = map.get('auth_dingding_app_secret')
        if map.get('auth_dingding_enable') is not None:
            self.auth_dingding_enable = map.get('auth_dingding_enable')
        if map.get('auth_endpoint_enable') is not None:
            self.auth_endpoint_enable = map.get('auth_endpoint_enable')
        if map.get('auth_ram_app_id') is not None:
            self.auth_ram_app_id = map.get('auth_ram_app_id')
        if map.get('auth_ram_app_secret') is not None:
            self.auth_ram_app_secret = map.get('auth_ram_app_secret')
        if map.get('auth_ram_enable') is not None:
            self.auth_ram_enable = map.get('auth_ram_enable')
        if map.get('created_at') is not None:
            self.created_at = map.get('created_at')
        if map.get('data_hash_name') is not None:
            self.data_hash_name = map.get('data_hash_name')
        if map.get('description') is not None:
            self.description = map.get('description')
        if map.get('domain_id') is not None:
            self.domain_id = map.get('domain_id')
        if map.get('domain_name') is not None:
            self.domain_name = map.get('domain_name')
        if map.get('event_filename_matches') is not None:
            self.event_filename_matches = map.get('event_filename_matches')
        if map.get('event_mns_endpoint') is not None:
            self.event_mns_endpoint = map.get('event_mns_endpoint')
        if map.get('event_mns_topic') is not None:
            self.event_mns_topic = map.get('event_mns_topic')
        if map.get('event_names') is not None:
            self.event_names = map.get('event_names')
        if map.get('event_role_arn') is not None:
            self.event_role_arn = map.get('event_role_arn')
        if map.get('init_drive_enable') is not None:
            self.init_drive_enable = map.get('init_drive_enable')
        if map.get('init_drive_size') is not None:
            self.init_drive_size = map.get('init_drive_size')
        if map.get('init_drive_store_id') is not None:
            self.init_drive_store_id = map.get('init_drive_store_id')
        if map.get('mode') is not None:
            self.mode = map.get('mode')
        if map.get('path_type') is not None:
            self.path_type = map.get('path_type')
        if map.get('published_app_access_strategy') is not None:
            temp_model = AppAccessStrategy()
            self.published_app_access_strategy = temp_model.from_map(map['published_app_access_strategy'])
        if map.get('sharable') is not None:
            self.sharable = map.get('sharable')
        if map.get('store_level') is not None:
            self.store_level = map.get('store_level')
        if map.get('store_region_list') is not None:
            self.store_region_list = map.get('store_region_list')
        if map.get('updated_at') is not None:
            self.updated_at = map.get('updated_at')
        return self


class DataCName(TeaModel):
    """
    *
    """
    def __init__(self, data_cname=None, location=None):
        # datacname
        self.data_cname = data_cname    # type: str
        # data location
        self.location = location        # type: str

    def validate(self):
        self.validate_required(self.data_cname, 'data_cname')
        self.validate_required(self.location, 'location')

    def to_map(self):
        result = {}
        if self.data_cname is not None:
            result['data_cname'] = self.data_cname
        if self.location is not None:
            result['location'] = self.location
        return result

    def from_map(self, map={}):
        if map.get('data_cname') is not None:
            self.data_cname = map.get('data_cname')
        if map.get('location') is not None:
            self.location = map.get('location')
        return self


class DomainCNameResponse(TeaModel):
    """
    *
    """
    def __init__(self, data_cname_list=None, domain_id=None):
        # data cname list
        self.data_cname_list = data_cname_list  # type: List[DataCName]
        # domain ID
        self.domain_id = domain_id      # type: str

    def validate(self):
        self.validate_required(self.data_cname_list, 'data_cname_list')
        if self.data_cname_list:
            for k in self.data_cname_list:
                if k:
                    k.validate()
        self.validate_required(self.domain_id, 'domain_id')

    def to_map(self):
        result = {}
        result['data_cname_list'] = []
        if self.data_cname_list is not None:
            for k in self.data_cname_list:
                result['data_cname_list'].append(k.to_map() if k else None)
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        return result

    def from_map(self, map={}):
        self.data_cname_list = []
        if map.get('data_cname_list') is not None:
            for k in map.get('data_cname_list'):
                temp_model = DataCName()
                self.data_cname_list.append(temp_model.from_map(k))
        if map.get('domain_id') is not None:
            self.domain_id = map.get('domain_id')
        return self


class GetAppPublicKeyResponse(TeaModel):
    """
    *
    """
    def __init__(self, app_id=None, public_key=None):
        # App ID
        self.app_id = app_id            # type: str
        # RSA加密算法的公钥, PEM格式
        self.public_key = public_key    # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.public_key, 'public_key')

    def to_map(self):
        result = {}
        if self.app_id is not None:
            result['app_id'] = self.app_id
        if self.public_key is not None:
            result['public_key'] = self.public_key
        return result

    def from_map(self, map={}):
        if map.get('app_id') is not None:
            self.app_id = map.get('app_id')
        if map.get('public_key') is not None:
            self.public_key = map.get('public_key')
        return self


class GetAppResponse(TeaModel):
    """
    *
    """
    def __init__(self, ali_owner_id=None, app_id=None, app_name=None, app_secret=None, created_at=None,
                 description=None, logo=None, provider=None, redirect_uri=None, scope=None, screenshots=None, stage=None,
                 type=None, updated_at=None):
        # App 拥有者
        self.ali_owner_id = ali_owner_id  # type: str
        # App ID
        self.app_id = app_id            # type: str
        # App名称
        self.app_name = app_name        # type: str
        # App 秘钥
        self.app_secret = app_secret    # type: str
        # App 创建时间
        self.created_at = created_at    # type: str
        # App描述
        self.description = description  # type: str
        # App图标
        self.logo = logo                # type: str
        # App 提供方
        self.provider = provider        # type: str
        # App回调地址
        self.redirect_uri = redirect_uri  # type: str
        # App权限列表
        self.scope = scope              # type: List[str]
        # App 屏幕截图
        self.screenshots = screenshots  # type: List[str]
        # App 当前阶段
        self.stage = stage              # type: str
        # App类型
        self.type = type                # type: str
        # App 修改时间
        self.updated_at = updated_at    # type: str

    def validate(self):
        self.validate_required(self.ali_owner_id, 'ali_owner_id')
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.app_name, 'app_name')
        if self.app_name is not None:
            self.validate_max_length(self.app_name, 'app_name', 128)
            self.validate_pattern(self.app_name, 'app_name', '[0-9a-zA-Z]+')
        self.validate_required(self.app_secret, 'app_secret')
        self.validate_required(self.created_at, 'created_at')
        self.validate_required(self.description, 'description')
        if self.description is not None:
            self.validate_max_length(self.description, 'description', 128)
        self.validate_required(self.logo, 'logo')
        self.validate_required(self.provider, 'provider')
        self.validate_required(self.redirect_uri, 'redirect_uri')
        self.validate_required(self.scope, 'scope')
        self.validate_required(self.screenshots, 'screenshots')
        self.validate_required(self.stage, 'stage')
        self.validate_required(self.type, 'type')
        self.validate_required(self.updated_at, 'updated_at')

    def to_map(self):
        result = {}
        if self.ali_owner_id is not None:
            result['ali_owner_id'] = self.ali_owner_id
        if self.app_id is not None:
            result['app_id'] = self.app_id
        if self.app_name is not None:
            result['app_name'] = self.app_name
        if self.app_secret is not None:
            result['app_secret'] = self.app_secret
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.logo is not None:
            result['logo'] = self.logo
        if self.provider is not None:
            result['provider'] = self.provider
        if self.redirect_uri is not None:
            result['redirect_uri'] = self.redirect_uri
        if self.scope is not None:
            result['scope'] = self.scope
        if self.screenshots is not None:
            result['screenshots'] = self.screenshots
        if self.stage is not None:
            result['stage'] = self.stage
        if self.type is not None:
            result['type'] = self.type
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        return result

    def from_map(self, map={}):
        if map.get('ali_owner_id') is not None:
            self.ali_owner_id = map.get('ali_owner_id')
        if map.get('app_id') is not None:
            self.app_id = map.get('app_id')
        if map.get('app_name') is not None:
            self.app_name = map.get('app_name')
        if map.get('app_secret') is not None:
            self.app_secret = map.get('app_secret')
        if map.get('created_at') is not None:
            self.created_at = map.get('created_at')
        if map.get('description') is not None:
            self.description = map.get('description')
        if map.get('logo') is not None:
            self.logo = map.get('logo')
        if map.get('provider') is not None:
            self.provider = map.get('provider')
        if map.get('redirect_uri') is not None:
            self.redirect_uri = map.get('redirect_uri')
        if map.get('scope') is not None:
            self.scope = map.get('scope')
        if map.get('screenshots') is not None:
            self.screenshots = map.get('screenshots')
        if map.get('stage') is not None:
            self.stage = map.get('stage')
        if map.get('type') is not None:
            self.type = map.get('type')
        if map.get('updated_at') is not None:
            self.updated_at = map.get('updated_at')
        return self


class GetBizCNameInfoResponse(TeaModel):
    """
    *
    """
    def __init__(self, biz_cname=None, cert_id=None, cert_name=None, cname_status=None, cname_type=None,
                 domain_id=None, is_vpc=None):
        # biz cname
        self.biz_cname = biz_cname      # type: str
        # cert name
        self.cert_id = cert_id          # type: str
        # cert name
        self.cert_name = cert_name      # type: str
        self.cname_status = cname_status  # type: CNameStatus
        # cname type
        self.cname_type = cname_type    # type: str
        # domain ID
        self.domain_id = domain_id      # type: str
        # is vpc
        self.is_vpc = is_vpc            # type: bool

    def validate(self):
        if self.cname_status:
            self.cname_status.validate()
        self.validate_required(self.domain_id, 'domain_id')

    def to_map(self):
        result = {}
        if self.biz_cname is not None:
            result['biz_cname'] = self.biz_cname
        if self.cert_id is not None:
            result['cert_id'] = self.cert_id
        if self.cert_name is not None:
            result['cert_name'] = self.cert_name
        if self.cname_status is not None:
            result['cname_status'] = self.cname_status.to_map()
        if self.cname_type is not None:
            result['cname_type'] = self.cname_type
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.is_vpc is not None:
            result['is_vpc'] = self.is_vpc
        return result

    def from_map(self, map={}):
        if map.get('biz_cname') is not None:
            self.biz_cname = map.get('biz_cname')
        if map.get('cert_id') is not None:
            self.cert_id = map.get('cert_id')
        if map.get('cert_name') is not None:
            self.cert_name = map.get('cert_name')
        if map.get('cname_status') is not None:
            temp_model = CNameStatus()
            self.cname_status = temp_model.from_map(map['cname_status'])
        if map.get('cname_type') is not None:
            self.cname_type = map.get('cname_type')
        if map.get('domain_id') is not None:
            self.domain_id = map.get('domain_id')
        if map.get('is_vpc') is not None:
            self.is_vpc = map.get('is_vpc')
        return self


class GetDomainResponse(TeaModel):
    """
    get domain response
    """
    def __init__(self, api_cname=None, auth_alipay_app_id=None, auth_alipay_enable=None,
                 auth_alipay_private_key=None, auth_config=None, auth_dingding_app_id=None, auth_dingding_app_secret=None,
                 auth_dingding_enable=None, auth_endpoint_enable=None, auth_ram_app_id=None, auth_ram_app_secret=None,
                 auth_ram_enable=None, created_at=None, data_hash_name=None, description=None, domain_id=None, domain_name=None,
                 event_filename_matches=None, event_mns_endpoint=None, event_mns_topic=None, event_names=None, event_role_arn=None,
                 init_drive_enable=None, init_drive_size=None, init_drive_store_id=None, mode=None, path_type=None,
                 published_app_access_strategy=None, sharable=None, store_level=None, store_region_list=None, updated_at=None):
        # Domain CName
        self.api_cname = api_cname      # type: str
        # 支付宝 App Id
        self.auth_alipay_app_id = auth_alipay_app_id  # type: str
        # 是否开启了支付宝认证
        self.auth_alipay_enable = auth_alipay_enable  # type: bool
        # 支付宝 App Secret
        self.auth_alipay_private_key = auth_alipay_private_key  # type: str
        # 登录相关信息
        self.auth_config = auth_config  # type: dict
        # 钉钉 App Id
        self.auth_dingding_app_id = auth_dingding_app_id  # type: str
        # 钉钉 App Secret
        self.auth_dingding_app_secret = auth_dingding_app_secret  # type: str
        # 是否开启了钉钉认证
        self.auth_dingding_enable = auth_dingding_enable  # type: bool
        self.auth_endpoint_enable = auth_endpoint_enable  # type: bool
        # RAM App Id
        self.auth_ram_app_id = auth_ram_app_id  # type: str
        # RAM App Secret
        self.auth_ram_app_secret = auth_ram_app_secret  # type: str
        # 是否开启了 RAM 认证
        self.auth_ram_enable = auth_ram_enable  # type: bool
        # Domain 创建时间
        self.created_at = created_at    # type: str
        # 数据 Hash 算法
        self.data_hash_name = data_hash_name  # type: str
        # Domain 描述
        self.description = description  # type: str
        # Domain ID
        self.domain_id = domain_id      # type: str
        # Domain 描述
        self.domain_name = domain_name  # type: str
        # 事件通知 MNS 匹配文件名
        self.event_filename_matches = event_filename_matches  # type: str
        # 事件通知 MNS Endpoint
        self.event_mns_endpoint = event_mns_endpoint  # type: str
        # 事件通知 MNS Topic
        self.event_mns_topic = event_mns_topic  # type: str
        # 事件名列表
        self.event_names = event_names  # type: List[str]
        # 事件通知 Role Arn
        self.event_role_arn = event_role_arn  # type: str
        # 是否开启了自动初始化 Drive
        self.init_drive_enable = init_drive_enable  # type: bool
        # 自动初始化 Drive 大小
        self.init_drive_size = init_drive_size  # type: int
        # 自动初始化 Drive 所用 Store ID
        self.init_drive_store_id = init_drive_store_id  # type: str
        # Domain 类型
        self.mode = mode                # type: str
        # Domain 类型
        self.path_type = path_type      # type: str
        self.published_app_access_strategy = published_app_access_strategy  # type: AppAccessStrategy
        # 是否开启了分享
        self.sharable = sharable        # type: bool
        # 存储级别
        self.store_level = store_level  # type: str
        # 存储 Region 列表
        self.store_region_list = store_region_list  # type: List[str]
        # Domain 更新时间
        self.updated_at = updated_at    # type: str

    def validate(self):
        if self.published_app_access_strategy:
            self.published_app_access_strategy.validate()

    def to_map(self):
        result = {}
        if self.api_cname is not None:
            result['api_cname'] = self.api_cname
        if self.auth_alipay_app_id is not None:
            result['auth_alipay_app_id'] = self.auth_alipay_app_id
        if self.auth_alipay_enable is not None:
            result['auth_alipay_enable'] = self.auth_alipay_enable
        if self.auth_alipay_private_key is not None:
            result['auth_alipay_private_key'] = self.auth_alipay_private_key
        if self.auth_config is not None:
            result['auth_config'] = self.auth_config
        if self.auth_dingding_app_id is not None:
            result['auth_dingding_app_id'] = self.auth_dingding_app_id
        if self.auth_dingding_app_secret is not None:
            result['auth_dingding_app_secret'] = self.auth_dingding_app_secret
        if self.auth_dingding_enable is not None:
            result['auth_dingding_enable'] = self.auth_dingding_enable
        if self.auth_endpoint_enable is not None:
            result['auth_endpoint_enable'] = self.auth_endpoint_enable
        if self.auth_ram_app_id is not None:
            result['auth_ram_app_id'] = self.auth_ram_app_id
        if self.auth_ram_app_secret is not None:
            result['auth_ram_app_secret'] = self.auth_ram_app_secret
        if self.auth_ram_enable is not None:
            result['auth_ram_enable'] = self.auth_ram_enable
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.data_hash_name is not None:
            result['data_hash_name'] = self.data_hash_name
        if self.description is not None:
            result['description'] = self.description
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.domain_name is not None:
            result['domain_name'] = self.domain_name
        if self.event_filename_matches is not None:
            result['event_filename_matches'] = self.event_filename_matches
        if self.event_mns_endpoint is not None:
            result['event_mns_endpoint'] = self.event_mns_endpoint
        if self.event_mns_topic is not None:
            result['event_mns_topic'] = self.event_mns_topic
        if self.event_names is not None:
            result['event_names'] = self.event_names
        if self.event_role_arn is not None:
            result['event_role_arn'] = self.event_role_arn
        if self.init_drive_enable is not None:
            result['init_drive_enable'] = self.init_drive_enable
        if self.init_drive_size is not None:
            result['init_drive_size'] = self.init_drive_size
        if self.init_drive_store_id is not None:
            result['init_drive_store_id'] = self.init_drive_store_id
        if self.mode is not None:
            result['mode'] = self.mode
        if self.path_type is not None:
            result['path_type'] = self.path_type
        if self.published_app_access_strategy is not None:
            result['published_app_access_strategy'] = self.published_app_access_strategy.to_map()
        if self.sharable is not None:
            result['sharable'] = self.sharable
        if self.store_level is not None:
            result['store_level'] = self.store_level
        if self.store_region_list is not None:
            result['store_region_list'] = self.store_region_list
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        return result

    def from_map(self, map={}):
        if map.get('api_cname') is not None:
            self.api_cname = map.get('api_cname')
        if map.get('auth_alipay_app_id') is not None:
            self.auth_alipay_app_id = map.get('auth_alipay_app_id')
        if map.get('auth_alipay_enable') is not None:
            self.auth_alipay_enable = map.get('auth_alipay_enable')
        if map.get('auth_alipay_private_key') is not None:
            self.auth_alipay_private_key = map.get('auth_alipay_private_key')
        if map.get('auth_config') is not None:
            self.auth_config = map.get('auth_config')
        if map.get('auth_dingding_app_id') is not None:
            self.auth_dingding_app_id = map.get('auth_dingding_app_id')
        if map.get('auth_dingding_app_secret') is not None:
            self.auth_dingding_app_secret = map.get('auth_dingding_app_secret')
        if map.get('auth_dingding_enable') is not None:
            self.auth_dingding_enable = map.get('auth_dingding_enable')
        if map.get('auth_endpoint_enable') is not None:
            self.auth_endpoint_enable = map.get('auth_endpoint_enable')
        if map.get('auth_ram_app_id') is not None:
            self.auth_ram_app_id = map.get('auth_ram_app_id')
        if map.get('auth_ram_app_secret') is not None:
            self.auth_ram_app_secret = map.get('auth_ram_app_secret')
        if map.get('auth_ram_enable') is not None:
            self.auth_ram_enable = map.get('auth_ram_enable')
        if map.get('created_at') is not None:
            self.created_at = map.get('created_at')
        if map.get('data_hash_name') is not None:
            self.data_hash_name = map.get('data_hash_name')
        if map.get('description') is not None:
            self.description = map.get('description')
        if map.get('domain_id') is not None:
            self.domain_id = map.get('domain_id')
        if map.get('domain_name') is not None:
            self.domain_name = map.get('domain_name')
        if map.get('event_filename_matches') is not None:
            self.event_filename_matches = map.get('event_filename_matches')
        if map.get('event_mns_endpoint') is not None:
            self.event_mns_endpoint = map.get('event_mns_endpoint')
        if map.get('event_mns_topic') is not None:
            self.event_mns_topic = map.get('event_mns_topic')
        if map.get('event_names') is not None:
            self.event_names = map.get('event_names')
        if map.get('event_role_arn') is not None:
            self.event_role_arn = map.get('event_role_arn')
        if map.get('init_drive_enable') is not None:
            self.init_drive_enable = map.get('init_drive_enable')
        if map.get('init_drive_size') is not None:
            self.init_drive_size = map.get('init_drive_size')
        if map.get('init_drive_store_id') is not None:
            self.init_drive_store_id = map.get('init_drive_store_id')
        if map.get('mode') is not None:
            self.mode = map.get('mode')
        if map.get('path_type') is not None:
            self.path_type = map.get('path_type')
        if map.get('published_app_access_strategy') is not None:
            temp_model = AppAccessStrategy()
            self.published_app_access_strategy = temp_model.from_map(map['published_app_access_strategy'])
        if map.get('sharable') is not None:
            self.sharable = map.get('sharable')
        if map.get('store_level') is not None:
            self.store_level = map.get('store_level')
        if map.get('store_region_list') is not None:
            self.store_region_list = map.get('store_region_list')
        if map.get('updated_at') is not None:
            self.updated_at = map.get('updated_at')
        return self


class GetUserAccessTokenRequest(TeaModel):
    """
    *
    """
    def __init__(self, headers=None, role=None, user_id=None):
        self.headers = headers          # type: Dict[str, str]
        # 角色
        self.role = role                # type: str
        # 用户 ID
        self.user_id = user_id          # type: str

    def validate(self):
        self.validate_required(self.user_id, 'user_id')

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.role is not None:
            result['role'] = self.role
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('role') is not None:
            self.role = map.get('role')
        if map.get('user_id') is not None:
            self.user_id = map.get('user_id')
        return self


class ListAppsResponse(TeaModel):
    """
    *
    """
    def __init__(self, items=None, next_marker=None):
        # App 列表
        self.items = items              # type: List[GetAppResponse]
        # App 分批查询游标
        self.next_marker = next_marker  # type: str

    def validate(self):
        self.validate_required(self.items, 'items')
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, map={}):
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = GetAppResponse()
                self.items.append(temp_model.from_map(k))
        if map.get('next_marker') is not None:
            self.next_marker = map.get('next_marker')
        return self


class ListDomainCORSRuleResponse(TeaModel):
    """
    list domain cors response
    """
    def __init__(self, cors_rule_list=None, domain_id=None):
        # cors rule 列表
        self.cors_rule_list = cors_rule_list  # type: List[CorsRule]
        # Domain ID
        self.domain_id = domain_id      # type: str

    def validate(self):
        if self.cors_rule_list:
            for k in self.cors_rule_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['cors_rule_list'] = []
        if self.cors_rule_list is not None:
            for k in self.cors_rule_list:
                result['cors_rule_list'].append(k.to_map() if k else None)
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        return result

    def from_map(self, map={}):
        self.cors_rule_list = []
        if map.get('cors_rule_list') is not None:
            for k in map.get('cors_rule_list'):
                temp_model = CorsRule()
                self.cors_rule_list.append(temp_model.from_map(k))
        if map.get('domain_id') is not None:
            self.domain_id = map.get('domain_id')
        return self


class ListDomainsResponse(TeaModel):
    """
    list domain response
    """
    def __init__(self, items=None, next_marker=None):
        # domain 列表
        self.items = items              # type: List[BaseDomainResponse]
        # 下次分页查询游标
        self.next_marker = next_marker  # type: str

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, map={}):
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = BaseDomainResponse()
                self.items.append(temp_model.from_map(k))
        if map.get('next_marker') is not None:
            self.next_marker = map.get('next_marker')
        return self


class ListStoresResponse(TeaModel):
    """
    *
    """
    def __init__(self, items=None):
        # Store 列表
        self.items = items              # type: List[Store]

    def validate(self):
        self.validate_required(self.items, 'items')
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = Store()
                self.items.append(temp_model.from_map(k))
        return self


class SetBizCNameCertResponse(TeaModel):
    """
    *
    """
    def __init__(self, biz_cname=None, cert_name=None, cname_type=None, domain_id=None, is_vpc=None):
        # biz cname
        self.biz_cname = biz_cname      # type: str
        # cert name
        self.cert_name = cert_name      # type: str
        # cname type
        self.cname_type = cname_type    # type: str
        # domain ID
        self.domain_id = domain_id      # type: str
        # is vpc
        self.is_vpc = is_vpc            # type: bool

    def validate(self):
        self.validate_required(self.domain_id, 'domain_id')

    def to_map(self):
        result = {}
        if self.biz_cname is not None:
            result['biz_cname'] = self.biz_cname
        if self.cert_name is not None:
            result['cert_name'] = self.cert_name
        if self.cname_type is not None:
            result['cname_type'] = self.cname_type
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.is_vpc is not None:
            result['is_vpc'] = self.is_vpc
        return result

    def from_map(self, map={}):
        if map.get('biz_cname') is not None:
            self.biz_cname = map.get('biz_cname')
        if map.get('cert_name') is not None:
            self.cert_name = map.get('cert_name')
        if map.get('cname_type') is not None:
            self.cname_type = map.get('cname_type')
        if map.get('domain_id') is not None:
            self.domain_id = map.get('domain_id')
        if map.get('is_vpc') is not None:
            self.is_vpc = map.get('is_vpc')
        return self


class SetBizCNameResponse(TeaModel):
    """
    *
    """
    def __init__(self, biz_cname=None, cname_status=None, cname_type=None, domain_id=None, is_vpc=None):
        # biz cname
        self.biz_cname = biz_cname      # type: str
        self.cname_status = cname_status  # type: CNameStatus
        # cname type
        self.cname_type = cname_type    # type: str
        # domain ID
        self.domain_id = domain_id      # type: str
        # is vpc
        self.is_vpc = is_vpc            # type: bool

    def validate(self):
        if self.cname_status:
            self.cname_status.validate()
        self.validate_required(self.domain_id, 'domain_id')

    def to_map(self):
        result = {}
        if self.biz_cname is not None:
            result['biz_cname'] = self.biz_cname
        if self.cname_status is not None:
            result['cname_status'] = self.cname_status.to_map()
        if self.cname_type is not None:
            result['cname_type'] = self.cname_type
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.is_vpc is not None:
            result['is_vpc'] = self.is_vpc
        return result

    def from_map(self, map={}):
        if map.get('biz_cname') is not None:
            self.biz_cname = map.get('biz_cname')
        if map.get('cname_status') is not None:
            temp_model = CNameStatus()
            self.cname_status = temp_model.from_map(map['cname_status'])
        if map.get('cname_type') is not None:
            self.cname_type = map.get('cname_type')
        if map.get('domain_id') is not None:
            self.domain_id = map.get('domain_id')
        if map.get('is_vpc') is not None:
            self.is_vpc = map.get('is_vpc')
        return self


class SetDataCNameResponse(TeaModel):
    """
    *
    """
    def __init__(self, data_cname=None, domain_id=None, location=None):
        # datacname
        self.data_cname = data_cname    # type: str
        # domain ID
        self.domain_id = domain_id      # type: str
        # data location
        self.location = location        # type: str

    def validate(self):
        self.validate_required(self.data_cname, 'data_cname')
        self.validate_required(self.domain_id, 'domain_id')
        self.validate_required(self.location, 'location')

    def to_map(self):
        result = {}
        if self.data_cname is not None:
            result['data_cname'] = self.data_cname
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.location is not None:
            result['location'] = self.location
        return result

    def from_map(self, map={}):
        if map.get('data_cname') is not None:
            self.data_cname = map.get('data_cname')
        if map.get('domain_id') is not None:
            self.domain_id = map.get('domain_id')
        if map.get('location') is not None:
            self.location = map.get('location')
        return self


class Store(TeaModel):
    """
    *
    """
    def __init__(self, accelerate_endpoint=None, base_path=None, bucket=None, cdn_endpoint=None,
                 customized_accelerate_endpoint=None, customized_cdn_endpoint=None, customized_endpoint=None, customized_internal_endpoint=None,
                 endpoint=None, internal_endpoint=None, location=None, ownership=None, policy=None, role_arn=None,
                 store_id=None, type=None):
        # 全球加速地址
        self.accelerate_endpoint = accelerate_endpoint  # type: str
        # 存储公共前缀
        self.base_path = base_path      # type: str
        # bucket名称
        self.bucket = bucket            # type: str
        # 内容分发地址
        self.cdn_endpoint = cdn_endpoint  # type: str
        # 自定义全球加速地址
        self.customized_accelerate_endpoint = customized_accelerate_endpoint  # type: str
        # 自定义内容分发地址
        self.customized_cdn_endpoint = customized_cdn_endpoint  # type: str
        # 自定义Public访问地址
        self.customized_endpoint = customized_endpoint  # type: str
        # 自定义vpc访问地址
        self.customized_internal_endpoint = customized_internal_endpoint  # type: str
        # Public访问地址
        self.endpoint = endpoint        # type: str
        # vpc访问地址
        self.internal_endpoint = internal_endpoint  # type: str
        # 地点
        self.location = location        # type: str
        # 存储归属，system表示系统提供，custom表示使用自己的存储
        self.ownership = ownership      # type: str
        # Policy授权,system类型store会将bucket权限授予当前云账号
        self.policy = policy            # type: str
        # 访问Bucket的角色ARN
        self.role_arn = role_arn        # type: str
        # store ID
        self.store_id = store_id        # type: str
        # 存储类型，当前只支持oss
        self.type = type                # type: str

    def validate(self):
        self.validate_required(self.bucket, 'bucket')
        self.validate_required(self.endpoint, 'endpoint')
        self.validate_required(self.ownership, 'ownership')
        self.validate_required(self.policy, 'policy')
        self.validate_required(self.store_id, 'store_id')
        self.validate_required(self.type, 'type')

    def to_map(self):
        result = {}
        if self.accelerate_endpoint is not None:
            result['accelerate_endpoint'] = self.accelerate_endpoint
        if self.base_path is not None:
            result['base_path'] = self.base_path
        if self.bucket is not None:
            result['bucket'] = self.bucket
        if self.cdn_endpoint is not None:
            result['cdn_endpoint'] = self.cdn_endpoint
        if self.customized_accelerate_endpoint is not None:
            result['customized_accelerate_endpoint'] = self.customized_accelerate_endpoint
        if self.customized_cdn_endpoint is not None:
            result['customized_cdn_endpoint'] = self.customized_cdn_endpoint
        if self.customized_endpoint is not None:
            result['customized_endpoint'] = self.customized_endpoint
        if self.customized_internal_endpoint is not None:
            result['customized_internal_endpoint'] = self.customized_internal_endpoint
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.internal_endpoint is not None:
            result['internal_endpoint'] = self.internal_endpoint
        if self.location is not None:
            result['location'] = self.location
        if self.ownership is not None:
            result['ownership'] = self.ownership
        if self.policy is not None:
            result['policy'] = self.policy
        if self.role_arn is not None:
            result['role_arn'] = self.role_arn
        if self.store_id is not None:
            result['store_id'] = self.store_id
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, map={}):
        if map.get('accelerate_endpoint') is not None:
            self.accelerate_endpoint = map.get('accelerate_endpoint')
        if map.get('base_path') is not None:
            self.base_path = map.get('base_path')
        if map.get('bucket') is not None:
            self.bucket = map.get('bucket')
        if map.get('cdn_endpoint') is not None:
            self.cdn_endpoint = map.get('cdn_endpoint')
        if map.get('customized_accelerate_endpoint') is not None:
            self.customized_accelerate_endpoint = map.get('customized_accelerate_endpoint')
        if map.get('customized_cdn_endpoint') is not None:
            self.customized_cdn_endpoint = map.get('customized_cdn_endpoint')
        if map.get('customized_endpoint') is not None:
            self.customized_endpoint = map.get('customized_endpoint')
        if map.get('customized_internal_endpoint') is not None:
            self.customized_internal_endpoint = map.get('customized_internal_endpoint')
        if map.get('endpoint') is not None:
            self.endpoint = map.get('endpoint')
        if map.get('internal_endpoint') is not None:
            self.internal_endpoint = map.get('internal_endpoint')
        if map.get('location') is not None:
            self.location = map.get('location')
        if map.get('ownership') is not None:
            self.ownership = map.get('ownership')
        if map.get('policy') is not None:
            self.policy = map.get('policy')
        if map.get('role_arn') is not None:
            self.role_arn = map.get('role_arn')
        if map.get('store_id') is not None:
            self.store_id = map.get('store_id')
        if map.get('type') is not None:
            self.type = map.get('type')
        return self


class UpdateDomainResponse(TeaModel):
    """
    create domain response
    """
    def __init__(self, api_cname=None, auth_alipay_app_id=None, auth_alipay_enable=None,
                 auth_alipay_private_key=None, auth_config=None, auth_dingding_app_id=None, auth_dingding_app_secret=None,
                 auth_dingding_enable=None, auth_endpoint_enable=None, auth_ram_app_id=None, auth_ram_app_secret=None,
                 auth_ram_enable=None, created_at=None, data_hash_name=None, description=None, domain_id=None, domain_name=None,
                 event_filename_matches=None, event_mns_endpoint=None, event_mns_topic=None, event_names=None, event_role_arn=None,
                 init_drive_enable=None, init_drive_size=None, init_drive_store_id=None, mode=None, path_type=None,
                 published_app_access_strategy=None, sharable=None, store_level=None, store_region_list=None, updated_at=None):
        # Domain CName
        self.api_cname = api_cname      # type: str
        # 支付宝 App Id
        self.auth_alipay_app_id = auth_alipay_app_id  # type: str
        # 是否开启了支付宝认证
        self.auth_alipay_enable = auth_alipay_enable  # type: bool
        # 支付宝 App Secret
        self.auth_alipay_private_key = auth_alipay_private_key  # type: str
        # 登录相关信息
        self.auth_config = auth_config  # type: dict
        # 钉钉 App Id
        self.auth_dingding_app_id = auth_dingding_app_id  # type: str
        # 钉钉 App Secret
        self.auth_dingding_app_secret = auth_dingding_app_secret  # type: str
        # 是否开启了钉钉认证
        self.auth_dingding_enable = auth_dingding_enable  # type: bool
        self.auth_endpoint_enable = auth_endpoint_enable  # type: bool
        # RAM App Id
        self.auth_ram_app_id = auth_ram_app_id  # type: str
        # RAM App Secret
        self.auth_ram_app_secret = auth_ram_app_secret  # type: str
        # 是否开启了 RAM 认证
        self.auth_ram_enable = auth_ram_enable  # type: bool
        # Domain 创建时间
        self.created_at = created_at    # type: str
        # 数据 Hash 算法
        self.data_hash_name = data_hash_name  # type: str
        # Domain 描述
        self.description = description  # type: str
        # Domain ID
        self.domain_id = domain_id      # type: str
        # Domain 描述
        self.domain_name = domain_name  # type: str
        # 事件通知 MNS 匹配文件名
        self.event_filename_matches = event_filename_matches  # type: str
        # 事件通知 MNS Endpoint
        self.event_mns_endpoint = event_mns_endpoint  # type: str
        # 事件通知 MNS Topic
        self.event_mns_topic = event_mns_topic  # type: str
        # 事件名列表
        self.event_names = event_names  # type: List[str]
        # 事件通知 Role Arn
        self.event_role_arn = event_role_arn  # type: str
        # 是否开启了自动初始化 Drive
        self.init_drive_enable = init_drive_enable  # type: bool
        # 自动初始化 Drive 大小
        self.init_drive_size = init_drive_size  # type: int
        # 自动初始化 Drive 所用 Store ID
        self.init_drive_store_id = init_drive_store_id  # type: str
        # Domain 类型
        self.mode = mode                # type: str
        # Domain 类型
        self.path_type = path_type      # type: str
        self.published_app_access_strategy = published_app_access_strategy  # type: AppAccessStrategy
        # 是否开启了分享
        self.sharable = sharable        # type: bool
        # 存储级别
        self.store_level = store_level  # type: str
        # 存储 Region 列表
        self.store_region_list = store_region_list  # type: List[str]
        # Domain 更新时间
        self.updated_at = updated_at    # type: str

    def validate(self):
        if self.published_app_access_strategy:
            self.published_app_access_strategy.validate()

    def to_map(self):
        result = {}
        if self.api_cname is not None:
            result['api_cname'] = self.api_cname
        if self.auth_alipay_app_id is not None:
            result['auth_alipay_app_id'] = self.auth_alipay_app_id
        if self.auth_alipay_enable is not None:
            result['auth_alipay_enable'] = self.auth_alipay_enable
        if self.auth_alipay_private_key is not None:
            result['auth_alipay_private_key'] = self.auth_alipay_private_key
        if self.auth_config is not None:
            result['auth_config'] = self.auth_config
        if self.auth_dingding_app_id is not None:
            result['auth_dingding_app_id'] = self.auth_dingding_app_id
        if self.auth_dingding_app_secret is not None:
            result['auth_dingding_app_secret'] = self.auth_dingding_app_secret
        if self.auth_dingding_enable is not None:
            result['auth_dingding_enable'] = self.auth_dingding_enable
        if self.auth_endpoint_enable is not None:
            result['auth_endpoint_enable'] = self.auth_endpoint_enable
        if self.auth_ram_app_id is not None:
            result['auth_ram_app_id'] = self.auth_ram_app_id
        if self.auth_ram_app_secret is not None:
            result['auth_ram_app_secret'] = self.auth_ram_app_secret
        if self.auth_ram_enable is not None:
            result['auth_ram_enable'] = self.auth_ram_enable
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.data_hash_name is not None:
            result['data_hash_name'] = self.data_hash_name
        if self.description is not None:
            result['description'] = self.description
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.domain_name is not None:
            result['domain_name'] = self.domain_name
        if self.event_filename_matches is not None:
            result['event_filename_matches'] = self.event_filename_matches
        if self.event_mns_endpoint is not None:
            result['event_mns_endpoint'] = self.event_mns_endpoint
        if self.event_mns_topic is not None:
            result['event_mns_topic'] = self.event_mns_topic
        if self.event_names is not None:
            result['event_names'] = self.event_names
        if self.event_role_arn is not None:
            result['event_role_arn'] = self.event_role_arn
        if self.init_drive_enable is not None:
            result['init_drive_enable'] = self.init_drive_enable
        if self.init_drive_size is not None:
            result['init_drive_size'] = self.init_drive_size
        if self.init_drive_store_id is not None:
            result['init_drive_store_id'] = self.init_drive_store_id
        if self.mode is not None:
            result['mode'] = self.mode
        if self.path_type is not None:
            result['path_type'] = self.path_type
        if self.published_app_access_strategy is not None:
            result['published_app_access_strategy'] = self.published_app_access_strategy.to_map()
        if self.sharable is not None:
            result['sharable'] = self.sharable
        if self.store_level is not None:
            result['store_level'] = self.store_level
        if self.store_region_list is not None:
            result['store_region_list'] = self.store_region_list
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        return result

    def from_map(self, map={}):
        if map.get('api_cname') is not None:
            self.api_cname = map.get('api_cname')
        if map.get('auth_alipay_app_id') is not None:
            self.auth_alipay_app_id = map.get('auth_alipay_app_id')
        if map.get('auth_alipay_enable') is not None:
            self.auth_alipay_enable = map.get('auth_alipay_enable')
        if map.get('auth_alipay_private_key') is not None:
            self.auth_alipay_private_key = map.get('auth_alipay_private_key')
        if map.get('auth_config') is not None:
            self.auth_config = map.get('auth_config')
        if map.get('auth_dingding_app_id') is not None:
            self.auth_dingding_app_id = map.get('auth_dingding_app_id')
        if map.get('auth_dingding_app_secret') is not None:
            self.auth_dingding_app_secret = map.get('auth_dingding_app_secret')
        if map.get('auth_dingding_enable') is not None:
            self.auth_dingding_enable = map.get('auth_dingding_enable')
        if map.get('auth_endpoint_enable') is not None:
            self.auth_endpoint_enable = map.get('auth_endpoint_enable')
        if map.get('auth_ram_app_id') is not None:
            self.auth_ram_app_id = map.get('auth_ram_app_id')
        if map.get('auth_ram_app_secret') is not None:
            self.auth_ram_app_secret = map.get('auth_ram_app_secret')
        if map.get('auth_ram_enable') is not None:
            self.auth_ram_enable = map.get('auth_ram_enable')
        if map.get('created_at') is not None:
            self.created_at = map.get('created_at')
        if map.get('data_hash_name') is not None:
            self.data_hash_name = map.get('data_hash_name')
        if map.get('description') is not None:
            self.description = map.get('description')
        if map.get('domain_id') is not None:
            self.domain_id = map.get('domain_id')
        if map.get('domain_name') is not None:
            self.domain_name = map.get('domain_name')
        if map.get('event_filename_matches') is not None:
            self.event_filename_matches = map.get('event_filename_matches')
        if map.get('event_mns_endpoint') is not None:
            self.event_mns_endpoint = map.get('event_mns_endpoint')
        if map.get('event_mns_topic') is not None:
            self.event_mns_topic = map.get('event_mns_topic')
        if map.get('event_names') is not None:
            self.event_names = map.get('event_names')
        if map.get('event_role_arn') is not None:
            self.event_role_arn = map.get('event_role_arn')
        if map.get('init_drive_enable') is not None:
            self.init_drive_enable = map.get('init_drive_enable')
        if map.get('init_drive_size') is not None:
            self.init_drive_size = map.get('init_drive_size')
        if map.get('init_drive_store_id') is not None:
            self.init_drive_store_id = map.get('init_drive_store_id')
        if map.get('mode') is not None:
            self.mode = map.get('mode')
        if map.get('path_type') is not None:
            self.path_type = map.get('path_type')
        if map.get('published_app_access_strategy') is not None:
            temp_model = AppAccessStrategy()
            self.published_app_access_strategy = temp_model.from_map(map['published_app_access_strategy'])
        if map.get('sharable') is not None:
            self.sharable = map.get('sharable')
        if map.get('store_level') is not None:
            self.store_level = map.get('store_level')
        if map.get('store_region_list') is not None:
            self.store_region_list = map.get('store_region_list')
        if map.get('updated_at') is not None:
            self.updated_at = map.get('updated_at')
        return self


class GetAsyncTaskInfoModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: GetAsyncTaskResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetAsyncTaskResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class BatchOperationModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: BatchResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = BatchResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class CreateDriveModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: CreateDriveResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = CreateDriveResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class DeleteDriveModel(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        return self


class GetDriveModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: GetDriveResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetDriveResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class GetDefaultDriveModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: GetDriveResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetDriveResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class ListDrivesModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: ListDriveResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = ListDriveResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class ListMyDrivesModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: ListDriveResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = ListDriveResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class UpdateDriveModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: UpdateDriveResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = UpdateDriveResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class CompleteFileModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: CompleteFileResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = CompleteFileResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class CopyFileModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: CopyFileResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = CopyFileResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class CreateFileModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: CreateFileResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = CreateFileResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class DeleteFileModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: DeleteFileResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = DeleteFileResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class GetFileModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: GetFileResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetFileResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class GetFileByPathModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: GetFileByPathResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetFileByPathResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class GetDownloadUrlModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: GetDownloadUrlResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetDownloadUrlResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class GetLastCursorModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: GetLastCursorResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetLastCursorResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class GetMediaPlayUrlModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: GetMediaPlayURLResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetMediaPlayURLResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class GetOfficePreviewUrlModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: GetOfficePreviewUrlResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetOfficePreviewUrlResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class GetUploadUrlModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: GetUploadUrlResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetUploadUrlResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class GetVideoPreviewSpriteUrlModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: GetVideoPreviewSpriteURLResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetVideoPreviewSpriteURLResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class GetVideoPreviewUrlModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: GetVideoPreviewURLResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetVideoPreviewURLResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class ListFileModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: ListFileResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = ListFileResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class ListFileByAnonymousModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: ListByAnonymousResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = ListByAnonymousResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class ListFileByCustomIndexKeyModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: ListFileResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = ListFileResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class ListFileDeltaModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: ListFileDeltaResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = ListFileDeltaResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class ListUploadedPartsModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: ListUploadedPartResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = ListUploadedPartResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class MoveFileModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: MoveFileResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = MoveFileResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class ScanFileMetaModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: ScanFileMetaResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = ScanFileMetaResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class SearchFileModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: SearchFileResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = SearchFileResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class UpdateFileModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: UpdateFileMetaResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = UpdateFileMetaResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class CancelShareLinkModel(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        return self


class CreateShareLinkModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: CreateShareLinkResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = CreateShareLinkResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class GetShareIdModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: GetShareLinkIDResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetShareLinkIDResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class GetShareTokenModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: GetShareLinkTokenResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetShareLinkTokenResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class ListShareLinkModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: ListShareLinkResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = ListShareLinkResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class BaseCompleteFileRequest(TeaModel):
    """
    complete file request
    """
    def __init__(self, addition_data=None, drive_id=None, part_info_list=None, upload_id=None):
        # addition_data
        self.addition_data = addition_data  # type: dict
        # drive_id
        self.drive_id = drive_id        # type: str
        # part_info_list
        self.part_info_list = part_info_list  # type: List[UploadPartInfo]
        # upload_id
        self.upload_id = upload_id      # type: str

    def validate(self):
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.part_info_list:
            for k in self.part_info_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.addition_data is not None:
            result['addition_data'] = self.addition_data
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k in self.part_info_list:
                result['part_info_list'].append(k.to_map() if k else None)
        if self.upload_id is not None:
            result['upload_id'] = self.upload_id
        return result

    def from_map(self, map={}):
        if map.get('addition_data') is not None:
            self.addition_data = map.get('addition_data')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        self.part_info_list = []
        if map.get('part_info_list') is not None:
            for k in map.get('part_info_list'):
                temp_model = UploadPartInfo()
                self.part_info_list.append(temp_model.from_map(k))
        if map.get('upload_id') is not None:
            self.upload_id = map.get('upload_id')
        return self


class BaseCreateFileRequest(TeaModel):
    """
    create file request
    """
    def __init__(self, addition_data=None, content_md_5=None, content_type=None, name=None, part_info_list=None,
                 size=None, type=None):
        # addition_data
        self.addition_data = addition_data  # type: dict
        # ContentMd5
        self.content_md_5 = content_md_5  # type: str
        # ContentType
        self.content_type = content_type  # type: str
        # Name
        self.name = name                # type: str
        # part_info_list
        self.part_info_list = part_info_list  # type: List[UploadPartInfo]
        # Size
        self.size = size                # type: int
        # Type
        self.type = type                # type: str

    def validate(self):
        self.validate_required(self.name, 'name')
        if self.name is not None:
            self.validate_max_length(self.name, 'name', 1024)
        if self.part_info_list:
            for k in self.part_info_list:
                if k:
                    k.validate()
        if self.size is not None:
            self.validate_maximum(self.size, 'size', 53687091200)
            self.validate_minimum(self.size, 'size', 0)
        self.validate_required(self.type, 'type')

    def to_map(self):
        result = {}
        if self.addition_data is not None:
            result['addition_data'] = self.addition_data
        if self.content_md_5 is not None:
            result['content_md5'] = self.content_md_5
        if self.content_type is not None:
            result['content_type'] = self.content_type
        if self.name is not None:
            result['name'] = self.name
        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k in self.part_info_list:
                result['part_info_list'].append(k.to_map() if k else None)
        if self.size is not None:
            result['size'] = self.size
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, map={}):
        if map.get('addition_data') is not None:
            self.addition_data = map.get('addition_data')
        if map.get('content_md5') is not None:
            self.content_md_5 = map.get('content_md5')
        if map.get('content_type') is not None:
            self.content_type = map.get('content_type')
        if map.get('name') is not None:
            self.name = map.get('name')
        self.part_info_list = []
        if map.get('part_info_list') is not None:
            for k in map.get('part_info_list'):
                temp_model = UploadPartInfo()
                self.part_info_list.append(temp_model.from_map(k))
        if map.get('size') is not None:
            self.size = map.get('size')
        if map.get('type') is not None:
            self.type = map.get('type')
        return self


class BaseFileRequest(TeaModel):
    """
    *
    """
    def __init__(self, addition_data=None):
        # addition_data
        self.addition_data = addition_data  # type: dict

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.addition_data is not None:
            result['addition_data'] = self.addition_data
        return result

    def from_map(self, map={}):
        if map.get('addition_data') is not None:
            self.addition_data = map.get('addition_data')
        return self


class BaseGetUploadUrlRequest(TeaModel):
    """
    获取文件上传URL
    """
    def __init__(self, content_md_5=None, drive_id=None, part_info_list=None, upload_id=None):
        # content_md5
        self.content_md_5 = content_md_5  # type: str
        # drive_id
        self.drive_id = drive_id        # type: str
        # upload_part_list
        self.part_info_list = part_info_list  # type: List[UploadPartInfo]
        # upload_id
        self.upload_id = upload_id      # type: str

    def validate(self):
        if self.content_md_5 is not None:
            self.validate_max_length(self.content_md_5, 'content_md_5', 32)
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.part_info_list:
            for k in self.part_info_list:
                if k:
                    k.validate()
        self.validate_required(self.upload_id, 'upload_id')

    def to_map(self):
        result = {}
        if self.content_md_5 is not None:
            result['content_md5'] = self.content_md_5
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k in self.part_info_list:
                result['part_info_list'].append(k.to_map() if k else None)
        if self.upload_id is not None:
            result['upload_id'] = self.upload_id
        return result

    def from_map(self, map={}):
        if map.get('content_md5') is not None:
            self.content_md_5 = map.get('content_md5')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        self.part_info_list = []
        if map.get('part_info_list') is not None:
            for k in map.get('part_info_list'):
                temp_model = UploadPartInfo()
                self.part_info_list.append(temp_model.from_map(k))
        if map.get('upload_id') is not None:
            self.upload_id = map.get('upload_id')
        return self


class BaseListFileRequest(TeaModel):
    """
    list file request
    """
    def __init__(self, drive_id=None, image_thumbnail_process=None, image_url_process=None, limit=None, marker=None,
                 video_thumbnail_process=None):
        # drive_id
        self.drive_id = drive_id        # type: str
        # image_thumbnail_process
        self.image_thumbnail_process = image_thumbnail_process  # type: str
        # image_url_process
        self.image_url_process = image_url_process  # type: str
        # limit
        self.limit = limit              # type: int
        # marker
        self.marker = marker            # type: str
        # video_thumbnail_process
        # type:string
        self.video_thumbnail_process = video_thumbnail_process  # type: str

    def validate(self):
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.limit is not None:
            self.validate_pattern(self.limit, 'limit', '[0-9]{1,3}')
            self.validate_maximum(self.limit, 'limit', 100)
            self.validate_minimum(self.limit, 'limit', 0)

    def to_map(self):
        result = {}
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.image_thumbnail_process is not None:
            result['image_thumbnail_process'] = self.image_thumbnail_process
        if self.image_url_process is not None:
            result['image_url_process'] = self.image_url_process
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        if self.video_thumbnail_process is not None:
            result['video_thumbnail_process'] = self.video_thumbnail_process
        return result

    def from_map(self, map={}):
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('image_thumbnail_process') is not None:
            self.image_thumbnail_process = map.get('image_thumbnail_process')
        if map.get('image_url_process') is not None:
            self.image_url_process = map.get('image_url_process')
        if map.get('limit') is not None:
            self.limit = map.get('limit')
        if map.get('marker') is not None:
            self.marker = map.get('marker')
        if map.get('video_thumbnail_process') is not None:
            self.video_thumbnail_process = map.get('video_thumbnail_process')
        return self


class BaseMoveFileRequest(TeaModel):
    """
    文件移动请求
    """
    def __init__(self, drive_id=None, new_name=None, overwrite=None):
        # drive_id
        self.drive_id = drive_id        # type: str
        # new_name
        self.new_name = new_name        # type: str
        # overwrite
        # type: boolean
        self.overwrite = overwrite      # type: bool

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.new_name is not None:
            self.validate_max_length(self.new_name, 'new_name', 1024)

    def to_map(self):
        result = {}
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.new_name is not None:
            result['new_name'] = self.new_name
        if self.overwrite is not None:
            result['overwrite'] = self.overwrite
        return result

    def from_map(self, map={}):
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('new_name') is not None:
            self.new_name = map.get('new_name')
        if map.get('overwrite') is not None:
            self.overwrite = map.get('overwrite')
        return self


class BatchRequest(TeaModel):
    """
    批处理
    """
    def __init__(self, headers=None, requests=None, resource=None):
        self.headers = headers          # type: Dict[str, str]
        # Requests 请求合集
        self.requests = requests        # type: List[BatchSubRequest]
        # 支持的资源类型
        self.resource = resource        # type: str

    def validate(self):
        self.validate_required(self.requests, 'requests')
        if self.requests:
            for k in self.requests:
                if k:
                    k.validate()
        self.validate_required(self.resource, 'resource')

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        result['requests'] = []
        if self.requests is not None:
            for k in self.requests:
                result['requests'].append(k.to_map() if k else None)
        if self.resource is not None:
            result['resource'] = self.resource
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        self.requests = []
        if map.get('requests') is not None:
            for k in map.get('requests'):
                temp_model = BatchSubRequest()
                self.requests.append(temp_model.from_map(k))
        if map.get('resource') is not None:
            self.resource = map.get('resource')
        return self


class BatchSubRequest(TeaModel):
    """
    *
    """
    def __init__(self, body=None, headers=None, id=None, method=None, url=None):
        # body 子请求的请求参数 json 字符串，可参考对于子请求文档, 当指定了body 必须传headers ： "Content-Type" 对应的类型，目前子请求入参是"application/json"
        self.body = body                # type: dict
        # headers 请求头，表示body传入数据的类型
        self.headers = headers          # type: dict
        # id 用于request 和 response关联， 不允许重复
        self.id = id                    # type: str
        # method
        self.method = method            # type: str
        # url 子请求的api path路径， 可参考对于子请求文档
        self.url = url                  # type: str

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.method, 'method')
        self.validate_required(self.url, 'url')

    def to_map(self):
        result = {}
        if self.body is not None:
            result['body'] = self.body
        if self.headers is not None:
            result['headers'] = self.headers
        if self.id is not None:
            result['id'] = self.id
        if self.method is not None:
            result['method'] = self.method
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, map={}):
        if map.get('body') is not None:
            self.body = map.get('body')
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('id') is not None:
            self.id = map.get('id')
        if map.get('method') is not None:
            self.method = map.get('method')
        if map.get('url') is not None:
            self.url = map.get('url')
        return self


class CancelShareLinkRequest(TeaModel):
    """
    cancel_share_link request
    """
    def __init__(self, headers=None, share_id=None):
        self.headers = headers          # type: Dict[str, str]
        # share_id
        self.share_id = share_id        # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.share_id is not None:
            result['share_id'] = self.share_id
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('share_id') is not None:
            self.share_id = map.get('share_id')
        return self


class CompleteFileRequest(TeaModel):
    """
    合并文件上传任务
    """
    def __init__(self, headers=None, addition_data=None, drive_id=None, file_id=None, part_info_list=None,
                 upload_id=None):
        self.headers = headers          # type: Dict[str, str]
        # addition_data
        self.addition_data = addition_data  # type: dict
        # drive_id
        self.drive_id = drive_id        # type: str
        # file_id
        self.file_id = file_id          # type: str
        # part_info_list
        self.part_info_list = part_info_list  # type: List[UploadPartInfo]
        # upload_id
        self.upload_id = upload_id      # type: str

    def validate(self):
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_id, 'file_id')
        if self.file_id is not None:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9]{1,50}')
        if self.part_info_list:
            for k in self.part_info_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.addition_data is not None:
            result['addition_data'] = self.addition_data
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k in self.part_info_list:
                result['part_info_list'].append(k.to_map() if k else None)
        if self.upload_id is not None:
            result['upload_id'] = self.upload_id
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('addition_data') is not None:
            self.addition_data = map.get('addition_data')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('file_id') is not None:
            self.file_id = map.get('file_id')
        self.part_info_list = []
        if map.get('part_info_list') is not None:
            for k in map.get('part_info_list'):
                temp_model = UploadPartInfo()
                self.part_info_list.append(temp_model.from_map(k))
        if map.get('upload_id') is not None:
            self.upload_id = map.get('upload_id')
        return self


class CopyFileRequest(TeaModel):
    """
    文件拷贝
    """
    def __init__(self, headers=None, auto_rename=None, drive_id=None, file_id=None, new_name=None, share_id=None,
                 to_drive_id=None, to_parent_file_id=None):
        self.headers = headers          # type: Dict[str, str]
        # auto_rename
        # type: boolean
        self.auto_rename = auto_rename  # type: bool
        # drive_id
        self.drive_id = drive_id        # type: str
        # file_id
        self.file_id = file_id          # type: str
        # new_name
        self.new_name = new_name        # type: str
        # share_id, either share_id or drive_id is required
        self.share_id = share_id        # type: str
        # to_drive_id
        self.to_drive_id = to_drive_id  # type: str
        # to_parent_file_id
        self.to_parent_file_id = to_parent_file_id  # type: str

    def validate(self):
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_id, 'file_id')
        if self.file_id is not None:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9.-_]{1,50}')
        if self.new_name is not None:
            self.validate_max_length(self.new_name, 'new_name', 1024)
        if self.to_drive_id is not None:
            self.validate_pattern(self.to_drive_id, 'to_drive_id', '[0-9]+')
        self.validate_required(self.to_parent_file_id, 'to_parent_file_id')
        if self.to_parent_file_id is not None:
            self.validate_max_length(self.to_parent_file_id, 'to_parent_file_id', 50)
            self.validate_pattern(self.to_parent_file_id, 'to_parent_file_id', '[a-z0-9.-_]{1,50}')

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.auto_rename is not None:
            result['auto_rename'] = self.auto_rename
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.new_name is not None:
            result['new_name'] = self.new_name
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.to_drive_id is not None:
            result['to_drive_id'] = self.to_drive_id
        if self.to_parent_file_id is not None:
            result['to_parent_file_id'] = self.to_parent_file_id
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('auto_rename') is not None:
            self.auto_rename = map.get('auto_rename')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('file_id') is not None:
            self.file_id = map.get('file_id')
        if map.get('new_name') is not None:
            self.new_name = map.get('new_name')
        if map.get('share_id') is not None:
            self.share_id = map.get('share_id')
        if map.get('to_drive_id') is not None:
            self.to_drive_id = map.get('to_drive_id')
        if map.get('to_parent_file_id') is not None:
            self.to_parent_file_id = map.get('to_parent_file_id')
        return self


class CreateDriveRequest(TeaModel):
    """
    create drive request
    """
    def __init__(self, headers=None, default=None, description=None, drive_name=None, drive_type=None,
                 encrypt_mode=None, owner=None, relative_path=None, status=None, store_id=None, total_size=None):
        self.headers = headers          # type: Dict[str, str]
        # 是否默认drive, 只允许设置一个默认drive
        self.default = default          # type: bool
        # 描述信息
        self.description = description  # type: str
        # Drive 名称
        self.drive_name = drive_name    # type: str
        # Drive类型
        self.drive_type = drive_type    # type: str
        self.encrypt_mode = encrypt_mode  # type: str
        # 所属者
        self.owner = owner              # type: str
        # domain的PathType为OSSPath时必选。 Drive存储基于store的相对路径
        self.relative_path = relative_path  # type: str
        # 状态
        self.status = status            # type: str
        # StoreID , domain的PathType为OSSPath时必选
        self.store_id = store_id        # type: str
        # 总大小,单位Byte [如果设置 -1 代表不限制]
        self.total_size = total_size    # type: int

    def validate(self):
        if self.description is not None:
            self.validate_max_length(self.description, 'description', 1024)
        self.validate_required(self.drive_name, 'drive_name')
        if self.drive_name is not None:
            self.validate_max_length(self.drive_name, 'drive_name', 1024)
        self.validate_required(self.owner, 'owner')

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.default is not None:
            result['default'] = self.default
        if self.description is not None:
            result['description'] = self.description
        if self.drive_name is not None:
            result['drive_name'] = self.drive_name
        if self.drive_type is not None:
            result['drive_type'] = self.drive_type
        if self.encrypt_mode is not None:
            result['encrypt_mode'] = self.encrypt_mode
        if self.owner is not None:
            result['owner'] = self.owner
        if self.relative_path is not None:
            result['relative_path'] = self.relative_path
        if self.status is not None:
            result['status'] = self.status
        if self.store_id is not None:
            result['store_id'] = self.store_id
        if self.total_size is not None:
            result['total_size'] = self.total_size
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('default') is not None:
            self.default = map.get('default')
        if map.get('description') is not None:
            self.description = map.get('description')
        if map.get('drive_name') is not None:
            self.drive_name = map.get('drive_name')
        if map.get('drive_type') is not None:
            self.drive_type = map.get('drive_type')
        if map.get('encrypt_mode') is not None:
            self.encrypt_mode = map.get('encrypt_mode')
        if map.get('owner') is not None:
            self.owner = map.get('owner')
        if map.get('relative_path') is not None:
            self.relative_path = map.get('relative_path')
        if map.get('status') is not None:
            self.status = map.get('status')
        if map.get('store_id') is not None:
            self.store_id = map.get('store_id')
        if map.get('total_size') is not None:
            self.total_size = map.get('total_size')
        return self


class CreateFileRequest(TeaModel):
    """
    创建文件
    """
    def __init__(self, headers=None, addition_data=None, auto_rename=None, check_name_mode=None, content_hash=None,
                 content_hash_name=None, content_md_5=None, content_type=None, description=None, drive_id=None, encrypt_mode=None,
                 file_id=None, hidden=None, image_media_metadata=None, labels=None, last_updated_at=None, meta=None,
                 name=None, parent_file_id=None, part_info_list=None, pre_hash=None, size=None, streams_info=None,
                 type=None, user_meta=None, video_media_metadata=None):
        self.headers = headers          # type: Dict[str, str]
        # addition_data
        self.addition_data = addition_data  # type: dict
        self.auto_rename = auto_rename  # type: bool
        # check_name_mode
        self.check_name_mode = check_name_mode  # type: str
        # content_hash
        self.content_hash = content_hash  # type: str
        # content_hash_name
        self.content_hash_name = content_hash_name  # type: str
        # ContentMd5
        self.content_md_5 = content_md_5  # type: str
        # ContentType
        self.content_type = content_type  # type: str
        # description
        self.description = description  # type: str
        # drive_id
        self.drive_id = drive_id        # type: str
        # encrypt_mode
        self.encrypt_mode = encrypt_mode  # type: str
        # file_id
        self.file_id = file_id          # type: str
        # hidden
        self.hidden = hidden            # type: bool
        self.image_media_metadata = image_media_metadata  # type: ImageMediaMetadata
        # labels
        self.labels = labels            # type: List[str]
        # last_updated_at
        self.last_updated_at = last_updated_at  # type: str
        self.meta = meta                # type: str
        # Name
        self.name = name                # type: str
        # parent_file_id
        self.parent_file_id = parent_file_id  # type: str
        # part_info_list
        self.part_info_list = part_info_list  # type: List[UploadPartInfo]
        # pre_hash
        self.pre_hash = pre_hash        # type: str
        # Size
        self.size = size                # type: int
        # streams_info
        self.streams_info = streams_info  # type: dict
        # Type
        self.type = type                # type: str
        # user_meta
        self.user_meta = user_meta      # type: str
        self.video_media_metadata = video_media_metadata  # type: VideoMediaMetadata

    def validate(self):
        if self.description is not None:
            self.validate_max_length(self.description, 'description', 1024)
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.image_media_metadata:
            self.image_media_metadata.validate()
        self.validate_required(self.name, 'name')
        if self.name is not None:
            self.validate_max_length(self.name, 'name', 1024)
        self.validate_required(self.parent_file_id, 'parent_file_id')
        if self.parent_file_id is not None:
            self.validate_max_length(self.parent_file_id, 'parent_file_id', 50)
            self.validate_pattern(self.parent_file_id, 'parent_file_id', '[a-z0-9]{1,50}')
        if self.part_info_list:
            for k in self.part_info_list:
                if k:
                    k.validate()
        if self.size is not None:
            self.validate_maximum(self.size, 'size', 53687091200)
            self.validate_minimum(self.size, 'size', 0)
        self.validate_required(self.type, 'type')
        if self.video_media_metadata:
            self.video_media_metadata.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.addition_data is not None:
            result['addition_data'] = self.addition_data
        if self.auto_rename is not None:
            result['auto_rename'] = self.auto_rename
        if self.check_name_mode is not None:
            result['check_name_mode'] = self.check_name_mode
        if self.content_hash is not None:
            result['content_hash'] = self.content_hash
        if self.content_hash_name is not None:
            result['content_hash_name'] = self.content_hash_name
        if self.content_md_5 is not None:
            result['content_md5'] = self.content_md_5
        if self.content_type is not None:
            result['content_type'] = self.content_type
        if self.description is not None:
            result['description'] = self.description
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.encrypt_mode is not None:
            result['encrypt_mode'] = self.encrypt_mode
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.hidden is not None:
            result['hidden'] = self.hidden
        if self.image_media_metadata is not None:
            result['image_media_metadata'] = self.image_media_metadata.to_map()
        if self.labels is not None:
            result['labels'] = self.labels
        if self.last_updated_at is not None:
            result['last_updated_at'] = self.last_updated_at
        if self.meta is not None:
            result['meta'] = self.meta
        if self.name is not None:
            result['name'] = self.name
        if self.parent_file_id is not None:
            result['parent_file_id'] = self.parent_file_id
        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k in self.part_info_list:
                result['part_info_list'].append(k.to_map() if k else None)
        if self.pre_hash is not None:
            result['pre_hash'] = self.pre_hash
        if self.size is not None:
            result['size'] = self.size
        if self.streams_info is not None:
            result['streams_info'] = self.streams_info
        if self.type is not None:
            result['type'] = self.type
        if self.user_meta is not None:
            result['user_meta'] = self.user_meta
        if self.video_media_metadata is not None:
            result['video_media_metadata'] = self.video_media_metadata.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('addition_data') is not None:
            self.addition_data = map.get('addition_data')
        if map.get('auto_rename') is not None:
            self.auto_rename = map.get('auto_rename')
        if map.get('check_name_mode') is not None:
            self.check_name_mode = map.get('check_name_mode')
        if map.get('content_hash') is not None:
            self.content_hash = map.get('content_hash')
        if map.get('content_hash_name') is not None:
            self.content_hash_name = map.get('content_hash_name')
        if map.get('content_md5') is not None:
            self.content_md_5 = map.get('content_md5')
        if map.get('content_type') is not None:
            self.content_type = map.get('content_type')
        if map.get('description') is not None:
            self.description = map.get('description')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('encrypt_mode') is not None:
            self.encrypt_mode = map.get('encrypt_mode')
        if map.get('file_id') is not None:
            self.file_id = map.get('file_id')
        if map.get('hidden') is not None:
            self.hidden = map.get('hidden')
        if map.get('image_media_metadata') is not None:
            temp_model = ImageMediaMetadata()
            self.image_media_metadata = temp_model.from_map(map['image_media_metadata'])
        if map.get('labels') is not None:
            self.labels = map.get('labels')
        if map.get('last_updated_at') is not None:
            self.last_updated_at = map.get('last_updated_at')
        if map.get('meta') is not None:
            self.meta = map.get('meta')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('parent_file_id') is not None:
            self.parent_file_id = map.get('parent_file_id')
        self.part_info_list = []
        if map.get('part_info_list') is not None:
            for k in map.get('part_info_list'):
                temp_model = UploadPartInfo()
                self.part_info_list.append(temp_model.from_map(k))
        if map.get('pre_hash') is not None:
            self.pre_hash = map.get('pre_hash')
        if map.get('size') is not None:
            self.size = map.get('size')
        if map.get('streams_info') is not None:
            self.streams_info = map.get('streams_info')
        if map.get('type') is not None:
            self.type = map.get('type')
        if map.get('user_meta') is not None:
            self.user_meta = map.get('user_meta')
        if map.get('video_media_metadata') is not None:
            temp_model = VideoMediaMetadata()
            self.video_media_metadata = temp_model.from_map(map['video_media_metadata'])
        return self


class CreateShareLinkRequest(TeaModel):
    """
    create_share_link request
    """
    def __init__(self, headers=None, drive_id=None, expiration=None, file_id=None, share_pwd=None):
        self.headers = headers          # type: Dict[str, str]
        # drive_id
        self.drive_id = drive_id        # type: str
        # expiration
        self.expiration = expiration    # type: str
        # file_id
        self.file_id = file_id          # type: str
        # share_pwd
        self.share_pwd = share_pwd      # type: str

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.expiration, 'expiration')
        self.validate_required(self.file_id, 'file_id')

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.expiration is not None:
            result['expiration'] = self.expiration
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.share_pwd is not None:
            result['share_pwd'] = self.share_pwd
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('expiration') is not None:
            self.expiration = map.get('expiration')
        if map.get('file_id') is not None:
            self.file_id = map.get('file_id')
        if map.get('share_pwd') is not None:
            self.share_pwd = map.get('share_pwd')
        return self


class CreateShareRequest(TeaModel):
    """
    create share request
    """
    def __init__(self, description=None, drive_id=None, expiration=None, owner=None, permissions=None,
                 share_file_path=None, share_name=None, share_policy=None, status=None):
        # description
        self.description = description  # type: str
        # drive_id
        self.drive_id = drive_id        # type: str
        # expiration
        self.expiration = expiration    # type: str
        # creator
        self.owner = owner              # type: str
        # permissions
        self.permissions = permissions  # type: List[str]
        # share_file_path
        self.share_file_path = share_file_path  # type: str
        # share_name
        self.share_name = share_name    # type: str
        # share create policy
        # 
        # share_policy
        self.share_policy = share_policy  # type: List[SharePermissionPolicy]
        # status
        self.status = status            # type: str

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.owner, 'owner')
        self.validate_required(self.share_file_path, 'share_file_path')
        if self.share_policy:
            for k in self.share_policy:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.description is not None:
            result['description'] = self.description
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.expiration is not None:
            result['expiration'] = self.expiration
        if self.owner is not None:
            result['owner'] = self.owner
        if self.permissions is not None:
            result['permissions'] = self.permissions
        if self.share_file_path is not None:
            result['share_file_path'] = self.share_file_path
        if self.share_name is not None:
            result['share_name'] = self.share_name
        result['share_policy'] = []
        if self.share_policy is not None:
            for k in self.share_policy:
                result['share_policy'].append(k.to_map() if k else None)
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, map={}):
        if map.get('description') is not None:
            self.description = map.get('description')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('expiration') is not None:
            self.expiration = map.get('expiration')
        if map.get('owner') is not None:
            self.owner = map.get('owner')
        if map.get('permissions') is not None:
            self.permissions = map.get('permissions')
        if map.get('share_file_path') is not None:
            self.share_file_path = map.get('share_file_path')
        if map.get('share_name') is not None:
            self.share_name = map.get('share_name')
        self.share_policy = []
        if map.get('share_policy') is not None:
            for k in map.get('share_policy'):
                temp_model = SharePermissionPolicy()
                self.share_policy.append(temp_model.from_map(k))
        if map.get('status') is not None:
            self.status = map.get('status')
        return self


class DeleteDriveRequest(TeaModel):
    """
    Delete drive request
    """
    def __init__(self, headers=None, drive_id=None):
        self.headers = headers          # type: Dict[str, str]
        # Drive ID
        self.drive_id = drive_id        # type: str

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        return self


class DeleteFileRequest(TeaModel):
    """
    删除文件请求
    """
    def __init__(self, headers=None, drive_id=None, file_id=None, permanently=None):
        self.headers = headers          # type: Dict[str, str]
        # drive_id
        self.drive_id = drive_id        # type: str
        # file_id
        self.file_id = file_id          # type: str
        # permanently
        # type: false
        self.permanently = permanently  # type: bool

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_id, 'file_id')
        if self.file_id is not None:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9.-_]{1,50}')

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.permanently is not None:
            result['permanently'] = self.permanently
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('file_id') is not None:
            self.file_id = map.get('file_id')
        if map.get('permanently') is not None:
            self.permanently = map.get('permanently')
        return self


class DeleteFilesRequest(TeaModel):
    """
    批量删除文件请求
    """
    def __init__(self, drive_id=None, file_id_list=None):
        # drive_id
        self.drive_id = drive_id        # type: str
        # file_id_list
        self.file_id_list = file_id_list  # type: List[str]

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_id_list, 'file_id_list')

    def to_map(self):
        result = {}
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id_list is not None:
            result['file_id_list'] = self.file_id_list
        return result

    def from_map(self, map={}):
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('file_id_list') is not None:
            self.file_id_list = map.get('file_id_list')
        return self


class DeleteShareRequest(TeaModel):
    """
    delete share request
    """
    def __init__(self, share_id=None):
        # share_id
        self.share_id = share_id        # type: str

    def validate(self):
        self.validate_required(self.share_id, 'share_id')

    def to_map(self):
        result = {}
        if self.share_id is not None:
            result['share_id'] = self.share_id
        return result

    def from_map(self, map={}):
        if map.get('share_id') is not None:
            self.share_id = map.get('share_id')
        return self


class DownloadRequest(TeaModel):
    """
    下载文件请求body
    """
    def __init__(self, drive_id=None, file_id=None, image_thumbnail_process=None, share_id=None,
                 video_thumbnail_process=None):
        # drive id
        self.drive_id = drive_id        # type: str
        # file id
        self.file_id = file_id          # type: str
        # in: query
        # image_thumbnail_process
        self.image_thumbnail_process = image_thumbnail_process  # type: str
        # share_id, either share_id or drive_id is required
        self.share_id = share_id        # type: str
        # video_thumbnail_process
        # type:string
        self.video_thumbnail_process = video_thumbnail_process  # type: str

    def validate(self):
        self.validate_required(self.file_id, 'file_id')

    def to_map(self):
        result = {}
        if self.drive_id is not None:
            result['DriveID'] = self.drive_id
        if self.file_id is not None:
            result['FileID'] = self.file_id
        if self.image_thumbnail_process is not None:
            result['ImageThumbnailProcess'] = self.image_thumbnail_process
        if self.share_id is not None:
            result['ShareID'] = self.share_id
        if self.video_thumbnail_process is not None:
            result['VideoThumbnailProcess'] = self.video_thumbnail_process
        return result

    def from_map(self, map={}):
        if map.get('DriveID') is not None:
            self.drive_id = map.get('DriveID')
        if map.get('FileID') is not None:
            self.file_id = map.get('FileID')
        if map.get('ImageThumbnailProcess') is not None:
            self.image_thumbnail_process = map.get('ImageThumbnailProcess')
        if map.get('ShareID') is not None:
            self.share_id = map.get('ShareID')
        if map.get('VideoThumbnailProcess') is not None:
            self.video_thumbnail_process = map.get('VideoThumbnailProcess')
        return self


class GetAsyncTaskRequest(TeaModel):
    """
    获取异步人去信息
    """
    def __init__(self, headers=None, async_task_id=None):
        self.headers = headers          # type: Dict[str, str]
        # async_task_id
        # type:string
        self.async_task_id = async_task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.async_task_id is not None:
            result['async_task_id'] = self.async_task_id
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('async_task_id') is not None:
            self.async_task_id = map.get('async_task_id')
        return self


class GetDefaultDriveRequest(TeaModel):
    """
    Get default drive request
    """
    def __init__(self, headers=None, user_id=None):
        self.headers = headers          # type: Dict[str, str]
        # 用户ID
        self.user_id = user_id          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('user_id') is not None:
            self.user_id = map.get('user_id')
        return self


class GetDownloadUrlRequest(TeaModel):
    """
    获取文件下载地址的请求body
    """
    def __init__(self, headers=None, addition_data=None, drive_id=None, expire_sec=None, file_id=None,
                 file_name=None):
        self.headers = headers          # type: Dict[str, str]
        # addition_data
        self.addition_data = addition_data  # type: dict
        # drive_id
        self.drive_id = drive_id        # type: str
        # expire_sec
        self.expire_sec = expire_sec    # type: int
        # file_id
        self.file_id = file_id          # type: str
        # file_name
        self.file_name = file_name      # type: str

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.expire_sec is not None:
            self.validate_maximum(self.expire_sec, 'expire_sec', 14400)
            self.validate_minimum(self.expire_sec, 'expire_sec', 0)
        self.validate_required(self.file_id, 'file_id')
        if self.file_id is not None:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9.-_]{1,50}')
        if self.file_name is not None:
            self.validate_max_length(self.file_name, 'file_name', 1024)

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.addition_data is not None:
            result['addition_data'] = self.addition_data
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.expire_sec is not None:
            result['expire_sec'] = self.expire_sec
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.file_name is not None:
            result['file_name'] = self.file_name
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('addition_data') is not None:
            self.addition_data = map.get('addition_data')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('expire_sec') is not None:
            self.expire_sec = map.get('expire_sec')
        if map.get('file_id') is not None:
            self.file_id = map.get('file_id')
        if map.get('file_name') is not None:
            self.file_name = map.get('file_name')
        return self


class GetDriveRequest(TeaModel):
    """
    Get drive request
    """
    def __init__(self, headers=None, drive_id=None):
        self.headers = headers          # type: Dict[str, str]
        # Drive ID
        self.drive_id = drive_id        # type: str

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        return self


class GetFileByPathRequest(TeaModel):
    """
    根据路径获取 File 接口 body
    """
    def __init__(self, headers=None, drive_id=None, fields=None, file_id=None, file_path=None,
                 image_thumbnail_process=None, image_url_process=None, url_expire_sec=None, video_thumbnail_process=None):
        self.headers = headers          # type: Dict[str, str]
        # drive_id
        self.drive_id = drive_id        # type: str
        # fields
        self.fields = fields            # type: str
        # file_id
        self.file_id = file_id          # type: str
        # file_path
        self.file_path = file_path      # type: str
        # image_thumbnail_process
        # type:string
        self.image_thumbnail_process = image_thumbnail_process  # type: str
        # image_thumbnail_process
        # type:string
        self.image_url_process = image_url_process  # type: str
        # url_expire_sec
        self.url_expire_sec = url_expire_sec  # type: int
        # video_thumbnail_process
        # type:string
        self.video_thumbnail_process = video_thumbnail_process  # type: str

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_id, 'file_id')
        if self.file_id is not None:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9.-_]{1,50}')
        if self.url_expire_sec is not None:
            self.validate_maximum(self.url_expire_sec, 'url_expire_sec', 14400)
            self.validate_minimum(self.url_expire_sec, 'url_expire_sec', 10)

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.fields is not None:
            result['fields'] = self.fields
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.file_path is not None:
            result['file_path'] = self.file_path
        if self.image_thumbnail_process is not None:
            result['image_thumbnail_process'] = self.image_thumbnail_process
        if self.image_url_process is not None:
            result['image_url_process'] = self.image_url_process
        if self.url_expire_sec is not None:
            result['url_expire_sec'] = self.url_expire_sec
        if self.video_thumbnail_process is not None:
            result['video_thumbnail_process'] = self.video_thumbnail_process
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('fields') is not None:
            self.fields = map.get('fields')
        if map.get('file_id') is not None:
            self.file_id = map.get('file_id')
        if map.get('file_path') is not None:
            self.file_path = map.get('file_path')
        if map.get('image_thumbnail_process') is not None:
            self.image_thumbnail_process = map.get('image_thumbnail_process')
        if map.get('image_url_process') is not None:
            self.image_url_process = map.get('image_url_process')
        if map.get('url_expire_sec') is not None:
            self.url_expire_sec = map.get('url_expire_sec')
        if map.get('video_thumbnail_process') is not None:
            self.video_thumbnail_process = map.get('video_thumbnail_process')
        return self


class GetFileRequest(TeaModel):
    """
    获取文件元数据
    """
    def __init__(self, headers=None, drive_id=None, fields=None, file_id=None, image_thumbnail_process=None,
                 image_url_process=None, url_expire_sec=None, video_thumbnail_process=None):
        self.headers = headers          # type: Dict[str, str]
        # drive_id
        self.drive_id = drive_id        # type: str
        # fields
        self.fields = fields            # type: str
        # file_id
        self.file_id = file_id          # type: str
        # image_thumbnail_process
        # type:string
        self.image_thumbnail_process = image_thumbnail_process  # type: str
        # image_thumbnail_process
        # type:string
        self.image_url_process = image_url_process  # type: str
        # url_expire_sec
        self.url_expire_sec = url_expire_sec  # type: int
        # video_thumbnail_process
        # type:string
        self.video_thumbnail_process = video_thumbnail_process  # type: str

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_id, 'file_id')
        if self.file_id is not None:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9.-_]{1,50}')
        if self.url_expire_sec is not None:
            self.validate_maximum(self.url_expire_sec, 'url_expire_sec', 14400)
            self.validate_minimum(self.url_expire_sec, 'url_expire_sec', 10)

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.fields is not None:
            result['fields'] = self.fields
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.image_thumbnail_process is not None:
            result['image_thumbnail_process'] = self.image_thumbnail_process
        if self.image_url_process is not None:
            result['image_url_process'] = self.image_url_process
        if self.url_expire_sec is not None:
            result['url_expire_sec'] = self.url_expire_sec
        if self.video_thumbnail_process is not None:
            result['video_thumbnail_process'] = self.video_thumbnail_process
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('fields') is not None:
            self.fields = map.get('fields')
        if map.get('file_id') is not None:
            self.file_id = map.get('file_id')
        if map.get('image_thumbnail_process') is not None:
            self.image_thumbnail_process = map.get('image_thumbnail_process')
        if map.get('image_url_process') is not None:
            self.image_url_process = map.get('image_url_process')
        if map.get('url_expire_sec') is not None:
            self.url_expire_sec = map.get('url_expire_sec')
        if map.get('video_thumbnail_process') is not None:
            self.video_thumbnail_process = map.get('video_thumbnail_process')
        return self


class GetLastCursorRequest(TeaModel):
    """
    获取最新游标
    """
    def __init__(self, headers=None, drive_id=None):
        self.headers = headers          # type: Dict[str, str]
        # drive_id
        self.drive_id = drive_id        # type: str

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        return self


class GetMediaPlayURLRequest(TeaModel):
    """
    get_media_play_url request
    """
    def __init__(self, headers=None, drive_id=None, file_id=None):
        self.headers = headers          # type: Dict[str, str]
        # drive_id
        self.drive_id = drive_id        # type: str
        # file_id
        self.file_id = file_id          # type: str

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_id, 'file_id')
        if self.file_id is not None:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9.-_]{1,50}')

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('file_id') is not None:
            self.file_id = map.get('file_id')
        return self


class GetOfficePreviewUrlRequest(TeaModel):
    """
    获取office文档预览地址
    """
    def __init__(self, headers=None, addition_data=None, drive_id=None, file_id=None):
        self.headers = headers          # type: Dict[str, str]
        # addition_data
        self.addition_data = addition_data  # type: dict
        # drive_id
        self.drive_id = drive_id        # type: str
        # file_id
        self.file_id = file_id          # type: str

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_id, 'file_id')
        if self.file_id is not None:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9.-_]{1,50}')

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.addition_data is not None:
            result['addition_data'] = self.addition_data
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('addition_data') is not None:
            self.addition_data = map.get('addition_data')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('file_id') is not None:
            self.file_id = map.get('file_id')
        return self


class GetShareLinkByAnonymousRequest(TeaModel):
    """
    get_share_link_by_anonymous request
    """
    def __init__(self, share_id=None):
        # share_id
        self.share_id = share_id        # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.share_id is not None:
            result['share_id'] = self.share_id
        return result

    def from_map(self, map={}):
        if map.get('share_id') is not None:
            self.share_id = map.get('share_id')
        return self


class GetShareLinkIDRequest(TeaModel):
    """
    get_share_id request
    """
    def __init__(self, headers=None, share_msg=None):
        self.headers = headers          # type: Dict[str, str]
        # share_msg
        self.share_msg = share_msg      # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.share_msg is not None:
            result['share_msg'] = self.share_msg
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('share_msg') is not None:
            self.share_msg = map.get('share_msg')
        return self


class GetShareLinkTokenRequest(TeaModel):
    """
    get_share_token request
    """
    def __init__(self, headers=None, share_id=None, share_pwd=None):
        self.headers = headers          # type: Dict[str, str]
        # share_id
        self.share_id = share_id        # type: str
        # share_pwd
        self.share_pwd = share_pwd      # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.share_pwd is not None:
            result['share_pwd'] = self.share_pwd
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('share_id') is not None:
            self.share_id = map.get('share_id')
        if map.get('share_pwd') is not None:
            self.share_pwd = map.get('share_pwd')
        return self


class GetShareRequest(TeaModel):
    """
    get share request
    """
    def __init__(self, share_id=None):
        # share_id
        self.share_id = share_id        # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.share_id is not None:
            result['share_id'] = self.share_id
        return result

    def from_map(self, map={}):
        if map.get('share_id') is not None:
            self.share_id = map.get('share_id')
        return self


class GetUploadUrlRequest(TeaModel):
    """
    获取文件上传URL
    """
    def __init__(self, headers=None, content_md_5=None, drive_id=None, file_id=None, part_info_list=None,
                 upload_id=None):
        self.headers = headers          # type: Dict[str, str]
        # content_md5
        self.content_md_5 = content_md_5  # type: str
        # drive_id
        self.drive_id = drive_id        # type: str
        # file_id
        self.file_id = file_id          # type: str
        # upload_part_list
        self.part_info_list = part_info_list  # type: List[UploadPartInfo]
        # upload_id
        self.upload_id = upload_id      # type: str

    def validate(self):
        if self.content_md_5 is not None:
            self.validate_max_length(self.content_md_5, 'content_md_5', 32)
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_id, 'file_id')
        if self.file_id is not None:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9]{1,50}')
        if self.part_info_list:
            for k in self.part_info_list:
                if k:
                    k.validate()
        self.validate_required(self.upload_id, 'upload_id')

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.content_md_5 is not None:
            result['content_md5'] = self.content_md_5
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k in self.part_info_list:
                result['part_info_list'].append(k.to_map() if k else None)
        if self.upload_id is not None:
            result['upload_id'] = self.upload_id
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('content_md5') is not None:
            self.content_md_5 = map.get('content_md5')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('file_id') is not None:
            self.file_id = map.get('file_id')
        self.part_info_list = []
        if map.get('part_info_list') is not None:
            for k in map.get('part_info_list'):
                temp_model = UploadPartInfo()
                self.part_info_list.append(temp_model.from_map(k))
        if map.get('upload_id') is not None:
            self.upload_id = map.get('upload_id')
        return self


class GetVideoPreviewSpriteURLRequest(TeaModel):
    """
    获取视频雪碧图地址的请求body
    """
    def __init__(self, headers=None, drive_id=None, expire_sec=None, file_id=None):
        self.headers = headers          # type: Dict[str, str]
        # drive_id
        self.drive_id = drive_id        # type: str
        # expire_sec
        self.expire_sec = expire_sec    # type: int
        # file_id
        self.file_id = file_id          # type: str

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.expire_sec is not None:
            self.validate_maximum(self.expire_sec, 'expire_sec', 14400)
            self.validate_minimum(self.expire_sec, 'expire_sec', 0)
        self.validate_required(self.file_id, 'file_id')
        if self.file_id is not None:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9.-_]{1,50}')

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.expire_sec is not None:
            result['expire_sec'] = self.expire_sec
        if self.file_id is not None:
            result['file_id'] = self.file_id
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('expire_sec') is not None:
            self.expire_sec = map.get('expire_sec')
        if map.get('file_id') is not None:
            self.file_id = map.get('file_id')
        return self


class GetVideoPreviewURLRequest(TeaModel):
    """
    获取视频文件播放地址的请求body
    """
    def __init__(self, headers=None, addition_data=None, drive_id=None, expire_sec=None, file_id=None,
                 template_id=None):
        self.headers = headers          # type: Dict[str, str]
        # addition_data
        self.addition_data = addition_data  # type: dict
        # drive_id
        self.drive_id = drive_id        # type: str
        # expire_sec
        self.expire_sec = expire_sec    # type: int
        # file_id
        self.file_id = file_id          # type: str
        # template_id
        self.template_id = template_id  # type: str

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.expire_sec is not None:
            self.validate_maximum(self.expire_sec, 'expire_sec', 14400)
            self.validate_minimum(self.expire_sec, 'expire_sec', 0)
        self.validate_required(self.file_id, 'file_id')
        if self.file_id is not None:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9.-_]{1,50}')

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.addition_data is not None:
            result['addition_data'] = self.addition_data
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.expire_sec is not None:
            result['expire_sec'] = self.expire_sec
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.template_id is not None:
            result['template_id'] = self.template_id
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('addition_data') is not None:
            self.addition_data = map.get('addition_data')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('expire_sec') is not None:
            self.expire_sec = map.get('expire_sec')
        if map.get('file_id') is not None:
            self.file_id = map.get('file_id')
        if map.get('template_id') is not None:
            self.template_id = map.get('template_id')
        return self


class ImageMediaMetadata(TeaModel):
    """
    *
    """
    def __init__(self, height=None, width=None):
        # height
        self.height = height            # type: int
        # width：
        self.width = width              # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.height is not None:
            result['height'] = self.height
        if self.width is not None:
            result['width'] = self.width
        return result

    def from_map(self, map={}):
        if map.get('height') is not None:
            self.height = map.get('height')
        if map.get('width') is not None:
            self.width = map.get('width')
        return self


class ListByAnonymousRequest(TeaModel):
    """
    list_file_by_anonymous request
    """
    def __init__(self, headers=None, limit=None, marker=None, parent_file_id=None, share_id=None):
        self.headers = headers          # type: Dict[str, str]
        # limit
        self.limit = limit              # type: int
        # marker
        self.marker = marker            # type: str
        # parent_file_id
        self.parent_file_id = parent_file_id  # type: str
        # share_id
        self.share_id = share_id        # type: str

    def validate(self):
        if self.limit is not None:
            self.validate_maximum(self.limit, 'limit', 100)
            self.validate_minimum(self.limit, 'limit', 1)
        self.validate_required(self.parent_file_id, 'parent_file_id')
        if self.parent_file_id is not None:
            self.validate_max_length(self.parent_file_id, 'parent_file_id', 50)
            self.validate_pattern(self.parent_file_id, 'parent_file_id', '[a-z0-9]{1,50}')
        self.validate_required(self.share_id, 'share_id')

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        if self.parent_file_id is not None:
            result['parent_file_id'] = self.parent_file_id
        if self.share_id is not None:
            result['share_id'] = self.share_id
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('limit') is not None:
            self.limit = map.get('limit')
        if map.get('marker') is not None:
            self.marker = map.get('marker')
        if map.get('parent_file_id') is not None:
            self.parent_file_id = map.get('parent_file_id')
        if map.get('share_id') is not None:
            self.share_id = map.get('share_id')
        return self


class ListDriveRequest(TeaModel):
    """
    List drive request
    """
    def __init__(self, headers=None, limit=None, marker=None, owner=None):
        self.headers = headers          # type: Dict[str, str]
        # 每页大小限制
        self.limit = limit              # type: int
        # 翻页标记, 接口返回的标记值
        self.marker = marker            # type: str
        # 所属者
        self.owner = owner              # type: str

    def validate(self):
        if self.limit is not None:
            self.validate_maximum(self.limit, 'limit', 100)
            self.validate_minimum(self.limit, 'limit', 1)

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        if self.owner is not None:
            result['owner'] = self.owner
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('limit') is not None:
            self.limit = map.get('limit')
        if map.get('marker') is not None:
            self.marker = map.get('marker')
        if map.get('owner') is not None:
            self.owner = map.get('owner')
        return self


class ListFileByCustomIndexKeyRequest(TeaModel):
    """
    列举文件
    """
    def __init__(self, headers=None, starred=None, category=None, custom_index_key=None, drive_id=None,
                 encrypt_mode=None, fields=None, image_thumbnail_process=None, image_url_process=None, limit=None, marker=None,
                 order_direction=None, status=None, type=None, url_expire_sec=None, video_thumbnail_process=None):
        self.headers = headers          # type: Dict[str, str]
        # starred
        self.starred = starred          # type: bool
        # category
        self.category = category        # type: str
        # custom_index_key
        self.custom_index_key = custom_index_key  # type: str
        # drive_id
        self.drive_id = drive_id        # type: str
        # encrypt_mode
        self.encrypt_mode = encrypt_mode  # type: str
        # fields
        self.fields = fields            # type: str
        # image_thumbnail_process
        self.image_thumbnail_process = image_thumbnail_process  # type: str
        # image_url_process
        self.image_url_process = image_url_process  # type: str
        # limit
        self.limit = limit              # type: int
        # marker
        self.marker = marker            # type: str
        # order_direction
        self.order_direction = order_direction  # type: str
        # status
        self.status = status            # type: str
        # type
        self.type = type                # type: str
        # url_expire_sec
        self.url_expire_sec = url_expire_sec  # type: int
        # video_thumbnail_process
        # type:string
        self.video_thumbnail_process = video_thumbnail_process  # type: str

    def validate(self):
        self.validate_required(self.custom_index_key, 'custom_index_key')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.limit is not None:
            self.validate_pattern(self.limit, 'limit', '[0-9]{1,3}')
            self.validate_maximum(self.limit, 'limit', 100)
            self.validate_minimum(self.limit, 'limit', 0)
        if self.url_expire_sec is not None:
            self.validate_maximum(self.url_expire_sec, 'url_expire_sec', 14400)
            self.validate_minimum(self.url_expire_sec, 'url_expire_sec', 10)

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.starred is not None:
            result['Starred'] = self.starred
        if self.category is not None:
            result['category'] = self.category
        if self.custom_index_key is not None:
            result['custom_index_key'] = self.custom_index_key
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.encrypt_mode is not None:
            result['encrypt_mode'] = self.encrypt_mode
        if self.fields is not None:
            result['fields'] = self.fields
        if self.image_thumbnail_process is not None:
            result['image_thumbnail_process'] = self.image_thumbnail_process
        if self.image_url_process is not None:
            result['image_url_process'] = self.image_url_process
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        if self.order_direction is not None:
            result['order_direction'] = self.order_direction
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        if self.url_expire_sec is not None:
            result['url_expire_sec'] = self.url_expire_sec
        if self.video_thumbnail_process is not None:
            result['video_thumbnail_process'] = self.video_thumbnail_process
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('Starred') is not None:
            self.starred = map.get('Starred')
        if map.get('category') is not None:
            self.category = map.get('category')
        if map.get('custom_index_key') is not None:
            self.custom_index_key = map.get('custom_index_key')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('encrypt_mode') is not None:
            self.encrypt_mode = map.get('encrypt_mode')
        if map.get('fields') is not None:
            self.fields = map.get('fields')
        if map.get('image_thumbnail_process') is not None:
            self.image_thumbnail_process = map.get('image_thumbnail_process')
        if map.get('image_url_process') is not None:
            self.image_url_process = map.get('image_url_process')
        if map.get('limit') is not None:
            self.limit = map.get('limit')
        if map.get('marker') is not None:
            self.marker = map.get('marker')
        if map.get('order_direction') is not None:
            self.order_direction = map.get('order_direction')
        if map.get('status') is not None:
            self.status = map.get('status')
        if map.get('type') is not None:
            self.type = map.get('type')
        if map.get('url_expire_sec') is not None:
            self.url_expire_sec = map.get('url_expire_sec')
        if map.get('video_thumbnail_process') is not None:
            self.video_thumbnail_process = map.get('video_thumbnail_process')
        return self


class ListFileDeltaRequest(TeaModel):
    """
    获取增量文件操作记录
    """
    def __init__(self, headers=None, cursor=None, drive_id=None, limit=None):
        self.headers = headers          # type: Dict[str, str]
        # cursor 游标
        self.cursor = cursor            # type: str
        # drive_id
        self.drive_id = drive_id        # type: str
        # limit
        # default 100
        self.limit = limit              # type: int

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.cursor is not None:
            result['cursor'] = self.cursor
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.limit is not None:
            result['limit'] = self.limit
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('cursor') is not None:
            self.cursor = map.get('cursor')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('limit') is not None:
            self.limit = map.get('limit')
        return self


class ListFileRequest(TeaModel):
    """
    列举文件
    """
    def __init__(self, headers=None, starred=None, all=None, category=None, drive_id=None, fields=None,
                 image_thumbnail_process=None, image_url_process=None, limit=None, marker=None, order_by=None, order_direction=None,
                 parent_file_id=None, status=None, type=None, url_expire_sec=None, video_thumbnail_process=None):
        self.headers = headers          # type: Dict[str, str]
        # starred
        self.starred = starred          # type: bool
        # all
        self.all = all                  # type: bool
        # category
        self.category = category        # type: str
        # drive_id
        self.drive_id = drive_id        # type: str
        # fields
        self.fields = fields            # type: str
        # image_thumbnail_process
        self.image_thumbnail_process = image_thumbnail_process  # type: str
        # image_url_process
        self.image_url_process = image_url_process  # type: str
        # limit
        self.limit = limit              # type: int
        # marker
        self.marker = marker            # type: str
        # order_by
        self.order_by = order_by        # type: str
        # order_direction
        self.order_direction = order_direction  # type: str
        # ParentFileID
        self.parent_file_id = parent_file_id  # type: str
        # status
        self.status = status            # type: str
        # type
        self.type = type                # type: str
        # url_expire_sec
        self.url_expire_sec = url_expire_sec  # type: int
        # video_thumbnail_process
        # type:string
        self.video_thumbnail_process = video_thumbnail_process  # type: str

    def validate(self):
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.limit is not None:
            self.validate_pattern(self.limit, 'limit', '[0-9]{1,3}')
            self.validate_maximum(self.limit, 'limit', 100)
            self.validate_minimum(self.limit, 'limit', 0)
        self.validate_required(self.parent_file_id, 'parent_file_id')
        if self.parent_file_id is not None:
            self.validate_max_length(self.parent_file_id, 'parent_file_id', 50)
            self.validate_pattern(self.parent_file_id, 'parent_file_id', '[a-z0-9.-_]{1,50}')
        if self.url_expire_sec is not None:
            self.validate_maximum(self.url_expire_sec, 'url_expire_sec', 14400)
            self.validate_minimum(self.url_expire_sec, 'url_expire_sec', 10)

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.starred is not None:
            result['Starred'] = self.starred
        if self.all is not None:
            result['all'] = self.all
        if self.category is not None:
            result['category'] = self.category
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.fields is not None:
            result['fields'] = self.fields
        if self.image_thumbnail_process is not None:
            result['image_thumbnail_process'] = self.image_thumbnail_process
        if self.image_url_process is not None:
            result['image_url_process'] = self.image_url_process
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        if self.order_by is not None:
            result['order_by'] = self.order_by
        if self.order_direction is not None:
            result['order_direction'] = self.order_direction
        if self.parent_file_id is not None:
            result['parent_file_id'] = self.parent_file_id
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        if self.url_expire_sec is not None:
            result['url_expire_sec'] = self.url_expire_sec
        if self.video_thumbnail_process is not None:
            result['video_thumbnail_process'] = self.video_thumbnail_process
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('Starred') is not None:
            self.starred = map.get('Starred')
        if map.get('all') is not None:
            self.all = map.get('all')
        if map.get('category') is not None:
            self.category = map.get('category')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('fields') is not None:
            self.fields = map.get('fields')
        if map.get('image_thumbnail_process') is not None:
            self.image_thumbnail_process = map.get('image_thumbnail_process')
        if map.get('image_url_process') is not None:
            self.image_url_process = map.get('image_url_process')
        if map.get('limit') is not None:
            self.limit = map.get('limit')
        if map.get('marker') is not None:
            self.marker = map.get('marker')
        if map.get('order_by') is not None:
            self.order_by = map.get('order_by')
        if map.get('order_direction') is not None:
            self.order_direction = map.get('order_direction')
        if map.get('parent_file_id') is not None:
            self.parent_file_id = map.get('parent_file_id')
        if map.get('status') is not None:
            self.status = map.get('status')
        if map.get('type') is not None:
            self.type = map.get('type')
        if map.get('url_expire_sec') is not None:
            self.url_expire_sec = map.get('url_expire_sec')
        if map.get('video_thumbnail_process') is not None:
            self.video_thumbnail_process = map.get('video_thumbnail_process')
        return self


class ListMyDriveRequest(TeaModel):
    """
    List my drive request
    """
    def __init__(self, headers=None, limit=None, marker=None):
        self.headers = headers          # type: Dict[str, str]
        # 每页大小限制
        self.limit = limit              # type: int
        # 翻页标记, 接口返回的标记值
        self.marker = marker            # type: str

    def validate(self):
        if self.limit is not None:
            self.validate_maximum(self.limit, 'limit', 100)
            self.validate_minimum(self.limit, 'limit', 1)

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('limit') is not None:
            self.limit = map.get('limit')
        if map.get('marker') is not None:
            self.marker = map.get('marker')
        return self


class ListShareLinkRequest(TeaModel):
    """
    list_share_link request
    """
    def __init__(self, headers=None, creator=None, limit=None, marker=None):
        self.headers = headers          # type: Dict[str, str]
        # creator
        self.creator = creator          # type: str
        # limit
        self.limit = limit              # type: int
        # marker
        self.marker = marker            # type: str

    def validate(self):
        if self.limit is not None:
            self.validate_maximum(self.limit, 'limit', 100)
            self.validate_minimum(self.limit, 'limit', 1)

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.creator is not None:
            result['creator'] = self.creator
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('creator') is not None:
            self.creator = map.get('creator')
        if map.get('limit') is not None:
            self.limit = map.get('limit')
        if map.get('marker') is not None:
            self.marker = map.get('marker')
        return self


class ListShareRequest(TeaModel):
    """
    list share request
    """
    def __init__(self, creator=None, drive_id=None, limit=None, marker=None, owner=None, share_file_path=None):
        # creator
        self.creator = creator          # type: str
        self.drive_id = drive_id        # type: str
        # limit
        self.limit = limit              # type: int
        # marker
        self.marker = marker            # type: str
        # Owner
        self.owner = owner              # type: str
        # share_file_path
        self.share_file_path = share_file_path  # type: str

    def validate(self):
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.limit is not None:
            self.validate_maximum(self.limit, 'limit', 100)
            self.validate_minimum(self.limit, 'limit', 1)

    def to_map(self):
        result = {}
        if self.creator is not None:
            result['creator'] = self.creator
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        if self.owner is not None:
            result['owner'] = self.owner
        if self.share_file_path is not None:
            result['share_file_path'] = self.share_file_path
        return result

    def from_map(self, map={}):
        if map.get('creator') is not None:
            self.creator = map.get('creator')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('limit') is not None:
            self.limit = map.get('limit')
        if map.get('marker') is not None:
            self.marker = map.get('marker')
        if map.get('owner') is not None:
            self.owner = map.get('owner')
        if map.get('share_file_path') is not None:
            self.share_file_path = map.get('share_file_path')
        return self


class ListStoreFileRequest(TeaModel):
    """
    list store file
    """
    def __init__(self, limit=None, marker=None, parent_file_path=None, store_id=None, type=None):
        # limit
        self.limit = limit              # type: int
        # marker
        self.marker = marker            # type: str
        # parent_file_path
        self.parent_file_path = parent_file_path  # type: str
        # store_id
        self.store_id = store_id        # type: str
        # type
        self.type = type                # type: str

    def validate(self):
        if self.limit is not None:
            self.validate_maximum(self.limit, 'limit', 1000)
            self.validate_minimum(self.limit, 'limit', 1)

    def to_map(self):
        result = {}
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        if self.parent_file_path is not None:
            result['parent_file_path'] = self.parent_file_path
        if self.store_id is not None:
            result['store_id'] = self.store_id
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, map={}):
        if map.get('limit') is not None:
            self.limit = map.get('limit')
        if map.get('marker') is not None:
            self.marker = map.get('marker')
        if map.get('parent_file_path') is not None:
            self.parent_file_path = map.get('parent_file_path')
        if map.get('store_id') is not None:
            self.store_id = map.get('store_id')
        if map.get('type') is not None:
            self.type = map.get('type')
        return self


class ListStoreRequest(TeaModel):
    """
    list storage file
    """
    def __init__(self, domain_id=None):
        # domain_id
        self.domain_id = domain_id      # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        return result

    def from_map(self, map={}):
        if map.get('domain_id') is not None:
            self.domain_id = map.get('domain_id')
        return self


class ListUploadedPartRequest(TeaModel):
    """
    列举uploadID对应的已上传分片
    """
    def __init__(self, headers=None, drive_id=None, file_id=None, limit=None, part_number_marker=None,
                 upload_id=None):
        self.headers = headers          # type: Dict[str, str]
        # drive_id
        self.drive_id = drive_id        # type: str
        # file_id
        self.file_id = file_id          # type: str
        # limit
        self.limit = limit              # type: int
        # part_number_marker
        self.part_number_marker = part_number_marker  # type: int
        # upload_id
        self.upload_id = upload_id      # type: str

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_id, 'file_id')
        if self.file_id is not None:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9.-_]{1,50}')
        if self.limit is not None:
            self.validate_pattern(self.limit, 'limit', '[0-9]+')
            self.validate_maximum(self.limit, 'limit', 1000)
            self.validate_minimum(self.limit, 'limit', 1)
        if self.part_number_marker is not None:
            self.validate_pattern(self.part_number_marker, 'part_number_marker', '[0-9]+')
            self.validate_minimum(self.part_number_marker, 'part_number_marker', 1)

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.limit is not None:
            result['limit'] = self.limit
        if self.part_number_marker is not None:
            result['part_number_marker'] = self.part_number_marker
        if self.upload_id is not None:
            result['upload_id'] = self.upload_id
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('file_id') is not None:
            self.file_id = map.get('file_id')
        if map.get('limit') is not None:
            self.limit = map.get('limit')
        if map.get('part_number_marker') is not None:
            self.part_number_marker = map.get('part_number_marker')
        if map.get('upload_id') is not None:
            self.upload_id = map.get('upload_id')
        return self


class MoveFileRequest(TeaModel):
    """
    文件移动请求
    """
    def __init__(self, headers=None, drive_id=None, file_id=None, new_name=None, overwrite=None,
                 to_parent_file_id=None):
        self.headers = headers          # type: Dict[str, str]
        # drive_id
        self.drive_id = drive_id        # type: str
        # file_id
        self.file_id = file_id          # type: str
        # new_name
        self.new_name = new_name        # type: str
        # overwrite
        # type: boolean
        self.overwrite = overwrite      # type: bool
        # to_parent_file_id
        self.to_parent_file_id = to_parent_file_id  # type: str

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_id, 'file_id')
        if self.file_id is not None:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9.-_]{1,50}')
        if self.new_name is not None:
            self.validate_max_length(self.new_name, 'new_name', 1024)
        self.validate_required(self.to_parent_file_id, 'to_parent_file_id')
        if self.to_parent_file_id is not None:
            self.validate_max_length(self.to_parent_file_id, 'to_parent_file_id', 50)

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.new_name is not None:
            result['new_name'] = self.new_name
        if self.overwrite is not None:
            result['overwrite'] = self.overwrite
        if self.to_parent_file_id is not None:
            result['to_parent_file_id'] = self.to_parent_file_id
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('file_id') is not None:
            self.file_id = map.get('file_id')
        if map.get('new_name') is not None:
            self.new_name = map.get('new_name')
        if map.get('overwrite') is not None:
            self.overwrite = map.get('overwrite')
        if map.get('to_parent_file_id') is not None:
            self.to_parent_file_id = map.get('to_parent_file_id')
        return self


class OSSCompleteFileRequest(TeaModel):
    """
    complete file request
    """
    def __init__(self, addition_data=None, drive_id=None, file_path=None, forbid_overwrite=None,
                 part_info_list=None, share_id=None, upload_id=None):
        # addition_data
        self.addition_data = addition_data  # type: dict
        # drive_id
        self.drive_id = drive_id        # type: str
        self.file_path = file_path      # type: str
        # forbid_overwrite
        # type: boolean
        self.forbid_overwrite = forbid_overwrite  # type: bool
        # part_info_list
        self.part_info_list = part_info_list  # type: List[UploadPartInfo]
        self.share_id = share_id        # type: str
        # upload_id
        self.upload_id = upload_id      # type: str

    def validate(self):
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.part_info_list:
            for k in self.part_info_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.addition_data is not None:
            result['addition_data'] = self.addition_data
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_path is not None:
            result['file_path'] = self.file_path
        if self.forbid_overwrite is not None:
            result['forbid_overwrite'] = self.forbid_overwrite
        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k in self.part_info_list:
                result['part_info_list'].append(k.to_map() if k else None)
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.upload_id is not None:
            result['upload_id'] = self.upload_id
        return result

    def from_map(self, map={}):
        if map.get('addition_data') is not None:
            self.addition_data = map.get('addition_data')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('file_path') is not None:
            self.file_path = map.get('file_path')
        if map.get('forbid_overwrite') is not None:
            self.forbid_overwrite = map.get('forbid_overwrite')
        self.part_info_list = []
        if map.get('part_info_list') is not None:
            for k in map.get('part_info_list'):
                temp_model = UploadPartInfo()
                self.part_info_list.append(temp_model.from_map(k))
        if map.get('share_id') is not None:
            self.share_id = map.get('share_id')
        if map.get('upload_id') is not None:
            self.upload_id = map.get('upload_id')
        return self


class OSSCopyFileRequest(TeaModel):
    """
    copy file request
    """
    def __init__(self, drive_id=None, file_path=None, new_name=None, overwrite=None, share_id=None, to_drive_id=None,
                 to_parent_file_path=None, to_share_id=None):
        # drive_id
        self.drive_id = drive_id        # type: str
        # file_path
        self.file_path = file_path      # type: str
        # new_name
        self.new_name = new_name        # type: str
        # overwrite
        # type: boolean
        self.overwrite = overwrite      # type: bool
        # share_id
        self.share_id = share_id        # type: str
        # to_drive_id
        self.to_drive_id = to_drive_id  # type: str
        # to_parent_file_path
        self.to_parent_file_path = to_parent_file_path  # type: str
        # share_id
        self.to_share_id = to_share_id  # type: str

    def validate(self):
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_path, 'file_path')
        if self.new_name is not None:
            self.validate_pattern(self.new_name, 'new_name', '[a-zA-Z0-9.-]{1,1000}')
        if self.share_id is not None:
            self.validate_pattern(self.share_id, 'share_id', '[0-9a-zA-Z-]+')
        if self.to_drive_id is not None:
            self.validate_pattern(self.to_drive_id, 'to_drive_id', '[0-9]+')
        self.validate_required(self.to_parent_file_path, 'to_parent_file_path')

    def to_map(self):
        result = {}
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_path is not None:
            result['file_path'] = self.file_path
        if self.new_name is not None:
            result['new_name'] = self.new_name
        if self.overwrite is not None:
            result['overwrite'] = self.overwrite
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.to_drive_id is not None:
            result['to_drive_id'] = self.to_drive_id
        if self.to_parent_file_path is not None:
            result['to_parent_file_path'] = self.to_parent_file_path
        if self.to_share_id is not None:
            result['to_share_id'] = self.to_share_id
        return result

    def from_map(self, map={}):
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('file_path') is not None:
            self.file_path = map.get('file_path')
        if map.get('new_name') is not None:
            self.new_name = map.get('new_name')
        if map.get('overwrite') is not None:
            self.overwrite = map.get('overwrite')
        if map.get('share_id') is not None:
            self.share_id = map.get('share_id')
        if map.get('to_drive_id') is not None:
            self.to_drive_id = map.get('to_drive_id')
        if map.get('to_parent_file_path') is not None:
            self.to_parent_file_path = map.get('to_parent_file_path')
        if map.get('to_share_id') is not None:
            self.to_share_id = map.get('to_share_id')
        return self


class OSSCreateFileRequest(TeaModel):
    """
    create file request
    """
    def __init__(self, addition_data=None, content_md_5=None, content_type=None, drive_id=None,
                 forbid_overwrite=None, name=None, parent_file_path=None, part_info_list=None, share_id=None, size=None, type=None):
        # addition_data
        self.addition_data = addition_data  # type: dict
        # ContentMd5
        self.content_md_5 = content_md_5  # type: str
        # ContentType
        self.content_type = content_type  # type: str
        # drive_id
        self.drive_id = drive_id        # type: str
        # forbid_overwrite
        # type: boolean
        self.forbid_overwrite = forbid_overwrite  # type: bool
        # Name
        self.name = name                # type: str
        # parent_file_path
        self.parent_file_path = parent_file_path  # type: str
        # part_info_list
        self.part_info_list = part_info_list  # type: List[UploadPartInfo]
        # share_id
        self.share_id = share_id        # type: str
        # Size
        self.size = size                # type: int
        # Type
        self.type = type                # type: str

    def validate(self):
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.name, 'name')
        if self.name is not None:
            self.validate_max_length(self.name, 'name', 1024)
        self.validate_required(self.parent_file_path, 'parent_file_path')
        if self.part_info_list:
            for k in self.part_info_list:
                if k:
                    k.validate()
        if self.share_id is not None:
            self.validate_pattern(self.share_id, 'share_id', '[0-9a-zA-Z-]+')
        if self.size is not None:
            self.validate_maximum(self.size, 'size', 53687091200)
            self.validate_minimum(self.size, 'size', 0)
        self.validate_required(self.type, 'type')

    def to_map(self):
        result = {}
        if self.addition_data is not None:
            result['addition_data'] = self.addition_data
        if self.content_md_5 is not None:
            result['content_md5'] = self.content_md_5
        if self.content_type is not None:
            result['content_type'] = self.content_type
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.forbid_overwrite is not None:
            result['forbid_overwrite'] = self.forbid_overwrite
        if self.name is not None:
            result['name'] = self.name
        if self.parent_file_path is not None:
            result['parent_file_path'] = self.parent_file_path
        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k in self.part_info_list:
                result['part_info_list'].append(k.to_map() if k else None)
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.size is not None:
            result['size'] = self.size
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, map={}):
        if map.get('addition_data') is not None:
            self.addition_data = map.get('addition_data')
        if map.get('content_md5') is not None:
            self.content_md_5 = map.get('content_md5')
        if map.get('content_type') is not None:
            self.content_type = map.get('content_type')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('forbid_overwrite') is not None:
            self.forbid_overwrite = map.get('forbid_overwrite')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('parent_file_path') is not None:
            self.parent_file_path = map.get('parent_file_path')
        self.part_info_list = []
        if map.get('part_info_list') is not None:
            for k in map.get('part_info_list'):
                temp_model = UploadPartInfo()
                self.part_info_list.append(temp_model.from_map(k))
        if map.get('share_id') is not None:
            self.share_id = map.get('share_id')
        if map.get('size') is not None:
            self.size = map.get('size')
        if map.get('type') is not None:
            self.type = map.get('type')
        return self


class OSSDeleteFileRequest(TeaModel):
    """
    删除文件请求
    """
    def __init__(self, drive_id=None, file_path=None, permanently=None, share_id=None):
        # drive_id
        self.drive_id = drive_id        # type: str
        # file_path
        self.file_path = file_path      # type: str
        # permanently
        # type: false
        self.permanently = permanently  # type: bool
        # share_id
        self.share_id = share_id        # type: str

    def validate(self):
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_path, 'file_path')
        if self.file_path is not None:
            self.validate_max_length(self.file_path, 'file_path', 1000)
        if self.share_id is not None:
            self.validate_pattern(self.share_id, 'share_id', '[0-9a-zA-Z-]+')

    def to_map(self):
        result = {}
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_path is not None:
            result['file_path'] = self.file_path
        if self.permanently is not None:
            result['permanently'] = self.permanently
        if self.share_id is not None:
            result['share_id'] = self.share_id
        return result

    def from_map(self, map={}):
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('file_path') is not None:
            self.file_path = map.get('file_path')
        if map.get('permanently') is not None:
            self.permanently = map.get('permanently')
        if map.get('share_id') is not None:
            self.share_id = map.get('share_id')
        return self


class OSSGetDownloadUrlRequest(TeaModel):
    """
    获取文件下载地址的请求body
    """
    def __init__(self, drive_id=None, expire_sec=None, file_name=None, file_path=None, share_id=None):
        # drive_id
        self.drive_id = drive_id        # type: str
        # expire_sec
        self.expire_sec = expire_sec    # type: int
        # file_name
        self.file_name = file_name      # type: str
        # file_path
        self.file_path = file_path      # type: str
        # share_id
        self.share_id = share_id        # type: str

    def validate(self):
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.expire_sec is not None:
            self.validate_maximum(self.expire_sec, 'expire_sec', 14400)
            self.validate_minimum(self.expire_sec, 'expire_sec', 10)
        self.validate_required(self.file_path, 'file_path')
        if self.file_path is not None:
            self.validate_max_length(self.file_path, 'file_path', 1000)
        if self.share_id is not None:
            self.validate_pattern(self.share_id, 'share_id', '[0-9a-zA-Z-]+')

    def to_map(self):
        result = {}
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.expire_sec is not None:
            result['expire_sec'] = self.expire_sec
        if self.file_name is not None:
            result['file_name'] = self.file_name
        if self.file_path is not None:
            result['file_path'] = self.file_path
        if self.share_id is not None:
            result['share_id'] = self.share_id
        return result

    def from_map(self, map={}):
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('expire_sec') is not None:
            self.expire_sec = map.get('expire_sec')
        if map.get('file_name') is not None:
            self.file_name = map.get('file_name')
        if map.get('file_path') is not None:
            self.file_path = map.get('file_path')
        if map.get('share_id') is not None:
            self.share_id = map.get('share_id')
        return self


class OSSGetFileRequest(TeaModel):
    """
    获取文件元数据
    """
    def __init__(self, drive_id=None, file_path=None, image_thumbnail_process=None, image_url_process=None,
                 share_id=None, url_expire_sec=None):
        # drive_id
        self.drive_id = drive_id        # type: str
        # file_id
        self.file_path = file_path      # type: str
        # image_thumbnail_process
        # type:string
        self.image_thumbnail_process = image_thumbnail_process  # type: str
        # image_thumbnail_process
        # type:string
        self.image_url_process = image_url_process  # type: str
        # share_id
        self.share_id = share_id        # type: str
        # url_expire_sec
        self.url_expire_sec = url_expire_sec  # type: int

    def validate(self):
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_path, 'file_path')
        if self.file_path is not None:
            self.validate_max_length(self.file_path, 'file_path', 1000)
        if self.share_id is not None:
            self.validate_pattern(self.share_id, 'share_id', '[0-9a-zA-Z-]+')
        if self.url_expire_sec is not None:
            self.validate_maximum(self.url_expire_sec, 'url_expire_sec', 14400)
            self.validate_minimum(self.url_expire_sec, 'url_expire_sec', 10)

    def to_map(self):
        result = {}
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_path is not None:
            result['file_path'] = self.file_path
        if self.image_thumbnail_process is not None:
            result['image_thumbnail_process'] = self.image_thumbnail_process
        if self.image_url_process is not None:
            result['image_url_process'] = self.image_url_process
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.url_expire_sec is not None:
            result['url_expire_sec'] = self.url_expire_sec
        return result

    def from_map(self, map={}):
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('file_path') is not None:
            self.file_path = map.get('file_path')
        if map.get('image_thumbnail_process') is not None:
            self.image_thumbnail_process = map.get('image_thumbnail_process')
        if map.get('image_url_process') is not None:
            self.image_url_process = map.get('image_url_process')
        if map.get('share_id') is not None:
            self.share_id = map.get('share_id')
        if map.get('url_expire_sec') is not None:
            self.url_expire_sec = map.get('url_expire_sec')
        return self


class OSSGetSecureUrlRequest(TeaModel):
    """
    获取文件安全地址的请求body
    """
    def __init__(self, drive_id=None, expire_sec=None, file_path=None, secure_ip=None, share_id=None):
        # drive_id
        self.drive_id = drive_id        # type: str
        # expire_sec 单位秒
        self.expire_sec = expire_sec    # type: int
        # file_path
        self.file_path = file_path      # type: str
        # secure_ip
        self.secure_ip = secure_ip      # type: str
        # share_id
        self.share_id = share_id        # type: str

    def validate(self):
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_path, 'file_path')
        if self.file_path is not None:
            self.validate_max_length(self.file_path, 'file_path', 1000)
        if self.share_id is not None:
            self.validate_pattern(self.share_id, 'share_id', '[0-9a-zA-Z-]+')

    def to_map(self):
        result = {}
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.expire_sec is not None:
            result['expire_sec'] = self.expire_sec
        if self.file_path is not None:
            result['file_path'] = self.file_path
        if self.secure_ip is not None:
            result['secure_ip'] = self.secure_ip
        if self.share_id is not None:
            result['share_id'] = self.share_id
        return result

    def from_map(self, map={}):
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('expire_sec') is not None:
            self.expire_sec = map.get('expire_sec')
        if map.get('file_path') is not None:
            self.file_path = map.get('file_path')
        if map.get('secure_ip') is not None:
            self.secure_ip = map.get('secure_ip')
        if map.get('share_id') is not None:
            self.share_id = map.get('share_id')
        return self


class OSSGetUploadUrlRequest(TeaModel):
    """
    获取文件上传URL
    """
    def __init__(self, content_md_5=None, drive_id=None, file_path=None, part_info_list=None, share_id=None,
                 upload_id=None):
        # content_md5
        self.content_md_5 = content_md_5  # type: str
        # drive_id
        self.drive_id = drive_id        # type: str
        # file_path
        self.file_path = file_path      # type: str
        # upload_part_list
        self.part_info_list = part_info_list  # type: List[UploadPartInfo]
        # share_id
        self.share_id = share_id        # type: str
        # upload_id
        self.upload_id = upload_id      # type: str

    def validate(self):
        if self.content_md_5 is not None:
            self.validate_max_length(self.content_md_5, 'content_md_5', 32)
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_path, 'file_path')
        if self.part_info_list:
            for k in self.part_info_list:
                if k:
                    k.validate()
        if self.share_id is not None:
            self.validate_pattern(self.share_id, 'share_id', '[0-9a-zA-Z-]+')
        self.validate_required(self.upload_id, 'upload_id')

    def to_map(self):
        result = {}
        if self.content_md_5 is not None:
            result['content_md5'] = self.content_md_5
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_path is not None:
            result['file_path'] = self.file_path
        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k in self.part_info_list:
                result['part_info_list'].append(k.to_map() if k else None)
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.upload_id is not None:
            result['upload_id'] = self.upload_id
        return result

    def from_map(self, map={}):
        if map.get('content_md5') is not None:
            self.content_md_5 = map.get('content_md5')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('file_path') is not None:
            self.file_path = map.get('file_path')
        self.part_info_list = []
        if map.get('part_info_list') is not None:
            for k in map.get('part_info_list'):
                temp_model = UploadPartInfo()
                self.part_info_list.append(temp_model.from_map(k))
        if map.get('share_id') is not None:
            self.share_id = map.get('share_id')
        if map.get('upload_id') is not None:
            self.upload_id = map.get('upload_id')
        return self


class OSSListFileRequest(TeaModel):
    """
    list file request
    """
    def __init__(self, drive_id=None, image_thumbnail_process=None, image_url_process=None, limit=None, marker=None,
                 parent_file_path=None, share_id=None, url_expire_sec=None, video_thumbnail_process=None):
        # drive_id
        self.drive_id = drive_id        # type: str
        # image_thumbnail_process
        self.image_thumbnail_process = image_thumbnail_process  # type: str
        # image_url_process
        self.image_url_process = image_url_process  # type: str
        # limit
        self.limit = limit              # type: int
        # marker
        self.marker = marker            # type: str
        # ParentFilePath
        self.parent_file_path = parent_file_path  # type: str
        # share_id
        self.share_id = share_id        # type: str
        # url_expire_sec
        self.url_expire_sec = url_expire_sec  # type: int
        # video_thumbnail_process
        # type:string
        self.video_thumbnail_process = video_thumbnail_process  # type: str

    def validate(self):
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.limit is not None:
            self.validate_pattern(self.limit, 'limit', '[0-9]{1,3}')
            self.validate_maximum(self.limit, 'limit', 100)
            self.validate_minimum(self.limit, 'limit', 0)
        self.validate_required(self.parent_file_path, 'parent_file_path')
        if self.share_id is not None:
            self.validate_pattern(self.share_id, 'share_id', '[0-9a-zA-Z-]+')
        if self.url_expire_sec is not None:
            self.validate_maximum(self.url_expire_sec, 'url_expire_sec', 14400)
            self.validate_minimum(self.url_expire_sec, 'url_expire_sec', 10)

    def to_map(self):
        result = {}
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.image_thumbnail_process is not None:
            result['image_thumbnail_process'] = self.image_thumbnail_process
        if self.image_url_process is not None:
            result['image_url_process'] = self.image_url_process
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        if self.parent_file_path is not None:
            result['parent_file_path'] = self.parent_file_path
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.url_expire_sec is not None:
            result['url_expire_sec'] = self.url_expire_sec
        if self.video_thumbnail_process is not None:
            result['video_thumbnail_process'] = self.video_thumbnail_process
        return result

    def from_map(self, map={}):
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('image_thumbnail_process') is not None:
            self.image_thumbnail_process = map.get('image_thumbnail_process')
        if map.get('image_url_process') is not None:
            self.image_url_process = map.get('image_url_process')
        if map.get('limit') is not None:
            self.limit = map.get('limit')
        if map.get('marker') is not None:
            self.marker = map.get('marker')
        if map.get('parent_file_path') is not None:
            self.parent_file_path = map.get('parent_file_path')
        if map.get('share_id') is not None:
            self.share_id = map.get('share_id')
        if map.get('url_expire_sec') is not None:
            self.url_expire_sec = map.get('url_expire_sec')
        if map.get('video_thumbnail_process') is not None:
            self.video_thumbnail_process = map.get('video_thumbnail_process')
        return self


class OSSListUploadedPartRequest(TeaModel):
    """
    列举uploadID对应的已上传分片
    """
    def __init__(self, drive_id=None, file_path=None, limit=None, part_number_marker=None, share_id=None,
                 upload_id=None):
        # drive_id
        self.drive_id = drive_id        # type: str
        # file_path
        self.file_path = file_path      # type: str
        # limit
        self.limit = limit              # type: int
        # part_number_marker
        self.part_number_marker = part_number_marker  # type: int
        # share_id
        self.share_id = share_id        # type: str
        # upload_id
        self.upload_id = upload_id      # type: str

    def validate(self):
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_path, 'file_path')
        if self.limit is not None:
            self.validate_pattern(self.limit, 'limit', '[0-9]+')
            self.validate_maximum(self.limit, 'limit', 1000)
            self.validate_minimum(self.limit, 'limit', 1)
        if self.part_number_marker is not None:
            self.validate_pattern(self.part_number_marker, 'part_number_marker', '[0-9]+')
            self.validate_minimum(self.part_number_marker, 'part_number_marker', 1)
        if self.share_id is not None:
            self.validate_pattern(self.share_id, 'share_id', '[0-9a-zA-Z-]+')

    def to_map(self):
        result = {}
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_path is not None:
            result['file_path'] = self.file_path
        if self.limit is not None:
            result['limit'] = self.limit
        if self.part_number_marker is not None:
            result['part_number_marker'] = self.part_number_marker
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.upload_id is not None:
            result['upload_id'] = self.upload_id
        return result

    def from_map(self, map={}):
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('file_path') is not None:
            self.file_path = map.get('file_path')
        if map.get('limit') is not None:
            self.limit = map.get('limit')
        if map.get('part_number_marker') is not None:
            self.part_number_marker = map.get('part_number_marker')
        if map.get('share_id') is not None:
            self.share_id = map.get('share_id')
        if map.get('upload_id') is not None:
            self.upload_id = map.get('upload_id')
        return self


class OSSMoveFileRequest(TeaModel):
    """
    文件移动请求
    """
    def __init__(self, drive_id=None, file_path=None, new_name=None, overwrite=None, share_id=None,
                 to_parent_file_path=None):
        # drive_id
        self.drive_id = drive_id        # type: str
        # file_path
        self.file_path = file_path      # type: str
        # new_name
        self.new_name = new_name        # type: str
        # overwrite
        # type: boolean
        self.overwrite = overwrite      # type: bool
        # share_id
        self.share_id = share_id        # type: str
        # file_path
        self.to_parent_file_path = to_parent_file_path  # type: str

    def validate(self):
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.share_id is not None:
            self.validate_pattern(self.share_id, 'share_id', '[0-9a-zA-Z-]+')

    def to_map(self):
        result = {}
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_path is not None:
            result['file_path'] = self.file_path
        if self.new_name is not None:
            result['new_name'] = self.new_name
        if self.overwrite is not None:
            result['overwrite'] = self.overwrite
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.to_parent_file_path is not None:
            result['to_parent_file_path'] = self.to_parent_file_path
        return result

    def from_map(self, map={}):
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('file_path') is not None:
            self.file_path = map.get('file_path')
        if map.get('new_name') is not None:
            self.new_name = map.get('new_name')
        if map.get('overwrite') is not None:
            self.overwrite = map.get('overwrite')
        if map.get('share_id') is not None:
            self.share_id = map.get('share_id')
        if map.get('to_parent_file_path') is not None:
            self.to_parent_file_path = map.get('to_parent_file_path')
        return self


class OSSVideoDRMLicenseRequest(TeaModel):
    """
    获取视频DRM License
    """
    def __init__(self, drm_type=None, license_request=None):
        # drmType
        self.drm_type = drm_type        # type: str
        # licenseRequest
        self.license_request = license_request  # type: str

    def validate(self):
        self.validate_required(self.drm_type, 'drm_type')
        self.validate_required(self.license_request, 'license_request')

    def to_map(self):
        result = {}
        if self.drm_type is not None:
            result['drmType'] = self.drm_type
        if self.license_request is not None:
            result['licenseRequest'] = self.license_request
        return result

    def from_map(self, map={}):
        if map.get('drmType') is not None:
            self.drm_type = map.get('drmType')
        if map.get('licenseRequest') is not None:
            self.license_request = map.get('licenseRequest')
        return self


class OSSVideoDefinitionRequest(TeaModel):
    """
    获取视频分辨率列表
    """
    def __init__(self, drive_id=None, file_path=None, protection_scheme=None, share_id=None):
        # drive_id
        self.drive_id = drive_id        # type: str
        # file_path
        self.file_path = file_path      # type: str
        # protection_scheme
        self.protection_scheme = protection_scheme  # type: str
        # share_id
        self.share_id = share_id        # type: str

    def validate(self):
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_path, 'file_path')
        if self.file_path is not None:
            self.validate_max_length(self.file_path, 'file_path', 1000)
        if self.share_id is not None:
            self.validate_pattern(self.share_id, 'share_id', '[0-9a-zA-Z-]+')

    def to_map(self):
        result = {}
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_path is not None:
            result['file_path'] = self.file_path
        if self.protection_scheme is not None:
            result['protection_scheme'] = self.protection_scheme
        if self.share_id is not None:
            result['share_id'] = self.share_id
        return result

    def from_map(self, map={}):
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('file_path') is not None:
            self.file_path = map.get('file_path')
        if map.get('protection_scheme') is not None:
            self.protection_scheme = map.get('protection_scheme')
        if map.get('share_id') is not None:
            self.share_id = map.get('share_id')
        return self


class OSSVideoM3U8Request(TeaModel):
    """
    获取视频的m3u8文件
    """
    def __init__(self, definition=None, drive_id=None, expire_sec=None, file_path=None, protection_scheme=None,
                 share_id=None, sign_token=None):
        # definition
        self.definition = definition    # type: str
        # drive_id
        self.drive_id = drive_id        # type: str
        # expire_sec
        self.expire_sec = expire_sec    # type: int
        # file_path
        self.file_path = file_path      # type: str
        # protection_scheme
        self.protection_scheme = protection_scheme  # type: str
        # share_id
        self.share_id = share_id        # type: str
        # sign_token
        self.sign_token = sign_token    # type: str

    def validate(self):
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.expire_sec is not None:
            self.validate_maximum(self.expire_sec, 'expire_sec', 86400)
            self.validate_minimum(self.expire_sec, 'expire_sec', 60)
        self.validate_required(self.file_path, 'file_path')
        if self.file_path is not None:
            self.validate_max_length(self.file_path, 'file_path', 1000)
        if self.share_id is not None:
            self.validate_pattern(self.share_id, 'share_id', '[0-9a-zA-Z-]+')
        self.validate_required(self.sign_token, 'sign_token')

    def to_map(self):
        result = {}
        if self.definition is not None:
            result['definition'] = self.definition
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.expire_sec is not None:
            result['expire_sec'] = self.expire_sec
        if self.file_path is not None:
            result['file_path'] = self.file_path
        if self.protection_scheme is not None:
            result['protection_scheme'] = self.protection_scheme
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.sign_token is not None:
            result['sign_token'] = self.sign_token
        return result

    def from_map(self, map={}):
        if map.get('definition') is not None:
            self.definition = map.get('definition')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('expire_sec') is not None:
            self.expire_sec = map.get('expire_sec')
        if map.get('file_path') is not None:
            self.file_path = map.get('file_path')
        if map.get('protection_scheme') is not None:
            self.protection_scheme = map.get('protection_scheme')
        if map.get('share_id') is not None:
            self.share_id = map.get('share_id')
        if map.get('sign_token') is not None:
            self.sign_token = map.get('sign_token')
        return self


class OSSVideoTranscodeRequest(TeaModel):
    """
    启动视频转码请求
    """
    def __init__(self, drive_id=None, file_path=None, hls_time=None, protection_scheme=None, remarks=None,
                 share_id=None, transcode=None):
        # drive_id
        self.drive_id = drive_id        # type: str
        # file_path
        self.file_path = file_path      # type: str
        # hls_time
        self.hls_time = hls_time        # type: int
        # protection_scheme
        self.protection_scheme = protection_scheme  # type: str
        # remarks
        self.remarks = remarks          # type: str
        # share_id
        self.share_id = share_id        # type: str
        # transcode
        self.transcode = transcode      # type: bool

    def validate(self):
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_path, 'file_path')
        if self.file_path is not None:
            self.validate_max_length(self.file_path, 'file_path', 1000)
        if self.share_id is not None:
            self.validate_pattern(self.share_id, 'share_id', '[0-9a-zA-Z-]+')

    def to_map(self):
        result = {}
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_path is not None:
            result['file_path'] = self.file_path
        if self.hls_time is not None:
            result['hls_time'] = self.hls_time
        if self.protection_scheme is not None:
            result['protection_scheme'] = self.protection_scheme
        if self.remarks is not None:
            result['remarks'] = self.remarks
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.transcode is not None:
            result['transcode'] = self.transcode
        return result

    def from_map(self, map={}):
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('file_path') is not None:
            self.file_path = map.get('file_path')
        if map.get('hls_time') is not None:
            self.hls_time = map.get('hls_time')
        if map.get('protection_scheme') is not None:
            self.protection_scheme = map.get('protection_scheme')
        if map.get('remarks') is not None:
            self.remarks = map.get('remarks')
        if map.get('share_id') is not None:
            self.share_id = map.get('share_id')
        if map.get('transcode') is not None:
            self.transcode = map.get('transcode')
        return self


class PlayMediaRequest(TeaModel):
    """
    play_media request
    """
    def __init__(self, auth_key=None, drive_id=None, file_id=None):
        # auth_key
        self.auth_key = auth_key        # type: str
        # drive_id
        self.drive_id = drive_id        # type: str
        # file_id
        self.file_id = file_id          # type: str

    def validate(self):
        self.validate_required(self.auth_key, 'auth_key')
        if self.auth_key is not None:
            self.validate_pattern(self.auth_key, 'auth_key', '[a-z0-9]+')
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_id, 'file_id')
        if self.file_id is not None:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9.-_]{1,50}')

    def to_map(self):
        result = {}
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        if self.drive_id is not None:
            result['DriveID'] = self.drive_id
        if self.file_id is not None:
            result['FileID'] = self.file_id
        return result

    def from_map(self, map={}):
        if map.get('AuthKey') is not None:
            self.auth_key = map.get('AuthKey')
        if map.get('DriveID') is not None:
            self.drive_id = map.get('DriveID')
        if map.get('FileID') is not None:
            self.file_id = map.get('FileID')
        return self


class ScanFileMetaRequest(TeaModel):
    """
    全量获取file元信息的请求body
    """
    def __init__(self, headers=None, category=None, drive_id=None, limit=None, marker=None):
        self.headers = headers          # type: Dict[str, str]
        # category
        self.category = category        # type: str
        # drive_id
        self.drive_id = drive_id        # type: str
        # limit
        self.limit = limit              # type: int
        # marker
        self.marker = marker            # type: str

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.limit is not None:
            self.validate_maximum(self.limit, 'limit', 5000)
            self.validate_minimum(self.limit, 'limit', 1)

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.category is not None:
            result['category'] = self.category
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('category') is not None:
            self.category = map.get('category')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('limit') is not None:
            self.limit = map.get('limit')
        if map.get('marker') is not None:
            self.marker = map.get('marker')
        return self


class SearchFileRequest(TeaModel):
    """
    搜索文件元数据
    """
    def __init__(self, headers=None, drive_id=None, image_thumbnail_process=None, image_url_process=None,
                 limit=None, marker=None, order_by=None, query=None, url_expire_sec=None, video_thumbnail_process=None):
        self.headers = headers          # type: Dict[str, str]
        # drive_id
        self.drive_id = drive_id        # type: str
        # image_thumbnail_process
        self.image_thumbnail_process = image_thumbnail_process  # type: str
        # image_url_process
        self.image_url_process = image_url_process  # type: str
        # limit
        self.limit = limit              # type: int
        # Marker
        self.marker = marker            # type: str
        # order_by
        self.order_by = order_by        # type: str
        # query
        self.query = query              # type: str
        # url_expire_sec
        self.url_expire_sec = url_expire_sec  # type: int
        # video_thumbnail_process
        # type:string
        self.video_thumbnail_process = video_thumbnail_process  # type: str

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.limit is not None:
            self.validate_maximum(self.limit, 'limit', 100)
            self.validate_minimum(self.limit, 'limit', 1)
        if self.query is not None:
            self.validate_max_length(self.query, 'query', 4096)
        if self.url_expire_sec is not None:
            self.validate_maximum(self.url_expire_sec, 'url_expire_sec', 14400)
            self.validate_minimum(self.url_expire_sec, 'url_expire_sec', 10)

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.image_thumbnail_process is not None:
            result['image_thumbnail_process'] = self.image_thumbnail_process
        if self.image_url_process is not None:
            result['image_url_process'] = self.image_url_process
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        if self.order_by is not None:
            result['order_by'] = self.order_by
        if self.query is not None:
            result['query'] = self.query
        if self.url_expire_sec is not None:
            result['url_expire_sec'] = self.url_expire_sec
        if self.video_thumbnail_process is not None:
            result['video_thumbnail_process'] = self.video_thumbnail_process
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('image_thumbnail_process') is not None:
            self.image_thumbnail_process = map.get('image_thumbnail_process')
        if map.get('image_url_process') is not None:
            self.image_url_process = map.get('image_url_process')
        if map.get('limit') is not None:
            self.limit = map.get('limit')
        if map.get('marker') is not None:
            self.marker = map.get('marker')
        if map.get('order_by') is not None:
            self.order_by = map.get('order_by')
        if map.get('query') is not None:
            self.query = map.get('query')
        if map.get('url_expire_sec') is not None:
            self.url_expire_sec = map.get('url_expire_sec')
        if map.get('video_thumbnail_process') is not None:
            self.video_thumbnail_process = map.get('video_thumbnail_process')
        return self


class UCGetObjectInfoByObjectKeyRequest(TeaModel):
    """
    UCGetObjectInfoByObjectKeyRequest
    """
    def __init__(self, object_key=None):
        self.object_key = object_key    # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.object_key is not None:
            result['object_key'] = self.object_key
        return result

    def from_map(self, map={}):
        if map.get('object_key') is not None:
            self.object_key = map.get('object_key')
        return self


class UCGetObjectInfoBySha1Request(TeaModel):
    """
    UCGetObjectInfoBySha1Request
    """
    def __init__(self, sha_1=None):
        self.sha_1 = sha_1              # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.sha_1 is not None:
            result['sha1'] = self.sha_1
        return result

    def from_map(self, map={}):
        if map.get('sha1') is not None:
            self.sha_1 = map.get('sha1')
        return self


class UpdateDriveRequest(TeaModel):
    """
    Update drive request
    """
    def __init__(self, headers=None, description=None, drive_id=None, drive_name=None, encrypt_data_access=None,
                 encrypt_mode=None, status=None, total_size=None):
        self.headers = headers          # type: Dict[str, str]
        # 描述信息
        self.description = description  # type: str
        # Drive ID
        self.drive_id = drive_id        # type: str
        # Drive 名称
        self.drive_name = drive_name    # type: str
        # 授权访问加密数据
        self.encrypt_data_access = encrypt_data_access  # type: bool
        # 加密模式
        self.encrypt_mode = encrypt_mode  # type: str
        # 状态
        self.status = status            # type: str
        # 总大小,单位Byte [如果设置 -1 代表不限制]
        self.total_size = total_size    # type: int

    def validate(self):
        if self.description is not None:
            self.validate_max_length(self.description, 'description', 1024)
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_name is not None:
            self.validate_max_length(self.drive_name, 'drive_name', 1024)

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.description is not None:
            result['description'] = self.description
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.drive_name is not None:
            result['drive_name'] = self.drive_name
        if self.encrypt_data_access is not None:
            result['encrypt_data_access'] = self.encrypt_data_access
        if self.encrypt_mode is not None:
            result['encrypt_mode'] = self.encrypt_mode
        if self.status is not None:
            result['status'] = self.status
        if self.total_size is not None:
            result['total_size'] = self.total_size
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('description') is not None:
            self.description = map.get('description')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('drive_name') is not None:
            self.drive_name = map.get('drive_name')
        if map.get('encrypt_data_access') is not None:
            self.encrypt_data_access = map.get('encrypt_data_access')
        if map.get('encrypt_mode') is not None:
            self.encrypt_mode = map.get('encrypt_mode')
        if map.get('status') is not None:
            self.status = map.get('status')
        if map.get('total_size') is not None:
            self.total_size = map.get('total_size')
        return self


class UpdateFileMetaRequest(TeaModel):
    """
    更新文件元数据
    """
    def __init__(self, headers=None, check_name_mode=None, custom_index_key=None, description=None, drive_id=None,
                 encrypt_mode=None, file_id=None, hidden=None, labels=None, meta=None, name=None, starred=None, user_meta=None):
        self.headers = headers          # type: Dict[str, str]
        # check_name_mode
        self.check_name_mode = check_name_mode  # type: str
        self.custom_index_key = custom_index_key  # type: str
        # description
        # type: string
        self.description = description  # type: str
        # drive_id
        self.drive_id = drive_id        # type: str
        self.encrypt_mode = encrypt_mode  # type: str
        # file_id
        self.file_id = file_id          # type: str
        # hidden
        # type: boolean
        self.hidden = hidden            # type: bool
        # labels
        self.labels = labels            # type: List[str]
        self.meta = meta                # type: str
        # name
        self.name = name                # type: str
        # starred
        # type: boolean
        self.starred = starred          # type: bool
        # user_meta
        self.user_meta = user_meta      # type: str

    def validate(self):
        if self.description is not None:
            self.validate_max_length(self.description, 'description', 1024)
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_id, 'file_id')
        if self.file_id is not None:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9.-_]{1,50}')
        if self.name is not None:
            self.validate_max_length(self.name, 'name', 1024)

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.check_name_mode is not None:
            result['check_name_mode'] = self.check_name_mode
        if self.custom_index_key is not None:
            result['custom_index_key'] = self.custom_index_key
        if self.description is not None:
            result['description'] = self.description
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.encrypt_mode is not None:
            result['encrypt_mode'] = self.encrypt_mode
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.hidden is not None:
            result['hidden'] = self.hidden
        if self.labels is not None:
            result['labels'] = self.labels
        if self.meta is not None:
            result['meta'] = self.meta
        if self.name is not None:
            result['name'] = self.name
        if self.starred is not None:
            result['starred'] = self.starred
        if self.user_meta is not None:
            result['user_meta'] = self.user_meta
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('check_name_mode') is not None:
            self.check_name_mode = map.get('check_name_mode')
        if map.get('custom_index_key') is not None:
            self.custom_index_key = map.get('custom_index_key')
        if map.get('description') is not None:
            self.description = map.get('description')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('encrypt_mode') is not None:
            self.encrypt_mode = map.get('encrypt_mode')
        if map.get('file_id') is not None:
            self.file_id = map.get('file_id')
        if map.get('hidden') is not None:
            self.hidden = map.get('hidden')
        if map.get('labels') is not None:
            self.labels = map.get('labels')
        if map.get('meta') is not None:
            self.meta = map.get('meta')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('starred') is not None:
            self.starred = map.get('starred')
        if map.get('user_meta') is not None:
            self.user_meta = map.get('user_meta')
        return self


class UpdateShareRequest(TeaModel):
    """
    update share request
    """
    def __init__(self, description=None, expiration=None, permissions=None, share_id=None, share_name=None,
                 share_policy=None, status=None):
        # description
        self.description = description  # type: str
        # expiration
        self.expiration = expiration    # type: str
        # permissions
        self.permissions = permissions  # type: List[str]
        # share_id
        self.share_id = share_id        # type: str
        # share_name
        self.share_name = share_name    # type: str
        # share_policy
        self.share_policy = share_policy  # type: List[SharePermissionPolicy]
        # status
        self.status = status            # type: str

    def validate(self):
        if self.description is not None:
            self.validate_max_length(self.description, 'description', 1024)
        self.validate_required(self.share_id, 'share_id')
        if self.share_policy:
            for k in self.share_policy:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.description is not None:
            result['description'] = self.description
        if self.expiration is not None:
            result['expiration'] = self.expiration
        if self.permissions is not None:
            result['permissions'] = self.permissions
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.share_name is not None:
            result['share_name'] = self.share_name
        result['share_policy'] = []
        if self.share_policy is not None:
            for k in self.share_policy:
                result['share_policy'].append(k.to_map() if k else None)
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, map={}):
        if map.get('description') is not None:
            self.description = map.get('description')
        if map.get('expiration') is not None:
            self.expiration = map.get('expiration')
        if map.get('permissions') is not None:
            self.permissions = map.get('permissions')
        if map.get('share_id') is not None:
            self.share_id = map.get('share_id')
        if map.get('share_name') is not None:
            self.share_name = map.get('share_name')
        self.share_policy = []
        if map.get('share_policy') is not None:
            for k in map.get('share_policy'):
                temp_model = SharePermissionPolicy()
                self.share_policy.append(temp_model.from_map(k))
        if map.get('status') is not None:
            self.status = map.get('status')
        return self


class VideoMediaMetadata(TeaModel):
    """
    *
    """
    def __init__(self, duration=None):
        # Duration
        self.duration = duration        # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.duration is not None:
            result['duration'] = self.duration
        return result

    def from_map(self, map={}):
        if map.get('duration') is not None:
            self.duration = map.get('duration')
        return self


class CreateUserModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: CreateUserResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = CreateUserResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class DeleteUserModel(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        return self


class GetUserModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: GetUserResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetUserResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class ListUsersModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: ListUserResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = ListUserResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class SearchUserModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: ListUserResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = ListUserResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class UpdateUserModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: UpdateUserResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = UpdateUserResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class BaseUserResponse(TeaModel):
    """
    Base user response
    """
    def __init__(self, avatar=None, created_at=None, default_drive_id=None, description=None, domain_id=None,
                 email=None, nick_name=None, phone=None, role=None, status=None, updated_at=None, user_data=None,
                 user_id=None, user_name=None):
        # 头像
        self.avatar = avatar            # type: str
        # 用户创建时间
        self.created_at = created_at    # type: int
        # 默认 Drive ID
        self.default_drive_id = default_drive_id  # type: str
        # 用户备注信息
        self.description = description  # type: str
        # Domain ID
        self.domain_id = domain_id      # type: str
        # 邮箱
        self.email = email              # type: str
        # 昵称
        self.nick_name = nick_name      # type: str
        # 电话
        self.phone = phone              # type: str
        # 角色
        self.role = role                # type: str
        # 用户状态
        self.status = status            # type: str
        # 用户修改时间
        self.updated_at = updated_at    # type: int
        # 用户自定义数据，格式为json，可用于配置项、少量临时数据等存储，不超过1K
        self.user_data = user_data      # type: dict
        # 用户 ID
        self.user_id = user_id          # type: str
        # 用户名称
        self.user_name = user_name      # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.avatar is not None:
            result['avatar'] = self.avatar
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.default_drive_id is not None:
            result['default_drive_id'] = self.default_drive_id
        if self.description is not None:
            result['description'] = self.description
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.email is not None:
            result['email'] = self.email
        if self.nick_name is not None:
            result['nick_name'] = self.nick_name
        if self.phone is not None:
            result['phone'] = self.phone
        if self.role is not None:
            result['role'] = self.role
        if self.status is not None:
            result['status'] = self.status
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        if self.user_data is not None:
            result['user_data'] = self.user_data
        if self.user_id is not None:
            result['user_id'] = self.user_id
        if self.user_name is not None:
            result['user_name'] = self.user_name
        return result

    def from_map(self, map={}):
        if map.get('avatar') is not None:
            self.avatar = map.get('avatar')
        if map.get('created_at') is not None:
            self.created_at = map.get('created_at')
        if map.get('default_drive_id') is not None:
            self.default_drive_id = map.get('default_drive_id')
        if map.get('description') is not None:
            self.description = map.get('description')
        if map.get('domain_id') is not None:
            self.domain_id = map.get('domain_id')
        if map.get('email') is not None:
            self.email = map.get('email')
        if map.get('nick_name') is not None:
            self.nick_name = map.get('nick_name')
        if map.get('phone') is not None:
            self.phone = map.get('phone')
        if map.get('role') is not None:
            self.role = map.get('role')
        if map.get('status') is not None:
            self.status = map.get('status')
        if map.get('updated_at') is not None:
            self.updated_at = map.get('updated_at')
        if map.get('user_data') is not None:
            self.user_data = map.get('user_data')
        if map.get('user_id') is not None:
            self.user_id = map.get('user_id')
        if map.get('user_name') is not None:
            self.user_name = map.get('user_name')
        return self


class CreateUserRequest(TeaModel):
    """
    Create user request
    """
    def __init__(self, headers=None, avatar=None, description=None, email=None, nick_name=None, phone=None, role=None,
                 status=None, user_data=None, user_id=None, user_name=None):
        self.headers = headers          # type: Dict[str, str]
        # 头像
        self.avatar = avatar            # type: str
        # 描述信息
        self.description = description  # type: str
        # 邮箱
        self.email = email              # type: str
        # 昵称
        self.nick_name = nick_name      # type: str
        # 电话号码
        self.phone = phone              # type: str
        # 角色
        self.role = role                # type: str
        # 状态
        self.status = status            # type: str
        # 用户自定义数据，格式为json，可用于配置项、少量临时数据等存储，不超过1K
        self.user_data = user_data      # type: dict
        # 用户 ID
        self.user_id = user_id          # type: str
        # 用户名称
        self.user_name = user_name      # type: str

    def validate(self):
        if self.description is not None:
            self.validate_max_length(self.description, 'description', 1024)
        self.validate_required(self.user_id, 'user_id')

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.avatar is not None:
            result['avatar'] = self.avatar
        if self.description is not None:
            result['description'] = self.description
        if self.email is not None:
            result['email'] = self.email
        if self.nick_name is not None:
            result['nick_name'] = self.nick_name
        if self.phone is not None:
            result['phone'] = self.phone
        if self.role is not None:
            result['role'] = self.role
        if self.status is not None:
            result['status'] = self.status
        if self.user_data is not None:
            result['user_data'] = self.user_data
        if self.user_id is not None:
            result['user_id'] = self.user_id
        if self.user_name is not None:
            result['user_name'] = self.user_name
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('avatar') is not None:
            self.avatar = map.get('avatar')
        if map.get('description') is not None:
            self.description = map.get('description')
        if map.get('email') is not None:
            self.email = map.get('email')
        if map.get('nick_name') is not None:
            self.nick_name = map.get('nick_name')
        if map.get('phone') is not None:
            self.phone = map.get('phone')
        if map.get('role') is not None:
            self.role = map.get('role')
        if map.get('status') is not None:
            self.status = map.get('status')
        if map.get('user_data') is not None:
            self.user_data = map.get('user_data')
        if map.get('user_id') is not None:
            self.user_id = map.get('user_id')
        if map.get('user_name') is not None:
            self.user_name = map.get('user_name')
        return self


class CreateUserResponse(TeaModel):
    """
    Create user response
    """
    def __init__(self, avatar=None, created_at=None, default_drive_id=None, description=None, domain_id=None,
                 email=None, nick_name=None, phone=None, role=None, status=None, updated_at=None, user_data=None,
                 user_id=None, user_name=None):
        # 头像
        self.avatar = avatar            # type: str
        # 用户创建时间
        self.created_at = created_at    # type: int
        # 默认 Drive ID
        self.default_drive_id = default_drive_id  # type: str
        # 用户备注信息
        self.description = description  # type: str
        # Domain ID
        self.domain_id = domain_id      # type: str
        # 邮箱
        self.email = email              # type: str
        # 昵称
        self.nick_name = nick_name      # type: str
        # 电话
        self.phone = phone              # type: str
        # 角色
        self.role = role                # type: str
        # 用户状态
        self.status = status            # type: str
        # 用户修改时间
        self.updated_at = updated_at    # type: int
        # 用户自定义数据，格式为json，可用于配置项、少量临时数据等存储，不超过1K
        self.user_data = user_data      # type: dict
        # 用户 ID
        self.user_id = user_id          # type: str
        # 用户名称
        self.user_name = user_name      # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.avatar is not None:
            result['avatar'] = self.avatar
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.default_drive_id is not None:
            result['default_drive_id'] = self.default_drive_id
        if self.description is not None:
            result['description'] = self.description
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.email is not None:
            result['email'] = self.email
        if self.nick_name is not None:
            result['nick_name'] = self.nick_name
        if self.phone is not None:
            result['phone'] = self.phone
        if self.role is not None:
            result['role'] = self.role
        if self.status is not None:
            result['status'] = self.status
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        if self.user_data is not None:
            result['user_data'] = self.user_data
        if self.user_id is not None:
            result['user_id'] = self.user_id
        if self.user_name is not None:
            result['user_name'] = self.user_name
        return result

    def from_map(self, map={}):
        if map.get('avatar') is not None:
            self.avatar = map.get('avatar')
        if map.get('created_at') is not None:
            self.created_at = map.get('created_at')
        if map.get('default_drive_id') is not None:
            self.default_drive_id = map.get('default_drive_id')
        if map.get('description') is not None:
            self.description = map.get('description')
        if map.get('domain_id') is not None:
            self.domain_id = map.get('domain_id')
        if map.get('email') is not None:
            self.email = map.get('email')
        if map.get('nick_name') is not None:
            self.nick_name = map.get('nick_name')
        if map.get('phone') is not None:
            self.phone = map.get('phone')
        if map.get('role') is not None:
            self.role = map.get('role')
        if map.get('status') is not None:
            self.status = map.get('status')
        if map.get('updated_at') is not None:
            self.updated_at = map.get('updated_at')
        if map.get('user_data') is not None:
            self.user_data = map.get('user_data')
        if map.get('user_id') is not None:
            self.user_id = map.get('user_id')
        if map.get('user_name') is not None:
            self.user_name = map.get('user_name')
        return self


class DeleteUserRequest(TeaModel):
    """
    Delete user request
    """
    def __init__(self, headers=None, user_id=None):
        self.headers = headers          # type: Dict[str, str]
        # 用户 ID
        self.user_id = user_id          # type: str

    def validate(self):
        self.validate_required(self.user_id, 'user_id')

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('user_id') is not None:
            self.user_id = map.get('user_id')
        return self


class DeleteUserResponse(TeaModel):
    """
    Delete user response
    """
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = {}
        return result

    def from_map(self, map={}):
        return self


class GetUserRequest(TeaModel):
    """
    Get user request
    """
    def __init__(self, headers=None, user_id=None):
        self.headers = headers          # type: Dict[str, str]
        # 用户 ID, 使用ak方式访问，该项必传, access_token访问如果不传，默认取自己的user信息
        # example
        self.user_id = user_id          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('user_id') is not None:
            self.user_id = map.get('user_id')
        return self


class GetUserResponse(TeaModel):
    """
    Get user response
    """
    def __init__(self, avatar=None, created_at=None, default_drive_id=None, description=None, domain_id=None,
                 email=None, nick_name=None, phone=None, role=None, status=None, updated_at=None, user_data=None,
                 user_id=None, user_name=None):
        # 头像
        self.avatar = avatar            # type: str
        # 用户创建时间
        self.created_at = created_at    # type: int
        # 默认 Drive ID
        self.default_drive_id = default_drive_id  # type: str
        # 用户备注信息
        self.description = description  # type: str
        # Domain ID
        self.domain_id = domain_id      # type: str
        # 邮箱
        self.email = email              # type: str
        # 昵称
        self.nick_name = nick_name      # type: str
        # 电话
        self.phone = phone              # type: str
        # 角色
        self.role = role                # type: str
        # 用户状态
        self.status = status            # type: str
        # 用户修改时间
        self.updated_at = updated_at    # type: int
        # 用户自定义数据，格式为json，可用于配置项、少量临时数据等存储，不超过1K
        self.user_data = user_data      # type: dict
        # 用户 ID
        self.user_id = user_id          # type: str
        # 用户名称
        self.user_name = user_name      # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.avatar is not None:
            result['avatar'] = self.avatar
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.default_drive_id is not None:
            result['default_drive_id'] = self.default_drive_id
        if self.description is not None:
            result['description'] = self.description
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.email is not None:
            result['email'] = self.email
        if self.nick_name is not None:
            result['nick_name'] = self.nick_name
        if self.phone is not None:
            result['phone'] = self.phone
        if self.role is not None:
            result['role'] = self.role
        if self.status is not None:
            result['status'] = self.status
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        if self.user_data is not None:
            result['user_data'] = self.user_data
        if self.user_id is not None:
            result['user_id'] = self.user_id
        if self.user_name is not None:
            result['user_name'] = self.user_name
        return result

    def from_map(self, map={}):
        if map.get('avatar') is not None:
            self.avatar = map.get('avatar')
        if map.get('created_at') is not None:
            self.created_at = map.get('created_at')
        if map.get('default_drive_id') is not None:
            self.default_drive_id = map.get('default_drive_id')
        if map.get('description') is not None:
            self.description = map.get('description')
        if map.get('domain_id') is not None:
            self.domain_id = map.get('domain_id')
        if map.get('email') is not None:
            self.email = map.get('email')
        if map.get('nick_name') is not None:
            self.nick_name = map.get('nick_name')
        if map.get('phone') is not None:
            self.phone = map.get('phone')
        if map.get('role') is not None:
            self.role = map.get('role')
        if map.get('status') is not None:
            self.status = map.get('status')
        if map.get('updated_at') is not None:
            self.updated_at = map.get('updated_at')
        if map.get('user_data') is not None:
            self.user_data = map.get('user_data')
        if map.get('user_id') is not None:
            self.user_id = map.get('user_id')
        if map.get('user_name') is not None:
            self.user_name = map.get('user_name')
        return self


class ListUserRequest(TeaModel):
    """
    List user request
    """
    def __init__(self, headers=None, limit=None, marker=None):
        self.headers = headers          # type: Dict[str, str]
        # 每页大小限制
        self.limit = limit              # type: int
        # 翻页标记
        self.marker = marker            # type: str

    def validate(self):
        if self.limit is not None:
            self.validate_maximum(self.limit, 'limit', 100)
            self.validate_minimum(self.limit, 'limit', 1)

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('limit') is not None:
            self.limit = map.get('limit')
        if map.get('marker') is not None:
            self.marker = map.get('marker')
        return self


class ListUserResponse(TeaModel):
    """
    List user response
    """
    def __init__(self, items=None, next_marker=None):
        self.items = items              # type: List[BaseUserResponse]
        # 翻页标记
        self.next_marker = next_marker  # type: str

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, map={}):
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = BaseUserResponse()
                self.items.append(temp_model.from_map(k))
        if map.get('next_marker') is not None:
            self.next_marker = map.get('next_marker')
        return self


class SearchUserRequest(TeaModel):
    """
    Search user request
    """
    def __init__(self, headers=None, email=None, limit=None, marker=None, nick_name=None, phone=None, role=None,
                 status=None, user_name=None):
        self.headers = headers          # type: Dict[str, str]
        # 邮箱
        self.email = email              # type: str
        # 每页大小限制
        self.limit = limit              # type: int
        # 翻页标记
        self.marker = marker            # type: str
        # 昵称
        self.nick_name = nick_name      # type: str
        # 电话号码
        self.phone = phone              # type: str
        # 角色
        self.role = role                # type: str
        # 状态
        self.status = status            # type: str
        # 用户名
        self.user_name = user_name      # type: str

    def validate(self):
        if self.limit is not None:
            self.validate_maximum(self.limit, 'limit', 100)
            self.validate_minimum(self.limit, 'limit', 1)

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.email is not None:
            result['email'] = self.email
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        if self.nick_name is not None:
            result['nick_name'] = self.nick_name
        if self.phone is not None:
            result['phone'] = self.phone
        if self.role is not None:
            result['role'] = self.role
        if self.status is not None:
            result['status'] = self.status
        if self.user_name is not None:
            result['user_name'] = self.user_name
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('email') is not None:
            self.email = map.get('email')
        if map.get('limit') is not None:
            self.limit = map.get('limit')
        if map.get('marker') is not None:
            self.marker = map.get('marker')
        if map.get('nick_name') is not None:
            self.nick_name = map.get('nick_name')
        if map.get('phone') is not None:
            self.phone = map.get('phone')
        if map.get('role') is not None:
            self.role = map.get('role')
        if map.get('status') is not None:
            self.status = map.get('status')
        if map.get('user_name') is not None:
            self.user_name = map.get('user_name')
        return self


class UpdateUserRequest(TeaModel):
    """
    Update user request
    """
    def __init__(self, headers=None, avatar=None, description=None, email=None, nick_name=None, phone=None, role=None,
                 status=None, user_data=None, user_id=None):
        self.headers = headers          # type: Dict[str, str]
        # 头像
        self.avatar = avatar            # type: str
        # 描述信息
        self.description = description  # type: str
        # 邮箱
        self.email = email              # type: str
        # 昵称
        self.nick_name = nick_name      # type: str
        # 电话号码
        self.phone = phone              # type: str
        # 角色
        self.role = role                # type: str
        # 状态
        self.status = status            # type: str
        # 用户自定义数据，格式为json，可用于配置项、少量临时数据等存储，不超过1K
        self.user_data = user_data      # type: dict
        # 用户 ID
        self.user_id = user_id          # type: str

    def validate(self):
        if self.description is not None:
            self.validate_max_length(self.description, 'description', 1024)
        self.validate_required(self.user_id, 'user_id')

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.avatar is not None:
            result['avatar'] = self.avatar
        if self.description is not None:
            result['description'] = self.description
        if self.email is not None:
            result['email'] = self.email
        if self.nick_name is not None:
            result['nick_name'] = self.nick_name
        if self.phone is not None:
            result['phone'] = self.phone
        if self.role is not None:
            result['role'] = self.role
        if self.status is not None:
            result['status'] = self.status
        if self.user_data is not None:
            result['user_data'] = self.user_data
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('avatar') is not None:
            self.avatar = map.get('avatar')
        if map.get('description') is not None:
            self.description = map.get('description')
        if map.get('email') is not None:
            self.email = map.get('email')
        if map.get('nick_name') is not None:
            self.nick_name = map.get('nick_name')
        if map.get('phone') is not None:
            self.phone = map.get('phone')
        if map.get('role') is not None:
            self.role = map.get('role')
        if map.get('status') is not None:
            self.status = map.get('status')
        if map.get('user_data') is not None:
            self.user_data = map.get('user_data')
        if map.get('user_id') is not None:
            self.user_id = map.get('user_id')
        return self


class UpdateUserResponse(TeaModel):
    """
    Update user response
    """
    def __init__(self, avatar=None, created_at=None, default_drive_id=None, description=None, domain_id=None,
                 email=None, nick_name=None, phone=None, role=None, status=None, updated_at=None, user_data=None,
                 user_id=None, user_name=None):
        # 头像
        self.avatar = avatar            # type: str
        # 用户创建时间
        self.created_at = created_at    # type: int
        # 默认 Drive ID
        self.default_drive_id = default_drive_id  # type: str
        # 用户备注信息
        self.description = description  # type: str
        # Domain ID
        self.domain_id = domain_id      # type: str
        # 邮箱
        self.email = email              # type: str
        # 昵称
        self.nick_name = nick_name      # type: str
        # 电话
        self.phone = phone              # type: str
        # 角色
        self.role = role                # type: str
        # 用户状态
        self.status = status            # type: str
        # 用户修改时间
        self.updated_at = updated_at    # type: int
        # 用户自定义数据，格式为json，可用于配置项、少量临时数据等存储，不超过1K
        self.user_data = user_data      # type: dict
        # 用户 ID
        self.user_id = user_id          # type: str
        # 用户名称
        self.user_name = user_name      # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.avatar is not None:
            result['avatar'] = self.avatar
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.default_drive_id is not None:
            result['default_drive_id'] = self.default_drive_id
        if self.description is not None:
            result['description'] = self.description
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.email is not None:
            result['email'] = self.email
        if self.nick_name is not None:
            result['nick_name'] = self.nick_name
        if self.phone is not None:
            result['phone'] = self.phone
        if self.role is not None:
            result['role'] = self.role
        if self.status is not None:
            result['status'] = self.status
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        if self.user_data is not None:
            result['user_data'] = self.user_data
        if self.user_id is not None:
            result['user_id'] = self.user_id
        if self.user_name is not None:
            result['user_name'] = self.user_name
        return result

    def from_map(self, map={}):
        if map.get('avatar') is not None:
            self.avatar = map.get('avatar')
        if map.get('created_at') is not None:
            self.created_at = map.get('created_at')
        if map.get('default_drive_id') is not None:
            self.default_drive_id = map.get('default_drive_id')
        if map.get('description') is not None:
            self.description = map.get('description')
        if map.get('domain_id') is not None:
            self.domain_id = map.get('domain_id')
        if map.get('email') is not None:
            self.email = map.get('email')
        if map.get('nick_name') is not None:
            self.nick_name = map.get('nick_name')
        if map.get('phone') is not None:
            self.phone = map.get('phone')
        if map.get('role') is not None:
            self.role = map.get('role')
        if map.get('status') is not None:
            self.status = map.get('status')
        if map.get('updated_at') is not None:
            self.updated_at = map.get('updated_at')
        if map.get('user_data') is not None:
            self.user_data = map.get('user_data')
        if map.get('user_id') is not None:
            self.user_id = map.get('user_id')
        if map.get('user_name') is not None:
            self.user_name = map.get('user_name')
        return self


class CreateStoryModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: CreateStoryResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = CreateStoryResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class GetPhotoCountModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: GetImageCountResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetImageCountResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class GetStoryDetailModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: GetStoryDetailResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetStoryDetailResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class GetStoryTaskModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: GetStoryTaskResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetStoryTaskResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class ListAddressGroupsModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: ListImageAddressGroupsResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = ListImageAddressGroupsResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class ListFaceGroupsModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: ListImageFaceGroupsResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = ListImageFaceGroupsResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class ListStoryModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: ListStoryResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = ListStoryResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class ListTagsModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: ListImageTagsResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = ListImageTagsResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class SearchAddressGroupsModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: SearchImageAddressGroupsResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = SearchImageAddressGroupsResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class UpdateFacegroupInfoModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: UpdateFaceGroupInfoResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = UpdateFaceGroupInfoResponse()
            self.body = temp_model.from_map(map['body'])
        return self


class Address(TeaModel):
    """
    *
    """
    def __init__(self, city=None, country=None, district=None, province=None, township=None):
        self.city = city                # type: str
        self.country = country          # type: str
        self.district = district        # type: str
        self.province = province        # type: str
        self.township = township        # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.city is not None:
            result['city'] = self.city
        if self.country is not None:
            result['country'] = self.country
        if self.district is not None:
            result['district'] = self.district
        if self.province is not None:
            result['province'] = self.province
        if self.township is not None:
            result['township'] = self.township
        return result

    def from_map(self, map={}):
        if map.get('city') is not None:
            self.city = map.get('city')
        if map.get('country') is not None:
            self.country = map.get('country')
        if map.get('district') is not None:
            self.district = map.get('district')
        if map.get('province') is not None:
            self.province = map.get('province')
        if map.get('township') is not None:
            self.township = map.get('township')
        return self


class CreateStoryRequest(TeaModel):
    """
    Create story request
    """
    def __init__(self, headers=None, drive_id=None):
        self.headers = headers          # type: Dict[str, str]
        # drive_id
        self.drive_id = drive_id        # type: str

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        return self


class CreateStoryResponse(TeaModel):
    """
    生成故事
    """
    def __init__(self, drive_id=None):
        self.drive_id = drive_id        # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        return result

    def from_map(self, map={}):
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        return self


class GetImageCountRequest(TeaModel):
    """
    Get photo count request
    """
    def __init__(self, headers=None, drive_id=None):
        self.headers = headers          # type: Dict[str, str]
        # drive_id
        self.drive_id = drive_id        # type: str

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        return self


class GetImageCountResponse(TeaModel):
    """
    获取云照片个数结果
    """
    def __init__(self, image_count=None):
        # image_count
        self.image_count = image_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.image_count is not None:
            result['image_count'] = self.image_count
        return result

    def from_map(self, map={}):
        if map.get('image_count') is not None:
            self.image_count = map.get('image_count')
        return self


class GetStoryDetailRequest(TeaModel):
    """
    Get story detail request
    """
    def __init__(self, headers=None, drive_id=None, story_id=None, video_url_expire_sec=None):
        self.headers = headers          # type: Dict[str, str]
        # drive_id
        self.drive_id = drive_id        # type: str
        # story_id
        self.story_id = story_id        # type: str
        # url_expire_sec
        self.video_url_expire_sec = video_url_expire_sec  # type: int

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.story_id, 'story_id')
        if self.video_url_expire_sec is not None:
            self.validate_maximum(self.video_url_expire_sec, 'video_url_expire_sec', 14400)
            self.validate_minimum(self.video_url_expire_sec, 'video_url_expire_sec', 10)

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.story_id is not None:
            result['story_id'] = self.story_id
        if self.video_url_expire_sec is not None:
            result['video_url_expire_sec'] = self.video_url_expire_sec
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('story_id') is not None:
            self.story_id = map.get('story_id')
        if map.get('video_url_expire_sec') is not None:
            self.video_url_expire_sec = map.get('video_url_expire_sec')
        return self


class GetStoryDetailResponse(TeaModel):
    """
    故事详情
    """
    def __init__(self, cover_file_id=None, created_at=None, items=None, score=None, story_id=None,
                 story_images_date_range=None, sub_title=None, title=None, updated_at=None, video_status=None, video_url=None):
        # cover_file_id
        self.cover_file_id = cover_file_id  # type: str
        # created_at
        self.created_at = created_at    # type: str
        # items
        self.items = items              # type: List[BaseFileResponse]
        # score
        self.score = score              # type: float
        # story_id
        self.story_id = story_id        # type: str
        # story_images_date_range
        self.story_images_date_range = story_images_date_range  # type: List[int]
        # sub_title
        self.sub_title = sub_title      # type: str
        # title
        self.title = title              # type: str
        # updated_at
        self.updated_at = updated_at    # type: str
        # video_status
        self.video_status = video_status  # type: str
        # video_url
        self.video_url = video_url      # type: str

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.cover_file_id is not None:
            result['cover_file_id'] = self.cover_file_id
        if self.created_at is not None:
            result['created_at'] = self.created_at
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.score is not None:
            result['score'] = self.score
        if self.story_id is not None:
            result['story_id'] = self.story_id
        if self.story_images_date_range is not None:
            result['story_images_date_range'] = self.story_images_date_range
        if self.sub_title is not None:
            result['sub_title'] = self.sub_title
        if self.title is not None:
            result['title'] = self.title
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        if self.video_status is not None:
            result['video_status'] = self.video_status
        if self.video_url is not None:
            result['video_url'] = self.video_url
        return result

    def from_map(self, map={}):
        if map.get('cover_file_id') is not None:
            self.cover_file_id = map.get('cover_file_id')
        if map.get('created_at') is not None:
            self.created_at = map.get('created_at')
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = BaseFileResponse()
                self.items.append(temp_model.from_map(k))
        if map.get('score') is not None:
            self.score = map.get('score')
        if map.get('story_id') is not None:
            self.story_id = map.get('story_id')
        if map.get('story_images_date_range') is not None:
            self.story_images_date_range = map.get('story_images_date_range')
        if map.get('sub_title') is not None:
            self.sub_title = map.get('sub_title')
        if map.get('title') is not None:
            self.title = map.get('title')
        if map.get('updated_at') is not None:
            self.updated_at = map.get('updated_at')
        if map.get('video_status') is not None:
            self.video_status = map.get('video_status')
        if map.get('video_url') is not None:
            self.video_url = map.get('video_url')
        return self


class GetStoryTaskRequest(TeaModel):
    """
    Get create story task request
    """
    def __init__(self, headers=None, drive_id=None):
        self.headers = headers          # type: Dict[str, str]
        # Drive ID
        self.drive_id = drive_id        # type: str

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        return self


class GetStoryTaskResponse(TeaModel):
    """
    故事任务状态
    """
    def __init__(self, drive_id=None, status=None):
        self.drive_id = drive_id        # type: str
        self.status = status            # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, map={}):
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('status') is not None:
            self.status = map.get('status')
        return self


class ImageAddressResponse(TeaModel):
    """
    *
    """
    def __init__(self, address_detail=None, count=None, cover_file_id=None, cover_url=None, location=None, name=None):
        self.address_detail = address_detail  # type: Address
        # 聚类地点计数
        self.count = count              # type: int
        # cover_file_id
        self.cover_file_id = cover_file_id  # type: str
        # 聚类地点封面图片地址
        self.cover_url = cover_url      # type: str
        # 经纬度
        self.location = location        # type: str
        # 聚类地点名称
        self.name = name                # type: str

    def validate(self):
        if self.address_detail:
            self.address_detail.validate()

    def to_map(self):
        result = {}
        if self.address_detail is not None:
            result['address_detail'] = self.address_detail.to_map()
        if self.count is not None:
            result['count'] = self.count
        if self.cover_file_id is not None:
            result['cover_file_id'] = self.cover_file_id
        if self.cover_url is not None:
            result['cover_url'] = self.cover_url
        if self.location is not None:
            result['location'] = self.location
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, map={}):
        if map.get('address_detail') is not None:
            temp_model = Address()
            self.address_detail = temp_model.from_map(map['address_detail'])
        if map.get('count') is not None:
            self.count = map.get('count')
        if map.get('cover_file_id') is not None:
            self.cover_file_id = map.get('cover_file_id')
        if map.get('cover_url') is not None:
            self.cover_url = map.get('cover_url')
        if map.get('location') is not None:
            self.location = map.get('location')
        if map.get('name') is not None:
            self.name = map.get('name')
        return self


class ImageFaceGroupResponse(TeaModel):
    """
    *
    """
    def __init__(self, cover_file_id=None, created_at=None, face_count=None, group_cover_url=None, group_id=None,
                 group_name=None, image_count=None, updated_at=None):
        # cover_file_id
        self.cover_file_id = cover_file_id  # type: str
        # 人脸分组生成时间
        self.created_at = created_at    # type: str
        # 人脸个数
        self.face_count = face_count    # type: int
        # 人脸分组封面头像地址
        self.group_cover_url = group_cover_url  # type: str
        # 人脸分组 ID
        self.group_id = group_id        # type: str
        # 人脸分组名称
        self.group_name = group_name    # type: str
        # 照片个数
        self.image_count = image_count  # type: int
        # 人脸分组修改时间
        self.updated_at = updated_at    # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.cover_file_id is not None:
            result['cover_file_id'] = self.cover_file_id
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.face_count is not None:
            result['face_count'] = self.face_count
        if self.group_cover_url is not None:
            result['group_cover_url'] = self.group_cover_url
        if self.group_id is not None:
            result['group_id'] = self.group_id
        if self.group_name is not None:
            result['group_name'] = self.group_name
        if self.image_count is not None:
            result['image_count'] = self.image_count
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        return result

    def from_map(self, map={}):
        if map.get('cover_file_id') is not None:
            self.cover_file_id = map.get('cover_file_id')
        if map.get('created_at') is not None:
            self.created_at = map.get('created_at')
        if map.get('face_count') is not None:
            self.face_count = map.get('face_count')
        if map.get('group_cover_url') is not None:
            self.group_cover_url = map.get('group_cover_url')
        if map.get('group_id') is not None:
            self.group_id = map.get('group_id')
        if map.get('group_name') is not None:
            self.group_name = map.get('group_name')
        if map.get('image_count') is not None:
            self.image_count = map.get('image_count')
        if map.get('updated_at') is not None:
            self.updated_at = map.get('updated_at')
        return self


class ImageTagResponse(TeaModel):
    """
    *
    """
    def __init__(self, count=None, cover_file_id=None, cover_url=None, name=None):
        # 聚类标签计数
        self.count = count              # type: int
        # cover_file_id
        self.cover_file_id = cover_file_id  # type: str
        # 聚类标签封面图片地址
        self.cover_url = cover_url      # type: str
        # 聚类标签名称
        self.name = name                # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.count is not None:
            result['count'] = self.count
        if self.cover_file_id is not None:
            result['cover_file_id'] = self.cover_file_id
        if self.cover_url is not None:
            result['cover_url'] = self.cover_url
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, map={}):
        if map.get('count') is not None:
            self.count = map.get('count')
        if map.get('cover_file_id') is not None:
            self.cover_file_id = map.get('cover_file_id')
        if map.get('cover_url') is not None:
            self.cover_url = map.get('cover_url')
        if map.get('name') is not None:
            self.name = map.get('name')
        return self


class ListImageAddressGroupsRequest(TeaModel):
    """
    List image address groups request
    """
    def __init__(self, headers=None, drive_id=None, image_thumbnail_process=None, limit=None, marker=None):
        self.headers = headers          # type: Dict[str, str]
        # Drive ID
        self.drive_id = drive_id        # type: str
        # image_thumbnail_process
        # type:string
        self.image_thumbnail_process = image_thumbnail_process  # type: str
        # 每页大小限制
        self.limit = limit              # type: int
        # 翻页标记
        self.marker = marker            # type: str

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.limit is not None:
            self.validate_maximum(self.limit, 'limit', 100)
            self.validate_minimum(self.limit, 'limit', 1)

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.image_thumbnail_process is not None:
            result['image_thumbnail_process'] = self.image_thumbnail_process
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('image_thumbnail_process') is not None:
            self.image_thumbnail_process = map.get('image_thumbnail_process')
        if map.get('limit') is not None:
            self.limit = map.get('limit')
        if map.get('marker') is not None:
            self.marker = map.get('marker')
        return self


class ListImageAddressGroupsResponse(TeaModel):
    """
    展示地点分组集合
    """
    def __init__(self, items=None, next_marker=None):
        self.items = items              # type: List[ImageAddressResponse]
        self.next_marker = next_marker  # type: str

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, map={}):
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = ImageAddressResponse()
                self.items.append(temp_model.from_map(k))
        if map.get('next_marker') is not None:
            self.next_marker = map.get('next_marker')
        return self


class ListImageFaceGroupsRequest(TeaModel):
    """
    List image face groups request
    """
    def __init__(self, headers=None, drive_id=None, limit=None, marker=None):
        self.headers = headers          # type: Dict[str, str]
        # Drive ID
        self.drive_id = drive_id        # type: str
        # 每页大小限制
        self.limit = limit              # type: int
        # 翻页标记
        self.marker = marker            # type: str

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.limit is not None:
            self.validate_maximum(self.limit, 'limit', 100)
            self.validate_minimum(self.limit, 'limit', 1)

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('limit') is not None:
            self.limit = map.get('limit')
        if map.get('marker') is not None:
            self.marker = map.get('marker')
        return self


class ListImageFaceGroupsResponse(TeaModel):
    """
    展示人脸分组集合
    """
    def __init__(self, items=None, next_marker=None):
        self.items = items              # type: List[ImageFaceGroupResponse]
        self.next_marker = next_marker  # type: str

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, map={}):
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = ImageFaceGroupResponse()
                self.items.append(temp_model.from_map(k))
        if map.get('next_marker') is not None:
            self.next_marker = map.get('next_marker')
        return self


class ListImageTagsRequest(TeaModel):
    """
    List image tags request
    """
    def __init__(self, headers=None, drive_id=None, image_thumbnail_process=None):
        self.headers = headers          # type: Dict[str, str]
        # Drive ID
        self.drive_id = drive_id        # type: str
        # image_thumbnail_process
        # type:string
        self.image_thumbnail_process = image_thumbnail_process  # type: str

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.image_thumbnail_process is not None:
            result['image_thumbnail_process'] = self.image_thumbnail_process
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('image_thumbnail_process') is not None:
            self.image_thumbnail_process = map.get('image_thumbnail_process')
        return self


class ListImageTagsResponse(TeaModel):
    """
    展示标签集合
    """
    def __init__(self, tags=None):
        self.tags = tags                # type: List[ImageTagResponse]

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        self.tags = []
        if map.get('tags') is not None:
            for k in map.get('tags'):
                temp_model = ImageTagResponse()
                self.tags.append(temp_model.from_map(k))
        return self


class ListStoryRequest(TeaModel):
    """
    List story request
    """
    def __init__(self, headers=None, drive_id=None, limit=None, marker=None):
        self.headers = headers          # type: Dict[str, str]
        # drive_id
        self.drive_id = drive_id        # type: str
        # 每页大小限制
        self.limit = limit              # type: int
        # 翻页标记
        self.marker = marker            # type: str

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.limit is not None:
            self.validate_maximum(self.limit, 'limit', 100)
            self.validate_minimum(self.limit, 'limit', 1)

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('limit') is not None:
            self.limit = map.get('limit')
        if map.get('marker') is not None:
            self.marker = map.get('marker')
        return self


class ListStoryResponse(TeaModel):
    """
    故事列表
    """
    def __init__(self, items=None, next_marker=None):
        # items
        self.items = items              # type: List[StoryResponse]
        # next_marker
        self.next_marker = next_marker  # type: str

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, map={}):
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = StoryResponse()
                self.items.append(temp_model.from_map(k))
        if map.get('next_marker') is not None:
            self.next_marker = map.get('next_marker')
        return self


class RemoveStoryImagesRequest(TeaModel):
    """
    Remove story images request
    """
    def __init__(self, drive_id=None, file_ids=None, story_id=None):
        self.drive_id = drive_id        # type: str
        self.file_ids = file_ids        # type: List[str]
        self.story_id = story_id        # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_ids is not None:
            result['file_ids'] = self.file_ids
        if self.story_id is not None:
            result['story_id'] = self.story_id
        return result

    def from_map(self, map={}):
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('file_ids') is not None:
            self.file_ids = map.get('file_ids')
        if map.get('story_id') is not None:
            self.story_id = map.get('story_id')
        return self


class SearchImageAddressGroupsRequest(TeaModel):
    """
    Search image address groups request
    """
    def __init__(self, headers=None, address_level=None, address_names=None, br_geo_point=None, drive_id=None,
                 image_thumbnail_process=None, tl_geo_point=None):
        self.headers = headers          # type: Dict[str, str]
        # 查询的地点级别
        self.address_level = address_level  # type: str
        # 查询的地点数组
        self.address_names = address_names  # type: List[str]
        # br_geo_point
        self.br_geo_point = br_geo_point  # type: str
        # Drive ID
        self.drive_id = drive_id        # type: str
        # image_thumbnail_process
        # type:string
        self.image_thumbnail_process = image_thumbnail_process  # type: str
        # tl_geo_point
        self.tl_geo_point = tl_geo_point  # type: str

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.address_level is not None:
            result['address_level'] = self.address_level
        if self.address_names is not None:
            result['address_names'] = self.address_names
        if self.br_geo_point is not None:
            result['br_geo_point'] = self.br_geo_point
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.image_thumbnail_process is not None:
            result['image_thumbnail_process'] = self.image_thumbnail_process
        if self.tl_geo_point is not None:
            result['tl_geo_point'] = self.tl_geo_point
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('address_level') is not None:
            self.address_level = map.get('address_level')
        if map.get('address_names') is not None:
            self.address_names = map.get('address_names')
        if map.get('br_geo_point') is not None:
            self.br_geo_point = map.get('br_geo_point')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('image_thumbnail_process') is not None:
            self.image_thumbnail_process = map.get('image_thumbnail_process')
        if map.get('tl_geo_point') is not None:
            self.tl_geo_point = map.get('tl_geo_point')
        return self


class SearchImageAddressGroupsResponse(TeaModel):
    """
    展示地点分组列表
    """
    def __init__(self, items=None):
        self.items = items              # type: List[ImageAddressResponse]

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = ImageAddressResponse()
                self.items.append(temp_model.from_map(k))
        return self


class StoryResponse(TeaModel):
    """
    *
    """
    def __init__(self, cover_file_id=None, created_at=None, score=None, story_id=None, story_images_date_range=None,
                 sub_title=None, title=None, updated_at=None, video_status=None, video_url=None):
        # cover_file_id
        self.cover_file_id = cover_file_id  # type: str
        # created_at
        self.created_at = created_at    # type: str
        # score
        self.score = score              # type: float
        # story_id
        self.story_id = story_id        # type: str
        # story_images_date_range
        self.story_images_date_range = story_images_date_range  # type: List[int]
        # sub_title
        self.sub_title = sub_title      # type: str
        # title
        self.title = title              # type: str
        # updated_at
        self.updated_at = updated_at    # type: str
        # video_status
        self.video_status = video_status  # type: str
        # video_url
        self.video_url = video_url      # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.cover_file_id is not None:
            result['cover_file_id'] = self.cover_file_id
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.score is not None:
            result['score'] = self.score
        if self.story_id is not None:
            result['story_id'] = self.story_id
        if self.story_images_date_range is not None:
            result['story_images_date_range'] = self.story_images_date_range
        if self.sub_title is not None:
            result['sub_title'] = self.sub_title
        if self.title is not None:
            result['title'] = self.title
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        if self.video_status is not None:
            result['video_status'] = self.video_status
        if self.video_url is not None:
            result['video_url'] = self.video_url
        return result

    def from_map(self, map={}):
        if map.get('cover_file_id') is not None:
            self.cover_file_id = map.get('cover_file_id')
        if map.get('created_at') is not None:
            self.created_at = map.get('created_at')
        if map.get('score') is not None:
            self.score = map.get('score')
        if map.get('story_id') is not None:
            self.story_id = map.get('story_id')
        if map.get('story_images_date_range') is not None:
            self.story_images_date_range = map.get('story_images_date_range')
        if map.get('sub_title') is not None:
            self.sub_title = map.get('sub_title')
        if map.get('title') is not None:
            self.title = map.get('title')
        if map.get('updated_at') is not None:
            self.updated_at = map.get('updated_at')
        if map.get('video_status') is not None:
            self.video_status = map.get('video_status')
        if map.get('video_url') is not None:
            self.video_url = map.get('video_url')
        return self


class UpdateFaceGroupInfoRequest(TeaModel):
    """
    Update face group info request
    """
    def __init__(self, headers=None, drive_id=None, group_id=None, group_name=None):
        self.headers = headers          # type: Dict[str, str]
        # drive_id
        self.drive_id = drive_id        # type: str
        # group_id 列举人脸分组接口中获取
        self.group_id = group_id        # type: str
        # group_name
        self.group_name = group_name    # type: str

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.group_id, 'group_id')

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.group_id is not None:
            result['group_id'] = self.group_id
        if self.group_name is not None:
            result['group_name'] = self.group_name
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('group_id') is not None:
            self.group_id = map.get('group_id')
        if map.get('group_name') is not None:
            self.group_name = map.get('group_name')
        return self


class UpdateFaceGroupInfoResponse(TeaModel):
    """
    更新人脸分组信息结果
    """
    def __init__(self, drive_id=None, group_id=None):
        # drive_id
        self.drive_id = drive_id        # type: str
        # group_id
        self.group_id = group_id        # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.group_id is not None:
            result['group_id'] = self.group_id
        return result

    def from_map(self, map={}):
        if map.get('drive_id') is not None:
            self.drive_id = map.get('drive_id')
        if map.get('group_id') is not None:
            self.group_id = map.get('group_id')
        return self
