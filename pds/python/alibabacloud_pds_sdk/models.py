# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class RuntimeOptions(TeaModel):
    def __init__(self, autoretry=None, ignore_ssl=None, max_attempts=None, backoff_policy=None, backoff_period=None,
                 read_timeout=None, connect_timeout=None, http_proxy=None, https_proxy=None, no_proxy=None, max_idle_conns=None,
                 local_addr=None, socks_5proxy=None, socks_5net_work=None):
        # whether to try again
        self.autoretry = autoretry  # type: bool
        # ignore SSL validation
        self.ignore_ssl = ignore_ssl  # type: bool
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
        self.http_proxy = http_proxy  # type: str
        # https Proxy url
        self.https_proxy = https_proxy  # type: str
        # agent blacklist
        self.no_proxy = no_proxy  # type: str
        # maximum number of connections
        self.max_idle_conns = max_idle_conns  # type: int
        # local addr
        self.local_addr = local_addr  # type: str
        # SOCKS5 proxy
        self.socks_5proxy = socks_5proxy  # type: str
        # SOCKS5 netWork
        self.socks_5net_work = socks_5net_work  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['autoretry'] = self.autoretry
        result['ignoreSSL'] = self.ignore_ssl
        result['maxAttempts'] = self.max_attempts
        result['backoffPolicy'] = self.backoff_policy
        result['backoffPeriod'] = self.backoff_period
        result['readTimeout'] = self.read_timeout
        result['connectTimeout'] = self.connect_timeout
        result['httpProxy'] = self.http_proxy
        result['httpsProxy'] = self.https_proxy
        result['noProxy'] = self.no_proxy
        result['maxIdleConns'] = self.max_idle_conns
        result['localAddr'] = self.local_addr
        result['socks5Proxy'] = self.socks_5proxy
        result['socks5NetWork'] = self.socks_5net_work
        return result

    def from_map(self, map={}):
        self.autoretry = map.get('autoretry')
        self.ignore_ssl = map.get('ignoreSSL')
        self.max_attempts = map.get('maxAttempts')
        self.backoff_policy = map.get('backoffPolicy')
        self.backoff_period = map.get('backoffPeriod')
        self.read_timeout = map.get('readTimeout')
        self.connect_timeout = map.get('connectTimeout')
        self.http_proxy = map.get('httpProxy')
        self.https_proxy = map.get('httpsProxy')
        self.no_proxy = map.get('noProxy')
        self.max_idle_conns = map.get('maxIdleConns')
        self.local_addr = map.get('localAddr')
        self.socks_5proxy = map.get('socks5Proxy')
        self.socks_5net_work = map.get('socks5NetWork')
        return self


class Config(TeaModel):
    def __init__(self, endpoint=None, domain_id=None, client_id=None, refresh_token=None, client_secret=None,
                 access_token=None, expire_time=None, protocol=None, type=None, security_token=None, access_key_id=None,
                 access_key_secret=None, nickname=None, user_agent=None):
        self.endpoint = endpoint  # type: str
        self.domain_id = domain_id  # type: str
        self.client_id = client_id  # type: str
        self.refresh_token = refresh_token  # type: str
        self.client_secret = client_secret  # type: str
        self.access_token = access_token  # type: str
        self.expire_time = expire_time  # type: str
        self.protocol = protocol  # type: str
        self.type = type  # type: str
        self.security_token = security_token  # type: str
        self.access_key_id = access_key_id  # type: str
        self.access_key_secret = access_key_secret  # type: str
        self.nickname = nickname  # type: str
        self.user_agent = user_agent  # type: str

    def validate(self):
        if self.domain_id:
            self.validate_pattern(self.domain_id, 'domain_id', '^[a-zA-Z0-9_-]+$')

    def to_map(self):
        result = {}
        result['endpoint'] = self.endpoint
        result['domainId'] = self.domain_id
        result['clientId'] = self.client_id
        result['refreshToken'] = self.refresh_token
        result['clientSecret'] = self.client_secret
        result['accessToken'] = self.access_token
        result['expireTime'] = self.expire_time
        result['protocol'] = self.protocol
        result['type'] = self.type
        result['securityToken'] = self.security_token
        result['accessKeyId'] = self.access_key_id
        result['accessKeySecret'] = self.access_key_secret
        result['nickname'] = self.nickname
        result['userAgent'] = self.user_agent
        return result

    def from_map(self, map={}):
        self.endpoint = map.get('endpoint')
        self.domain_id = map.get('domainId')
        self.client_id = map.get('clientId')
        self.refresh_token = map.get('refreshToken')
        self.client_secret = map.get('clientSecret')
        self.access_token = map.get('accessToken')
        self.expire_time = map.get('expireTime')
        self.protocol = map.get('protocol')
        self.type = map.get('type')
        self.security_token = map.get('securityToken')
        self.access_key_id = map.get('accessKeyId')
        self.access_key_secret = map.get('accessKeySecret')
        self.nickname = map.get('nickname')
        self.user_agent = map.get('userAgent')
        return self


class CancelLinkModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: AccountAccessTokenResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = AccountAccessTokenResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class ConfirmLinkModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: AccountAccessTokenResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = AccountAccessTokenResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class ChangePasswordModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: AccountAccessTokenResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = AccountAccessTokenResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class SetPasswordModel(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class VerifyCodeModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: VerifyCodeResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = VerifyCodeResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class GetAccessTokenByLinkInfoModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: AccountAccessTokenResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = AccountAccessTokenResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class GetCaptchaModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: Captcha

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = Captcha()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class GetLinkInfoModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: LinkInfoResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = LinkInfoResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class GetLinkInfoByUserIdModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: LinkInfoListResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = LinkInfoListResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class GetPublicKeyModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: GetAppPublicKeyResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetAppPublicKeyResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class LinkModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: AccountAccessTokenResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = AccountAccessTokenResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class CheckExistModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: MobileCheckExistResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = MobileCheckExistResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class LoginModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: AccountAccessTokenResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = AccountAccessTokenResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class RegisterModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: AccountAccessTokenResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = AccountAccessTokenResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class MobileSendSmsCodeModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: MobileSendSmsCodeResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = MobileSendSmsCodeResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class AccountRevokeModel(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class AccountTokenModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: AccountAccessTokenResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = AccountAccessTokenResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
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
        self.expires_in = expires_in  # type: int
        # 用于刷新accessToken
        self.refresh_token = refresh_token  # type: str
        # 当前用户角色
        self.role = role  # type: str
        # accessToken类型，Bearer
        self.token_type = token_type  # type: str
        # 当前用户ID
        self.user_id = user_id  # type: str

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
        result['access_token'] = self.access_token
        result['default_drive_id'] = self.default_drive_id
        result['expire_time'] = self.expire_time
        result['expires_in'] = self.expires_in
        result['refresh_token'] = self.refresh_token
        result['role'] = self.role
        result['token_type'] = self.token_type
        result['user_id'] = self.user_id
        return result

    def from_map(self, map={}):
        self.access_token = map.get('access_token')
        self.default_drive_id = map.get('default_drive_id')
        self.expire_time = map.get('expire_time')
        self.expires_in = map.get('expires_in')
        self.refresh_token = map.get('refresh_token')
        self.role = map.get('role')
        self.token_type = map.get('token_type')
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
        self.avatar = avatar  # type: str
        # 用户的数据密码是否保存服务端
        self.data_pin_saved = data_pin_saved  # type: bool
        # 用户的数据密码是否设置过
        self.data_pin_setup = data_pin_setup  # type: bool
        # Default Drive ID
        self.default_drive_id = default_drive_id  # type: str
        # 当前用户已存在的登录方式
        self.exist_link = exist_link  # type: list
        # accessToken过期时间，ISO时间
        self.expire_time = expire_time  # type: str
        # accessToken过期时间，单位秒
        self.expires_in = expires_in  # type: int
        # 用户是否为第一次登录
        self.is_first_login = is_first_login  # type: bool
        # 是否需要绑定
        self.need_link = need_link  # type: bool
        # 当前用户昵称
        self.nick_name = nick_name  # type: str
        # 用于刷新accessToken
        self.refresh_token = refresh_token  # type: str
        # 当前用户角色
        self.role = role  # type: str
        # 临时权限，用于登录成功后设置密码
        self.state = state  # type: str
        # accessToken类型，Bearer
        self.token_type = token_type  # type: str
        # 用户自定义数据，格式为json，可用于配置项、少量临时数据等存储，不超过1K
        self.user_data = user_data  # type: dict
        # 当前用户ID
        self.user_id = user_id  # type: str
        # 当前用户名
        self.user_name = user_name  # type: str

    def validate(self):
        self.validate_required(self.access_token, 'access_token')
        if self.exist_link:
            for k in self.exist_link:
                if k:
                    k.validate()
        self.validate_required(self.need_link, 'need_link')

    def to_map(self):
        result = {}
        result['access_token'] = self.access_token
        result['avatar'] = self.avatar
        result['data_pin_saved'] = self.data_pin_saved
        result['data_pin_setup'] = self.data_pin_setup
        result['default_drive_id'] = self.default_drive_id
        result['exist_link'] = []
        if self.exist_link is not None:
            for k in self.exist_link:
                result['exist_link'].append(k.to_map() if k else None)
        else:
            result['exist_link'] = None
        result['expire_time'] = self.expire_time
        result['expires_in'] = self.expires_in
        result['is_first_login'] = self.is_first_login
        result['need_link'] = self.need_link
        result['nick_name'] = self.nick_name
        result['refresh_token'] = self.refresh_token
        result['role'] = self.role
        result['state'] = self.state
        result['token_type'] = self.token_type
        result['user_data'] = self.user_data
        result['user_id'] = self.user_id
        result['user_name'] = self.user_name
        return result

    def from_map(self, map={}):
        self.access_token = map.get('access_token')
        self.avatar = map.get('avatar')
        self.data_pin_saved = map.get('data_pin_saved')
        self.data_pin_setup = map.get('data_pin_setup')
        self.default_drive_id = map.get('default_drive_id')
        self.exist_link = []
        if map.get('exist_link') is not None:
            for k in map.get('exist_link'):
                temp_model = LinkInfo()
                self.exist_link.append(temp_model.from_map(k))
        else:
            self.exist_link = None
        self.expire_time = map.get('expire_time')
        self.expires_in = map.get('expires_in')
        self.is_first_login = map.get('is_first_login')
        self.need_link = map.get('need_link')
        self.nick_name = map.get('nick_name')
        self.refresh_token = map.get('refresh_token')
        self.role = map.get('role')
        self.state = map.get('state')
        self.token_type = map.get('token_type')
        self.user_data = map.get('user_data')
        self.user_id = map.get('user_id')
        self.user_name = map.get('user_name')
        return self


class AccountLinkRequest(TeaModel):
    """
    *
    """
    def __init__(self, headers=None, detail=None, extra=None, identity=None, status=None, type=None, user_id=None):
        self.headers = headers  # type: dict
        # 账号信息
        self.detail = detail  # type: str
        # 额外的信息，比如type为mobile时，此字段为国家编号，不填默认86
        self.extra = extra  # type: str
        # 唯一身份标识
        self.identity = identity  # type: str
        # 状态
        self.status = status  # type: str
        # 认证类型
        self.type = type  # type: str
        # 绑定的user_id
        self.user_id = user_id  # type: str

    def validate(self):
        self.validate_required(self.identity, 'identity')
        self.validate_required(self.type, 'type')
        self.validate_required(self.user_id, 'user_id')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['detail'] = self.detail
        result['extra'] = self.extra
        result['identity'] = self.identity
        result['status'] = self.status
        result['type'] = self.type
        result['user_id'] = self.user_id
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.detail = map.get('detail')
        self.extra = map.get('extra')
        self.identity = map.get('identity')
        self.status = map.get('status')
        self.type = map.get('type')
        self.user_id = map.get('user_id')
        return self


class AuthorizeRequest(TeaModel):
    """
    *
    """
    def __init__(self, client_id=None, login_type=None, redirect_uri=None, response_type=None, scope=None,
                 state=None):
        # Client ID, 此处填写创建App时返回的AppID
        self.client_id = client_id  # type: str
        # 鉴权方式，目前支持ding,ram鉴权
        self.login_type = login_type  # type: str
        # 回调地址, 此处填写创建App时填写的回调地址
        self.redirect_uri = redirect_uri  # type: str
        # 返回类型, 只能填写code
        self.response_type = response_type  # type: str
        # 申请的权限列表, 默认为所有权限
        self.scope = scope  # type: list
        # 用户自定义字段，会在鉴权成功后的callback带回
        self.state = state  # type: str

    def validate(self):
        self.validate_required(self.client_id, 'client_id')
        self.validate_required(self.redirect_uri, 'redirect_uri')
        self.validate_required(self.response_type, 'response_type')

    def to_map(self):
        result = {}
        result['ClientID'] = self.client_id
        result['LoginType'] = self.login_type
        result['RedirectUri'] = self.redirect_uri
        result['ResponseType'] = self.response_type
        result['Scope'] = self.scope
        result['State'] = self.state
        return result

    def from_map(self, map={}):
        self.client_id = map.get('ClientID')
        self.login_type = map.get('LoginType')
        self.redirect_uri = map.get('RedirectUri')
        self.response_type = map.get('ResponseType')
        self.scope = map.get('Scope')
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
        self.creator = creator  # type: str
        # Drive 备注信息
        self.description = description  # type: str
        # Domain ID
        self.domain_id = domain_id  # type: str
        # Drive ID
        self.drive_id = drive_id  # type: str
        # Drive 名称
        self.drive_name = drive_name  # type: str
        # Drive 类型
        self.drive_type = drive_type  # type: str
        self.encrypt_data_access = encrypt_data_access  # type: bool
        self.encrypt_mode = encrypt_mode  # type: str
        # Drive 所有者
        self.owner = owner  # type: str
        # Drive存储基于store的相对路径，domain的PathType为OSSPath时返回
        self.relative_path = relative_path  # type: str
        # Drive 状态
        self.status = status  # type: str
        # 存储 ID, domain的PathType为OSSPath时返回
        self.store_id = store_id  # type: str
        # Drive 空间总量
        self.total_size = total_size  # type: int
        # Drive 空间已使用量
        self.used_size = used_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['creator'] = self.creator
        result['description'] = self.description
        result['domain_id'] = self.domain_id
        result['drive_id'] = self.drive_id
        result['drive_name'] = self.drive_name
        result['drive_type'] = self.drive_type
        result['encrypt_data_access'] = self.encrypt_data_access
        result['encrypt_mode'] = self.encrypt_mode
        result['owner'] = self.owner
        result['relative_path'] = self.relative_path
        result['status'] = self.status
        result['store_id'] = self.store_id
        result['total_size'] = self.total_size
        result['used_size'] = self.used_size
        return result

    def from_map(self, map={}):
        self.creator = map.get('creator')
        self.description = map.get('description')
        self.domain_id = map.get('domain_id')
        self.drive_id = map.get('drive_id')
        self.drive_name = map.get('drive_name')
        self.drive_type = map.get('drive_type')
        self.encrypt_data_access = map.get('encrypt_data_access')
        self.encrypt_mode = map.get('encrypt_mode')
        self.owner = map.get('owner')
        self.relative_path = map.get('relative_path')
        self.status = map.get('status')
        self.store_id = map.get('store_id')
        self.total_size = map.get('total_size')
        self.used_size = map.get('used_size')
        return self


class BaseFileAnonymousResponse(TeaModel):
    """
    list_file_by_anonymous base response
    """
    def __init__(self, file_id=None, name=None, size=None, thumbnail=None, type=None, updated_at=None):
        # file_id
        self.file_id = file_id  # type: str
        # name
        self.name = name  # type: str
        # size, type=file时才有效
        self.size = size  # type: int
        # thumbnail
        self.thumbnail = thumbnail  # type: str
        # type
        self.type = type  # type: str
        # updated_at
        self.updated_at = updated_at  # type: str

    def validate(self):
        if self.file_id:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9]{1,50}')
        if self.name:
            self.validate_pattern(self.name, 'name', '[a-zA-Z0-9.-]{1,1000}')

    def to_map(self):
        result = {}
        result['file_id'] = self.file_id
        result['name'] = self.name
        result['size'] = self.size
        result['thumbnail'] = self.thumbnail
        result['type'] = self.type
        result['updated_at'] = self.updated_at
        return result

    def from_map(self, map={}):
        self.file_id = map.get('file_id')
        self.name = map.get('name')
        self.size = map.get('size')
        self.thumbnail = map.get('thumbnail')
        self.type = map.get('type')
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
        self.category = category  # type: str
        # Content Hash
        self.content_hash = content_hash  # type: str
        # content_hash_name
        self.content_hash_name = content_hash_name  # type: str
        # content_type
        self.content_type = content_type  # type: str
        # crc64_hash
        self.crc_64hash = crc_64hash  # type: str
        # created_at
        self.created_at = created_at  # type: str
        # description
        self.description = description  # type: str
        # DomainID
        self.domain_id = domain_id  # type: str
        # download_url
        self.download_url = download_url  # type: str
        # drive_id
        self.drive_id = drive_id  # type: str
        # encrypt_mode
        self.encrypt_mode = encrypt_mode  # type: str
        # file_extension
        self.file_extension = file_extension  # type: str
        # file_id
        self.file_id = file_id  # type: str
        # Hidden
        # type: boolean
        self.hidden = hidden  # type: bool
        self.image_media_metadata = image_media_metadata  # type: ImageMediaResponse
        # labels
        self.labels = labels  # type: list
        self.meta = meta  # type: str
        # name
        self.name = name  # type: str
        # parent_file_id
        self.parent_file_id = parent_file_id  # type: str
        self.punish_flag = punish_flag  # type: int
        # Size
        self.size = size  # type: int
        # starred
        # type: boolean
        self.starred = starred  # type: bool
        # status
        self.status = status  # type: str
        # @Deprecated streams url info
        self.streams_info = streams_info  # type: dict
        # thumbnail
        self.thumbnail = thumbnail  # type: str
        # trashed_at
        self.trashed_at = trashed_at  # type: str
        # type
        self.type = type  # type: str
        # updated_at
        self.updated_at = updated_at  # type: str
        # upload_id
        self.upload_id = upload_id  # type: str
        # url
        self.url = url  # type: str
        # user_meta
        self.user_meta = user_meta  # type: str
        self.video_media_metadata = video_media_metadata  # type: VideoMediaResponse
        self.video_preview_metadata = video_preview_metadata  # type: VideoPreviewResponse

    def validate(self):
        if self.domain_id:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z]+')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.file_id:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9]{1,50}')
        if self.image_media_metadata:
            self.image_media_metadata.validate()
        self.validate_required(self.name, 'name')
        if self.name:
            self.validate_pattern(self.name, 'name', '[a-zA-Z0-9.-]{1,1000}')
        if self.parent_file_id:
            self.validate_max_length(self.parent_file_id, 'parent_file_id', 50)
            self.validate_pattern(self.parent_file_id, 'parent_file_id', '[a-z0-9]{1,50}')
        if self.video_media_metadata:
            self.video_media_metadata.validate()
        if self.video_preview_metadata:
            self.video_preview_metadata.validate()

    def to_map(self):
        result = {}
        result['category'] = self.category
        result['content_hash'] = self.content_hash
        result['content_hash_name'] = self.content_hash_name
        result['content_type'] = self.content_type
        result['crc64_hash'] = self.crc_64hash
        result['created_at'] = self.created_at
        result['description'] = self.description
        result['domain_id'] = self.domain_id
        result['download_url'] = self.download_url
        result['drive_id'] = self.drive_id
        result['encrypt_mode'] = self.encrypt_mode
        result['file_extension'] = self.file_extension
        result['file_id'] = self.file_id
        result['hidden'] = self.hidden
        if self.image_media_metadata is not None:
            result['image_media_metadata'] = self.image_media_metadata.to_map()
        else:
            result['image_media_metadata'] = None
        result['labels'] = self.labels
        result['meta'] = self.meta
        result['name'] = self.name
        result['parent_file_id'] = self.parent_file_id
        result['punish_flag'] = self.punish_flag
        result['size'] = self.size
        result['starred'] = self.starred
        result['status'] = self.status
        result['streams_info'] = self.streams_info
        result['thumbnail'] = self.thumbnail
        result['trashed_at'] = self.trashed_at
        result['type'] = self.type
        result['updated_at'] = self.updated_at
        result['upload_id'] = self.upload_id
        result['url'] = self.url
        result['user_meta'] = self.user_meta
        if self.video_media_metadata is not None:
            result['video_media_metadata'] = self.video_media_metadata.to_map()
        else:
            result['video_media_metadata'] = None
        if self.video_preview_metadata is not None:
            result['video_preview_metadata'] = self.video_preview_metadata.to_map()
        else:
            result['video_preview_metadata'] = None
        return result

    def from_map(self, map={}):
        self.category = map.get('category')
        self.content_hash = map.get('content_hash')
        self.content_hash_name = map.get('content_hash_name')
        self.content_type = map.get('content_type')
        self.crc_64hash = map.get('crc64_hash')
        self.created_at = map.get('created_at')
        self.description = map.get('description')
        self.domain_id = map.get('domain_id')
        self.download_url = map.get('download_url')
        self.drive_id = map.get('drive_id')
        self.encrypt_mode = map.get('encrypt_mode')
        self.file_extension = map.get('file_extension')
        self.file_id = map.get('file_id')
        self.hidden = map.get('hidden')
        if map.get('image_media_metadata') is not None:
            temp_model = ImageMediaResponse()
            self.image_media_metadata = temp_model.from_map(map['image_media_metadata'])
        else:
            self.image_media_metadata = None
        self.labels = map.get('labels')
        self.meta = map.get('meta')
        self.name = map.get('name')
        self.parent_file_id = map.get('parent_file_id')
        self.punish_flag = map.get('punish_flag')
        self.size = map.get('size')
        self.starred = map.get('starred')
        self.status = map.get('status')
        self.streams_info = map.get('streams_info')
        self.thumbnail = map.get('thumbnail')
        self.trashed_at = map.get('trashed_at')
        self.type = map.get('type')
        self.updated_at = map.get('updated_at')
        self.upload_id = map.get('upload_id')
        self.url = map.get('url')
        self.user_meta = map.get('user_meta')
        if map.get('video_media_metadata') is not None:
            temp_model = VideoMediaResponse()
            self.video_media_metadata = temp_model.from_map(map['video_media_metadata'])
        else:
            self.video_media_metadata = None
        if map.get('video_preview_metadata') is not None:
            temp_model = VideoPreviewResponse()
            self.video_preview_metadata = temp_model.from_map(map['video_preview_metadata'])
        else:
            self.video_preview_metadata = None
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
        self.city = city  # type: str
        # country
        self.country = country  # type: str
        # district
        self.district = district  # type: str
        # height
        self.height = height  # type: int
        # location
        self.location = location  # type: str
        # province
        self.province = province  # type: str
        # time
        self.time = time  # type: str
        # township
        self.township = township  # type: str
        # width
        self.width = width  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['address_line'] = self.address_line
        result['city'] = self.city
        result['country'] = self.country
        result['district'] = self.district
        result['height'] = self.height
        result['location'] = self.location
        result['province'] = self.province
        result['time'] = self.time
        result['township'] = self.township
        result['width'] = self.width
        return result

    def from_map(self, map={}):
        self.address_line = map.get('address_line')
        self.city = map.get('city')
        self.country = map.get('country')
        self.district = map.get('district')
        self.height = map.get('height')
        self.location = map.get('location')
        self.province = map.get('province')
        self.time = map.get('time')
        self.township = map.get('township')
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
        self.crc_64hash = crc_64hash  # type: str
        # created_at
        self.created_at = created_at  # type: str
        # description
        self.description = description  # type: str
        # domain_id
        self.domain_id = domain_id  # type: str
        # download_url
        self.download_url = download_url  # type: str
        # drive_id
        self.drive_id = drive_id  # type: str
        # file_extension
        self.file_extension = file_extension  # type: str
        # file_path
        self.file_path = file_path  # type: str
        # name
        self.name = name  # type: str
        # parent_file_id
        self.parent_file_path = parent_file_path  # type: str
        # share_id
        self.share_id = share_id  # type: str
        # Size
        self.size = size  # type: int
        # status
        self.status = status  # type: str
        # thumbnail
        self.thumbnail = thumbnail  # type: str
        # trashed_at
        self.trashed_at = trashed_at  # type: str
        # type
        self.type = type  # type: str
        # updated_at
        self.updated_at = updated_at  # type: str
        # upload_id
        self.upload_id = upload_id  # type: str
        # url
        self.url = url  # type: str

    def validate(self):
        if self.domain_id:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z]+')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.name, 'name')
        if self.name:
            self.validate_pattern(self.name, 'name', '[a-zA-Z0-9.-]{1,1000}')
        if self.parent_file_path:
            self.validate_max_length(self.parent_file_path, 'parent_file_path', 50)
            self.validate_pattern(self.parent_file_path, 'parent_file_path', '[a-z0-9]{1,50}')
        if self.share_id:
            self.validate_pattern(self.share_id, 'share_id', '[0-9]+')

    def to_map(self):
        result = {}
        result['content_hash'] = self.content_hash
        result['content_hash_name'] = self.content_hash_name
        result['content_type'] = self.content_type
        result['crc64_hash'] = self.crc_64hash
        result['created_at'] = self.created_at
        result['description'] = self.description
        result['domain_id'] = self.domain_id
        result['download_url'] = self.download_url
        result['drive_id'] = self.drive_id
        result['file_extension'] = self.file_extension
        result['file_path'] = self.file_path
        result['name'] = self.name
        result['parent_file_path'] = self.parent_file_path
        result['share_id'] = self.share_id
        result['size'] = self.size
        result['status'] = self.status
        result['thumbnail'] = self.thumbnail
        result['trashed_at'] = self.trashed_at
        result['type'] = self.type
        result['updated_at'] = self.updated_at
        result['upload_id'] = self.upload_id
        result['url'] = self.url
        return result

    def from_map(self, map={}):
        self.content_hash = map.get('content_hash')
        self.content_hash_name = map.get('content_hash_name')
        self.content_type = map.get('content_type')
        self.crc_64hash = map.get('crc64_hash')
        self.created_at = map.get('created_at')
        self.description = map.get('description')
        self.domain_id = map.get('domain_id')
        self.download_url = map.get('download_url')
        self.drive_id = map.get('drive_id')
        self.file_extension = map.get('file_extension')
        self.file_path = map.get('file_path')
        self.name = map.get('name')
        self.parent_file_path = map.get('parent_file_path')
        self.share_id = map.get('share_id')
        self.size = map.get('size')
        self.status = map.get('status')
        self.thumbnail = map.get('thumbnail')
        self.trashed_at = map.get('trashed_at')
        self.type = map.get('type')
        self.updated_at = map.get('updated_at')
        self.upload_id = map.get('upload_id')
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
        self.created_at = created_at  # type: str
        # 下载次数
        self.download_count = download_count  # type: int
        # drive_id
        self.drive_id = drive_id  # type: str
        # expiration
        self.expiration = expiration  # type: str
        # expired
        self.expired = expired  # type: bool
        # file_id
        self.file_id = file_id  # type: str
        # preview_count
        self.preview_count = preview_count  # type: int
        # 转存次数
        self.save_count = save_count  # type: int
        # share_id
        self.share_id = share_id  # type: str
        # share_msg
        self.share_msg = share_msg  # type: str
        # share_policy
        self.share_policy = share_policy  # type: str
        # share_pwd
        self.share_pwd = share_pwd  # type: str
        # share_url
        self.share_url = share_url  # type: str
        # updated_at
        self.updated_at = updated_at  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['created_at'] = self.created_at
        result['download_count'] = self.download_count
        result['drive_id'] = self.drive_id
        result['expiration'] = self.expiration
        result['expired'] = self.expired
        result['file_id'] = self.file_id
        result['preview_count'] = self.preview_count
        result['save_count'] = self.save_count
        result['share_id'] = self.share_id
        result['share_msg'] = self.share_msg
        result['share_policy'] = self.share_policy
        result['share_pwd'] = self.share_pwd
        result['share_url'] = self.share_url
        result['updated_at'] = self.updated_at
        return result

    def from_map(self, map={}):
        self.created_at = map.get('created_at')
        self.download_count = map.get('download_count')
        self.drive_id = map.get('drive_id')
        self.expiration = map.get('expiration')
        self.expired = map.get('expired')
        self.file_id = map.get('file_id')
        self.preview_count = map.get('preview_count')
        self.save_count = map.get('save_count')
        self.share_id = map.get('share_id')
        self.share_msg = map.get('share_msg')
        self.share_policy = map.get('share_policy')
        self.share_pwd = map.get('share_pwd')
        self.share_url = map.get('share_url')
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
        self.created_at = created_at  # type: str
        # creator
        self.creator = creator  # type: str
        # description
        self.description = description  # type: str
        # domain_id
        self.domain_id = domain_id  # type: str
        # drive_id
        self.drive_id = drive_id  # type: str
        # expiration
        self.expiration = expiration  # type: str
        # expired
        self.expired = expired  # type: bool
        # owner
        self.owner = owner  # type: str
        # permissions
        self.permissions = permissions  # type: list
        # share_path
        self.share_file_path = share_file_path  # type: str
        # share_id
        self.share_id = share_id  # type: str
        # share_name
        self.share_name = share_name  # type: str
        self.share_policy = share_policy  # type: list
        # status
        self.status = status  # type: str
        # updated_at
        self.updated_at = updated_at  # type: str

    def validate(self):
        if self.share_policy:
            for k in self.share_policy:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['created_at'] = self.created_at
        result['creator'] = self.creator
        result['description'] = self.description
        result['domain_id'] = self.domain_id
        result['drive_id'] = self.drive_id
        result['expiration'] = self.expiration
        result['expired'] = self.expired
        result['owner'] = self.owner
        result['permissions'] = self.permissions
        result['share_file_path'] = self.share_file_path
        result['share_id'] = self.share_id
        result['share_name'] = self.share_name
        result['share_policy'] = []
        if self.share_policy is not None:
            for k in self.share_policy:
                result['share_policy'].append(k.to_map() if k else None)
        else:
            result['share_policy'] = None
        result['status'] = self.status
        result['updated_at'] = self.updated_at
        return result

    def from_map(self, map={}):
        self.created_at = map.get('created_at')
        self.creator = map.get('creator')
        self.description = map.get('description')
        self.domain_id = map.get('domain_id')
        self.drive_id = map.get('drive_id')
        self.expiration = map.get('expiration')
        self.expired = map.get('expired')
        self.owner = map.get('owner')
        self.permissions = map.get('permissions')
        self.share_file_path = map.get('share_file_path')
        self.share_id = map.get('share_id')
        self.share_name = map.get('share_name')
        self.share_policy = []
        if map.get('share_policy') is not None:
            for k in map.get('share_policy'):
                temp_model = SharePermissionPolicy()
                self.share_policy.append(temp_model.from_map(k))
        else:
            self.share_policy = None
        self.status = map.get('status')
        self.updated_at = map.get('updated_at')
        return self


class BatchResponse(TeaModel):
    """
    batch operation response
    """
    def __init__(self, responses=None):
        # responses 返回结果合集
        self.responses = responses  # type: list

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
        else:
            result['responses'] = None
        return result

    def from_map(self, map={}):
        self.responses = []
        if map.get('responses') is not None:
            for k in map.get('responses'):
                temp_model = BatchSubResponse()
                self.responses.append(temp_model.from_map(k))
        else:
            self.responses = None
        return self


class BatchSubResponse(TeaModel):
    """
    *
    """
    def __init__(self, body=None, id=None, status=None):
        # body 子请求的返回结果，可参考对于子请求文档 json 字符串
        self.body = body  # type: dict
        # id 请求带过来的id, 可以跟 request 进行关联
        self.id = id  # type: str
        # status 子请求的返回状态码，可参考对于子请求文档
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['body'] = self.body
        result['id'] = self.id
        result['status'] = self.status
        return result

    def from_map(self, map={}):
        self.body = map.get('body')
        self.id = map.get('id')
        self.status = map.get('status')
        return self


class CancelLinkRequest(TeaModel):
    """
    *
    """
    def __init__(self, headers=None, temporary_token=None):
        self.headers = headers  # type: dict
        # 待绑定的临时token，此token只能访问绑定、取消绑定接口
        self.temporary_token = temporary_token  # type: str

    def validate(self):
        self.validate_required(self.temporary_token, 'temporary_token')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['temporary_token'] = self.temporary_token
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.temporary_token = map.get('temporary_token')
        return self


class Captcha(TeaModel):
    """
    *
    """
    def __init__(self, captcha=None, captcha_format=None, captcha_id=None):
        # 图片验证码，base64格式
        self.captcha = captcha  # type: str
        # 图片格式
        self.captcha_format = captcha_format  # type: str
        # 图片验证码ID
        self.captcha_id = captcha_id  # type: str

    def validate(self):
        self.validate_required(self.captcha, 'captcha')
        self.validate_required(self.captcha_format, 'captcha_format')
        self.validate_required(self.captcha_id, 'captcha_id')

    def to_map(self):
        result = {}
        result['captcha'] = self.captcha
        result['captcha_format'] = self.captcha_format
        result['captcha_id'] = self.captcha_id
        return result

    def from_map(self, map={}):
        self.captcha = map.get('captcha')
        self.captcha_format = map.get('captcha_format')
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
        self.category = category  # type: str
        # Content Hash
        self.content_hash = content_hash  # type: str
        # content_hash_name
        self.content_hash_name = content_hash_name  # type: str
        # content_type
        self.content_type = content_type  # type: str
        # crc64_hash
        self.crc_64hash = crc_64hash  # type: str
        # created_at
        self.created_at = created_at  # type: str
        # description
        self.description = description  # type: str
        # DomainID
        self.domain_id = domain_id  # type: str
        # download_url
        self.download_url = download_url  # type: str
        # drive_id
        self.drive_id = drive_id  # type: str
        # encrypt_mode
        self.encrypt_mode = encrypt_mode  # type: str
        # file_extension
        self.file_extension = file_extension  # type: str
        # file_id
        self.file_id = file_id  # type: str
        # Hidden
        # type: boolean
        self.hidden = hidden  # type: bool
        self.image_media_metadata = image_media_metadata  # type: ImageMediaResponse
        # labels
        self.labels = labels  # type: list
        self.meta = meta  # type: str
        # name
        self.name = name  # type: str
        # parent_file_id
        self.parent_file_id = parent_file_id  # type: str
        self.punish_flag = punish_flag  # type: int
        # Size
        self.size = size  # type: int
        # starred
        # type: boolean
        self.starred = starred  # type: bool
        # status
        self.status = status  # type: str
        # @Deprecated streams url info
        self.streams_info = streams_info  # type: dict
        # thumbnail
        self.thumbnail = thumbnail  # type: str
        # trashed_at
        self.trashed_at = trashed_at  # type: str
        # type
        self.type = type  # type: str
        # updated_at
        self.updated_at = updated_at  # type: str
        # upload_id
        self.upload_id = upload_id  # type: str
        # url
        self.url = url  # type: str
        # user_meta
        self.user_meta = user_meta  # type: str
        self.video_media_metadata = video_media_metadata  # type: VideoMediaResponse
        self.video_preview_metadata = video_preview_metadata  # type: VideoPreviewResponse

    def validate(self):
        if self.domain_id:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z]+')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.file_id:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9]{1,50}')
        if self.image_media_metadata:
            self.image_media_metadata.validate()
        self.validate_required(self.name, 'name')
        if self.name:
            self.validate_pattern(self.name, 'name', '[a-zA-Z0-9.-]{1,1000}')
        if self.parent_file_id:
            self.validate_max_length(self.parent_file_id, 'parent_file_id', 50)
            self.validate_pattern(self.parent_file_id, 'parent_file_id', '[a-z0-9]{1,50}')
        if self.video_media_metadata:
            self.video_media_metadata.validate()
        if self.video_preview_metadata:
            self.video_preview_metadata.validate()

    def to_map(self):
        result = {}
        result['category'] = self.category
        result['content_hash'] = self.content_hash
        result['content_hash_name'] = self.content_hash_name
        result['content_type'] = self.content_type
        result['crc64_hash'] = self.crc_64hash
        result['created_at'] = self.created_at
        result['description'] = self.description
        result['domain_id'] = self.domain_id
        result['download_url'] = self.download_url
        result['drive_id'] = self.drive_id
        result['encrypt_mode'] = self.encrypt_mode
        result['file_extension'] = self.file_extension
        result['file_id'] = self.file_id
        result['hidden'] = self.hidden
        if self.image_media_metadata is not None:
            result['image_media_metadata'] = self.image_media_metadata.to_map()
        else:
            result['image_media_metadata'] = None
        result['labels'] = self.labels
        result['meta'] = self.meta
        result['name'] = self.name
        result['parent_file_id'] = self.parent_file_id
        result['punish_flag'] = self.punish_flag
        result['size'] = self.size
        result['starred'] = self.starred
        result['status'] = self.status
        result['streams_info'] = self.streams_info
        result['thumbnail'] = self.thumbnail
        result['trashed_at'] = self.trashed_at
        result['type'] = self.type
        result['updated_at'] = self.updated_at
        result['upload_id'] = self.upload_id
        result['url'] = self.url
        result['user_meta'] = self.user_meta
        if self.video_media_metadata is not None:
            result['video_media_metadata'] = self.video_media_metadata.to_map()
        else:
            result['video_media_metadata'] = None
        if self.video_preview_metadata is not None:
            result['video_preview_metadata'] = self.video_preview_metadata.to_map()
        else:
            result['video_preview_metadata'] = None
        return result

    def from_map(self, map={}):
        self.category = map.get('category')
        self.content_hash = map.get('content_hash')
        self.content_hash_name = map.get('content_hash_name')
        self.content_type = map.get('content_type')
        self.crc_64hash = map.get('crc64_hash')
        self.created_at = map.get('created_at')
        self.description = map.get('description')
        self.domain_id = map.get('domain_id')
        self.download_url = map.get('download_url')
        self.drive_id = map.get('drive_id')
        self.encrypt_mode = map.get('encrypt_mode')
        self.file_extension = map.get('file_extension')
        self.file_id = map.get('file_id')
        self.hidden = map.get('hidden')
        if map.get('image_media_metadata') is not None:
            temp_model = ImageMediaResponse()
            self.image_media_metadata = temp_model.from_map(map['image_media_metadata'])
        else:
            self.image_media_metadata = None
        self.labels = map.get('labels')
        self.meta = map.get('meta')
        self.name = map.get('name')
        self.parent_file_id = map.get('parent_file_id')
        self.punish_flag = map.get('punish_flag')
        self.size = map.get('size')
        self.starred = map.get('starred')
        self.status = map.get('status')
        self.streams_info = map.get('streams_info')
        self.thumbnail = map.get('thumbnail')
        self.trashed_at = map.get('trashed_at')
        self.type = map.get('type')
        self.updated_at = map.get('updated_at')
        self.upload_id = map.get('upload_id')
        self.url = map.get('url')
        self.user_meta = map.get('user_meta')
        if map.get('video_media_metadata') is not None:
            temp_model = VideoMediaResponse()
            self.video_media_metadata = temp_model.from_map(map['video_media_metadata'])
        else:
            self.video_media_metadata = None
        if map.get('video_preview_metadata') is not None:
            temp_model = VideoPreviewResponse()
            self.video_preview_metadata = temp_model.from_map(map['video_preview_metadata'])
        else:
            self.video_preview_metadata = None
        return self


class ConfirmLinkRequest(TeaModel):
    """
    *
    """
    def __init__(self, headers=None, temporary_token=None):
        self.headers = headers  # type: dict
        # 待绑定的临时token，此token只能访问绑定、取消绑定接口
        self.temporary_token = temporary_token  # type: str

    def validate(self):
        self.validate_required(self.temporary_token, 'temporary_token')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['temporary_token'] = self.temporary_token
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
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
        self.domain_id = domain_id  # type: str
        # drive_id
        self.drive_id = drive_id  # type: str
        # file_id
        self.file_id = file_id  # type: str

    def validate(self):
        if self.domain_id:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z]+')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.file_id:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9]{1,50}')

    def to_map(self):
        result = {}
        result['async_task_id'] = self.async_task_id
        result['domain_id'] = self.domain_id
        result['drive_id'] = self.drive_id
        result['file_id'] = self.file_id
        return result

    def from_map(self, map={}):
        self.async_task_id = map.get('async_task_id')
        self.domain_id = map.get('domain_id')
        self.drive_id = map.get('drive_id')
        self.file_id = map.get('file_id')
        return self


class CorsRule(TeaModel):
    """
    *
    """
    def __init__(self, allowed_header=None, allowed_method=None, allowed_origin=None, expose_header=None,
                 max_age_seconds=None):
        # AllowedHeader
        self.allowed_header = allowed_header  # type: list
        # AllowedMethod
        self.allowed_method = allowed_method  # type: list
        # AllowedOrigin
        self.allowed_origin = allowed_origin  # type: list
        # ExposeHeader
        self.expose_header = expose_header  # type: list
        # MaxAgeSeconds
        self.max_age_seconds = max_age_seconds  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['allowed_header'] = self.allowed_header
        result['allowed_method'] = self.allowed_method
        result['allowed_origin'] = self.allowed_origin
        result['expose_header'] = self.expose_header
        result['max_age_seconds'] = self.max_age_seconds
        return result

    def from_map(self, map={}):
        self.allowed_header = map.get('allowed_header')
        self.allowed_method = map.get('allowed_method')
        self.allowed_origin = map.get('allowed_origin')
        self.expose_header = map.get('expose_header')
        self.max_age_seconds = map.get('max_age_seconds')
        return self


class CreateDriveResponse(TeaModel):
    """
    Create drive response
    """
    def __init__(self, domain_id=None, drive_id=None):
        # Domain ID
        self.domain_id = domain_id  # type: str
        # Drive ID
        self.drive_id = drive_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['domain_id'] = self.domain_id
        result['drive_id'] = self.drive_id
        return result

    def from_map(self, map={}):
        self.domain_id = map.get('domain_id')
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
        self.domain_id = domain_id  # type: str
        # drive_id
        self.drive_id = drive_id  # type: str
        # encrypt_mode
        self.encrypt_mode = encrypt_mode  # type: str
        # exist
        # type: boolean
        self.exist = exist  # type: bool
        # file_id
        self.file_id = file_id  # type: str
        # file_name
        self.file_name = file_name  # type: str
        # parent_file_id
        self.parent_file_id = parent_file_id  # type: str
        # part_info_list
        self.part_info_list = part_info_list  # type: list
        # rapid_upload
        # type: boolean
        self.rapid_upload = rapid_upload  # type: bool
        # status
        self.status = status  # type: str
        # streams_upload_info
        self.streams_upload_info = streams_upload_info  # type: dict
        # type
        self.type = type  # type: str
        # upload_id
        self.upload_id = upload_id  # type: str

    def validate(self):
        if self.domain_id:
            self.validate_max_length(self.domain_id, 'domain_id', 50)
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9]{1,50}')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.file_id:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9]{1,50}')
        if self.file_name:
            self.validate_max_length(self.file_name, 'file_name', 255)
        if self.parent_file_id:
            self.validate_max_length(self.parent_file_id, 'parent_file_id', 50)
            self.validate_pattern(self.parent_file_id, 'parent_file_id', '[a-z0-9]{1,50}')
        if self.part_info_list:
            for k in self.part_info_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['domain_id'] = self.domain_id
        result['drive_id'] = self.drive_id
        result['encrypt_mode'] = self.encrypt_mode
        result['exist'] = self.exist
        result['file_id'] = self.file_id
        result['file_name'] = self.file_name
        result['parent_file_id'] = self.parent_file_id
        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k in self.part_info_list:
                result['part_info_list'].append(k.to_map() if k else None)
        else:
            result['part_info_list'] = None
        result['rapid_upload'] = self.rapid_upload
        result['status'] = self.status
        result['streams_upload_info'] = self.streams_upload_info
        result['type'] = self.type
        result['upload_id'] = self.upload_id
        return result

    def from_map(self, map={}):
        self.domain_id = map.get('domain_id')
        self.drive_id = map.get('drive_id')
        self.encrypt_mode = map.get('encrypt_mode')
        self.exist = map.get('exist')
        self.file_id = map.get('file_id')
        self.file_name = map.get('file_name')
        self.parent_file_id = map.get('parent_file_id')
        self.part_info_list = []
        if map.get('part_info_list') is not None:
            for k in map.get('part_info_list'):
                temp_model = UploadPartInfo()
                self.part_info_list.append(temp_model.from_map(k))
        else:
            self.part_info_list = None
        self.rapid_upload = map.get('rapid_upload')
        self.status = map.get('status')
        self.streams_upload_info = map.get('streams_upload_info')
        self.type = map.get('type')
        self.upload_id = map.get('upload_id')
        return self


class CreateShareLinkResponse(TeaModel):
    """
    create_share_link response
    """
    def __init__(self, share_id=None, share_msg=None, share_policy=None, share_pwd=None, share_url=None):
        # share_id
        self.share_id = share_id  # type: str
        # share_msg
        self.share_msg = share_msg  # type: str
        # share_policy
        self.share_policy = share_policy  # type: str
        # share_pwd
        self.share_pwd = share_pwd  # type: str
        # share_url
        self.share_url = share_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['share_id'] = self.share_id
        result['share_msg'] = self.share_msg
        result['share_policy'] = self.share_policy
        result['share_pwd'] = self.share_pwd
        result['share_url'] = self.share_url
        return result

    def from_map(self, map={}):
        self.share_id = map.get('share_id')
        self.share_msg = map.get('share_msg')
        self.share_policy = map.get('share_policy')
        self.share_pwd = map.get('share_pwd')
        self.share_url = map.get('share_url')
        return self


class CreateShareResponse(TeaModel):
    """
    Create share response
    """
    def __init__(self, domain_id=None, share_id=None):
        # domain_id
        self.domain_id = domain_id  # type: str
        # share_id
        self.share_id = share_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['domain_id'] = self.domain_id
        result['share_id'] = self.share_id
        return result

    def from_map(self, map={}):
        self.domain_id = map.get('domain_id')
        self.share_id = map.get('share_id')
        return self


class CroppingBoundary(TeaModel):
    """
    *
    """
    def __init__(self, height=None, left=None, top=None, width=None):
        self.height = height  # type: int
        self.left = left  # type: int
        self.top = top  # type: int
        self.width = width  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['height'] = self.height
        result['left'] = self.left
        result['top'] = self.top
        result['width'] = self.width
        return result

    def from_map(self, map={}):
        self.height = map.get('height')
        self.left = map.get('left')
        self.top = map.get('top')
        self.width = map.get('width')
        return self


class CroppingSuggestionItem(TeaModel):
    """
    *
    """
    def __init__(self, aspect_ratio=None, cropping_boundary=None, score=None):
        self.aspect_ratio = aspect_ratio  # type: str
        self.cropping_boundary = cropping_boundary  # type: CroppingBoundary
        self.score = score  # type: int

    def validate(self):
        if self.cropping_boundary:
            self.cropping_boundary.validate()

    def to_map(self):
        result = {}
        result['aspect_ratio'] = self.aspect_ratio
        if self.cropping_boundary is not None:
            result['cropping_boundary'] = self.cropping_boundary.to_map()
        else:
            result['cropping_boundary'] = None
        result['score'] = self.score
        return result

    def from_map(self, map={}):
        self.aspect_ratio = map.get('aspect_ratio')
        if map.get('cropping_boundary') is not None:
            temp_model = CroppingBoundary()
            self.cropping_boundary = temp_model.from_map(map['cropping_boundary'])
        else:
            self.cropping_boundary = None
        self.score = map.get('score')
        return self


class DefaultChangePasswordRequest(TeaModel):
    """
    *
    """
    def __init__(self, headers=None, app_id=None, encrypted_key=None, new_password=None, phone_number=None,
                 phone_region=None, state=None):
        self.headers = headers  # type: dict
        # App ID, 当前访问的App
        self.app_id = app_id  # type: str
        # AES-256对称加密密钥，通过App公钥加密后传输
        self.encrypted_key = encrypted_key  # type: str
        # 新密码，必须包含数字和字母，长度8-20个字符
        self.new_password = new_password  # type: str
        # 手机号
        self.phone_number = phone_number  # type: str
        # 国家编号，默认86，不需要填+号，直接填数字
        self.phone_region = phone_region  # type: str
        # 修改密码的临时授权码
        self.state = state  # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.encrypted_key, 'encrypted_key')
        self.validate_required(self.new_password, 'new_password')
        self.validate_required(self.phone_number, 'phone_number')
        self.validate_required(self.state, 'state')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['app_id'] = self.app_id
        result['encrypted_key'] = self.encrypted_key
        result['new_password'] = self.new_password
        result['phone_number'] = self.phone_number
        result['phone_region'] = self.phone_region
        result['state'] = self.state
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.app_id = map.get('app_id')
        self.encrypted_key = map.get('encrypted_key')
        self.new_password = map.get('new_password')
        self.phone_number = map.get('phone_number')
        self.phone_region = map.get('phone_region')
        self.state = map.get('state')
        return self


class DefaultSetPasswordRequest(TeaModel):
    """
    *
    """
    def __init__(self, headers=None, app_id=None, encrypted_key=None, new_password=None, state=None):
        self.headers = headers  # type: dict
        # App ID, 当前访问的App
        self.app_id = app_id  # type: str
        # AES-256对称加密密钥，通过App公钥加密后传输
        self.encrypted_key = encrypted_key  # type: str
        # 新密码，必须包含数字和字母，长度8-20个字符，使用AES-256对称加密后传输（CBC模式, 填充算法为PKCS7Padding，生成base64字符串）
        self.new_password = new_password  # type: str
        # 修改密码的临时授权码
        self.state = state  # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.encrypted_key, 'encrypted_key')
        self.validate_required(self.new_password, 'new_password')
        self.validate_required(self.state, 'state')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['app_id'] = self.app_id
        result['encrypted_key'] = self.encrypted_key
        result['new_password'] = self.new_password
        result['state'] = self.state
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.app_id = map.get('app_id')
        self.encrypted_key = map.get('encrypted_key')
        self.new_password = map.get('new_password')
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
        self.domain_id = domain_id  # type: str
        # drive_id
        self.drive_id = drive_id  # type: str
        # file_id
        self.file_id = file_id  # type: str

    def validate(self):
        if self.domain_id:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z]+')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.file_id:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9]{1,50}')

    def to_map(self):
        result = {}
        result['async_task_id'] = self.async_task_id
        result['domain_id'] = self.domain_id
        result['drive_id'] = self.drive_id
        result['file_id'] = self.file_id
        return result

    def from_map(self, map={}):
        self.async_task_id = map.get('async_task_id')
        self.domain_id = map.get('domain_id')
        self.drive_id = map.get('drive_id')
        self.file_id = map.get('file_id')
        return self


class DeleteFilesResponse(TeaModel):
    """
    批量删除文件 response
    """
    def __init__(self, deleted_file_id_list=None, domain_id=None, drive_id=None):
        # deleted_file_id_list
        self.deleted_file_id_list = deleted_file_id_list  # type: list
        # domain_id
        self.domain_id = domain_id  # type: str
        # drive_id
        self.drive_id = drive_id  # type: str

    def validate(self):
        if self.domain_id:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z]+')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')

    def to_map(self):
        result = {}
        result['deleted_file_id_list'] = self.deleted_file_id_list
        result['domain_id'] = self.domain_id
        result['drive_id'] = self.drive_id
        return result

    def from_map(self, map={}):
        self.deleted_file_id_list = map.get('deleted_file_id_list')
        self.domain_id = map.get('domain_id')
        self.drive_id = map.get('drive_id')
        return self


class DeviceAuthorizeRequest(TeaModel):
    """
    *
    """
    def __init__(self, client_id=None, device_info=None, device_name=None, login_type=None, scope=None):
        # Client ID, 此处填写创建App时返回的AppID
        self.client_id = client_id  # type: str
        # 设备信息，用于用户识别设备
        self.device_info = device_info  # type: str
        # 设备名，实现方需保证不同设备的设备名不重复（推荐用硬件名称+硬件型号作为设备名）
        self.device_name = device_name  # type: str
        # 鉴权方式，目前支持ding,ram鉴权
        self.login_type = login_type  # type: str
        # 申请的权限列表, 默认为所有权限
        self.scope = scope  # type: list

    def validate(self):
        self.validate_required(self.client_id, 'client_id')
        self.validate_required(self.device_name, 'device_name')

    def to_map(self):
        result = {}
        result['ClientID'] = self.client_id
        result['DeviceInfo'] = self.device_info
        result['DeviceName'] = self.device_name
        result['LoginType'] = self.login_type
        result['Scope'] = self.scope
        return result

    def from_map(self, map={}):
        self.client_id = map.get('ClientID')
        self.device_info = map.get('DeviceInfo')
        self.device_name = map.get('DeviceName')
        self.login_type = map.get('LoginType')
        self.scope = map.get('Scope')
        return self


class FileDeltaResponse(TeaModel):
    """
    the file op info
    """
    def __init__(self, current_category=None, file=None, file_id=None, op=None):
        self.current_category = current_category  # type: str
        self.file = file  # type: BaseFileResponse
        self.file_id = file_id  # type: str
        self.op = op  # type: str

    def validate(self):
        if self.file:
            self.file.validate()

    def to_map(self):
        result = {}
        result['current_category'] = self.current_category
        if self.file is not None:
            result['file'] = self.file.to_map()
        else:
            result['file'] = None
        result['file_id'] = self.file_id
        result['op'] = self.op
        return result

    def from_map(self, map={}):
        self.current_category = map.get('current_category')
        if map.get('file') is not None:
            temp_model = BaseFileResponse()
            self.file = temp_model.from_map(map['file'])
        else:
            self.file = None
        self.file_id = map.get('file_id')
        self.op = map.get('op')
        return self


class GetAccessTokenByLinkInfoRequest(TeaModel):
    """
    *
    """
    def __init__(self, headers=None, extra=None, identity=None, type=None):
        self.headers = headers  # type: dict
        # 额外的信息，比如type为mobile时，此字段为国家编号，不填默认86
        self.extra = extra  # type: str
        # 唯一身份标识
        self.identity = identity  # type: str
        # 认证类型
        self.type = type  # type: str

    def validate(self):
        self.validate_required(self.identity, 'identity')
        self.validate_required(self.type, 'type')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['extra'] = self.extra
        result['identity'] = self.identity
        result['type'] = self.type
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.extra = map.get('extra')
        self.identity = map.get('identity')
        self.type = map.get('type')
        return self


class GetAppPublicKeyRequest(TeaModel):
    """
    *
    """
    def __init__(self, headers=None, app_id=None):
        self.headers = headers  # type: dict
        # App ID
        self.app_id = app_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['app_id'] = self.app_id
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
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
        self.message = message  # type: str
        # state
        self.state = state  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['async_task_id'] = self.async_task_id
        result['message'] = self.message
        result['state'] = self.state
        return result

    def from_map(self, map={}):
        self.async_task_id = map.get('async_task_id')
        self.message = map.get('message')
        self.state = map.get('state')
        return self


class GetByLinkInfoRequest(TeaModel):
    """
    *
    """
    def __init__(self, headers=None, extra=None, identity=None, type=None):
        self.headers = headers  # type: dict
        # 额外的信息，比如type为mobile时，此字段为国家编号，不填默认86
        self.extra = extra  # type: str
        # 唯一身份标识
        self.identity = identity  # type: str
        # 认证类型
        self.type = type  # type: str

    def validate(self):
        self.validate_required(self.identity, 'identity')
        self.validate_required(self.type, 'type')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['extra'] = self.extra
        result['identity'] = self.identity
        result['type'] = self.type
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.extra = map.get('extra')
        self.identity = map.get('identity')
        self.type = map.get('type')
        return self


class GetCaptchaRequest(TeaModel):
    """
    *
    """
    def __init__(self, headers=None, app_id=None):
        self.headers = headers  # type: dict
        # App ID, 当前访问的App
        self.app_id = app_id  # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['app_id'] = self.app_id
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.app_id = map.get('app_id')
        return self


class GetDownloadUrlResponse(TeaModel):
    """
    获取download url response
    """
    def __init__(self, expiration=None, method=None, ratelimit=None, size=None, streams_url=None, url=None):
        # expiration
        self.expiration = expiration  # type: str
        # method
        self.method = method  # type: str
        self.ratelimit = ratelimit  # type: RateLimit
        # size
        self.size = size  # type: int
        # streams url info
        self.streams_url = streams_url  # type: dict
        # url
        self.url = url  # type: str

    def validate(self):
        if self.ratelimit:
            self.ratelimit.validate()

    def to_map(self):
        result = {}
        result['expiration'] = self.expiration
        result['method'] = self.method
        if self.ratelimit is not None:
            result['ratelimit'] = self.ratelimit.to_map()
        else:
            result['ratelimit'] = None
        result['size'] = self.size
        result['streams_url'] = self.streams_url
        result['url'] = self.url
        return result

    def from_map(self, map={}):
        self.expiration = map.get('expiration')
        self.method = map.get('method')
        if map.get('ratelimit') is not None:
            temp_model = RateLimit()
            self.ratelimit = temp_model.from_map(map['ratelimit'])
        else:
            self.ratelimit = None
        self.size = map.get('size')
        self.streams_url = map.get('streams_url')
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
        self.creator = creator  # type: str
        # Drive 备注信息
        self.description = description  # type: str
        # Domain ID
        self.domain_id = domain_id  # type: str
        # Drive ID
        self.drive_id = drive_id  # type: str
        # Drive 名称
        self.drive_name = drive_name  # type: str
        # Drive 类型
        self.drive_type = drive_type  # type: str
        self.encrypt_data_access = encrypt_data_access  # type: bool
        self.encrypt_mode = encrypt_mode  # type: str
        # Drive 所有者
        self.owner = owner  # type: str
        # Drive存储基于store的相对路径，domain的PathType为OSSPath时返回
        self.relative_path = relative_path  # type: str
        # Drive 状态
        self.status = status  # type: str
        # 存储 ID, domain的PathType为OSSPath时返回
        self.store_id = store_id  # type: str
        # Drive 空间总量
        self.total_size = total_size  # type: int
        # Drive 空间已使用量
        self.used_size = used_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['creator'] = self.creator
        result['description'] = self.description
        result['domain_id'] = self.domain_id
        result['drive_id'] = self.drive_id
        result['drive_name'] = self.drive_name
        result['drive_type'] = self.drive_type
        result['encrypt_data_access'] = self.encrypt_data_access
        result['encrypt_mode'] = self.encrypt_mode
        result['owner'] = self.owner
        result['relative_path'] = self.relative_path
        result['status'] = self.status
        result['store_id'] = self.store_id
        result['total_size'] = self.total_size
        result['used_size'] = self.used_size
        return result

    def from_map(self, map={}):
        self.creator = map.get('creator')
        self.description = map.get('description')
        self.domain_id = map.get('domain_id')
        self.drive_id = map.get('drive_id')
        self.drive_name = map.get('drive_name')
        self.drive_type = map.get('drive_type')
        self.encrypt_data_access = map.get('encrypt_data_access')
        self.encrypt_mode = map.get('encrypt_mode')
        self.owner = map.get('owner')
        self.relative_path = map.get('relative_path')
        self.status = map.get('status')
        self.store_id = map.get('store_id')
        self.total_size = map.get('total_size')
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
        self.category = category  # type: str
        # Content Hash
        self.content_hash = content_hash  # type: str
        # content_hash_name
        self.content_hash_name = content_hash_name  # type: str
        # content_type
        self.content_type = content_type  # type: str
        # crc64_hash
        self.crc_64hash = crc_64hash  # type: str
        # created_at
        self.created_at = created_at  # type: str
        # description
        self.description = description  # type: str
        # DomainID
        self.domain_id = domain_id  # type: str
        # download_url
        self.download_url = download_url  # type: str
        # drive_id
        self.drive_id = drive_id  # type: str
        # encrypt_mode
        self.encrypt_mode = encrypt_mode  # type: str
        # file_extension
        self.file_extension = file_extension  # type: str
        # file_id
        self.file_id = file_id  # type: str
        # Hidden
        # type: boolean
        self.hidden = hidden  # type: bool
        self.image_media_metadata = image_media_metadata  # type: ImageMediaResponse
        # labels
        self.labels = labels  # type: list
        self.meta = meta  # type: str
        # name
        self.name = name  # type: str
        # parent_file_id
        self.parent_file_id = parent_file_id  # type: str
        self.punish_flag = punish_flag  # type: int
        # Size
        self.size = size  # type: int
        # starred
        # type: boolean
        self.starred = starred  # type: bool
        # status
        self.status = status  # type: str
        # @Deprecated streams url info
        self.streams_info = streams_info  # type: dict
        # thumbnail
        self.thumbnail = thumbnail  # type: str
        # trashed_at
        self.trashed_at = trashed_at  # type: str
        # type
        self.type = type  # type: str
        # updated_at
        self.updated_at = updated_at  # type: str
        # upload_id
        self.upload_id = upload_id  # type: str
        # url
        self.url = url  # type: str
        # user_meta
        self.user_meta = user_meta  # type: str
        self.video_media_metadata = video_media_metadata  # type: VideoMediaResponse
        self.video_preview_metadata = video_preview_metadata  # type: VideoPreviewResponse

    def validate(self):
        if self.domain_id:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z]+')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.file_id:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9]{1,50}')
        if self.image_media_metadata:
            self.image_media_metadata.validate()
        self.validate_required(self.name, 'name')
        if self.name:
            self.validate_pattern(self.name, 'name', '[a-zA-Z0-9.-]{1,1000}')
        if self.parent_file_id:
            self.validate_max_length(self.parent_file_id, 'parent_file_id', 50)
            self.validate_pattern(self.parent_file_id, 'parent_file_id', '[a-z0-9]{1,50}')
        if self.video_media_metadata:
            self.video_media_metadata.validate()
        if self.video_preview_metadata:
            self.video_preview_metadata.validate()

    def to_map(self):
        result = {}
        result['category'] = self.category
        result['content_hash'] = self.content_hash
        result['content_hash_name'] = self.content_hash_name
        result['content_type'] = self.content_type
        result['crc64_hash'] = self.crc_64hash
        result['created_at'] = self.created_at
        result['description'] = self.description
        result['domain_id'] = self.domain_id
        result['download_url'] = self.download_url
        result['drive_id'] = self.drive_id
        result['encrypt_mode'] = self.encrypt_mode
        result['file_extension'] = self.file_extension
        result['file_id'] = self.file_id
        result['hidden'] = self.hidden
        if self.image_media_metadata is not None:
            result['image_media_metadata'] = self.image_media_metadata.to_map()
        else:
            result['image_media_metadata'] = None
        result['labels'] = self.labels
        result['meta'] = self.meta
        result['name'] = self.name
        result['parent_file_id'] = self.parent_file_id
        result['punish_flag'] = self.punish_flag
        result['size'] = self.size
        result['starred'] = self.starred
        result['status'] = self.status
        result['streams_info'] = self.streams_info
        result['thumbnail'] = self.thumbnail
        result['trashed_at'] = self.trashed_at
        result['type'] = self.type
        result['updated_at'] = self.updated_at
        result['upload_id'] = self.upload_id
        result['url'] = self.url
        result['user_meta'] = self.user_meta
        if self.video_media_metadata is not None:
            result['video_media_metadata'] = self.video_media_metadata.to_map()
        else:
            result['video_media_metadata'] = None
        if self.video_preview_metadata is not None:
            result['video_preview_metadata'] = self.video_preview_metadata.to_map()
        else:
            result['video_preview_metadata'] = None
        return result

    def from_map(self, map={}):
        self.category = map.get('category')
        self.content_hash = map.get('content_hash')
        self.content_hash_name = map.get('content_hash_name')
        self.content_type = map.get('content_type')
        self.crc_64hash = map.get('crc64_hash')
        self.created_at = map.get('created_at')
        self.description = map.get('description')
        self.domain_id = map.get('domain_id')
        self.download_url = map.get('download_url')
        self.drive_id = map.get('drive_id')
        self.encrypt_mode = map.get('encrypt_mode')
        self.file_extension = map.get('file_extension')
        self.file_id = map.get('file_id')
        self.hidden = map.get('hidden')
        if map.get('image_media_metadata') is not None:
            temp_model = ImageMediaResponse()
            self.image_media_metadata = temp_model.from_map(map['image_media_metadata'])
        else:
            self.image_media_metadata = None
        self.labels = map.get('labels')
        self.meta = map.get('meta')
        self.name = map.get('name')
        self.parent_file_id = map.get('parent_file_id')
        self.punish_flag = map.get('punish_flag')
        self.size = map.get('size')
        self.starred = map.get('starred')
        self.status = map.get('status')
        self.streams_info = map.get('streams_info')
        self.thumbnail = map.get('thumbnail')
        self.trashed_at = map.get('trashed_at')
        self.type = map.get('type')
        self.updated_at = map.get('updated_at')
        self.upload_id = map.get('upload_id')
        self.url = map.get('url')
        self.user_meta = map.get('user_meta')
        if map.get('video_media_metadata') is not None:
            temp_model = VideoMediaResponse()
            self.video_media_metadata = temp_model.from_map(map['video_media_metadata'])
        else:
            self.video_media_metadata = None
        if map.get('video_preview_metadata') is not None:
            temp_model = VideoPreviewResponse()
            self.video_preview_metadata = temp_model.from_map(map['video_preview_metadata'])
        else:
            self.video_preview_metadata = None
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
        self.category = category  # type: str
        # Content Hash
        self.content_hash = content_hash  # type: str
        # content_hash_name
        self.content_hash_name = content_hash_name  # type: str
        # content_type
        self.content_type = content_type  # type: str
        # crc64_hash
        self.crc_64hash = crc_64hash  # type: str
        # created_at
        self.created_at = created_at  # type: str
        # description
        self.description = description  # type: str
        # DomainID
        self.domain_id = domain_id  # type: str
        # download_url
        self.download_url = download_url  # type: str
        # drive_id
        self.drive_id = drive_id  # type: str
        # encrypt_mode
        self.encrypt_mode = encrypt_mode  # type: str
        # file_extension
        self.file_extension = file_extension  # type: str
        # file_id
        self.file_id = file_id  # type: str
        # Hidden
        # type: boolean
        self.hidden = hidden  # type: bool
        self.image_media_metadata = image_media_metadata  # type: ImageMediaResponse
        # labels
        self.labels = labels  # type: list
        self.meta = meta  # type: str
        # name
        self.name = name  # type: str
        # parent_file_id
        self.parent_file_id = parent_file_id  # type: str
        self.punish_flag = punish_flag  # type: int
        # Size
        self.size = size  # type: int
        # starred
        # type: boolean
        self.starred = starred  # type: bool
        # status
        self.status = status  # type: str
        # @Deprecated streams url info
        self.streams_info = streams_info  # type: dict
        # thumbnail
        self.thumbnail = thumbnail  # type: str
        # trashed_at
        self.trashed_at = trashed_at  # type: str
        # type
        self.type = type  # type: str
        # updated_at
        self.updated_at = updated_at  # type: str
        # upload_id
        self.upload_id = upload_id  # type: str
        # url
        self.url = url  # type: str
        # user_meta
        self.user_meta = user_meta  # type: str
        self.video_media_metadata = video_media_metadata  # type: VideoMediaResponse
        self.video_preview_metadata = video_preview_metadata  # type: VideoPreviewResponse

    def validate(self):
        if self.domain_id:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z]+')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.file_id:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9]{1,50}')
        if self.image_media_metadata:
            self.image_media_metadata.validate()
        self.validate_required(self.name, 'name')
        if self.name:
            self.validate_pattern(self.name, 'name', '[a-zA-Z0-9.-]{1,1000}')
        if self.parent_file_id:
            self.validate_max_length(self.parent_file_id, 'parent_file_id', 50)
            self.validate_pattern(self.parent_file_id, 'parent_file_id', '[a-z0-9]{1,50}')
        if self.video_media_metadata:
            self.video_media_metadata.validate()
        if self.video_preview_metadata:
            self.video_preview_metadata.validate()

    def to_map(self):
        result = {}
        result['category'] = self.category
        result['content_hash'] = self.content_hash
        result['content_hash_name'] = self.content_hash_name
        result['content_type'] = self.content_type
        result['crc64_hash'] = self.crc_64hash
        result['created_at'] = self.created_at
        result['description'] = self.description
        result['domain_id'] = self.domain_id
        result['download_url'] = self.download_url
        result['drive_id'] = self.drive_id
        result['encrypt_mode'] = self.encrypt_mode
        result['file_extension'] = self.file_extension
        result['file_id'] = self.file_id
        result['hidden'] = self.hidden
        if self.image_media_metadata is not None:
            result['image_media_metadata'] = self.image_media_metadata.to_map()
        else:
            result['image_media_metadata'] = None
        result['labels'] = self.labels
        result['meta'] = self.meta
        result['name'] = self.name
        result['parent_file_id'] = self.parent_file_id
        result['punish_flag'] = self.punish_flag
        result['size'] = self.size
        result['starred'] = self.starred
        result['status'] = self.status
        result['streams_info'] = self.streams_info
        result['thumbnail'] = self.thumbnail
        result['trashed_at'] = self.trashed_at
        result['type'] = self.type
        result['updated_at'] = self.updated_at
        result['upload_id'] = self.upload_id
        result['url'] = self.url
        result['user_meta'] = self.user_meta
        if self.video_media_metadata is not None:
            result['video_media_metadata'] = self.video_media_metadata.to_map()
        else:
            result['video_media_metadata'] = None
        if self.video_preview_metadata is not None:
            result['video_preview_metadata'] = self.video_preview_metadata.to_map()
        else:
            result['video_preview_metadata'] = None
        return result

    def from_map(self, map={}):
        self.category = map.get('category')
        self.content_hash = map.get('content_hash')
        self.content_hash_name = map.get('content_hash_name')
        self.content_type = map.get('content_type')
        self.crc_64hash = map.get('crc64_hash')
        self.created_at = map.get('created_at')
        self.description = map.get('description')
        self.domain_id = map.get('domain_id')
        self.download_url = map.get('download_url')
        self.drive_id = map.get('drive_id')
        self.encrypt_mode = map.get('encrypt_mode')
        self.file_extension = map.get('file_extension')
        self.file_id = map.get('file_id')
        self.hidden = map.get('hidden')
        if map.get('image_media_metadata') is not None:
            temp_model = ImageMediaResponse()
            self.image_media_metadata = temp_model.from_map(map['image_media_metadata'])
        else:
            self.image_media_metadata = None
        self.labels = map.get('labels')
        self.meta = map.get('meta')
        self.name = map.get('name')
        self.parent_file_id = map.get('parent_file_id')
        self.punish_flag = map.get('punish_flag')
        self.size = map.get('size')
        self.starred = map.get('starred')
        self.status = map.get('status')
        self.streams_info = map.get('streams_info')
        self.thumbnail = map.get('thumbnail')
        self.trashed_at = map.get('trashed_at')
        self.type = map.get('type')
        self.updated_at = map.get('updated_at')
        self.upload_id = map.get('upload_id')
        self.url = map.get('url')
        self.user_meta = map.get('user_meta')
        if map.get('video_media_metadata') is not None:
            temp_model = VideoMediaResponse()
            self.video_media_metadata = temp_model.from_map(map['video_media_metadata'])
        else:
            self.video_media_metadata = None
        if map.get('video_preview_metadata') is not None:
            temp_model = VideoPreviewResponse()
            self.video_preview_metadata = temp_model.from_map(map['video_preview_metadata'])
        else:
            self.video_preview_metadata = None
        return self


class GetLastCursorResponse(TeaModel):
    """
    get last file op cursor response
    """
    def __init__(self, cursor=None):
        self.cursor = cursor  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['cursor'] = self.cursor
        return result

    def from_map(self, map={}):
        self.cursor = map.get('cursor')
        return self


class GetLinkInfoByUserIDRequest(TeaModel):
    """
    *
    """
    def __init__(self, headers=None, user_id=None):
        self.headers = headers  # type: dict
        # user ID
        self.user_id = user_id  # type: str

    def validate(self):
        self.validate_required(self.user_id, 'user_id')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['user_id'] = self.user_id
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.user_id = map.get('user_id')
        return self


class GetMediaPlayURLResponse(TeaModel):
    """
    get_media_play_url response
    """
    def __init__(self, url=None):
        # url
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['url'] = self.url
        return result

    def from_map(self, map={}):
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
        result['access_token'] = self.access_token
        result['preview_url'] = self.preview_url
        return result

    def from_map(self, map={}):
        self.access_token = map.get('access_token')
        self.preview_url = map.get('preview_url')
        return self


class GetPublicKeyResponse(TeaModel):
    """
    *
    """
    def __init__(self, app_id=None, key_pair_id=None, public_key=None):
        # App ID
        self.app_id = app_id  # type: str
        self.key_pair_id = key_pair_id  # type: str
        # RSA加密算法的公钥, PEM格式
        self.public_key = public_key  # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.public_key, 'public_key')

    def to_map(self):
        result = {}
        result['app_id'] = self.app_id
        result['key_pair_id'] = self.key_pair_id
        result['public_key'] = self.public_key
        return result

    def from_map(self, map={}):
        self.app_id = map.get('app_id')
        self.key_pair_id = map.get('key_pair_id')
        self.public_key = map.get('public_key')
        return self


class GetShareLinkByAnonymousResponse(TeaModel):
    """
    get_share_link_by_anonymous response
    """
    def __init__(self, creator_id=None, creator_name=None, expiration=None, updated_at=None):
        # creator_id
        self.creator_id = creator_id  # type: str
        # creator_name
        self.creator_name = creator_name  # type: str
        # expiration
        self.expiration = expiration  # type: str
        # updated_at
        self.updated_at = updated_at  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['creator_id'] = self.creator_id
        result['creator_name'] = self.creator_name
        result['expiration'] = self.expiration
        result['updated_at'] = self.updated_at
        return result

    def from_map(self, map={}):
        self.creator_id = map.get('creator_id')
        self.creator_name = map.get('creator_name')
        self.expiration = map.get('expiration')
        self.updated_at = map.get('updated_at')
        return self


class GetShareLinkIDResponse(TeaModel):
    """
    get_share_id response
    """
    def __init__(self, share_id=None, share_pwd=None):
        # share_id
        self.share_id = share_id  # type: str
        # share_pwd
        self.share_pwd = share_pwd  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['share_id'] = self.share_id
        result['share_pwd'] = self.share_pwd
        return result

    def from_map(self, map={}):
        self.share_id = map.get('share_id')
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
        self.expires_in = expires_in  # type: int
        # share_token
        self.share_token = share_token  # type: str

    def validate(self):
        self.validate_required(self.expire_time, 'expire_time')
        self.validate_required(self.expires_in, 'expires_in')
        self.validate_required(self.share_token, 'share_token')

    def to_map(self):
        result = {}
        result['expire_time'] = self.expire_time
        result['expires_in'] = self.expires_in
        result['share_token'] = self.share_token
        return result

    def from_map(self, map={}):
        self.expire_time = map.get('expire_time')
        self.expires_in = map.get('expires_in')
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
        self.created_at = created_at  # type: str
        # creator
        self.creator = creator  # type: str
        # description
        self.description = description  # type: str
        # domain_id
        self.domain_id = domain_id  # type: str
        # drive_id
        self.drive_id = drive_id  # type: str
        # expiration
        self.expiration = expiration  # type: str
        # expired
        self.expired = expired  # type: bool
        # owner
        self.owner = owner  # type: str
        # permissions
        self.permissions = permissions  # type: list
        # share_path
        self.share_file_path = share_file_path  # type: str
        # share_id
        self.share_id = share_id  # type: str
        # share_name
        self.share_name = share_name  # type: str
        self.share_policy = share_policy  # type: list
        # status
        self.status = status  # type: str
        # updated_at
        self.updated_at = updated_at  # type: str

    def validate(self):
        if self.share_policy:
            for k in self.share_policy:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['created_at'] = self.created_at
        result['creator'] = self.creator
        result['description'] = self.description
        result['domain_id'] = self.domain_id
        result['drive_id'] = self.drive_id
        result['expiration'] = self.expiration
        result['expired'] = self.expired
        result['owner'] = self.owner
        result['permissions'] = self.permissions
        result['share_file_path'] = self.share_file_path
        result['share_id'] = self.share_id
        result['share_name'] = self.share_name
        result['share_policy'] = []
        if self.share_policy is not None:
            for k in self.share_policy:
                result['share_policy'].append(k.to_map() if k else None)
        else:
            result['share_policy'] = None
        result['status'] = self.status
        result['updated_at'] = self.updated_at
        return result

    def from_map(self, map={}):
        self.created_at = map.get('created_at')
        self.creator = map.get('creator')
        self.description = map.get('description')
        self.domain_id = map.get('domain_id')
        self.drive_id = map.get('drive_id')
        self.expiration = map.get('expiration')
        self.expired = map.get('expired')
        self.owner = map.get('owner')
        self.permissions = map.get('permissions')
        self.share_file_path = map.get('share_file_path')
        self.share_id = map.get('share_id')
        self.share_name = map.get('share_name')
        self.share_policy = []
        if map.get('share_policy') is not None:
            for k in map.get('share_policy'):
                temp_model = SharePermissionPolicy()
                self.share_policy.append(temp_model.from_map(k))
        else:
            self.share_policy = None
        self.status = map.get('status')
        self.updated_at = map.get('updated_at')
        return self


class GetUploadUrlResponse(TeaModel):
    """
    Get UploadUrl Response
    """
    def __init__(self, create_at=None, domain_id=None, drive_id=None, file_id=None, part_info_list=None,
                 upload_id=None):
        # created_at
        self.create_at = create_at  # type: str
        # domain_id
        self.domain_id = domain_id  # type: str
        # drive_id
        self.drive_id = drive_id  # type: str
        # file_id
        self.file_id = file_id  # type: str
        # part_info_list
        self.part_info_list = part_info_list  # type: list
        # upload_id
        self.upload_id = upload_id  # type: str

    def validate(self):
        if self.domain_id:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z]+')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.file_id:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9]{1,50}')
        if self.part_info_list:
            for k in self.part_info_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['create_at'] = self.create_at
        result['domain_id'] = self.domain_id
        result['drive_id'] = self.drive_id
        result['file_id'] = self.file_id
        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k in self.part_info_list:
                result['part_info_list'].append(k.to_map() if k else None)
        else:
            result['part_info_list'] = None
        result['upload_id'] = self.upload_id
        return result

    def from_map(self, map={}):
        self.create_at = map.get('create_at')
        self.domain_id = map.get('domain_id')
        self.drive_id = map.get('drive_id')
        self.file_id = map.get('file_id')
        self.part_info_list = []
        if map.get('part_info_list') is not None:
            for k in map.get('part_info_list'):
                temp_model = UploadPartInfo()
                self.part_info_list.append(temp_model.from_map(k))
        else:
            self.part_info_list = None
        self.upload_id = map.get('upload_id')
        return self


class GetVideoPreviewSpriteURLResponse(TeaModel):
    """
    获取视频雪碧图地址 url response
    """
    def __init__(self, col=None, count=None, frame_count=None, frame_height=None, frame_width=None, row=None,
                 sprite_url_list=None):
        # col
        self.col = col  # type: int
        # count
        self.count = count  # type: int
        # frame_count
        self.frame_count = frame_count  # type: int
        # frame_height
        self.frame_height = frame_height  # type: int
        # frame_width
        self.frame_width = frame_width  # type: int
        # row
        self.row = row  # type: int
        # sprite_url_list
        self.sprite_url_list = sprite_url_list  # type: list

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['col'] = self.col
        result['count'] = self.count
        result['frame_count'] = self.frame_count
        result['frame_height'] = self.frame_height
        result['frame_width'] = self.frame_width
        result['row'] = self.row
        result['sprite_url_list'] = self.sprite_url_list
        return result

    def from_map(self, map={}):
        self.col = map.get('col')
        self.count = map.get('count')
        self.frame_count = map.get('frame_count')
        self.frame_height = map.get('frame_height')
        self.frame_width = map.get('frame_width')
        self.row = map.get('row')
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
        result['preview_url'] = self.preview_url
        return result

    def from_map(self, map={}):
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
        self.city = city  # type: str
        # country
        self.country = country  # type: str
        # cropping_suggestion
        self.cropping_suggestion = cropping_suggestion  # type: list
        # district
        self.district = district  # type: str
        # exif json string
        self.exif = exif  # type: str
        # faces json string
        self.faces = faces  # type: str
        # height
        self.height = height  # type: int
        self.image_quality = image_quality  # type: ImageQuality
        # system_tags
        self.image_tags = image_tags  # type: list
        # location
        self.location = location  # type: str
        # province
        self.province = province  # type: str
        # story_image_score
        self.story_image_score = story_image_score  # type: int
        # time
        self.time = time  # type: str
        # township
        self.township = township  # type: str
        # width
        self.width = width  # type: int

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
        result['address_line'] = self.address_line
        result['city'] = self.city
        result['country'] = self.country
        result['cropping_suggestion'] = []
        if self.cropping_suggestion is not None:
            for k in self.cropping_suggestion:
                result['cropping_suggestion'].append(k.to_map() if k else None)
        else:
            result['cropping_suggestion'] = None
        result['district'] = self.district
        result['exif'] = self.exif
        result['faces'] = self.faces
        result['height'] = self.height
        if self.image_quality is not None:
            result['image_quality'] = self.image_quality.to_map()
        else:
            result['image_quality'] = None
        result['image_tags'] = []
        if self.image_tags is not None:
            for k in self.image_tags:
                result['image_tags'].append(k.to_map() if k else None)
        else:
            result['image_tags'] = None
        result['location'] = self.location
        result['province'] = self.province
        result['story_image_score'] = self.story_image_score
        result['time'] = self.time
        result['township'] = self.township
        result['width'] = self.width
        return result

    def from_map(self, map={}):
        self.address_line = map.get('address_line')
        self.city = map.get('city')
        self.country = map.get('country')
        self.cropping_suggestion = []
        if map.get('cropping_suggestion') is not None:
            for k in map.get('cropping_suggestion'):
                temp_model = CroppingSuggestionItem()
                self.cropping_suggestion.append(temp_model.from_map(k))
        else:
            self.cropping_suggestion = None
        self.district = map.get('district')
        self.exif = map.get('exif')
        self.faces = map.get('faces')
        self.height = map.get('height')
        if map.get('image_quality') is not None:
            temp_model = ImageQuality()
            self.image_quality = temp_model.from_map(map['image_quality'])
        else:
            self.image_quality = None
        self.image_tags = []
        if map.get('image_tags') is not None:
            for k in map.get('image_tags'):
                temp_model = SystemTag()
                self.image_tags.append(temp_model.from_map(k))
        else:
            self.image_tags = None
        self.location = map.get('location')
        self.province = map.get('province')
        self.story_image_score = map.get('story_image_score')
        self.time = map.get('time')
        self.township = map.get('township')
        self.width = map.get('width')
        return self


class ImageQuality(TeaModel):
    """
    *
    """
    def __init__(self, clarity=None, clarity_score=None, color=None, color_score=None, composition_score=None,
                 contrast=None, contrast_score=None, exposure=None, exposure_score=None, overall_score=None):
        self.clarity = clarity  # type: int
        self.clarity_score = clarity_score  # type: int
        self.color = color  # type: int
        self.color_score = color_score  # type: int
        self.composition_score = composition_score  # type: int
        self.contrast = contrast  # type: int
        self.contrast_score = contrast_score  # type: int
        self.exposure = exposure  # type: int
        self.exposure_score = exposure_score  # type: int
        self.overall_score = overall_score  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['clarity'] = self.clarity
        result['clarity_score'] = self.clarity_score
        result['color'] = self.color
        result['color_score'] = self.color_score
        result['composition_score'] = self.composition_score
        result['contrast'] = self.contrast
        result['contrast_score'] = self.contrast_score
        result['exposure'] = self.exposure
        result['exposure_score'] = self.exposure_score
        result['overall_score'] = self.overall_score
        return result

    def from_map(self, map={}):
        self.clarity = map.get('clarity')
        self.clarity_score = map.get('clarity_score')
        self.color = map.get('color')
        self.color_score = map.get('color_score')
        self.composition_score = map.get('composition_score')
        self.contrast = map.get('contrast')
        self.contrast_score = map.get('contrast_score')
        self.exposure = map.get('exposure')
        self.exposure_score = map.get('exposure_score')
        self.overall_score = map.get('overall_score')
        return self


class LinkInfo(TeaModel):
    """
    *
    """
    def __init__(self, extra=None, identity=None, type=None):
        # 额外的信息，比如type为mobile时，此字段为国家编号，不填默认86
        self.extra = extra  # type: str
        # 当前用户已存在的登录标识
        self.identity = identity  # type: str
        # 当前用户已存在的登录方式
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['extra'] = self.extra
        result['identity'] = self.identity
        result['type'] = self.type
        return result

    def from_map(self, map={}):
        self.extra = map.get('extra')
        self.identity = map.get('identity')
        self.type = map.get('type')
        return self


class LinkInfoListResponse(TeaModel):
    """
    *
    """
    def __init__(self, items=None):
        # items
        self.items = items  # type: list

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
        else:
            result['items'] = None
        return result

    def from_map(self, map={}):
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = LinkInfoResponse()
                self.items.append(temp_model.from_map(k))
        else:
            self.items = None
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
        self.created_at = created_at  # type: int
        # Domain ID
        self.domain_id = domain_id  # type: str
        # 额外的信息，比如type为mobile时，此字段为国家编号，不填默认86
        self.extra = extra  # type: str
        # 唯一身份标识
        self.identity = identity  # type: str
        # 最后登录时间
        self.last_login_time = last_login_time  # type: int
        # 状态
        self.status = status  # type: str
        # 用户ID
        self.user_id = user_id  # type: str

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
        result['authentication_type'] = self.authentication_type
        result['created_at'] = self.created_at
        result['domain_id'] = self.domain_id
        result['extra'] = self.extra
        result['identity'] = self.identity
        result['last_login_time'] = self.last_login_time
        result['status'] = self.status
        result['user_id'] = self.user_id
        return result

    def from_map(self, map={}):
        self.authentication_type = map.get('authentication_type')
        self.created_at = map.get('created_at')
        self.domain_id = map.get('domain_id')
        self.extra = map.get('extra')
        self.identity = map.get('identity')
        self.last_login_time = map.get('last_login_time')
        self.status = map.get('status')
        self.user_id = map.get('user_id')
        return self


class ListByAnonymousResponse(TeaModel):
    """
    list_file_by_anonymous response
    """
    def __init__(self, items=None, next_marker=None):
        # items
        self.items = items  # type: list
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
        else:
            result['items'] = None
        result['next_marker'] = self.next_marker
        return result

    def from_map(self, map={}):
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = BaseFileAnonymousResponse()
                self.items.append(temp_model.from_map(k))
        else:
            self.items = None
        self.next_marker = map.get('next_marker')
        return self


class ListDriveResponse(TeaModel):
    """
    list drive response
    """
    def __init__(self, items=None, next_marker=None):
        # Drive 列表
        self.items = items  # type: list
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
        else:
            result['items'] = None
        result['next_marker'] = self.next_marker
        return result

    def from_map(self, map={}):
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = BaseDriveResponse()
                self.items.append(temp_model.from_map(k))
        else:
            self.items = None
        self.next_marker = map.get('next_marker')
        return self


class ListFileDeltaResponse(TeaModel):
    """
    list file op response
    """
    def __init__(self, cursor=None, has_more=None, items=None):
        # cursor
        self.cursor = cursor  # type: str
        # has_more
        self.has_more = has_more  # type: bool
        # items
        self.items = items  # type: list

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['cursor'] = self.cursor
        result['has_more'] = self.has_more
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        else:
            result['items'] = None
        return result

    def from_map(self, map={}):
        self.cursor = map.get('cursor')
        self.has_more = map.get('has_more')
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = FileDeltaResponse()
                self.items.append(temp_model.from_map(k))
        else:
            self.items = None
        return self


class ListFileResponse(TeaModel):
    """
    List file response
    """
    def __init__(self, items=None, next_marker=None):
        # items
        self.items = items  # type: list
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
        else:
            result['items'] = None
        result['next_marker'] = self.next_marker
        return result

    def from_map(self, map={}):
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = BaseFileResponse()
                self.items.append(temp_model.from_map(k))
        else:
            self.items = None
        self.next_marker = map.get('next_marker')
        return self


class ListShareLinkResponse(TeaModel):
    """
    list_share_link response
    """
    def __init__(self, items=None, next_marker=None):
        # items
        self.items = items  # type: list
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
        else:
            result['items'] = None
        result['next_marker'] = self.next_marker
        return result

    def from_map(self, map={}):
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = BaseShareLinkResponse()
                self.items.append(temp_model.from_map(k))
        else:
            self.items = None
        self.next_marker = map.get('next_marker')
        return self


class ListShareResponse(TeaModel):
    """
    List share response
    """
    def __init__(self, items=None, next_marker=None):
        # items
        self.items = items  # type: list
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
        else:
            result['items'] = None
        result['next_marker'] = self.next_marker
        return result

    def from_map(self, map={}):
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = BaseShareResponse()
                self.items.append(temp_model.from_map(k))
        else:
            self.items = None
        self.next_marker = map.get('next_marker')
        return self


class ListStoreFileResponse(TeaModel):
    """
    List storage file
    """
    def __init__(self, items=None, next_marker=None):
        # items
        # file list
        self.items = items  # type: list
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
        else:
            result['items'] = None
        result['next_marker'] = self.next_marker
        return result

    def from_map(self, map={}):
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = StoreFile()
                self.items.append(temp_model.from_map(k))
        else:
            self.items = None
        self.next_marker = map.get('next_marker')
        return self


class ListStoreResponse(TeaModel):
    """
    List storage
    """
    def __init__(self, items=None):
        # items
        self.items = items  # type: list

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
        else:
            result['items'] = None
        return result

    def from_map(self, map={}):
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = StoreItemResponse()
                self.items.append(temp_model.from_map(k))
        else:
            self.items = None
        return self


class ListUploadedPartResponse(TeaModel):
    """
    获取签名 response
    """
    def __init__(self, file_id=None, next_part_number_marker=None, upload_id=None, uploaded_parts=None):
        # file_id
        self.file_id = file_id  # type: str
        # next_part_number_marker
        self.next_part_number_marker = next_part_number_marker  # type: str
        # upload_id
        self.upload_id = upload_id  # type: str
        # uploaded_parts
        self.uploaded_parts = uploaded_parts  # type: list

    def validate(self):
        if self.file_id:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9]{1,50}')
        if self.uploaded_parts:
            for k in self.uploaded_parts:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['file_id'] = self.file_id
        result['next_part_number_marker'] = self.next_part_number_marker
        result['upload_id'] = self.upload_id
        result['uploaded_parts'] = []
        if self.uploaded_parts is not None:
            for k in self.uploaded_parts:
                result['uploaded_parts'].append(k.to_map() if k else None)
        else:
            result['uploaded_parts'] = None
        return result

    def from_map(self, map={}):
        self.file_id = map.get('file_id')
        self.next_part_number_marker = map.get('next_part_number_marker')
        self.upload_id = map.get('upload_id')
        self.uploaded_parts = []
        if map.get('uploaded_parts') is not None:
            for k in map.get('uploaded_parts'):
                temp_model = UploadPartInfo()
                self.uploaded_parts.append(temp_model.from_map(k))
        else:
            self.uploaded_parts = None
        return self


class LoginByCodeRequest(TeaModel):
    """
    *
    """
    def __init__(self, access_token=None, app_id=None, auth_code=None, type=None):
        # 鉴权后返回的accessToken，淘宝登录需要此字段
        self.access_token = access_token  # type: str
        # App ID, 当前访问的App
        self.app_id = app_id  # type: str
        # 鉴权后返回的AuthCode，支付宝登录需要此字段
        self.auth_code = auth_code  # type: str
        # 鉴权类型，淘宝、支付宝
        self.type = type  # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.type, 'type')

    def to_map(self):
        result = {}
        result['access_token'] = self.access_token
        result['app_id'] = self.app_id
        result['auth_code'] = self.auth_code
        result['type'] = self.type
        return result

    def from_map(self, map={}):
        self.access_token = map.get('access_token')
        self.app_id = map.get('app_id')
        self.auth_code = map.get('auth_code')
        self.type = map.get('type')
        return self


class MobileCheckExistRequest(TeaModel):
    """
    *
    """
    def __init__(self, headers=None, app_id=None, phone_number=None, phone_region=None):
        self.headers = headers  # type: dict
        # App ID, 当前访问的App
        self.app_id = app_id  # type: str
        # 待查询的手机号
        self.phone_number = phone_number  # type: str
        # 国家编号，默认86，不需要填+号，直接填数字
        self.phone_region = phone_region  # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.phone_number, 'phone_number')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['app_id'] = self.app_id
        result['phone_number'] = self.phone_number
        result['phone_region'] = self.phone_region
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.app_id = map.get('app_id')
        self.phone_number = map.get('phone_number')
        self.phone_region = map.get('phone_region')
        return self


class MobileCheckExistResponse(TeaModel):
    """
    *
    """
    def __init__(self, is_exist=None, phone_number=None, phone_region=None):
        # 当前手机号是否存在
        self.is_exist = is_exist  # type: bool
        # 待查询的手机号
        self.phone_number = phone_number  # type: str
        # 国家编号，默认86，不需要填+号，直接填数字
        self.phone_region = phone_region  # type: str

    def validate(self):
        self.validate_required(self.is_exist, 'is_exist')
        self.validate_required(self.phone_number, 'phone_number')

    def to_map(self):
        result = {}
        result['is_exist'] = self.is_exist
        result['phone_number'] = self.phone_number
        result['phone_region'] = self.phone_region
        return result

    def from_map(self, map={}):
        self.is_exist = map.get('is_exist')
        self.phone_number = map.get('phone_number')
        self.phone_region = map.get('phone_region')
        return self


class MobileLoginRequest(TeaModel):
    """
    *
    """
    def __init__(self, headers=None, app_id=None, auto_register=None, captcha_id=None, captcha_text=None,
                 encrypted_key=None, password=None, phone_number=None, phone_region=None, sms_code=None, sms_code_id=None):
        self.headers = headers  # type: dict
        # App ID, 当前访问的App
        self.app_id = app_id  # type: str
        # 是否自动注册用户，使用密码登录此参数不生效
        self.auto_register = auto_register  # type: bool
        # 图片验证码ID, 密码登录需要此参数
        self.captcha_id = captcha_id  # type: str
        # 用户输入的验证码值, 密码登录需要此参数
        self.captcha_text = captcha_text  # type: str
        # AES-256对称加密密钥，通过App公钥加密后传输
        self.encrypted_key = encrypted_key  # type: str
        # 登录密码, 传入此参数则忽略短信验证码，不传此参数则默认使用短信登录。
        self.password = password  # type: str
        # 待查询的手机号
        self.phone_number = phone_number  # type: str
        # 国家编号，默认86，不需要填+号，直接填数字
        self.phone_region = phone_region  # type: str
        # 短信验证码内容，使用密码登录此参数不生效
        self.sms_code = sms_code  # type: str
        # 短信验证码ID，使用密码登录此参数不生效
        self.sms_code_id = sms_code_id  # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.phone_number, 'phone_number')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['app_id'] = self.app_id
        result['auto_register'] = self.auto_register
        result['captcha_id'] = self.captcha_id
        result['captcha_text'] = self.captcha_text
        result['encrypted_key'] = self.encrypted_key
        result['password'] = self.password
        result['phone_number'] = self.phone_number
        result['phone_region'] = self.phone_region
        result['sms_code'] = self.sms_code
        result['sms_code_id'] = self.sms_code_id
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.app_id = map.get('app_id')
        self.auto_register = map.get('auto_register')
        self.captcha_id = map.get('captcha_id')
        self.captcha_text = map.get('captcha_text')
        self.encrypted_key = map.get('encrypted_key')
        self.password = map.get('password')
        self.phone_number = map.get('phone_number')
        self.phone_region = map.get('phone_region')
        self.sms_code = map.get('sms_code')
        self.sms_code_id = map.get('sms_code_id')
        return self


class MobileRegisterRequest(TeaModel):
    """
    *
    """
    def __init__(self, headers=None, app_id=None, phone_number=None, phone_region=None, sms_code=None,
                 sms_code_id=None):
        self.headers = headers  # type: dict
        # App ID, 当前访问的App
        self.app_id = app_id  # type: str
        # 待查询的手机号
        self.phone_number = phone_number  # type: str
        # 国家编号，默认86，不需要填+号，直接填数字
        self.phone_region = phone_region  # type: str
        # 短信验证码内容
        self.sms_code = sms_code  # type: str
        # 短信验证码ID
        self.sms_code_id = sms_code_id  # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.phone_number, 'phone_number')
        self.validate_required(self.sms_code, 'sms_code')
        self.validate_required(self.sms_code_id, 'sms_code_id')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['app_id'] = self.app_id
        result['phone_number'] = self.phone_number
        result['phone_region'] = self.phone_region
        result['sms_code'] = self.sms_code
        result['sms_code_id'] = self.sms_code_id
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.app_id = map.get('app_id')
        self.phone_number = map.get('phone_number')
        self.phone_region = map.get('phone_region')
        self.sms_code = map.get('sms_code')
        self.sms_code_id = map.get('sms_code_id')
        return self


class MobileSendSmsCodeRequest(TeaModel):
    """
    *
    """
    def __init__(self, headers=None, app_id=None, captcha_id=None, captcha_text=None, phone_number=None,
                 phone_region=None, type=None):
        self.headers = headers  # type: dict
        # App ID, 当前访问的App
        self.app_id = app_id  # type: str
        # 图片验证码ID
        self.captcha_id = captcha_id  # type: str
        # 用户输入的验证码值
        self.captcha_text = captcha_text  # type: str
        # 待发送验证短信的手机号
        self.phone_number = phone_number  # type: str
        # 国家编号，默认86，不需要填+号，直接填数字
        self.phone_region = phone_region  # type: str
        # 验证码用途, 可下发: login、register、change_password
        self.type = type  # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.phone_number, 'phone_number')
        self.validate_required(self.type, 'type')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['app_id'] = self.app_id
        result['captcha_id'] = self.captcha_id
        result['captcha_text'] = self.captcha_text
        result['phone_number'] = self.phone_number
        result['phone_region'] = self.phone_region
        result['type'] = self.type
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.app_id = map.get('app_id')
        self.captcha_id = map.get('captcha_id')
        self.captcha_text = map.get('captcha_text')
        self.phone_number = map.get('phone_number')
        self.phone_region = map.get('phone_region')
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
        result['sms_code_id'] = self.sms_code_id
        return result

    def from_map(self, map={}):
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
        self.domain_id = domain_id  # type: str
        # drive_id
        self.drive_id = drive_id  # type: str
        # file_id
        self.file_id = file_id  # type: str

    def validate(self):
        if self.domain_id:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z]+')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.file_id:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9]{1,50}')

    def to_map(self):
        result = {}
        result['async_task_id'] = self.async_task_id
        result['domain_id'] = self.domain_id
        result['drive_id'] = self.drive_id
        result['file_id'] = self.file_id
        return result

    def from_map(self, map={}):
        self.async_task_id = map.get('async_task_id')
        self.domain_id = map.get('domain_id')
        self.drive_id = map.get('drive_id')
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
        self.crc = crc  # type: str
        # crc64_hash
        self.crc_64hash = crc_64hash  # type: str
        # created_at
        self.created_at = created_at  # type: str
        # description
        self.description = description  # type: str
        # domain_id
        self.domain_id = domain_id  # type: str
        # download_url
        self.download_url = download_url  # type: str
        # drive_id
        self.drive_id = drive_id  # type: str
        # file_extension
        self.file_extension = file_extension  # type: str
        # file_path
        self.file_path = file_path  # type: str
        # name
        self.name = name  # type: str
        # parent_file_id
        self.parent_file_path = parent_file_path  # type: str
        # share_id
        self.share_id = share_id  # type: str
        # Size
        self.size = size  # type: int
        # status
        self.status = status  # type: str
        # thumbnail
        self.thumbnail = thumbnail  # type: str
        # trashed_at
        self.trashed_at = trashed_at  # type: str
        # type
        self.type = type  # type: str
        # updated_at
        self.updated_at = updated_at  # type: str
        # upload_id
        self.upload_id = upload_id  # type: str
        # url
        self.url = url  # type: str

    def validate(self):
        if self.domain_id:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z]+')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.name, 'name')
        if self.name:
            self.validate_pattern(self.name, 'name', '[a-zA-Z0-9.-]{1,1000}')
        if self.parent_file_path:
            self.validate_max_length(self.parent_file_path, 'parent_file_path', 50)
            self.validate_pattern(self.parent_file_path, 'parent_file_path', '[a-z0-9]{1,50}')
        if self.share_id:
            self.validate_pattern(self.share_id, 'share_id', '[0-9]+')

    def to_map(self):
        result = {}
        result['content_hash'] = self.content_hash
        result['content_hash_name'] = self.content_hash_name
        result['content_type'] = self.content_type
        result['crc'] = self.crc
        result['crc64_hash'] = self.crc_64hash
        result['created_at'] = self.created_at
        result['description'] = self.description
        result['domain_id'] = self.domain_id
        result['download_url'] = self.download_url
        result['drive_id'] = self.drive_id
        result['file_extension'] = self.file_extension
        result['file_path'] = self.file_path
        result['name'] = self.name
        result['parent_file_path'] = self.parent_file_path
        result['share_id'] = self.share_id
        result['size'] = self.size
        result['status'] = self.status
        result['thumbnail'] = self.thumbnail
        result['trashed_at'] = self.trashed_at
        result['type'] = self.type
        result['updated_at'] = self.updated_at
        result['upload_id'] = self.upload_id
        result['url'] = self.url
        return result

    def from_map(self, map={}):
        self.content_hash = map.get('content_hash')
        self.content_hash_name = map.get('content_hash_name')
        self.content_type = map.get('content_type')
        self.crc = map.get('crc')
        self.crc_64hash = map.get('crc64_hash')
        self.created_at = map.get('created_at')
        self.description = map.get('description')
        self.domain_id = map.get('domain_id')
        self.download_url = map.get('download_url')
        self.drive_id = map.get('drive_id')
        self.file_extension = map.get('file_extension')
        self.file_path = map.get('file_path')
        self.name = map.get('name')
        self.parent_file_path = map.get('parent_file_path')
        self.share_id = map.get('share_id')
        self.size = map.get('size')
        self.status = map.get('status')
        self.thumbnail = map.get('thumbnail')
        self.trashed_at = map.get('trashed_at')
        self.type = map.get('type')
        self.updated_at = map.get('updated_at')
        self.upload_id = map.get('upload_id')
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
        self.domain_id = domain_id  # type: str
        # drive_id
        self.drive_id = drive_id  # type: str
        # file_path
        self.file_path = file_path  # type: str
        # drive_id
        self.share_id = share_id  # type: str

    def validate(self):
        if self.domain_id:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z-]+')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.share_id:
            self.validate_pattern(self.share_id, 'share_id', '[a-z0-9A-Z]+')

    def to_map(self):
        result = {}
        result['async_task_id'] = self.async_task_id
        result['domain_id'] = self.domain_id
        result['drive_id'] = self.drive_id
        result['file_path'] = self.file_path
        result['share_id'] = self.share_id
        return result

    def from_map(self, map={}):
        self.async_task_id = map.get('async_task_id')
        self.domain_id = map.get('domain_id')
        self.drive_id = map.get('drive_id')
        self.file_path = map.get('file_path')
        self.share_id = map.get('share_id')
        return self


class OSSCreateFileResponse(TeaModel):
    """
    Create file response
    """
    def __init__(self, domain_id=None, drive_id=None, file_path=None, part_info_list=None, share_id=None, type=None,
                 upload_id=None):
        # domain_id
        self.domain_id = domain_id  # type: str
        # drive_id
        self.drive_id = drive_id  # type: str
        # file_path
        self.file_path = file_path  # type: str
        # part_info_list
        self.part_info_list = part_info_list  # type: list
        # share_id
        self.share_id = share_id  # type: str
        # type
        self.type = type  # type: str
        # upload_id
        self.upload_id = upload_id  # type: str

    def validate(self):
        if self.domain_id:
            self.validate_max_length(self.domain_id, 'domain_id', 50)
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9]{1,50}')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.part_info_list:
            for k in self.part_info_list:
                if k:
                    k.validate()
        if self.share_id:
            self.validate_pattern(self.share_id, 'share_id', '[0-9]+')

    def to_map(self):
        result = {}
        result['domain_id'] = self.domain_id
        result['drive_id'] = self.drive_id
        result['file_path'] = self.file_path
        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k in self.part_info_list:
                result['part_info_list'].append(k.to_map() if k else None)
        else:
            result['part_info_list'] = None
        result['share_id'] = self.share_id
        result['type'] = self.type
        result['upload_id'] = self.upload_id
        return result

    def from_map(self, map={}):
        self.domain_id = map.get('domain_id')
        self.drive_id = map.get('drive_id')
        self.file_path = map.get('file_path')
        self.part_info_list = []
        if map.get('part_info_list') is not None:
            for k in map.get('part_info_list'):
                temp_model = UploadPartInfo()
                self.part_info_list.append(temp_model.from_map(k))
        else:
            self.part_info_list = None
        self.share_id = map.get('share_id')
        self.type = map.get('type')
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
        self.domain_id = domain_id  # type: str
        # drive_id
        self.drive_id = drive_id  # type: str
        # file_path
        self.file_path = file_path  # type: str
        # share_id
        self.share_id = share_id  # type: str

    def validate(self):
        if self.domain_id:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z]+')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.share_id:
            self.validate_pattern(self.share_id, 'share_id', '[a-z0-9A-Z]+')

    def to_map(self):
        result = {}
        result['async_task_id'] = self.async_task_id
        result['domain_id'] = self.domain_id
        result['drive_id'] = self.drive_id
        result['file_path'] = self.file_path
        result['share_id'] = self.share_id
        return result

    def from_map(self, map={}):
        self.async_task_id = map.get('async_task_id')
        self.domain_id = map.get('domain_id')
        self.drive_id = map.get('drive_id')
        self.file_path = map.get('file_path')
        self.share_id = map.get('share_id')
        return self


class OSSDeleteFilesResponse(TeaModel):
    """
    批量删除文件 response
    """
    def __init__(self, deleted_file_id_list=None, domain_id=None, drive_id=None, share_id=None):
        # deleted_file_id_list
        self.deleted_file_id_list = deleted_file_id_list  # type: list
        # domain_id
        self.domain_id = domain_id  # type: str
        # drive_id
        self.drive_id = drive_id  # type: str
        # share_id
        self.share_id = share_id  # type: str

    def validate(self):
        if self.domain_id:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z]+')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.share_id:
            self.validate_pattern(self.share_id, 'share_id', '[0-9]+')

    def to_map(self):
        result = {}
        result['deleted_file_id_list'] = self.deleted_file_id_list
        result['domain_id'] = self.domain_id
        result['drive_id'] = self.drive_id
        result['share_id'] = self.share_id
        return result

    def from_map(self, map={}):
        self.deleted_file_id_list = map.get('deleted_file_id_list')
        self.domain_id = map.get('domain_id')
        self.drive_id = map.get('drive_id')
        self.share_id = map.get('share_id')
        return self


class OSSGetDownloadUrlResponse(TeaModel):
    """
    获取download url response
    """
    def __init__(self, expiration=None, method=None, url=None):
        # expiration
        self.expiration = expiration  # type: str
        # method
        self.method = method  # type: str
        # url
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['expiration'] = self.expiration
        result['method'] = self.method
        result['url'] = self.url
        return result

    def from_map(self, map={}):
        self.expiration = map.get('expiration')
        self.method = map.get('method')
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
        self.crc_64hash = crc_64hash  # type: str
        # created_at
        self.created_at = created_at  # type: str
        # description
        self.description = description  # type: str
        # domain_id
        self.domain_id = domain_id  # type: str
        # download_url
        self.download_url = download_url  # type: str
        # drive_id
        self.drive_id = drive_id  # type: str
        # file_extension
        self.file_extension = file_extension  # type: str
        # file_path
        self.file_path = file_path  # type: str
        # name
        self.name = name  # type: str
        # parent_file_id
        self.parent_file_path = parent_file_path  # type: str
        # share_id
        self.share_id = share_id  # type: str
        # Size
        self.size = size  # type: int
        # status
        self.status = status  # type: str
        # thumbnail
        self.thumbnail = thumbnail  # type: str
        # trashed_at
        self.trashed_at = trashed_at  # type: str
        # type
        self.type = type  # type: str
        # updated_at
        self.updated_at = updated_at  # type: str
        # upload_id
        self.upload_id = upload_id  # type: str
        # url
        self.url = url  # type: str

    def validate(self):
        if self.domain_id:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z]+')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.name, 'name')
        if self.name:
            self.validate_pattern(self.name, 'name', '[a-zA-Z0-9.-]{1,1000}')
        if self.parent_file_path:
            self.validate_max_length(self.parent_file_path, 'parent_file_path', 50)
            self.validate_pattern(self.parent_file_path, 'parent_file_path', '[a-z0-9]{1,50}')
        if self.share_id:
            self.validate_pattern(self.share_id, 'share_id', '[0-9]+')

    def to_map(self):
        result = {}
        result['content_hash'] = self.content_hash
        result['content_hash_name'] = self.content_hash_name
        result['content_type'] = self.content_type
        result['crc64_hash'] = self.crc_64hash
        result['created_at'] = self.created_at
        result['description'] = self.description
        result['domain_id'] = self.domain_id
        result['download_url'] = self.download_url
        result['drive_id'] = self.drive_id
        result['file_extension'] = self.file_extension
        result['file_path'] = self.file_path
        result['name'] = self.name
        result['parent_file_path'] = self.parent_file_path
        result['share_id'] = self.share_id
        result['size'] = self.size
        result['status'] = self.status
        result['thumbnail'] = self.thumbnail
        result['trashed_at'] = self.trashed_at
        result['type'] = self.type
        result['updated_at'] = self.updated_at
        result['upload_id'] = self.upload_id
        result['url'] = self.url
        return result

    def from_map(self, map={}):
        self.content_hash = map.get('content_hash')
        self.content_hash_name = map.get('content_hash_name')
        self.content_type = map.get('content_type')
        self.crc_64hash = map.get('crc64_hash')
        self.created_at = map.get('created_at')
        self.description = map.get('description')
        self.domain_id = map.get('domain_id')
        self.download_url = map.get('download_url')
        self.drive_id = map.get('drive_id')
        self.file_extension = map.get('file_extension')
        self.file_path = map.get('file_path')
        self.name = map.get('name')
        self.parent_file_path = map.get('parent_file_path')
        self.share_id = map.get('share_id')
        self.size = map.get('size')
        self.status = map.get('status')
        self.thumbnail = map.get('thumbnail')
        self.trashed_at = map.get('trashed_at')
        self.type = map.get('type')
        self.updated_at = map.get('updated_at')
        self.upload_id = map.get('upload_id')
        self.url = map.get('url')
        return self


class OSSGetSecureUrlResponse(TeaModel):
    """
    获取secure url response
    """
    def __init__(self, expiration=None, url=None):
        # expiration
        self.expiration = expiration  # type: str
        # url
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['expiration'] = self.expiration
        result['url'] = self.url
        return result

    def from_map(self, map={}):
        self.expiration = map.get('expiration')
        self.url = map.get('url')
        return self


class OSSGetUploadUrlResponse(TeaModel):
    """
    Get UploadUrl Response
    """
    def __init__(self, create_at=None, domain_id=None, drive_id=None, file_path=None, part_info_list=None,
                 upload_id=None):
        # created_at
        self.create_at = create_at  # type: str
        # domain_id
        self.domain_id = domain_id  # type: str
        # drive_id
        self.drive_id = drive_id  # type: str
        # file_path
        self.file_path = file_path  # type: str
        # part_info_list
        self.part_info_list = part_info_list  # type: list
        # upload_id
        self.upload_id = upload_id  # type: str

    def validate(self):
        if self.domain_id:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z]+')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.part_info_list:
            for k in self.part_info_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['create_at'] = self.create_at
        result['domain_id'] = self.domain_id
        result['drive_id'] = self.drive_id
        result['file_path'] = self.file_path
        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k in self.part_info_list:
                result['part_info_list'].append(k.to_map() if k else None)
        else:
            result['part_info_list'] = None
        result['upload_id'] = self.upload_id
        return result

    def from_map(self, map={}):
        self.create_at = map.get('create_at')
        self.domain_id = map.get('domain_id')
        self.drive_id = map.get('drive_id')
        self.file_path = map.get('file_path')
        self.part_info_list = []
        if map.get('part_info_list') is not None:
            for k in map.get('part_info_list'):
                temp_model = UploadPartInfo()
                self.part_info_list.append(temp_model.from_map(k))
        else:
            self.part_info_list = None
        self.upload_id = map.get('upload_id')
        return self


class OSSListFileResponse(TeaModel):
    """
    List file response
    """
    def __init__(self, items=None, next_marker=None):
        # items
        self.items = items  # type: list
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
        else:
            result['items'] = None
        result['next_marker'] = self.next_marker
        return result

    def from_map(self, map={}):
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = BaseOSSFileResponse()
                self.items.append(temp_model.from_map(k))
        else:
            self.items = None
        self.next_marker = map.get('next_marker')
        return self


class OSSListUploadedPartResponse(TeaModel):
    """
    获取签名 response
    """
    def __init__(self, file_path=None, next_part_number_marker=None, upload_id=None, uploaded_parts=None):
        # file_path
        self.file_path = file_path  # type: str
        # next_part_number_marker
        self.next_part_number_marker = next_part_number_marker  # type: str
        # upload_id
        self.upload_id = upload_id  # type: str
        # uploaded_parts
        self.uploaded_parts = uploaded_parts  # type: list

    def validate(self):
        if self.uploaded_parts:
            for k in self.uploaded_parts:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['file_path'] = self.file_path
        result['next_part_number_marker'] = self.next_part_number_marker
        result['upload_id'] = self.upload_id
        result['uploaded_parts'] = []
        if self.uploaded_parts is not None:
            for k in self.uploaded_parts:
                result['uploaded_parts'].append(k.to_map() if k else None)
        else:
            result['uploaded_parts'] = None
        return result

    def from_map(self, map={}):
        self.file_path = map.get('file_path')
        self.next_part_number_marker = map.get('next_part_number_marker')
        self.upload_id = map.get('upload_id')
        self.uploaded_parts = []
        if map.get('uploaded_parts') is not None:
            for k in map.get('uploaded_parts'):
                temp_model = UploadPartInfo()
                self.uploaded_parts.append(temp_model.from_map(k))
        else:
            self.uploaded_parts = None
        return self


class OSSMoveFileResponse(TeaModel):
    """
    文件移动 response
    """
    def __init__(self, async_task_id=None, domain_id=None, drive_id=None, file_path=None, share_id=None):
        # async_task_id
        self.async_task_id = async_task_id  # type: str
        # domain_id
        self.domain_id = domain_id  # type: str
        # drive_id
        self.drive_id = drive_id  # type: str
        # file_path
        self.file_path = file_path  # type: str
        # drive_id
        self.share_id = share_id  # type: str

    def validate(self):
        if self.domain_id:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z-]+')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.share_id:
            self.validate_pattern(self.share_id, 'share_id', '[a-z0-9A-Z]+')

    def to_map(self):
        result = {}
        result['async_task_id'] = self.async_task_id
        result['domain_id'] = self.domain_id
        result['drive_id'] = self.drive_id
        result['file_path'] = self.file_path
        result['share_id'] = self.share_id
        return result

    def from_map(self, map={}):
        self.async_task_id = map.get('async_task_id')
        self.domain_id = map.get('domain_id')
        self.drive_id = map.get('drive_id')
        self.file_path = map.get('file_path')
        self.share_id = map.get('share_id')
        return self


class OSSSearchFileResponse(TeaModel):
    """
    search file response
    """
    def __init__(self, items=None, next_marker=None):
        # items
        self.items = items  # type: list
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
        else:
            result['items'] = None
        result['next_marker'] = self.next_marker
        return result

    def from_map(self, map={}):
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = BaseOSSFileResponse()
                self.items.append(temp_model.from_map(k))
        else:
            self.items = None
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
        self.crc_64hash = crc_64hash  # type: str
        # created_at
        self.created_at = created_at  # type: str
        # description
        self.description = description  # type: str
        # domain_id
        self.domain_id = domain_id  # type: str
        # download_url
        self.download_url = download_url  # type: str
        # drive_id
        self.drive_id = drive_id  # type: str
        # file_extension
        self.file_extension = file_extension  # type: str
        # file_path
        self.file_path = file_path  # type: str
        # name
        self.name = name  # type: str
        # parent_file_id
        self.parent_file_path = parent_file_path  # type: str
        # share_id
        self.share_id = share_id  # type: str
        # Size
        self.size = size  # type: int
        # status
        self.status = status  # type: str
        # thumbnail
        self.thumbnail = thumbnail  # type: str
        # trashed_at
        self.trashed_at = trashed_at  # type: str
        # type
        self.type = type  # type: str
        # updated_at
        self.updated_at = updated_at  # type: str
        # upload_id
        self.upload_id = upload_id  # type: str
        # url
        self.url = url  # type: str

    def validate(self):
        if self.domain_id:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z]+')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.name, 'name')
        if self.name:
            self.validate_pattern(self.name, 'name', '[a-zA-Z0-9.-]{1,1000}')
        if self.parent_file_path:
            self.validate_max_length(self.parent_file_path, 'parent_file_path', 50)
            self.validate_pattern(self.parent_file_path, 'parent_file_path', '[a-z0-9]{1,50}')
        if self.share_id:
            self.validate_pattern(self.share_id, 'share_id', '[0-9]+')

    def to_map(self):
        result = {}
        result['content_hash'] = self.content_hash
        result['content_hash_name'] = self.content_hash_name
        result['content_type'] = self.content_type
        result['crc64_hash'] = self.crc_64hash
        result['created_at'] = self.created_at
        result['description'] = self.description
        result['domain_id'] = self.domain_id
        result['download_url'] = self.download_url
        result['drive_id'] = self.drive_id
        result['file_extension'] = self.file_extension
        result['file_path'] = self.file_path
        result['name'] = self.name
        result['parent_file_path'] = self.parent_file_path
        result['share_id'] = self.share_id
        result['size'] = self.size
        result['status'] = self.status
        result['thumbnail'] = self.thumbnail
        result['trashed_at'] = self.trashed_at
        result['type'] = self.type
        result['updated_at'] = self.updated_at
        result['upload_id'] = self.upload_id
        result['url'] = self.url
        return result

    def from_map(self, map={}):
        self.content_hash = map.get('content_hash')
        self.content_hash_name = map.get('content_hash_name')
        self.content_type = map.get('content_type')
        self.crc_64hash = map.get('crc64_hash')
        self.created_at = map.get('created_at')
        self.description = map.get('description')
        self.domain_id = map.get('domain_id')
        self.download_url = map.get('download_url')
        self.drive_id = map.get('drive_id')
        self.file_extension = map.get('file_extension')
        self.file_path = map.get('file_path')
        self.name = map.get('name')
        self.parent_file_path = map.get('parent_file_path')
        self.share_id = map.get('share_id')
        self.size = map.get('size')
        self.status = map.get('status')
        self.thumbnail = map.get('thumbnail')
        self.trashed_at = map.get('trashed_at')
        self.type = map.get('type')
        self.updated_at = map.get('updated_at')
        self.upload_id = map.get('upload_id')
        self.url = map.get('url')
        return self


class OSSVideoDRMLicenseResponse(TeaModel):
    """
    DRM License response
    """
    def __init__(self, data=None, states=None):
        # drm_data
        self.data = data  # type: str
        # states
        self.states = states  # type: int

    def validate(self):
        self.validate_required(self.data, 'data')
        self.validate_required(self.states, 'states')

    def to_map(self):
        result = {}
        result['data'] = self.data
        result['states'] = self.states
        return result

    def from_map(self, map={}):
        self.data = map.get('data')
        self.states = map.get('states')
        return self


class OSSVideoDefinitionResponse(TeaModel):
    """
    转码接口response
    """
    def __init__(self, definition_list=None, frame_rate=None):
        # definition_list
        self.definition_list = definition_list  # type: list
        # frame_rate
        self.frame_rate = frame_rate  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['definition_list'] = self.definition_list
        result['frame_rate'] = self.frame_rate
        return result

    def from_map(self, map={}):
        self.definition_list = map.get('definition_list')
        self.frame_rate = map.get('frame_rate')
        return self


class OSSVideoTranscodeResponse(TeaModel):
    """
    转码接口response
    """
    def __init__(self, definition_list=None, duration=None, hls_time=None):
        # definition_list
        self.definition_list = definition_list  # type: list
        # duration
        self.duration = duration  # type: int
        # hls_time
        self.hls_time = hls_time  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['definition_list'] = self.definition_list
        result['duration'] = self.duration
        result['hls_time'] = self.hls_time
        return result

    def from_map(self, map={}):
        self.definition_list = map.get('definition_list')
        self.duration = map.get('duration')
        self.hls_time = map.get('hls_time')
        return self


class PreHashCheckSuccessResponse(TeaModel):
    """
    Pre hash check Response
    """
    def __init__(self, code=None, file_name=None, message=None, parent_file_id=None, pre_hash=None):
        # code
        self.code = code  # type: str
        # file_name
        self.file_name = file_name  # type: str
        # message
        self.message = message  # type: str
        # parent_file_id
        self.parent_file_id = parent_file_id  # type: str
        # pre_hash
        self.pre_hash = pre_hash  # type: str

    def validate(self):
        self.validate_required(self.parent_file_id, 'parent_file_id')
        if self.parent_file_id:
            self.validate_max_length(self.parent_file_id, 'parent_file_id', 50)
            self.validate_pattern(self.parent_file_id, 'parent_file_id', '[a-z0-9]{1,50}')

    def to_map(self):
        result = {}
        result['code'] = self.code
        result['file_name'] = self.file_name
        result['message'] = self.message
        result['parent_file_id'] = self.parent_file_id
        result['pre_hash'] = self.pre_hash
        return result

    def from_map(self, map={}):
        self.code = map.get('code')
        self.file_name = map.get('file_name')
        self.message = map.get('message')
        self.parent_file_id = map.get('parent_file_id')
        self.pre_hash = map.get('pre_hash')
        return self


class RateLimit(TeaModel):
    """
    下载限速配置
    """
    def __init__(self, part_size=None, part_speed=None):
        self.part_size = part_size  # type: int
        self.part_speed = part_speed  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['part_size'] = self.part_size
        result['part_speed'] = self.part_speed
        return result

    def from_map(self, map={}):
        self.part_size = map.get('part_size')
        self.part_speed = map.get('part_speed')
        return self


class RevokeRequest(TeaModel):
    """
    *
    """
    def __init__(self, headers=None, app_id=None, refresh_token=None):
        self.headers = headers  # type: dict
        # App ID, 当前访问的App
        self.app_id = app_id  # type: str
        # refresh token, 登录时返回的
        self.refresh_token = refresh_token  # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.refresh_token, 'refresh_token')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['app_id'] = self.app_id
        result['refresh_token'] = self.refresh_token
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.app_id = map.get('app_id')
        self.refresh_token = map.get('refresh_token')
        return self


class ScanFileMetaResponse(TeaModel):
    """
    scan file meta response
    """
    def __init__(self, items=None, next_marker=None):
        # items
        self.items = items  # type: list
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
        else:
            result['items'] = None
        result['next_marker'] = self.next_marker
        return result

    def from_map(self, map={}):
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = BaseFileResponse()
                self.items.append(temp_model.from_map(k))
        else:
            self.items = None
        self.next_marker = map.get('next_marker')
        return self


class SearchFileResponse(TeaModel):
    """
    search file response
    """
    def __init__(self, items=None, next_marker=None):
        # items
        self.items = items  # type: list
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
        else:
            result['items'] = None
        result['next_marker'] = self.next_marker
        return result

    def from_map(self, map={}):
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = BaseFileResponse()
                self.items.append(temp_model.from_map(k))
        else:
            self.items = None
        self.next_marker = map.get('next_marker')
        return self


class SharePermissionPolicy(TeaModel):
    """
    *
    """
    def __init__(self, file_path=None, permission_inheritable=None, permission_list=None, permission_type=None):
        self.file_path = file_path  # type: str
        self.permission_inheritable = permission_inheritable  # type: bool
        self.permission_list = permission_list  # type: list
        self.permission_type = permission_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['file_path'] = self.file_path
        result['permission_inheritable'] = self.permission_inheritable
        result['permission_list'] = self.permission_list
        result['permission_type'] = self.permission_type
        return result

    def from_map(self, map={}):
        self.file_path = map.get('file_path')
        self.permission_inheritable = map.get('permission_inheritable')
        self.permission_list = map.get('permission_list')
        self.permission_type = map.get('permission_type')
        return self


class StoreFile(TeaModel):
    """
    *
    """
    def __init__(self, domain_id=None, name=None, parent_file_path=None, store_id=None, type=None):
        self.domain_id = domain_id  # type: str
        self.name = name  # type: str
        self.parent_file_path = parent_file_path  # type: str
        self.store_id = store_id  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['domain_id'] = self.domain_id
        result['name'] = self.name
        result['parent_file_path'] = self.parent_file_path
        result['store_id'] = self.store_id
        result['type'] = self.type
        return result

    def from_map(self, map={}):
        self.domain_id = map.get('domain_id')
        self.name = map.get('name')
        self.parent_file_path = map.get('parent_file_path')
        self.store_id = map.get('store_id')
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
        self.base_path = base_path  # type: str
        # bucket名称
        self.bucket = bucket  # type: str
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
        self.domain_id = domain_id  # type: str
        # Public访问地址
        self.endpoint = endpoint  # type: str
        # vpc访问地址
        self.internal_endpoint = internal_endpoint  # type: str
        # 地点
        self.location = location  # type: str
        # 存储归属，system表示系统提供，custom表示使用自己的存储
        self.ownership = ownership  # type: str
        # Policy授权,system类型store会将bucket权限授予当前云账号
        self.policy = policy  # type: str
        # 访问Bucket的角色ARN
        self.role_arn = role_arn  # type: str
        # store ID
        self.store_id = store_id  # type: str
        # 存储类型，当前只支持oss
        self.type = type  # type: str

    def validate(self):
        self.validate_required(self.bucket, 'bucket')
        self.validate_required(self.endpoint, 'endpoint')
        self.validate_required(self.ownership, 'ownership')
        self.validate_required(self.policy, 'policy')
        self.validate_required(self.store_id, 'store_id')
        self.validate_required(self.type, 'type')

    def to_map(self):
        result = {}
        result['accelerate_endpoint'] = self.accelerate_endpoint
        result['base_path'] = self.base_path
        result['bucket'] = self.bucket
        result['cdn_endpoint'] = self.cdn_endpoint
        result['customized_accelerate_endpoint'] = self.customized_accelerate_endpoint
        result['customized_cdn_endpoint'] = self.customized_cdn_endpoint
        result['customized_endpoint'] = self.customized_endpoint
        result['customized_internal_endpoint'] = self.customized_internal_endpoint
        result['domain_id'] = self.domain_id
        result['endpoint'] = self.endpoint
        result['internal_endpoint'] = self.internal_endpoint
        result['location'] = self.location
        result['ownership'] = self.ownership
        result['policy'] = self.policy
        result['role_arn'] = self.role_arn
        result['store_id'] = self.store_id
        result['type'] = self.type
        return result

    def from_map(self, map={}):
        self.accelerate_endpoint = map.get('accelerate_endpoint')
        self.base_path = map.get('base_path')
        self.bucket = map.get('bucket')
        self.cdn_endpoint = map.get('cdn_endpoint')
        self.customized_accelerate_endpoint = map.get('customized_accelerate_endpoint')
        self.customized_cdn_endpoint = map.get('customized_cdn_endpoint')
        self.customized_endpoint = map.get('customized_endpoint')
        self.customized_internal_endpoint = map.get('customized_internal_endpoint')
        self.domain_id = map.get('domain_id')
        self.endpoint = map.get('endpoint')
        self.internal_endpoint = map.get('internal_endpoint')
        self.location = map.get('location')
        self.ownership = map.get('ownership')
        self.policy = map.get('policy')
        self.role_arn = map.get('role_arn')
        self.store_id = map.get('store_id')
        self.type = map.get('type')
        return self


class StreamInfo(TeaModel):
    """
    *
    """
    def __init__(self, crc_64hash=None, download_url=None, thumbnail=None, url=None):
        # crc64_hash
        self.crc_64hash = crc_64hash  # type: str
        # download_url
        self.download_url = download_url  # type: str
        # thumbnail
        self.thumbnail = thumbnail  # type: str
        # url
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['crc64_hash'] = self.crc_64hash
        result['download_url'] = self.download_url
        result['thumbnail'] = self.thumbnail
        result['url'] = self.url
        return result

    def from_map(self, map={}):
        self.crc_64hash = map.get('crc64_hash')
        self.download_url = map.get('download_url')
        self.thumbnail = map.get('thumbnail')
        self.url = map.get('url')
        return self


class StreamUploadInfo(TeaModel):
    """
    *
    """
    def __init__(self, part_info_list=None, pre_rapid_upload=None, rapid_upload=None, upload_id=None):
        # part_info_list
        self.part_info_list = part_info_list  # type: list
        # pre_rapid_upload
        # type: boolean
        self.pre_rapid_upload = pre_rapid_upload  # type: bool
        # rapid_upload
        # type: boolean
        self.rapid_upload = rapid_upload  # type: bool
        # upload_id
        self.upload_id = upload_id  # type: str

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
        else:
            result['part_info_list'] = None
        result['pre_rapid_upload'] = self.pre_rapid_upload
        result['rapid_upload'] = self.rapid_upload
        result['upload_id'] = self.upload_id
        return result

    def from_map(self, map={}):
        self.part_info_list = []
        if map.get('part_info_list') is not None:
            for k in map.get('part_info_list'):
                temp_model = UploadPartInfo()
                self.part_info_list.append(temp_model.from_map(k))
        else:
            self.part_info_list = None
        self.pre_rapid_upload = map.get('pre_rapid_upload')
        self.rapid_upload = map.get('rapid_upload')
        self.upload_id = map.get('upload_id')
        return self


class SystemTag(TeaModel):
    """
    *
    """
    def __init__(self, confidence=None, en_name=None, name=None, parent_en_name=None, parent_name=None,
                 selected=None, tag_level=None):
        self.confidence = confidence  # type: int
        self.en_name = en_name  # type: str
        self.name = name  # type: str
        self.parent_en_name = parent_en_name  # type: str
        self.parent_name = parent_name  # type: str
        self.selected = selected  # type: bool
        self.tag_level = tag_level  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['confidence'] = self.confidence
        result['en_name'] = self.en_name
        result['name'] = self.name
        result['parent_en_name'] = self.parent_en_name
        result['parent_name'] = self.parent_name
        result['selected'] = self.selected
        result['tag_level'] = self.tag_level
        return result

    def from_map(self, map={}):
        self.confidence = map.get('confidence')
        self.en_name = map.get('en_name')
        self.name = map.get('name')
        self.parent_en_name = map.get('parent_en_name')
        self.parent_name = map.get('parent_name')
        self.selected = map.get('selected')
        self.tag_level = map.get('tag_level')
        return self


class TokenRequest(TeaModel):
    """
    *
    """
    def __init__(self, headers=None, addition_data=None, app_id=None, grant_type=None, refresh_token=None):
        self.headers = headers  # type: dict
        # addition_data
        self.addition_data = addition_data  # type: dict
        # App ID, 当前访问的App
        self.app_id = app_id  # type: str
        # 只能填refresh_token
        self.grant_type = grant_type  # type: str
        # refresh token, 登录时返回的
        self.refresh_token = refresh_token  # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.grant_type, 'grant_type')
        self.validate_required(self.refresh_token, 'refresh_token')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['addition_data'] = self.addition_data
        result['app_id'] = self.app_id
        result['grant_type'] = self.grant_type
        result['refresh_token'] = self.refresh_token
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.addition_data = map.get('addition_data')
        self.app_id = map.get('app_id')
        self.grant_type = map.get('grant_type')
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
        self.creator = creator  # type: str
        # Drive 备注信息
        self.description = description  # type: str
        # Domain ID
        self.domain_id = domain_id  # type: str
        # Drive ID
        self.drive_id = drive_id  # type: str
        # Drive 名称
        self.drive_name = drive_name  # type: str
        # Drive 类型
        self.drive_type = drive_type  # type: str
        self.encrypt_data_access = encrypt_data_access  # type: bool
        self.encrypt_mode = encrypt_mode  # type: str
        # Drive 所有者
        self.owner = owner  # type: str
        # Drive存储基于store的相对路径，domain的PathType为OSSPath时返回
        self.relative_path = relative_path  # type: str
        # Drive 状态
        self.status = status  # type: str
        # 存储 ID, domain的PathType为OSSPath时返回
        self.store_id = store_id  # type: str
        # Drive 空间总量
        self.total_size = total_size  # type: int
        # Drive 空间已使用量
        self.used_size = used_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['creator'] = self.creator
        result['description'] = self.description
        result['domain_id'] = self.domain_id
        result['drive_id'] = self.drive_id
        result['drive_name'] = self.drive_name
        result['drive_type'] = self.drive_type
        result['encrypt_data_access'] = self.encrypt_data_access
        result['encrypt_mode'] = self.encrypt_mode
        result['owner'] = self.owner
        result['relative_path'] = self.relative_path
        result['status'] = self.status
        result['store_id'] = self.store_id
        result['total_size'] = self.total_size
        result['used_size'] = self.used_size
        return result

    def from_map(self, map={}):
        self.creator = map.get('creator')
        self.description = map.get('description')
        self.domain_id = map.get('domain_id')
        self.drive_id = map.get('drive_id')
        self.drive_name = map.get('drive_name')
        self.drive_type = map.get('drive_type')
        self.encrypt_data_access = map.get('encrypt_data_access')
        self.encrypt_mode = map.get('encrypt_mode')
        self.owner = map.get('owner')
        self.relative_path = map.get('relative_path')
        self.status = map.get('status')
        self.store_id = map.get('store_id')
        self.total_size = map.get('total_size')
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
        self.category = category  # type: str
        # Content Hash
        self.content_hash = content_hash  # type: str
        # content_hash_name
        self.content_hash_name = content_hash_name  # type: str
        # content_type
        self.content_type = content_type  # type: str
        # crc64_hash
        self.crc_64hash = crc_64hash  # type: str
        # created_at
        self.created_at = created_at  # type: str
        # description
        self.description = description  # type: str
        # DomainID
        self.domain_id = domain_id  # type: str
        # download_url
        self.download_url = download_url  # type: str
        # drive_id
        self.drive_id = drive_id  # type: str
        # encrypt_mode
        self.encrypt_mode = encrypt_mode  # type: str
        # file_extension
        self.file_extension = file_extension  # type: str
        # file_id
        self.file_id = file_id  # type: str
        # Hidden
        # type: boolean
        self.hidden = hidden  # type: bool
        self.image_media_metadata = image_media_metadata  # type: ImageMediaResponse
        # labels
        self.labels = labels  # type: list
        self.meta = meta  # type: str
        # name
        self.name = name  # type: str
        # parent_file_id
        self.parent_file_id = parent_file_id  # type: str
        self.punish_flag = punish_flag  # type: int
        # Size
        self.size = size  # type: int
        # starred
        # type: boolean
        self.starred = starred  # type: bool
        # status
        self.status = status  # type: str
        # @Deprecated streams url info
        self.streams_info = streams_info  # type: dict
        # thumbnail
        self.thumbnail = thumbnail  # type: str
        # trashed_at
        self.trashed_at = trashed_at  # type: str
        # type
        self.type = type  # type: str
        # updated_at
        self.updated_at = updated_at  # type: str
        # upload_id
        self.upload_id = upload_id  # type: str
        # url
        self.url = url  # type: str
        # user_meta
        self.user_meta = user_meta  # type: str
        self.video_media_metadata = video_media_metadata  # type: VideoMediaResponse
        self.video_preview_metadata = video_preview_metadata  # type: VideoPreviewResponse

    def validate(self):
        if self.domain_id:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z]+')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.file_id:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9]{1,50}')
        if self.image_media_metadata:
            self.image_media_metadata.validate()
        self.validate_required(self.name, 'name')
        if self.name:
            self.validate_pattern(self.name, 'name', '[a-zA-Z0-9.-]{1,1000}')
        if self.parent_file_id:
            self.validate_max_length(self.parent_file_id, 'parent_file_id', 50)
            self.validate_pattern(self.parent_file_id, 'parent_file_id', '[a-z0-9]{1,50}')
        if self.video_media_metadata:
            self.video_media_metadata.validate()
        if self.video_preview_metadata:
            self.video_preview_metadata.validate()

    def to_map(self):
        result = {}
        result['category'] = self.category
        result['content_hash'] = self.content_hash
        result['content_hash_name'] = self.content_hash_name
        result['content_type'] = self.content_type
        result['crc64_hash'] = self.crc_64hash
        result['created_at'] = self.created_at
        result['description'] = self.description
        result['domain_id'] = self.domain_id
        result['download_url'] = self.download_url
        result['drive_id'] = self.drive_id
        result['encrypt_mode'] = self.encrypt_mode
        result['file_extension'] = self.file_extension
        result['file_id'] = self.file_id
        result['hidden'] = self.hidden
        if self.image_media_metadata is not None:
            result['image_media_metadata'] = self.image_media_metadata.to_map()
        else:
            result['image_media_metadata'] = None
        result['labels'] = self.labels
        result['meta'] = self.meta
        result['name'] = self.name
        result['parent_file_id'] = self.parent_file_id
        result['punish_flag'] = self.punish_flag
        result['size'] = self.size
        result['starred'] = self.starred
        result['status'] = self.status
        result['streams_info'] = self.streams_info
        result['thumbnail'] = self.thumbnail
        result['trashed_at'] = self.trashed_at
        result['type'] = self.type
        result['updated_at'] = self.updated_at
        result['upload_id'] = self.upload_id
        result['url'] = self.url
        result['user_meta'] = self.user_meta
        if self.video_media_metadata is not None:
            result['video_media_metadata'] = self.video_media_metadata.to_map()
        else:
            result['video_media_metadata'] = None
        if self.video_preview_metadata is not None:
            result['video_preview_metadata'] = self.video_preview_metadata.to_map()
        else:
            result['video_preview_metadata'] = None
        return result

    def from_map(self, map={}):
        self.category = map.get('category')
        self.content_hash = map.get('content_hash')
        self.content_hash_name = map.get('content_hash_name')
        self.content_type = map.get('content_type')
        self.crc_64hash = map.get('crc64_hash')
        self.created_at = map.get('created_at')
        self.description = map.get('description')
        self.domain_id = map.get('domain_id')
        self.download_url = map.get('download_url')
        self.drive_id = map.get('drive_id')
        self.encrypt_mode = map.get('encrypt_mode')
        self.file_extension = map.get('file_extension')
        self.file_id = map.get('file_id')
        self.hidden = map.get('hidden')
        if map.get('image_media_metadata') is not None:
            temp_model = ImageMediaResponse()
            self.image_media_metadata = temp_model.from_map(map['image_media_metadata'])
        else:
            self.image_media_metadata = None
        self.labels = map.get('labels')
        self.meta = map.get('meta')
        self.name = map.get('name')
        self.parent_file_id = map.get('parent_file_id')
        self.punish_flag = map.get('punish_flag')
        self.size = map.get('size')
        self.starred = map.get('starred')
        self.status = map.get('status')
        self.streams_info = map.get('streams_info')
        self.thumbnail = map.get('thumbnail')
        self.trashed_at = map.get('trashed_at')
        self.type = map.get('type')
        self.updated_at = map.get('updated_at')
        self.upload_id = map.get('upload_id')
        self.url = map.get('url')
        self.user_meta = map.get('user_meta')
        if map.get('video_media_metadata') is not None:
            temp_model = VideoMediaResponse()
            self.video_media_metadata = temp_model.from_map(map['video_media_metadata'])
        else:
            self.video_media_metadata = None
        if map.get('video_preview_metadata') is not None:
            temp_model = VideoPreviewResponse()
            self.video_preview_metadata = temp_model.from_map(map['video_preview_metadata'])
        else:
            self.video_preview_metadata = None
        return self


class UpdateShareResponse(TeaModel):
    """
    Update share response
    """
    def __init__(self, created_at=None, creator=None, description=None, domain_id=None, drive_id=None,
                 expiration=None, expired=None, owner=None, permissions=None, share_file_path=None, share_id=None,
                 share_name=None, share_policy=None, status=None, updated_at=None):
        # created_at
        self.created_at = created_at  # type: str
        # creator
        self.creator = creator  # type: str
        # description
        self.description = description  # type: str
        # domain_id
        self.domain_id = domain_id  # type: str
        # drive_id
        self.drive_id = drive_id  # type: str
        # expiration
        self.expiration = expiration  # type: str
        # expired
        self.expired = expired  # type: bool
        # owner
        self.owner = owner  # type: str
        # permissions
        self.permissions = permissions  # type: list
        # share_path
        self.share_file_path = share_file_path  # type: str
        # share_id
        self.share_id = share_id  # type: str
        # share_name
        self.share_name = share_name  # type: str
        self.share_policy = share_policy  # type: list
        # status
        self.status = status  # type: str
        # updated_at
        self.updated_at = updated_at  # type: str

    def validate(self):
        if self.share_policy:
            for k in self.share_policy:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['created_at'] = self.created_at
        result['creator'] = self.creator
        result['description'] = self.description
        result['domain_id'] = self.domain_id
        result['drive_id'] = self.drive_id
        result['expiration'] = self.expiration
        result['expired'] = self.expired
        result['owner'] = self.owner
        result['permissions'] = self.permissions
        result['share_file_path'] = self.share_file_path
        result['share_id'] = self.share_id
        result['share_name'] = self.share_name
        result['share_policy'] = []
        if self.share_policy is not None:
            for k in self.share_policy:
                result['share_policy'].append(k.to_map() if k else None)
        else:
            result['share_policy'] = None
        result['status'] = self.status
        result['updated_at'] = self.updated_at
        return result

    def from_map(self, map={}):
        self.created_at = map.get('created_at')
        self.creator = map.get('creator')
        self.description = map.get('description')
        self.domain_id = map.get('domain_id')
        self.drive_id = map.get('drive_id')
        self.expiration = map.get('expiration')
        self.expired = map.get('expired')
        self.owner = map.get('owner')
        self.permissions = map.get('permissions')
        self.share_file_path = map.get('share_file_path')
        self.share_id = map.get('share_id')
        self.share_name = map.get('share_name')
        self.share_policy = []
        if map.get('share_policy') is not None:
            for k in map.get('share_policy'):
                temp_model = SharePermissionPolicy()
                self.share_policy.append(temp_model.from_map(k))
        else:
            self.share_policy = None
        self.status = map.get('status')
        self.updated_at = map.get('updated_at')
        return self


class UploadPartInfo(TeaModel):
    """
    *
    """
    def __init__(self, etag=None, part_number=None, part_size=None, upload_url=None):
        # etag
        self.etag = etag  # type: str
        # PartNumber
        self.part_number = part_number  # type: int
        # PartSize：
        self.part_size = part_size  # type: int
        # upload_url
        self.upload_url = upload_url  # type: str

    def validate(self):
        if self.part_number:
            self.validate_pattern(self.part_number, 'part_number', '[0-9]+')

    def to_map(self):
        result = {}
        result['etag'] = self.etag
        result['part_number'] = self.part_number
        result['part_size'] = self.part_size
        result['upload_url'] = self.upload_url
        return result

    def from_map(self, map={}):
        self.etag = map.get('etag')
        self.part_number = map.get('part_number')
        self.part_size = map.get('part_size')
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
        self.thumbnail = thumbnail  # type: str
        # url
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['download_url'] = self.download_url
        result['thumbnail'] = self.thumbnail
        result['url'] = self.url
        return result

    def from_map(self, map={}):
        self.download_url = map.get('download_url')
        self.thumbnail = map.get('thumbnail')
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
        self.created_at = created_at  # type: int
        # 详情
        self.detail = detail  # type: str
        # Domain ID
        self.domain_id = domain_id  # type: str
        # 唯一身份标识
        self.identity = identity  # type: str
        # 最后登录时间
        self.last_login_time = last_login_time  # type: int
        # 状态
        self.status = status  # type: str
        # 用户ID
        self.user_id = user_id  # type: str
        # 额外的信息，比如type为mobile时，此字段为国家编号，不填默认86
        self.extra = extra  # type: str

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
        result['AuthenticationType'] = self.authentication_type
        result['CreatedAt'] = self.created_at
        result['Detail'] = self.detail
        result['DomainID'] = self.domain_id
        result['Identity'] = self.identity
        result['LastLoginTime'] = self.last_login_time
        result['Status'] = self.status
        result['UserID'] = self.user_id
        result['extra'] = self.extra
        return result

    def from_map(self, map={}):
        self.authentication_type = map.get('AuthenticationType')
        self.created_at = map.get('CreatedAt')
        self.detail = map.get('Detail')
        self.domain_id = map.get('DomainID')
        self.identity = map.get('Identity')
        self.last_login_time = map.get('LastLoginTime')
        self.status = map.get('Status')
        self.user_id = map.get('UserID')
        self.extra = map.get('extra')
        return self


class VerifyCodeRequest(TeaModel):
    """
    *
    """
    def __init__(self, headers=None, app_id=None, phone_number=None, phone_region=None, sms_code=None,
                 sms_code_id=None, verify_type=None):
        self.headers = headers  # type: dict
        # App ID, 当前访问的App
        self.app_id = app_id  # type: str
        # 手机号
        self.phone_number = phone_number  # type: str
        # 国家编号，默认86，不需要填+号，直接填数字
        self.phone_region = phone_region  # type: str
        # 短信验证码内容
        self.sms_code = sms_code  # type: str
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
        result['headers'] = self.headers
        result['app_id'] = self.app_id
        result['phone_number'] = self.phone_number
        result['phone_region'] = self.phone_region
        result['sms_code'] = self.sms_code
        result['sms_code_id'] = self.sms_code_id
        result['verify_type'] = self.verify_type
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.app_id = map.get('app_id')
        self.phone_number = map.get('phone_number')
        self.phone_region = map.get('phone_region')
        self.sms_code = map.get('sms_code')
        self.sms_code_id = map.get('sms_code_id')
        self.verify_type = map.get('verify_type')
        return self


class VerifyCodeResponse(TeaModel):
    """
    *
    """
    def __init__(self, state=None):
        # 修改密码的临时授权码
        self.state = state  # type: str

    def validate(self):
        self.validate_required(self.state, 'state')

    def to_map(self):
        result = {}
        result['state'] = self.state
        return result

    def from_map(self, map={}):
        self.state = map.get('state')
        return self


class VideoMediaAudioStream(TeaModel):
    """
    *
    """
    def __init__(self, bit_rate=None, channel_layout=None, channels=None, code_name=None, duration=None,
                 sample_rate=None):
        # bit_rate 音频比特率 单位：bps
        self.bit_rate = bit_rate  # type: str
        # channel_layout 声道布局
        self.channel_layout = channel_layout  # type: str
        # channels 音频数/声道数
        self.channels = channels  # type: int
        # code_name 音频编码模式
        self.code_name = code_name  # type: str
        # duration 单位 秒
        self.duration = duration  # type: str
        # sample_rate 音频采样率
        self.sample_rate = sample_rate  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['bit_rate'] = self.bit_rate
        result['channel_layout'] = self.channel_layout
        result['channels'] = self.channels
        result['code_name'] = self.code_name
        result['duration'] = self.duration
        result['sample_rate'] = self.sample_rate
        return result

    def from_map(self, map={}):
        self.bit_rate = map.get('bit_rate')
        self.channel_layout = map.get('channel_layout')
        self.channels = map.get('channels')
        self.code_name = map.get('code_name')
        self.duration = map.get('duration')
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
        self.city = city  # type: str
        # country
        self.country = country  # type: str
        # district
        self.district = district  # type: str
        # duration 单位 秒
        self.duration = duration  # type: str
        # height
        self.height = height  # type: int
        # location
        self.location = location  # type: str
        # province
        self.province = province  # type: str
        # time
        self.time = time  # type: str
        # township
        self.township = township  # type: str
        self.video_media_audio_stream = video_media_audio_stream  # type: list
        self.video_media_video_stream = video_media_video_stream  # type: list
        # width
        self.width = width  # type: int

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
        result['address_line'] = self.address_line
        result['city'] = self.city
        result['country'] = self.country
        result['district'] = self.district
        result['duration'] = self.duration
        result['height'] = self.height
        result['location'] = self.location
        result['province'] = self.province
        result['time'] = self.time
        result['township'] = self.township
        result['video_media_audio_stream'] = []
        if self.video_media_audio_stream is not None:
            for k in self.video_media_audio_stream:
                result['video_media_audio_stream'].append(k.to_map() if k else None)
        else:
            result['video_media_audio_stream'] = None
        result['video_media_video_stream'] = []
        if self.video_media_video_stream is not None:
            for k in self.video_media_video_stream:
                result['video_media_video_stream'].append(k.to_map() if k else None)
        else:
            result['video_media_video_stream'] = None
        result['width'] = self.width
        return result

    def from_map(self, map={}):
        self.address_line = map.get('address_line')
        self.city = map.get('city')
        self.country = map.get('country')
        self.district = map.get('district')
        self.duration = map.get('duration')
        self.height = map.get('height')
        self.location = map.get('location')
        self.province = map.get('province')
        self.time = map.get('time')
        self.township = map.get('township')
        self.video_media_audio_stream = []
        if map.get('video_media_audio_stream') is not None:
            for k in map.get('video_media_audio_stream'):
                temp_model = VideoMediaAudioStream()
                self.video_media_audio_stream.append(temp_model.from_map(k))
        else:
            self.video_media_audio_stream = None
        self.video_media_video_stream = []
        if map.get('video_media_video_stream') is not None:
            for k in map.get('video_media_video_stream'):
                temp_model = VideoMediaVideoStream()
                self.video_media_video_stream.append(temp_model.from_map(k))
        else:
            self.video_media_video_stream = None
        self.width = map.get('width')
        return self


class VideoMediaVideoStream(TeaModel):
    """
    *
    """
    def __init__(self, bitrate=None, clarity=None, code_name=None, duration=None, fps=None):
        # bitrate 视频比特率 单位：bps
        self.bitrate = bitrate  # type: str
        # clarity 清晰度（扫描）
        self.clarity = clarity  # type: str
        # code_name 视频编码模式
        self.code_name = code_name  # type: str
        # duration 单位 秒
        self.duration = duration  # type: str
        # fps 视频平均帧率
        self.fps = fps  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['bitrate'] = self.bitrate
        result['clarity'] = self.clarity
        result['code_name'] = self.code_name
        result['duration'] = self.duration
        result['fps'] = self.fps
        return result

    def from_map(self, map={}):
        self.bitrate = map.get('bitrate')
        self.clarity = map.get('clarity')
        self.code_name = map.get('code_name')
        self.duration = map.get('duration')
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
        self.bitrate = bitrate  # type: str
        # duration
        self.duration = duration  # type: str
        # frame_rate
        self.frame_rate = frame_rate  # type: str
        # height
        self.height = height  # type: int
        self.sprite_info = sprite_info  # type: VideoPreviewSprite
        # template_list
        self.template_list = template_list  # type: list
        # thumbnail
        self.thumbnail = thumbnail  # type: str
        # video_format
        self.video_format = video_format  # type: str
        # width
        self.width = width  # type: int

    def validate(self):
        if self.sprite_info:
            self.sprite_info.validate()
        if self.template_list:
            for k in self.template_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['audio_format'] = self.audio_format
        result['bitrate'] = self.bitrate
        result['duration'] = self.duration
        result['frame_rate'] = self.frame_rate
        result['height'] = self.height
        if self.sprite_info is not None:
            result['sprite_info'] = self.sprite_info.to_map()
        else:
            result['sprite_info'] = None
        result['template_list'] = []
        if self.template_list is not None:
            for k in self.template_list:
                result['template_list'].append(k.to_map() if k else None)
        else:
            result['template_list'] = None
        result['thumbnail'] = self.thumbnail
        result['video_format'] = self.video_format
        result['width'] = self.width
        return result

    def from_map(self, map={}):
        self.audio_format = map.get('audio_format')
        self.bitrate = map.get('bitrate')
        self.duration = map.get('duration')
        self.frame_rate = map.get('frame_rate')
        self.height = map.get('height')
        if map.get('sprite_info') is not None:
            temp_model = VideoPreviewSprite()
            self.sprite_info = temp_model.from_map(map['sprite_info'])
        else:
            self.sprite_info = None
        self.template_list = []
        if map.get('template_list') is not None:
            for k in map.get('template_list'):
                temp_model = VideoPreviewTranscode()
                self.template_list.append(temp_model.from_map(k))
        else:
            self.template_list = None
        self.thumbnail = map.get('thumbnail')
        self.video_format = map.get('video_format')
        self.width = map.get('width')
        return self


class VideoPreviewSprite(TeaModel):
    """
    *
    """
    def __init__(self, col=None, count=None, frame_count=None, frame_height=None, frame_width=None, row=None,
                 status=None):
        # col
        self.col = col  # type: int
        # count
        self.count = count  # type: int
        # frame_count
        self.frame_count = frame_count  # type: int
        # frame_height
        self.frame_height = frame_height  # type: int
        # frame_width
        self.frame_width = frame_width  # type: int
        # row
        self.row = row  # type: int
        # status
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['col'] = self.col
        result['count'] = self.count
        result['frame_count'] = self.frame_count
        result['frame_height'] = self.frame_height
        result['frame_width'] = self.frame_width
        result['row'] = self.row
        result['status'] = self.status
        return result

    def from_map(self, map={}):
        self.col = map.get('col')
        self.count = map.get('count')
        self.frame_count = map.get('frame_count')
        self.frame_height = map.get('frame_height')
        self.frame_width = map.get('frame_width')
        self.row = map.get('row')
        self.status = map.get('status')
        return self


class VideoPreviewTranscode(TeaModel):
    """
    *
    """
    def __init__(self, status=None, template_id=None):
        # status
        self.status = status  # type: str
        # template_id
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['status'] = self.status
        result['template_id'] = self.template_id
        return result

    def from_map(self, map={}):
        self.status = map.get('status')
        self.template_id = map.get('template_id')
        return self


class AdminListStoresModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: ListStoresResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = ListStoresResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class GetUserAccessTokenModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: AccessTokenResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = AccessTokenResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
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
        self.base_path = base_path  # type: str
        # bucket名称
        self.bucket = bucket  # type: str
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
        self.domain_id = domain_id  # type: str
        # Public访问地址
        self.endpoint = endpoint  # type: str
        # vpc访问地址
        self.internal_endpoint = internal_endpoint  # type: str
        # 地点
        self.location = location  # type: str
        # 存储归属，system表示系统提供，custom表示使用自己的存储
        self.ownership = ownership  # type: str
        # Policy授权,system类型store会将bucket权限授予当前云账号
        self.policy = policy  # type: str
        # 访问Bucket的角色ARN
        self.role_arn = role_arn  # type: str
        # store ID
        self.store_id = store_id  # type: str
        # 存储类型，当前只支持oss
        self.type = type  # type: str

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
        result['accelerate_endpoint'] = self.accelerate_endpoint
        result['base_path'] = self.base_path
        result['bucket'] = self.bucket
        result['cdn_endpoint'] = self.cdn_endpoint
        result['customized_accelerate_endpoint'] = self.customized_accelerate_endpoint
        result['customized_cdn_endpoint'] = self.customized_cdn_endpoint
        result['customized_endpoint'] = self.customized_endpoint
        result['customized_internal_endpoint'] = self.customized_internal_endpoint
        result['domain_id'] = self.domain_id
        result['endpoint'] = self.endpoint
        result['internal_endpoint'] = self.internal_endpoint
        result['location'] = self.location
        result['ownership'] = self.ownership
        result['policy'] = self.policy
        result['role_arn'] = self.role_arn
        result['store_id'] = self.store_id
        result['type'] = self.type
        return result

    def from_map(self, map={}):
        self.accelerate_endpoint = map.get('accelerate_endpoint')
        self.base_path = map.get('base_path')
        self.bucket = map.get('bucket')
        self.cdn_endpoint = map.get('cdn_endpoint')
        self.customized_accelerate_endpoint = map.get('customized_accelerate_endpoint')
        self.customized_cdn_endpoint = map.get('customized_cdn_endpoint')
        self.customized_endpoint = map.get('customized_endpoint')
        self.customized_internal_endpoint = map.get('customized_internal_endpoint')
        self.domain_id = map.get('domain_id')
        self.endpoint = map.get('endpoint')
        self.internal_endpoint = map.get('internal_endpoint')
        self.location = map.get('location')
        self.ownership = map.get('ownership')
        self.policy = map.get('policy')
        self.role_arn = map.get('role_arn')
        self.store_id = map.get('store_id')
        self.type = map.get('type')
        return self


class AdminListStoresRequest(TeaModel):
    """
    *
    """
    def __init__(self, headers=None):
        self.headers = headers  # type: dict

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class AppAccessStrategy(TeaModel):
    """
    *
    """
    def __init__(self, effect=None, except_app_id_list=None):
        self.effect = effect  # type: str
        self.except_app_id_list = except_app_id_list  # type: list

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['effect'] = self.effect
        result['except_app_id_list'] = self.except_app_id_list
        return result

    def from_map(self, map={}):
        self.effect = map.get('effect')
        self.except_app_id_list = map.get('except_app_id_list')
        return self


class AuthConfig(TeaModel):
    """
    *
    """
    def __init__(self, app_id=None, app_secret=None, callback_security=None, enable=None, endpoint=None,
                 enterprise_id=None, login_page_headers=None, login_page_template=None, login_page_vars=None):
        self.app_id = app_id  # type: str
        self.app_secret = app_secret  # type: str
        self.callback_security = callback_security  # type: bool
        self.enable = enable  # type: bool
        self.endpoint = endpoint  # type: str
        self.enterprise_id = enterprise_id  # type: str
        self.login_page_headers = login_page_headers  # type: dict
        self.login_page_template = login_page_template  # type: str
        self.login_page_vars = login_page_vars  # type: dict

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['app_id'] = self.app_id
        result['app_secret'] = self.app_secret
        result['callback_security'] = self.callback_security
        result['enable'] = self.enable
        result['endpoint'] = self.endpoint
        result['enterprise_id'] = self.enterprise_id
        result['login_page_headers'] = self.login_page_headers
        result['login_page_template'] = self.login_page_template
        result['login_page_vars'] = self.login_page_vars
        return result

    def from_map(self, map={}):
        self.app_id = map.get('app_id')
        self.app_secret = map.get('app_secret')
        self.callback_security = map.get('callback_security')
        self.enable = map.get('enable')
        self.endpoint = map.get('endpoint')
        self.enterprise_id = map.get('enterprise_id')
        self.login_page_headers = map.get('login_page_headers')
        self.login_page_template = map.get('login_page_template')
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
        self.api_cname = api_cname  # type: str
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
        self.created_at = created_at  # type: str
        # 数据 Hash 算法
        self.data_hash_name = data_hash_name  # type: str
        # Domain 描述
        self.description = description  # type: str
        # Domain ID
        self.domain_id = domain_id  # type: str
        # Domain 描述
        self.domain_name = domain_name  # type: str
        # 事件通知 MNS 匹配文件名
        self.event_filename_matches = event_filename_matches  # type: str
        # 事件通知 MNS Endpoint
        self.event_mns_endpoint = event_mns_endpoint  # type: str
        # 事件通知 MNS Topic
        self.event_mns_topic = event_mns_topic  # type: str
        # 事件名列表
        self.event_names = event_names  # type: list
        # 事件通知 Role Arn
        self.event_role_arn = event_role_arn  # type: str
        # 是否开启了自动初始化 Drive
        self.init_drive_enable = init_drive_enable  # type: bool
        # 自动初始化 Drive 大小
        self.init_drive_size = init_drive_size  # type: int
        # 自动初始化 Drive 所用 Store ID
        self.init_drive_store_id = init_drive_store_id  # type: str
        # Domain 类型
        self.mode = mode  # type: str
        # Domain 类型
        self.path_type = path_type  # type: str
        self.published_app_access_strategy = published_app_access_strategy  # type: AppAccessStrategy
        # 是否开启了分享
        self.sharable = sharable  # type: bool
        # 存储级别
        self.store_level = store_level  # type: str
        # 存储 Region 列表
        self.store_region_list = store_region_list  # type: list
        # Domain 更新时间
        self.updated_at = updated_at  # type: str

    def validate(self):
        if self.published_app_access_strategy:
            self.published_app_access_strategy.validate()

    def to_map(self):
        result = {}
        result['api_cname'] = self.api_cname
        result['auth_alipay_app_id'] = self.auth_alipay_app_id
        result['auth_alipay_enable'] = self.auth_alipay_enable
        result['auth_alipay_private_key'] = self.auth_alipay_private_key
        result['auth_config'] = self.auth_config
        result['auth_dingding_app_id'] = self.auth_dingding_app_id
        result['auth_dingding_app_secret'] = self.auth_dingding_app_secret
        result['auth_dingding_enable'] = self.auth_dingding_enable
        result['auth_endpoint_enable'] = self.auth_endpoint_enable
        result['auth_ram_app_id'] = self.auth_ram_app_id
        result['auth_ram_app_secret'] = self.auth_ram_app_secret
        result['auth_ram_enable'] = self.auth_ram_enable
        result['created_at'] = self.created_at
        result['data_hash_name'] = self.data_hash_name
        result['description'] = self.description
        result['domain_id'] = self.domain_id
        result['domain_name'] = self.domain_name
        result['event_filename_matches'] = self.event_filename_matches
        result['event_mns_endpoint'] = self.event_mns_endpoint
        result['event_mns_topic'] = self.event_mns_topic
        result['event_names'] = self.event_names
        result['event_role_arn'] = self.event_role_arn
        result['init_drive_enable'] = self.init_drive_enable
        result['init_drive_size'] = self.init_drive_size
        result['init_drive_store_id'] = self.init_drive_store_id
        result['mode'] = self.mode
        result['path_type'] = self.path_type
        if self.published_app_access_strategy is not None:
            result['published_app_access_strategy'] = self.published_app_access_strategy.to_map()
        else:
            result['published_app_access_strategy'] = None
        result['sharable'] = self.sharable
        result['store_level'] = self.store_level
        result['store_region_list'] = self.store_region_list
        result['updated_at'] = self.updated_at
        return result

    def from_map(self, map={}):
        self.api_cname = map.get('api_cname')
        self.auth_alipay_app_id = map.get('auth_alipay_app_id')
        self.auth_alipay_enable = map.get('auth_alipay_enable')
        self.auth_alipay_private_key = map.get('auth_alipay_private_key')
        self.auth_config = map.get('auth_config')
        self.auth_dingding_app_id = map.get('auth_dingding_app_id')
        self.auth_dingding_app_secret = map.get('auth_dingding_app_secret')
        self.auth_dingding_enable = map.get('auth_dingding_enable')
        self.auth_endpoint_enable = map.get('auth_endpoint_enable')
        self.auth_ram_app_id = map.get('auth_ram_app_id')
        self.auth_ram_app_secret = map.get('auth_ram_app_secret')
        self.auth_ram_enable = map.get('auth_ram_enable')
        self.created_at = map.get('created_at')
        self.data_hash_name = map.get('data_hash_name')
        self.description = map.get('description')
        self.domain_id = map.get('domain_id')
        self.domain_name = map.get('domain_name')
        self.event_filename_matches = map.get('event_filename_matches')
        self.event_mns_endpoint = map.get('event_mns_endpoint')
        self.event_mns_topic = map.get('event_mns_topic')
        self.event_names = map.get('event_names')
        self.event_role_arn = map.get('event_role_arn')
        self.init_drive_enable = map.get('init_drive_enable')
        self.init_drive_size = map.get('init_drive_size')
        self.init_drive_store_id = map.get('init_drive_store_id')
        self.mode = map.get('mode')
        self.path_type = map.get('path_type')
        if map.get('published_app_access_strategy') is not None:
            temp_model = AppAccessStrategy()
            self.published_app_access_strategy = temp_model.from_map(map['published_app_access_strategy'])
        else:
            self.published_app_access_strategy = None
        self.sharable = map.get('sharable')
        self.store_level = map.get('store_level')
        self.store_region_list = map.get('store_region_list')
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
        self.remark = remark  # type: str

    def validate(self):
        self.validate_required(self.bingding_state, 'bingding_state')
        self.validate_required(self.legal_state, 'legal_state')
        self.validate_required(self.remark, 'remark')

    def to_map(self):
        result = {}
        result['bingding_state'] = self.bingding_state
        result['legal_state'] = self.legal_state
        result['remark'] = self.remark
        return result

    def from_map(self, map={}):
        self.bingding_state = map.get('bingding_state')
        self.legal_state = map.get('legal_state')
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
        self.api_cname = api_cname  # type: str
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
        self.created_at = created_at  # type: str
        # 数据 Hash 算法
        self.data_hash_name = data_hash_name  # type: str
        # Domain 描述
        self.description = description  # type: str
        # Domain ID
        self.domain_id = domain_id  # type: str
        # Domain 描述
        self.domain_name = domain_name  # type: str
        # 事件通知 MNS 匹配文件名
        self.event_filename_matches = event_filename_matches  # type: str
        # 事件通知 MNS Endpoint
        self.event_mns_endpoint = event_mns_endpoint  # type: str
        # 事件通知 MNS Topic
        self.event_mns_topic = event_mns_topic  # type: str
        # 事件名列表
        self.event_names = event_names  # type: list
        # 事件通知 Role Arn
        self.event_role_arn = event_role_arn  # type: str
        # 是否开启了自动初始化 Drive
        self.init_drive_enable = init_drive_enable  # type: bool
        # 自动初始化 Drive 大小
        self.init_drive_size = init_drive_size  # type: int
        # 自动初始化 Drive 所用 Store ID
        self.init_drive_store_id = init_drive_store_id  # type: str
        # Domain 类型
        self.mode = mode  # type: str
        # Domain 类型
        self.path_type = path_type  # type: str
        self.published_app_access_strategy = published_app_access_strategy  # type: AppAccessStrategy
        # 是否开启了分享
        self.sharable = sharable  # type: bool
        # 存储级别
        self.store_level = store_level  # type: str
        # 存储 Region 列表
        self.store_region_list = store_region_list  # type: list
        # Domain 更新时间
        self.updated_at = updated_at  # type: str

    def validate(self):
        if self.published_app_access_strategy:
            self.published_app_access_strategy.validate()

    def to_map(self):
        result = {}
        result['api_cname'] = self.api_cname
        result['auth_alipay_app_id'] = self.auth_alipay_app_id
        result['auth_alipay_enable'] = self.auth_alipay_enable
        result['auth_alipay_private_key'] = self.auth_alipay_private_key
        result['auth_config'] = self.auth_config
        result['auth_dingding_app_id'] = self.auth_dingding_app_id
        result['auth_dingding_app_secret'] = self.auth_dingding_app_secret
        result['auth_dingding_enable'] = self.auth_dingding_enable
        result['auth_endpoint_enable'] = self.auth_endpoint_enable
        result['auth_ram_app_id'] = self.auth_ram_app_id
        result['auth_ram_app_secret'] = self.auth_ram_app_secret
        result['auth_ram_enable'] = self.auth_ram_enable
        result['created_at'] = self.created_at
        result['data_hash_name'] = self.data_hash_name
        result['description'] = self.description
        result['domain_id'] = self.domain_id
        result['domain_name'] = self.domain_name
        result['event_filename_matches'] = self.event_filename_matches
        result['event_mns_endpoint'] = self.event_mns_endpoint
        result['event_mns_topic'] = self.event_mns_topic
        result['event_names'] = self.event_names
        result['event_role_arn'] = self.event_role_arn
        result['init_drive_enable'] = self.init_drive_enable
        result['init_drive_size'] = self.init_drive_size
        result['init_drive_store_id'] = self.init_drive_store_id
        result['mode'] = self.mode
        result['path_type'] = self.path_type
        if self.published_app_access_strategy is not None:
            result['published_app_access_strategy'] = self.published_app_access_strategy.to_map()
        else:
            result['published_app_access_strategy'] = None
        result['sharable'] = self.sharable
        result['store_level'] = self.store_level
        result['store_region_list'] = self.store_region_list
        result['updated_at'] = self.updated_at
        return result

    def from_map(self, map={}):
        self.api_cname = map.get('api_cname')
        self.auth_alipay_app_id = map.get('auth_alipay_app_id')
        self.auth_alipay_enable = map.get('auth_alipay_enable')
        self.auth_alipay_private_key = map.get('auth_alipay_private_key')
        self.auth_config = map.get('auth_config')
        self.auth_dingding_app_id = map.get('auth_dingding_app_id')
        self.auth_dingding_app_secret = map.get('auth_dingding_app_secret')
        self.auth_dingding_enable = map.get('auth_dingding_enable')
        self.auth_endpoint_enable = map.get('auth_endpoint_enable')
        self.auth_ram_app_id = map.get('auth_ram_app_id')
        self.auth_ram_app_secret = map.get('auth_ram_app_secret')
        self.auth_ram_enable = map.get('auth_ram_enable')
        self.created_at = map.get('created_at')
        self.data_hash_name = map.get('data_hash_name')
        self.description = map.get('description')
        self.domain_id = map.get('domain_id')
        self.domain_name = map.get('domain_name')
        self.event_filename_matches = map.get('event_filename_matches')
        self.event_mns_endpoint = map.get('event_mns_endpoint')
        self.event_mns_topic = map.get('event_mns_topic')
        self.event_names = map.get('event_names')
        self.event_role_arn = map.get('event_role_arn')
        self.init_drive_enable = map.get('init_drive_enable')
        self.init_drive_size = map.get('init_drive_size')
        self.init_drive_store_id = map.get('init_drive_store_id')
        self.mode = map.get('mode')
        self.path_type = map.get('path_type')
        if map.get('published_app_access_strategy') is not None:
            temp_model = AppAccessStrategy()
            self.published_app_access_strategy = temp_model.from_map(map['published_app_access_strategy'])
        else:
            self.published_app_access_strategy = None
        self.sharable = map.get('sharable')
        self.store_level = map.get('store_level')
        self.store_region_list = map.get('store_region_list')
        self.updated_at = map.get('updated_at')
        return self


class DataCName(TeaModel):
    """
    *
    """
    def __init__(self, data_cname=None, location=None):
        # datacname
        self.data_cname = data_cname  # type: str
        # data location
        self.location = location  # type: str

    def validate(self):
        self.validate_required(self.data_cname, 'data_cname')
        self.validate_required(self.location, 'location')

    def to_map(self):
        result = {}
        result['data_cname'] = self.data_cname
        result['location'] = self.location
        return result

    def from_map(self, map={}):
        self.data_cname = map.get('data_cname')
        self.location = map.get('location')
        return self


class DomainCNameResponse(TeaModel):
    """
    *
    """
    def __init__(self, data_cname_list=None, domain_id=None):
        # data cname list
        self.data_cname_list = data_cname_list  # type: list
        # domain ID
        self.domain_id = domain_id  # type: str

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
        else:
            result['data_cname_list'] = None
        result['domain_id'] = self.domain_id
        return result

    def from_map(self, map={}):
        self.data_cname_list = []
        if map.get('data_cname_list') is not None:
            for k in map.get('data_cname_list'):
                temp_model = DataCName()
                self.data_cname_list.append(temp_model.from_map(k))
        else:
            self.data_cname_list = None
        self.domain_id = map.get('domain_id')
        return self


class GetAppPublicKeyResponse(TeaModel):
    """
    *
    """
    def __init__(self, app_id=None, public_key=None):
        # App ID
        self.app_id = app_id  # type: str
        # RSA加密算法的公钥, PEM格式
        self.public_key = public_key  # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.public_key, 'public_key')

    def to_map(self):
        result = {}
        result['app_id'] = self.app_id
        result['public_key'] = self.public_key
        return result

    def from_map(self, map={}):
        self.app_id = map.get('app_id')
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
        self.app_id = app_id  # type: str
        # App名称
        self.app_name = app_name  # type: str
        # App 秘钥
        self.app_secret = app_secret  # type: str
        # App 创建时间
        self.created_at = created_at  # type: str
        # App描述
        self.description = description  # type: str
        # App图标
        self.logo = logo  # type: str
        # App 提供方
        self.provider = provider  # type: str
        # App回调地址
        self.redirect_uri = redirect_uri  # type: str
        # App权限列表
        self.scope = scope  # type: list
        # App 屏幕截图
        self.screenshots = screenshots  # type: list
        # App 当前阶段
        self.stage = stage  # type: str
        # App类型
        self.type = type  # type: str
        # App 修改时间
        self.updated_at = updated_at  # type: str

    def validate(self):
        self.validate_required(self.ali_owner_id, 'ali_owner_id')
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.app_name, 'app_name')
        if self.app_name:
            self.validate_max_length(self.app_name, 'app_name', 128)
            self.validate_pattern(self.app_name, 'app_name', '[0-9a-zA-Z]+')
        self.validate_required(self.app_secret, 'app_secret')
        self.validate_required(self.created_at, 'created_at')
        self.validate_required(self.description, 'description')
        if self.description:
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
        result['ali_owner_id'] = self.ali_owner_id
        result['app_id'] = self.app_id
        result['app_name'] = self.app_name
        result['app_secret'] = self.app_secret
        result['created_at'] = self.created_at
        result['description'] = self.description
        result['logo'] = self.logo
        result['provider'] = self.provider
        result['redirect_uri'] = self.redirect_uri
        result['scope'] = self.scope
        result['screenshots'] = self.screenshots
        result['stage'] = self.stage
        result['type'] = self.type
        result['updated_at'] = self.updated_at
        return result

    def from_map(self, map={}):
        self.ali_owner_id = map.get('ali_owner_id')
        self.app_id = map.get('app_id')
        self.app_name = map.get('app_name')
        self.app_secret = map.get('app_secret')
        self.created_at = map.get('created_at')
        self.description = map.get('description')
        self.logo = map.get('logo')
        self.provider = map.get('provider')
        self.redirect_uri = map.get('redirect_uri')
        self.scope = map.get('scope')
        self.screenshots = map.get('screenshots')
        self.stage = map.get('stage')
        self.type = map.get('type')
        self.updated_at = map.get('updated_at')
        return self


class GetBizCNameInfoResponse(TeaModel):
    """
    *
    """
    def __init__(self, biz_cname=None, cert_id=None, cert_name=None, cname_status=None, cname_type=None,
                 domain_id=None, is_vpc=None):
        # biz cname
        self.biz_cname = biz_cname  # type: str
        # cert name
        self.cert_id = cert_id  # type: str
        # cert name
        self.cert_name = cert_name  # type: str
        self.cname_status = cname_status  # type: CNameStatus
        # cname type
        self.cname_type = cname_type  # type: str
        # domain ID
        self.domain_id = domain_id  # type: str
        # is vpc
        self.is_vpc = is_vpc  # type: bool

    def validate(self):
        if self.cname_status:
            self.cname_status.validate()
        self.validate_required(self.domain_id, 'domain_id')

    def to_map(self):
        result = {}
        result['biz_cname'] = self.biz_cname
        result['cert_id'] = self.cert_id
        result['cert_name'] = self.cert_name
        if self.cname_status is not None:
            result['cname_status'] = self.cname_status.to_map()
        else:
            result['cname_status'] = None
        result['cname_type'] = self.cname_type
        result['domain_id'] = self.domain_id
        result['is_vpc'] = self.is_vpc
        return result

    def from_map(self, map={}):
        self.biz_cname = map.get('biz_cname')
        self.cert_id = map.get('cert_id')
        self.cert_name = map.get('cert_name')
        if map.get('cname_status') is not None:
            temp_model = CNameStatus()
            self.cname_status = temp_model.from_map(map['cname_status'])
        else:
            self.cname_status = None
        self.cname_type = map.get('cname_type')
        self.domain_id = map.get('domain_id')
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
        self.api_cname = api_cname  # type: str
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
        self.created_at = created_at  # type: str
        # 数据 Hash 算法
        self.data_hash_name = data_hash_name  # type: str
        # Domain 描述
        self.description = description  # type: str
        # Domain ID
        self.domain_id = domain_id  # type: str
        # Domain 描述
        self.domain_name = domain_name  # type: str
        # 事件通知 MNS 匹配文件名
        self.event_filename_matches = event_filename_matches  # type: str
        # 事件通知 MNS Endpoint
        self.event_mns_endpoint = event_mns_endpoint  # type: str
        # 事件通知 MNS Topic
        self.event_mns_topic = event_mns_topic  # type: str
        # 事件名列表
        self.event_names = event_names  # type: list
        # 事件通知 Role Arn
        self.event_role_arn = event_role_arn  # type: str
        # 是否开启了自动初始化 Drive
        self.init_drive_enable = init_drive_enable  # type: bool
        # 自动初始化 Drive 大小
        self.init_drive_size = init_drive_size  # type: int
        # 自动初始化 Drive 所用 Store ID
        self.init_drive_store_id = init_drive_store_id  # type: str
        # Domain 类型
        self.mode = mode  # type: str
        # Domain 类型
        self.path_type = path_type  # type: str
        self.published_app_access_strategy = published_app_access_strategy  # type: AppAccessStrategy
        # 是否开启了分享
        self.sharable = sharable  # type: bool
        # 存储级别
        self.store_level = store_level  # type: str
        # 存储 Region 列表
        self.store_region_list = store_region_list  # type: list
        # Domain 更新时间
        self.updated_at = updated_at  # type: str

    def validate(self):
        if self.published_app_access_strategy:
            self.published_app_access_strategy.validate()

    def to_map(self):
        result = {}
        result['api_cname'] = self.api_cname
        result['auth_alipay_app_id'] = self.auth_alipay_app_id
        result['auth_alipay_enable'] = self.auth_alipay_enable
        result['auth_alipay_private_key'] = self.auth_alipay_private_key
        result['auth_config'] = self.auth_config
        result['auth_dingding_app_id'] = self.auth_dingding_app_id
        result['auth_dingding_app_secret'] = self.auth_dingding_app_secret
        result['auth_dingding_enable'] = self.auth_dingding_enable
        result['auth_endpoint_enable'] = self.auth_endpoint_enable
        result['auth_ram_app_id'] = self.auth_ram_app_id
        result['auth_ram_app_secret'] = self.auth_ram_app_secret
        result['auth_ram_enable'] = self.auth_ram_enable
        result['created_at'] = self.created_at
        result['data_hash_name'] = self.data_hash_name
        result['description'] = self.description
        result['domain_id'] = self.domain_id
        result['domain_name'] = self.domain_name
        result['event_filename_matches'] = self.event_filename_matches
        result['event_mns_endpoint'] = self.event_mns_endpoint
        result['event_mns_topic'] = self.event_mns_topic
        result['event_names'] = self.event_names
        result['event_role_arn'] = self.event_role_arn
        result['init_drive_enable'] = self.init_drive_enable
        result['init_drive_size'] = self.init_drive_size
        result['init_drive_store_id'] = self.init_drive_store_id
        result['mode'] = self.mode
        result['path_type'] = self.path_type
        if self.published_app_access_strategy is not None:
            result['published_app_access_strategy'] = self.published_app_access_strategy.to_map()
        else:
            result['published_app_access_strategy'] = None
        result['sharable'] = self.sharable
        result['store_level'] = self.store_level
        result['store_region_list'] = self.store_region_list
        result['updated_at'] = self.updated_at
        return result

    def from_map(self, map={}):
        self.api_cname = map.get('api_cname')
        self.auth_alipay_app_id = map.get('auth_alipay_app_id')
        self.auth_alipay_enable = map.get('auth_alipay_enable')
        self.auth_alipay_private_key = map.get('auth_alipay_private_key')
        self.auth_config = map.get('auth_config')
        self.auth_dingding_app_id = map.get('auth_dingding_app_id')
        self.auth_dingding_app_secret = map.get('auth_dingding_app_secret')
        self.auth_dingding_enable = map.get('auth_dingding_enable')
        self.auth_endpoint_enable = map.get('auth_endpoint_enable')
        self.auth_ram_app_id = map.get('auth_ram_app_id')
        self.auth_ram_app_secret = map.get('auth_ram_app_secret')
        self.auth_ram_enable = map.get('auth_ram_enable')
        self.created_at = map.get('created_at')
        self.data_hash_name = map.get('data_hash_name')
        self.description = map.get('description')
        self.domain_id = map.get('domain_id')
        self.domain_name = map.get('domain_name')
        self.event_filename_matches = map.get('event_filename_matches')
        self.event_mns_endpoint = map.get('event_mns_endpoint')
        self.event_mns_topic = map.get('event_mns_topic')
        self.event_names = map.get('event_names')
        self.event_role_arn = map.get('event_role_arn')
        self.init_drive_enable = map.get('init_drive_enable')
        self.init_drive_size = map.get('init_drive_size')
        self.init_drive_store_id = map.get('init_drive_store_id')
        self.mode = map.get('mode')
        self.path_type = map.get('path_type')
        if map.get('published_app_access_strategy') is not None:
            temp_model = AppAccessStrategy()
            self.published_app_access_strategy = temp_model.from_map(map['published_app_access_strategy'])
        else:
            self.published_app_access_strategy = None
        self.sharable = map.get('sharable')
        self.store_level = map.get('store_level')
        self.store_region_list = map.get('store_region_list')
        self.updated_at = map.get('updated_at')
        return self


class GetUserAccessTokenRequest(TeaModel):
    """
    *
    """
    def __init__(self, headers=None, role=None, user_id=None):
        self.headers = headers  # type: dict
        # 角色
        self.role = role  # type: str
        # 用户 ID
        self.user_id = user_id  # type: str

    def validate(self):
        self.validate_required(self.user_id, 'user_id')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['role'] = self.role
        result['user_id'] = self.user_id
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.role = map.get('role')
        self.user_id = map.get('user_id')
        return self


class ListAppsResponse(TeaModel):
    """
    *
    """
    def __init__(self, items=None, next_marker=None):
        # App 列表
        self.items = items  # type: list
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
        else:
            result['items'] = None
        result['next_marker'] = self.next_marker
        return result

    def from_map(self, map={}):
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = GetAppResponse()
                self.items.append(temp_model.from_map(k))
        else:
            self.items = None
        self.next_marker = map.get('next_marker')
        return self


class ListDomainCORSRuleResponse(TeaModel):
    """
    list domain cors response
    """
    def __init__(self, cors_rule_list=None, domain_id=None):
        # cors rule 列表
        self.cors_rule_list = cors_rule_list  # type: list
        # Domain ID
        self.domain_id = domain_id  # type: str

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
        else:
            result['cors_rule_list'] = None
        result['domain_id'] = self.domain_id
        return result

    def from_map(self, map={}):
        self.cors_rule_list = []
        if map.get('cors_rule_list') is not None:
            for k in map.get('cors_rule_list'):
                temp_model = CorsRule()
                self.cors_rule_list.append(temp_model.from_map(k))
        else:
            self.cors_rule_list = None
        self.domain_id = map.get('domain_id')
        return self


class ListDomainsResponse(TeaModel):
    """
    list domain response
    """
    def __init__(self, items=None, next_marker=None):
        # domain 列表
        self.items = items  # type: list
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
        else:
            result['items'] = None
        result['next_marker'] = self.next_marker
        return result

    def from_map(self, map={}):
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = BaseDomainResponse()
                self.items.append(temp_model.from_map(k))
        else:
            self.items = None
        self.next_marker = map.get('next_marker')
        return self


class ListStoresResponse(TeaModel):
    """
    *
    """
    def __init__(self, items=None):
        # Store 列表
        self.items = items  # type: list

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
        else:
            result['items'] = None
        return result

    def from_map(self, map={}):
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = Store()
                self.items.append(temp_model.from_map(k))
        else:
            self.items = None
        return self


class SetBizCNameCertResponse(TeaModel):
    """
    *
    """
    def __init__(self, biz_cname=None, cert_name=None, cname_type=None, domain_id=None, is_vpc=None):
        # biz cname
        self.biz_cname = biz_cname  # type: str
        # cert name
        self.cert_name = cert_name  # type: str
        # cname type
        self.cname_type = cname_type  # type: str
        # domain ID
        self.domain_id = domain_id  # type: str
        # is vpc
        self.is_vpc = is_vpc  # type: bool

    def validate(self):
        self.validate_required(self.domain_id, 'domain_id')

    def to_map(self):
        result = {}
        result['biz_cname'] = self.biz_cname
        result['cert_name'] = self.cert_name
        result['cname_type'] = self.cname_type
        result['domain_id'] = self.domain_id
        result['is_vpc'] = self.is_vpc
        return result

    def from_map(self, map={}):
        self.biz_cname = map.get('biz_cname')
        self.cert_name = map.get('cert_name')
        self.cname_type = map.get('cname_type')
        self.domain_id = map.get('domain_id')
        self.is_vpc = map.get('is_vpc')
        return self


class SetBizCNameResponse(TeaModel):
    """
    *
    """
    def __init__(self, biz_cname=None, cname_status=None, cname_type=None, domain_id=None, is_vpc=None):
        # biz cname
        self.biz_cname = biz_cname  # type: str
        self.cname_status = cname_status  # type: CNameStatus
        # cname type
        self.cname_type = cname_type  # type: str
        # domain ID
        self.domain_id = domain_id  # type: str
        # is vpc
        self.is_vpc = is_vpc  # type: bool

    def validate(self):
        if self.cname_status:
            self.cname_status.validate()
        self.validate_required(self.domain_id, 'domain_id')

    def to_map(self):
        result = {}
        result['biz_cname'] = self.biz_cname
        if self.cname_status is not None:
            result['cname_status'] = self.cname_status.to_map()
        else:
            result['cname_status'] = None
        result['cname_type'] = self.cname_type
        result['domain_id'] = self.domain_id
        result['is_vpc'] = self.is_vpc
        return result

    def from_map(self, map={}):
        self.biz_cname = map.get('biz_cname')
        if map.get('cname_status') is not None:
            temp_model = CNameStatus()
            self.cname_status = temp_model.from_map(map['cname_status'])
        else:
            self.cname_status = None
        self.cname_type = map.get('cname_type')
        self.domain_id = map.get('domain_id')
        self.is_vpc = map.get('is_vpc')
        return self


class SetDataCNameResponse(TeaModel):
    """
    *
    """
    def __init__(self, data_cname=None, domain_id=None, location=None):
        # datacname
        self.data_cname = data_cname  # type: str
        # domain ID
        self.domain_id = domain_id  # type: str
        # data location
        self.location = location  # type: str

    def validate(self):
        self.validate_required(self.data_cname, 'data_cname')
        self.validate_required(self.domain_id, 'domain_id')
        self.validate_required(self.location, 'location')

    def to_map(self):
        result = {}
        result['data_cname'] = self.data_cname
        result['domain_id'] = self.domain_id
        result['location'] = self.location
        return result

    def from_map(self, map={}):
        self.data_cname = map.get('data_cname')
        self.domain_id = map.get('domain_id')
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
        self.base_path = base_path  # type: str
        # bucket名称
        self.bucket = bucket  # type: str
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
        self.endpoint = endpoint  # type: str
        # vpc访问地址
        self.internal_endpoint = internal_endpoint  # type: str
        # 地点
        self.location = location  # type: str
        # 存储归属，system表示系统提供，custom表示使用自己的存储
        self.ownership = ownership  # type: str
        # Policy授权,system类型store会将bucket权限授予当前云账号
        self.policy = policy  # type: str
        # 访问Bucket的角色ARN
        self.role_arn = role_arn  # type: str
        # store ID
        self.store_id = store_id  # type: str
        # 存储类型，当前只支持oss
        self.type = type  # type: str

    def validate(self):
        self.validate_required(self.bucket, 'bucket')
        self.validate_required(self.endpoint, 'endpoint')
        self.validate_required(self.ownership, 'ownership')
        self.validate_required(self.policy, 'policy')
        self.validate_required(self.store_id, 'store_id')
        self.validate_required(self.type, 'type')

    def to_map(self):
        result = {}
        result['accelerate_endpoint'] = self.accelerate_endpoint
        result['base_path'] = self.base_path
        result['bucket'] = self.bucket
        result['cdn_endpoint'] = self.cdn_endpoint
        result['customized_accelerate_endpoint'] = self.customized_accelerate_endpoint
        result['customized_cdn_endpoint'] = self.customized_cdn_endpoint
        result['customized_endpoint'] = self.customized_endpoint
        result['customized_internal_endpoint'] = self.customized_internal_endpoint
        result['endpoint'] = self.endpoint
        result['internal_endpoint'] = self.internal_endpoint
        result['location'] = self.location
        result['ownership'] = self.ownership
        result['policy'] = self.policy
        result['role_arn'] = self.role_arn
        result['store_id'] = self.store_id
        result['type'] = self.type
        return result

    def from_map(self, map={}):
        self.accelerate_endpoint = map.get('accelerate_endpoint')
        self.base_path = map.get('base_path')
        self.bucket = map.get('bucket')
        self.cdn_endpoint = map.get('cdn_endpoint')
        self.customized_accelerate_endpoint = map.get('customized_accelerate_endpoint')
        self.customized_cdn_endpoint = map.get('customized_cdn_endpoint')
        self.customized_endpoint = map.get('customized_endpoint')
        self.customized_internal_endpoint = map.get('customized_internal_endpoint')
        self.endpoint = map.get('endpoint')
        self.internal_endpoint = map.get('internal_endpoint')
        self.location = map.get('location')
        self.ownership = map.get('ownership')
        self.policy = map.get('policy')
        self.role_arn = map.get('role_arn')
        self.store_id = map.get('store_id')
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
        self.api_cname = api_cname  # type: str
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
        self.created_at = created_at  # type: str
        # 数据 Hash 算法
        self.data_hash_name = data_hash_name  # type: str
        # Domain 描述
        self.description = description  # type: str
        # Domain ID
        self.domain_id = domain_id  # type: str
        # Domain 描述
        self.domain_name = domain_name  # type: str
        # 事件通知 MNS 匹配文件名
        self.event_filename_matches = event_filename_matches  # type: str
        # 事件通知 MNS Endpoint
        self.event_mns_endpoint = event_mns_endpoint  # type: str
        # 事件通知 MNS Topic
        self.event_mns_topic = event_mns_topic  # type: str
        # 事件名列表
        self.event_names = event_names  # type: list
        # 事件通知 Role Arn
        self.event_role_arn = event_role_arn  # type: str
        # 是否开启了自动初始化 Drive
        self.init_drive_enable = init_drive_enable  # type: bool
        # 自动初始化 Drive 大小
        self.init_drive_size = init_drive_size  # type: int
        # 自动初始化 Drive 所用 Store ID
        self.init_drive_store_id = init_drive_store_id  # type: str
        # Domain 类型
        self.mode = mode  # type: str
        # Domain 类型
        self.path_type = path_type  # type: str
        self.published_app_access_strategy = published_app_access_strategy  # type: AppAccessStrategy
        # 是否开启了分享
        self.sharable = sharable  # type: bool
        # 存储级别
        self.store_level = store_level  # type: str
        # 存储 Region 列表
        self.store_region_list = store_region_list  # type: list
        # Domain 更新时间
        self.updated_at = updated_at  # type: str

    def validate(self):
        if self.published_app_access_strategy:
            self.published_app_access_strategy.validate()

    def to_map(self):
        result = {}
        result['api_cname'] = self.api_cname
        result['auth_alipay_app_id'] = self.auth_alipay_app_id
        result['auth_alipay_enable'] = self.auth_alipay_enable
        result['auth_alipay_private_key'] = self.auth_alipay_private_key
        result['auth_config'] = self.auth_config
        result['auth_dingding_app_id'] = self.auth_dingding_app_id
        result['auth_dingding_app_secret'] = self.auth_dingding_app_secret
        result['auth_dingding_enable'] = self.auth_dingding_enable
        result['auth_endpoint_enable'] = self.auth_endpoint_enable
        result['auth_ram_app_id'] = self.auth_ram_app_id
        result['auth_ram_app_secret'] = self.auth_ram_app_secret
        result['auth_ram_enable'] = self.auth_ram_enable
        result['created_at'] = self.created_at
        result['data_hash_name'] = self.data_hash_name
        result['description'] = self.description
        result['domain_id'] = self.domain_id
        result['domain_name'] = self.domain_name
        result['event_filename_matches'] = self.event_filename_matches
        result['event_mns_endpoint'] = self.event_mns_endpoint
        result['event_mns_topic'] = self.event_mns_topic
        result['event_names'] = self.event_names
        result['event_role_arn'] = self.event_role_arn
        result['init_drive_enable'] = self.init_drive_enable
        result['init_drive_size'] = self.init_drive_size
        result['init_drive_store_id'] = self.init_drive_store_id
        result['mode'] = self.mode
        result['path_type'] = self.path_type
        if self.published_app_access_strategy is not None:
            result['published_app_access_strategy'] = self.published_app_access_strategy.to_map()
        else:
            result['published_app_access_strategy'] = None
        result['sharable'] = self.sharable
        result['store_level'] = self.store_level
        result['store_region_list'] = self.store_region_list
        result['updated_at'] = self.updated_at
        return result

    def from_map(self, map={}):
        self.api_cname = map.get('api_cname')
        self.auth_alipay_app_id = map.get('auth_alipay_app_id')
        self.auth_alipay_enable = map.get('auth_alipay_enable')
        self.auth_alipay_private_key = map.get('auth_alipay_private_key')
        self.auth_config = map.get('auth_config')
        self.auth_dingding_app_id = map.get('auth_dingding_app_id')
        self.auth_dingding_app_secret = map.get('auth_dingding_app_secret')
        self.auth_dingding_enable = map.get('auth_dingding_enable')
        self.auth_endpoint_enable = map.get('auth_endpoint_enable')
        self.auth_ram_app_id = map.get('auth_ram_app_id')
        self.auth_ram_app_secret = map.get('auth_ram_app_secret')
        self.auth_ram_enable = map.get('auth_ram_enable')
        self.created_at = map.get('created_at')
        self.data_hash_name = map.get('data_hash_name')
        self.description = map.get('description')
        self.domain_id = map.get('domain_id')
        self.domain_name = map.get('domain_name')
        self.event_filename_matches = map.get('event_filename_matches')
        self.event_mns_endpoint = map.get('event_mns_endpoint')
        self.event_mns_topic = map.get('event_mns_topic')
        self.event_names = map.get('event_names')
        self.event_role_arn = map.get('event_role_arn')
        self.init_drive_enable = map.get('init_drive_enable')
        self.init_drive_size = map.get('init_drive_size')
        self.init_drive_store_id = map.get('init_drive_store_id')
        self.mode = map.get('mode')
        self.path_type = map.get('path_type')
        if map.get('published_app_access_strategy') is not None:
            temp_model = AppAccessStrategy()
            self.published_app_access_strategy = temp_model.from_map(map['published_app_access_strategy'])
        else:
            self.published_app_access_strategy = None
        self.sharable = map.get('sharable')
        self.store_level = map.get('store_level')
        self.store_region_list = map.get('store_region_list')
        self.updated_at = map.get('updated_at')
        return self


class GetAsyncTaskInfoModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: GetAsyncTaskResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetAsyncTaskResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class BatchOperationModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: BatchResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = BatchResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class CreateDriveModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: CreateDriveResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = CreateDriveResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class DeleteDriveModel(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class GetDriveModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: GetDriveResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetDriveResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class GetDefaultDriveModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: GetDriveResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetDriveResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class ListDrivesModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: ListDriveResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = ListDriveResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class ListMyDrivesModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: ListDriveResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = ListDriveResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class UpdateDriveModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: UpdateDriveResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = UpdateDriveResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class CompleteFileModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: CompleteFileResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = CompleteFileResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class CopyFileModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: CopyFileResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = CopyFileResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class CreateFileModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: CreateFileResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = CreateFileResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class DeleteFileModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: DeleteFileResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = DeleteFileResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class GetFileModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: GetFileResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetFileResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class GetFileByPathModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: GetFileByPathResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetFileByPathResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class GetDownloadUrlModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: GetDownloadUrlResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetDownloadUrlResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class GetLastCursorModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: GetLastCursorResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetLastCursorResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class GetMediaPlayUrlModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: GetMediaPlayURLResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetMediaPlayURLResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class GetOfficePreviewUrlModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: GetOfficePreviewUrlResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetOfficePreviewUrlResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class GetUploadUrlModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: GetUploadUrlResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetUploadUrlResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class GetVideoPreviewSpriteUrlModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: GetVideoPreviewSpriteURLResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetVideoPreviewSpriteURLResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class GetVideoPreviewUrlModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: GetVideoPreviewURLResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetVideoPreviewURLResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class ListFileModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: ListFileResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = ListFileResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class ListFileByAnonymousModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: ListByAnonymousResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = ListByAnonymousResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class ListFileByCustomIndexKeyModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: ListFileResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = ListFileResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class ListFileDeltaModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: ListFileDeltaResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = ListFileDeltaResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class ListUploadedPartsModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: ListUploadedPartResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = ListUploadedPartResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class MoveFileModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: MoveFileResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = MoveFileResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class ScanFileMetaModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: ScanFileMetaResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = ScanFileMetaResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class SearchFileModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: SearchFileResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = SearchFileResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class UpdateFileModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: UpdateFileMetaResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = UpdateFileMetaResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class CancelShareLinkModel(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class CreateShareLinkModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: CreateShareLinkResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = CreateShareLinkResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class GetShareIdModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: GetShareLinkIDResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetShareLinkIDResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class GetShareTokenModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: GetShareLinkTokenResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetShareLinkTokenResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class ListShareLinkModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: ListShareLinkResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = ListShareLinkResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class BaseCompleteFileRequest(TeaModel):
    """
    complete file request
    """
    def __init__(self, addition_data=None, drive_id=None, part_info_list=None, upload_id=None):
        # addition_data
        self.addition_data = addition_data  # type: dict
        # drive_id
        self.drive_id = drive_id  # type: str
        # part_info_list
        self.part_info_list = part_info_list  # type: list
        # upload_id
        self.upload_id = upload_id  # type: str

    def validate(self):
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.part_info_list:
            for k in self.part_info_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['addition_data'] = self.addition_data
        result['drive_id'] = self.drive_id
        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k in self.part_info_list:
                result['part_info_list'].append(k.to_map() if k else None)
        else:
            result['part_info_list'] = None
        result['upload_id'] = self.upload_id
        return result

    def from_map(self, map={}):
        self.addition_data = map.get('addition_data')
        self.drive_id = map.get('drive_id')
        self.part_info_list = []
        if map.get('part_info_list') is not None:
            for k in map.get('part_info_list'):
                temp_model = UploadPartInfo()
                self.part_info_list.append(temp_model.from_map(k))
        else:
            self.part_info_list = None
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
        self.name = name  # type: str
        # part_info_list
        self.part_info_list = part_info_list  # type: list
        # Size
        self.size = size  # type: int
        # Type
        self.type = type  # type: str

    def validate(self):
        self.validate_required(self.name, 'name')
        if self.name:
            self.validate_max_length(self.name, 'name', 1024)
        if self.part_info_list:
            for k in self.part_info_list:
                if k:
                    k.validate()
        self.validate_required(self.type, 'type')

    def to_map(self):
        result = {}
        result['addition_data'] = self.addition_data
        result['content_md5'] = self.content_md_5
        result['content_type'] = self.content_type
        result['name'] = self.name
        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k in self.part_info_list:
                result['part_info_list'].append(k.to_map() if k else None)
        else:
            result['part_info_list'] = None
        result['size'] = self.size
        result['type'] = self.type
        return result

    def from_map(self, map={}):
        self.addition_data = map.get('addition_data')
        self.content_md_5 = map.get('content_md5')
        self.content_type = map.get('content_type')
        self.name = map.get('name')
        self.part_info_list = []
        if map.get('part_info_list') is not None:
            for k in map.get('part_info_list'):
                temp_model = UploadPartInfo()
                self.part_info_list.append(temp_model.from_map(k))
        else:
            self.part_info_list = None
        self.size = map.get('size')
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
        result['addition_data'] = self.addition_data
        return result

    def from_map(self, map={}):
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
        self.drive_id = drive_id  # type: str
        # upload_part_list
        self.part_info_list = part_info_list  # type: list
        # upload_id
        self.upload_id = upload_id  # type: str

    def validate(self):
        if self.content_md_5:
            self.validate_max_length(self.content_md_5, 'content_md_5', 32)
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.part_info_list:
            for k in self.part_info_list:
                if k:
                    k.validate()
        self.validate_required(self.upload_id, 'upload_id')

    def to_map(self):
        result = {}
        result['content_md5'] = self.content_md_5
        result['drive_id'] = self.drive_id
        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k in self.part_info_list:
                result['part_info_list'].append(k.to_map() if k else None)
        else:
            result['part_info_list'] = None
        result['upload_id'] = self.upload_id
        return result

    def from_map(self, map={}):
        self.content_md_5 = map.get('content_md5')
        self.drive_id = map.get('drive_id')
        self.part_info_list = []
        if map.get('part_info_list') is not None:
            for k in map.get('part_info_list'):
                temp_model = UploadPartInfo()
                self.part_info_list.append(temp_model.from_map(k))
        else:
            self.part_info_list = None
        self.upload_id = map.get('upload_id')
        return self


class BaseListFileRequest(TeaModel):
    """
    list file request
    """
    def __init__(self, drive_id=None, image_thumbnail_process=None, image_url_process=None, limit=None, marker=None,
                 video_thumbnail_process=None):
        # drive_id
        self.drive_id = drive_id  # type: str
        # image_thumbnail_process
        self.image_thumbnail_process = image_thumbnail_process  # type: str
        # image_url_process
        self.image_url_process = image_url_process  # type: str
        # limit
        self.limit = limit  # type: int
        # marker
        self.marker = marker  # type: str
        # video_thumbnail_process
        # type:string
        self.video_thumbnail_process = video_thumbnail_process  # type: str

    def validate(self):
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.limit:
            self.validate_pattern(self.limit, 'limit', '[0-9]{1,3}')

    def to_map(self):
        result = {}
        result['drive_id'] = self.drive_id
        result['image_thumbnail_process'] = self.image_thumbnail_process
        result['image_url_process'] = self.image_url_process
        result['limit'] = self.limit
        result['marker'] = self.marker
        result['video_thumbnail_process'] = self.video_thumbnail_process
        return result

    def from_map(self, map={}):
        self.drive_id = map.get('drive_id')
        self.image_thumbnail_process = map.get('image_thumbnail_process')
        self.image_url_process = map.get('image_url_process')
        self.limit = map.get('limit')
        self.marker = map.get('marker')
        self.video_thumbnail_process = map.get('video_thumbnail_process')
        return self


class BaseMoveFileRequest(TeaModel):
    """
    文件移动请求
    """
    def __init__(self, drive_id=None, new_name=None, overwrite=None):
        # drive_id
        self.drive_id = drive_id  # type: str
        # new_name
        self.new_name = new_name  # type: str
        # overwrite
        # type: boolean
        self.overwrite = overwrite  # type: bool

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.new_name:
            self.validate_max_length(self.new_name, 'new_name', 1024)

    def to_map(self):
        result = {}
        result['drive_id'] = self.drive_id
        result['new_name'] = self.new_name
        result['overwrite'] = self.overwrite
        return result

    def from_map(self, map={}):
        self.drive_id = map.get('drive_id')
        self.new_name = map.get('new_name')
        self.overwrite = map.get('overwrite')
        return self


class BatchRequest(TeaModel):
    """
    批处理
    """
    def __init__(self, headers=None, requests=None, resource=None):
        self.headers = headers  # type: dict
        # Requests 请求合集
        self.requests = requests  # type: list
        # 支持的资源类型
        self.resource = resource  # type: str

    def validate(self):
        self.validate_required(self.requests, 'requests')
        if self.requests:
            for k in self.requests:
                if k:
                    k.validate()
        self.validate_required(self.resource, 'resource')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['requests'] = []
        if self.requests is not None:
            for k in self.requests:
                result['requests'].append(k.to_map() if k else None)
        else:
            result['requests'] = None
        result['resource'] = self.resource
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.requests = []
        if map.get('requests') is not None:
            for k in map.get('requests'):
                temp_model = BatchSubRequest()
                self.requests.append(temp_model.from_map(k))
        else:
            self.requests = None
        self.resource = map.get('resource')
        return self


class BatchSubRequest(TeaModel):
    """
    *
    """
    def __init__(self, body=None, headers=None, id=None, method=None, url=None):
        # body 子请求的请求参数 json 字符串，可参考对于子请求文档, 当指定了body 必须传headers ： "Content-Type" 对应的类型，目前子请求入参是"application/json"
        self.body = body  # type: dict
        # headers 请求头，表示body传入数据的类型
        self.headers = headers  # type: dict
        # id 用于request 和 response关联， 不允许重复
        self.id = id  # type: str
        # method
        self.method = method  # type: str
        # url 子请求的api path路径， 可参考对于子请求文档
        self.url = url  # type: str

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.method, 'method')
        self.validate_required(self.url, 'url')

    def to_map(self):
        result = {}
        result['body'] = self.body
        result['headers'] = self.headers
        result['id'] = self.id
        result['method'] = self.method
        result['url'] = self.url
        return result

    def from_map(self, map={}):
        self.body = map.get('body')
        self.headers = map.get('headers')
        self.id = map.get('id')
        self.method = map.get('method')
        self.url = map.get('url')
        return self


class CancelShareLinkRequest(TeaModel):
    """
    cancel_share_link request
    """
    def __init__(self, headers=None, share_id=None):
        self.headers = headers  # type: dict
        # share_id
        self.share_id = share_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['share_id'] = self.share_id
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.share_id = map.get('share_id')
        return self


class CompleteFileRequest(TeaModel):
    """
    合并文件上传任务
    """
    def __init__(self, headers=None, addition_data=None, drive_id=None, file_id=None, part_info_list=None,
                 upload_id=None):
        self.headers = headers  # type: dict
        # addition_data
        self.addition_data = addition_data  # type: dict
        # drive_id
        self.drive_id = drive_id  # type: str
        # file_id
        self.file_id = file_id  # type: str
        # part_info_list
        self.part_info_list = part_info_list  # type: list
        # upload_id
        self.upload_id = upload_id  # type: str

    def validate(self):
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_id, 'file_id')
        if self.file_id:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9]{1,50}')
        if self.part_info_list:
            for k in self.part_info_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['addition_data'] = self.addition_data
        result['drive_id'] = self.drive_id
        result['file_id'] = self.file_id
        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k in self.part_info_list:
                result['part_info_list'].append(k.to_map() if k else None)
        else:
            result['part_info_list'] = None
        result['upload_id'] = self.upload_id
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.addition_data = map.get('addition_data')
        self.drive_id = map.get('drive_id')
        self.file_id = map.get('file_id')
        self.part_info_list = []
        if map.get('part_info_list') is not None:
            for k in map.get('part_info_list'):
                temp_model = UploadPartInfo()
                self.part_info_list.append(temp_model.from_map(k))
        else:
            self.part_info_list = None
        self.upload_id = map.get('upload_id')
        return self


class CopyFileRequest(TeaModel):
    """
    文件拷贝
    """
    def __init__(self, headers=None, auto_rename=None, drive_id=None, file_id=None, new_name=None, share_id=None,
                 to_drive_id=None, to_parent_file_id=None):
        self.headers = headers  # type: dict
        # auto_rename
        # type: boolean
        self.auto_rename = auto_rename  # type: bool
        # drive_id
        self.drive_id = drive_id  # type: str
        # file_id
        self.file_id = file_id  # type: str
        # new_name
        self.new_name = new_name  # type: str
        # share_id, either share_id or drive_id is required
        self.share_id = share_id  # type: str
        # to_drive_id
        self.to_drive_id = to_drive_id  # type: str
        # to_parent_file_id
        self.to_parent_file_id = to_parent_file_id  # type: str

    def validate(self):
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_id, 'file_id')
        if self.file_id:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9.-_]{1,50}')
        if self.new_name:
            self.validate_max_length(self.new_name, 'new_name', 1024)
        if self.to_drive_id:
            self.validate_pattern(self.to_drive_id, 'to_drive_id', '[0-9]+')
        self.validate_required(self.to_parent_file_id, 'to_parent_file_id')
        if self.to_parent_file_id:
            self.validate_max_length(self.to_parent_file_id, 'to_parent_file_id', 50)
            self.validate_pattern(self.to_parent_file_id, 'to_parent_file_id', '[a-z0-9.-_]{1,50}')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['auto_rename'] = self.auto_rename
        result['drive_id'] = self.drive_id
        result['file_id'] = self.file_id
        result['new_name'] = self.new_name
        result['share_id'] = self.share_id
        result['to_drive_id'] = self.to_drive_id
        result['to_parent_file_id'] = self.to_parent_file_id
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.auto_rename = map.get('auto_rename')
        self.drive_id = map.get('drive_id')
        self.file_id = map.get('file_id')
        self.new_name = map.get('new_name')
        self.share_id = map.get('share_id')
        self.to_drive_id = map.get('to_drive_id')
        self.to_parent_file_id = map.get('to_parent_file_id')
        return self


class CreateDriveRequest(TeaModel):
    """
    create drive request
    """
    def __init__(self, headers=None, default=None, description=None, drive_name=None, drive_type=None,
                 encrypt_mode=None, owner=None, relative_path=None, status=None, store_id=None, total_size=None):
        self.headers = headers  # type: dict
        # 是否默认drive, 只允许设置一个默认drive
        self.default = default  # type: bool
        # 描述信息
        self.description = description  # type: str
        # Drive 名称
        self.drive_name = drive_name  # type: str
        # Drive类型
        self.drive_type = drive_type  # type: str
        self.encrypt_mode = encrypt_mode  # type: str
        # 所属者
        self.owner = owner  # type: str
        # domain的PathType为OSSPath时必选。 Drive存储基于store的相对路径
        self.relative_path = relative_path  # type: str
        # 状态
        self.status = status  # type: str
        # StoreID , domain的PathType为OSSPath时必选
        self.store_id = store_id  # type: str
        # 总大小,单位Byte [如果设置 -1 代表不限制]
        self.total_size = total_size  # type: int

    def validate(self):
        if self.description:
            self.validate_max_length(self.description, 'description', 1024)
        self.validate_required(self.drive_name, 'drive_name')
        if self.drive_name:
            self.validate_max_length(self.drive_name, 'drive_name', 1024)
        self.validate_required(self.owner, 'owner')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['default'] = self.default
        result['description'] = self.description
        result['drive_name'] = self.drive_name
        result['drive_type'] = self.drive_type
        result['encrypt_mode'] = self.encrypt_mode
        result['owner'] = self.owner
        result['relative_path'] = self.relative_path
        result['status'] = self.status
        result['store_id'] = self.store_id
        result['total_size'] = self.total_size
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.default = map.get('default')
        self.description = map.get('description')
        self.drive_name = map.get('drive_name')
        self.drive_type = map.get('drive_type')
        self.encrypt_mode = map.get('encrypt_mode')
        self.owner = map.get('owner')
        self.relative_path = map.get('relative_path')
        self.status = map.get('status')
        self.store_id = map.get('store_id')
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
        self.headers = headers  # type: dict
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
        self.drive_id = drive_id  # type: str
        # encrypt_mode
        self.encrypt_mode = encrypt_mode  # type: str
        # file_id
        self.file_id = file_id  # type: str
        # hidden
        self.hidden = hidden  # type: bool
        self.image_media_metadata = image_media_metadata  # type: ImageMediaMetadata
        # labels
        self.labels = labels  # type: list
        # last_updated_at
        self.last_updated_at = last_updated_at  # type: str
        self.meta = meta  # type: str
        # Name
        self.name = name  # type: str
        # parent_file_id
        self.parent_file_id = parent_file_id  # type: str
        # part_info_list
        self.part_info_list = part_info_list  # type: list
        # pre_hash
        self.pre_hash = pre_hash  # type: str
        # Size
        self.size = size  # type: int
        # streams_info
        self.streams_info = streams_info  # type: dict
        # Type
        self.type = type  # type: str
        # user_meta
        self.user_meta = user_meta  # type: str
        self.video_media_metadata = video_media_metadata  # type: VideoMediaMetadata

    def validate(self):
        if self.description:
            self.validate_max_length(self.description, 'description', 1024)
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.image_media_metadata:
            self.image_media_metadata.validate()
        self.validate_required(self.name, 'name')
        if self.name:
            self.validate_max_length(self.name, 'name', 1024)
        self.validate_required(self.parent_file_id, 'parent_file_id')
        if self.parent_file_id:
            self.validate_max_length(self.parent_file_id, 'parent_file_id', 50)
            self.validate_pattern(self.parent_file_id, 'parent_file_id', '[a-z0-9]{1,50}')
        if self.part_info_list:
            for k in self.part_info_list:
                if k:
                    k.validate()
        self.validate_required(self.type, 'type')
        if self.video_media_metadata:
            self.video_media_metadata.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['addition_data'] = self.addition_data
        result['auto_rename'] = self.auto_rename
        result['check_name_mode'] = self.check_name_mode
        result['content_hash'] = self.content_hash
        result['content_hash_name'] = self.content_hash_name
        result['content_md5'] = self.content_md_5
        result['content_type'] = self.content_type
        result['description'] = self.description
        result['drive_id'] = self.drive_id
        result['encrypt_mode'] = self.encrypt_mode
        result['file_id'] = self.file_id
        result['hidden'] = self.hidden
        if self.image_media_metadata is not None:
            result['image_media_metadata'] = self.image_media_metadata.to_map()
        else:
            result['image_media_metadata'] = None
        result['labels'] = self.labels
        result['last_updated_at'] = self.last_updated_at
        result['meta'] = self.meta
        result['name'] = self.name
        result['parent_file_id'] = self.parent_file_id
        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k in self.part_info_list:
                result['part_info_list'].append(k.to_map() if k else None)
        else:
            result['part_info_list'] = None
        result['pre_hash'] = self.pre_hash
        result['size'] = self.size
        result['streams_info'] = self.streams_info
        result['type'] = self.type
        result['user_meta'] = self.user_meta
        if self.video_media_metadata is not None:
            result['video_media_metadata'] = self.video_media_metadata.to_map()
        else:
            result['video_media_metadata'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.addition_data = map.get('addition_data')
        self.auto_rename = map.get('auto_rename')
        self.check_name_mode = map.get('check_name_mode')
        self.content_hash = map.get('content_hash')
        self.content_hash_name = map.get('content_hash_name')
        self.content_md_5 = map.get('content_md5')
        self.content_type = map.get('content_type')
        self.description = map.get('description')
        self.drive_id = map.get('drive_id')
        self.encrypt_mode = map.get('encrypt_mode')
        self.file_id = map.get('file_id')
        self.hidden = map.get('hidden')
        if map.get('image_media_metadata') is not None:
            temp_model = ImageMediaMetadata()
            self.image_media_metadata = temp_model.from_map(map['image_media_metadata'])
        else:
            self.image_media_metadata = None
        self.labels = map.get('labels')
        self.last_updated_at = map.get('last_updated_at')
        self.meta = map.get('meta')
        self.name = map.get('name')
        self.parent_file_id = map.get('parent_file_id')
        self.part_info_list = []
        if map.get('part_info_list') is not None:
            for k in map.get('part_info_list'):
                temp_model = UploadPartInfo()
                self.part_info_list.append(temp_model.from_map(k))
        else:
            self.part_info_list = None
        self.pre_hash = map.get('pre_hash')
        self.size = map.get('size')
        self.streams_info = map.get('streams_info')
        self.type = map.get('type')
        self.user_meta = map.get('user_meta')
        if map.get('video_media_metadata') is not None:
            temp_model = VideoMediaMetadata()
            self.video_media_metadata = temp_model.from_map(map['video_media_metadata'])
        else:
            self.video_media_metadata = None
        return self


class CreateShareLinkRequest(TeaModel):
    """
    create_share_link request
    """
    def __init__(self, headers=None, drive_id=None, expiration=None, file_id=None, share_pwd=None):
        self.headers = headers  # type: dict
        # drive_id
        self.drive_id = drive_id  # type: str
        # expiration
        self.expiration = expiration  # type: str
        # file_id
        self.file_id = file_id  # type: str
        # share_pwd
        self.share_pwd = share_pwd  # type: str

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.expiration, 'expiration')
        self.validate_required(self.file_id, 'file_id')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['drive_id'] = self.drive_id
        result['expiration'] = self.expiration
        result['file_id'] = self.file_id
        result['share_pwd'] = self.share_pwd
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.drive_id = map.get('drive_id')
        self.expiration = map.get('expiration')
        self.file_id = map.get('file_id')
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
        self.drive_id = drive_id  # type: str
        # expiration
        self.expiration = expiration  # type: str
        # creator
        self.owner = owner  # type: str
        # permissions
        self.permissions = permissions  # type: list
        # share_file_path
        self.share_file_path = share_file_path  # type: str
        # share_name
        self.share_name = share_name  # type: str
        # share create policy
        # 
        # share_policy
        self.share_policy = share_policy  # type: list
        # status
        self.status = status  # type: str

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.owner, 'owner')
        self.validate_required(self.share_file_path, 'share_file_path')
        if self.share_policy:
            for k in self.share_policy:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['description'] = self.description
        result['drive_id'] = self.drive_id
        result['expiration'] = self.expiration
        result['owner'] = self.owner
        result['permissions'] = self.permissions
        result['share_file_path'] = self.share_file_path
        result['share_name'] = self.share_name
        result['share_policy'] = []
        if self.share_policy is not None:
            for k in self.share_policy:
                result['share_policy'].append(k.to_map() if k else None)
        else:
            result['share_policy'] = None
        result['status'] = self.status
        return result

    def from_map(self, map={}):
        self.description = map.get('description')
        self.drive_id = map.get('drive_id')
        self.expiration = map.get('expiration')
        self.owner = map.get('owner')
        self.permissions = map.get('permissions')
        self.share_file_path = map.get('share_file_path')
        self.share_name = map.get('share_name')
        self.share_policy = []
        if map.get('share_policy') is not None:
            for k in map.get('share_policy'):
                temp_model = SharePermissionPolicy()
                self.share_policy.append(temp_model.from_map(k))
        else:
            self.share_policy = None
        self.status = map.get('status')
        return self


class DeleteDriveRequest(TeaModel):
    """
    Delete drive request
    """
    def __init__(self, headers=None, drive_id=None):
        self.headers = headers  # type: dict
        # Drive ID
        self.drive_id = drive_id  # type: str

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['drive_id'] = self.drive_id
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.drive_id = map.get('drive_id')
        return self


class DeleteFileRequest(TeaModel):
    """
    删除文件请求
    """
    def __init__(self, headers=None, drive_id=None, file_id=None, permanently=None):
        self.headers = headers  # type: dict
        # drive_id
        self.drive_id = drive_id  # type: str
        # file_id
        self.file_id = file_id  # type: str
        # permanently
        # type: false
        self.permanently = permanently  # type: bool

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_id, 'file_id')
        if self.file_id:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9.-_]{1,50}')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['drive_id'] = self.drive_id
        result['file_id'] = self.file_id
        result['permanently'] = self.permanently
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.drive_id = map.get('drive_id')
        self.file_id = map.get('file_id')
        self.permanently = map.get('permanently')
        return self


class DeleteFilesRequest(TeaModel):
    """
    批量删除文件请求
    """
    def __init__(self, drive_id=None, file_id_list=None):
        # drive_id
        self.drive_id = drive_id  # type: str
        # file_id_list
        self.file_id_list = file_id_list  # type: list

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_id_list, 'file_id_list')

    def to_map(self):
        result = {}
        result['drive_id'] = self.drive_id
        result['file_id_list'] = self.file_id_list
        return result

    def from_map(self, map={}):
        self.drive_id = map.get('drive_id')
        self.file_id_list = map.get('file_id_list')
        return self


class DeleteShareRequest(TeaModel):
    """
    delete share request
    """
    def __init__(self, share_id=None):
        # share_id
        self.share_id = share_id  # type: str

    def validate(self):
        self.validate_required(self.share_id, 'share_id')

    def to_map(self):
        result = {}
        result['share_id'] = self.share_id
        return result

    def from_map(self, map={}):
        self.share_id = map.get('share_id')
        return self


class DownloadRequest(TeaModel):
    """
    下载文件请求body
    """
    def __init__(self, drive_id=None, file_id=None, image_thumbnail_process=None, share_id=None,
                 video_thumbnail_process=None):
        # drive id
        self.drive_id = drive_id  # type: str
        # file id
        self.file_id = file_id  # type: str
        # in: query
        # image_thumbnail_process
        self.image_thumbnail_process = image_thumbnail_process  # type: str
        # share_id, either share_id or drive_id is required
        self.share_id = share_id  # type: str
        # video_thumbnail_process
        # type:string
        self.video_thumbnail_process = video_thumbnail_process  # type: str

    def validate(self):
        self.validate_required(self.file_id, 'file_id')

    def to_map(self):
        result = {}
        result['DriveID'] = self.drive_id
        result['FileID'] = self.file_id
        result['ImageThumbnailProcess'] = self.image_thumbnail_process
        result['ShareID'] = self.share_id
        result['VideoThumbnailProcess'] = self.video_thumbnail_process
        return result

    def from_map(self, map={}):
        self.drive_id = map.get('DriveID')
        self.file_id = map.get('FileID')
        self.image_thumbnail_process = map.get('ImageThumbnailProcess')
        self.share_id = map.get('ShareID')
        self.video_thumbnail_process = map.get('VideoThumbnailProcess')
        return self


class GetAsyncTaskRequest(TeaModel):
    """
    获取异步人去信息
    """
    def __init__(self, headers=None, async_task_id=None):
        self.headers = headers  # type: dict
        # async_task_id
        # type:string
        self.async_task_id = async_task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['async_task_id'] = self.async_task_id
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.async_task_id = map.get('async_task_id')
        return self


class GetDefaultDriveRequest(TeaModel):
    """
    Get default drive request
    """
    def __init__(self, headers=None, user_id=None):
        self.headers = headers  # type: dict
        # 用户ID
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['user_id'] = self.user_id
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.user_id = map.get('user_id')
        return self


class GetDownloadUrlRequest(TeaModel):
    """
    获取文件下载地址的请求body
    """
    def __init__(self, headers=None, addition_data=None, drive_id=None, expire_sec=None, file_id=None,
                 file_name=None):
        self.headers = headers  # type: dict
        # addition_data
        self.addition_data = addition_data  # type: dict
        # drive_id
        self.drive_id = drive_id  # type: str
        # expire_sec
        self.expire_sec = expire_sec  # type: int
        # file_id
        self.file_id = file_id  # type: str
        # file_name
        self.file_name = file_name  # type: str

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_id, 'file_id')
        if self.file_id:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9.-_]{1,50}')
        if self.file_name:
            self.validate_max_length(self.file_name, 'file_name', 1024)

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['addition_data'] = self.addition_data
        result['drive_id'] = self.drive_id
        result['expire_sec'] = self.expire_sec
        result['file_id'] = self.file_id
        result['file_name'] = self.file_name
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.addition_data = map.get('addition_data')
        self.drive_id = map.get('drive_id')
        self.expire_sec = map.get('expire_sec')
        self.file_id = map.get('file_id')
        self.file_name = map.get('file_name')
        return self


class GetDriveRequest(TeaModel):
    """
    Get drive request
    """
    def __init__(self, headers=None, drive_id=None):
        self.headers = headers  # type: dict
        # Drive ID
        self.drive_id = drive_id  # type: str

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['drive_id'] = self.drive_id
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.drive_id = map.get('drive_id')
        return self


class GetFileByPathRequest(TeaModel):
    """
    根据路径获取 File 接口 body
    """
    def __init__(self, headers=None, drive_id=None, fields=None, file_id=None, file_path=None,
                 image_thumbnail_process=None, image_url_process=None, url_expire_sec=None, video_thumbnail_process=None):
        self.headers = headers  # type: dict
        # drive_id
        self.drive_id = drive_id  # type: str
        # fields
        self.fields = fields  # type: str
        # file_id
        self.file_id = file_id  # type: str
        # file_path
        self.file_path = file_path  # type: str
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
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_id, 'file_id')
        if self.file_id:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9.-_]{1,50}')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['drive_id'] = self.drive_id
        result['fields'] = self.fields
        result['file_id'] = self.file_id
        result['file_path'] = self.file_path
        result['image_thumbnail_process'] = self.image_thumbnail_process
        result['image_url_process'] = self.image_url_process
        result['url_expire_sec'] = self.url_expire_sec
        result['video_thumbnail_process'] = self.video_thumbnail_process
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.drive_id = map.get('drive_id')
        self.fields = map.get('fields')
        self.file_id = map.get('file_id')
        self.file_path = map.get('file_path')
        self.image_thumbnail_process = map.get('image_thumbnail_process')
        self.image_url_process = map.get('image_url_process')
        self.url_expire_sec = map.get('url_expire_sec')
        self.video_thumbnail_process = map.get('video_thumbnail_process')
        return self


class GetFileRequest(TeaModel):
    """
    获取文件元数据
    """
    def __init__(self, headers=None, drive_id=None, fields=None, file_id=None, image_thumbnail_process=None,
                 image_url_process=None, url_expire_sec=None, video_thumbnail_process=None):
        self.headers = headers  # type: dict
        # drive_id
        self.drive_id = drive_id  # type: str
        # fields
        self.fields = fields  # type: str
        # file_id
        self.file_id = file_id  # type: str
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
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_id, 'file_id')
        if self.file_id:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9.-_]{1,50}')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['drive_id'] = self.drive_id
        result['fields'] = self.fields
        result['file_id'] = self.file_id
        result['image_thumbnail_process'] = self.image_thumbnail_process
        result['image_url_process'] = self.image_url_process
        result['url_expire_sec'] = self.url_expire_sec
        result['video_thumbnail_process'] = self.video_thumbnail_process
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.drive_id = map.get('drive_id')
        self.fields = map.get('fields')
        self.file_id = map.get('file_id')
        self.image_thumbnail_process = map.get('image_thumbnail_process')
        self.image_url_process = map.get('image_url_process')
        self.url_expire_sec = map.get('url_expire_sec')
        self.video_thumbnail_process = map.get('video_thumbnail_process')
        return self


class GetLastCursorRequest(TeaModel):
    """
    获取最新游标
    """
    def __init__(self, headers=None, drive_id=None):
        self.headers = headers  # type: dict
        # drive_id
        self.drive_id = drive_id  # type: str

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['drive_id'] = self.drive_id
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.drive_id = map.get('drive_id')
        return self


class GetMediaPlayURLRequest(TeaModel):
    """
    get_media_play_url request
    """
    def __init__(self, headers=None, drive_id=None, file_id=None):
        self.headers = headers  # type: dict
        # drive_id
        self.drive_id = drive_id  # type: str
        # file_id
        self.file_id = file_id  # type: str

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_id, 'file_id')
        if self.file_id:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9.-_]{1,50}')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['drive_id'] = self.drive_id
        result['file_id'] = self.file_id
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.drive_id = map.get('drive_id')
        self.file_id = map.get('file_id')
        return self


class GetOfficePreviewUrlRequest(TeaModel):
    """
    获取office文档预览地址
    """
    def __init__(self, headers=None, addition_data=None, drive_id=None, file_id=None):
        self.headers = headers  # type: dict
        # addition_data
        self.addition_data = addition_data  # type: dict
        # drive_id
        self.drive_id = drive_id  # type: str
        # file_id
        self.file_id = file_id  # type: str

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_id, 'file_id')
        if self.file_id:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9.-_]{1,50}')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['addition_data'] = self.addition_data
        result['drive_id'] = self.drive_id
        result['file_id'] = self.file_id
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.addition_data = map.get('addition_data')
        self.drive_id = map.get('drive_id')
        self.file_id = map.get('file_id')
        return self


class GetShareLinkByAnonymousRequest(TeaModel):
    """
    get_share_link_by_anonymous request
    """
    def __init__(self, share_id=None):
        # share_id
        self.share_id = share_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['share_id'] = self.share_id
        return result

    def from_map(self, map={}):
        self.share_id = map.get('share_id')
        return self


class GetShareLinkIDRequest(TeaModel):
    """
    get_share_id request
    """
    def __init__(self, headers=None, share_msg=None):
        self.headers = headers  # type: dict
        # share_msg
        self.share_msg = share_msg  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['share_msg'] = self.share_msg
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.share_msg = map.get('share_msg')
        return self


class GetShareLinkTokenRequest(TeaModel):
    """
    get_share_token request
    """
    def __init__(self, headers=None, share_id=None, share_pwd=None):
        self.headers = headers  # type: dict
        # share_id
        self.share_id = share_id  # type: str
        # share_pwd
        self.share_pwd = share_pwd  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['share_id'] = self.share_id
        result['share_pwd'] = self.share_pwd
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.share_id = map.get('share_id')
        self.share_pwd = map.get('share_pwd')
        return self


class GetShareRequest(TeaModel):
    """
    get share request
    """
    def __init__(self, share_id=None):
        # share_id
        self.share_id = share_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['share_id'] = self.share_id
        return result

    def from_map(self, map={}):
        self.share_id = map.get('share_id')
        return self


class GetUploadUrlRequest(TeaModel):
    """
    获取文件上传URL
    """
    def __init__(self, headers=None, content_md_5=None, drive_id=None, file_id=None, part_info_list=None,
                 upload_id=None):
        self.headers = headers  # type: dict
        # content_md5
        self.content_md_5 = content_md_5  # type: str
        # drive_id
        self.drive_id = drive_id  # type: str
        # file_id
        self.file_id = file_id  # type: str
        # upload_part_list
        self.part_info_list = part_info_list  # type: list
        # upload_id
        self.upload_id = upload_id  # type: str

    def validate(self):
        if self.content_md_5:
            self.validate_max_length(self.content_md_5, 'content_md_5', 32)
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_id, 'file_id')
        if self.file_id:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9]{1,50}')
        if self.part_info_list:
            for k in self.part_info_list:
                if k:
                    k.validate()
        self.validate_required(self.upload_id, 'upload_id')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['content_md5'] = self.content_md_5
        result['drive_id'] = self.drive_id
        result['file_id'] = self.file_id
        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k in self.part_info_list:
                result['part_info_list'].append(k.to_map() if k else None)
        else:
            result['part_info_list'] = None
        result['upload_id'] = self.upload_id
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.content_md_5 = map.get('content_md5')
        self.drive_id = map.get('drive_id')
        self.file_id = map.get('file_id')
        self.part_info_list = []
        if map.get('part_info_list') is not None:
            for k in map.get('part_info_list'):
                temp_model = UploadPartInfo()
                self.part_info_list.append(temp_model.from_map(k))
        else:
            self.part_info_list = None
        self.upload_id = map.get('upload_id')
        return self


class GetVideoPreviewSpriteURLRequest(TeaModel):
    """
    获取视频雪碧图地址的请求body
    """
    def __init__(self, headers=None, drive_id=None, expire_sec=None, file_id=None):
        self.headers = headers  # type: dict
        # drive_id
        self.drive_id = drive_id  # type: str
        # expire_sec
        self.expire_sec = expire_sec  # type: int
        # file_id
        self.file_id = file_id  # type: str

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_id, 'file_id')
        if self.file_id:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9.-_]{1,50}')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['drive_id'] = self.drive_id
        result['expire_sec'] = self.expire_sec
        result['file_id'] = self.file_id
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.drive_id = map.get('drive_id')
        self.expire_sec = map.get('expire_sec')
        self.file_id = map.get('file_id')
        return self


class GetVideoPreviewURLRequest(TeaModel):
    """
    获取视频文件播放地址的请求body
    """
    def __init__(self, headers=None, addition_data=None, drive_id=None, expire_sec=None, file_id=None,
                 template_id=None):
        self.headers = headers  # type: dict
        # addition_data
        self.addition_data = addition_data  # type: dict
        # drive_id
        self.drive_id = drive_id  # type: str
        # expire_sec
        self.expire_sec = expire_sec  # type: int
        # file_id
        self.file_id = file_id  # type: str
        # template_id
        self.template_id = template_id  # type: str

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_id, 'file_id')
        if self.file_id:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9.-_]{1,50}')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['addition_data'] = self.addition_data
        result['drive_id'] = self.drive_id
        result['expire_sec'] = self.expire_sec
        result['file_id'] = self.file_id
        result['template_id'] = self.template_id
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.addition_data = map.get('addition_data')
        self.drive_id = map.get('drive_id')
        self.expire_sec = map.get('expire_sec')
        self.file_id = map.get('file_id')
        self.template_id = map.get('template_id')
        return self


class ImageMediaMetadata(TeaModel):
    """
    *
    """
    def __init__(self, height=None, width=None):
        # height
        self.height = height  # type: int
        # width：
        self.width = width  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['height'] = self.height
        result['width'] = self.width
        return result

    def from_map(self, map={}):
        self.height = map.get('height')
        self.width = map.get('width')
        return self


class ListByAnonymousRequest(TeaModel):
    """
    list_file_by_anonymous request
    """
    def __init__(self, headers=None, limit=None, marker=None, parent_file_id=None, share_id=None):
        self.headers = headers  # type: dict
        # limit
        self.limit = limit  # type: int
        # marker
        self.marker = marker  # type: str
        # parent_file_id
        self.parent_file_id = parent_file_id  # type: str
        # share_id
        self.share_id = share_id  # type: str

    def validate(self):
        self.validate_required(self.parent_file_id, 'parent_file_id')
        if self.parent_file_id:
            self.validate_max_length(self.parent_file_id, 'parent_file_id', 50)
            self.validate_pattern(self.parent_file_id, 'parent_file_id', '[a-z0-9]{1,50}')
        self.validate_required(self.share_id, 'share_id')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['limit'] = self.limit
        result['marker'] = self.marker
        result['parent_file_id'] = self.parent_file_id
        result['share_id'] = self.share_id
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.limit = map.get('limit')
        self.marker = map.get('marker')
        self.parent_file_id = map.get('parent_file_id')
        self.share_id = map.get('share_id')
        return self


class ListDriveRequest(TeaModel):
    """
    List drive request
    """
    def __init__(self, headers=None, limit=None, marker=None, owner=None):
        self.headers = headers  # type: dict
        # 每页大小限制
        self.limit = limit  # type: int
        # 翻页标记, 接口返回的标记值
        self.marker = marker  # type: str
        # 所属者
        self.owner = owner  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['limit'] = self.limit
        result['marker'] = self.marker
        result['owner'] = self.owner
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.limit = map.get('limit')
        self.marker = map.get('marker')
        self.owner = map.get('owner')
        return self


class ListFileByCustomIndexKeyRequest(TeaModel):
    """
    列举文件
    """
    def __init__(self, headers=None, starred=None, category=None, custom_index_key=None, drive_id=None,
                 encrypt_mode=None, fields=None, image_thumbnail_process=None, image_url_process=None, limit=None, marker=None,
                 order_direction=None, status=None, type=None, url_expire_sec=None, video_thumbnail_process=None):
        self.headers = headers  # type: dict
        # starred
        self.starred = starred  # type: bool
        # category
        self.category = category  # type: str
        # custom_index_key
        self.custom_index_key = custom_index_key  # type: str
        # drive_id
        self.drive_id = drive_id  # type: str
        # encrypt_mode
        self.encrypt_mode = encrypt_mode  # type: str
        # fields
        self.fields = fields  # type: str
        # image_thumbnail_process
        self.image_thumbnail_process = image_thumbnail_process  # type: str
        # image_url_process
        self.image_url_process = image_url_process  # type: str
        # limit
        self.limit = limit  # type: int
        # marker
        self.marker = marker  # type: str
        # order_direction
        self.order_direction = order_direction  # type: str
        # status
        self.status = status  # type: str
        # type
        self.type = type  # type: str
        # url_expire_sec
        self.url_expire_sec = url_expire_sec  # type: int
        # video_thumbnail_process
        # type:string
        self.video_thumbnail_process = video_thumbnail_process  # type: str

    def validate(self):
        self.validate_required(self.custom_index_key, 'custom_index_key')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.limit:
            self.validate_pattern(self.limit, 'limit', '[0-9]{1,3}')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['Starred'] = self.starred
        result['category'] = self.category
        result['custom_index_key'] = self.custom_index_key
        result['drive_id'] = self.drive_id
        result['encrypt_mode'] = self.encrypt_mode
        result['fields'] = self.fields
        result['image_thumbnail_process'] = self.image_thumbnail_process
        result['image_url_process'] = self.image_url_process
        result['limit'] = self.limit
        result['marker'] = self.marker
        result['order_direction'] = self.order_direction
        result['status'] = self.status
        result['type'] = self.type
        result['url_expire_sec'] = self.url_expire_sec
        result['video_thumbnail_process'] = self.video_thumbnail_process
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.starred = map.get('Starred')
        self.category = map.get('category')
        self.custom_index_key = map.get('custom_index_key')
        self.drive_id = map.get('drive_id')
        self.encrypt_mode = map.get('encrypt_mode')
        self.fields = map.get('fields')
        self.image_thumbnail_process = map.get('image_thumbnail_process')
        self.image_url_process = map.get('image_url_process')
        self.limit = map.get('limit')
        self.marker = map.get('marker')
        self.order_direction = map.get('order_direction')
        self.status = map.get('status')
        self.type = map.get('type')
        self.url_expire_sec = map.get('url_expire_sec')
        self.video_thumbnail_process = map.get('video_thumbnail_process')
        return self


class ListFileDeltaRequest(TeaModel):
    """
    获取增量文件操作记录
    """
    def __init__(self, headers=None, cursor=None, drive_id=None, limit=None):
        self.headers = headers  # type: dict
        # cursor 游标
        self.cursor = cursor  # type: str
        # drive_id
        self.drive_id = drive_id  # type: str
        # limit
        # default 100
        self.limit = limit  # type: int

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['cursor'] = self.cursor
        result['drive_id'] = self.drive_id
        result['limit'] = self.limit
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.cursor = map.get('cursor')
        self.drive_id = map.get('drive_id')
        self.limit = map.get('limit')
        return self


class ListFileRequest(TeaModel):
    """
    列举文件
    """
    def __init__(self, headers=None, starred=None, all=None, category=None, drive_id=None, fields=None,
                 image_thumbnail_process=None, image_url_process=None, limit=None, marker=None, order_by=None, order_direction=None,
                 parent_file_id=None, status=None, type=None, url_expire_sec=None, video_thumbnail_process=None):
        self.headers = headers  # type: dict
        # starred
        self.starred = starred  # type: bool
        # all
        self.all = all  # type: bool
        # category
        self.category = category  # type: str
        # drive_id
        self.drive_id = drive_id  # type: str
        # fields
        self.fields = fields  # type: str
        # image_thumbnail_process
        self.image_thumbnail_process = image_thumbnail_process  # type: str
        # image_url_process
        self.image_url_process = image_url_process  # type: str
        # limit
        self.limit = limit  # type: int
        # marker
        self.marker = marker  # type: str
        # order_by
        self.order_by = order_by  # type: str
        # order_direction
        self.order_direction = order_direction  # type: str
        # ParentFileID
        self.parent_file_id = parent_file_id  # type: str
        # status
        self.status = status  # type: str
        # type
        self.type = type  # type: str
        # url_expire_sec
        self.url_expire_sec = url_expire_sec  # type: int
        # video_thumbnail_process
        # type:string
        self.video_thumbnail_process = video_thumbnail_process  # type: str

    def validate(self):
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.limit:
            self.validate_pattern(self.limit, 'limit', '[0-9]{1,3}')
        self.validate_required(self.parent_file_id, 'parent_file_id')
        if self.parent_file_id:
            self.validate_max_length(self.parent_file_id, 'parent_file_id', 50)
            self.validate_pattern(self.parent_file_id, 'parent_file_id', '[a-z0-9.-_]{1,50}')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['Starred'] = self.starred
        result['all'] = self.all
        result['category'] = self.category
        result['drive_id'] = self.drive_id
        result['fields'] = self.fields
        result['image_thumbnail_process'] = self.image_thumbnail_process
        result['image_url_process'] = self.image_url_process
        result['limit'] = self.limit
        result['marker'] = self.marker
        result['order_by'] = self.order_by
        result['order_direction'] = self.order_direction
        result['parent_file_id'] = self.parent_file_id
        result['status'] = self.status
        result['type'] = self.type
        result['url_expire_sec'] = self.url_expire_sec
        result['video_thumbnail_process'] = self.video_thumbnail_process
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.starred = map.get('Starred')
        self.all = map.get('all')
        self.category = map.get('category')
        self.drive_id = map.get('drive_id')
        self.fields = map.get('fields')
        self.image_thumbnail_process = map.get('image_thumbnail_process')
        self.image_url_process = map.get('image_url_process')
        self.limit = map.get('limit')
        self.marker = map.get('marker')
        self.order_by = map.get('order_by')
        self.order_direction = map.get('order_direction')
        self.parent_file_id = map.get('parent_file_id')
        self.status = map.get('status')
        self.type = map.get('type')
        self.url_expire_sec = map.get('url_expire_sec')
        self.video_thumbnail_process = map.get('video_thumbnail_process')
        return self


class ListMyDriveRequest(TeaModel):
    """
    List my drive request
    """
    def __init__(self, headers=None, limit=None, marker=None):
        self.headers = headers  # type: dict
        # 每页大小限制
        self.limit = limit  # type: int
        # 翻页标记, 接口返回的标记值
        self.marker = marker  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['limit'] = self.limit
        result['marker'] = self.marker
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.limit = map.get('limit')
        self.marker = map.get('marker')
        return self


class ListShareLinkRequest(TeaModel):
    """
    list_share_link request
    """
    def __init__(self, headers=None, creator=None, limit=None, marker=None):
        self.headers = headers  # type: dict
        # creator
        self.creator = creator  # type: str
        # limit
        self.limit = limit  # type: int
        # marker
        self.marker = marker  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['creator'] = self.creator
        result['limit'] = self.limit
        result['marker'] = self.marker
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.creator = map.get('creator')
        self.limit = map.get('limit')
        self.marker = map.get('marker')
        return self


class ListShareRequest(TeaModel):
    """
    list share request
    """
    def __init__(self, creator=None, drive_id=None, limit=None, marker=None, owner=None, share_file_path=None):
        # creator
        self.creator = creator  # type: str
        self.drive_id = drive_id  # type: str
        # limit
        self.limit = limit  # type: int
        # marker
        self.marker = marker  # type: str
        # Owner
        self.owner = owner  # type: str
        # share_file_path
        self.share_file_path = share_file_path  # type: str

    def validate(self):
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')

    def to_map(self):
        result = {}
        result['creator'] = self.creator
        result['drive_id'] = self.drive_id
        result['limit'] = self.limit
        result['marker'] = self.marker
        result['owner'] = self.owner
        result['share_file_path'] = self.share_file_path
        return result

    def from_map(self, map={}):
        self.creator = map.get('creator')
        self.drive_id = map.get('drive_id')
        self.limit = map.get('limit')
        self.marker = map.get('marker')
        self.owner = map.get('owner')
        self.share_file_path = map.get('share_file_path')
        return self


class ListStoreFileRequest(TeaModel):
    """
    list store file
    """
    def __init__(self, limit=None, marker=None, parent_file_path=None, store_id=None, type=None):
        # limit
        self.limit = limit  # type: int
        # marker
        self.marker = marker  # type: str
        # parent_file_path
        self.parent_file_path = parent_file_path  # type: str
        # store_id
        self.store_id = store_id  # type: str
        # type
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['limit'] = self.limit
        result['marker'] = self.marker
        result['parent_file_path'] = self.parent_file_path
        result['store_id'] = self.store_id
        result['type'] = self.type
        return result

    def from_map(self, map={}):
        self.limit = map.get('limit')
        self.marker = map.get('marker')
        self.parent_file_path = map.get('parent_file_path')
        self.store_id = map.get('store_id')
        self.type = map.get('type')
        return self


class ListStoreRequest(TeaModel):
    """
    list storage file
    """
    def __init__(self, domain_id=None):
        # domain_id
        self.domain_id = domain_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['domain_id'] = self.domain_id
        return result

    def from_map(self, map={}):
        self.domain_id = map.get('domain_id')
        return self


class ListUploadedPartRequest(TeaModel):
    """
    列举uploadID对应的已上传分片
    """
    def __init__(self, headers=None, drive_id=None, file_id=None, limit=None, part_number_marker=None,
                 upload_id=None):
        self.headers = headers  # type: dict
        # drive_id
        self.drive_id = drive_id  # type: str
        # file_id
        self.file_id = file_id  # type: str
        # limit
        self.limit = limit  # type: int
        # part_number_marker
        self.part_number_marker = part_number_marker  # type: int
        # upload_id
        self.upload_id = upload_id  # type: str

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_id, 'file_id')
        if self.file_id:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9.-_]{1,50}')
        if self.limit:
            self.validate_pattern(self.limit, 'limit', '[0-9]+')
        if self.part_number_marker:
            self.validate_pattern(self.part_number_marker, 'part_number_marker', '[0-9]+')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['drive_id'] = self.drive_id
        result['file_id'] = self.file_id
        result['limit'] = self.limit
        result['part_number_marker'] = self.part_number_marker
        result['upload_id'] = self.upload_id
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.drive_id = map.get('drive_id')
        self.file_id = map.get('file_id')
        self.limit = map.get('limit')
        self.part_number_marker = map.get('part_number_marker')
        self.upload_id = map.get('upload_id')
        return self


class MoveFileRequest(TeaModel):
    """
    文件移动请求
    """
    def __init__(self, headers=None, drive_id=None, file_id=None, new_name=None, overwrite=None,
                 to_parent_file_id=None):
        self.headers = headers  # type: dict
        # drive_id
        self.drive_id = drive_id  # type: str
        # file_id
        self.file_id = file_id  # type: str
        # new_name
        self.new_name = new_name  # type: str
        # overwrite
        # type: boolean
        self.overwrite = overwrite  # type: bool
        # to_parent_file_id
        self.to_parent_file_id = to_parent_file_id  # type: str

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_id, 'file_id')
        if self.file_id:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9.-_]{1,50}')
        if self.new_name:
            self.validate_max_length(self.new_name, 'new_name', 1024)
        self.validate_required(self.to_parent_file_id, 'to_parent_file_id')
        if self.to_parent_file_id:
            self.validate_max_length(self.to_parent_file_id, 'to_parent_file_id', 50)

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['drive_id'] = self.drive_id
        result['file_id'] = self.file_id
        result['new_name'] = self.new_name
        result['overwrite'] = self.overwrite
        result['to_parent_file_id'] = self.to_parent_file_id
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.drive_id = map.get('drive_id')
        self.file_id = map.get('file_id')
        self.new_name = map.get('new_name')
        self.overwrite = map.get('overwrite')
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
        self.drive_id = drive_id  # type: str
        self.file_path = file_path  # type: str
        # forbid_overwrite
        # type: boolean
        self.forbid_overwrite = forbid_overwrite  # type: bool
        # part_info_list
        self.part_info_list = part_info_list  # type: list
        self.share_id = share_id  # type: str
        # upload_id
        self.upload_id = upload_id  # type: str

    def validate(self):
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.part_info_list:
            for k in self.part_info_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['addition_data'] = self.addition_data
        result['drive_id'] = self.drive_id
        result['file_path'] = self.file_path
        result['forbid_overwrite'] = self.forbid_overwrite
        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k in self.part_info_list:
                result['part_info_list'].append(k.to_map() if k else None)
        else:
            result['part_info_list'] = None
        result['share_id'] = self.share_id
        result['upload_id'] = self.upload_id
        return result

    def from_map(self, map={}):
        self.addition_data = map.get('addition_data')
        self.drive_id = map.get('drive_id')
        self.file_path = map.get('file_path')
        self.forbid_overwrite = map.get('forbid_overwrite')
        self.part_info_list = []
        if map.get('part_info_list') is not None:
            for k in map.get('part_info_list'):
                temp_model = UploadPartInfo()
                self.part_info_list.append(temp_model.from_map(k))
        else:
            self.part_info_list = None
        self.share_id = map.get('share_id')
        self.upload_id = map.get('upload_id')
        return self


class OSSCopyFileRequest(TeaModel):
    """
    copy file request
    """
    def __init__(self, drive_id=None, file_path=None, new_name=None, overwrite=None, share_id=None, to_drive_id=None,
                 to_parent_file_path=None, to_share_id=None):
        # drive_id
        self.drive_id = drive_id  # type: str
        # file_path
        self.file_path = file_path  # type: str
        # new_name
        self.new_name = new_name  # type: str
        # overwrite
        # type: boolean
        self.overwrite = overwrite  # type: bool
        # share_id
        self.share_id = share_id  # type: str
        # to_drive_id
        self.to_drive_id = to_drive_id  # type: str
        # to_parent_file_path
        self.to_parent_file_path = to_parent_file_path  # type: str
        # share_id
        self.to_share_id = to_share_id  # type: str

    def validate(self):
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_path, 'file_path')
        if self.new_name:
            self.validate_pattern(self.new_name, 'new_name', '[a-zA-Z0-9.-]{1,1000}')
        if self.share_id:
            self.validate_pattern(self.share_id, 'share_id', '[0-9a-zA-Z-]+')
        if self.to_drive_id:
            self.validate_pattern(self.to_drive_id, 'to_drive_id', '[0-9]+')
        self.validate_required(self.to_parent_file_path, 'to_parent_file_path')

    def to_map(self):
        result = {}
        result['drive_id'] = self.drive_id
        result['file_path'] = self.file_path
        result['new_name'] = self.new_name
        result['overwrite'] = self.overwrite
        result['share_id'] = self.share_id
        result['to_drive_id'] = self.to_drive_id
        result['to_parent_file_path'] = self.to_parent_file_path
        result['to_share_id'] = self.to_share_id
        return result

    def from_map(self, map={}):
        self.drive_id = map.get('drive_id')
        self.file_path = map.get('file_path')
        self.new_name = map.get('new_name')
        self.overwrite = map.get('overwrite')
        self.share_id = map.get('share_id')
        self.to_drive_id = map.get('to_drive_id')
        self.to_parent_file_path = map.get('to_parent_file_path')
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
        self.drive_id = drive_id  # type: str
        # forbid_overwrite
        # type: boolean
        self.forbid_overwrite = forbid_overwrite  # type: bool
        # Name
        self.name = name  # type: str
        # parent_file_path
        self.parent_file_path = parent_file_path  # type: str
        # part_info_list
        self.part_info_list = part_info_list  # type: list
        # share_id
        self.share_id = share_id  # type: str
        # Size
        self.size = size  # type: int
        # Type
        self.type = type  # type: str

    def validate(self):
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.name, 'name')
        if self.name:
            self.validate_max_length(self.name, 'name', 1024)
        self.validate_required(self.parent_file_path, 'parent_file_path')
        if self.part_info_list:
            for k in self.part_info_list:
                if k:
                    k.validate()
        if self.share_id:
            self.validate_pattern(self.share_id, 'share_id', '[0-9a-zA-Z-]+')
        self.validate_required(self.type, 'type')

    def to_map(self):
        result = {}
        result['addition_data'] = self.addition_data
        result['content_md5'] = self.content_md_5
        result['content_type'] = self.content_type
        result['drive_id'] = self.drive_id
        result['forbid_overwrite'] = self.forbid_overwrite
        result['name'] = self.name
        result['parent_file_path'] = self.parent_file_path
        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k in self.part_info_list:
                result['part_info_list'].append(k.to_map() if k else None)
        else:
            result['part_info_list'] = None
        result['share_id'] = self.share_id
        result['size'] = self.size
        result['type'] = self.type
        return result

    def from_map(self, map={}):
        self.addition_data = map.get('addition_data')
        self.content_md_5 = map.get('content_md5')
        self.content_type = map.get('content_type')
        self.drive_id = map.get('drive_id')
        self.forbid_overwrite = map.get('forbid_overwrite')
        self.name = map.get('name')
        self.parent_file_path = map.get('parent_file_path')
        self.part_info_list = []
        if map.get('part_info_list') is not None:
            for k in map.get('part_info_list'):
                temp_model = UploadPartInfo()
                self.part_info_list.append(temp_model.from_map(k))
        else:
            self.part_info_list = None
        self.share_id = map.get('share_id')
        self.size = map.get('size')
        self.type = map.get('type')
        return self


class OSSDeleteFileRequest(TeaModel):
    """
    删除文件请求
    """
    def __init__(self, drive_id=None, file_path=None, permanently=None, share_id=None):
        # drive_id
        self.drive_id = drive_id  # type: str
        # file_path
        self.file_path = file_path  # type: str
        # permanently
        # type: false
        self.permanently = permanently  # type: bool
        # share_id
        self.share_id = share_id  # type: str

    def validate(self):
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_path, 'file_path')
        if self.file_path:
            self.validate_max_length(self.file_path, 'file_path', 1000)
        if self.share_id:
            self.validate_pattern(self.share_id, 'share_id', '[0-9a-zA-Z-]+')

    def to_map(self):
        result = {}
        result['drive_id'] = self.drive_id
        result['file_path'] = self.file_path
        result['permanently'] = self.permanently
        result['share_id'] = self.share_id
        return result

    def from_map(self, map={}):
        self.drive_id = map.get('drive_id')
        self.file_path = map.get('file_path')
        self.permanently = map.get('permanently')
        self.share_id = map.get('share_id')
        return self


class OSSGetDownloadUrlRequest(TeaModel):
    """
    获取文件下载地址的请求body
    """
    def __init__(self, drive_id=None, expire_sec=None, file_name=None, file_path=None, share_id=None):
        # drive_id
        self.drive_id = drive_id  # type: str
        # expire_sec
        self.expire_sec = expire_sec  # type: int
        # file_name
        self.file_name = file_name  # type: str
        # file_path
        self.file_path = file_path  # type: str
        # share_id
        self.share_id = share_id  # type: str

    def validate(self):
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_path, 'file_path')
        if self.file_path:
            self.validate_max_length(self.file_path, 'file_path', 1000)
        if self.share_id:
            self.validate_pattern(self.share_id, 'share_id', '[0-9a-zA-Z-]+')

    def to_map(self):
        result = {}
        result['drive_id'] = self.drive_id
        result['expire_sec'] = self.expire_sec
        result['file_name'] = self.file_name
        result['file_path'] = self.file_path
        result['share_id'] = self.share_id
        return result

    def from_map(self, map={}):
        self.drive_id = map.get('drive_id')
        self.expire_sec = map.get('expire_sec')
        self.file_name = map.get('file_name')
        self.file_path = map.get('file_path')
        self.share_id = map.get('share_id')
        return self


class OSSGetFileRequest(TeaModel):
    """
    获取文件元数据
    """
    def __init__(self, drive_id=None, file_path=None, image_thumbnail_process=None, image_url_process=None,
                 share_id=None, url_expire_sec=None):
        # drive_id
        self.drive_id = drive_id  # type: str
        # file_id
        self.file_path = file_path  # type: str
        # image_thumbnail_process
        # type:string
        self.image_thumbnail_process = image_thumbnail_process  # type: str
        # image_thumbnail_process
        # type:string
        self.image_url_process = image_url_process  # type: str
        # share_id
        self.share_id = share_id  # type: str
        # url_expire_sec
        self.url_expire_sec = url_expire_sec  # type: int

    def validate(self):
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_path, 'file_path')
        if self.file_path:
            self.validate_max_length(self.file_path, 'file_path', 1000)
        if self.share_id:
            self.validate_pattern(self.share_id, 'share_id', '[0-9a-zA-Z-]+')

    def to_map(self):
        result = {}
        result['drive_id'] = self.drive_id
        result['file_path'] = self.file_path
        result['image_thumbnail_process'] = self.image_thumbnail_process
        result['image_url_process'] = self.image_url_process
        result['share_id'] = self.share_id
        result['url_expire_sec'] = self.url_expire_sec
        return result

    def from_map(self, map={}):
        self.drive_id = map.get('drive_id')
        self.file_path = map.get('file_path')
        self.image_thumbnail_process = map.get('image_thumbnail_process')
        self.image_url_process = map.get('image_url_process')
        self.share_id = map.get('share_id')
        self.url_expire_sec = map.get('url_expire_sec')
        return self


class OSSGetSecureUrlRequest(TeaModel):
    """
    获取文件安全地址的请求body
    """
    def __init__(self, drive_id=None, expire_sec=None, file_path=None, secure_ip=None, share_id=None):
        # drive_id
        self.drive_id = drive_id  # type: str
        # expire_sec 单位秒
        self.expire_sec = expire_sec  # type: int
        # file_path
        self.file_path = file_path  # type: str
        # secure_ip
        self.secure_ip = secure_ip  # type: str
        # share_id
        self.share_id = share_id  # type: str

    def validate(self):
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_path, 'file_path')
        if self.file_path:
            self.validate_max_length(self.file_path, 'file_path', 1000)
        if self.share_id:
            self.validate_pattern(self.share_id, 'share_id', '[0-9a-zA-Z-]+')

    def to_map(self):
        result = {}
        result['drive_id'] = self.drive_id
        result['expire_sec'] = self.expire_sec
        result['file_path'] = self.file_path
        result['secure_ip'] = self.secure_ip
        result['share_id'] = self.share_id
        return result

    def from_map(self, map={}):
        self.drive_id = map.get('drive_id')
        self.expire_sec = map.get('expire_sec')
        self.file_path = map.get('file_path')
        self.secure_ip = map.get('secure_ip')
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
        self.drive_id = drive_id  # type: str
        # file_path
        self.file_path = file_path  # type: str
        # upload_part_list
        self.part_info_list = part_info_list  # type: list
        # share_id
        self.share_id = share_id  # type: str
        # upload_id
        self.upload_id = upload_id  # type: str

    def validate(self):
        if self.content_md_5:
            self.validate_max_length(self.content_md_5, 'content_md_5', 32)
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_path, 'file_path')
        if self.part_info_list:
            for k in self.part_info_list:
                if k:
                    k.validate()
        if self.share_id:
            self.validate_pattern(self.share_id, 'share_id', '[0-9a-zA-Z-]+')
        self.validate_required(self.upload_id, 'upload_id')

    def to_map(self):
        result = {}
        result['content_md5'] = self.content_md_5
        result['drive_id'] = self.drive_id
        result['file_path'] = self.file_path
        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k in self.part_info_list:
                result['part_info_list'].append(k.to_map() if k else None)
        else:
            result['part_info_list'] = None
        result['share_id'] = self.share_id
        result['upload_id'] = self.upload_id
        return result

    def from_map(self, map={}):
        self.content_md_5 = map.get('content_md5')
        self.drive_id = map.get('drive_id')
        self.file_path = map.get('file_path')
        self.part_info_list = []
        if map.get('part_info_list') is not None:
            for k in map.get('part_info_list'):
                temp_model = UploadPartInfo()
                self.part_info_list.append(temp_model.from_map(k))
        else:
            self.part_info_list = None
        self.share_id = map.get('share_id')
        self.upload_id = map.get('upload_id')
        return self


class OSSListFileRequest(TeaModel):
    """
    list file request
    """
    def __init__(self, drive_id=None, image_thumbnail_process=None, image_url_process=None, limit=None, marker=None,
                 parent_file_path=None, share_id=None, url_expire_sec=None, video_thumbnail_process=None):
        # drive_id
        self.drive_id = drive_id  # type: str
        # image_thumbnail_process
        self.image_thumbnail_process = image_thumbnail_process  # type: str
        # image_url_process
        self.image_url_process = image_url_process  # type: str
        # limit
        self.limit = limit  # type: int
        # marker
        self.marker = marker  # type: str
        # ParentFilePath
        self.parent_file_path = parent_file_path  # type: str
        # share_id
        self.share_id = share_id  # type: str
        # url_expire_sec
        self.url_expire_sec = url_expire_sec  # type: int
        # video_thumbnail_process
        # type:string
        self.video_thumbnail_process = video_thumbnail_process  # type: str

    def validate(self):
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.limit:
            self.validate_pattern(self.limit, 'limit', '[0-9]{1,3}')
        self.validate_required(self.parent_file_path, 'parent_file_path')
        if self.share_id:
            self.validate_pattern(self.share_id, 'share_id', '[0-9a-zA-Z-]+')

    def to_map(self):
        result = {}
        result['drive_id'] = self.drive_id
        result['image_thumbnail_process'] = self.image_thumbnail_process
        result['image_url_process'] = self.image_url_process
        result['limit'] = self.limit
        result['marker'] = self.marker
        result['parent_file_path'] = self.parent_file_path
        result['share_id'] = self.share_id
        result['url_expire_sec'] = self.url_expire_sec
        result['video_thumbnail_process'] = self.video_thumbnail_process
        return result

    def from_map(self, map={}):
        self.drive_id = map.get('drive_id')
        self.image_thumbnail_process = map.get('image_thumbnail_process')
        self.image_url_process = map.get('image_url_process')
        self.limit = map.get('limit')
        self.marker = map.get('marker')
        self.parent_file_path = map.get('parent_file_path')
        self.share_id = map.get('share_id')
        self.url_expire_sec = map.get('url_expire_sec')
        self.video_thumbnail_process = map.get('video_thumbnail_process')
        return self


class OSSListUploadedPartRequest(TeaModel):
    """
    列举uploadID对应的已上传分片
    """
    def __init__(self, drive_id=None, file_path=None, limit=None, part_number_marker=None, share_id=None,
                 upload_id=None):
        # drive_id
        self.drive_id = drive_id  # type: str
        # file_path
        self.file_path = file_path  # type: str
        # limit
        self.limit = limit  # type: int
        # part_number_marker
        self.part_number_marker = part_number_marker  # type: int
        # share_id
        self.share_id = share_id  # type: str
        # upload_id
        self.upload_id = upload_id  # type: str

    def validate(self):
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_path, 'file_path')
        if self.limit:
            self.validate_pattern(self.limit, 'limit', '[0-9]+')
        if self.part_number_marker:
            self.validate_pattern(self.part_number_marker, 'part_number_marker', '[0-9]+')
        if self.share_id:
            self.validate_pattern(self.share_id, 'share_id', '[0-9a-zA-Z-]+')

    def to_map(self):
        result = {}
        result['drive_id'] = self.drive_id
        result['file_path'] = self.file_path
        result['limit'] = self.limit
        result['part_number_marker'] = self.part_number_marker
        result['share_id'] = self.share_id
        result['upload_id'] = self.upload_id
        return result

    def from_map(self, map={}):
        self.drive_id = map.get('drive_id')
        self.file_path = map.get('file_path')
        self.limit = map.get('limit')
        self.part_number_marker = map.get('part_number_marker')
        self.share_id = map.get('share_id')
        self.upload_id = map.get('upload_id')
        return self


class OSSMoveFileRequest(TeaModel):
    """
    文件移动请求
    """
    def __init__(self, drive_id=None, file_path=None, new_name=None, overwrite=None, share_id=None,
                 to_parent_file_path=None):
        # drive_id
        self.drive_id = drive_id  # type: str
        # file_path
        self.file_path = file_path  # type: str
        # new_name
        self.new_name = new_name  # type: str
        # overwrite
        # type: boolean
        self.overwrite = overwrite  # type: bool
        # share_id
        self.share_id = share_id  # type: str
        # file_path
        self.to_parent_file_path = to_parent_file_path  # type: str

    def validate(self):
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.share_id:
            self.validate_pattern(self.share_id, 'share_id', '[0-9a-zA-Z-]+')

    def to_map(self):
        result = {}
        result['drive_id'] = self.drive_id
        result['file_path'] = self.file_path
        result['new_name'] = self.new_name
        result['overwrite'] = self.overwrite
        result['share_id'] = self.share_id
        result['to_parent_file_path'] = self.to_parent_file_path
        return result

    def from_map(self, map={}):
        self.drive_id = map.get('drive_id')
        self.file_path = map.get('file_path')
        self.new_name = map.get('new_name')
        self.overwrite = map.get('overwrite')
        self.share_id = map.get('share_id')
        self.to_parent_file_path = map.get('to_parent_file_path')
        return self


class OSSVideoDRMLicenseRequest(TeaModel):
    """
    获取视频DRM License
    """
    def __init__(self, drm_type=None, license_request=None):
        # drmType
        self.drm_type = drm_type  # type: str
        # licenseRequest
        self.license_request = license_request  # type: str

    def validate(self):
        self.validate_required(self.drm_type, 'drm_type')
        self.validate_required(self.license_request, 'license_request')

    def to_map(self):
        result = {}
        result['drmType'] = self.drm_type
        result['licenseRequest'] = self.license_request
        return result

    def from_map(self, map={}):
        self.drm_type = map.get('drmType')
        self.license_request = map.get('licenseRequest')
        return self


class OSSVideoDefinitionRequest(TeaModel):
    """
    获取视频分辨率列表
    """
    def __init__(self, drive_id=None, file_path=None, protection_scheme=None, share_id=None):
        # drive_id
        self.drive_id = drive_id  # type: str
        # file_path
        self.file_path = file_path  # type: str
        # protection_scheme
        self.protection_scheme = protection_scheme  # type: str
        # share_id
        self.share_id = share_id  # type: str

    def validate(self):
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_path, 'file_path')
        if self.file_path:
            self.validate_max_length(self.file_path, 'file_path', 1000)
        if self.share_id:
            self.validate_pattern(self.share_id, 'share_id', '[0-9a-zA-Z-]+')

    def to_map(self):
        result = {}
        result['drive_id'] = self.drive_id
        result['file_path'] = self.file_path
        result['protection_scheme'] = self.protection_scheme
        result['share_id'] = self.share_id
        return result

    def from_map(self, map={}):
        self.drive_id = map.get('drive_id')
        self.file_path = map.get('file_path')
        self.protection_scheme = map.get('protection_scheme')
        self.share_id = map.get('share_id')
        return self


class OSSVideoM3U8Request(TeaModel):
    """
    获取视频的m3u8文件
    """
    def __init__(self, definition=None, drive_id=None, expire_sec=None, file_path=None, protection_scheme=None,
                 share_id=None, sign_token=None):
        # definition
        self.definition = definition  # type: str
        # drive_id
        self.drive_id = drive_id  # type: str
        # expire_sec
        self.expire_sec = expire_sec  # type: int
        # file_path
        self.file_path = file_path  # type: str
        # protection_scheme
        self.protection_scheme = protection_scheme  # type: str
        # share_id
        self.share_id = share_id  # type: str
        # sign_token
        self.sign_token = sign_token  # type: str

    def validate(self):
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_path, 'file_path')
        if self.file_path:
            self.validate_max_length(self.file_path, 'file_path', 1000)
        if self.share_id:
            self.validate_pattern(self.share_id, 'share_id', '[0-9a-zA-Z-]+')
        self.validate_required(self.sign_token, 'sign_token')

    def to_map(self):
        result = {}
        result['definition'] = self.definition
        result['drive_id'] = self.drive_id
        result['expire_sec'] = self.expire_sec
        result['file_path'] = self.file_path
        result['protection_scheme'] = self.protection_scheme
        result['share_id'] = self.share_id
        result['sign_token'] = self.sign_token
        return result

    def from_map(self, map={}):
        self.definition = map.get('definition')
        self.drive_id = map.get('drive_id')
        self.expire_sec = map.get('expire_sec')
        self.file_path = map.get('file_path')
        self.protection_scheme = map.get('protection_scheme')
        self.share_id = map.get('share_id')
        self.sign_token = map.get('sign_token')
        return self


class OSSVideoTranscodeRequest(TeaModel):
    """
    启动视频转码请求
    """
    def __init__(self, drive_id=None, file_path=None, hls_time=None, protection_scheme=None, remarks=None,
                 share_id=None, transcode=None):
        # drive_id
        self.drive_id = drive_id  # type: str
        # file_path
        self.file_path = file_path  # type: str
        # hls_time
        self.hls_time = hls_time  # type: int
        # protection_scheme
        self.protection_scheme = protection_scheme  # type: str
        # remarks
        self.remarks = remarks  # type: str
        # share_id
        self.share_id = share_id  # type: str
        # transcode
        self.transcode = transcode  # type: bool

    def validate(self):
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_path, 'file_path')
        if self.file_path:
            self.validate_max_length(self.file_path, 'file_path', 1000)
        if self.share_id:
            self.validate_pattern(self.share_id, 'share_id', '[0-9a-zA-Z-]+')

    def to_map(self):
        result = {}
        result['drive_id'] = self.drive_id
        result['file_path'] = self.file_path
        result['hls_time'] = self.hls_time
        result['protection_scheme'] = self.protection_scheme
        result['remarks'] = self.remarks
        result['share_id'] = self.share_id
        result['transcode'] = self.transcode
        return result

    def from_map(self, map={}):
        self.drive_id = map.get('drive_id')
        self.file_path = map.get('file_path')
        self.hls_time = map.get('hls_time')
        self.protection_scheme = map.get('protection_scheme')
        self.remarks = map.get('remarks')
        self.share_id = map.get('share_id')
        self.transcode = map.get('transcode')
        return self


class PlayMediaRequest(TeaModel):
    """
    play_media request
    """
    def __init__(self, auth_key=None, drive_id=None, file_id=None):
        # auth_key
        self.auth_key = auth_key  # type: str
        # drive_id
        self.drive_id = drive_id  # type: str
        # file_id
        self.file_id = file_id  # type: str

    def validate(self):
        self.validate_required(self.auth_key, 'auth_key')
        if self.auth_key:
            self.validate_pattern(self.auth_key, 'auth_key', '[a-z0-9]+')
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_id, 'file_id')
        if self.file_id:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9.-_]{1,50}')

    def to_map(self):
        result = {}
        result['AuthKey'] = self.auth_key
        result['DriveID'] = self.drive_id
        result['FileID'] = self.file_id
        return result

    def from_map(self, map={}):
        self.auth_key = map.get('AuthKey')
        self.drive_id = map.get('DriveID')
        self.file_id = map.get('FileID')
        return self


class ScanFileMetaRequest(TeaModel):
    """
    全量获取file元信息的请求body
    """
    def __init__(self, headers=None, category=None, drive_id=None, limit=None, marker=None):
        self.headers = headers  # type: dict
        # category
        self.category = category  # type: str
        # drive_id
        self.drive_id = drive_id  # type: str
        # limit
        self.limit = limit  # type: int
        # marker
        self.marker = marker  # type: str

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['category'] = self.category
        result['drive_id'] = self.drive_id
        result['limit'] = self.limit
        result['marker'] = self.marker
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.category = map.get('category')
        self.drive_id = map.get('drive_id')
        self.limit = map.get('limit')
        self.marker = map.get('marker')
        return self


class SearchFileRequest(TeaModel):
    """
    搜索文件元数据
    """
    def __init__(self, headers=None, drive_id=None, image_thumbnail_process=None, image_url_process=None,
                 limit=None, marker=None, order_by=None, query=None, url_expire_sec=None, video_thumbnail_process=None):
        self.headers = headers  # type: dict
        # drive_id
        self.drive_id = drive_id  # type: str
        # image_thumbnail_process
        self.image_thumbnail_process = image_thumbnail_process  # type: str
        # image_url_process
        self.image_url_process = image_url_process  # type: str
        # limit
        self.limit = limit  # type: int
        # Marker
        self.marker = marker  # type: str
        # order_by
        self.order_by = order_by  # type: str
        # query
        self.query = query  # type: str
        # url_expire_sec
        self.url_expire_sec = url_expire_sec  # type: int
        # video_thumbnail_process
        # type:string
        self.video_thumbnail_process = video_thumbnail_process  # type: str

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.query:
            self.validate_max_length(self.query, 'query', 4096)

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['drive_id'] = self.drive_id
        result['image_thumbnail_process'] = self.image_thumbnail_process
        result['image_url_process'] = self.image_url_process
        result['limit'] = self.limit
        result['marker'] = self.marker
        result['order_by'] = self.order_by
        result['query'] = self.query
        result['url_expire_sec'] = self.url_expire_sec
        result['video_thumbnail_process'] = self.video_thumbnail_process
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.drive_id = map.get('drive_id')
        self.image_thumbnail_process = map.get('image_thumbnail_process')
        self.image_url_process = map.get('image_url_process')
        self.limit = map.get('limit')
        self.marker = map.get('marker')
        self.order_by = map.get('order_by')
        self.query = map.get('query')
        self.url_expire_sec = map.get('url_expire_sec')
        self.video_thumbnail_process = map.get('video_thumbnail_process')
        return self


class UCGetObjectInfoByObjectKeyRequest(TeaModel):
    """
    UCGetObjectInfoByObjectKeyRequest
    """
    def __init__(self, object_key=None):
        self.object_key = object_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['object_key'] = self.object_key
        return result

    def from_map(self, map={}):
        self.object_key = map.get('object_key')
        return self


class UCGetObjectInfoBySha1Request(TeaModel):
    """
    UCGetObjectInfoBySha1Request
    """
    def __init__(self, sha_1=None):
        self.sha_1 = sha_1  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['sha1'] = self.sha_1
        return result

    def from_map(self, map={}):
        self.sha_1 = map.get('sha1')
        return self


class UpdateDriveRequest(TeaModel):
    """
    Update drive request
    """
    def __init__(self, headers=None, description=None, drive_id=None, drive_name=None, encrypt_data_access=None,
                 encrypt_mode=None, status=None, total_size=None):
        self.headers = headers  # type: dict
        # 描述信息
        self.description = description  # type: str
        # Drive ID
        self.drive_id = drive_id  # type: str
        # Drive 名称
        self.drive_name = drive_name  # type: str
        # 授权访问加密数据
        self.encrypt_data_access = encrypt_data_access  # type: bool
        # 加密模式
        self.encrypt_mode = encrypt_mode  # type: str
        # 状态
        self.status = status  # type: str
        # 总大小,单位Byte [如果设置 -1 代表不限制]
        self.total_size = total_size  # type: int

    def validate(self):
        if self.description:
            self.validate_max_length(self.description, 'description', 1024)
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_name:
            self.validate_max_length(self.drive_name, 'drive_name', 1024)

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['description'] = self.description
        result['drive_id'] = self.drive_id
        result['drive_name'] = self.drive_name
        result['encrypt_data_access'] = self.encrypt_data_access
        result['encrypt_mode'] = self.encrypt_mode
        result['status'] = self.status
        result['total_size'] = self.total_size
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.description = map.get('description')
        self.drive_id = map.get('drive_id')
        self.drive_name = map.get('drive_name')
        self.encrypt_data_access = map.get('encrypt_data_access')
        self.encrypt_mode = map.get('encrypt_mode')
        self.status = map.get('status')
        self.total_size = map.get('total_size')
        return self


class UpdateFileMetaRequest(TeaModel):
    """
    更新文件元数据
    """
    def __init__(self, headers=None, check_name_mode=None, custom_index_key=None, description=None, drive_id=None,
                 encrypt_mode=None, file_id=None, hidden=None, labels=None, meta=None, name=None, starred=None, user_meta=None):
        self.headers = headers  # type: dict
        # check_name_mode
        self.check_name_mode = check_name_mode  # type: str
        self.custom_index_key = custom_index_key  # type: str
        # description
        # type: string
        self.description = description  # type: str
        # drive_id
        self.drive_id = drive_id  # type: str
        self.encrypt_mode = encrypt_mode  # type: str
        # file_id
        self.file_id = file_id  # type: str
        # hidden
        # type: boolean
        self.hidden = hidden  # type: bool
        # labels
        self.labels = labels  # type: list
        self.meta = meta  # type: str
        # name
        self.name = name  # type: str
        # starred
        # type: boolean
        self.starred = starred  # type: bool
        # user_meta
        self.user_meta = user_meta  # type: str

    def validate(self):
        if self.description:
            self.validate_max_length(self.description, 'description', 1024)
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_id, 'file_id')
        if self.file_id:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9.-_]{1,50}')
        if self.name:
            self.validate_max_length(self.name, 'name', 1024)

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['check_name_mode'] = self.check_name_mode
        result['custom_index_key'] = self.custom_index_key
        result['description'] = self.description
        result['drive_id'] = self.drive_id
        result['encrypt_mode'] = self.encrypt_mode
        result['file_id'] = self.file_id
        result['hidden'] = self.hidden
        result['labels'] = self.labels
        result['meta'] = self.meta
        result['name'] = self.name
        result['starred'] = self.starred
        result['user_meta'] = self.user_meta
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.check_name_mode = map.get('check_name_mode')
        self.custom_index_key = map.get('custom_index_key')
        self.description = map.get('description')
        self.drive_id = map.get('drive_id')
        self.encrypt_mode = map.get('encrypt_mode')
        self.file_id = map.get('file_id')
        self.hidden = map.get('hidden')
        self.labels = map.get('labels')
        self.meta = map.get('meta')
        self.name = map.get('name')
        self.starred = map.get('starred')
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
        self.expiration = expiration  # type: str
        # permissions
        self.permissions = permissions  # type: list
        # share_id
        self.share_id = share_id  # type: str
        # share_name
        self.share_name = share_name  # type: str
        # share_policy
        self.share_policy = share_policy  # type: list
        # status
        self.status = status  # type: str

    def validate(self):
        if self.description:
            self.validate_max_length(self.description, 'description', 1024)
        self.validate_required(self.share_id, 'share_id')
        if self.share_policy:
            for k in self.share_policy:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['description'] = self.description
        result['expiration'] = self.expiration
        result['permissions'] = self.permissions
        result['share_id'] = self.share_id
        result['share_name'] = self.share_name
        result['share_policy'] = []
        if self.share_policy is not None:
            for k in self.share_policy:
                result['share_policy'].append(k.to_map() if k else None)
        else:
            result['share_policy'] = None
        result['status'] = self.status
        return result

    def from_map(self, map={}):
        self.description = map.get('description')
        self.expiration = map.get('expiration')
        self.permissions = map.get('permissions')
        self.share_id = map.get('share_id')
        self.share_name = map.get('share_name')
        self.share_policy = []
        if map.get('share_policy') is not None:
            for k in map.get('share_policy'):
                temp_model = SharePermissionPolicy()
                self.share_policy.append(temp_model.from_map(k))
        else:
            self.share_policy = None
        self.status = map.get('status')
        return self


class VideoMediaMetadata(TeaModel):
    """
    *
    """
    def __init__(self, duration=None):
        # Duration
        self.duration = duration  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['duration'] = self.duration
        return result

    def from_map(self, map={}):
        self.duration = map.get('duration')
        return self


class CreateUserModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: CreateUserResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = CreateUserResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class DeleteUserModel(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class GetUserModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: GetUserResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetUserResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class ListUsersModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: ListUserResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = ListUserResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class SearchUserModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: ListUserResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = ListUserResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class UpdateUserModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: UpdateUserResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = UpdateUserResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class BaseUserResponse(TeaModel):
    """
    Base user response
    """
    def __init__(self, avatar=None, created_at=None, default_drive_id=None, description=None, domain_id=None,
                 email=None, nick_name=None, phone=None, role=None, status=None, updated_at=None, user_data=None,
                 user_id=None, user_name=None):
        # 头像
        self.avatar = avatar  # type: str
        # 用户创建时间
        self.created_at = created_at  # type: int
        # 默认 Drive ID
        self.default_drive_id = default_drive_id  # type: str
        # 用户备注信息
        self.description = description  # type: str
        # Domain ID
        self.domain_id = domain_id  # type: str
        # 邮箱
        self.email = email  # type: str
        # 昵称
        self.nick_name = nick_name  # type: str
        # 电话
        self.phone = phone  # type: str
        # 角色
        self.role = role  # type: str
        # 用户状态
        self.status = status  # type: str
        # 用户修改时间
        self.updated_at = updated_at  # type: int
        # 用户自定义数据，格式为json，可用于配置项、少量临时数据等存储，不超过1K
        self.user_data = user_data  # type: dict
        # 用户 ID
        self.user_id = user_id  # type: str
        # 用户名称
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['avatar'] = self.avatar
        result['created_at'] = self.created_at
        result['default_drive_id'] = self.default_drive_id
        result['description'] = self.description
        result['domain_id'] = self.domain_id
        result['email'] = self.email
        result['nick_name'] = self.nick_name
        result['phone'] = self.phone
        result['role'] = self.role
        result['status'] = self.status
        result['updated_at'] = self.updated_at
        result['user_data'] = self.user_data
        result['user_id'] = self.user_id
        result['user_name'] = self.user_name
        return result

    def from_map(self, map={}):
        self.avatar = map.get('avatar')
        self.created_at = map.get('created_at')
        self.default_drive_id = map.get('default_drive_id')
        self.description = map.get('description')
        self.domain_id = map.get('domain_id')
        self.email = map.get('email')
        self.nick_name = map.get('nick_name')
        self.phone = map.get('phone')
        self.role = map.get('role')
        self.status = map.get('status')
        self.updated_at = map.get('updated_at')
        self.user_data = map.get('user_data')
        self.user_id = map.get('user_id')
        self.user_name = map.get('user_name')
        return self


class CreateUserRequest(TeaModel):
    """
    Create user request
    """
    def __init__(self, headers=None, avatar=None, description=None, email=None, nick_name=None, phone=None, role=None,
                 status=None, user_data=None, user_id=None, user_name=None):
        self.headers = headers  # type: dict
        # 头像
        self.avatar = avatar  # type: str
        # 描述信息
        self.description = description  # type: str
        # 邮箱
        self.email = email  # type: str
        # 昵称
        self.nick_name = nick_name  # type: str
        # 电话号码
        self.phone = phone  # type: str
        # 角色
        self.role = role  # type: str
        # 状态
        self.status = status  # type: str
        # 用户自定义数据，格式为json，可用于配置项、少量临时数据等存储，不超过1K
        self.user_data = user_data  # type: dict
        # 用户 ID
        self.user_id = user_id  # type: str
        # 用户名称
        self.user_name = user_name  # type: str

    def validate(self):
        if self.description:
            self.validate_max_length(self.description, 'description', 1024)
        self.validate_required(self.user_id, 'user_id')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['avatar'] = self.avatar
        result['description'] = self.description
        result['email'] = self.email
        result['nick_name'] = self.nick_name
        result['phone'] = self.phone
        result['role'] = self.role
        result['status'] = self.status
        result['user_data'] = self.user_data
        result['user_id'] = self.user_id
        result['user_name'] = self.user_name
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.avatar = map.get('avatar')
        self.description = map.get('description')
        self.email = map.get('email')
        self.nick_name = map.get('nick_name')
        self.phone = map.get('phone')
        self.role = map.get('role')
        self.status = map.get('status')
        self.user_data = map.get('user_data')
        self.user_id = map.get('user_id')
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
        self.avatar = avatar  # type: str
        # 用户创建时间
        self.created_at = created_at  # type: int
        # 默认 Drive ID
        self.default_drive_id = default_drive_id  # type: str
        # 用户备注信息
        self.description = description  # type: str
        # Domain ID
        self.domain_id = domain_id  # type: str
        # 邮箱
        self.email = email  # type: str
        # 昵称
        self.nick_name = nick_name  # type: str
        # 电话
        self.phone = phone  # type: str
        # 角色
        self.role = role  # type: str
        # 用户状态
        self.status = status  # type: str
        # 用户修改时间
        self.updated_at = updated_at  # type: int
        # 用户自定义数据，格式为json，可用于配置项、少量临时数据等存储，不超过1K
        self.user_data = user_data  # type: dict
        # 用户 ID
        self.user_id = user_id  # type: str
        # 用户名称
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['avatar'] = self.avatar
        result['created_at'] = self.created_at
        result['default_drive_id'] = self.default_drive_id
        result['description'] = self.description
        result['domain_id'] = self.domain_id
        result['email'] = self.email
        result['nick_name'] = self.nick_name
        result['phone'] = self.phone
        result['role'] = self.role
        result['status'] = self.status
        result['updated_at'] = self.updated_at
        result['user_data'] = self.user_data
        result['user_id'] = self.user_id
        result['user_name'] = self.user_name
        return result

    def from_map(self, map={}):
        self.avatar = map.get('avatar')
        self.created_at = map.get('created_at')
        self.default_drive_id = map.get('default_drive_id')
        self.description = map.get('description')
        self.domain_id = map.get('domain_id')
        self.email = map.get('email')
        self.nick_name = map.get('nick_name')
        self.phone = map.get('phone')
        self.role = map.get('role')
        self.status = map.get('status')
        self.updated_at = map.get('updated_at')
        self.user_data = map.get('user_data')
        self.user_id = map.get('user_id')
        self.user_name = map.get('user_name')
        return self


class DeleteUserRequest(TeaModel):
    """
    Delete user request
    """
    def __init__(self, headers=None, user_id=None):
        self.headers = headers  # type: dict
        # 用户 ID
        self.user_id = user_id  # type: str

    def validate(self):
        self.validate_required(self.user_id, 'user_id')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['user_id'] = self.user_id
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
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
        self.headers = headers  # type: dict
        # 用户 ID, 使用ak方式访问，该项必传, access_token访问如果不传，默认取自己的user信息
        # example
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['user_id'] = self.user_id
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
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
        self.avatar = avatar  # type: str
        # 用户创建时间
        self.created_at = created_at  # type: int
        # 默认 Drive ID
        self.default_drive_id = default_drive_id  # type: str
        # 用户备注信息
        self.description = description  # type: str
        # Domain ID
        self.domain_id = domain_id  # type: str
        # 邮箱
        self.email = email  # type: str
        # 昵称
        self.nick_name = nick_name  # type: str
        # 电话
        self.phone = phone  # type: str
        # 角色
        self.role = role  # type: str
        # 用户状态
        self.status = status  # type: str
        # 用户修改时间
        self.updated_at = updated_at  # type: int
        # 用户自定义数据，格式为json，可用于配置项、少量临时数据等存储，不超过1K
        self.user_data = user_data  # type: dict
        # 用户 ID
        self.user_id = user_id  # type: str
        # 用户名称
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['avatar'] = self.avatar
        result['created_at'] = self.created_at
        result['default_drive_id'] = self.default_drive_id
        result['description'] = self.description
        result['domain_id'] = self.domain_id
        result['email'] = self.email
        result['nick_name'] = self.nick_name
        result['phone'] = self.phone
        result['role'] = self.role
        result['status'] = self.status
        result['updated_at'] = self.updated_at
        result['user_data'] = self.user_data
        result['user_id'] = self.user_id
        result['user_name'] = self.user_name
        return result

    def from_map(self, map={}):
        self.avatar = map.get('avatar')
        self.created_at = map.get('created_at')
        self.default_drive_id = map.get('default_drive_id')
        self.description = map.get('description')
        self.domain_id = map.get('domain_id')
        self.email = map.get('email')
        self.nick_name = map.get('nick_name')
        self.phone = map.get('phone')
        self.role = map.get('role')
        self.status = map.get('status')
        self.updated_at = map.get('updated_at')
        self.user_data = map.get('user_data')
        self.user_id = map.get('user_id')
        self.user_name = map.get('user_name')
        return self


class ListUserRequest(TeaModel):
    """
    List user request
    """
    def __init__(self, headers=None, limit=None, marker=None):
        self.headers = headers  # type: dict
        # 每页大小限制
        self.limit = limit  # type: int
        # 翻页标记
        self.marker = marker  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['limit'] = self.limit
        result['marker'] = self.marker
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.limit = map.get('limit')
        self.marker = map.get('marker')
        return self


class ListUserResponse(TeaModel):
    """
    List user response
    """
    def __init__(self, items=None, next_marker=None):
        self.items = items  # type: list
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
        else:
            result['items'] = None
        result['next_marker'] = self.next_marker
        return result

    def from_map(self, map={}):
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = BaseUserResponse()
                self.items.append(temp_model.from_map(k))
        else:
            self.items = None
        self.next_marker = map.get('next_marker')
        return self


class SearchUserRequest(TeaModel):
    """
    Search user request
    """
    def __init__(self, headers=None, email=None, limit=None, marker=None, nick_name=None, phone=None, role=None,
                 status=None, user_name=None):
        self.headers = headers  # type: dict
        # 邮箱
        self.email = email  # type: str
        # 每页大小限制
        self.limit = limit  # type: int
        # 翻页标记
        self.marker = marker  # type: str
        # 昵称
        self.nick_name = nick_name  # type: str
        # 电话号码
        self.phone = phone  # type: str
        # 角色
        self.role = role  # type: str
        # 状态
        self.status = status  # type: str
        # 用户名
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['email'] = self.email
        result['limit'] = self.limit
        result['marker'] = self.marker
        result['nick_name'] = self.nick_name
        result['phone'] = self.phone
        result['role'] = self.role
        result['status'] = self.status
        result['user_name'] = self.user_name
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.email = map.get('email')
        self.limit = map.get('limit')
        self.marker = map.get('marker')
        self.nick_name = map.get('nick_name')
        self.phone = map.get('phone')
        self.role = map.get('role')
        self.status = map.get('status')
        self.user_name = map.get('user_name')
        return self


class UpdateUserRequest(TeaModel):
    """
    Update user request
    """
    def __init__(self, headers=None, avatar=None, description=None, email=None, nick_name=None, phone=None, role=None,
                 status=None, user_data=None, user_id=None):
        self.headers = headers  # type: dict
        # 头像
        self.avatar = avatar  # type: str
        # 描述信息
        self.description = description  # type: str
        # 邮箱
        self.email = email  # type: str
        # 昵称
        self.nick_name = nick_name  # type: str
        # 电话号码
        self.phone = phone  # type: str
        # 角色
        self.role = role  # type: str
        # 状态
        self.status = status  # type: str
        # 用户自定义数据，格式为json，可用于配置项、少量临时数据等存储，不超过1K
        self.user_data = user_data  # type: dict
        # 用户 ID
        self.user_id = user_id  # type: str

    def validate(self):
        if self.description:
            self.validate_max_length(self.description, 'description', 1024)
        self.validate_required(self.user_id, 'user_id')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['avatar'] = self.avatar
        result['description'] = self.description
        result['email'] = self.email
        result['nick_name'] = self.nick_name
        result['phone'] = self.phone
        result['role'] = self.role
        result['status'] = self.status
        result['user_data'] = self.user_data
        result['user_id'] = self.user_id
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.avatar = map.get('avatar')
        self.description = map.get('description')
        self.email = map.get('email')
        self.nick_name = map.get('nick_name')
        self.phone = map.get('phone')
        self.role = map.get('role')
        self.status = map.get('status')
        self.user_data = map.get('user_data')
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
        self.avatar = avatar  # type: str
        # 用户创建时间
        self.created_at = created_at  # type: int
        # 默认 Drive ID
        self.default_drive_id = default_drive_id  # type: str
        # 用户备注信息
        self.description = description  # type: str
        # Domain ID
        self.domain_id = domain_id  # type: str
        # 邮箱
        self.email = email  # type: str
        # 昵称
        self.nick_name = nick_name  # type: str
        # 电话
        self.phone = phone  # type: str
        # 角色
        self.role = role  # type: str
        # 用户状态
        self.status = status  # type: str
        # 用户修改时间
        self.updated_at = updated_at  # type: int
        # 用户自定义数据，格式为json，可用于配置项、少量临时数据等存储，不超过1K
        self.user_data = user_data  # type: dict
        # 用户 ID
        self.user_id = user_id  # type: str
        # 用户名称
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['avatar'] = self.avatar
        result['created_at'] = self.created_at
        result['default_drive_id'] = self.default_drive_id
        result['description'] = self.description
        result['domain_id'] = self.domain_id
        result['email'] = self.email
        result['nick_name'] = self.nick_name
        result['phone'] = self.phone
        result['role'] = self.role
        result['status'] = self.status
        result['updated_at'] = self.updated_at
        result['user_data'] = self.user_data
        result['user_id'] = self.user_id
        result['user_name'] = self.user_name
        return result

    def from_map(self, map={}):
        self.avatar = map.get('avatar')
        self.created_at = map.get('created_at')
        self.default_drive_id = map.get('default_drive_id')
        self.description = map.get('description')
        self.domain_id = map.get('domain_id')
        self.email = map.get('email')
        self.nick_name = map.get('nick_name')
        self.phone = map.get('phone')
        self.role = map.get('role')
        self.status = map.get('status')
        self.updated_at = map.get('updated_at')
        self.user_data = map.get('user_data')
        self.user_id = map.get('user_id')
        self.user_name = map.get('user_name')
        return self


class CreateStoryModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: CreateStoryResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = CreateStoryResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class GetPhotoCountModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: GetImageCountResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetImageCountResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class GetStoryDetailModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: GetStoryDetailResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetStoryDetailResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class GetStoryTaskModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: GetStoryTaskResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetStoryTaskResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class ListAddressGroupsModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: ListImageAddressGroupsResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = ListImageAddressGroupsResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class ListFaceGroupsModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: ListImageFaceGroupsResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = ListImageFaceGroupsResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class ListStoryModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: ListStoryResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = ListStoryResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class ListTagsModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: ListImageTagsResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = ListImageTagsResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class SearchAddressGroupsModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: SearchImageAddressGroupsResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = SearchImageAddressGroupsResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class UpdateFacegroupInfoModel(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict
        self.body = body  # type: UpdateFaceGroupInfoResponse

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = UpdateFaceGroupInfoResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class Address(TeaModel):
    """
    *
    """
    def __init__(self, city=None, country=None, district=None, province=None, township=None):
        self.city = city  # type: str
        self.country = country  # type: str
        self.district = district  # type: str
        self.province = province  # type: str
        self.township = township  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['city'] = self.city
        result['country'] = self.country
        result['district'] = self.district
        result['province'] = self.province
        result['township'] = self.township
        return result

    def from_map(self, map={}):
        self.city = map.get('city')
        self.country = map.get('country')
        self.district = map.get('district')
        self.province = map.get('province')
        self.township = map.get('township')
        return self


class CreateStoryRequest(TeaModel):
    """
    Create story request
    """
    def __init__(self, headers=None, drive_id=None):
        self.headers = headers  # type: dict
        # drive_id
        self.drive_id = drive_id  # type: str

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['drive_id'] = self.drive_id
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.drive_id = map.get('drive_id')
        return self


class CreateStoryResponse(TeaModel):
    """
    生成故事
    """
    def __init__(self, drive_id=None):
        self.drive_id = drive_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['drive_id'] = self.drive_id
        return result

    def from_map(self, map={}):
        self.drive_id = map.get('drive_id')
        return self


class GetImageCountRequest(TeaModel):
    """
    Get photo count request
    """
    def __init__(self, headers=None, drive_id=None):
        self.headers = headers  # type: dict
        # drive_id
        self.drive_id = drive_id  # type: str

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['drive_id'] = self.drive_id
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
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
        result['image_count'] = self.image_count
        return result

    def from_map(self, map={}):
        self.image_count = map.get('image_count')
        return self


class GetStoryDetailRequest(TeaModel):
    """
    Get story detail request
    """
    def __init__(self, headers=None, drive_id=None, story_id=None, video_url_expire_sec=None):
        self.headers = headers  # type: dict
        # drive_id
        self.drive_id = drive_id  # type: str
        # story_id
        self.story_id = story_id  # type: str
        # url_expire_sec
        self.video_url_expire_sec = video_url_expire_sec  # type: int

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.story_id, 'story_id')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['drive_id'] = self.drive_id
        result['story_id'] = self.story_id
        result['video_url_expire_sec'] = self.video_url_expire_sec
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.drive_id = map.get('drive_id')
        self.story_id = map.get('story_id')
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
        self.created_at = created_at  # type: str
        # items
        self.items = items  # type: list
        # score
        self.score = score  # type: int
        # story_id
        self.story_id = story_id  # type: str
        # story_images_date_range
        self.story_images_date_range = story_images_date_range  # type: list
        # sub_title
        self.sub_title = sub_title  # type: str
        # title
        self.title = title  # type: str
        # updated_at
        self.updated_at = updated_at  # type: str
        # video_status
        self.video_status = video_status  # type: str
        # video_url
        self.video_url = video_url  # type: str

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['cover_file_id'] = self.cover_file_id
        result['created_at'] = self.created_at
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        else:
            result['items'] = None
        result['score'] = self.score
        result['story_id'] = self.story_id
        result['story_images_date_range'] = self.story_images_date_range
        result['sub_title'] = self.sub_title
        result['title'] = self.title
        result['updated_at'] = self.updated_at
        result['video_status'] = self.video_status
        result['video_url'] = self.video_url
        return result

    def from_map(self, map={}):
        self.cover_file_id = map.get('cover_file_id')
        self.created_at = map.get('created_at')
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = BaseFileResponse()
                self.items.append(temp_model.from_map(k))
        else:
            self.items = None
        self.score = map.get('score')
        self.story_id = map.get('story_id')
        self.story_images_date_range = map.get('story_images_date_range')
        self.sub_title = map.get('sub_title')
        self.title = map.get('title')
        self.updated_at = map.get('updated_at')
        self.video_status = map.get('video_status')
        self.video_url = map.get('video_url')
        return self


class GetStoryTaskRequest(TeaModel):
    """
    Get create story task request
    """
    def __init__(self, headers=None, drive_id=None):
        self.headers = headers  # type: dict
        # Drive ID
        self.drive_id = drive_id  # type: str

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['drive_id'] = self.drive_id
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.drive_id = map.get('drive_id')
        return self


class GetStoryTaskResponse(TeaModel):
    """
    故事任务状态
    """
    def __init__(self, drive_id=None, status=None):
        self.drive_id = drive_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['drive_id'] = self.drive_id
        result['status'] = self.status
        return result

    def from_map(self, map={}):
        self.drive_id = map.get('drive_id')
        self.status = map.get('status')
        return self


class ImageAddressResponse(TeaModel):
    """
    *
    """
    def __init__(self, address_detail=None, count=None, cover_file_id=None, cover_url=None, location=None, name=None):
        self.address_detail = address_detail  # type: Address
        # 聚类地点计数
        self.count = count  # type: int
        # cover_file_id
        self.cover_file_id = cover_file_id  # type: str
        # 聚类地点封面图片地址
        self.cover_url = cover_url  # type: str
        # 经纬度
        self.location = location  # type: str
        # 聚类地点名称
        self.name = name  # type: str

    def validate(self):
        if self.address_detail:
            self.address_detail.validate()

    def to_map(self):
        result = {}
        if self.address_detail is not None:
            result['address_detail'] = self.address_detail.to_map()
        else:
            result['address_detail'] = None
        result['count'] = self.count
        result['cover_file_id'] = self.cover_file_id
        result['cover_url'] = self.cover_url
        result['location'] = self.location
        result['name'] = self.name
        return result

    def from_map(self, map={}):
        if map.get('address_detail') is not None:
            temp_model = Address()
            self.address_detail = temp_model.from_map(map['address_detail'])
        else:
            self.address_detail = None
        self.count = map.get('count')
        self.cover_file_id = map.get('cover_file_id')
        self.cover_url = map.get('cover_url')
        self.location = map.get('location')
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
        self.created_at = created_at  # type: str
        # 人脸个数
        self.face_count = face_count  # type: int
        # 人脸分组封面头像地址
        self.group_cover_url = group_cover_url  # type: str
        # 人脸分组 ID
        self.group_id = group_id  # type: str
        # 人脸分组名称
        self.group_name = group_name  # type: str
        # 照片个数
        self.image_count = image_count  # type: int
        # 人脸分组修改时间
        self.updated_at = updated_at  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['cover_file_id'] = self.cover_file_id
        result['created_at'] = self.created_at
        result['face_count'] = self.face_count
        result['group_cover_url'] = self.group_cover_url
        result['group_id'] = self.group_id
        result['group_name'] = self.group_name
        result['image_count'] = self.image_count
        result['updated_at'] = self.updated_at
        return result

    def from_map(self, map={}):
        self.cover_file_id = map.get('cover_file_id')
        self.created_at = map.get('created_at')
        self.face_count = map.get('face_count')
        self.group_cover_url = map.get('group_cover_url')
        self.group_id = map.get('group_id')
        self.group_name = map.get('group_name')
        self.image_count = map.get('image_count')
        self.updated_at = map.get('updated_at')
        return self


class ImageTagResponse(TeaModel):
    """
    *
    """
    def __init__(self, count=None, cover_file_id=None, cover_url=None, name=None):
        # 聚类标签计数
        self.count = count  # type: int
        # cover_file_id
        self.cover_file_id = cover_file_id  # type: str
        # 聚类标签封面图片地址
        self.cover_url = cover_url  # type: str
        # 聚类标签名称
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['count'] = self.count
        result['cover_file_id'] = self.cover_file_id
        result['cover_url'] = self.cover_url
        result['name'] = self.name
        return result

    def from_map(self, map={}):
        self.count = map.get('count')
        self.cover_file_id = map.get('cover_file_id')
        self.cover_url = map.get('cover_url')
        self.name = map.get('name')
        return self


class ListImageAddressGroupsRequest(TeaModel):
    """
    List image address groups request
    """
    def __init__(self, headers=None, drive_id=None, image_thumbnail_process=None, limit=None, marker=None):
        self.headers = headers  # type: dict
        # Drive ID
        self.drive_id = drive_id  # type: str
        # image_thumbnail_process
        # type:string
        self.image_thumbnail_process = image_thumbnail_process  # type: str
        # 每页大小限制
        self.limit = limit  # type: int
        # 翻页标记
        self.marker = marker  # type: str

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['drive_id'] = self.drive_id
        result['image_thumbnail_process'] = self.image_thumbnail_process
        result['limit'] = self.limit
        result['marker'] = self.marker
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.drive_id = map.get('drive_id')
        self.image_thumbnail_process = map.get('image_thumbnail_process')
        self.limit = map.get('limit')
        self.marker = map.get('marker')
        return self


class ListImageAddressGroupsResponse(TeaModel):
    """
    展示地点分组集合
    """
    def __init__(self, items=None, next_marker=None):
        self.items = items  # type: list
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
        else:
            result['items'] = None
        result['next_marker'] = self.next_marker
        return result

    def from_map(self, map={}):
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = ImageAddressResponse()
                self.items.append(temp_model.from_map(k))
        else:
            self.items = None
        self.next_marker = map.get('next_marker')
        return self


class ListImageFaceGroupsRequest(TeaModel):
    """
    List image face groups request
    """
    def __init__(self, headers=None, drive_id=None, limit=None, marker=None):
        self.headers = headers  # type: dict
        # Drive ID
        self.drive_id = drive_id  # type: str
        # 每页大小限制
        self.limit = limit  # type: int
        # 翻页标记
        self.marker = marker  # type: str

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['drive_id'] = self.drive_id
        result['limit'] = self.limit
        result['marker'] = self.marker
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.drive_id = map.get('drive_id')
        self.limit = map.get('limit')
        self.marker = map.get('marker')
        return self


class ListImageFaceGroupsResponse(TeaModel):
    """
    展示人脸分组集合
    """
    def __init__(self, items=None, next_marker=None):
        self.items = items  # type: list
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
        else:
            result['items'] = None
        result['next_marker'] = self.next_marker
        return result

    def from_map(self, map={}):
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = ImageFaceGroupResponse()
                self.items.append(temp_model.from_map(k))
        else:
            self.items = None
        self.next_marker = map.get('next_marker')
        return self


class ListImageTagsRequest(TeaModel):
    """
    List image tags request
    """
    def __init__(self, headers=None, drive_id=None, image_thumbnail_process=None):
        self.headers = headers  # type: dict
        # Drive ID
        self.drive_id = drive_id  # type: str
        # image_thumbnail_process
        # type:string
        self.image_thumbnail_process = image_thumbnail_process  # type: str

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['drive_id'] = self.drive_id
        result['image_thumbnail_process'] = self.image_thumbnail_process
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.drive_id = map.get('drive_id')
        self.image_thumbnail_process = map.get('image_thumbnail_process')
        return self


class ListImageTagsResponse(TeaModel):
    """
    展示标签集合
    """
    def __init__(self, tags=None):
        self.tags = tags  # type: list

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
        else:
            result['tags'] = None
        return result

    def from_map(self, map={}):
        self.tags = []
        if map.get('tags') is not None:
            for k in map.get('tags'):
                temp_model = ImageTagResponse()
                self.tags.append(temp_model.from_map(k))
        else:
            self.tags = None
        return self


class ListStoryRequest(TeaModel):
    """
    List story request
    """
    def __init__(self, headers=None, drive_id=None, limit=None, marker=None):
        self.headers = headers  # type: dict
        # drive_id
        self.drive_id = drive_id  # type: str
        # 每页大小限制
        self.limit = limit  # type: int
        # 翻页标记
        self.marker = marker  # type: str

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['drive_id'] = self.drive_id
        result['limit'] = self.limit
        result['marker'] = self.marker
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.drive_id = map.get('drive_id')
        self.limit = map.get('limit')
        self.marker = map.get('marker')
        return self


class ListStoryResponse(TeaModel):
    """
    故事列表
    """
    def __init__(self, items=None, next_marker=None):
        # items
        self.items = items  # type: list
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
        else:
            result['items'] = None
        result['next_marker'] = self.next_marker
        return result

    def from_map(self, map={}):
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = StoryResponse()
                self.items.append(temp_model.from_map(k))
        else:
            self.items = None
        self.next_marker = map.get('next_marker')
        return self


class RemoveStoryImagesRequest(TeaModel):
    """
    Remove story images request
    """
    def __init__(self, drive_id=None, file_ids=None, story_id=None):
        self.drive_id = drive_id  # type: str
        self.file_ids = file_ids  # type: list
        self.story_id = story_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['drive_id'] = self.drive_id
        result['file_ids'] = self.file_ids
        result['story_id'] = self.story_id
        return result

    def from_map(self, map={}):
        self.drive_id = map.get('drive_id')
        self.file_ids = map.get('file_ids')
        self.story_id = map.get('story_id')
        return self


class SearchImageAddressGroupsRequest(TeaModel):
    """
    Search image address groups request
    """
    def __init__(self, headers=None, address_level=None, address_names=None, br_geo_point=None, drive_id=None,
                 image_thumbnail_process=None, tl_geo_point=None):
        self.headers = headers  # type: dict
        # 查询的地点级别
        self.address_level = address_level  # type: str
        # 查询的地点数组
        self.address_names = address_names  # type: list
        # br_geo_point
        self.br_geo_point = br_geo_point  # type: str
        # Drive ID
        self.drive_id = drive_id  # type: str
        # image_thumbnail_process
        # type:string
        self.image_thumbnail_process = image_thumbnail_process  # type: str
        # tl_geo_point
        self.tl_geo_point = tl_geo_point  # type: str

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['address_level'] = self.address_level
        result['address_names'] = self.address_names
        result['br_geo_point'] = self.br_geo_point
        result['drive_id'] = self.drive_id
        result['image_thumbnail_process'] = self.image_thumbnail_process
        result['tl_geo_point'] = self.tl_geo_point
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.address_level = map.get('address_level')
        self.address_names = map.get('address_names')
        self.br_geo_point = map.get('br_geo_point')
        self.drive_id = map.get('drive_id')
        self.image_thumbnail_process = map.get('image_thumbnail_process')
        self.tl_geo_point = map.get('tl_geo_point')
        return self


class SearchImageAddressGroupsResponse(TeaModel):
    """
    展示地点分组列表
    """
    def __init__(self, items=None):
        self.items = items  # type: list

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
        else:
            result['items'] = None
        return result

    def from_map(self, map={}):
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = ImageAddressResponse()
                self.items.append(temp_model.from_map(k))
        else:
            self.items = None
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
        self.created_at = created_at  # type: str
        # score
        self.score = score  # type: int
        # story_id
        self.story_id = story_id  # type: str
        # story_images_date_range
        self.story_images_date_range = story_images_date_range  # type: list
        # sub_title
        self.sub_title = sub_title  # type: str
        # title
        self.title = title  # type: str
        # updated_at
        self.updated_at = updated_at  # type: str
        # video_status
        self.video_status = video_status  # type: str
        # video_url
        self.video_url = video_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['cover_file_id'] = self.cover_file_id
        result['created_at'] = self.created_at
        result['score'] = self.score
        result['story_id'] = self.story_id
        result['story_images_date_range'] = self.story_images_date_range
        result['sub_title'] = self.sub_title
        result['title'] = self.title
        result['updated_at'] = self.updated_at
        result['video_status'] = self.video_status
        result['video_url'] = self.video_url
        return result

    def from_map(self, map={}):
        self.cover_file_id = map.get('cover_file_id')
        self.created_at = map.get('created_at')
        self.score = map.get('score')
        self.story_id = map.get('story_id')
        self.story_images_date_range = map.get('story_images_date_range')
        self.sub_title = map.get('sub_title')
        self.title = map.get('title')
        self.updated_at = map.get('updated_at')
        self.video_status = map.get('video_status')
        self.video_url = map.get('video_url')
        return self


class UpdateFaceGroupInfoRequest(TeaModel):
    """
    Update face group info request
    """
    def __init__(self, headers=None, drive_id=None, group_id=None, group_name=None):
        self.headers = headers  # type: dict
        # drive_id
        self.drive_id = drive_id  # type: str
        # group_id 列举人脸分组接口中获取
        self.group_id = group_id  # type: str
        # group_name
        self.group_name = group_name  # type: str

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.group_id, 'group_id')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['drive_id'] = self.drive_id
        result['group_id'] = self.group_id
        result['group_name'] = self.group_name
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.drive_id = map.get('drive_id')
        self.group_id = map.get('group_id')
        self.group_name = map.get('group_name')
        return self


class UpdateFaceGroupInfoResponse(TeaModel):
    """
    更新人脸分组信息结果
    """
    def __init__(self, drive_id=None, group_id=None):
        # drive_id
        self.drive_id = drive_id  # type: str
        # group_id
        self.group_id = group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['drive_id'] = self.drive_id
        result['group_id'] = self.group_id
        return result

    def from_map(self, map={}):
        self.drive_id = map.get('drive_id')
        self.group_id = map.get('group_id')
        return self
