# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class RuntimeOptions(TeaModel):
    def __init__(
        self,
        autoretry: bool = None,
        ignore_ssl: bool = None,
        max_attempts: int = None,
        backoff_policy: str = None,
        backoff_period: int = None,
        read_timeout: int = None,
        connect_timeout: int = None,
        http_proxy: str = None,
        https_proxy: str = None,
        no_proxy: str = None,
        max_idle_conns: int = None,
        local_addr: str = None,
        socks_5proxy: str = None,
        socks_5net_work: str = None,
    ):
        # whether to try again
        self.autoretry = autoretry
        # ignore SSL validation
        self.ignore_ssl = ignore_ssl
        # maximum number of retries
        self.max_attempts = max_attempts
        # backoff policy
        self.backoff_policy = backoff_policy
        # backoff period
        self.backoff_period = backoff_period
        # read timeout
        self.read_timeout = read_timeout
        # connect timeout
        self.connect_timeout = connect_timeout
        # http proxy url
        self.http_proxy = http_proxy
        # https Proxy url
        self.https_proxy = https_proxy
        # agent blacklist
        self.no_proxy = no_proxy
        # maximum number of connections
        self.max_idle_conns = max_idle_conns
        # local addr
        self.local_addr = local_addr
        # SOCKS5 proxy
        self.socks_5proxy = socks_5proxy
        # SOCKS5 netWork
        self.socks_5net_work = socks_5net_work

    def validate(self):
        pass

    def to_map(self):
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoretry') is not None:
            self.autoretry = m.get('autoretry')
        if m.get('ignoreSSL') is not None:
            self.ignore_ssl = m.get('ignoreSSL')
        if m.get('maxAttempts') is not None:
            self.max_attempts = m.get('maxAttempts')
        if m.get('backoffPolicy') is not None:
            self.backoff_policy = m.get('backoffPolicy')
        if m.get('backoffPeriod') is not None:
            self.backoff_period = m.get('backoffPeriod')
        if m.get('readTimeout') is not None:
            self.read_timeout = m.get('readTimeout')
        if m.get('connectTimeout') is not None:
            self.connect_timeout = m.get('connectTimeout')
        if m.get('httpProxy') is not None:
            self.http_proxy = m.get('httpProxy')
        if m.get('httpsProxy') is not None:
            self.https_proxy = m.get('httpsProxy')
        if m.get('noProxy') is not None:
            self.no_proxy = m.get('noProxy')
        if m.get('maxIdleConns') is not None:
            self.max_idle_conns = m.get('maxIdleConns')
        if m.get('localAddr') is not None:
            self.local_addr = m.get('localAddr')
        if m.get('socks5Proxy') is not None:
            self.socks_5proxy = m.get('socks5Proxy')
        if m.get('socks5NetWork') is not None:
            self.socks_5net_work = m.get('socks5NetWork')
        return self


class Config(TeaModel):
    def __init__(
        self,
        endpoint: str = None,
        domain_id: str = None,
        client_id: str = None,
        refresh_token: str = None,
        client_secret: str = None,
        access_token: str = None,
        expire_time: str = None,
        protocol: str = None,
        type: str = None,
        security_token: str = None,
        access_key_id: str = None,
        access_key_secret: str = None,
        nickname: str = None,
        user_agent: str = None,
    ):
        self.endpoint = endpoint
        self.domain_id = domain_id
        self.client_id = client_id
        self.refresh_token = refresh_token
        self.client_secret = client_secret
        self.access_token = access_token
        self.expire_time = expire_time
        self.protocol = protocol
        self.type = type
        self.security_token = security_token
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        self.nickname = nickname
        self.user_agent = user_agent

    def validate(self):
        if self.domain_id is not None:
            self.validate_pattern(self.domain_id, 'domain_id', '^[a-zA-Z0-9_-]+$')

    def to_map(self):
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')
        if m.get('clientId') is not None:
            self.client_id = m.get('clientId')
        if m.get('refreshToken') is not None:
            self.refresh_token = m.get('refreshToken')
        if m.get('clientSecret') is not None:
            self.client_secret = m.get('clientSecret')
        if m.get('accessToken') is not None:
            self.access_token = m.get('accessToken')
        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('securityToken') is not None:
            self.security_token = m.get('securityToken')
        if m.get('accessKeyId') is not None:
            self.access_key_id = m.get('accessKeyId')
        if m.get('accessKeySecret') is not None:
            self.access_key_secret = m.get('accessKeySecret')
        if m.get('nickname') is not None:
            self.nickname = m.get('nickname')
        if m.get('userAgent') is not None:
            self.user_agent = m.get('userAgent')
        return self


class LinkInfo(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        extra: str = None,
        identity: str = None,
        type: str = None,
    ):
        # 额外的信息，比如type为mobile时，此字段为国家编号，不填默认86
        self.extra = extra
        # 当前用户已存在的登录标识
        self.identity = identity
        # 当前用户已存在的登录方式
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.extra is not None:
            result['extra'] = self.extra
        if self.identity is not None:
            result['identity'] = self.identity
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('extra') is not None:
            self.extra = m.get('extra')
        if m.get('identity') is not None:
            self.identity = m.get('identity')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class AccountAccessTokenResponse(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        access_token: str = None,
        avatar: str = None,
        default_drive_id: str = None,
        default_sbox_drive_id: str = None,
        device_id: str = None,
        device_name: str = None,
        exist_link: List[LinkInfo] = None,
        expire_time: str = None,
        expires_in: int = None,
        is_first_login: bool = None,
        need_link: bool = None,
        need_rp_verify: bool = None,
        nick_name: str = None,
        pin_setup: bool = None,
        refresh_token: str = None,
        role: str = None,
        state: str = None,
        status: str = None,
        subdomain_id: str = None,
        token_type: str = None,
        user_data: dict = None,
        user_id: str = None,
        user_name: str = None,
    ):
        # 用于调用业务接口的accessToken
        self.access_token = access_token
        # 当前用户头像
        self.avatar = avatar
        # Default Drive ID
        self.default_drive_id = default_drive_id
        # Default Sbox Drive ID
        self.default_sbox_drive_id = default_sbox_drive_id
        # device_id 通过device flow 绑定的设备ID
        self.device_id = device_id
        # device_name 通过device flow 绑定的设备名
        self.device_name = device_name
        # 当前用户已存在的登录方式
        self.exist_link = exist_link
        # accessToken过期时间，ISO时间
        self.expire_time = expire_time
        # accessToken过期时间，单位秒
        self.expires_in = expires_in
        # 用户是否为第一次登录
        self.is_first_login = is_first_login
        # 是否需要绑定
        self.need_link = need_link
        # 用户是否需要进行的实人认证
        self.need_rp_verify = need_rp_verify
        # 当前用户昵称
        self.nick_name = nick_name
        # 用户的数据密码是否设置过
        self.pin_setup = pin_setup
        # 用于刷新accessToken
        self.refresh_token = refresh_token
        # 当前用户角色
        self.role = role
        # 临时权限，用于登录成功后设置密码
        self.state = state
        # 当前用户状态
        self.status = status
        # subdomain_id 用户登录的subdomain_id
        self.subdomain_id = subdomain_id
        # accessToken类型，Bearer
        self.token_type = token_type
        # 用户自定义数据，格式为json，可用于配置项、少量临时数据等存储，不超过1K
        self.user_data = user_data
        # 当前用户ID
        self.user_id = user_id
        # 当前用户名
        self.user_name = user_name

    def validate(self):
        self.validate_required(self.access_token, 'access_token')
        if self.exist_link:
            for k in self.exist_link:
                if k:
                    k.validate()
        self.validate_required(self.need_link, 'need_link')

    def to_map(self):
        result = dict()
        if self.access_token is not None:
            result['access_token'] = self.access_token
        if self.avatar is not None:
            result['avatar'] = self.avatar
        if self.default_drive_id is not None:
            result['default_drive_id'] = self.default_drive_id
        if self.default_sbox_drive_id is not None:
            result['default_sbox_drive_id'] = self.default_sbox_drive_id
        if self.device_id is not None:
            result['device_id'] = self.device_id
        if self.device_name is not None:
            result['device_name'] = self.device_name
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
        if self.need_rp_verify is not None:
            result['need_rp_verify'] = self.need_rp_verify
        if self.nick_name is not None:
            result['nick_name'] = self.nick_name
        if self.pin_setup is not None:
            result['pin_setup'] = self.pin_setup
        if self.refresh_token is not None:
            result['refresh_token'] = self.refresh_token
        if self.role is not None:
            result['role'] = self.role
        if self.state is not None:
            result['state'] = self.state
        if self.status is not None:
            result['status'] = self.status
        if self.subdomain_id is not None:
            result['subdomain_id'] = self.subdomain_id
        if self.token_type is not None:
            result['token_type'] = self.token_type
        if self.user_data is not None:
            result['user_data'] = self.user_data
        if self.user_id is not None:
            result['user_id'] = self.user_id
        if self.user_name is not None:
            result['user_name'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('access_token') is not None:
            self.access_token = m.get('access_token')
        if m.get('avatar') is not None:
            self.avatar = m.get('avatar')
        if m.get('default_drive_id') is not None:
            self.default_drive_id = m.get('default_drive_id')
        if m.get('default_sbox_drive_id') is not None:
            self.default_sbox_drive_id = m.get('default_sbox_drive_id')
        if m.get('device_id') is not None:
            self.device_id = m.get('device_id')
        if m.get('device_name') is not None:
            self.device_name = m.get('device_name')
        self.exist_link = []
        if m.get('exist_link') is not None:
            for k in m.get('exist_link'):
                temp_model = LinkInfo()
                self.exist_link.append(temp_model.from_map(k))
        if m.get('expire_time') is not None:
            self.expire_time = m.get('expire_time')
        if m.get('expires_in') is not None:
            self.expires_in = m.get('expires_in')
        if m.get('is_first_login') is not None:
            self.is_first_login = m.get('is_first_login')
        if m.get('need_link') is not None:
            self.need_link = m.get('need_link')
        if m.get('need_rp_verify') is not None:
            self.need_rp_verify = m.get('need_rp_verify')
        if m.get('nick_name') is not None:
            self.nick_name = m.get('nick_name')
        if m.get('pin_setup') is not None:
            self.pin_setup = m.get('pin_setup')
        if m.get('refresh_token') is not None:
            self.refresh_token = m.get('refresh_token')
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('subdomain_id') is not None:
            self.subdomain_id = m.get('subdomain_id')
        if m.get('token_type') is not None:
            self.token_type = m.get('token_type')
        if m.get('user_data') is not None:
            self.user_data = m.get('user_data')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')
        return self


class CancelLinkModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AccountAccessTokenResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AccountAccessTokenResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfirmLinkModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AccountAccessTokenResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AccountAccessTokenResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangePasswordModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AccountAccessTokenResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AccountAccessTokenResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class SetPasswordModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class VerifyCodeResponse(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        state: str = None,
    ):
        # 修改密码的临时授权码
        self.state = state

    def validate(self):
        self.validate_required(self.state, 'state')

    def to_map(self):
        result = dict()
        if self.state is not None:
            result['state'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('state') is not None:
            self.state = m.get('state')
        return self


class VerifyCodeModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: VerifyCodeResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = VerifyCodeResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAccessTokenByLinkInfoModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AccountAccessTokenResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AccountAccessTokenResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class Captcha(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        captcha: str = None,
        captcha_format: str = None,
        captcha_id: str = None,
    ):
        # 图片验证码，base64格式
        self.captcha = captcha
        # 图片格式
        self.captcha_format = captcha_format
        # 图片验证码ID
        self.captcha_id = captcha_id

    def validate(self):
        self.validate_required(self.captcha, 'captcha')
        self.validate_required(self.captcha_format, 'captcha_format')
        self.validate_required(self.captcha_id, 'captcha_id')

    def to_map(self):
        result = dict()
        if self.captcha is not None:
            result['captcha'] = self.captcha
        if self.captcha_format is not None:
            result['captcha_format'] = self.captcha_format
        if self.captcha_id is not None:
            result['captcha_id'] = self.captcha_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('captcha') is not None:
            self.captcha = m.get('captcha')
        if m.get('captcha_format') is not None:
            self.captcha_format = m.get('captcha_format')
        if m.get('captcha_id') is not None:
            self.captcha_id = m.get('captcha_id')
        return self


class GetCaptchaModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: Captcha = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = Captcha()
            self.body = temp_model.from_map(m['body'])
        return self


class LinkInfoResponse(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        authentication_type: str = None,
        created_at: int = None,
        domain_id: str = None,
        extra: str = None,
        identity: str = None,
        last_login_time: int = None,
        status: str = None,
        user_id: str = None,
    ):
        # 认证类型
        self.authentication_type = authentication_type
        # 创建时间
        self.created_at = created_at
        # Domain ID
        self.domain_id = domain_id
        # 额外的信息，比如type为mobile时，此字段为国家编号，不填默认86
        self.extra = extra
        # 唯一身份标识
        self.identity = identity
        # 最后登录时间
        self.last_login_time = last_login_time
        # 状态
        self.status = status
        # 用户ID
        self.user_id = user_id

    def validate(self):
        self.validate_required(self.authentication_type, 'authentication_type')
        self.validate_required(self.created_at, 'created_at')
        self.validate_required(self.domain_id, 'domain_id')
        self.validate_required(self.identity, 'identity')
        self.validate_required(self.last_login_time, 'last_login_time')
        self.validate_required(self.status, 'status')
        self.validate_required(self.user_id, 'user_id')

    def to_map(self):
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authentication_type') is not None:
            self.authentication_type = m.get('authentication_type')
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('extra') is not None:
            self.extra = m.get('extra')
        if m.get('identity') is not None:
            self.identity = m.get('identity')
        if m.get('last_login_time') is not None:
            self.last_login_time = m.get('last_login_time')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class GetLinkInfoModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: LinkInfoResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = LinkInfoResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class LinkInfoListResponse(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        items: List[LinkInfoResponse] = None,
    ):
        # items
        self.items = items

    def validate(self):
        self.validate_required(self.items, 'items')
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = LinkInfoResponse()
                self.items.append(temp_model.from_map(k))
        return self


class GetLinkInfoByUserIdModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: LinkInfoListResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = LinkInfoListResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPublicKeyResponse(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        app_id: str = None,
        key_pair_id: str = None,
        public_key: str = None,
    ):
        # App ID
        self.app_id = app_id
        self.key_pair_id = key_pair_id
        # RSA加密算法的公钥, PEM格式
        self.public_key = public_key

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.public_key, 'public_key')

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['app_id'] = self.app_id
        if self.key_pair_id is not None:
            result['key_pair_id'] = self.key_pair_id
        if self.public_key is not None:
            result['public_key'] = self.public_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('app_id') is not None:
            self.app_id = m.get('app_id')
        if m.get('key_pair_id') is not None:
            self.key_pair_id = m.get('key_pair_id')
        if m.get('public_key') is not None:
            self.public_key = m.get('public_key')
        return self


class GetPublicKeyModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPublicKeyResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetPublicKeyResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class LinkModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AccountAccessTokenResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AccountAccessTokenResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class MobileCheckExistResponse(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        is_exist: bool = None,
        phone_number: str = None,
        phone_region: str = None,
    ):
        # 当前手机号是否存在
        self.is_exist = is_exist
        # 待查询的手机号
        self.phone_number = phone_number
        # 国家编号，默认86，不需要填+号，直接填数字
        self.phone_region = phone_region

    def validate(self):
        self.validate_required(self.is_exist, 'is_exist')
        self.validate_required(self.phone_number, 'phone_number')

    def to_map(self):
        result = dict()
        if self.is_exist is not None:
            result['is_exist'] = self.is_exist
        if self.phone_number is not None:
            result['phone_number'] = self.phone_number
        if self.phone_region is not None:
            result['phone_region'] = self.phone_region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('is_exist') is not None:
            self.is_exist = m.get('is_exist')
        if m.get('phone_number') is not None:
            self.phone_number = m.get('phone_number')
        if m.get('phone_region') is not None:
            self.phone_region = m.get('phone_region')
        return self


class CheckExistModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: MobileCheckExistResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = MobileCheckExistResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class LoginModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AccountAccessTokenResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AccountAccessTokenResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class RegisterModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AccountAccessTokenResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AccountAccessTokenResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class MobileSendSmsCodeResponse(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        sms_code_id: str = None,
    ):
        # 短信验证码ID
        self.sms_code_id = sms_code_id

    def validate(self):
        self.validate_required(self.sms_code_id, 'sms_code_id')

    def to_map(self):
        result = dict()
        if self.sms_code_id is not None:
            result['sms_code_id'] = self.sms_code_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sms_code_id') is not None:
            self.sms_code_id = m.get('sms_code_id')
        return self


class MobileSendSmsCodeModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: MobileSendSmsCodeResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = MobileSendSmsCodeResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class AccountRevokeModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class AccountTokenModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AccountAccessTokenResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AccountAccessTokenResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class AccessTokenResponse(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        access_token: str = None,
        default_drive_id: str = None,
        expire_time: str = None,
        expires_in: int = None,
        refresh_token: str = None,
        role: str = None,
        token_type: str = None,
        user_id: str = None,
    ):
        # 用于调用业务接口的accessToken
        self.access_token = access_token
        # Default Drive ID
        self.default_drive_id = default_drive_id
        # accessToken过期时间，ISO时间
        self.expire_time = expire_time
        # accessToken过期时间，单位秒
        self.expires_in = expires_in
        # 用于刷新accessToken
        self.refresh_token = refresh_token
        # 当前用户角色
        self.role = role
        # accessToken类型，Bearer
        self.token_type = token_type
        # 当前用户ID
        self.user_id = user_id

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
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('access_token') is not None:
            self.access_token = m.get('access_token')
        if m.get('default_drive_id') is not None:
            self.default_drive_id = m.get('default_drive_id')
        if m.get('expire_time') is not None:
            self.expire_time = m.get('expire_time')
        if m.get('expires_in') is not None:
            self.expires_in = m.get('expires_in')
        if m.get('refresh_token') is not None:
            self.refresh_token = m.get('refresh_token')
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('token_type') is not None:
            self.token_type = m.get('token_type')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class AccountLinkRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        detail: str = None,
        extra: str = None,
        identity: str = None,
        status: str = None,
        type: str = None,
        user_id: str = None,
    ):
        self.headers = headers
        # 账号信息
        self.detail = detail
        # 额外的信息，比如type为mobile时，此字段为国家编号，不填默认86
        self.extra = extra
        # 唯一身份标识
        self.identity = identity
        # 状态
        self.status = status
        # 认证类型
        self.type = type
        # 绑定的user_id
        self.user_id = user_id

    def validate(self):
        self.validate_required(self.identity, 'identity')
        self.validate_required(self.type, 'type')
        self.validate_required(self.user_id, 'user_id')

    def to_map(self):
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('detail') is not None:
            self.detail = m.get('detail')
        if m.get('extra') is not None:
            self.extra = m.get('extra')
        if m.get('identity') is not None:
            self.identity = m.get('identity')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class AccountTokenRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        addition_data: dict = None,
        app_id: str = None,
        grant_type: str = None,
        refresh_token: str = None,
    ):
        self.headers = headers
        # addition_data
        self.addition_data = addition_data
        # App ID, 当前访问的App
        self.app_id = app_id
        # 只能填refresh_token
        self.grant_type = grant_type
        # refresh token, 登录时返回的
        self.refresh_token = refresh_token

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.grant_type, 'grant_type')
        self.validate_required(self.refresh_token, 'refresh_token')

    def to_map(self):
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('addition_data') is not None:
            self.addition_data = m.get('addition_data')
        if m.get('app_id') is not None:
            self.app_id = m.get('app_id')
        if m.get('grant_type') is not None:
            self.grant_type = m.get('grant_type')
        if m.get('refresh_token') is not None:
            self.refresh_token = m.get('refresh_token')
        return self


class AddStoreRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        base_path: str = None,
        bucket: str = None,
        domain_id: str = None,
        endpoint: str = None,
        ownership: str = None,
        role_arn: str = None,
        type: str = None,
    ):
        # 存储公共前缀
        self.base_path = base_path
        # bucket名称
        self.bucket = bucket
        # domain ID
        self.domain_id = domain_id
        # 存储访问地址
        self.endpoint = endpoint
        # 存储归属，system表示系统提供，custom表示使用自己的存储
        self.ownership = ownership
        # 访问Bucket的角色ARN
        self.role_arn = role_arn
        # 存储类型，当前只支持oss
        self.type = type

    def validate(self):
        self.validate_required(self.domain_id, 'domain_id')
        self.validate_required(self.endpoint, 'endpoint')
        self.validate_required(self.type, 'type')

    def to_map(self):
        result = dict()
        if self.base_path is not None:
            result['base_path'] = self.base_path
        if self.bucket is not None:
            result['bucket'] = self.bucket
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.ownership is not None:
            result['ownership'] = self.ownership
        if self.role_arn is not None:
            result['role_arn'] = self.role_arn
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('base_path') is not None:
            self.base_path = m.get('base_path')
        if m.get('bucket') is not None:
            self.bucket = m.get('bucket')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('ownership') is not None:
            self.ownership = m.get('ownership')
        if m.get('role_arn') is not None:
            self.role_arn = m.get('role_arn')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class AppAccessStrategy(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        effect: str = None,
        except_app_id_list: List[str] = None,
    ):
        self.effect = effect
        self.except_app_id_list = except_app_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.effect is not None:
            result['effect'] = self.effect
        if self.except_app_id_list is not None:
            result['except_app_id_list'] = self.except_app_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('effect') is not None:
            self.effect = m.get('effect')
        if m.get('except_app_id_list') is not None:
            self.except_app_id_list = m.get('except_app_id_list')
        return self


class LdapConfig(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        admin_dn: str = None,
        admin_password: str = None,
        base_dn: str = None,
        host: str = None,
        port: int = None,
        uid: str = None,
    ):
        self.admin_dn = admin_dn
        self.admin_password = admin_password
        self.base_dn = base_dn
        self.host = host
        self.port = port
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.admin_dn is not None:
            result['admin_dn'] = self.admin_dn
        if self.admin_password is not None:
            result['admin_password'] = self.admin_password
        if self.base_dn is not None:
            result['base_dn'] = self.base_dn
        if self.host is not None:
            result['host'] = self.host
        if self.port is not None:
            result['port'] = self.port
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('admin_dn') is not None:
            self.admin_dn = m.get('admin_dn')
        if m.get('admin_password') is not None:
            self.admin_password = m.get('admin_password')
        if m.get('base_dn') is not None:
            self.base_dn = m.get('base_dn')
        if m.get('host') is not None:
            self.host = m.get('host')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class AuthConfig(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        app_id: str = None,
        app_secret: str = None,
        callback_security: bool = None,
        enable: bool = None,
        endpoint: str = None,
        enterprise_id: str = None,
        ldap_config: LdapConfig = None,
        login_page_headers: dict = None,
        login_page_template: str = None,
        login_page_vars: dict = None,
        white_list_config: dict = None,
        white_list_enable: bool = None,
    ):
        self.app_id = app_id
        self.app_secret = app_secret
        self.callback_security = callback_security
        self.enable = enable
        self.endpoint = endpoint
        self.enterprise_id = enterprise_id
        self.ldap_config = ldap_config
        self.login_page_headers = login_page_headers
        self.login_page_template = login_page_template
        self.login_page_vars = login_page_vars
        self.white_list_config = white_list_config
        self.white_list_enable = white_list_enable

    def validate(self):
        if self.ldap_config:
            self.ldap_config.validate()

    def to_map(self):
        result = dict()
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
        if self.ldap_config is not None:
            result['ldap_config'] = self.ldap_config.to_map()
        if self.login_page_headers is not None:
            result['login_page_headers'] = self.login_page_headers
        if self.login_page_template is not None:
            result['login_page_template'] = self.login_page_template
        if self.login_page_vars is not None:
            result['login_page_vars'] = self.login_page_vars
        if self.white_list_config is not None:
            result['white_list_config'] = self.white_list_config
        if self.white_list_enable is not None:
            result['white_list_enable'] = self.white_list_enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('app_id') is not None:
            self.app_id = m.get('app_id')
        if m.get('app_secret') is not None:
            self.app_secret = m.get('app_secret')
        if m.get('callback_security') is not None:
            self.callback_security = m.get('callback_security')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('enterprise_id') is not None:
            self.enterprise_id = m.get('enterprise_id')
        if m.get('ldap_config') is not None:
            temp_model = LdapConfig()
            self.ldap_config = temp_model.from_map(m['ldap_config'])
        if m.get('login_page_headers') is not None:
            self.login_page_headers = m.get('login_page_headers')
        if m.get('login_page_template') is not None:
            self.login_page_template = m.get('login_page_template')
        if m.get('login_page_vars') is not None:
            self.login_page_vars = m.get('login_page_vars')
        if m.get('white_list_config') is not None:
            self.white_list_config = m.get('white_list_config')
        if m.get('white_list_enable') is not None:
            self.white_list_enable = m.get('white_list_enable')
        return self


class AuthorizeRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        client_id: str = None,
        login_type: str = None,
        redirect_uri: str = None,
        response_type: str = None,
        scope: List[str] = None,
        state: str = None,
        user_code: str = None,
    ):
        # Client ID, 此处填写创建App时返回的AppID
        self.client_id = client_id
        # 鉴权方式，目前支持ding,ram鉴权
        self.login_type = login_type
        # 回调地址, 此处填写创建App时填写的回调地址
        self.redirect_uri = redirect_uri
        # 返回类型, 只能填写code
        self.response_type = response_type
        # 申请的权限列表, 默认为所有权限
        self.scope = scope
        # 用户自定义字段，会在鉴权成功后的callback带回
        self.state = state
        # 内部使用
        self.user_code = user_code

    def validate(self):
        self.validate_required(self.client_id, 'client_id')
        self.validate_required(self.redirect_uri, 'redirect_uri')
        self.validate_required(self.response_type, 'response_type')

    def to_map(self):
        result = dict()
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
        if self.user_code is not None:
            result['UserCode'] = self.user_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientID') is not None:
            self.client_id = m.get('ClientID')
        if m.get('LoginType') is not None:
            self.login_type = m.get('LoginType')
        if m.get('RedirectUri') is not None:
            self.redirect_uri = m.get('RedirectUri')
        if m.get('ResponseType') is not None:
            self.response_type = m.get('ResponseType')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('UserCode') is not None:
            self.user_code = m.get('UserCode')
        return self


class CroppingBoundary(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        height: int = None,
        left: int = None,
        top: int = None,
        width: int = None,
    ):
        self.height = height
        self.left = left
        self.top = top
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.height is not None:
            result['height'] = self.height
        if self.left is not None:
            result['left'] = self.left
        if self.top is not None:
            result['top'] = self.top
        if self.width is not None:
            result['width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('height') is not None:
            self.height = m.get('height')
        if m.get('left') is not None:
            self.left = m.get('left')
        if m.get('top') is not None:
            self.top = m.get('top')
        if m.get('width') is not None:
            self.width = m.get('width')
        return self


class CroppingSuggestionItem(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        aspect_ratio: str = None,
        cropping_boundary: CroppingBoundary = None,
        score: float = None,
    ):
        self.aspect_ratio = aspect_ratio
        self.cropping_boundary = cropping_boundary
        self.score = score

    def validate(self):
        if self.cropping_boundary:
            self.cropping_boundary.validate()

    def to_map(self):
        result = dict()
        if self.aspect_ratio is not None:
            result['aspect_ratio'] = self.aspect_ratio
        if self.cropping_boundary is not None:
            result['cropping_boundary'] = self.cropping_boundary.to_map()
        if self.score is not None:
            result['score'] = self.score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aspect_ratio') is not None:
            self.aspect_ratio = m.get('aspect_ratio')
        if m.get('cropping_boundary') is not None:
            temp_model = CroppingBoundary()
            self.cropping_boundary = temp_model.from_map(m['cropping_boundary'])
        if m.get('score') is not None:
            self.score = m.get('score')
        return self


class ImageQuality(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        clarity: float = None,
        clarity_score: float = None,
        color: float = None,
        color_score: float = None,
        composition_score: float = None,
        contrast: float = None,
        contrast_score: float = None,
        exposure: float = None,
        exposure_score: float = None,
        overall_score: float = None,
    ):
        self.clarity = clarity
        self.clarity_score = clarity_score
        self.color = color
        self.color_score = color_score
        self.composition_score = composition_score
        self.contrast = contrast
        self.contrast_score = contrast_score
        self.exposure = exposure
        self.exposure_score = exposure_score
        self.overall_score = overall_score

    def validate(self):
        pass

    def to_map(self):
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clarity') is not None:
            self.clarity = m.get('clarity')
        if m.get('clarity_score') is not None:
            self.clarity_score = m.get('clarity_score')
        if m.get('color') is not None:
            self.color = m.get('color')
        if m.get('color_score') is not None:
            self.color_score = m.get('color_score')
        if m.get('composition_score') is not None:
            self.composition_score = m.get('composition_score')
        if m.get('contrast') is not None:
            self.contrast = m.get('contrast')
        if m.get('contrast_score') is not None:
            self.contrast_score = m.get('contrast_score')
        if m.get('exposure') is not None:
            self.exposure = m.get('exposure')
        if m.get('exposure_score') is not None:
            self.exposure_score = m.get('exposure_score')
        if m.get('overall_score') is not None:
            self.overall_score = m.get('overall_score')
        return self


class SystemTag(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        confidence: float = None,
        en_name: str = None,
        name: str = None,
        parent_en_name: str = None,
        parent_name: str = None,
        selected: bool = None,
        source: str = None,
        tag_level: int = None,
    ):
        self.confidence = confidence
        self.en_name = en_name
        self.name = name
        self.parent_en_name = parent_en_name
        self.parent_name = parent_name
        self.selected = selected
        self.source = source
        self.tag_level = tag_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
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
        if self.source is not None:
            result['source'] = self.source
        if self.tag_level is not None:
            result['tag_level'] = self.tag_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('confidence') is not None:
            self.confidence = m.get('confidence')
        if m.get('en_name') is not None:
            self.en_name = m.get('en_name')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parent_en_name') is not None:
            self.parent_en_name = m.get('parent_en_name')
        if m.get('parent_name') is not None:
            self.parent_name = m.get('parent_name')
        if m.get('selected') is not None:
            self.selected = m.get('selected')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('tag_level') is not None:
            self.tag_level = m.get('tag_level')
        return self


class ImageMediaResponse(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        address_line: str = None,
        city: str = None,
        country: str = None,
        cropping_suggestion: List[CroppingSuggestionItem] = None,
        district: str = None,
        exif: str = None,
        faces: str = None,
        height: int = None,
        image_quality: ImageQuality = None,
        image_tags: List[SystemTag] = None,
        location: str = None,
        province: str = None,
        story_image_score: float = None,
        time: str = None,
        township: str = None,
        width: int = None,
    ):
        # address_line
        self.address_line = address_line
        # city
        self.city = city
        # country
        self.country = country
        # cropping_suggestion
        self.cropping_suggestion = cropping_suggestion
        # district
        self.district = district
        # exif json string
        self.exif = exif
        # faces json string
        self.faces = faces
        # height
        self.height = height
        self.image_quality = image_quality
        # system_tags
        self.image_tags = image_tags
        # location
        self.location = location
        # province
        self.province = province
        # story_image_score
        self.story_image_score = story_image_score
        # time
        self.time = time
        # township
        self.township = township
        # width
        self.width = width

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
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address_line') is not None:
            self.address_line = m.get('address_line')
        if m.get('city') is not None:
            self.city = m.get('city')
        if m.get('country') is not None:
            self.country = m.get('country')
        self.cropping_suggestion = []
        if m.get('cropping_suggestion') is not None:
            for k in m.get('cropping_suggestion'):
                temp_model = CroppingSuggestionItem()
                self.cropping_suggestion.append(temp_model.from_map(k))
        if m.get('district') is not None:
            self.district = m.get('district')
        if m.get('exif') is not None:
            self.exif = m.get('exif')
        if m.get('faces') is not None:
            self.faces = m.get('faces')
        if m.get('height') is not None:
            self.height = m.get('height')
        if m.get('image_quality') is not None:
            temp_model = ImageQuality()
            self.image_quality = temp_model.from_map(m['image_quality'])
        self.image_tags = []
        if m.get('image_tags') is not None:
            for k in m.get('image_tags'):
                temp_model = SystemTag()
                self.image_tags.append(temp_model.from_map(k))
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('story_image_score') is not None:
            self.story_image_score = m.get('story_image_score')
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('township') is not None:
            self.township = m.get('township')
        if m.get('width') is not None:
            self.width = m.get('width')
        return self


class VideoMediaAudioStream(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        bit_rate: str = None,
        channel_layout: str = None,
        channels: int = None,
        code_name: str = None,
        duration: str = None,
        sample_rate: str = None,
    ):
        # bit_rate 音频比特率 单位：bps
        self.bit_rate = bit_rate
        # channel_layout 声道布局
        self.channel_layout = channel_layout
        # channels 音频数/声道数
        self.channels = channels
        # code_name 音频编码模式
        self.code_name = code_name
        # duration 单位 秒
        self.duration = duration
        # sample_rate 音频采样率
        self.sample_rate = sample_rate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bit_rate') is not None:
            self.bit_rate = m.get('bit_rate')
        if m.get('channel_layout') is not None:
            self.channel_layout = m.get('channel_layout')
        if m.get('channels') is not None:
            self.channels = m.get('channels')
        if m.get('code_name') is not None:
            self.code_name = m.get('code_name')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('sample_rate') is not None:
            self.sample_rate = m.get('sample_rate')
        return self


class VideoMediaVideoStream(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        bitrate: str = None,
        clarity: str = None,
        code_name: str = None,
        duration: str = None,
        fps: str = None,
        rotate: str = None,
    ):
        # bitrate 视频比特率 单位：bps
        self.bitrate = bitrate
        # clarity 清晰度（扫描）
        self.clarity = clarity
        # code_name 视频编码模式
        self.code_name = code_name
        # duration 单位 秒
        self.duration = duration
        # fps 视频平均帧率
        self.fps = fps
        # rotate 视频横屏 竖屏
        self.rotate = rotate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
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
        if self.rotate is not None:
            result['rotate'] = self.rotate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bitrate') is not None:
            self.bitrate = m.get('bitrate')
        if m.get('clarity') is not None:
            self.clarity = m.get('clarity')
        if m.get('code_name') is not None:
            self.code_name = m.get('code_name')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('fps') is not None:
            self.fps = m.get('fps')
        if m.get('rotate') is not None:
            self.rotate = m.get('rotate')
        return self


class VideoMediaResponse(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        address_line: str = None,
        city: str = None,
        country: str = None,
        district: str = None,
        duration: str = None,
        height: int = None,
        image_tags: List[SystemTag] = None,
        location: str = None,
        province: str = None,
        time: str = None,
        township: str = None,
        video_media_audio_stream: List[VideoMediaAudioStream] = None,
        video_media_video_stream: List[VideoMediaVideoStream] = None,
        width: int = None,
    ):
        # address_line
        self.address_line = address_line
        # city
        self.city = city
        # country
        self.country = country
        # district
        self.district = district
        # duration 单位 秒
        self.duration = duration
        # height
        self.height = height
        # system_tags
        self.image_tags = image_tags
        # location
        self.location = location
        # province
        self.province = province
        # time
        self.time = time
        # township
        self.township = township
        self.video_media_audio_stream = video_media_audio_stream
        self.video_media_video_stream = video_media_video_stream
        # width
        self.width = width

    def validate(self):
        if self.image_tags:
            for k in self.image_tags:
                if k:
                    k.validate()
        if self.video_media_audio_stream:
            for k in self.video_media_audio_stream:
                if k:
                    k.validate()
        if self.video_media_video_stream:
            for k in self.video_media_video_stream:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
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
        result['image_tags'] = []
        if self.image_tags is not None:
            for k in self.image_tags:
                result['image_tags'].append(k.to_map() if k else None)
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address_line') is not None:
            self.address_line = m.get('address_line')
        if m.get('city') is not None:
            self.city = m.get('city')
        if m.get('country') is not None:
            self.country = m.get('country')
        if m.get('district') is not None:
            self.district = m.get('district')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('height') is not None:
            self.height = m.get('height')
        self.image_tags = []
        if m.get('image_tags') is not None:
            for k in m.get('image_tags'):
                temp_model = SystemTag()
                self.image_tags.append(temp_model.from_map(k))
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('township') is not None:
            self.township = m.get('township')
        self.video_media_audio_stream = []
        if m.get('video_media_audio_stream') is not None:
            for k in m.get('video_media_audio_stream'):
                temp_model = VideoMediaAudioStream()
                self.video_media_audio_stream.append(temp_model.from_map(k))
        self.video_media_video_stream = []
        if m.get('video_media_video_stream') is not None:
            for k in m.get('video_media_video_stream'):
                temp_model = VideoMediaVideoStream()
                self.video_media_video_stream.append(temp_model.from_map(k))
        if m.get('width') is not None:
            self.width = m.get('width')
        return self


class VideoPreviewAudioMeta(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        bitrate: float = None,
        channels: int = None,
        duration: float = None,
        sample_rate: float = None,
    ):
        # bitrate
        self.bitrate = bitrate
        # channels
        self.channels = channels
        # duration
        self.duration = duration
        # sample_rate
        self.sample_rate = sample_rate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.bitrate is not None:
            result['bitrate'] = self.bitrate
        if self.channels is not None:
            result['channels'] = self.channels
        if self.duration is not None:
            result['duration'] = self.duration
        if self.sample_rate is not None:
            result['sample_rate'] = self.sample_rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bitrate') is not None:
            self.bitrate = m.get('bitrate')
        if m.get('channels') is not None:
            self.channels = m.get('channels')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('sample_rate') is not None:
            self.sample_rate = m.get('sample_rate')
        return self


class VideoPreviewAudioMusicMeta(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        album: str = None,
        artist: str = None,
        cover_url: str = None,
        title: str = None,
    ):
        # album
        self.album = album
        # artist
        self.artist = artist
        # cover_url
        self.cover_url = cover_url
        # title
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.album is not None:
            result['album'] = self.album
        if self.artist is not None:
            result['artist'] = self.artist
        if self.cover_url is not None:
            result['cover_url'] = self.cover_url
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('album') is not None:
            self.album = m.get('album')
        if m.get('artist') is not None:
            self.artist = m.get('artist')
        if m.get('cover_url') is not None:
            self.cover_url = m.get('cover_url')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class VideoPreviewTranscode(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        status: str = None,
        template_id: str = None,
    ):
        # status
        self.status = status
        # template_id
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['status'] = self.status
        if self.template_id is not None:
            result['template_id'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('template_id') is not None:
            self.template_id = m.get('template_id')
        return self


class VideoPreviewSprite(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        col: int = None,
        count: int = None,
        frame_count: int = None,
        frame_height: int = None,
        frame_width: int = None,
        row: int = None,
        status: str = None,
    ):
        # col
        self.col = col
        # count
        self.count = count
        # frame_count
        self.frame_count = frame_count
        # frame_height
        self.frame_height = frame_height
        # frame_width
        self.frame_width = frame_width
        # row
        self.row = row
        # status
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('col') is not None:
            self.col = m.get('col')
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('frame_count') is not None:
            self.frame_count = m.get('frame_count')
        if m.get('frame_height') is not None:
            self.frame_height = m.get('frame_height')
        if m.get('frame_width') is not None:
            self.frame_width = m.get('frame_width')
        if m.get('row') is not None:
            self.row = m.get('row')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class VideoPreviewResponse(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        audio_channels: int = None,
        audio_format: str = None,
        audio_meta: VideoPreviewAudioMeta = None,
        audio_music_meta: VideoPreviewAudioMusicMeta = None,
        audio_sample_rate: str = None,
        audio_template_list: List[VideoPreviewTranscode] = None,
        bitrate: str = None,
        duration: str = None,
        frame_rate: str = None,
        height: int = None,
        sprite_info: VideoPreviewSprite = None,
        template_list: List[VideoPreviewTranscode] = None,
        thumbnail: str = None,
        video_format: str = None,
        width: int = None,
    ):
        # audio_channels
        self.audio_channels = audio_channels
        # audio_format
        self.audio_format = audio_format
        self.audio_meta = audio_meta
        self.audio_music_meta = audio_music_meta
        # audio_sample_rate
        self.audio_sample_rate = audio_sample_rate
        # audio_template_list
        self.audio_template_list = audio_template_list
        # bitrate
        self.bitrate = bitrate
        # duration
        self.duration = duration
        # frame_rate
        self.frame_rate = frame_rate
        # height
        self.height = height
        self.sprite_info = sprite_info
        # template_list
        self.template_list = template_list
        # thumbnail
        self.thumbnail = thumbnail
        # video_format
        self.video_format = video_format
        # width
        self.width = width

    def validate(self):
        if self.audio_meta:
            self.audio_meta.validate()
        if self.audio_music_meta:
            self.audio_music_meta.validate()
        if self.audio_template_list:
            for k in self.audio_template_list:
                if k:
                    k.validate()
        if self.sprite_info:
            self.sprite_info.validate()
        if self.template_list:
            for k in self.template_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.audio_channels is not None:
            result['audio_channels'] = self.audio_channels
        if self.audio_format is not None:
            result['audio_format'] = self.audio_format
        if self.audio_meta is not None:
            result['audio_meta'] = self.audio_meta.to_map()
        if self.audio_music_meta is not None:
            result['audio_music_meta'] = self.audio_music_meta.to_map()
        if self.audio_sample_rate is not None:
            result['audio_sample_rate'] = self.audio_sample_rate
        result['audio_template_list'] = []
        if self.audio_template_list is not None:
            for k in self.audio_template_list:
                result['audio_template_list'].append(k.to_map() if k else None)
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('audio_channels') is not None:
            self.audio_channels = m.get('audio_channels')
        if m.get('audio_format') is not None:
            self.audio_format = m.get('audio_format')
        if m.get('audio_meta') is not None:
            temp_model = VideoPreviewAudioMeta()
            self.audio_meta = temp_model.from_map(m['audio_meta'])
        if m.get('audio_music_meta') is not None:
            temp_model = VideoPreviewAudioMusicMeta()
            self.audio_music_meta = temp_model.from_map(m['audio_music_meta'])
        if m.get('audio_sample_rate') is not None:
            self.audio_sample_rate = m.get('audio_sample_rate')
        self.audio_template_list = []
        if m.get('audio_template_list') is not None:
            for k in m.get('audio_template_list'):
                temp_model = VideoPreviewTranscode()
                self.audio_template_list.append(temp_model.from_map(k))
        if m.get('bitrate') is not None:
            self.bitrate = m.get('bitrate')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('frame_rate') is not None:
            self.frame_rate = m.get('frame_rate')
        if m.get('height') is not None:
            self.height = m.get('height')
        if m.get('sprite_info') is not None:
            temp_model = VideoPreviewSprite()
            self.sprite_info = temp_model.from_map(m['sprite_info'])
        self.template_list = []
        if m.get('template_list') is not None:
            for k in m.get('template_list'):
                temp_model = VideoPreviewTranscode()
                self.template_list.append(temp_model.from_map(k))
        if m.get('thumbnail') is not None:
            self.thumbnail = m.get('thumbnail')
        if m.get('video_format') is not None:
            self.video_format = m.get('video_format')
        if m.get('width') is not None:
            self.width = m.get('width')
        return self


class BaseCCPFileResponse(TeaModel):
    """
    Base file response
    """
    def __init__(
        self,
        category: str = None,
        characteristic_hash: str = None,
        content_hash: str = None,
        content_hash_name: str = None,
        content_type: str = None,
        crc_64hash: str = None,
        created_at: str = None,
        description: str = None,
        domain_id: str = None,
        download_url: str = None,
        drive_id: str = None,
        encrypt_mode: str = None,
        file_extension: str = None,
        file_id: str = None,
        hidden: bool = None,
        image_media_metadata: ImageMediaResponse = None,
        labels: List[str] = None,
        meta: str = None,
        name: str = None,
        parent_file_id: str = None,
        punish_flag: int = None,
        share_id: str = None,
        size: int = None,
        starred: bool = None,
        status: str = None,
        streams_info: dict = None,
        thumbnail: str = None,
        trashed_at: str = None,
        type: str = None,
        updated_at: str = None,
        upload_id: str = None,
        url: str = None,
        user_meta: str = None,
        video_media_metadata: VideoMediaResponse = None,
        video_preview_metadata: VideoPreviewResponse = None,
    ):
        # category
        self.category = category
        # CharacteristicHash
        self.characteristic_hash = characteristic_hash
        # Content Hash
        self.content_hash = content_hash
        # content_hash_name
        self.content_hash_name = content_hash_name
        # content_type
        self.content_type = content_type
        # crc64_hash
        self.crc_64hash = crc_64hash
        # created_at
        self.created_at = created_at
        # description
        self.description = description
        # DomainID
        self.domain_id = domain_id
        # download_url
        self.download_url = download_url
        # drive_id
        self.drive_id = drive_id
        # encrypt_mode
        self.encrypt_mode = encrypt_mode
        # file_extension
        self.file_extension = file_extension
        # file_id
        self.file_id = file_id
        # Hidden
        # type: boolean
        self.hidden = hidden
        self.image_media_metadata = image_media_metadata
        # labels
        self.labels = labels
        self.meta = meta
        # name
        self.name = name
        # parent_file_id
        self.parent_file_id = parent_file_id
        self.punish_flag = punish_flag
        self.share_id = share_id
        # Size
        self.size = size
        # starred
        # type: boolean
        self.starred = starred
        # status
        self.status = status
        # @Deprecated streams url info
        self.streams_info = streams_info
        # thumbnail
        self.thumbnail = thumbnail
        # trashed_at
        self.trashed_at = trashed_at
        # type
        self.type = type
        # updated_at
        self.updated_at = updated_at
        # upload_id
        self.upload_id = upload_id
        # url
        self.url = url
        # user_meta
        self.user_meta = user_meta
        self.video_media_metadata = video_media_metadata
        self.video_preview_metadata = video_preview_metadata

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
        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.characteristic_hash is not None:
            result['characteristic_hash'] = self.characteristic_hash
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
        if self.share_id is not None:
            result['share_id'] = self.share_id
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('characteristic_hash') is not None:
            self.characteristic_hash = m.get('characteristic_hash')
        if m.get('content_hash') is not None:
            self.content_hash = m.get('content_hash')
        if m.get('content_hash_name') is not None:
            self.content_hash_name = m.get('content_hash_name')
        if m.get('content_type') is not None:
            self.content_type = m.get('content_type')
        if m.get('crc64_hash') is not None:
            self.crc_64hash = m.get('crc64_hash')
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('download_url') is not None:
            self.download_url = m.get('download_url')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('encrypt_mode') is not None:
            self.encrypt_mode = m.get('encrypt_mode')
        if m.get('file_extension') is not None:
            self.file_extension = m.get('file_extension')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('hidden') is not None:
            self.hidden = m.get('hidden')
        if m.get('image_media_metadata') is not None:
            temp_model = ImageMediaResponse()
            self.image_media_metadata = temp_model.from_map(m['image_media_metadata'])
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('meta') is not None:
            self.meta = m.get('meta')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parent_file_id') is not None:
            self.parent_file_id = m.get('parent_file_id')
        if m.get('punish_flag') is not None:
            self.punish_flag = m.get('punish_flag')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('starred') is not None:
            self.starred = m.get('starred')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('streams_info') is not None:
            self.streams_info = m.get('streams_info')
        if m.get('thumbnail') is not None:
            self.thumbnail = m.get('thumbnail')
        if m.get('trashed_at') is not None:
            self.trashed_at = m.get('trashed_at')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        if m.get('upload_id') is not None:
            self.upload_id = m.get('upload_id')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('user_meta') is not None:
            self.user_meta = m.get('user_meta')
        if m.get('video_media_metadata') is not None:
            temp_model = VideoMediaResponse()
            self.video_media_metadata = temp_model.from_map(m['video_media_metadata'])
        if m.get('video_preview_metadata') is not None:
            temp_model = VideoPreviewResponse()
            self.video_preview_metadata = temp_model.from_map(m['video_preview_metadata'])
        return self


class BaseDriveResponse(TeaModel):
    """
    Base drive response
    """
    def __init__(
        self,
        creator: str = None,
        description: str = None,
        domain_id: str = None,
        drive_id: str = None,
        drive_name: str = None,
        drive_type: str = None,
        encrypt_data_access: bool = None,
        encrypt_mode: str = None,
        owner: str = None,
        owner_type: str = None,
        relative_path: str = None,
        status: str = None,
        store_id: str = None,
        total_size: int = None,
        used_size: int = None,
    ):
        # Drive 创建者
        self.creator = creator
        # Drive 备注信息
        self.description = description
        # Domain ID
        self.domain_id = domain_id
        # Drive ID
        self.drive_id = drive_id
        # Drive 名称
        self.drive_name = drive_name
        # Drive 类型
        self.drive_type = drive_type
        self.encrypt_data_access = encrypt_data_access
        self.encrypt_mode = encrypt_mode
        # Drive 所有者
        self.owner = owner
        # Drive 所有者类型
        self.owner_type = owner_type
        # Drive存储基于store的相对路径，domain的PathType为OSSPath时返回
        self.relative_path = relative_path
        # Drive 状态
        self.status = status
        # 存储 ID, domain的PathType为OSSPath时返回
        self.store_id = store_id
        # Drive 空间总量
        self.total_size = total_size
        # Drive 空间已使用量
        self.used_size = used_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
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
        if self.owner_type is not None:
            result['owner_type'] = self.owner_type
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('drive_name') is not None:
            self.drive_name = m.get('drive_name')
        if m.get('drive_type') is not None:
            self.drive_type = m.get('drive_type')
        if m.get('encrypt_data_access') is not None:
            self.encrypt_data_access = m.get('encrypt_data_access')
        if m.get('encrypt_mode') is not None:
            self.encrypt_mode = m.get('encrypt_mode')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('owner_type') is not None:
            self.owner_type = m.get('owner_type')
        if m.get('relative_path') is not None:
            self.relative_path = m.get('relative_path')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('store_id') is not None:
            self.store_id = m.get('store_id')
        if m.get('total_size') is not None:
            self.total_size = m.get('total_size')
        if m.get('used_size') is not None:
            self.used_size = m.get('used_size')
        return self


class BaseFileAnonymousResponse(TeaModel):
    """
    list_file_by_anonymous base response
    """
    def __init__(
        self,
        file_id: str = None,
        name: str = None,
        size: int = None,
        thumbnail: str = None,
        type: str = None,
        updated_at: str = None,
    ):
        # file_id
        self.file_id = file_id
        # name
        self.name = name
        # size, type=file时才有效
        self.size = size
        # thumbnail
        self.thumbnail = thumbnail
        # type
        self.type = type
        # updated_at
        self.updated_at = updated_at

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
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('thumbnail') is not None:
            self.thumbnail = m.get('thumbnail')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        return self


class BaseHostingFileResponse(TeaModel):
    """
    Base file response
    """
    def __init__(
        self,
        content_hash: str = None,
        content_hash_name: str = None,
        content_type: str = None,
        crc_64hash: str = None,
        created_at: str = None,
        description: str = None,
        domain_id: str = None,
        download_url: str = None,
        drive_id: str = None,
        file_extension: str = None,
        file_path: str = None,
        name: str = None,
        parent_file_path: str = None,
        share_id: str = None,
        size: int = None,
        status: str = None,
        thumbnail: str = None,
        trashed_at: str = None,
        type: str = None,
        updated_at: str = None,
        upload_id: str = None,
        url: str = None,
    ):
        # Content Hash
        self.content_hash = content_hash
        # content_hash_name
        self.content_hash_name = content_hash_name
        # content_type
        self.content_type = content_type
        # crc64_hash
        self.crc_64hash = crc_64hash
        # created_at
        self.created_at = created_at
        # description
        self.description = description
        # domain_id
        self.domain_id = domain_id
        # download_url
        self.download_url = download_url
        # drive_id
        self.drive_id = drive_id
        # file_extension
        self.file_extension = file_extension
        # file_path
        self.file_path = file_path
        # name
        self.name = name
        # parent_file_id
        self.parent_file_path = parent_file_path
        # share_id
        self.share_id = share_id
        # Size
        self.size = size
        # status
        self.status = status
        # thumbnail
        self.thumbnail = thumbnail
        # trashed_at
        self.trashed_at = trashed_at
        # type
        self.type = type
        # updated_at
        self.updated_at = updated_at
        # upload_id
        self.upload_id = upload_id
        # url
        self.url = url

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
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content_hash') is not None:
            self.content_hash = m.get('content_hash')
        if m.get('content_hash_name') is not None:
            self.content_hash_name = m.get('content_hash_name')
        if m.get('content_type') is not None:
            self.content_type = m.get('content_type')
        if m.get('crc64_hash') is not None:
            self.crc_64hash = m.get('crc64_hash')
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('download_url') is not None:
            self.download_url = m.get('download_url')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_extension') is not None:
            self.file_extension = m.get('file_extension')
        if m.get('file_path') is not None:
            self.file_path = m.get('file_path')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parent_file_path') is not None:
            self.parent_file_path = m.get('parent_file_path')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('thumbnail') is not None:
            self.thumbnail = m.get('thumbnail')
        if m.get('trashed_at') is not None:
            self.trashed_at = m.get('trashed_at')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        if m.get('upload_id') is not None:
            self.upload_id = m.get('upload_id')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class BaseMediaResponse(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        address_line: str = None,
        city: str = None,
        country: str = None,
        district: str = None,
        height: int = None,
        image_tags: List[SystemTag] = None,
        location: str = None,
        province: str = None,
        time: str = None,
        township: str = None,
        width: int = None,
    ):
        # address_line
        self.address_line = address_line
        # city
        self.city = city
        # country
        self.country = country
        # district
        self.district = district
        # height
        self.height = height
        # system_tags
        self.image_tags = image_tags
        # location
        self.location = location
        # province
        self.province = province
        # time
        self.time = time
        # township
        self.township = township
        # width
        self.width = width

    def validate(self):
        if self.image_tags:
            for k in self.image_tags:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
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
        result['image_tags'] = []
        if self.image_tags is not None:
            for k in self.image_tags:
                result['image_tags'].append(k.to_map() if k else None)
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address_line') is not None:
            self.address_line = m.get('address_line')
        if m.get('city') is not None:
            self.city = m.get('city')
        if m.get('country') is not None:
            self.country = m.get('country')
        if m.get('district') is not None:
            self.district = m.get('district')
        if m.get('height') is not None:
            self.height = m.get('height')
        self.image_tags = []
        if m.get('image_tags') is not None:
            for k in m.get('image_tags'):
                temp_model = SystemTag()
                self.image_tags.append(temp_model.from_map(k))
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('township') is not None:
            self.township = m.get('township')
        if m.get('width') is not None:
            self.width = m.get('width')
        return self


class BaseShareLinkResponse(TeaModel):
    """
    list_share_link response
    """
    def __init__(
        self,
        created_at: str = None,
        creator: str = None,
        description: str = None,
        download_count: int = None,
        drive_id: str = None,
        expiration: str = None,
        expired: bool = None,
        file_id: str = None,
        file_id_list: List[str] = None,
        file_path_list: List[str] = None,
        preview_count: int = None,
        save_count: int = None,
        share_id: str = None,
        share_msg: str = None,
        share_name: str = None,
        share_policy: str = None,
        share_pwd: str = None,
        share_url: str = None,
        updated_at: str = None,
    ):
        # created_at
        self.created_at = created_at
        # creator
        self.creator = creator
        # description
        self.description = description
        # 下载次数
        self.download_count = download_count
        # drive_id
        self.drive_id = drive_id
        # expiration
        self.expiration = expiration
        # expired
        self.expired = expired
        # file_id
        self.file_id = file_id
        # file_id_list
        self.file_id_list = file_id_list
        # file_id_list
        self.file_path_list = file_path_list
        # preview_count
        self.preview_count = preview_count
        # 转存次数
        self.save_count = save_count
        # share_id
        self.share_id = share_id
        # share_msg
        self.share_msg = share_msg
        # share_name
        self.share_name = share_name
        # share_policy
        self.share_policy = share_policy
        # share_pwd
        self.share_pwd = share_pwd
        # share_url
        self.share_url = share_url
        # updated_at
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.creator is not None:
            result['creator'] = self.creator
        if self.description is not None:
            result['description'] = self.description
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
        if self.file_id_list is not None:
            result['file_id_list'] = self.file_id_list
        if self.file_path_list is not None:
            result['file_path_list'] = self.file_path_list
        if self.preview_count is not None:
            result['preview_count'] = self.preview_count
        if self.save_count is not None:
            result['save_count'] = self.save_count
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.share_msg is not None:
            result['share_msg'] = self.share_msg
        if self.share_name is not None:
            result['share_name'] = self.share_name
        if self.share_policy is not None:
            result['share_policy'] = self.share_policy
        if self.share_pwd is not None:
            result['share_pwd'] = self.share_pwd
        if self.share_url is not None:
            result['share_url'] = self.share_url
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('download_count') is not None:
            self.download_count = m.get('download_count')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('expiration') is not None:
            self.expiration = m.get('expiration')
        if m.get('expired') is not None:
            self.expired = m.get('expired')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('file_id_list') is not None:
            self.file_id_list = m.get('file_id_list')
        if m.get('file_path_list') is not None:
            self.file_path_list = m.get('file_path_list')
        if m.get('preview_count') is not None:
            self.preview_count = m.get('preview_count')
        if m.get('save_count') is not None:
            self.save_count = m.get('save_count')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('share_msg') is not None:
            self.share_msg = m.get('share_msg')
        if m.get('share_name') is not None:
            self.share_name = m.get('share_name')
        if m.get('share_policy') is not None:
            self.share_policy = m.get('share_policy')
        if m.get('share_pwd') is not None:
            self.share_pwd = m.get('share_pwd')
        if m.get('share_url') is not None:
            self.share_url = m.get('share_url')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        return self


class SharePermissionPolicy(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        file_id: str = None,
        file_path: str = None,
        permission_inheritable: bool = None,
        permission_list: List[str] = None,
        permission_type: str = None,
    ):
        self.file_id = file_id
        self.file_path = file_path
        self.permission_inheritable = permission_inheritable
        self.permission_list = permission_list
        self.permission_type = permission_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.file_path is not None:
            result['file_path'] = self.file_path
        if self.permission_inheritable is not None:
            result['permission_inheritable'] = self.permission_inheritable
        if self.permission_list is not None:
            result['permission_list'] = self.permission_list
        if self.permission_type is not None:
            result['permission_type'] = self.permission_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('file_path') is not None:
            self.file_path = m.get('file_path')
        if m.get('permission_inheritable') is not None:
            self.permission_inheritable = m.get('permission_inheritable')
        if m.get('permission_list') is not None:
            self.permission_list = m.get('permission_list')
        if m.get('permission_type') is not None:
            self.permission_type = m.get('permission_type')
        return self


class BaseShareResponse(TeaModel):
    """
    List share response
    """
    def __init__(
        self,
        created_at: str = None,
        creator: str = None,
        description: str = None,
        domain_id: str = None,
        drive_id: str = None,
        expiration: str = None,
        expired: bool = None,
        owner: str = None,
        owner_type: str = None,
        permissions: List[str] = None,
        share_file_id: str = None,
        share_file_path: str = None,
        share_id: str = None,
        share_name: str = None,
        share_policy: List[SharePermissionPolicy] = None,
        status: str = None,
        updated_at: str = None,
    ):
        # created_at
        self.created_at = created_at
        # creator
        self.creator = creator
        # description
        self.description = description
        # domain_id
        self.domain_id = domain_id
        # drive_id
        self.drive_id = drive_id
        # expiration
        self.expiration = expiration
        # expired
        self.expired = expired
        # owner
        self.owner = owner
        # owner
        self.owner_type = owner_type
        # permissions
        self.permissions = permissions
        # share_file_id
        self.share_file_id = share_file_id
        # share_path
        self.share_file_path = share_file_path
        # share_id
        self.share_id = share_id
        # share_name
        self.share_name = share_name
        self.share_policy = share_policy
        # status
        self.status = status
        # updated_at
        self.updated_at = updated_at

    def validate(self):
        if self.share_policy:
            for k in self.share_policy:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
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
        if self.owner_type is not None:
            result['owner_type'] = self.owner_type
        if self.permissions is not None:
            result['permissions'] = self.permissions
        if self.share_file_id is not None:
            result['share_file_id'] = self.share_file_id
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('expiration') is not None:
            self.expiration = m.get('expiration')
        if m.get('expired') is not None:
            self.expired = m.get('expired')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('owner_type') is not None:
            self.owner_type = m.get('owner_type')
        if m.get('permissions') is not None:
            self.permissions = m.get('permissions')
        if m.get('share_file_id') is not None:
            self.share_file_id = m.get('share_file_id')
        if m.get('share_file_path') is not None:
            self.share_file_path = m.get('share_file_path')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('share_name') is not None:
            self.share_name = m.get('share_name')
        self.share_policy = []
        if m.get('share_policy') is not None:
            for k in m.get('share_policy'):
                temp_model = SharePermissionPolicy()
                self.share_policy.append(temp_model.from_map(k))
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        return self


class BatchSubResponse(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        body: dict = None,
        id: str = None,
        status: int = None,
    ):
        # body 子请求的返回结果，可参考对于子请求文档 json 字符串
        self.body = body
        # id 请求带过来的id, 可以跟 request 进行关联
        self.id = id
        # status 子请求的返回状态码，可参考对于子请求文档
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.body is not None:
            result['body'] = self.body
        if self.id is not None:
            result['id'] = self.id
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class BatchResponse(TeaModel):
    """
    batch operation response
    """
    def __init__(
        self,
        responses: List[BatchSubResponse] = None,
    ):
        # responses 返回结果合集
        self.responses = responses

    def validate(self):
        if self.responses:
            for k in self.responses:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['responses'] = []
        if self.responses is not None:
            for k in self.responses:
                result['responses'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.responses = []
        if m.get('responses') is not None:
            for k in m.get('responses'):
                temp_model = BatchSubResponse()
                self.responses.append(temp_model.from_map(k))
        return self


class CancelLinkRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        temporary_token: str = None,
    ):
        self.headers = headers
        # 待绑定的临时token，此token只能访问绑定、取消绑定接口
        self.temporary_token = temporary_token

    def validate(self):
        self.validate_required(self.temporary_token, 'temporary_token')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.temporary_token is not None:
            result['temporary_token'] = self.temporary_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('temporary_token') is not None:
            self.temporary_token = m.get('temporary_token')
        return self


class CertInfo(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        cert_id: str = None,
        cert_body: str = None,
        cert_name: str = None,
        cert_privatekey: str = None,
    ):
        self.cert_id = cert_id
        # cert body
        self.cert_body = cert_body
        # cert name
        self.cert_name = cert_name
        # cert privatekey
        self.cert_privatekey = cert_privatekey

    def validate(self):
        self.validate_required(self.cert_body, 'cert_body')
        self.validate_required(self.cert_name, 'cert_name')
        self.validate_required(self.cert_privatekey, 'cert_privatekey')

    def to_map(self):
        result = dict()
        if self.cert_id is not None:
            result['CertID'] = self.cert_id
        if self.cert_body is not None:
            result['cert_body'] = self.cert_body
        if self.cert_name is not None:
            result['cert_name'] = self.cert_name
        if self.cert_privatekey is not None:
            result['cert_privatekey'] = self.cert_privatekey
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertID') is not None:
            self.cert_id = m.get('CertID')
        if m.get('cert_body') is not None:
            self.cert_body = m.get('cert_body')
        if m.get('cert_name') is not None:
            self.cert_name = m.get('cert_name')
        if m.get('cert_privatekey') is not None:
            self.cert_privatekey = m.get('cert_privatekey')
        return self


class CompleteFileResponse(TeaModel):
    """
    complete file response
    """
    def __init__(
        self,
        category: str = None,
        characteristic_hash: str = None,
        content_hash: str = None,
        content_hash_name: str = None,
        content_type: str = None,
        crc_64hash: str = None,
        created_at: str = None,
        description: str = None,
        domain_id: str = None,
        download_url: str = None,
        drive_id: str = None,
        encrypt_mode: str = None,
        file_extension: str = None,
        file_id: str = None,
        hidden: bool = None,
        image_media_metadata: ImageMediaResponse = None,
        labels: List[str] = None,
        location: str = None,
        meta: str = None,
        name: str = None,
        parent_file_id: str = None,
        punish_flag: int = None,
        share_id: str = None,
        size: int = None,
        starred: bool = None,
        status: str = None,
        stream_locations: dict = None,
        streams_info: dict = None,
        thumbnail: str = None,
        trashed_at: str = None,
        type: str = None,
        updated_at: str = None,
        upload_id: str = None,
        url: str = None,
        user_meta: str = None,
        video_media_metadata: VideoMediaResponse = None,
        video_preview_metadata: VideoPreviewResponse = None,
    ):
        # category
        self.category = category
        # CharacteristicHash
        self.characteristic_hash = characteristic_hash
        # Content Hash
        self.content_hash = content_hash
        # content_hash_name
        self.content_hash_name = content_hash_name
        # content_type
        self.content_type = content_type
        # crc64_hash
        self.crc_64hash = crc_64hash
        # created_at
        self.created_at = created_at
        # description
        self.description = description
        # DomainID
        self.domain_id = domain_id
        # download_url
        self.download_url = download_url
        # drive_id
        self.drive_id = drive_id
        # encrypt_mode
        self.encrypt_mode = encrypt_mode
        # file_extension
        self.file_extension = file_extension
        # file_id
        self.file_id = file_id
        # Hidden
        # type: boolean
        self.hidden = hidden
        self.image_media_metadata = image_media_metadata
        # labels
        self.labels = labels
        # location
        self.location = location
        self.meta = meta
        # name
        self.name = name
        # parent_file_id
        self.parent_file_id = parent_file_id
        self.punish_flag = punish_flag
        self.share_id = share_id
        # Size
        self.size = size
        # starred
        # type: boolean
        self.starred = starred
        # status
        self.status = status
        self.stream_locations = stream_locations
        # @Deprecated streams url info
        self.streams_info = streams_info
        # thumbnail
        self.thumbnail = thumbnail
        # trashed_at
        self.trashed_at = trashed_at
        # type
        self.type = type
        # updated_at
        self.updated_at = updated_at
        # upload_id
        self.upload_id = upload_id
        # url
        self.url = url
        # user_meta
        self.user_meta = user_meta
        self.video_media_metadata = video_media_metadata
        self.video_preview_metadata = video_preview_metadata

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
        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.characteristic_hash is not None:
            result['characteristic_hash'] = self.characteristic_hash
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
        if self.location is not None:
            result['location'] = self.location
        if self.meta is not None:
            result['meta'] = self.meta
        if self.name is not None:
            result['name'] = self.name
        if self.parent_file_id is not None:
            result['parent_file_id'] = self.parent_file_id
        if self.punish_flag is not None:
            result['punish_flag'] = self.punish_flag
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.size is not None:
            result['size'] = self.size
        if self.starred is not None:
            result['starred'] = self.starred
        if self.status is not None:
            result['status'] = self.status
        if self.stream_locations is not None:
            result['stream_locations'] = self.stream_locations
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('characteristic_hash') is not None:
            self.characteristic_hash = m.get('characteristic_hash')
        if m.get('content_hash') is not None:
            self.content_hash = m.get('content_hash')
        if m.get('content_hash_name') is not None:
            self.content_hash_name = m.get('content_hash_name')
        if m.get('content_type') is not None:
            self.content_type = m.get('content_type')
        if m.get('crc64_hash') is not None:
            self.crc_64hash = m.get('crc64_hash')
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('download_url') is not None:
            self.download_url = m.get('download_url')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('encrypt_mode') is not None:
            self.encrypt_mode = m.get('encrypt_mode')
        if m.get('file_extension') is not None:
            self.file_extension = m.get('file_extension')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('hidden') is not None:
            self.hidden = m.get('hidden')
        if m.get('image_media_metadata') is not None:
            temp_model = ImageMediaResponse()
            self.image_media_metadata = temp_model.from_map(m['image_media_metadata'])
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('meta') is not None:
            self.meta = m.get('meta')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parent_file_id') is not None:
            self.parent_file_id = m.get('parent_file_id')
        if m.get('punish_flag') is not None:
            self.punish_flag = m.get('punish_flag')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('starred') is not None:
            self.starred = m.get('starred')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('stream_locations') is not None:
            self.stream_locations = m.get('stream_locations')
        if m.get('streams_info') is not None:
            self.streams_info = m.get('streams_info')
        if m.get('thumbnail') is not None:
            self.thumbnail = m.get('thumbnail')
        if m.get('trashed_at') is not None:
            self.trashed_at = m.get('trashed_at')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        if m.get('upload_id') is not None:
            self.upload_id = m.get('upload_id')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('user_meta') is not None:
            self.user_meta = m.get('user_meta')
        if m.get('video_media_metadata') is not None:
            temp_model = VideoMediaResponse()
            self.video_media_metadata = temp_model.from_map(m['video_media_metadata'])
        if m.get('video_preview_metadata') is not None:
            temp_model = VideoPreviewResponse()
            self.video_preview_metadata = temp_model.from_map(m['video_preview_metadata'])
        return self


class ConfirmLinkRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        temporary_token: str = None,
    ):
        self.headers = headers
        # 待绑定的临时token，此token只能访问绑定、取消绑定接口
        self.temporary_token = temporary_token

    def validate(self):
        self.validate_required(self.temporary_token, 'temporary_token')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.temporary_token is not None:
            result['temporary_token'] = self.temporary_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('temporary_token') is not None:
            self.temporary_token = m.get('temporary_token')
        return self


class CopyFileResponse(TeaModel):
    """
    文件拷贝 response
    """
    def __init__(
        self,
        async_task_id: str = None,
        domain_id: str = None,
        drive_id: str = None,
        file_id: str = None,
    ):
        # async_task_id
        self.async_task_id = async_task_id
        # DomainID
        self.domain_id = domain_id
        # drive_id
        self.drive_id = drive_id
        # file_id
        self.file_id = file_id

    def validate(self):
        if self.domain_id is not None:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z]+')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.file_id is not None:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9]{1,50}')

    def to_map(self):
        result = dict()
        if self.async_task_id is not None:
            result['async_task_id'] = self.async_task_id
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('async_task_id') is not None:
            self.async_task_id = m.get('async_task_id')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        return self


class CorsRule(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        allowed_header: List[str] = None,
        allowed_method: List[str] = None,
        allowed_origin: List[str] = None,
        expose_header: List[str] = None,
        max_age_seconds: int = None,
    ):
        # AllowedHeader
        self.allowed_header = allowed_header
        # AllowedMethod
        self.allowed_method = allowed_method
        # AllowedOrigin
        self.allowed_origin = allowed_origin
        # ExposeHeader
        self.expose_header = expose_header
        # MaxAgeSeconds
        self.max_age_seconds = max_age_seconds

    def validate(self):
        pass

    def to_map(self):
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allowed_header') is not None:
            self.allowed_header = m.get('allowed_header')
        if m.get('allowed_method') is not None:
            self.allowed_method = m.get('allowed_method')
        if m.get('allowed_origin') is not None:
            self.allowed_origin = m.get('allowed_origin')
        if m.get('expose_header') is not None:
            self.expose_header = m.get('expose_header')
        if m.get('max_age_seconds') is not None:
            self.max_age_seconds = m.get('max_age_seconds')
        return self


class CreateAppRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        app_name: str = None,
        description: str = None,
        is_third_party: bool = None,
        logo: str = None,
        public_key: str = None,
        redirect_uri: str = None,
        scope: List[str] = None,
        type: str = None,
    ):
        # App名称
        self.app_name = app_name
        # App描述
        self.description = description
        # 是否是domain私有App
        self.is_third_party = is_third_party
        # App图标
        self.logo = logo
        # RSA加密算法的公钥, PEM格式
        self.public_key = public_key
        # App回调地址
        self.redirect_uri = redirect_uri
        # App权限列表
        self.scope = scope
        # App类型
        self.type = type

    def validate(self):
        self.validate_required(self.app_name, 'app_name')
        if self.app_name is not None:
            self.validate_max_length(self.app_name, 'app_name', 128)
        if self.description is not None:
            self.validate_max_length(self.description, 'description', 128)
        self.validate_required(self.logo, 'logo')
        self.validate_required(self.public_key, 'public_key')
        self.validate_required(self.scope, 'scope')
        self.validate_required(self.type, 'type')

    def to_map(self):
        result = dict()
        if self.app_name is not None:
            result['app_name'] = self.app_name
        if self.description is not None:
            result['description'] = self.description
        if self.is_third_party is not None:
            result['is_third_party'] = self.is_third_party
        if self.logo is not None:
            result['logo'] = self.logo
        if self.public_key is not None:
            result['public_key'] = self.public_key
        if self.redirect_uri is not None:
            result['redirect_uri'] = self.redirect_uri
        if self.scope is not None:
            result['scope'] = self.scope
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('app_name') is not None:
            self.app_name = m.get('app_name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('is_third_party') is not None:
            self.is_third_party = m.get('is_third_party')
        if m.get('logo') is not None:
            self.logo = m.get('logo')
        if m.get('public_key') is not None:
            self.public_key = m.get('public_key')
        if m.get('redirect_uri') is not None:
            self.redirect_uri = m.get('redirect_uri')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateDomainRequest(TeaModel):
    """
    create domain request
    """
    def __init__(
        self,
        auth_config: dict = None,
        auth_dingding_app_id: str = None,
        auth_dingding_app_secret: str = None,
        auth_dingding_enable: bool = None,
        auth_endpoint_enable: bool = None,
        auth_ram_app_id: str = None,
        auth_ram_app_secret: str = None,
        auth_ram_enable: bool = None,
        data_hash_name: str = None,
        description: str = None,
        domain_name: str = None,
        event_filename_matches: str = None,
        event_mns_endpoint: str = None,
        event_mns_topic: str = None,
        event_names: List[str] = None,
        event_role_arn: str = None,
        init_drive_enable: bool = None,
        init_drive_size: int = None,
        mode: str = None,
        path_type: str = None,
        published_app_access_strategy: AppAccessStrategy = None,
        sharable: bool = None,
        store_level: str = None,
        store_region_list: List[str] = None,
    ):
        # 登录相关信息
        self.auth_config = auth_config
        # 钉钉 App Id
        self.auth_dingding_app_id = auth_dingding_app_id
        # 钉钉 App Secret
        self.auth_dingding_app_secret = auth_dingding_app_secret
        # 启用钉钉认证
        self.auth_dingding_enable = auth_dingding_enable
        self.auth_endpoint_enable = auth_endpoint_enable
        # RAM App Id
        self.auth_ram_app_id = auth_ram_app_id
        # RAM App Secret
        self.auth_ram_app_secret = auth_ram_app_secret
        # 启用 RAM 认证
        self.auth_ram_enable = auth_ram_enable
        # 数据 Hash 算法
        self.data_hash_name = data_hash_name
        # Domain 描述
        self.description = description
        # Domain 名称
        self.domain_name = domain_name
        # 事件通知 MNS 匹配文件名
        self.event_filename_matches = event_filename_matches
        # 事件通知 MNS Endpoint
        self.event_mns_endpoint = event_mns_endpoint
        # 事件通知 MNS Topic
        self.event_mns_topic = event_mns_topic
        # 事件名列表
        self.event_names = event_names
        # 事件通知 Role Arn
        self.event_role_arn = event_role_arn
        # 开启自动初始化 Drive
        self.init_drive_enable = init_drive_enable
        # 自动初始化 Drive 大小
        self.init_drive_size = init_drive_size
        # Domain 类型
        self.mode = mode
        # Domain 类型
        self.path_type = path_type
        self.published_app_access_strategy = published_app_access_strategy
        # 开启分享
        self.sharable = sharable
        # 存储级别
        self.store_level = store_level
        # 存储 Region 列表
        self.store_region_list = store_region_list

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.mode, 'mode')
        if self.published_app_access_strategy:
            self.published_app_access_strategy.validate()
        self.validate_required(self.store_region_list, 'store_region_list')

    def to_map(self):
        result = dict()
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
        if self.data_hash_name is not None:
            result['data_hash_name'] = self.data_hash_name
        if self.description is not None:
            result['description'] = self.description
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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_config') is not None:
            self.auth_config = m.get('auth_config')
        if m.get('auth_dingding_app_id') is not None:
            self.auth_dingding_app_id = m.get('auth_dingding_app_id')
        if m.get('auth_dingding_app_secret') is not None:
            self.auth_dingding_app_secret = m.get('auth_dingding_app_secret')
        if m.get('auth_dingding_enable') is not None:
            self.auth_dingding_enable = m.get('auth_dingding_enable')
        if m.get('auth_endpoint_enable') is not None:
            self.auth_endpoint_enable = m.get('auth_endpoint_enable')
        if m.get('auth_ram_app_id') is not None:
            self.auth_ram_app_id = m.get('auth_ram_app_id')
        if m.get('auth_ram_app_secret') is not None:
            self.auth_ram_app_secret = m.get('auth_ram_app_secret')
        if m.get('auth_ram_enable') is not None:
            self.auth_ram_enable = m.get('auth_ram_enable')
        if m.get('data_hash_name') is not None:
            self.data_hash_name = m.get('data_hash_name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain_name') is not None:
            self.domain_name = m.get('domain_name')
        if m.get('event_filename_matches') is not None:
            self.event_filename_matches = m.get('event_filename_matches')
        if m.get('event_mns_endpoint') is not None:
            self.event_mns_endpoint = m.get('event_mns_endpoint')
        if m.get('event_mns_topic') is not None:
            self.event_mns_topic = m.get('event_mns_topic')
        if m.get('event_names') is not None:
            self.event_names = m.get('event_names')
        if m.get('event_role_arn') is not None:
            self.event_role_arn = m.get('event_role_arn')
        if m.get('init_drive_enable') is not None:
            self.init_drive_enable = m.get('init_drive_enable')
        if m.get('init_drive_size') is not None:
            self.init_drive_size = m.get('init_drive_size')
        if m.get('mode') is not None:
            self.mode = m.get('mode')
        if m.get('path_type') is not None:
            self.path_type = m.get('path_type')
        if m.get('published_app_access_strategy') is not None:
            temp_model = AppAccessStrategy()
            self.published_app_access_strategy = temp_model.from_map(m['published_app_access_strategy'])
        if m.get('sharable') is not None:
            self.sharable = m.get('sharable')
        if m.get('store_level') is not None:
            self.store_level = m.get('store_level')
        if m.get('store_region_list') is not None:
            self.store_region_list = m.get('store_region_list')
        return self


class CreateDriveResponse(TeaModel):
    """
    Create drive response
    """
    def __init__(
        self,
        domain_id: str = None,
        drive_id: str = None,
    ):
        # Domain ID
        self.domain_id = domain_id
        # Drive ID
        self.drive_id = drive_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        return self


class UploadPartInfo(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        content_type: str = None,
        etag: str = None,
        part_number: int = None,
        part_size: int = None,
        upload_url: str = None,
    ):
        self.content_type = content_type
        # etag
        self.etag = etag
        # PartNumber
        self.part_number = part_number
        # PartSize：
        self.part_size = part_size
        # upload_url
        self.upload_url = upload_url

    def validate(self):
        if self.part_number is not None:
            self.validate_maximum(self.part_number, 'part_number', 10000)
            self.validate_minimum(self.part_number, 'part_number', 1)
        if self.part_size is not None:
            self.validate_maximum(self.part_size, 'part_size', 5368709120)
            self.validate_minimum(self.part_size, 'part_size', 102400)

    def to_map(self):
        result = dict()
        if self.content_type is not None:
            result['content_type'] = self.content_type
        if self.etag is not None:
            result['etag'] = self.etag
        if self.part_number is not None:
            result['part_number'] = self.part_number
        if self.part_size is not None:
            result['part_size'] = self.part_size
        if self.upload_url is not None:
            result['upload_url'] = self.upload_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content_type') is not None:
            self.content_type = m.get('content_type')
        if m.get('etag') is not None:
            self.etag = m.get('etag')
        if m.get('part_number') is not None:
            self.part_number = m.get('part_number')
        if m.get('part_size') is not None:
            self.part_size = m.get('part_size')
        if m.get('upload_url') is not None:
            self.upload_url = m.get('upload_url')
        return self


class CreateFileResponse(TeaModel):
    """
    Create file response
    """
    def __init__(
        self,
        domain_id: str = None,
        drive_id: str = None,
        encrypt_mode: str = None,
        exist: bool = None,
        file_id: str = None,
        file_name: str = None,
        location: str = None,
        parent_file_id: str = None,
        part_info_list: List[UploadPartInfo] = None,
        rapid_upload: bool = None,
        status: str = None,
        streams_upload_info: dict = None,
        type: str = None,
        upload_id: str = None,
    ):
        # domain_id
        self.domain_id = domain_id
        # drive_id
        self.drive_id = drive_id
        # encrypt_mode
        self.encrypt_mode = encrypt_mode
        # exist
        # type: boolean
        self.exist = exist
        # file_id
        self.file_id = file_id
        # file_name
        self.file_name = file_name
        # location
        self.location = location
        # parent_file_id
        self.parent_file_id = parent_file_id
        # part_info_list
        self.part_info_list = part_info_list
        # rapid_upload
        # type: boolean
        self.rapid_upload = rapid_upload
        # status
        self.status = status
        # streams_upload_info
        self.streams_upload_info = streams_upload_info
        # type
        self.type = type
        # upload_id
        self.upload_id = upload_id

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
        result = dict()
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
        if self.location is not None:
            result['location'] = self.location
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('encrypt_mode') is not None:
            self.encrypt_mode = m.get('encrypt_mode')
        if m.get('exist') is not None:
            self.exist = m.get('exist')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('file_name') is not None:
            self.file_name = m.get('file_name')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('parent_file_id') is not None:
            self.parent_file_id = m.get('parent_file_id')
        self.part_info_list = []
        if m.get('part_info_list') is not None:
            for k in m.get('part_info_list'):
                temp_model = UploadPartInfo()
                self.part_info_list.append(temp_model.from_map(k))
        if m.get('rapid_upload') is not None:
            self.rapid_upload = m.get('rapid_upload')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('streams_upload_info') is not None:
            self.streams_upload_info = m.get('streams_upload_info')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('upload_id') is not None:
            self.upload_id = m.get('upload_id')
        return self


class CreateShareLinkResponse(TeaModel):
    """
    create_share_link response
    """
    def __init__(
        self,
        created_at: str = None,
        creator: str = None,
        description: str = None,
        download_count: int = None,
        drive_id: str = None,
        expiration: str = None,
        expired: bool = None,
        file_id: str = None,
        file_id_list: List[str] = None,
        file_path_list: List[str] = None,
        preview_count: int = None,
        save_count: int = None,
        share_id: str = None,
        share_msg: str = None,
        share_name: str = None,
        share_policy: str = None,
        share_pwd: str = None,
        share_url: str = None,
        updated_at: str = None,
    ):
        # created_at
        self.created_at = created_at
        # creator
        self.creator = creator
        # description
        self.description = description
        # 下载次数
        self.download_count = download_count
        # drive_id
        self.drive_id = drive_id
        # expiration
        self.expiration = expiration
        # expired
        self.expired = expired
        # file_id
        self.file_id = file_id
        # file_id_list
        self.file_id_list = file_id_list
        # file_id_list
        self.file_path_list = file_path_list
        # preview_count
        self.preview_count = preview_count
        # 转存次数
        self.save_count = save_count
        # share_id
        self.share_id = share_id
        # share_msg
        self.share_msg = share_msg
        # share_name
        self.share_name = share_name
        # share_policy
        self.share_policy = share_policy
        # share_pwd
        self.share_pwd = share_pwd
        # share_url
        self.share_url = share_url
        # updated_at
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.creator is not None:
            result['creator'] = self.creator
        if self.description is not None:
            result['description'] = self.description
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
        if self.file_id_list is not None:
            result['file_id_list'] = self.file_id_list
        if self.file_path_list is not None:
            result['file_path_list'] = self.file_path_list
        if self.preview_count is not None:
            result['preview_count'] = self.preview_count
        if self.save_count is not None:
            result['save_count'] = self.save_count
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.share_msg is not None:
            result['share_msg'] = self.share_msg
        if self.share_name is not None:
            result['share_name'] = self.share_name
        if self.share_policy is not None:
            result['share_policy'] = self.share_policy
        if self.share_pwd is not None:
            result['share_pwd'] = self.share_pwd
        if self.share_url is not None:
            result['share_url'] = self.share_url
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('download_count') is not None:
            self.download_count = m.get('download_count')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('expiration') is not None:
            self.expiration = m.get('expiration')
        if m.get('expired') is not None:
            self.expired = m.get('expired')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('file_id_list') is not None:
            self.file_id_list = m.get('file_id_list')
        if m.get('file_path_list') is not None:
            self.file_path_list = m.get('file_path_list')
        if m.get('preview_count') is not None:
            self.preview_count = m.get('preview_count')
        if m.get('save_count') is not None:
            self.save_count = m.get('save_count')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('share_msg') is not None:
            self.share_msg = m.get('share_msg')
        if m.get('share_name') is not None:
            self.share_name = m.get('share_name')
        if m.get('share_policy') is not None:
            self.share_policy = m.get('share_policy')
        if m.get('share_pwd') is not None:
            self.share_pwd = m.get('share_pwd')
        if m.get('share_url') is not None:
            self.share_url = m.get('share_url')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        return self


class CreateShareResponse(TeaModel):
    """
    Create share response
    """
    def __init__(
        self,
        domain_id: str = None,
        share_id: str = None,
    ):
        # domain_id
        self.domain_id = domain_id
        # share_id
        self.share_id = share_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.share_id is not None:
            result['share_id'] = self.share_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        return self


class DefaultChangePasswordRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        app_id: str = None,
        encrypted_key: str = None,
        new_password: str = None,
        phone_number: str = None,
        phone_region: str = None,
        state: str = None,
    ):
        self.headers = headers
        # App ID, 当前访问的App
        self.app_id = app_id
        # AES-256对称加密密钥，通过App公钥加密后传输
        self.encrypted_key = encrypted_key
        # 新密码，必须包含数字和字母，长度8-20个字符
        self.new_password = new_password
        # 手机号
        self.phone_number = phone_number
        # 国家编号，默认86，不需要填+号，直接填数字
        self.phone_region = phone_region
        # 修改密码的临时授权码
        self.state = state

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.encrypted_key, 'encrypted_key')
        self.validate_required(self.new_password, 'new_password')
        self.validate_required(self.phone_number, 'phone_number')
        self.validate_required(self.state, 'state')

    def to_map(self):
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('app_id') is not None:
            self.app_id = m.get('app_id')
        if m.get('encrypted_key') is not None:
            self.encrypted_key = m.get('encrypted_key')
        if m.get('new_password') is not None:
            self.new_password = m.get('new_password')
        if m.get('phone_number') is not None:
            self.phone_number = m.get('phone_number')
        if m.get('phone_region') is not None:
            self.phone_region = m.get('phone_region')
        if m.get('state') is not None:
            self.state = m.get('state')
        return self


class DefaultSetPasswordRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        app_id: str = None,
        encrypted_key: str = None,
        new_password: str = None,
        state: str = None,
    ):
        self.headers = headers
        # App ID, 当前访问的App
        self.app_id = app_id
        # AES-256对称加密密钥，通过App公钥加密后传输
        self.encrypted_key = encrypted_key
        # 新密码，必须包含数字和字母，长度8-20个字符，使用AES-256对称加密后传输（CBC模式, 填充算法为PKCS7Padding，生成base64字符串）
        self.new_password = new_password
        # 修改密码的临时授权码
        self.state = state

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.encrypted_key, 'encrypted_key')
        self.validate_required(self.new_password, 'new_password')
        self.validate_required(self.state, 'state')

    def to_map(self):
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('app_id') is not None:
            self.app_id = m.get('app_id')
        if m.get('encrypted_key') is not None:
            self.encrypted_key = m.get('encrypted_key')
        if m.get('new_password') is not None:
            self.new_password = m.get('new_password')
        if m.get('state') is not None:
            self.state = m.get('state')
        return self


class DeleteAppRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        app_id: str = None,
    ):
        # App ID
        self.app_id = app_id

    def validate(self):
        self.validate_required(self.app_id, 'app_id')

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['app_id'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('app_id') is not None:
            self.app_id = m.get('app_id')
        return self


class DeleteBizCNameAndCertRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        biz_cname: str = None,
        cname_type: str = None,
        domain_id: str = None,
        is_vpc: bool = None,
    ):
        # api cname
        self.biz_cname = biz_cname
        # cname type
        self.cname_type = cname_type
        # domain ID
        self.domain_id = domain_id
        # vpc
        self.is_vpc = is_vpc

    def validate(self):
        self.validate_required(self.cname_type, 'cname_type')
        self.validate_required(self.domain_id, 'domain_id')

    def to_map(self):
        result = dict()
        if self.biz_cname is not None:
            result['biz_cname'] = self.biz_cname
        if self.cname_type is not None:
            result['cname_type'] = self.cname_type
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.is_vpc is not None:
            result['is_vpc'] = self.is_vpc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('biz_cname') is not None:
            self.biz_cname = m.get('biz_cname')
        if m.get('cname_type') is not None:
            self.cname_type = m.get('cname_type')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('is_vpc') is not None:
            self.is_vpc = m.get('is_vpc')
        return self


class DeleteBizCNameCertRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        biz_cname: str = None,
        cert_id: str = None,
        cname_type: str = None,
        domain_id: str = None,
        is_vpc: bool = None,
    ):
        # biz cname
        self.biz_cname = biz_cname
        # cert id
        self.cert_id = cert_id
        # cname type
        self.cname_type = cname_type
        # domain ID
        self.domain_id = domain_id
        # is vpc
        self.is_vpc = is_vpc

    def validate(self):
        self.validate_required(self.cname_type, 'cname_type')
        self.validate_required(self.domain_id, 'domain_id')

    def to_map(self):
        result = dict()
        if self.biz_cname is not None:
            result['biz_cname'] = self.biz_cname
        if self.cert_id is not None:
            result['cert_id'] = self.cert_id
        if self.cname_type is not None:
            result['cname_type'] = self.cname_type
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.is_vpc is not None:
            result['is_vpc'] = self.is_vpc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('biz_cname') is not None:
            self.biz_cname = m.get('biz_cname')
        if m.get('cert_id') is not None:
            self.cert_id = m.get('cert_id')
        if m.get('cname_type') is not None:
            self.cname_type = m.get('cname_type')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('is_vpc') is not None:
            self.is_vpc = m.get('is_vpc')
        return self


class DeleteDataCNameAndCertRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        data_cname: str = None,
        domain_id: str = None,
        location: str = None,
    ):
        # cn-shanghai data cname
        self.data_cname = data_cname
        # domain ID
        self.domain_id = domain_id
        # location
        self.location = location

    def validate(self):
        self.validate_required(self.data_cname, 'data_cname')
        self.validate_required(self.domain_id, 'domain_id')
        self.validate_required(self.location, 'location')

    def to_map(self):
        result = dict()
        if self.data_cname is not None:
            result['data_cname'] = self.data_cname
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.location is not None:
            result['location'] = self.location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data_cname') is not None:
            self.data_cname = m.get('data_cname')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('location') is not None:
            self.location = m.get('location')
        return self


class DeleteDomainRequest(TeaModel):
    """
    delete domain request
    """
    def __init__(
        self,
        domain_id: str = None,
    ):
        # Domain ID
        self.domain_id = domain_id

    def validate(self):
        self.validate_required(self.domain_id, 'domain_id')

    def to_map(self):
        result = dict()
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
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
        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteFileResponse(TeaModel):
    """
    删除文件 response
    """
    def __init__(
        self,
        async_task_id: str = None,
        domain_id: str = None,
        drive_id: str = None,
        file_id: str = None,
    ):
        # async_task_id
        self.async_task_id = async_task_id
        # domain_id
        self.domain_id = domain_id
        # drive_id
        self.drive_id = drive_id
        # file_id
        self.file_id = file_id

    def validate(self):
        if self.domain_id is not None:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z]+')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.file_id is not None:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9]{1,50}')

    def to_map(self):
        result = dict()
        if self.async_task_id is not None:
            result['async_task_id'] = self.async_task_id
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('async_task_id') is not None:
            self.async_task_id = m.get('async_task_id')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        return self


class DeleteFilesResponse(TeaModel):
    """
    批量删除文件 response
    """
    def __init__(
        self,
        deleted_file_id_list: List[str] = None,
        domain_id: str = None,
        drive_id: str = None,
    ):
        # deleted_file_id_list
        self.deleted_file_id_list = deleted_file_id_list
        # domain_id
        self.domain_id = domain_id
        # drive_id
        self.drive_id = drive_id

    def validate(self):
        if self.domain_id is not None:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z]+')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')

    def to_map(self):
        result = dict()
        if self.deleted_file_id_list is not None:
            result['deleted_file_id_list'] = self.deleted_file_id_list
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deleted_file_id_list') is not None:
            self.deleted_file_id_list = m.get('deleted_file_id_list')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        return self


class DeviceAuthorizeRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        client_id: str = None,
        device_info: str = None,
        device_name: str = None,
        login_type: str = None,
        scope: List[str] = None,
    ):
        # Client ID, 此处填写创建App时返回的AppID
        self.client_id = client_id
        # 设备信息，用于用户识别设备
        self.device_info = device_info
        # 设备名，实现方需保证不同设备的设备名不重复（推荐用硬件名称+硬件型号作为设备名）
        self.device_name = device_name
        # 鉴权方式，目前支持ding,ram鉴权
        self.login_type = login_type
        # 申请的权限列表, 默认为所有权限
        self.scope = scope

    def validate(self):
        self.validate_required(self.client_id, 'client_id')
        self.validate_required(self.device_name, 'device_name')

    def to_map(self):
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientID') is not None:
            self.client_id = m.get('ClientID')
        if m.get('DeviceInfo') is not None:
            self.device_info = m.get('DeviceInfo')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('LoginType') is not None:
            self.login_type = m.get('LoginType')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        return self


class FileDeltaResponse(TeaModel):
    """
    the file op info
    """
    def __init__(
        self,
        current_category: str = None,
        file: BaseCCPFileResponse = None,
        file_id: str = None,
        op: str = None,
    ):
        self.current_category = current_category
        self.file = file
        self.file_id = file_id
        self.op = op

    def validate(self):
        if self.file:
            self.file.validate()

    def to_map(self):
        result = dict()
        if self.current_category is not None:
            result['current_category'] = self.current_category
        if self.file is not None:
            result['file'] = self.file.to_map()
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.op is not None:
            result['op'] = self.op
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('current_category') is not None:
            self.current_category = m.get('current_category')
        if m.get('file') is not None:
            temp_model = BaseCCPFileResponse()
            self.file = temp_model.from_map(m['file'])
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('op') is not None:
            self.op = m.get('op')
        return self


class GetAccessTokenByLinkInfoRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        extra: str = None,
        identity: str = None,
        type: str = None,
    ):
        self.headers = headers
        # 额外的信息，比如type为mobile时，此字段为国家编号，不填默认86
        self.extra = extra
        # 唯一身份标识
        self.identity = identity
        # 认证类型
        self.type = type

    def validate(self):
        self.validate_required(self.identity, 'identity')
        self.validate_required(self.type, 'type')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.extra is not None:
            result['extra'] = self.extra
        if self.identity is not None:
            result['identity'] = self.identity
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('extra') is not None:
            self.extra = m.get('extra')
        if m.get('identity') is not None:
            self.identity = m.get('identity')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetAppPublicKeyRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        app_id: str = None,
    ):
        # App ID
        self.app_id = app_id

    def validate(self):
        self.validate_required(self.app_id, 'app_id')

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['app_id'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('app_id') is not None:
            self.app_id = m.get('app_id')
        return self


class GetAppRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        app_id: str = None,
    ):
        # App ID
        self.app_id = app_id

    def validate(self):
        self.validate_required(self.app_id, 'app_id')

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['app_id'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('app_id') is not None:
            self.app_id = m.get('app_id')
        return self


class GetAsyncTaskResponse(TeaModel):
    """
    Get AsyncTask Response
    """
    def __init__(
        self,
        async_task_id: str = None,
        consumed_process: int = None,
        err_code: int = None,
        message: str = None,
        state: str = None,
        total_process: int = None,
        url: str = None,
    ):
        # async_task_id
        # type:string
        self.async_task_id = async_task_id
        # consumed_process
        self.consumed_process = consumed_process
        # err_code
        self.err_code = err_code
        # message
        self.message = message
        # state
        self.state = state
        # total_process
        self.total_process = total_process
        # download_url
        # example
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.async_task_id is not None:
            result['async_task_id'] = self.async_task_id
        if self.consumed_process is not None:
            result['consumed_process'] = self.consumed_process
        if self.err_code is not None:
            result['err_code'] = self.err_code
        if self.message is not None:
            result['message'] = self.message
        if self.state is not None:
            result['state'] = self.state
        if self.total_process is not None:
            result['total_process'] = self.total_process
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('async_task_id') is not None:
            self.async_task_id = m.get('async_task_id')
        if m.get('consumed_process') is not None:
            self.consumed_process = m.get('consumed_process')
        if m.get('err_code') is not None:
            self.err_code = m.get('err_code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('total_process') is not None:
            self.total_process = m.get('total_process')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetBizCNameInfoRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        cname_type: str = None,
        domain_id: str = None,
        is_vpc: bool = None,
    ):
        # cname type
        self.cname_type = cname_type
        # domain ID
        self.domain_id = domain_id
        # is vpc
        self.is_vpc = is_vpc

    def validate(self):
        self.validate_required(self.cname_type, 'cname_type')
        self.validate_required(self.domain_id, 'domain_id')

    def to_map(self):
        result = dict()
        if self.cname_type is not None:
            result['cname_type'] = self.cname_type
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.is_vpc is not None:
            result['is_vpc'] = self.is_vpc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cname_type') is not None:
            self.cname_type = m.get('cname_type')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('is_vpc') is not None:
            self.is_vpc = m.get('is_vpc')
        return self


class GetByLinkInfoRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        extra: str = None,
        identity: str = None,
        type: str = None,
    ):
        self.headers = headers
        # 额外的信息，比如type为mobile时，此字段为国家编号，不填默认86
        self.extra = extra
        # 唯一身份标识
        self.identity = identity
        # 认证类型
        self.type = type

    def validate(self):
        self.validate_required(self.identity, 'identity')
        self.validate_required(self.type, 'type')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.extra is not None:
            result['extra'] = self.extra
        if self.identity is not None:
            result['identity'] = self.identity
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('extra') is not None:
            self.extra = m.get('extra')
        if m.get('identity') is not None:
            self.identity = m.get('identity')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetCaptchaRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        app_id: str = None,
    ):
        self.headers = headers
        # App ID, 当前访问的App
        self.app_id = app_id

    def validate(self):
        self.validate_required(self.app_id, 'app_id')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.app_id is not None:
            result['app_id'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('app_id') is not None:
            self.app_id = m.get('app_id')
        return self


class GetCorsRuleListRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        domain_id: str = None,
    ):
        # domain ID
        self.domain_id = domain_id

    def validate(self):
        self.validate_required(self.domain_id, 'domain_id')

    def to_map(self):
        result = dict()
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        return self


class GetDataCNameInfoRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        domain_id: str = None,
    ):
        # domain ID
        self.domain_id = domain_id

    def validate(self):
        self.validate_required(self.domain_id, 'domain_id')

    def to_map(self):
        result = dict()
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        return self


class GetDirSizeInfoResponse(TeaModel):
    """
    获取文件夹size信息
    """
    def __init__(
        self,
        dir_count: int = None,
        file_count: int = None,
        size: int = None,
    ):
        # dir_count
        self.dir_count = dir_count
        # file_count
        self.file_count = file_count
        # size
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.dir_count is not None:
            result['dir_count'] = self.dir_count
        if self.file_count is not None:
            result['file_count'] = self.file_count
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dir_count') is not None:
            self.dir_count = m.get('dir_count')
        if m.get('file_count') is not None:
            self.file_count = m.get('file_count')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class GetDomainRequest(TeaModel):
    """
    get domain request
    """
    def __init__(
        self,
        domain_id: str = None,
    ):
        # Domain ID
        self.domain_id = domain_id

    def validate(self):
        self.validate_required(self.domain_id, 'domain_id')

    def to_map(self):
        result = dict()
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        return self


class RateLimit(TeaModel):
    """
    下载限速配置
    """
    def __init__(
        self,
        part_size: int = None,
        part_speed: int = None,
    ):
        self.part_size = part_size
        self.part_speed = part_speed

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.part_size is not None:
            result['part_size'] = self.part_size
        if self.part_speed is not None:
            result['part_speed'] = self.part_speed
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('part_size') is not None:
            self.part_size = m.get('part_size')
        if m.get('part_speed') is not None:
            self.part_speed = m.get('part_speed')
        return self


class GetDownloadUrlResponse(TeaModel):
    """
    获取download url response
    """
    def __init__(
        self,
        expiration: str = None,
        method: str = None,
        ratelimit: RateLimit = None,
        size: int = None,
        streams_url: dict = None,
        url: str = None,
    ):
        # expiration
        self.expiration = expiration
        # method
        self.method = method
        self.ratelimit = ratelimit
        # size
        self.size = size
        # streams url info
        self.streams_url = streams_url
        # url
        self.url = url

    def validate(self):
        if self.ratelimit:
            self.ratelimit.validate()

    def to_map(self):
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expiration') is not None:
            self.expiration = m.get('expiration')
        if m.get('method') is not None:
            self.method = m.get('method')
        if m.get('ratelimit') is not None:
            temp_model = RateLimit()
            self.ratelimit = temp_model.from_map(m['ratelimit'])
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('streams_url') is not None:
            self.streams_url = m.get('streams_url')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetDriveResponse(TeaModel):
    """
    Get drive response
    """
    def __init__(
        self,
        creator: str = None,
        description: str = None,
        domain_id: str = None,
        drive_id: str = None,
        drive_name: str = None,
        drive_type: str = None,
        encrypt_data_access: bool = None,
        encrypt_mode: str = None,
        owner: str = None,
        owner_type: str = None,
        relative_path: str = None,
        status: str = None,
        store_id: str = None,
        total_size: int = None,
        used_size: int = None,
    ):
        # Drive 创建者
        self.creator = creator
        # Drive 备注信息
        self.description = description
        # Domain ID
        self.domain_id = domain_id
        # Drive ID
        self.drive_id = drive_id
        # Drive 名称
        self.drive_name = drive_name
        # Drive 类型
        self.drive_type = drive_type
        self.encrypt_data_access = encrypt_data_access
        self.encrypt_mode = encrypt_mode
        # Drive 所有者
        self.owner = owner
        # Drive 所有者类型
        self.owner_type = owner_type
        # Drive存储基于store的相对路径，domain的PathType为OSSPath时返回
        self.relative_path = relative_path
        # Drive 状态
        self.status = status
        # 存储 ID, domain的PathType为OSSPath时返回
        self.store_id = store_id
        # Drive 空间总量
        self.total_size = total_size
        # Drive 空间已使用量
        self.used_size = used_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
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
        if self.owner_type is not None:
            result['owner_type'] = self.owner_type
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('drive_name') is not None:
            self.drive_name = m.get('drive_name')
        if m.get('drive_type') is not None:
            self.drive_type = m.get('drive_type')
        if m.get('encrypt_data_access') is not None:
            self.encrypt_data_access = m.get('encrypt_data_access')
        if m.get('encrypt_mode') is not None:
            self.encrypt_mode = m.get('encrypt_mode')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('owner_type') is not None:
            self.owner_type = m.get('owner_type')
        if m.get('relative_path') is not None:
            self.relative_path = m.get('relative_path')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('store_id') is not None:
            self.store_id = m.get('store_id')
        if m.get('total_size') is not None:
            self.total_size = m.get('total_size')
        if m.get('used_size') is not None:
            self.used_size = m.get('used_size')
        return self


class GetFileByPathResponse(TeaModel):
    """
    根据路径获取文件元数据response
    """
    def __init__(
        self,
        category: str = None,
        characteristic_hash: str = None,
        content_hash: str = None,
        content_hash_name: str = None,
        content_type: str = None,
        crc_64hash: str = None,
        created_at: str = None,
        description: str = None,
        domain_id: str = None,
        download_url: str = None,
        drive_id: str = None,
        encrypt_mode: str = None,
        file_extension: str = None,
        file_id: str = None,
        hidden: bool = None,
        image_media_metadata: ImageMediaResponse = None,
        labels: List[str] = None,
        meta: str = None,
        name: str = None,
        parent_file_id: str = None,
        punish_flag: int = None,
        share_id: str = None,
        size: int = None,
        starred: bool = None,
        status: str = None,
        streams_info: dict = None,
        thumbnail: str = None,
        trashed_at: str = None,
        type: str = None,
        updated_at: str = None,
        upload_id: str = None,
        url: str = None,
        user_meta: str = None,
        video_media_metadata: VideoMediaResponse = None,
        video_preview_metadata: VideoPreviewResponse = None,
    ):
        # category
        self.category = category
        # CharacteristicHash
        self.characteristic_hash = characteristic_hash
        # Content Hash
        self.content_hash = content_hash
        # content_hash_name
        self.content_hash_name = content_hash_name
        # content_type
        self.content_type = content_type
        # crc64_hash
        self.crc_64hash = crc_64hash
        # created_at
        self.created_at = created_at
        # description
        self.description = description
        # DomainID
        self.domain_id = domain_id
        # download_url
        self.download_url = download_url
        # drive_id
        self.drive_id = drive_id
        # encrypt_mode
        self.encrypt_mode = encrypt_mode
        # file_extension
        self.file_extension = file_extension
        # file_id
        self.file_id = file_id
        # Hidden
        # type: boolean
        self.hidden = hidden
        self.image_media_metadata = image_media_metadata
        # labels
        self.labels = labels
        self.meta = meta
        # name
        self.name = name
        # parent_file_id
        self.parent_file_id = parent_file_id
        self.punish_flag = punish_flag
        self.share_id = share_id
        # Size
        self.size = size
        # starred
        # type: boolean
        self.starred = starred
        # status
        self.status = status
        # @Deprecated streams url info
        self.streams_info = streams_info
        # thumbnail
        self.thumbnail = thumbnail
        # trashed_at
        self.trashed_at = trashed_at
        # type
        self.type = type
        # updated_at
        self.updated_at = updated_at
        # upload_id
        self.upload_id = upload_id
        # url
        self.url = url
        # user_meta
        self.user_meta = user_meta
        self.video_media_metadata = video_media_metadata
        self.video_preview_metadata = video_preview_metadata

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
        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.characteristic_hash is not None:
            result['characteristic_hash'] = self.characteristic_hash
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
        if self.share_id is not None:
            result['share_id'] = self.share_id
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('characteristic_hash') is not None:
            self.characteristic_hash = m.get('characteristic_hash')
        if m.get('content_hash') is not None:
            self.content_hash = m.get('content_hash')
        if m.get('content_hash_name') is not None:
            self.content_hash_name = m.get('content_hash_name')
        if m.get('content_type') is not None:
            self.content_type = m.get('content_type')
        if m.get('crc64_hash') is not None:
            self.crc_64hash = m.get('crc64_hash')
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('download_url') is not None:
            self.download_url = m.get('download_url')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('encrypt_mode') is not None:
            self.encrypt_mode = m.get('encrypt_mode')
        if m.get('file_extension') is not None:
            self.file_extension = m.get('file_extension')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('hidden') is not None:
            self.hidden = m.get('hidden')
        if m.get('image_media_metadata') is not None:
            temp_model = ImageMediaResponse()
            self.image_media_metadata = temp_model.from_map(m['image_media_metadata'])
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('meta') is not None:
            self.meta = m.get('meta')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parent_file_id') is not None:
            self.parent_file_id = m.get('parent_file_id')
        if m.get('punish_flag') is not None:
            self.punish_flag = m.get('punish_flag')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('starred') is not None:
            self.starred = m.get('starred')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('streams_info') is not None:
            self.streams_info = m.get('streams_info')
        if m.get('thumbnail') is not None:
            self.thumbnail = m.get('thumbnail')
        if m.get('trashed_at') is not None:
            self.trashed_at = m.get('trashed_at')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        if m.get('upload_id') is not None:
            self.upload_id = m.get('upload_id')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('user_meta') is not None:
            self.user_meta = m.get('user_meta')
        if m.get('video_media_metadata') is not None:
            temp_model = VideoMediaResponse()
            self.video_media_metadata = temp_model.from_map(m['video_media_metadata'])
        if m.get('video_preview_metadata') is not None:
            temp_model = VideoPreviewResponse()
            self.video_preview_metadata = temp_model.from_map(m['video_preview_metadata'])
        return self


class GetFileResponse(TeaModel):
    """
    获取文件元数据response
    """
    def __init__(
        self,
        category: str = None,
        characteristic_hash: str = None,
        content_hash: str = None,
        content_hash_name: str = None,
        content_type: str = None,
        crc_64hash: str = None,
        created_at: str = None,
        description: str = None,
        domain_id: str = None,
        download_url: str = None,
        drive_id: str = None,
        encrypt_mode: str = None,
        file_extension: str = None,
        file_id: str = None,
        hidden: bool = None,
        image_media_metadata: ImageMediaResponse = None,
        labels: List[str] = None,
        meta: str = None,
        name: str = None,
        parent_file_id: str = None,
        punish_flag: int = None,
        share_id: str = None,
        size: int = None,
        starred: bool = None,
        status: str = None,
        streams_info: dict = None,
        thumbnail: str = None,
        trashed_at: str = None,
        type: str = None,
        updated_at: str = None,
        upload_id: str = None,
        url: str = None,
        user_meta: str = None,
        video_media_metadata: VideoMediaResponse = None,
        video_preview_metadata: VideoPreviewResponse = None,
    ):
        # category
        self.category = category
        # CharacteristicHash
        self.characteristic_hash = characteristic_hash
        # Content Hash
        self.content_hash = content_hash
        # content_hash_name
        self.content_hash_name = content_hash_name
        # content_type
        self.content_type = content_type
        # crc64_hash
        self.crc_64hash = crc_64hash
        # created_at
        self.created_at = created_at
        # description
        self.description = description
        # DomainID
        self.domain_id = domain_id
        # download_url
        self.download_url = download_url
        # drive_id
        self.drive_id = drive_id
        # encrypt_mode
        self.encrypt_mode = encrypt_mode
        # file_extension
        self.file_extension = file_extension
        # file_id
        self.file_id = file_id
        # Hidden
        # type: boolean
        self.hidden = hidden
        self.image_media_metadata = image_media_metadata
        # labels
        self.labels = labels
        self.meta = meta
        # name
        self.name = name
        # parent_file_id
        self.parent_file_id = parent_file_id
        self.punish_flag = punish_flag
        self.share_id = share_id
        # Size
        self.size = size
        # starred
        # type: boolean
        self.starred = starred
        # status
        self.status = status
        # @Deprecated streams url info
        self.streams_info = streams_info
        # thumbnail
        self.thumbnail = thumbnail
        # trashed_at
        self.trashed_at = trashed_at
        # type
        self.type = type
        # updated_at
        self.updated_at = updated_at
        # upload_id
        self.upload_id = upload_id
        # url
        self.url = url
        # user_meta
        self.user_meta = user_meta
        self.video_media_metadata = video_media_metadata
        self.video_preview_metadata = video_preview_metadata

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
        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.characteristic_hash is not None:
            result['characteristic_hash'] = self.characteristic_hash
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
        if self.share_id is not None:
            result['share_id'] = self.share_id
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('characteristic_hash') is not None:
            self.characteristic_hash = m.get('characteristic_hash')
        if m.get('content_hash') is not None:
            self.content_hash = m.get('content_hash')
        if m.get('content_hash_name') is not None:
            self.content_hash_name = m.get('content_hash_name')
        if m.get('content_type') is not None:
            self.content_type = m.get('content_type')
        if m.get('crc64_hash') is not None:
            self.crc_64hash = m.get('crc64_hash')
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('download_url') is not None:
            self.download_url = m.get('download_url')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('encrypt_mode') is not None:
            self.encrypt_mode = m.get('encrypt_mode')
        if m.get('file_extension') is not None:
            self.file_extension = m.get('file_extension')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('hidden') is not None:
            self.hidden = m.get('hidden')
        if m.get('image_media_metadata') is not None:
            temp_model = ImageMediaResponse()
            self.image_media_metadata = temp_model.from_map(m['image_media_metadata'])
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('meta') is not None:
            self.meta = m.get('meta')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parent_file_id') is not None:
            self.parent_file_id = m.get('parent_file_id')
        if m.get('punish_flag') is not None:
            self.punish_flag = m.get('punish_flag')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('starred') is not None:
            self.starred = m.get('starred')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('streams_info') is not None:
            self.streams_info = m.get('streams_info')
        if m.get('thumbnail') is not None:
            self.thumbnail = m.get('thumbnail')
        if m.get('trashed_at') is not None:
            self.trashed_at = m.get('trashed_at')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        if m.get('upload_id') is not None:
            self.upload_id = m.get('upload_id')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('user_meta') is not None:
            self.user_meta = m.get('user_meta')
        if m.get('video_media_metadata') is not None:
            temp_model = VideoMediaResponse()
            self.video_media_metadata = temp_model.from_map(m['video_media_metadata'])
        if m.get('video_preview_metadata') is not None:
            temp_model = VideoPreviewResponse()
            self.video_preview_metadata = temp_model.from_map(m['video_preview_metadata'])
        return self


class GetLastCursorResponse(TeaModel):
    """
    get last file op cursor response
    """
    def __init__(
        self,
        cursor: str = None,
    ):
        self.cursor = cursor

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cursor is not None:
            result['cursor'] = self.cursor
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cursor') is not None:
            self.cursor = m.get('cursor')
        return self


class GetLinkInfoByUserIDRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        user_id: str = None,
    ):
        self.headers = headers
        # user ID
        self.user_id = user_id

    def validate(self):
        self.validate_required(self.user_id, 'user_id')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class GetMediaPlayURLResponse(TeaModel):
    """
    get_media_play_url response
    """
    def __init__(
        self,
        url: str = None,
    ):
        # url
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetOfficeEditUrlResponse(TeaModel):
    """
    获取office文档在线编辑地址 response
    """
    def __init__(
        self,
        edit_url: str = None,
        office_access_token: str = None,
        office_refresh_token: str = None,
    ):
        # EditUrl
        self.edit_url = edit_url
        # AccessToken
        self.office_access_token = office_access_token
        # RefreshToken
        self.office_refresh_token = office_refresh_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.edit_url is not None:
            result['edit_url'] = self.edit_url
        if self.office_access_token is not None:
            result['office_access_token'] = self.office_access_token
        if self.office_refresh_token is not None:
            result['office_refresh_token'] = self.office_refresh_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('edit_url') is not None:
            self.edit_url = m.get('edit_url')
        if m.get('office_access_token') is not None:
            self.office_access_token = m.get('office_access_token')
        if m.get('office_refresh_token') is not None:
            self.office_refresh_token = m.get('office_refresh_token')
        return self


class GetOfficePreviewUrlResponse(TeaModel):
    """
    获取文档预览地址 response
    """
    def __init__(
        self,
        access_token: str = None,
        preview_url: str = None,
    ):
        # AccessToken
        self.access_token = access_token
        # preview_url
        self.preview_url = preview_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.access_token is not None:
            result['access_token'] = self.access_token
        if self.preview_url is not None:
            result['preview_url'] = self.preview_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('access_token') is not None:
            self.access_token = m.get('access_token')
        if m.get('preview_url') is not None:
            self.preview_url = m.get('preview_url')
        return self


class GetPublicKeyRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        app_id: str = None,
    ):
        self.headers = headers
        # App ID
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.app_id is not None:
            result['app_id'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('app_id') is not None:
            self.app_id = m.get('app_id')
        return self


class GetRPVerifyResultRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        user_id: str = None,
    ):
        # User ID, 当前访问的用户
        self.user_id = user_id

    def validate(self):
        self.validate_required(self.user_id, 'user_id')

    def to_map(self):
        result = dict()
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class GetRPVerifyTokenRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        user_id: str = None,
    ):
        # User ID, 当前访问的用户
        self.user_id = user_id

    def validate(self):
        self.validate_required(self.user_id, 'user_id')

    def to_map(self):
        result = dict()
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class GetShareLinkByAnonymousResponse(TeaModel):
    """
    get_share_link_by_anonymous response
    """
    def __init__(
        self,
        avatar: str = None,
        creator_id: str = None,
        creator_name: str = None,
        creator_phone: str = None,
        expiration: str = None,
        share_name: str = None,
        updated_at: str = None,
    ):
        # avatar
        self.avatar = avatar
        # creator_id
        self.creator_id = creator_id
        # creator_name
        self.creator_name = creator_name
        # creator_phone
        self.creator_phone = creator_phone
        # expiration
        self.expiration = expiration
        # share_name
        self.share_name = share_name
        # updated_at
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.avatar is not None:
            result['avatar'] = self.avatar
        if self.creator_id is not None:
            result['creator_id'] = self.creator_id
        if self.creator_name is not None:
            result['creator_name'] = self.creator_name
        if self.creator_phone is not None:
            result['creator_phone'] = self.creator_phone
        if self.expiration is not None:
            result['expiration'] = self.expiration
        if self.share_name is not None:
            result['share_name'] = self.share_name
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('avatar') is not None:
            self.avatar = m.get('avatar')
        if m.get('creator_id') is not None:
            self.creator_id = m.get('creator_id')
        if m.get('creator_name') is not None:
            self.creator_name = m.get('creator_name')
        if m.get('creator_phone') is not None:
            self.creator_phone = m.get('creator_phone')
        if m.get('expiration') is not None:
            self.expiration = m.get('expiration')
        if m.get('share_name') is not None:
            self.share_name = m.get('share_name')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        return self


class GetShareLinkIDResponse(TeaModel):
    """
    get_share_id response
    """
    def __init__(
        self,
        share_id: str = None,
        share_pwd: str = None,
    ):
        # share_id
        self.share_id = share_id
        # share_pwd
        self.share_pwd = share_pwd

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.share_pwd is not None:
            result['share_pwd'] = self.share_pwd
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('share_pwd') is not None:
            self.share_pwd = m.get('share_pwd')
        return self


class GetShareLinkTokenResponse(TeaModel):
    """
    get_share_token response
    """
    def __init__(
        self,
        expire_time: str = None,
        expires_in: int = None,
        share_token: str = None,
    ):
        # expire_time
        self.expire_time = expire_time
        # expires_in
        self.expires_in = expires_in
        # share_token
        self.share_token = share_token

    def validate(self):
        self.validate_required(self.expire_time, 'expire_time')
        self.validate_required(self.expires_in, 'expires_in')
        self.validate_required(self.share_token, 'share_token')

    def to_map(self):
        result = dict()
        if self.expire_time is not None:
            result['expire_time'] = self.expire_time
        if self.expires_in is not None:
            result['expires_in'] = self.expires_in
        if self.share_token is not None:
            result['share_token'] = self.share_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expire_time') is not None:
            self.expire_time = m.get('expire_time')
        if m.get('expires_in') is not None:
            self.expires_in = m.get('expires_in')
        if m.get('share_token') is not None:
            self.share_token = m.get('share_token')
        return self


class GetShareResponse(TeaModel):
    """
    Get share response
    """
    def __init__(
        self,
        created_at: str = None,
        creator: str = None,
        description: str = None,
        domain_id: str = None,
        drive_id: str = None,
        expiration: str = None,
        expired: bool = None,
        owner: str = None,
        owner_type: str = None,
        permissions: List[str] = None,
        share_file_id: str = None,
        share_file_path: str = None,
        share_id: str = None,
        share_name: str = None,
        share_policy: List[SharePermissionPolicy] = None,
        status: str = None,
        updated_at: str = None,
    ):
        # created_at
        self.created_at = created_at
        # creator
        self.creator = creator
        # description
        self.description = description
        # domain_id
        self.domain_id = domain_id
        # drive_id
        self.drive_id = drive_id
        # expiration
        self.expiration = expiration
        # expired
        self.expired = expired
        # owner
        self.owner = owner
        # owner
        self.owner_type = owner_type
        # permissions
        self.permissions = permissions
        # share_file_id
        self.share_file_id = share_file_id
        # share_path
        self.share_file_path = share_file_path
        # share_id
        self.share_id = share_id
        # share_name
        self.share_name = share_name
        self.share_policy = share_policy
        # status
        self.status = status
        # updated_at
        self.updated_at = updated_at

    def validate(self):
        if self.share_policy:
            for k in self.share_policy:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
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
        if self.owner_type is not None:
            result['owner_type'] = self.owner_type
        if self.permissions is not None:
            result['permissions'] = self.permissions
        if self.share_file_id is not None:
            result['share_file_id'] = self.share_file_id
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('expiration') is not None:
            self.expiration = m.get('expiration')
        if m.get('expired') is not None:
            self.expired = m.get('expired')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('owner_type') is not None:
            self.owner_type = m.get('owner_type')
        if m.get('permissions') is not None:
            self.permissions = m.get('permissions')
        if m.get('share_file_id') is not None:
            self.share_file_id = m.get('share_file_id')
        if m.get('share_file_path') is not None:
            self.share_file_path = m.get('share_file_path')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('share_name') is not None:
            self.share_name = m.get('share_name')
        self.share_policy = []
        if m.get('share_policy') is not None:
            for k in m.get('share_policy'):
                temp_model = SharePermissionPolicy()
                self.share_policy.append(temp_model.from_map(k))
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        return self


class GetUploadUrlResponse(TeaModel):
    """
    Get UploadUrl Response
    """
    def __init__(
        self,
        create_at: str = None,
        domain_id: str = None,
        drive_id: str = None,
        file_id: str = None,
        part_info_list: List[UploadPartInfo] = None,
        upload_id: str = None,
    ):
        # created_at
        self.create_at = create_at
        # domain_id
        self.domain_id = domain_id
        # drive_id
        self.drive_id = drive_id
        # file_id
        self.file_id = file_id
        # part_info_list
        self.part_info_list = part_info_list
        # upload_id
        self.upload_id = upload_id

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
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('create_at') is not None:
            self.create_at = m.get('create_at')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        self.part_info_list = []
        if m.get('part_info_list') is not None:
            for k in m.get('part_info_list'):
                temp_model = UploadPartInfo()
                self.part_info_list.append(temp_model.from_map(k))
        if m.get('upload_id') is not None:
            self.upload_id = m.get('upload_id')
        return self


class GetVideoPreviewSpriteURLResponse(TeaModel):
    """
    获取视频雪碧图地址 url response
    """
    def __init__(
        self,
        col: int = None,
        count: int = None,
        frame_count: int = None,
        frame_height: int = None,
        frame_width: int = None,
        row: int = None,
        sprite_url_list: List[str] = None,
    ):
        # col
        self.col = col
        # count
        self.count = count
        # frame_count
        self.frame_count = frame_count
        # frame_height
        self.frame_height = frame_height
        # frame_width
        self.frame_width = frame_width
        # row
        self.row = row
        # sprite_url_list
        self.sprite_url_list = sprite_url_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('col') is not None:
            self.col = m.get('col')
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('frame_count') is not None:
            self.frame_count = m.get('frame_count')
        if m.get('frame_height') is not None:
            self.frame_height = m.get('frame_height')
        if m.get('frame_width') is not None:
            self.frame_width = m.get('frame_width')
        if m.get('row') is not None:
            self.row = m.get('row')
        if m.get('sprite_url_list') is not None:
            self.sprite_url_list = m.get('sprite_url_list')
        return self


class GetVideoPreviewURLResponse(TeaModel):
    """
    获取视频文件播放 url response
    """
    def __init__(
        self,
        preview_url: str = None,
    ):
        # preview_url
        self.preview_url = preview_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.preview_url is not None:
            result['preview_url'] = self.preview_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('preview_url') is not None:
            self.preview_url = m.get('preview_url')
        return self


class HostingCompleteFileResponse(TeaModel):
    """
    complete file response
    """
    def __init__(
        self,
        content_hash: str = None,
        content_hash_name: str = None,
        content_type: str = None,
        crc: str = None,
        crc_64hash: str = None,
        created_at: str = None,
        description: str = None,
        domain_id: str = None,
        download_url: str = None,
        drive_id: str = None,
        file_extension: str = None,
        file_path: str = None,
        name: str = None,
        parent_file_path: str = None,
        share_id: str = None,
        size: int = None,
        status: str = None,
        thumbnail: str = None,
        trashed_at: str = None,
        type: str = None,
        updated_at: str = None,
        upload_id: str = None,
        url: str = None,
    ):
        # Content Hash
        self.content_hash = content_hash
        # content_hash_name
        self.content_hash_name = content_hash_name
        # content_type
        self.content_type = content_type
        # crc
        self.crc = crc
        # crc64_hash
        self.crc_64hash = crc_64hash
        # created_at
        self.created_at = created_at
        # description
        self.description = description
        # domain_id
        self.domain_id = domain_id
        # download_url
        self.download_url = download_url
        # drive_id
        self.drive_id = drive_id
        # file_extension
        self.file_extension = file_extension
        # file_path
        self.file_path = file_path
        # name
        self.name = name
        # parent_file_id
        self.parent_file_path = parent_file_path
        # share_id
        self.share_id = share_id
        # Size
        self.size = size
        # status
        self.status = status
        # thumbnail
        self.thumbnail = thumbnail
        # trashed_at
        self.trashed_at = trashed_at
        # type
        self.type = type
        # updated_at
        self.updated_at = updated_at
        # upload_id
        self.upload_id = upload_id
        # url
        self.url = url

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
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content_hash') is not None:
            self.content_hash = m.get('content_hash')
        if m.get('content_hash_name') is not None:
            self.content_hash_name = m.get('content_hash_name')
        if m.get('content_type') is not None:
            self.content_type = m.get('content_type')
        if m.get('crc') is not None:
            self.crc = m.get('crc')
        if m.get('crc64_hash') is not None:
            self.crc_64hash = m.get('crc64_hash')
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('download_url') is not None:
            self.download_url = m.get('download_url')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_extension') is not None:
            self.file_extension = m.get('file_extension')
        if m.get('file_path') is not None:
            self.file_path = m.get('file_path')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parent_file_path') is not None:
            self.parent_file_path = m.get('parent_file_path')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('thumbnail') is not None:
            self.thumbnail = m.get('thumbnail')
        if m.get('trashed_at') is not None:
            self.trashed_at = m.get('trashed_at')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        if m.get('upload_id') is not None:
            self.upload_id = m.get('upload_id')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class HostingCopyFileResponse(TeaModel):
    """
    文件拷贝 response
    """
    def __init__(
        self,
        async_task_id: str = None,
        domain_id: str = None,
        drive_id: str = None,
        file_path: str = None,
        share_id: str = None,
    ):
        # async_task_id
        self.async_task_id = async_task_id
        # domain_id
        self.domain_id = domain_id
        # drive_id
        self.drive_id = drive_id
        # file_path
        self.file_path = file_path
        # drive_id
        self.share_id = share_id

    def validate(self):
        if self.domain_id is not None:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z-]+')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.share_id is not None:
            self.validate_pattern(self.share_id, 'share_id', '[a-z0-9A-Z]+')

    def to_map(self):
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('async_task_id') is not None:
            self.async_task_id = m.get('async_task_id')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_path') is not None:
            self.file_path = m.get('file_path')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        return self


class HostingCreateFileResponse(TeaModel):
    """
    Create file response
    """
    def __init__(
        self,
        domain_id: str = None,
        drive_id: str = None,
        file_path: str = None,
        part_info_list: List[UploadPartInfo] = None,
        share_id: str = None,
        type: str = None,
        upload_id: str = None,
    ):
        # domain_id
        self.domain_id = domain_id
        # drive_id
        self.drive_id = drive_id
        # file_path
        self.file_path = file_path
        # part_info_list
        self.part_info_list = part_info_list
        # share_id
        self.share_id = share_id
        # type
        self.type = type
        # upload_id
        self.upload_id = upload_id

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
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_path') is not None:
            self.file_path = m.get('file_path')
        self.part_info_list = []
        if m.get('part_info_list') is not None:
            for k in m.get('part_info_list'):
                temp_model = UploadPartInfo()
                self.part_info_list.append(temp_model.from_map(k))
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('upload_id') is not None:
            self.upload_id = m.get('upload_id')
        return self


class HostingDeleteFileResponse(TeaModel):
    """
    删除文件 response
    """
    def __init__(
        self,
        async_task_id: str = None,
        domain_id: str = None,
        drive_id: str = None,
        file_path: str = None,
        share_id: str = None,
    ):
        # async_task_id
        self.async_task_id = async_task_id
        # domain_id
        self.domain_id = domain_id
        # drive_id
        self.drive_id = drive_id
        # file_path
        self.file_path = file_path
        # share_id
        self.share_id = share_id

    def validate(self):
        if self.domain_id is not None:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z]+')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.share_id is not None:
            self.validate_pattern(self.share_id, 'share_id', '[a-z0-9A-Z]+')

    def to_map(self):
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('async_task_id') is not None:
            self.async_task_id = m.get('async_task_id')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_path') is not None:
            self.file_path = m.get('file_path')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        return self


class HostingDeleteFilesResponse(TeaModel):
    """
    批量删除文件 response
    """
    def __init__(
        self,
        deleted_file_id_list: List[str] = None,
        domain_id: str = None,
        drive_id: str = None,
        share_id: str = None,
    ):
        # deleted_file_id_list
        self.deleted_file_id_list = deleted_file_id_list
        # domain_id
        self.domain_id = domain_id
        # drive_id
        self.drive_id = drive_id
        # share_id
        self.share_id = share_id

    def validate(self):
        if self.domain_id is not None:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z]+')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.share_id is not None:
            self.validate_pattern(self.share_id, 'share_id', '[0-9]+')

    def to_map(self):
        result = dict()
        if self.deleted_file_id_list is not None:
            result['deleted_file_id_list'] = self.deleted_file_id_list
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.share_id is not None:
            result['share_id'] = self.share_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deleted_file_id_list') is not None:
            self.deleted_file_id_list = m.get('deleted_file_id_list')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        return self


class HostingGetDownloadUrlResponse(TeaModel):
    """
    获取download url response
    """
    def __init__(
        self,
        expiration: str = None,
        method: str = None,
        url: str = None,
    ):
        # expiration
        self.expiration = expiration
        # method
        self.method = method
        # url
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.expiration is not None:
            result['expiration'] = self.expiration
        if self.method is not None:
            result['method'] = self.method
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expiration') is not None:
            self.expiration = m.get('expiration')
        if m.get('method') is not None:
            self.method = m.get('method')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class HostingGetFileResponse(TeaModel):
    """
    获取文件元数据response
    """
    def __init__(
        self,
        content_hash: str = None,
        content_hash_name: str = None,
        content_type: str = None,
        crc_64hash: str = None,
        created_at: str = None,
        description: str = None,
        domain_id: str = None,
        download_url: str = None,
        drive_id: str = None,
        file_extension: str = None,
        file_path: str = None,
        name: str = None,
        parent_file_path: str = None,
        share_id: str = None,
        size: int = None,
        status: str = None,
        thumbnail: str = None,
        trashed_at: str = None,
        type: str = None,
        updated_at: str = None,
        upload_id: str = None,
        url: str = None,
    ):
        # Content Hash
        self.content_hash = content_hash
        # content_hash_name
        self.content_hash_name = content_hash_name
        # content_type
        self.content_type = content_type
        # crc64_hash
        self.crc_64hash = crc_64hash
        # created_at
        self.created_at = created_at
        # description
        self.description = description
        # domain_id
        self.domain_id = domain_id
        # download_url
        self.download_url = download_url
        # drive_id
        self.drive_id = drive_id
        # file_extension
        self.file_extension = file_extension
        # file_path
        self.file_path = file_path
        # name
        self.name = name
        # parent_file_id
        self.parent_file_path = parent_file_path
        # share_id
        self.share_id = share_id
        # Size
        self.size = size
        # status
        self.status = status
        # thumbnail
        self.thumbnail = thumbnail
        # trashed_at
        self.trashed_at = trashed_at
        # type
        self.type = type
        # updated_at
        self.updated_at = updated_at
        # upload_id
        self.upload_id = upload_id
        # url
        self.url = url

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
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content_hash') is not None:
            self.content_hash = m.get('content_hash')
        if m.get('content_hash_name') is not None:
            self.content_hash_name = m.get('content_hash_name')
        if m.get('content_type') is not None:
            self.content_type = m.get('content_type')
        if m.get('crc64_hash') is not None:
            self.crc_64hash = m.get('crc64_hash')
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('download_url') is not None:
            self.download_url = m.get('download_url')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_extension') is not None:
            self.file_extension = m.get('file_extension')
        if m.get('file_path') is not None:
            self.file_path = m.get('file_path')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parent_file_path') is not None:
            self.parent_file_path = m.get('parent_file_path')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('thumbnail') is not None:
            self.thumbnail = m.get('thumbnail')
        if m.get('trashed_at') is not None:
            self.trashed_at = m.get('trashed_at')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        if m.get('upload_id') is not None:
            self.upload_id = m.get('upload_id')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class HostingGetSecureUrlResponse(TeaModel):
    """
    获取secure url response
    """
    def __init__(
        self,
        expiration: str = None,
        url: str = None,
    ):
        # expiration
        self.expiration = expiration
        # url
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.expiration is not None:
            result['expiration'] = self.expiration
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expiration') is not None:
            self.expiration = m.get('expiration')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class HostingGetUploadUrlResponse(TeaModel):
    """
    Get UploadUrl Response
    """
    def __init__(
        self,
        create_at: str = None,
        domain_id: str = None,
        drive_id: str = None,
        file_path: str = None,
        part_info_list: List[UploadPartInfo] = None,
        upload_id: str = None,
    ):
        # created_at
        self.create_at = create_at
        # domain_id
        self.domain_id = domain_id
        # drive_id
        self.drive_id = drive_id
        # file_path
        self.file_path = file_path
        # part_info_list
        self.part_info_list = part_info_list
        # upload_id
        self.upload_id = upload_id

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
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('create_at') is not None:
            self.create_at = m.get('create_at')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_path') is not None:
            self.file_path = m.get('file_path')
        self.part_info_list = []
        if m.get('part_info_list') is not None:
            for k in m.get('part_info_list'):
                temp_model = UploadPartInfo()
                self.part_info_list.append(temp_model.from_map(k))
        if m.get('upload_id') is not None:
            self.upload_id = m.get('upload_id')
        return self


class HostingListFileResponse(TeaModel):
    """
    List file response
    """
    def __init__(
        self,
        items: List[BaseHostingFileResponse] = None,
        next_marker: str = None,
    ):
        # items
        self.items = items
        # next_marker
        self.next_marker = next_marker

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = BaseHostingFileResponse()
                self.items.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        return self


class HostingListUploadedPartResponse(TeaModel):
    """
    获取签名 response
    """
    def __init__(
        self,
        file_path: str = None,
        next_part_number_marker: str = None,
        upload_id: str = None,
        uploaded_parts: List[UploadPartInfo] = None,
    ):
        # file_path
        self.file_path = file_path
        # next_part_number_marker
        self.next_part_number_marker = next_part_number_marker
        # upload_id
        self.upload_id = upload_id
        # uploaded_parts
        self.uploaded_parts = uploaded_parts

    def validate(self):
        if self.uploaded_parts:
            for k in self.uploaded_parts:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('file_path') is not None:
            self.file_path = m.get('file_path')
        if m.get('next_part_number_marker') is not None:
            self.next_part_number_marker = m.get('next_part_number_marker')
        if m.get('upload_id') is not None:
            self.upload_id = m.get('upload_id')
        self.uploaded_parts = []
        if m.get('uploaded_parts') is not None:
            for k in m.get('uploaded_parts'):
                temp_model = UploadPartInfo()
                self.uploaded_parts.append(temp_model.from_map(k))
        return self


class HostingMoveFileResponse(TeaModel):
    """
    文件移动 response
    """
    def __init__(
        self,
        async_task_id: str = None,
        domain_id: str = None,
        drive_id: str = None,
        file_path: str = None,
        share_id: str = None,
    ):
        # async_task_id
        self.async_task_id = async_task_id
        # domain_id
        self.domain_id = domain_id
        # drive_id
        self.drive_id = drive_id
        # file_path
        self.file_path = file_path
        # drive_id
        self.share_id = share_id

    def validate(self):
        if self.domain_id is not None:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z-]+')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.share_id is not None:
            self.validate_pattern(self.share_id, 'share_id', '[a-z0-9A-Z]+')

    def to_map(self):
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('async_task_id') is not None:
            self.async_task_id = m.get('async_task_id')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_path') is not None:
            self.file_path = m.get('file_path')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        return self


class HostingSearchFileResponse(TeaModel):
    """
    search file response
    """
    def __init__(
        self,
        items: List[BaseHostingFileResponse] = None,
        next_marker: str = None,
    ):
        # items
        self.items = items
        # next_marker
        self.next_marker = next_marker

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = BaseHostingFileResponse()
                self.items.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        return self


class HostingUpdateFileMetaResponse(TeaModel):
    """
    更新文件元数据 response
    """
    def __init__(
        self,
        content_hash: str = None,
        content_hash_name: str = None,
        content_type: str = None,
        crc_64hash: str = None,
        created_at: str = None,
        description: str = None,
        domain_id: str = None,
        download_url: str = None,
        drive_id: str = None,
        file_extension: str = None,
        file_path: str = None,
        name: str = None,
        parent_file_path: str = None,
        share_id: str = None,
        size: int = None,
        status: str = None,
        thumbnail: str = None,
        trashed_at: str = None,
        type: str = None,
        updated_at: str = None,
        upload_id: str = None,
        url: str = None,
    ):
        # Content Hash
        self.content_hash = content_hash
        # content_hash_name
        self.content_hash_name = content_hash_name
        # content_type
        self.content_type = content_type
        # crc64_hash
        self.crc_64hash = crc_64hash
        # created_at
        self.created_at = created_at
        # description
        self.description = description
        # domain_id
        self.domain_id = domain_id
        # download_url
        self.download_url = download_url
        # drive_id
        self.drive_id = drive_id
        # file_extension
        self.file_extension = file_extension
        # file_path
        self.file_path = file_path
        # name
        self.name = name
        # parent_file_id
        self.parent_file_path = parent_file_path
        # share_id
        self.share_id = share_id
        # Size
        self.size = size
        # status
        self.status = status
        # thumbnail
        self.thumbnail = thumbnail
        # trashed_at
        self.trashed_at = trashed_at
        # type
        self.type = type
        # updated_at
        self.updated_at = updated_at
        # upload_id
        self.upload_id = upload_id
        # url
        self.url = url

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
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content_hash') is not None:
            self.content_hash = m.get('content_hash')
        if m.get('content_hash_name') is not None:
            self.content_hash_name = m.get('content_hash_name')
        if m.get('content_type') is not None:
            self.content_type = m.get('content_type')
        if m.get('crc64_hash') is not None:
            self.crc_64hash = m.get('crc64_hash')
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('download_url') is not None:
            self.download_url = m.get('download_url')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_extension') is not None:
            self.file_extension = m.get('file_extension')
        if m.get('file_path') is not None:
            self.file_path = m.get('file_path')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parent_file_path') is not None:
            self.parent_file_path = m.get('parent_file_path')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('thumbnail') is not None:
            self.thumbnail = m.get('thumbnail')
        if m.get('trashed_at') is not None:
            self.trashed_at = m.get('trashed_at')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        if m.get('upload_id') is not None:
            self.upload_id = m.get('upload_id')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class HostingVideoDRMLicenseResponse(TeaModel):
    """
    DRM License response
    """
    def __init__(
        self,
        data: str = None,
        device_info: str = None,
        states: int = None,
    ):
        # drm_data
        self.data = data
        # device_info
        self.device_info = device_info
        # states
        self.states = states

    def validate(self):
        self.validate_required(self.data, 'data')
        self.validate_required(self.device_info, 'device_info')
        self.validate_required(self.states, 'states')

    def to_map(self):
        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.device_info is not None:
            result['device_info'] = self.device_info
        if self.states is not None:
            result['states'] = self.states
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('device_info') is not None:
            self.device_info = m.get('device_info')
        if m.get('states') is not None:
            self.states = m.get('states')
        return self


class HostingVideoDefinitionResponse(TeaModel):
    """
    转码接口response
    """
    def __init__(
        self,
        definition_list: List[str] = None,
        frame_rate: str = None,
    ):
        # definition_list
        self.definition_list = definition_list
        # frame_rate
        self.frame_rate = frame_rate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.definition_list is not None:
            result['definition_list'] = self.definition_list
        if self.frame_rate is not None:
            result['frame_rate'] = self.frame_rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('definition_list') is not None:
            self.definition_list = m.get('definition_list')
        if m.get('frame_rate') is not None:
            self.frame_rate = m.get('frame_rate')
        return self


class HostingVideoTranscodeResponse(TeaModel):
    """
    转码接口response
    """
    def __init__(
        self,
        definition_list: List[str] = None,
        duration: int = None,
        hls_time: int = None,
    ):
        # definition_list
        self.definition_list = definition_list
        # duration
        self.duration = duration
        # hls_time
        self.hls_time = hls_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.definition_list is not None:
            result['definition_list'] = self.definition_list
        if self.duration is not None:
            result['duration'] = self.duration
        if self.hls_time is not None:
            result['hls_time'] = self.hls_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('definition_list') is not None:
            self.definition_list = m.get('definition_list')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('hls_time') is not None:
            self.hls_time = m.get('hls_time')
        return self


class ListAppsRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        limit: int = None,
        marker: str = None,
    ):
        # 返回结果数据
        self.limit = limit
        # 下次查询游标
        self.marker = marker

    def validate(self):
        if self.limit is not None:
            self.validate_maximum(self.limit, 'limit', 100)
            self.validate_minimum(self.limit, 'limit', 1)

    def to_map(self):
        result = dict()
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        return self


class ListByAnonymousResponse(TeaModel):
    """
    list_file_by_anonymous response
    """
    def __init__(
        self,
        items: List[BaseFileAnonymousResponse] = None,
        next_marker: str = None,
    ):
        # items
        self.items = items
        # next_marker
        self.next_marker = next_marker

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = BaseFileAnonymousResponse()
                self.items.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        return self


class ListDomainsRequest(TeaModel):
    """
    list domain request
    """
    def __init__(
        self,
        limit: int = None,
        marker: str = None,
    ):
        # 分页大小
        self.limit = limit
        # 查询游标
        self.marker = marker

    def validate(self):
        if self.limit is not None:
            self.validate_maximum(self.limit, 'limit', 100)
            self.validate_minimum(self.limit, 'limit', 1)

    def to_map(self):
        result = dict()
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        return self


class ListDriveResponse(TeaModel):
    """
    list drive response
    """
    def __init__(
        self,
        items: List[BaseDriveResponse] = None,
        next_marker: str = None,
    ):
        # Drive 列表
        self.items = items
        # 翻页标记
        self.next_marker = next_marker

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = BaseDriveResponse()
                self.items.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        return self


class ListFileDeltaResponse(TeaModel):
    """
    list file op response
    """
    def __init__(
        self,
        cursor: str = None,
        has_more: bool = None,
        items: List[FileDeltaResponse] = None,
    ):
        # cursor
        self.cursor = cursor
        # has_more
        self.has_more = has_more
        # items
        self.items = items

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.cursor is not None:
            result['cursor'] = self.cursor
        if self.has_more is not None:
            result['has_more'] = self.has_more
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cursor') is not None:
            self.cursor = m.get('cursor')
        if m.get('has_more') is not None:
            self.has_more = m.get('has_more')
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = FileDeltaResponse()
                self.items.append(temp_model.from_map(k))
        return self


class ListFileResponse(TeaModel):
    """
    List file response
    """
    def __init__(
        self,
        items: List[BaseCCPFileResponse] = None,
        next_marker: str = None,
    ):
        # items
        self.items = items
        # next_marker
        self.next_marker = next_marker

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = BaseCCPFileResponse()
                self.items.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        return self


class ListShareLinkResponse(TeaModel):
    """
    list_share_link response
    """
    def __init__(
        self,
        items: List[BaseShareLinkResponse] = None,
        next_marker: str = None,
    ):
        # items
        self.items = items
        # next_marker
        self.next_marker = next_marker

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = BaseShareLinkResponse()
                self.items.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        return self


class ListShareResponse(TeaModel):
    """
    List share response
    """
    def __init__(
        self,
        items: List[BaseShareResponse] = None,
        next_marker: str = None,
    ):
        # items
        self.items = items
        # next_marker
        self.next_marker = next_marker

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = BaseShareResponse()
                self.items.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        return self


class StoreFile(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        domain_id: str = None,
        name: str = None,
        parent_file_path: str = None,
        store_id: str = None,
        type: str = None,
    ):
        self.domain_id = domain_id
        self.name = name
        self.parent_file_path = parent_file_path
        self.store_id = store_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parent_file_path') is not None:
            self.parent_file_path = m.get('parent_file_path')
        if m.get('store_id') is not None:
            self.store_id = m.get('store_id')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListStoreFileResponse(TeaModel):
    """
    List storage file
    """
    def __init__(
        self,
        items: List[StoreFile] = None,
        next_marker: str = None,
    ):
        # items
        # file list
        self.items = items
        self.next_marker = next_marker

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = StoreFile()
                self.items.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        return self


class StoreItemResponse(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        accelerate_endpoint: str = None,
        base_path: str = None,
        bucket: str = None,
        cdn_endpoint: str = None,
        customized_accelerate_endpoint: str = None,
        customized_cdn_endpoint: str = None,
        customized_endpoint: str = None,
        customized_internal_endpoint: str = None,
        domain_id: str = None,
        endpoint: str = None,
        internal_endpoint: str = None,
        location: str = None,
        ownership: str = None,
        policy: str = None,
        role_arn: str = None,
        store_id: str = None,
        type: str = None,
    ):
        # 全球加速地址
        self.accelerate_endpoint = accelerate_endpoint
        # 存储公共前缀
        self.base_path = base_path
        # bucket名称
        self.bucket = bucket
        # 内容分发地址
        self.cdn_endpoint = cdn_endpoint
        # 自定义全球加速地址
        self.customized_accelerate_endpoint = customized_accelerate_endpoint
        # 自定义内容分发地址
        self.customized_cdn_endpoint = customized_cdn_endpoint
        # 自定义Public访问地址
        self.customized_endpoint = customized_endpoint
        # 自定义vpc访问地址
        self.customized_internal_endpoint = customized_internal_endpoint
        self.domain_id = domain_id
        # Public访问地址
        self.endpoint = endpoint
        # vpc访问地址
        self.internal_endpoint = internal_endpoint
        # 地点
        self.location = location
        # 存储归属，system表示系统提供，custom表示使用自己的存储
        self.ownership = ownership
        # Policy授权,system类型store会将bucket权限授予当前云账号
        self.policy = policy
        # 访问Bucket的角色ARN
        self.role_arn = role_arn
        # store ID
        self.store_id = store_id
        # 存储类型，当前只支持oss
        self.type = type

    def validate(self):
        self.validate_required(self.bucket, 'bucket')
        self.validate_required(self.endpoint, 'endpoint')
        self.validate_required(self.ownership, 'ownership')
        self.validate_required(self.policy, 'policy')
        self.validate_required(self.store_id, 'store_id')
        self.validate_required(self.type, 'type')

    def to_map(self):
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accelerate_endpoint') is not None:
            self.accelerate_endpoint = m.get('accelerate_endpoint')
        if m.get('base_path') is not None:
            self.base_path = m.get('base_path')
        if m.get('bucket') is not None:
            self.bucket = m.get('bucket')
        if m.get('cdn_endpoint') is not None:
            self.cdn_endpoint = m.get('cdn_endpoint')
        if m.get('customized_accelerate_endpoint') is not None:
            self.customized_accelerate_endpoint = m.get('customized_accelerate_endpoint')
        if m.get('customized_cdn_endpoint') is not None:
            self.customized_cdn_endpoint = m.get('customized_cdn_endpoint')
        if m.get('customized_endpoint') is not None:
            self.customized_endpoint = m.get('customized_endpoint')
        if m.get('customized_internal_endpoint') is not None:
            self.customized_internal_endpoint = m.get('customized_internal_endpoint')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('internal_endpoint') is not None:
            self.internal_endpoint = m.get('internal_endpoint')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('ownership') is not None:
            self.ownership = m.get('ownership')
        if m.get('policy') is not None:
            self.policy = m.get('policy')
        if m.get('role_arn') is not None:
            self.role_arn = m.get('role_arn')
        if m.get('store_id') is not None:
            self.store_id = m.get('store_id')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListStoreResponse(TeaModel):
    """
    List storage
    """
    def __init__(
        self,
        items: List[StoreItemResponse] = None,
    ):
        # items
        self.items = items

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = StoreItemResponse()
                self.items.append(temp_model.from_map(k))
        return self


class ListStoresRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        domain_id: str = None,
    ):
        # domain ID
        self.domain_id = domain_id

    def validate(self):
        self.validate_required(self.domain_id, 'domain_id')

    def to_map(self):
        result = dict()
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        return self


class ListUploadedPartResponse(TeaModel):
    """
    获取签名 response
    """
    def __init__(
        self,
        file_id: str = None,
        next_part_number_marker: str = None,
        upload_id: str = None,
        uploaded_parts: List[UploadPartInfo] = None,
    ):
        # file_id
        self.file_id = file_id
        # next_part_number_marker
        self.next_part_number_marker = next_part_number_marker
        # upload_id
        self.upload_id = upload_id
        # uploaded_parts
        self.uploaded_parts = uploaded_parts

    def validate(self):
        if self.file_id is not None:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9]{1,50}')
        if self.uploaded_parts:
            for k in self.uploaded_parts:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('next_part_number_marker') is not None:
            self.next_part_number_marker = m.get('next_part_number_marker')
        if m.get('upload_id') is not None:
            self.upload_id = m.get('upload_id')
        self.uploaded_parts = []
        if m.get('uploaded_parts') is not None:
            for k in m.get('uploaded_parts'):
                temp_model = UploadPartInfo()
                self.uploaded_parts.append(temp_model.from_map(k))
        return self


class LoginByCodeRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        access_token: str = None,
        app_id: str = None,
        auth_code: str = None,
        type: str = None,
    ):
        # 鉴权后返回的accessToken，淘宝登录需要此字段
        self.access_token = access_token
        # App ID, 当前访问的App
        self.app_id = app_id
        # 鉴权后返回的AuthCode，支付宝登录需要此字段
        self.auth_code = auth_code
        # 鉴权类型，淘宝、支付宝
        self.type = type

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.type, 'type')

    def to_map(self):
        result = dict()
        if self.access_token is not None:
            result['access_token'] = self.access_token
        if self.app_id is not None:
            result['app_id'] = self.app_id
        if self.auth_code is not None:
            result['auth_code'] = self.auth_code
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('access_token') is not None:
            self.access_token = m.get('access_token')
        if m.get('app_id') is not None:
            self.app_id = m.get('app_id')
        if m.get('auth_code') is not None:
            self.auth_code = m.get('auth_code')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class LogoutRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        back_url: str = None,
        client_id: str = None,
        login_type: str = None,
    ):
        # 登出之后的跳转地址，默认跳转到App的域名下
        self.back_url = back_url
        # Client ID, 此处填写创建App时返回的AppID
        self.client_id = client_id
        # 用户自定义字段，会在鉴权成功后的callback带回
        self.login_type = login_type

    def validate(self):
        self.validate_required(self.client_id, 'client_id')

    def to_map(self):
        result = dict()
        if self.back_url is not None:
            result['BackUrl'] = self.back_url
        if self.client_id is not None:
            result['ClientID'] = self.client_id
        if self.login_type is not None:
            result['LoginType'] = self.login_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackUrl') is not None:
            self.back_url = m.get('BackUrl')
        if m.get('ClientID') is not None:
            self.client_id = m.get('ClientID')
        if m.get('LoginType') is not None:
            self.login_type = m.get('LoginType')
        return self


class MobileCheckExistRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        app_id: str = None,
        phone_number: str = None,
        phone_region: str = None,
    ):
        self.headers = headers
        # App ID, 当前访问的App
        self.app_id = app_id
        # 待查询的手机号
        self.phone_number = phone_number
        # 国家编号，默认86，不需要填+号，直接填数字
        self.phone_region = phone_region

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.phone_number, 'phone_number')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.app_id is not None:
            result['app_id'] = self.app_id
        if self.phone_number is not None:
            result['phone_number'] = self.phone_number
        if self.phone_region is not None:
            result['phone_region'] = self.phone_region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('app_id') is not None:
            self.app_id = m.get('app_id')
        if m.get('phone_number') is not None:
            self.phone_number = m.get('phone_number')
        if m.get('phone_region') is not None:
            self.phone_region = m.get('phone_region')
        return self


class MobileLoginRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        app_id: str = None,
        auto_register: bool = None,
        captcha_id: str = None,
        captcha_text: str = None,
        encrypted_key: str = None,
        nvc_param: str = None,
        password: str = None,
        phone_number: str = None,
        phone_region: str = None,
        sms_code: str = None,
        sms_code_id: str = None,
    ):
        self.headers = headers
        # App ID, 当前访问的App
        self.app_id = app_id
        # 是否自动注册用户，使用密码登录此参数不生效
        self.auto_register = auto_register
        # 图片验证码ID, 密码登录需要此参数
        self.captcha_id = captcha_id
        # 用户输入的验证码值, 密码登录需要此参数
        self.captcha_text = captcha_text
        # AES-256对称加密密钥，通过App公钥加密后传输
        self.encrypted_key = encrypted_key
        # 环境参数
        self.nvc_param = nvc_param
        # 登录密码, 传入此参数则忽略短信验证码，不传此参数则默认使用短信登录。
        self.password = password
        # 待查询的手机号
        self.phone_number = phone_number
        # 国家编号，默认86，不需要填+号，直接填数字
        self.phone_region = phone_region
        # 短信验证码内容，使用密码登录此参数不生效
        self.sms_code = sms_code
        # 短信验证码ID，使用密码登录此参数不生效
        self.sms_code_id = sms_code_id

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.nvc_param, 'nvc_param')
        self.validate_required(self.phone_number, 'phone_number')

    def to_map(self):
        result = dict()
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
        if self.nvc_param is not None:
            result['nvc_param'] = self.nvc_param
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('app_id') is not None:
            self.app_id = m.get('app_id')
        if m.get('auto_register') is not None:
            self.auto_register = m.get('auto_register')
        if m.get('captcha_id') is not None:
            self.captcha_id = m.get('captcha_id')
        if m.get('captcha_text') is not None:
            self.captcha_text = m.get('captcha_text')
        if m.get('encrypted_key') is not None:
            self.encrypted_key = m.get('encrypted_key')
        if m.get('nvc_param') is not None:
            self.nvc_param = m.get('nvc_param')
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('phone_number') is not None:
            self.phone_number = m.get('phone_number')
        if m.get('phone_region') is not None:
            self.phone_region = m.get('phone_region')
        if m.get('sms_code') is not None:
            self.sms_code = m.get('sms_code')
        if m.get('sms_code_id') is not None:
            self.sms_code_id = m.get('sms_code_id')
        return self


class MobileRegisterRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        app_id: str = None,
        nvc_param: str = None,
        phone_number: str = None,
        phone_region: str = None,
        sms_code: str = None,
        sms_code_id: str = None,
    ):
        self.headers = headers
        # App ID, 当前访问的App
        self.app_id = app_id
        # 环境参数
        self.nvc_param = nvc_param
        # 待查询的手机号
        self.phone_number = phone_number
        # 国家编号，默认86，不需要填+号，直接填数字
        self.phone_region = phone_region
        # 短信验证码内容
        self.sms_code = sms_code
        # 短信验证码ID
        self.sms_code_id = sms_code_id

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.nvc_param, 'nvc_param')
        self.validate_required(self.phone_number, 'phone_number')
        self.validate_required(self.sms_code, 'sms_code')
        self.validate_required(self.sms_code_id, 'sms_code_id')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.app_id is not None:
            result['app_id'] = self.app_id
        if self.nvc_param is not None:
            result['nvc_param'] = self.nvc_param
        if self.phone_number is not None:
            result['phone_number'] = self.phone_number
        if self.phone_region is not None:
            result['phone_region'] = self.phone_region
        if self.sms_code is not None:
            result['sms_code'] = self.sms_code
        if self.sms_code_id is not None:
            result['sms_code_id'] = self.sms_code_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('app_id') is not None:
            self.app_id = m.get('app_id')
        if m.get('nvc_param') is not None:
            self.nvc_param = m.get('nvc_param')
        if m.get('phone_number') is not None:
            self.phone_number = m.get('phone_number')
        if m.get('phone_region') is not None:
            self.phone_region = m.get('phone_region')
        if m.get('sms_code') is not None:
            self.sms_code = m.get('sms_code')
        if m.get('sms_code_id') is not None:
            self.sms_code_id = m.get('sms_code_id')
        return self


class MobileSendSmsCodeRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        app_id: str = None,
        captcha_id: str = None,
        captcha_text: str = None,
        nvc_param: str = None,
        phone_number: str = None,
        phone_region: str = None,
        type: str = None,
    ):
        self.headers = headers
        # App ID, 当前访问的App
        self.app_id = app_id
        # 图片验证码ID
        self.captcha_id = captcha_id
        # 用户输入的验证码值
        self.captcha_text = captcha_text
        # 环境参数
        self.nvc_param = nvc_param
        # 待发送验证短信的手机号
        self.phone_number = phone_number
        # 国家编号，默认86，不需要填+号，直接填数字
        self.phone_region = phone_region
        # 验证码用途, 可下发: login、register、change_password
        self.type = type

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.nvc_param, 'nvc_param')
        self.validate_required(self.phone_number, 'phone_number')
        self.validate_required(self.type, 'type')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.app_id is not None:
            result['app_id'] = self.app_id
        if self.captcha_id is not None:
            result['captcha_id'] = self.captcha_id
        if self.captcha_text is not None:
            result['captcha_text'] = self.captcha_text
        if self.nvc_param is not None:
            result['nvc_param'] = self.nvc_param
        if self.phone_number is not None:
            result['phone_number'] = self.phone_number
        if self.phone_region is not None:
            result['phone_region'] = self.phone_region
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('app_id') is not None:
            self.app_id = m.get('app_id')
        if m.get('captcha_id') is not None:
            self.captcha_id = m.get('captcha_id')
        if m.get('captcha_text') is not None:
            self.captcha_text = m.get('captcha_text')
        if m.get('nvc_param') is not None:
            self.nvc_param = m.get('nvc_param')
        if m.get('phone_number') is not None:
            self.phone_number = m.get('phone_number')
        if m.get('phone_region') is not None:
            self.phone_region = m.get('phone_region')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class MoveFileResponse(TeaModel):
    """
    文件移动 response
    """
    def __init__(
        self,
        async_task_id: str = None,
        domain_id: str = None,
        drive_id: str = None,
        file_id: str = None,
    ):
        # async_task_id
        self.async_task_id = async_task_id
        # DomainID
        self.domain_id = domain_id
        # drive_id
        self.drive_id = drive_id
        # file_id
        self.file_id = file_id

    def validate(self):
        if self.domain_id is not None:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z]+')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.file_id is not None:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9]{1,50}')

    def to_map(self):
        result = dict()
        if self.async_task_id is not None:
            result['async_task_id'] = self.async_task_id
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('async_task_id') is not None:
            self.async_task_id = m.get('async_task_id')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        return self


class PreHashCheckSuccessResponse(TeaModel):
    """
    Pre hash check Response
    """
    def __init__(
        self,
        code: str = None,
        file_name: str = None,
        message: str = None,
        parent_file_id: str = None,
        pre_hash: str = None,
    ):
        # code
        self.code = code
        # file_name
        self.file_name = file_name
        # message
        self.message = message
        # parent_file_id
        self.parent_file_id = parent_file_id
        # pre_hash
        self.pre_hash = pre_hash

    def validate(self):
        self.validate_required(self.parent_file_id, 'parent_file_id')
        if self.parent_file_id is not None:
            self.validate_max_length(self.parent_file_id, 'parent_file_id', 50)
            self.validate_pattern(self.parent_file_id, 'parent_file_id', '[a-z0-9]{1,50}')

    def to_map(self):
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('file_name') is not None:
            self.file_name = m.get('file_name')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('parent_file_id') is not None:
            self.parent_file_id = m.get('parent_file_id')
        if m.get('pre_hash') is not None:
            self.pre_hash = m.get('pre_hash')
        return self


class VerifyTokenResponse(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        token: str = None,
        ttl: int = None,
        url: str = None,
    ):
        # 实人认证的Token
        self.token = token
        # 实人认证token有效秒数，如1800
        self.ttl = ttl
        # 实人认证的URL，包含Token
        self.url = url

    def validate(self):
        self.validate_required(self.token, 'token')
        self.validate_required(self.ttl, 'ttl')
        self.validate_required(self.url, 'url')

    def to_map(self):
        result = dict()
        if self.token is not None:
            result['token'] = self.token
        if self.ttl is not None:
            result['ttl'] = self.ttl
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('token') is not None:
            self.token = m.get('token')
        if m.get('ttl') is not None:
            self.ttl = m.get('ttl')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class RPVerifyTokenResponse(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        need_rp_verify: bool = None,
        verify_token: VerifyTokenResponse = None,
    ):
        # 是否需要实人认证，如果用户已通过认证，或者未开启实人认证，返回false
        self.need_rp_verify = need_rp_verify
        self.verify_token = verify_token

    def validate(self):
        self.validate_required(self.need_rp_verify, 'need_rp_verify')
        self.validate_required(self.verify_token, 'verify_token')
        if self.verify_token:
            self.verify_token.validate()

    def to_map(self):
        result = dict()
        if self.need_rp_verify is not None:
            result['need_rp_verify'] = self.need_rp_verify
        if self.verify_token is not None:
            result['verify_token'] = self.verify_token.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('need_rp_verify') is not None:
            self.need_rp_verify = m.get('need_rp_verify')
        if m.get('verify_token') is not None:
            temp_model = VerifyTokenResponse()
            self.verify_token = temp_model.from_map(m['verify_token'])
        return self


class RefreshOfficeEditTokenResponse(TeaModel):
    """
    刷新office文档在线编辑凭证 response
    """
    def __init__(
        self,
        office_access_token: str = None,
        office_refresh_token: str = None,
    ):
        # AccessToken
        self.office_access_token = office_access_token
        # RefreshToken
        self.office_refresh_token = office_refresh_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.office_access_token is not None:
            result['office_access_token'] = self.office_access_token
        if self.office_refresh_token is not None:
            result['office_refresh_token'] = self.office_refresh_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('office_access_token') is not None:
            self.office_access_token = m.get('office_access_token')
        if m.get('office_refresh_token') is not None:
            self.office_refresh_token = m.get('office_refresh_token')
        return self


class RemoveStoreRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        domain_id: str = None,
        store_id: str = None,
    ):
        # domain ID
        self.domain_id = domain_id
        # store ID
        self.store_id = store_id

    def validate(self):
        self.validate_required(self.domain_id, 'domain_id')
        self.validate_required(self.store_id, 'store_id')

    def to_map(self):
        result = dict()
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.store_id is not None:
            result['store_id'] = self.store_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('store_id') is not None:
            self.store_id = m.get('store_id')
        return self


class RevokeRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        app_id: str = None,
        refresh_token: str = None,
    ):
        self.headers = headers
        # App ID, 当前访问的App
        self.app_id = app_id
        # refresh token, 登录时返回的
        self.refresh_token = refresh_token

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.refresh_token, 'refresh_token')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.app_id is not None:
            result['app_id'] = self.app_id
        if self.refresh_token is not None:
            result['refresh_token'] = self.refresh_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('app_id') is not None:
            self.app_id = m.get('app_id')
        if m.get('refresh_token') is not None:
            self.refresh_token = m.get('refresh_token')
        return self


class ScanFileMetaResponse(TeaModel):
    """
    scan file meta response
    """
    def __init__(
        self,
        items: List[BaseCCPFileResponse] = None,
        next_marker: str = None,
    ):
        # items
        self.items = items
        # next_marker
        self.next_marker = next_marker

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = BaseCCPFileResponse()
                self.items.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        return self


class SearchFileResponse(TeaModel):
    """
    search file response
    """
    def __init__(
        self,
        items: List[BaseCCPFileResponse] = None,
        next_marker: str = None,
        total_count: int = None,
    ):
        # items
        self.items = items
        # next_marker
        self.next_marker = next_marker
        # total_count
        self.total_count = total_count

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        if self.total_count is not None:
            result['total_count'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = BaseCCPFileResponse()
                self.items.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        if m.get('total_count') is not None:
            self.total_count = m.get('total_count')
        return self


class SetAppPublicKeyRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        app_id: str = None,
        public_key: str = None,
    ):
        # App ID
        self.app_id = app_id
        # RSA加密算法的公钥, PEM格式
        self.public_key = public_key

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.public_key, 'public_key')

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['app_id'] = self.app_id
        if self.public_key is not None:
            result['public_key'] = self.public_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('app_id') is not None:
            self.app_id = m.get('app_id')
        if m.get('public_key') is not None:
            self.public_key = m.get('public_key')
        return self


class SetBizCNameCertRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        cert_id: str = None,
        biz_cname: str = None,
        cert_body: str = None,
        cert_name: str = None,
        cert_privatekey: str = None,
        cname_type: str = None,
        domain_id: str = None,
        is_vpc: bool = None,
    ):
        self.cert_id = cert_id
        # biz cname
        self.biz_cname = biz_cname
        # cert body
        self.cert_body = cert_body
        # cert name
        self.cert_name = cert_name
        # cert privatekey
        self.cert_privatekey = cert_privatekey
        # cname type
        self.cname_type = cname_type
        # domain ID
        self.domain_id = domain_id
        # biz cname
        self.is_vpc = is_vpc

    def validate(self):
        self.validate_required(self.cert_body, 'cert_body')
        self.validate_required(self.cert_name, 'cert_name')
        self.validate_required(self.cert_privatekey, 'cert_privatekey')
        self.validate_required(self.cname_type, 'cname_type')
        self.validate_required(self.domain_id, 'domain_id')

    def to_map(self):
        result = dict()
        if self.cert_id is not None:
            result['CertID'] = self.cert_id
        if self.biz_cname is not None:
            result['biz_cname'] = self.biz_cname
        if self.cert_body is not None:
            result['cert_body'] = self.cert_body
        if self.cert_name is not None:
            result['cert_name'] = self.cert_name
        if self.cert_privatekey is not None:
            result['cert_privatekey'] = self.cert_privatekey
        if self.cname_type is not None:
            result['cname_type'] = self.cname_type
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.is_vpc is not None:
            result['is_vpc'] = self.is_vpc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertID') is not None:
            self.cert_id = m.get('CertID')
        if m.get('biz_cname') is not None:
            self.biz_cname = m.get('biz_cname')
        if m.get('cert_body') is not None:
            self.cert_body = m.get('cert_body')
        if m.get('cert_name') is not None:
            self.cert_name = m.get('cert_name')
        if m.get('cert_privatekey') is not None:
            self.cert_privatekey = m.get('cert_privatekey')
        if m.get('cname_type') is not None:
            self.cname_type = m.get('cname_type')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('is_vpc') is not None:
            self.is_vpc = m.get('is_vpc')
        return self


class SetBizCNameRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        biz_cname: str = None,
        cname_type: str = None,
        domain_id: str = None,
        is_vpc: bool = None,
    ):
        # biz cname
        self.biz_cname = biz_cname
        # cname type
        self.cname_type = cname_type
        # domain ID
        self.domain_id = domain_id
        # biz cname
        self.is_vpc = is_vpc

    def validate(self):
        self.validate_required(self.biz_cname, 'biz_cname')
        self.validate_required(self.cname_type, 'cname_type')
        self.validate_required(self.domain_id, 'domain_id')

    def to_map(self):
        result = dict()
        if self.biz_cname is not None:
            result['biz_cname'] = self.biz_cname
        if self.cname_type is not None:
            result['cname_type'] = self.cname_type
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.is_vpc is not None:
            result['is_vpc'] = self.is_vpc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('biz_cname') is not None:
            self.biz_cname = m.get('biz_cname')
        if m.get('cname_type') is not None:
            self.cname_type = m.get('cname_type')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('is_vpc') is not None:
            self.is_vpc = m.get('is_vpc')
        return self


class SetCorsRuleListRequest(TeaModel):
    """
    list cors rule request
    """
    def __init__(
        self,
        cors_rule_list: List[CorsRule] = None,
        domain_id: str = None,
    ):
        # cors rule list
        self.cors_rule_list = cors_rule_list
        # domain ID
        self.domain_id = domain_id

    def validate(self):
        self.validate_required(self.cors_rule_list, 'cors_rule_list')
        if self.cors_rule_list:
            for k in self.cors_rule_list:
                if k:
                    k.validate()
        self.validate_required(self.domain_id, 'domain_id')

    def to_map(self):
        result = dict()
        result['cors_rule_list'] = []
        if self.cors_rule_list is not None:
            for k in self.cors_rule_list:
                result['cors_rule_list'].append(k.to_map() if k else None)
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cors_rule_list = []
        if m.get('cors_rule_list') is not None:
            for k in m.get('cors_rule_list'):
                temp_model = CorsRule()
                self.cors_rule_list.append(temp_model.from_map(k))
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        return self


class SetDataCNameRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        data_cname: str = None,
        domain_id: str = None,
        location: str = None,
    ):
        # cn-shanghai data cname
        self.data_cname = data_cname
        # domain ID
        self.domain_id = domain_id
        # location
        self.location = location

    def validate(self):
        self.validate_required(self.data_cname, 'data_cname')
        self.validate_required(self.domain_id, 'domain_id')
        self.validate_required(self.location, 'location')

    def to_map(self):
        result = dict()
        if self.data_cname is not None:
            result['data_cname'] = self.data_cname
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.location is not None:
            result['location'] = self.location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data_cname') is not None:
            self.data_cname = m.get('data_cname')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('location') is not None:
            self.location = m.get('location')
        return self


class Store(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        accelerate_endpoint: str = None,
        base_path: str = None,
        bucket: str = None,
        cdn_endpoint: str = None,
        customized_accelerate_endpoint: str = None,
        customized_cdn_endpoint: str = None,
        customized_endpoint: str = None,
        customized_internal_endpoint: str = None,
        endpoint: str = None,
        internal_endpoint: str = None,
        location: str = None,
        ownership: str = None,
        policy: str = None,
        role_arn: str = None,
        store_id: str = None,
        type: str = None,
    ):
        # 全球加速地址
        self.accelerate_endpoint = accelerate_endpoint
        # 存储公共前缀
        self.base_path = base_path
        # bucket名称
        self.bucket = bucket
        # 内容分发地址
        self.cdn_endpoint = cdn_endpoint
        # 自定义全球加速地址
        self.customized_accelerate_endpoint = customized_accelerate_endpoint
        # 自定义内容分发地址
        self.customized_cdn_endpoint = customized_cdn_endpoint
        # 自定义Public访问地址
        self.customized_endpoint = customized_endpoint
        # 自定义vpc访问地址
        self.customized_internal_endpoint = customized_internal_endpoint
        # Public访问地址
        self.endpoint = endpoint
        # vpc访问地址
        self.internal_endpoint = internal_endpoint
        # 地点
        self.location = location
        # 存储归属，system表示系统提供，custom表示使用自己的存储
        self.ownership = ownership
        # Policy授权,system类型store会将bucket权限授予当前云账号
        self.policy = policy
        # 访问Bucket的角色ARN
        self.role_arn = role_arn
        # store ID
        self.store_id = store_id
        # 存储类型，当前只支持oss
        self.type = type

    def validate(self):
        self.validate_required(self.bucket, 'bucket')
        self.validate_required(self.endpoint, 'endpoint')
        self.validate_required(self.ownership, 'ownership')
        self.validate_required(self.policy, 'policy')
        self.validate_required(self.store_id, 'store_id')
        self.validate_required(self.type, 'type')

    def to_map(self):
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accelerate_endpoint') is not None:
            self.accelerate_endpoint = m.get('accelerate_endpoint')
        if m.get('base_path') is not None:
            self.base_path = m.get('base_path')
        if m.get('bucket') is not None:
            self.bucket = m.get('bucket')
        if m.get('cdn_endpoint') is not None:
            self.cdn_endpoint = m.get('cdn_endpoint')
        if m.get('customized_accelerate_endpoint') is not None:
            self.customized_accelerate_endpoint = m.get('customized_accelerate_endpoint')
        if m.get('customized_cdn_endpoint') is not None:
            self.customized_cdn_endpoint = m.get('customized_cdn_endpoint')
        if m.get('customized_endpoint') is not None:
            self.customized_endpoint = m.get('customized_endpoint')
        if m.get('customized_internal_endpoint') is not None:
            self.customized_internal_endpoint = m.get('customized_internal_endpoint')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('internal_endpoint') is not None:
            self.internal_endpoint = m.get('internal_endpoint')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('ownership') is not None:
            self.ownership = m.get('ownership')
        if m.get('policy') is not None:
            self.policy = m.get('policy')
        if m.get('role_arn') is not None:
            self.role_arn = m.get('role_arn')
        if m.get('store_id') is not None:
            self.store_id = m.get('store_id')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class StreamInfo(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        crc_64hash: str = None,
        download_url: str = None,
        size: int = None,
        thumbnail: str = None,
        url: str = None,
    ):
        # crc64_hash
        self.crc_64hash = crc_64hash
        # download_url
        self.download_url = download_url
        self.size = size
        # thumbnail
        self.thumbnail = thumbnail
        # url
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.crc_64hash is not None:
            result['crc64_hash'] = self.crc_64hash
        if self.download_url is not None:
            result['download_url'] = self.download_url
        if self.size is not None:
            result['size'] = self.size
        if self.thumbnail is not None:
            result['thumbnail'] = self.thumbnail
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('crc64_hash') is not None:
            self.crc_64hash = m.get('crc64_hash')
        if m.get('download_url') is not None:
            self.download_url = m.get('download_url')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('thumbnail') is not None:
            self.thumbnail = m.get('thumbnail')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class StreamUploadInfo(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        location: str = None,
        part_info_list: List[UploadPartInfo] = None,
        pre_rapid_upload: bool = None,
        rapid_upload: bool = None,
        upload_id: str = None,
    ):
        # location
        self.location = location
        # part_info_list
        self.part_info_list = part_info_list
        # pre_rapid_upload
        # type: boolean
        self.pre_rapid_upload = pre_rapid_upload
        # rapid_upload
        # type: boolean
        self.rapid_upload = rapid_upload
        # upload_id
        self.upload_id = upload_id

    def validate(self):
        if self.part_info_list:
            for k in self.part_info_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.location is not None:
            result['location'] = self.location
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('location') is not None:
            self.location = m.get('location')
        self.part_info_list = []
        if m.get('part_info_list') is not None:
            for k in m.get('part_info_list'):
                temp_model = UploadPartInfo()
                self.part_info_list.append(temp_model.from_map(k))
        if m.get('pre_rapid_upload') is not None:
            self.pre_rapid_upload = m.get('pre_rapid_upload')
        if m.get('rapid_upload') is not None:
            self.rapid_upload = m.get('rapid_upload')
        if m.get('upload_id') is not None:
            self.upload_id = m.get('upload_id')
        return self


class TokenRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        assertion: str = None,
        client_id: str = None,
        client_secret: str = None,
        code: str = None,
        device_code: str = None,
        grant_type: str = None,
        redirect_uri: str = None,
        refresh_token: str = None,
        sub_domain_id: str = None,
    ):
        # JWT方式授权需要传此参数，传入JWT签名的声明，用于更换accessToken
        self.assertion = assertion
        # Client ID, 此处填写创建App时返回的AppID
        self.client_id = client_id
        # Client ID, 此处填写创建App时返回的AppSecret
        self.client_secret = client_secret
        # 认证后回调参数中的code
        self.code = code
        # OAuth2.0 device flow换取token参数
        self.device_code = device_code
        # 通过code获取accessToken或者通过refresh_token获取accessToken
        self.grant_type = grant_type
        # 回调地址, 此处填写创建App时填写的回调地址，OAuth方式登录时需要传入
        self.redirect_uri = redirect_uri
        # 刷新accessToken使用的refreshToken
        self.refresh_token = refresh_token
        # SubDomainID
        self.sub_domain_id = sub_domain_id

    def validate(self):
        self.validate_required(self.client_id, 'client_id')
        self.validate_required(self.client_secret, 'client_secret')
        self.validate_required(self.grant_type, 'grant_type')

    def to_map(self):
        result = dict()
        if self.assertion is not None:
            result['Assertion'] = self.assertion
        if self.client_id is not None:
            result['ClientID'] = self.client_id
        if self.client_secret is not None:
            result['ClientSecret'] = self.client_secret
        if self.code is not None:
            result['Code'] = self.code
        if self.device_code is not None:
            result['DeviceCode'] = self.device_code
        if self.grant_type is not None:
            result['GrantType'] = self.grant_type
        if self.redirect_uri is not None:
            result['RedirectUri'] = self.redirect_uri
        if self.refresh_token is not None:
            result['RefreshToken'] = self.refresh_token
        if self.sub_domain_id is not None:
            result['SubDomainID'] = self.sub_domain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Assertion') is not None:
            self.assertion = m.get('Assertion')
        if m.get('ClientID') is not None:
            self.client_id = m.get('ClientID')
        if m.get('ClientSecret') is not None:
            self.client_secret = m.get('ClientSecret')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DeviceCode') is not None:
            self.device_code = m.get('DeviceCode')
        if m.get('GrantType') is not None:
            self.grant_type = m.get('GrantType')
        if m.get('RedirectUri') is not None:
            self.redirect_uri = m.get('RedirectUri')
        if m.get('RefreshToken') is not None:
            self.refresh_token = m.get('RefreshToken')
        if m.get('SubDomainID') is not None:
            self.sub_domain_id = m.get('SubDomainID')
        return self


class UpdateAppRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        description: str = None,
        logo: str = None,
        redirect_uri: str = None,
        scope: List[str] = None,
        type: str = None,
    ):
        # App ID
        self.app_id = app_id
        # App名称
        self.app_name = app_name
        # App描述
        self.description = description
        # App图标
        self.logo = logo
        # App回调地址
        self.redirect_uri = redirect_uri
        # App权限列表
        self.scope = scope
        # App类型
        self.type = type

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        if self.app_name is not None:
            self.validate_max_length(self.app_name, 'app_name', 128)
        if self.description is not None:
            self.validate_max_length(self.description, 'description', 1024)

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['app_id'] = self.app_id
        if self.app_name is not None:
            result['app_name'] = self.app_name
        if self.description is not None:
            result['description'] = self.description
        if self.logo is not None:
            result['logo'] = self.logo
        if self.redirect_uri is not None:
            result['redirect_uri'] = self.redirect_uri
        if self.scope is not None:
            result['scope'] = self.scope
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('app_id') is not None:
            self.app_id = m.get('app_id')
        if m.get('app_name') is not None:
            self.app_name = m.get('app_name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('logo') is not None:
            self.logo = m.get('logo')
        if m.get('redirect_uri') is not None:
            self.redirect_uri = m.get('redirect_uri')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class UpdateDomainRequest(TeaModel):
    """
    update domain request
    """
    def __init__(
        self,
        auth_config: dict = None,
        auth_dingding_app_id: str = None,
        auth_dingding_app_secret: str = None,
        auth_dingding_enable: bool = None,
        auth_endpoint_enable: bool = None,
        auth_ram_app_id: str = None,
        auth_ram_app_secret: str = None,
        auth_ram_enable: bool = None,
        data_hash_name: str = None,
        description: str = None,
        domain_id: str = None,
        domain_name: str = None,
        event_filename_matches: str = None,
        event_mns_endpoint: str = None,
        event_mns_topic: str = None,
        event_names: List[str] = None,
        event_role_arn: str = None,
        init_drive_enable: bool = None,
        init_drive_size: int = None,
        init_drive_store_id: str = None,
        published_app_access_strategy: AppAccessStrategy = None,
        sharable: bool = None,
    ):
        self.auth_config = auth_config
        # 钉钉 App Id
        self.auth_dingding_app_id = auth_dingding_app_id
        # 钉钉 App Secret
        self.auth_dingding_app_secret = auth_dingding_app_secret
        # 启用钉钉认证
        self.auth_dingding_enable = auth_dingding_enable
        self.auth_endpoint_enable = auth_endpoint_enable
        # RAM App Id
        self.auth_ram_app_id = auth_ram_app_id
        # RAM App Secret
        self.auth_ram_app_secret = auth_ram_app_secret
        # 启用 RAM 认证
        self.auth_ram_enable = auth_ram_enable
        # 数据 Hash 算法
        self.data_hash_name = data_hash_name
        # Domain 描述
        self.description = description
        # Domain ID
        self.domain_id = domain_id
        # Domain 名称
        self.domain_name = domain_name
        # 事件通知 MNS 匹配文件名
        self.event_filename_matches = event_filename_matches
        # 事件通知 MNS Endpoint
        self.event_mns_endpoint = event_mns_endpoint
        # 事件通知 MNS Topic
        self.event_mns_topic = event_mns_topic
        # 事件名列表
        self.event_names = event_names
        # 事件通知 Role Arn
        self.event_role_arn = event_role_arn
        # 开启自动初始化 Drive
        self.init_drive_enable = init_drive_enable
        # 自动初始化 Drive 大小
        self.init_drive_size = init_drive_size
        # 自动初始化 Drive 使用 Store ID
        self.init_drive_store_id = init_drive_store_id
        self.published_app_access_strategy = published_app_access_strategy
        # 开启分享
        self.sharable = sharable

    def validate(self):
        self.validate_required(self.domain_id, 'domain_id')
        if self.published_app_access_strategy:
            self.published_app_access_strategy.validate()

    def to_map(self):
        result = dict()
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
        if self.published_app_access_strategy is not None:
            result['published_app_access_strategy'] = self.published_app_access_strategy.to_map()
        if self.sharable is not None:
            result['sharable'] = self.sharable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_config') is not None:
            self.auth_config = m.get('auth_config')
        if m.get('auth_dingding_app_id') is not None:
            self.auth_dingding_app_id = m.get('auth_dingding_app_id')
        if m.get('auth_dingding_app_secret') is not None:
            self.auth_dingding_app_secret = m.get('auth_dingding_app_secret')
        if m.get('auth_dingding_enable') is not None:
            self.auth_dingding_enable = m.get('auth_dingding_enable')
        if m.get('auth_endpoint_enable') is not None:
            self.auth_endpoint_enable = m.get('auth_endpoint_enable')
        if m.get('auth_ram_app_id') is not None:
            self.auth_ram_app_id = m.get('auth_ram_app_id')
        if m.get('auth_ram_app_secret') is not None:
            self.auth_ram_app_secret = m.get('auth_ram_app_secret')
        if m.get('auth_ram_enable') is not None:
            self.auth_ram_enable = m.get('auth_ram_enable')
        if m.get('data_hash_name') is not None:
            self.data_hash_name = m.get('data_hash_name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('domain_name') is not None:
            self.domain_name = m.get('domain_name')
        if m.get('event_filename_matches') is not None:
            self.event_filename_matches = m.get('event_filename_matches')
        if m.get('event_mns_endpoint') is not None:
            self.event_mns_endpoint = m.get('event_mns_endpoint')
        if m.get('event_mns_topic') is not None:
            self.event_mns_topic = m.get('event_mns_topic')
        if m.get('event_names') is not None:
            self.event_names = m.get('event_names')
        if m.get('event_role_arn') is not None:
            self.event_role_arn = m.get('event_role_arn')
        if m.get('init_drive_enable') is not None:
            self.init_drive_enable = m.get('init_drive_enable')
        if m.get('init_drive_size') is not None:
            self.init_drive_size = m.get('init_drive_size')
        if m.get('init_drive_store_id') is not None:
            self.init_drive_store_id = m.get('init_drive_store_id')
        if m.get('published_app_access_strategy') is not None:
            temp_model = AppAccessStrategy()
            self.published_app_access_strategy = temp_model.from_map(m['published_app_access_strategy'])
        if m.get('sharable') is not None:
            self.sharable = m.get('sharable')
        return self


class UpdateDriveResponse(TeaModel):
    """
    Update drive response
    """
    def __init__(
        self,
        creator: str = None,
        description: str = None,
        domain_id: str = None,
        drive_id: str = None,
        drive_name: str = None,
        drive_type: str = None,
        encrypt_data_access: bool = None,
        encrypt_mode: str = None,
        owner: str = None,
        owner_type: str = None,
        relative_path: str = None,
        status: str = None,
        store_id: str = None,
        total_size: int = None,
        used_size: int = None,
    ):
        # Drive 创建者
        self.creator = creator
        # Drive 备注信息
        self.description = description
        # Domain ID
        self.domain_id = domain_id
        # Drive ID
        self.drive_id = drive_id
        # Drive 名称
        self.drive_name = drive_name
        # Drive 类型
        self.drive_type = drive_type
        self.encrypt_data_access = encrypt_data_access
        self.encrypt_mode = encrypt_mode
        # Drive 所有者
        self.owner = owner
        # Drive 所有者类型
        self.owner_type = owner_type
        # Drive存储基于store的相对路径，domain的PathType为OSSPath时返回
        self.relative_path = relative_path
        # Drive 状态
        self.status = status
        # 存储 ID, domain的PathType为OSSPath时返回
        self.store_id = store_id
        # Drive 空间总量
        self.total_size = total_size
        # Drive 空间已使用量
        self.used_size = used_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
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
        if self.owner_type is not None:
            result['owner_type'] = self.owner_type
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('drive_name') is not None:
            self.drive_name = m.get('drive_name')
        if m.get('drive_type') is not None:
            self.drive_type = m.get('drive_type')
        if m.get('encrypt_data_access') is not None:
            self.encrypt_data_access = m.get('encrypt_data_access')
        if m.get('encrypt_mode') is not None:
            self.encrypt_mode = m.get('encrypt_mode')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('owner_type') is not None:
            self.owner_type = m.get('owner_type')
        if m.get('relative_path') is not None:
            self.relative_path = m.get('relative_path')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('store_id') is not None:
            self.store_id = m.get('store_id')
        if m.get('total_size') is not None:
            self.total_size = m.get('total_size')
        if m.get('used_size') is not None:
            self.used_size = m.get('used_size')
        return self


class UpdateFileMetaResponse(TeaModel):
    """
    更新文件元数据 response
    """
    def __init__(
        self,
        category: str = None,
        characteristic_hash: str = None,
        content_hash: str = None,
        content_hash_name: str = None,
        content_type: str = None,
        crc_64hash: str = None,
        created_at: str = None,
        description: str = None,
        domain_id: str = None,
        download_url: str = None,
        drive_id: str = None,
        encrypt_mode: str = None,
        file_extension: str = None,
        file_id: str = None,
        hidden: bool = None,
        image_media_metadata: ImageMediaResponse = None,
        labels: List[str] = None,
        meta: str = None,
        name: str = None,
        parent_file_id: str = None,
        punish_flag: int = None,
        share_id: str = None,
        size: int = None,
        starred: bool = None,
        status: str = None,
        streams_info: dict = None,
        thumbnail: str = None,
        trashed_at: str = None,
        type: str = None,
        updated_at: str = None,
        upload_id: str = None,
        url: str = None,
        user_meta: str = None,
        video_media_metadata: VideoMediaResponse = None,
        video_preview_metadata: VideoPreviewResponse = None,
    ):
        # category
        self.category = category
        # CharacteristicHash
        self.characteristic_hash = characteristic_hash
        # Content Hash
        self.content_hash = content_hash
        # content_hash_name
        self.content_hash_name = content_hash_name
        # content_type
        self.content_type = content_type
        # crc64_hash
        self.crc_64hash = crc_64hash
        # created_at
        self.created_at = created_at
        # description
        self.description = description
        # DomainID
        self.domain_id = domain_id
        # download_url
        self.download_url = download_url
        # drive_id
        self.drive_id = drive_id
        # encrypt_mode
        self.encrypt_mode = encrypt_mode
        # file_extension
        self.file_extension = file_extension
        # file_id
        self.file_id = file_id
        # Hidden
        # type: boolean
        self.hidden = hidden
        self.image_media_metadata = image_media_metadata
        # labels
        self.labels = labels
        self.meta = meta
        # name
        self.name = name
        # parent_file_id
        self.parent_file_id = parent_file_id
        self.punish_flag = punish_flag
        self.share_id = share_id
        # Size
        self.size = size
        # starred
        # type: boolean
        self.starred = starred
        # status
        self.status = status
        # @Deprecated streams url info
        self.streams_info = streams_info
        # thumbnail
        self.thumbnail = thumbnail
        # trashed_at
        self.trashed_at = trashed_at
        # type
        self.type = type
        # updated_at
        self.updated_at = updated_at
        # upload_id
        self.upload_id = upload_id
        # url
        self.url = url
        # user_meta
        self.user_meta = user_meta
        self.video_media_metadata = video_media_metadata
        self.video_preview_metadata = video_preview_metadata

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
        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.characteristic_hash is not None:
            result['characteristic_hash'] = self.characteristic_hash
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
        if self.share_id is not None:
            result['share_id'] = self.share_id
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('characteristic_hash') is not None:
            self.characteristic_hash = m.get('characteristic_hash')
        if m.get('content_hash') is not None:
            self.content_hash = m.get('content_hash')
        if m.get('content_hash_name') is not None:
            self.content_hash_name = m.get('content_hash_name')
        if m.get('content_type') is not None:
            self.content_type = m.get('content_type')
        if m.get('crc64_hash') is not None:
            self.crc_64hash = m.get('crc64_hash')
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('download_url') is not None:
            self.download_url = m.get('download_url')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('encrypt_mode') is not None:
            self.encrypt_mode = m.get('encrypt_mode')
        if m.get('file_extension') is not None:
            self.file_extension = m.get('file_extension')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('hidden') is not None:
            self.hidden = m.get('hidden')
        if m.get('image_media_metadata') is not None:
            temp_model = ImageMediaResponse()
            self.image_media_metadata = temp_model.from_map(m['image_media_metadata'])
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('meta') is not None:
            self.meta = m.get('meta')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parent_file_id') is not None:
            self.parent_file_id = m.get('parent_file_id')
        if m.get('punish_flag') is not None:
            self.punish_flag = m.get('punish_flag')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('starred') is not None:
            self.starred = m.get('starred')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('streams_info') is not None:
            self.streams_info = m.get('streams_info')
        if m.get('thumbnail') is not None:
            self.thumbnail = m.get('thumbnail')
        if m.get('trashed_at') is not None:
            self.trashed_at = m.get('trashed_at')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        if m.get('upload_id') is not None:
            self.upload_id = m.get('upload_id')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('user_meta') is not None:
            self.user_meta = m.get('user_meta')
        if m.get('video_media_metadata') is not None:
            temp_model = VideoMediaResponse()
            self.video_media_metadata = temp_model.from_map(m['video_media_metadata'])
        if m.get('video_preview_metadata') is not None:
            temp_model = VideoPreviewResponse()
            self.video_preview_metadata = temp_model.from_map(m['video_preview_metadata'])
        return self


class UpdateShareLinkResponse(TeaModel):
    """
    update_share_link response
    """
    def __init__(
        self,
        created_at: str = None,
        creator: str = None,
        description: str = None,
        download_count: int = None,
        drive_id: str = None,
        expiration: str = None,
        expired: bool = None,
        file_id: str = None,
        file_id_list: List[str] = None,
        file_path_list: List[str] = None,
        preview_count: int = None,
        save_count: int = None,
        share_id: str = None,
        share_msg: str = None,
        share_name: str = None,
        share_policy: str = None,
        share_pwd: str = None,
        share_url: str = None,
        updated_at: str = None,
    ):
        # created_at
        self.created_at = created_at
        # creator
        self.creator = creator
        # description
        self.description = description
        # 下载次数
        self.download_count = download_count
        # drive_id
        self.drive_id = drive_id
        # expiration
        self.expiration = expiration
        # expired
        self.expired = expired
        # file_id
        self.file_id = file_id
        # file_id_list
        self.file_id_list = file_id_list
        # file_id_list
        self.file_path_list = file_path_list
        # preview_count
        self.preview_count = preview_count
        # 转存次数
        self.save_count = save_count
        # share_id
        self.share_id = share_id
        # share_msg
        self.share_msg = share_msg
        # share_name
        self.share_name = share_name
        # share_policy
        self.share_policy = share_policy
        # share_pwd
        self.share_pwd = share_pwd
        # share_url
        self.share_url = share_url
        # updated_at
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.creator is not None:
            result['creator'] = self.creator
        if self.description is not None:
            result['description'] = self.description
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
        if self.file_id_list is not None:
            result['file_id_list'] = self.file_id_list
        if self.file_path_list is not None:
            result['file_path_list'] = self.file_path_list
        if self.preview_count is not None:
            result['preview_count'] = self.preview_count
        if self.save_count is not None:
            result['save_count'] = self.save_count
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.share_msg is not None:
            result['share_msg'] = self.share_msg
        if self.share_name is not None:
            result['share_name'] = self.share_name
        if self.share_policy is not None:
            result['share_policy'] = self.share_policy
        if self.share_pwd is not None:
            result['share_pwd'] = self.share_pwd
        if self.share_url is not None:
            result['share_url'] = self.share_url
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('download_count') is not None:
            self.download_count = m.get('download_count')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('expiration') is not None:
            self.expiration = m.get('expiration')
        if m.get('expired') is not None:
            self.expired = m.get('expired')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('file_id_list') is not None:
            self.file_id_list = m.get('file_id_list')
        if m.get('file_path_list') is not None:
            self.file_path_list = m.get('file_path_list')
        if m.get('preview_count') is not None:
            self.preview_count = m.get('preview_count')
        if m.get('save_count') is not None:
            self.save_count = m.get('save_count')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('share_msg') is not None:
            self.share_msg = m.get('share_msg')
        if m.get('share_name') is not None:
            self.share_name = m.get('share_name')
        if m.get('share_policy') is not None:
            self.share_policy = m.get('share_policy')
        if m.get('share_pwd') is not None:
            self.share_pwd = m.get('share_pwd')
        if m.get('share_url') is not None:
            self.share_url = m.get('share_url')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        return self


class UpdateShareResponse(TeaModel):
    """
    Update share response
    """
    def __init__(
        self,
        created_at: str = None,
        creator: str = None,
        description: str = None,
        domain_id: str = None,
        drive_id: str = None,
        expiration: str = None,
        expired: bool = None,
        owner: str = None,
        owner_type: str = None,
        permissions: List[str] = None,
        share_file_id: str = None,
        share_file_path: str = None,
        share_id: str = None,
        share_name: str = None,
        share_policy: List[SharePermissionPolicy] = None,
        status: str = None,
        updated_at: str = None,
    ):
        # created_at
        self.created_at = created_at
        # creator
        self.creator = creator
        # description
        self.description = description
        # domain_id
        self.domain_id = domain_id
        # drive_id
        self.drive_id = drive_id
        # expiration
        self.expiration = expiration
        # expired
        self.expired = expired
        # owner
        self.owner = owner
        # owner
        self.owner_type = owner_type
        # permissions
        self.permissions = permissions
        # share_file_id
        self.share_file_id = share_file_id
        # share_path
        self.share_file_path = share_file_path
        # share_id
        self.share_id = share_id
        # share_name
        self.share_name = share_name
        self.share_policy = share_policy
        # status
        self.status = status
        # updated_at
        self.updated_at = updated_at

    def validate(self):
        if self.share_policy:
            for k in self.share_policy:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
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
        if self.owner_type is not None:
            result['owner_type'] = self.owner_type
        if self.permissions is not None:
            result['permissions'] = self.permissions
        if self.share_file_id is not None:
            result['share_file_id'] = self.share_file_id
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('expiration') is not None:
            self.expiration = m.get('expiration')
        if m.get('expired') is not None:
            self.expired = m.get('expired')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('owner_type') is not None:
            self.owner_type = m.get('owner_type')
        if m.get('permissions') is not None:
            self.permissions = m.get('permissions')
        if m.get('share_file_id') is not None:
            self.share_file_id = m.get('share_file_id')
        if m.get('share_file_path') is not None:
            self.share_file_path = m.get('share_file_path')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('share_name') is not None:
            self.share_name = m.get('share_name')
        self.share_policy = []
        if m.get('share_policy') is not None:
            for k in m.get('share_policy'):
                temp_model = SharePermissionPolicy()
                self.share_policy.append(temp_model.from_map(k))
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        return self


class UrlInfo(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        download_url: str = None,
        thumbnail: str = None,
        url: str = None,
    ):
        # download_url
        self.download_url = download_url
        # thumbnail
        self.thumbnail = thumbnail
        # url
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.download_url is not None:
            result['download_url'] = self.download_url
        if self.thumbnail is not None:
            result['thumbnail'] = self.thumbnail
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('download_url') is not None:
            self.download_url = m.get('download_url')
        if m.get('thumbnail') is not None:
            self.thumbnail = m.get('thumbnail')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class UserAuthentication(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        authentication_type: str = None,
        created_at: int = None,
        detail: str = None,
        domain_id: str = None,
        identity: str = None,
        last_login_time: int = None,
        status: str = None,
        user_id: str = None,
        extra: str = None,
        subdomain_id: str = None,
    ):
        # 认证类型
        self.authentication_type = authentication_type
        # 创建时间
        self.created_at = created_at
        # 详情
        self.detail = detail
        # Domain ID
        self.domain_id = domain_id
        # 唯一身份标识
        self.identity = identity
        # 最后登录时间
        self.last_login_time = last_login_time
        # 状态
        self.status = status
        # 用户ID
        self.user_id = user_id
        # 额外的信息，比如type为mobile时，此字段为国家编号，不填默认86
        self.extra = extra
        # subdomain id
        self.subdomain_id = subdomain_id

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
        result = dict()
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
        if self.subdomain_id is not None:
            result['subdomain_id'] = self.subdomain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthenticationType') is not None:
            self.authentication_type = m.get('AuthenticationType')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('DomainID') is not None:
            self.domain_id = m.get('DomainID')
        if m.get('Identity') is not None:
            self.identity = m.get('Identity')
        if m.get('LastLoginTime') is not None:
            self.last_login_time = m.get('LastLoginTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserID') is not None:
            self.user_id = m.get('UserID')
        if m.get('extra') is not None:
            self.extra = m.get('extra')
        if m.get('subdomain_id') is not None:
            self.subdomain_id = m.get('subdomain_id')
        return self


class VerifyCodeRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        app_id: str = None,
        phone_number: str = None,
        phone_region: str = None,
        sms_code: str = None,
        sms_code_id: str = None,
        verify_type: str = None,
    ):
        self.headers = headers
        # App ID, 当前访问的App
        self.app_id = app_id
        # 手机号
        self.phone_number = phone_number
        # 国家编号，默认86，不需要填+号，直接填数字
        self.phone_region = phone_region
        # 短信验证码内容
        self.sms_code = sms_code
        # 短信验证码ID
        self.sms_code_id = sms_code_id
        # 需要被校验内容的类型
        self.verify_type = verify_type

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.phone_number, 'phone_number')
        self.validate_required(self.sms_code, 'sms_code')
        self.validate_required(self.sms_code_id, 'sms_code_id')

    def to_map(self):
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('app_id') is not None:
            self.app_id = m.get('app_id')
        if m.get('phone_number') is not None:
            self.phone_number = m.get('phone_number')
        if m.get('phone_region') is not None:
            self.phone_region = m.get('phone_region')
        if m.get('sms_code') is not None:
            self.sms_code = m.get('sms_code')
        if m.get('sms_code_id') is not None:
            self.sms_code_id = m.get('sms_code_id')
        if m.get('verify_type') is not None:
            self.verify_type = m.get('verify_type')
        return self


class ListStoresResponse(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        items: List[Store] = None,
    ):
        # Store 列表
        self.items = items

    def validate(self):
        self.validate_required(self.items, 'items')
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = Store()
                self.items.append(temp_model.from_map(k))
        return self


class AdminListStoresModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListStoresResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListStoresResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSubdomainResponse(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        subdomain_id: str = None,
    ):
        # 用以唯一标识subdomain
        self.subdomain_id = subdomain_id

    def validate(self):
        self.validate_required(self.subdomain_id, 'subdomain_id')

    def to_map(self):
        result = dict()
        if self.subdomain_id is not None:
            result['subdomain_id'] = self.subdomain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('subdomain_id') is not None:
            self.subdomain_id = m.get('subdomain_id')
        return self


class CreateSubdomainModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSubdomainResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateSubdomainResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSubdomainResponse(TeaModel):
    """
    *\
    """
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteSubdomainModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteSubdomainResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteSubdomainResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSubdomainResponse(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        created_at: str = None,
        description: str = None,
        name: str = None,
        subdomain_id: str = None,
        total_size: int = None,
        updated_at: str = None,
        user_quota: int = None,
    ):
        # 创建时间
        self.created_at = created_at
        # 描述
        self.description = description
        # 名称
        self.name = name
        # 用以唯一标识subdomain
        self.subdomain_id = subdomain_id
        # 逻辑空间quota，-1表示无限制，单位为字节
        self.total_size = total_size
        # 更新时间
        self.updated_at = updated_at
        # 用户数quota，-1表示无限制
        self.user_quota = user_quota

    def validate(self):
        self.validate_required(self.created_at, 'created_at')
        self.validate_required(self.description, 'description')
        self.validate_required(self.name, 'name')
        self.validate_required(self.subdomain_id, 'subdomain_id')
        self.validate_required(self.total_size, 'total_size')
        self.validate_required(self.updated_at, 'updated_at')
        self.validate_required(self.user_quota, 'user_quota')

    def to_map(self):
        result = dict()
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.subdomain_id is not None:
            result['subdomain_id'] = self.subdomain_id
        if self.total_size is not None:
            result['total_size'] = self.total_size
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        if self.user_quota is not None:
            result['user_quota'] = self.user_quota
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('subdomain_id') is not None:
            self.subdomain_id = m.get('subdomain_id')
        if m.get('total_size') is not None:
            self.total_size = m.get('total_size')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        if m.get('user_quota') is not None:
            self.user_quota = m.get('user_quota')
        return self


class GetSubdomainModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSubdomainResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetSubdomainResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class BaseSubdomainResponse(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        created_at: str = None,
        description: str = None,
        name: str = None,
        subdomain_id: str = None,
        total_size: int = None,
        updated_at: str = None,
        user_quota: int = None,
    ):
        # 创建时间
        self.created_at = created_at
        # 描述
        self.description = description
        # 名称
        self.name = name
        # 用以唯一标识subdomain
        self.subdomain_id = subdomain_id
        # 逻辑空间quota，-1表示无限制，单位为字节
        self.total_size = total_size
        # 更新时间
        self.updated_at = updated_at
        # 用户数quota，-1表示无限制
        self.user_quota = user_quota

    def validate(self):
        self.validate_required(self.created_at, 'created_at')
        self.validate_required(self.description, 'description')
        self.validate_required(self.name, 'name')
        self.validate_required(self.subdomain_id, 'subdomain_id')
        self.validate_required(self.total_size, 'total_size')
        self.validate_required(self.updated_at, 'updated_at')
        self.validate_required(self.user_quota, 'user_quota')

    def to_map(self):
        result = dict()
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.subdomain_id is not None:
            result['subdomain_id'] = self.subdomain_id
        if self.total_size is not None:
            result['total_size'] = self.total_size
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        if self.user_quota is not None:
            result['user_quota'] = self.user_quota
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('subdomain_id') is not None:
            self.subdomain_id = m.get('subdomain_id')
        if m.get('total_size') is not None:
            self.total_size = m.get('total_size')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        if m.get('user_quota') is not None:
            self.user_quota = m.get('user_quota')
        return self


class ListSubdomainsResponse(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        items: List[BaseSubdomainResponse] = None,
        next_marker: str = None,
    ):
        # 分页的 subdomain 数据
        self.items = items
        # 分页游标，可以用作下次list的起点
        self.next_marker = next_marker

    def validate(self):
        self.validate_required(self.items, 'items')
        if self.items:
            for k in self.items:
                if k:
                    k.validate()
        self.validate_required(self.next_marker, 'next_marker')

    def to_map(self):
        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = BaseSubdomainResponse()
                self.items.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        return self


class ListSubdomainsModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSubdomainsResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListSubdomainsResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSubdomainResponse(TeaModel):
    """
    *\
    """
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateSubdomainModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateSubdomainResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateSubdomainResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserAccessTokenModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AccessTokenResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AccessTokenResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class AddStoreResponse(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        accelerate_endpoint: str = None,
        base_path: str = None,
        bucket: str = None,
        cdn_endpoint: str = None,
        customized_accelerate_endpoint: str = None,
        customized_cdn_endpoint: str = None,
        customized_endpoint: str = None,
        customized_internal_endpoint: str = None,
        domain_id: str = None,
        endpoint: str = None,
        internal_endpoint: str = None,
        location: str = None,
        ownership: str = None,
        policy: str = None,
        role_arn: str = None,
        store_id: str = None,
        type: str = None,
    ):
        # 全球加速地址
        self.accelerate_endpoint = accelerate_endpoint
        # 存储公共前缀
        self.base_path = base_path
        # bucket名称
        self.bucket = bucket
        # 内容分发地址
        self.cdn_endpoint = cdn_endpoint
        # 自定义全球加速地址
        self.customized_accelerate_endpoint = customized_accelerate_endpoint
        # 自定义内容分发地址
        self.customized_cdn_endpoint = customized_cdn_endpoint
        # 自定义Public访问地址
        self.customized_endpoint = customized_endpoint
        # 自定义vpc访问地址
        self.customized_internal_endpoint = customized_internal_endpoint
        # domain ID
        self.domain_id = domain_id
        # Public访问地址
        self.endpoint = endpoint
        # vpc访问地址
        self.internal_endpoint = internal_endpoint
        # 地点
        self.location = location
        # 存储归属，system表示系统提供，custom表示使用自己的存储
        self.ownership = ownership
        # Policy授权,system类型store会将bucket权限授予当前云账号
        self.policy = policy
        # 访问Bucket的角色ARN
        self.role_arn = role_arn
        # store ID
        self.store_id = store_id
        # 存储类型，当前只支持oss
        self.type = type

    def validate(self):
        self.validate_required(self.bucket, 'bucket')
        self.validate_required(self.domain_id, 'domain_id')
        self.validate_required(self.endpoint, 'endpoint')
        self.validate_required(self.ownership, 'ownership')
        self.validate_required(self.policy, 'policy')
        self.validate_required(self.store_id, 'store_id')
        self.validate_required(self.type, 'type')

    def to_map(self):
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accelerate_endpoint') is not None:
            self.accelerate_endpoint = m.get('accelerate_endpoint')
        if m.get('base_path') is not None:
            self.base_path = m.get('base_path')
        if m.get('bucket') is not None:
            self.bucket = m.get('bucket')
        if m.get('cdn_endpoint') is not None:
            self.cdn_endpoint = m.get('cdn_endpoint')
        if m.get('customized_accelerate_endpoint') is not None:
            self.customized_accelerate_endpoint = m.get('customized_accelerate_endpoint')
        if m.get('customized_cdn_endpoint') is not None:
            self.customized_cdn_endpoint = m.get('customized_cdn_endpoint')
        if m.get('customized_endpoint') is not None:
            self.customized_endpoint = m.get('customized_endpoint')
        if m.get('customized_internal_endpoint') is not None:
            self.customized_internal_endpoint = m.get('customized_internal_endpoint')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('internal_endpoint') is not None:
            self.internal_endpoint = m.get('internal_endpoint')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('ownership') is not None:
            self.ownership = m.get('ownership')
        if m.get('policy') is not None:
            self.policy = m.get('policy')
        if m.get('role_arn') is not None:
            self.role_arn = m.get('role_arn')
        if m.get('store_id') is not None:
            self.store_id = m.get('store_id')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class AdminListStoresRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class BaseDomainResponse(TeaModel):
    """
    base domain response
    """
    def __init__(
        self,
        api_cname: str = None,
        app_cname: str = None,
        auth_alipay_app_id: str = None,
        auth_alipay_enable: bool = None,
        auth_alipay_private_key: str = None,
        auth_cname: str = None,
        auth_config: dict = None,
        auth_dingding_app_id: str = None,
        auth_dingding_app_secret: str = None,
        auth_dingding_enable: bool = None,
        auth_endpoint_enable: bool = None,
        auth_ram_app_id: str = None,
        auth_ram_app_secret: str = None,
        auth_ram_enable: bool = None,
        created_at: str = None,
        data_hash_name: str = None,
        description: str = None,
        domain_id: str = None,
        domain_name: str = None,
        event_filename_matches: str = None,
        event_mns_endpoint: str = None,
        event_mns_topic: str = None,
        event_names: List[str] = None,
        event_role_arn: str = None,
        init_drive_enable: bool = None,
        init_drive_size: int = None,
        init_drive_store_id: str = None,
        mode: str = None,
        path_type: str = None,
        published_app_access_strategy: AppAccessStrategy = None,
        sharable: bool = None,
        store_level: str = None,
        store_region_list: List[str] = None,
        updated_at: str = None,
    ):
        # Domain APICName
        self.api_cname = api_cname
        # Domain AppCName
        self.app_cname = app_cname
        # 支付宝 App Id
        self.auth_alipay_app_id = auth_alipay_app_id
        # 是否开启了支付宝认证
        self.auth_alipay_enable = auth_alipay_enable
        # 支付宝 App Secret
        self.auth_alipay_private_key = auth_alipay_private_key
        # Domain AuthCName
        self.auth_cname = auth_cname
        # 登录相关信息
        self.auth_config = auth_config
        # 钉钉 App Id
        self.auth_dingding_app_id = auth_dingding_app_id
        # 钉钉 App Secret
        self.auth_dingding_app_secret = auth_dingding_app_secret
        # 是否开启了钉钉认证
        self.auth_dingding_enable = auth_dingding_enable
        self.auth_endpoint_enable = auth_endpoint_enable
        # RAM App Id
        self.auth_ram_app_id = auth_ram_app_id
        # RAM App Secret
        self.auth_ram_app_secret = auth_ram_app_secret
        # 是否开启了 RAM 认证
        self.auth_ram_enable = auth_ram_enable
        # Domain 创建时间
        self.created_at = created_at
        # 数据 Hash 算法
        self.data_hash_name = data_hash_name
        # Domain 描述
        self.description = description
        # Domain ID
        self.domain_id = domain_id
        # Domain 描述
        self.domain_name = domain_name
        # 事件通知 MNS 匹配文件名
        self.event_filename_matches = event_filename_matches
        # 事件通知 MNS Endpoint
        self.event_mns_endpoint = event_mns_endpoint
        # 事件通知 MNS Topic
        self.event_mns_topic = event_mns_topic
        # 事件名列表
        self.event_names = event_names
        # 事件通知 Role Arn
        self.event_role_arn = event_role_arn
        # 是否开启了自动初始化 Drive
        self.init_drive_enable = init_drive_enable
        # 自动初始化 Drive 大小
        self.init_drive_size = init_drive_size
        # 自动初始化 Drive 所用 Store ID
        self.init_drive_store_id = init_drive_store_id
        # Domain 类型
        self.mode = mode
        # Domain 类型
        self.path_type = path_type
        self.published_app_access_strategy = published_app_access_strategy
        # 是否开启了分享
        self.sharable = sharable
        # 存储级别
        self.store_level = store_level
        # 存储 Region 列表
        self.store_region_list = store_region_list
        # Domain 更新时间
        self.updated_at = updated_at

    def validate(self):
        if self.published_app_access_strategy:
            self.published_app_access_strategy.validate()

    def to_map(self):
        result = dict()
        if self.api_cname is not None:
            result['api_cname'] = self.api_cname
        if self.app_cname is not None:
            result['app_cname'] = self.app_cname
        if self.auth_alipay_app_id is not None:
            result['auth_alipay_app_id'] = self.auth_alipay_app_id
        if self.auth_alipay_enable is not None:
            result['auth_alipay_enable'] = self.auth_alipay_enable
        if self.auth_alipay_private_key is not None:
            result['auth_alipay_private_key'] = self.auth_alipay_private_key
        if self.auth_cname is not None:
            result['auth_cname'] = self.auth_cname
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('api_cname') is not None:
            self.api_cname = m.get('api_cname')
        if m.get('app_cname') is not None:
            self.app_cname = m.get('app_cname')
        if m.get('auth_alipay_app_id') is not None:
            self.auth_alipay_app_id = m.get('auth_alipay_app_id')
        if m.get('auth_alipay_enable') is not None:
            self.auth_alipay_enable = m.get('auth_alipay_enable')
        if m.get('auth_alipay_private_key') is not None:
            self.auth_alipay_private_key = m.get('auth_alipay_private_key')
        if m.get('auth_cname') is not None:
            self.auth_cname = m.get('auth_cname')
        if m.get('auth_config') is not None:
            self.auth_config = m.get('auth_config')
        if m.get('auth_dingding_app_id') is not None:
            self.auth_dingding_app_id = m.get('auth_dingding_app_id')
        if m.get('auth_dingding_app_secret') is not None:
            self.auth_dingding_app_secret = m.get('auth_dingding_app_secret')
        if m.get('auth_dingding_enable') is not None:
            self.auth_dingding_enable = m.get('auth_dingding_enable')
        if m.get('auth_endpoint_enable') is not None:
            self.auth_endpoint_enable = m.get('auth_endpoint_enable')
        if m.get('auth_ram_app_id') is not None:
            self.auth_ram_app_id = m.get('auth_ram_app_id')
        if m.get('auth_ram_app_secret') is not None:
            self.auth_ram_app_secret = m.get('auth_ram_app_secret')
        if m.get('auth_ram_enable') is not None:
            self.auth_ram_enable = m.get('auth_ram_enable')
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('data_hash_name') is not None:
            self.data_hash_name = m.get('data_hash_name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('domain_name') is not None:
            self.domain_name = m.get('domain_name')
        if m.get('event_filename_matches') is not None:
            self.event_filename_matches = m.get('event_filename_matches')
        if m.get('event_mns_endpoint') is not None:
            self.event_mns_endpoint = m.get('event_mns_endpoint')
        if m.get('event_mns_topic') is not None:
            self.event_mns_topic = m.get('event_mns_topic')
        if m.get('event_names') is not None:
            self.event_names = m.get('event_names')
        if m.get('event_role_arn') is not None:
            self.event_role_arn = m.get('event_role_arn')
        if m.get('init_drive_enable') is not None:
            self.init_drive_enable = m.get('init_drive_enable')
        if m.get('init_drive_size') is not None:
            self.init_drive_size = m.get('init_drive_size')
        if m.get('init_drive_store_id') is not None:
            self.init_drive_store_id = m.get('init_drive_store_id')
        if m.get('mode') is not None:
            self.mode = m.get('mode')
        if m.get('path_type') is not None:
            self.path_type = m.get('path_type')
        if m.get('published_app_access_strategy') is not None:
            temp_model = AppAccessStrategy()
            self.published_app_access_strategy = temp_model.from_map(m['published_app_access_strategy'])
        if m.get('sharable') is not None:
            self.sharable = m.get('sharable')
        if m.get('store_level') is not None:
            self.store_level = m.get('store_level')
        if m.get('store_region_list') is not None:
            self.store_region_list = m.get('store_region_list')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        return self


class CNameStatus(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        bingding_state: str = None,
        legal_state: str = None,
        remark: str = None,
    ):
        # binding state
        self.bingding_state = bingding_state
        # legal state
        self.legal_state = legal_state
        # remark
        self.remark = remark

    def validate(self):
        self.validate_required(self.bingding_state, 'bingding_state')
        self.validate_required(self.legal_state, 'legal_state')
        self.validate_required(self.remark, 'remark')

    def to_map(self):
        result = dict()
        if self.bingding_state is not None:
            result['bingding_state'] = self.bingding_state
        if self.legal_state is not None:
            result['legal_state'] = self.legal_state
        if self.remark is not None:
            result['remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bingding_state') is not None:
            self.bingding_state = m.get('bingding_state')
        if m.get('legal_state') is not None:
            self.legal_state = m.get('legal_state')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        return self


class CreateDomainResponse(TeaModel):
    """
    create domain response
    """
    def __init__(
        self,
        api_cname: str = None,
        app_cname: str = None,
        auth_alipay_app_id: str = None,
        auth_alipay_enable: bool = None,
        auth_alipay_private_key: str = None,
        auth_cname: str = None,
        auth_config: dict = None,
        auth_dingding_app_id: str = None,
        auth_dingding_app_secret: str = None,
        auth_dingding_enable: bool = None,
        auth_endpoint_enable: bool = None,
        auth_ram_app_id: str = None,
        auth_ram_app_secret: str = None,
        auth_ram_enable: bool = None,
        created_at: str = None,
        data_hash_name: str = None,
        description: str = None,
        domain_id: str = None,
        domain_name: str = None,
        event_filename_matches: str = None,
        event_mns_endpoint: str = None,
        event_mns_topic: str = None,
        event_names: List[str] = None,
        event_role_arn: str = None,
        init_drive_enable: bool = None,
        init_drive_size: int = None,
        init_drive_store_id: str = None,
        mode: str = None,
        path_type: str = None,
        published_app_access_strategy: AppAccessStrategy = None,
        sharable: bool = None,
        store_level: str = None,
        store_region_list: List[str] = None,
        updated_at: str = None,
    ):
        # Domain APICName
        self.api_cname = api_cname
        # Domain AppCName
        self.app_cname = app_cname
        # 支付宝 App Id
        self.auth_alipay_app_id = auth_alipay_app_id
        # 是否开启了支付宝认证
        self.auth_alipay_enable = auth_alipay_enable
        # 支付宝 App Secret
        self.auth_alipay_private_key = auth_alipay_private_key
        # Domain AuthCName
        self.auth_cname = auth_cname
        # 登录相关信息
        self.auth_config = auth_config
        # 钉钉 App Id
        self.auth_dingding_app_id = auth_dingding_app_id
        # 钉钉 App Secret
        self.auth_dingding_app_secret = auth_dingding_app_secret
        # 是否开启了钉钉认证
        self.auth_dingding_enable = auth_dingding_enable
        self.auth_endpoint_enable = auth_endpoint_enable
        # RAM App Id
        self.auth_ram_app_id = auth_ram_app_id
        # RAM App Secret
        self.auth_ram_app_secret = auth_ram_app_secret
        # 是否开启了 RAM 认证
        self.auth_ram_enable = auth_ram_enable
        # Domain 创建时间
        self.created_at = created_at
        # 数据 Hash 算法
        self.data_hash_name = data_hash_name
        # Domain 描述
        self.description = description
        # Domain ID
        self.domain_id = domain_id
        # Domain 描述
        self.domain_name = domain_name
        # 事件通知 MNS 匹配文件名
        self.event_filename_matches = event_filename_matches
        # 事件通知 MNS Endpoint
        self.event_mns_endpoint = event_mns_endpoint
        # 事件通知 MNS Topic
        self.event_mns_topic = event_mns_topic
        # 事件名列表
        self.event_names = event_names
        # 事件通知 Role Arn
        self.event_role_arn = event_role_arn
        # 是否开启了自动初始化 Drive
        self.init_drive_enable = init_drive_enable
        # 自动初始化 Drive 大小
        self.init_drive_size = init_drive_size
        # 自动初始化 Drive 所用 Store ID
        self.init_drive_store_id = init_drive_store_id
        # Domain 类型
        self.mode = mode
        # Domain 类型
        self.path_type = path_type
        self.published_app_access_strategy = published_app_access_strategy
        # 是否开启了分享
        self.sharable = sharable
        # 存储级别
        self.store_level = store_level
        # 存储 Region 列表
        self.store_region_list = store_region_list
        # Domain 更新时间
        self.updated_at = updated_at

    def validate(self):
        if self.published_app_access_strategy:
            self.published_app_access_strategy.validate()

    def to_map(self):
        result = dict()
        if self.api_cname is not None:
            result['api_cname'] = self.api_cname
        if self.app_cname is not None:
            result['app_cname'] = self.app_cname
        if self.auth_alipay_app_id is not None:
            result['auth_alipay_app_id'] = self.auth_alipay_app_id
        if self.auth_alipay_enable is not None:
            result['auth_alipay_enable'] = self.auth_alipay_enable
        if self.auth_alipay_private_key is not None:
            result['auth_alipay_private_key'] = self.auth_alipay_private_key
        if self.auth_cname is not None:
            result['auth_cname'] = self.auth_cname
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('api_cname') is not None:
            self.api_cname = m.get('api_cname')
        if m.get('app_cname') is not None:
            self.app_cname = m.get('app_cname')
        if m.get('auth_alipay_app_id') is not None:
            self.auth_alipay_app_id = m.get('auth_alipay_app_id')
        if m.get('auth_alipay_enable') is not None:
            self.auth_alipay_enable = m.get('auth_alipay_enable')
        if m.get('auth_alipay_private_key') is not None:
            self.auth_alipay_private_key = m.get('auth_alipay_private_key')
        if m.get('auth_cname') is not None:
            self.auth_cname = m.get('auth_cname')
        if m.get('auth_config') is not None:
            self.auth_config = m.get('auth_config')
        if m.get('auth_dingding_app_id') is not None:
            self.auth_dingding_app_id = m.get('auth_dingding_app_id')
        if m.get('auth_dingding_app_secret') is not None:
            self.auth_dingding_app_secret = m.get('auth_dingding_app_secret')
        if m.get('auth_dingding_enable') is not None:
            self.auth_dingding_enable = m.get('auth_dingding_enable')
        if m.get('auth_endpoint_enable') is not None:
            self.auth_endpoint_enable = m.get('auth_endpoint_enable')
        if m.get('auth_ram_app_id') is not None:
            self.auth_ram_app_id = m.get('auth_ram_app_id')
        if m.get('auth_ram_app_secret') is not None:
            self.auth_ram_app_secret = m.get('auth_ram_app_secret')
        if m.get('auth_ram_enable') is not None:
            self.auth_ram_enable = m.get('auth_ram_enable')
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('data_hash_name') is not None:
            self.data_hash_name = m.get('data_hash_name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('domain_name') is not None:
            self.domain_name = m.get('domain_name')
        if m.get('event_filename_matches') is not None:
            self.event_filename_matches = m.get('event_filename_matches')
        if m.get('event_mns_endpoint') is not None:
            self.event_mns_endpoint = m.get('event_mns_endpoint')
        if m.get('event_mns_topic') is not None:
            self.event_mns_topic = m.get('event_mns_topic')
        if m.get('event_names') is not None:
            self.event_names = m.get('event_names')
        if m.get('event_role_arn') is not None:
            self.event_role_arn = m.get('event_role_arn')
        if m.get('init_drive_enable') is not None:
            self.init_drive_enable = m.get('init_drive_enable')
        if m.get('init_drive_size') is not None:
            self.init_drive_size = m.get('init_drive_size')
        if m.get('init_drive_store_id') is not None:
            self.init_drive_store_id = m.get('init_drive_store_id')
        if m.get('mode') is not None:
            self.mode = m.get('mode')
        if m.get('path_type') is not None:
            self.path_type = m.get('path_type')
        if m.get('published_app_access_strategy') is not None:
            temp_model = AppAccessStrategy()
            self.published_app_access_strategy = temp_model.from_map(m['published_app_access_strategy'])
        if m.get('sharable') is not None:
            self.sharable = m.get('sharable')
        if m.get('store_level') is not None:
            self.store_level = m.get('store_level')
        if m.get('store_region_list') is not None:
            self.store_region_list = m.get('store_region_list')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        return self


class CreateSubdomainRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        description: str = None,
        name: str = None,
        total_size: int = None,
        user_quota: int = None,
    ):
        self.headers = headers
        # 描述
        self.description = description
        # 名称，注意该字段会校验重名的subdomain
        self.name = name
        # 逻辑空间quota，默认为-1，无限制，单位为字节
        self.total_size = total_size
        # 用户数quota，默认为-1，无限制
        self.user_quota = user_quota

    def validate(self):
        self.validate_required(self.name, 'name')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.total_size is not None:
            result['total_size'] = self.total_size
        if self.user_quota is not None:
            result['user_quota'] = self.user_quota
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('total_size') is not None:
            self.total_size = m.get('total_size')
        if m.get('user_quota') is not None:
            self.user_quota = m.get('user_quota')
        return self


class DataCName(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        data_cname: str = None,
        location: str = None,
    ):
        # datacname
        self.data_cname = data_cname
        # data location
        self.location = location

    def validate(self):
        self.validate_required(self.data_cname, 'data_cname')
        self.validate_required(self.location, 'location')

    def to_map(self):
        result = dict()
        if self.data_cname is not None:
            result['data_cname'] = self.data_cname
        if self.location is not None:
            result['location'] = self.location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data_cname') is not None:
            self.data_cname = m.get('data_cname')
        if m.get('location') is not None:
            self.location = m.get('location')
        return self


class DeleteSubdomainRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        subdomain_id: str = None,
    ):
        self.headers = headers
        # 用以唯一标识subdomain
        self.subdomain_id = subdomain_id

    def validate(self):
        self.validate_required(self.subdomain_id, 'subdomain_id')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.subdomain_id is not None:
            result['subdomain_id'] = self.subdomain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('subdomain_id') is not None:
            self.subdomain_id = m.get('subdomain_id')
        return self


class DomainCNameResponse(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        data_cname_list: List[DataCName] = None,
        domain_id: str = None,
    ):
        # data cname list
        self.data_cname_list = data_cname_list
        # domain ID
        self.domain_id = domain_id

    def validate(self):
        self.validate_required(self.data_cname_list, 'data_cname_list')
        if self.data_cname_list:
            for k in self.data_cname_list:
                if k:
                    k.validate()
        self.validate_required(self.domain_id, 'domain_id')

    def to_map(self):
        result = dict()
        result['data_cname_list'] = []
        if self.data_cname_list is not None:
            for k in self.data_cname_list:
                result['data_cname_list'].append(k.to_map() if k else None)
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_cname_list = []
        if m.get('data_cname_list') is not None:
            for k in m.get('data_cname_list'):
                temp_model = DataCName()
                self.data_cname_list.append(temp_model.from_map(k))
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        return self


class GetAppPublicKeyResponse(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        app_id: str = None,
        public_key: str = None,
    ):
        # App ID
        self.app_id = app_id
        # RSA加密算法的公钥, PEM格式
        self.public_key = public_key

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.public_key, 'public_key')

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['app_id'] = self.app_id
        if self.public_key is not None:
            result['public_key'] = self.public_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('app_id') is not None:
            self.app_id = m.get('app_id')
        if m.get('public_key') is not None:
            self.public_key = m.get('public_key')
        return self


class GetAppResponse(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        ali_owner_id: str = None,
        app_id: str = None,
        app_name: str = None,
        app_secret: str = None,
        created_at: str = None,
        description: str = None,
        logo: str = None,
        provider: str = None,
        redirect_uri: str = None,
        scope: List[str] = None,
        screenshots: List[str] = None,
        stage: str = None,
        type: str = None,
        updated_at: str = None,
    ):
        # App 拥有者
        self.ali_owner_id = ali_owner_id
        # App ID
        self.app_id = app_id
        # App名称
        self.app_name = app_name
        # App 秘钥
        self.app_secret = app_secret
        # App 创建时间
        self.created_at = created_at
        # App描述
        self.description = description
        # App图标
        self.logo = logo
        # App 提供方
        self.provider = provider
        # App回调地址
        self.redirect_uri = redirect_uri
        # App权限列表
        self.scope = scope
        # App 屏幕截图
        self.screenshots = screenshots
        # App 当前阶段
        self.stage = stage
        # App类型
        self.type = type
        # App 修改时间
        self.updated_at = updated_at

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
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ali_owner_id') is not None:
            self.ali_owner_id = m.get('ali_owner_id')
        if m.get('app_id') is not None:
            self.app_id = m.get('app_id')
        if m.get('app_name') is not None:
            self.app_name = m.get('app_name')
        if m.get('app_secret') is not None:
            self.app_secret = m.get('app_secret')
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('logo') is not None:
            self.logo = m.get('logo')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('redirect_uri') is not None:
            self.redirect_uri = m.get('redirect_uri')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('screenshots') is not None:
            self.screenshots = m.get('screenshots')
        if m.get('stage') is not None:
            self.stage = m.get('stage')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        return self


class GetBizCNameInfoResponse(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        biz_cname: str = None,
        cert_id: str = None,
        cert_name: str = None,
        cname_status: CNameStatus = None,
        cname_type: str = None,
        domain_id: str = None,
        is_vpc: bool = None,
    ):
        # biz cname
        self.biz_cname = biz_cname
        # cert name
        self.cert_id = cert_id
        # cert name
        self.cert_name = cert_name
        self.cname_status = cname_status
        # cname type
        self.cname_type = cname_type
        # domain ID
        self.domain_id = domain_id
        # is vpc
        self.is_vpc = is_vpc

    def validate(self):
        if self.cname_status:
            self.cname_status.validate()
        self.validate_required(self.domain_id, 'domain_id')

    def to_map(self):
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('biz_cname') is not None:
            self.biz_cname = m.get('biz_cname')
        if m.get('cert_id') is not None:
            self.cert_id = m.get('cert_id')
        if m.get('cert_name') is not None:
            self.cert_name = m.get('cert_name')
        if m.get('cname_status') is not None:
            temp_model = CNameStatus()
            self.cname_status = temp_model.from_map(m['cname_status'])
        if m.get('cname_type') is not None:
            self.cname_type = m.get('cname_type')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('is_vpc') is not None:
            self.is_vpc = m.get('is_vpc')
        return self


class GetDomainResponse(TeaModel):
    """
    get domain response
    """
    def __init__(
        self,
        api_cname: str = None,
        app_cname: str = None,
        auth_alipay_app_id: str = None,
        auth_alipay_enable: bool = None,
        auth_alipay_private_key: str = None,
        auth_cname: str = None,
        auth_config: dict = None,
        auth_dingding_app_id: str = None,
        auth_dingding_app_secret: str = None,
        auth_dingding_enable: bool = None,
        auth_endpoint_enable: bool = None,
        auth_ram_app_id: str = None,
        auth_ram_app_secret: str = None,
        auth_ram_enable: bool = None,
        created_at: str = None,
        data_hash_name: str = None,
        description: str = None,
        domain_id: str = None,
        domain_name: str = None,
        event_filename_matches: str = None,
        event_mns_endpoint: str = None,
        event_mns_topic: str = None,
        event_names: List[str] = None,
        event_role_arn: str = None,
        init_drive_enable: bool = None,
        init_drive_size: int = None,
        init_drive_store_id: str = None,
        mode: str = None,
        path_type: str = None,
        published_app_access_strategy: AppAccessStrategy = None,
        sharable: bool = None,
        store_level: str = None,
        store_region_list: List[str] = None,
        updated_at: str = None,
    ):
        # Domain APICName
        self.api_cname = api_cname
        # Domain AppCName
        self.app_cname = app_cname
        # 支付宝 App Id
        self.auth_alipay_app_id = auth_alipay_app_id
        # 是否开启了支付宝认证
        self.auth_alipay_enable = auth_alipay_enable
        # 支付宝 App Secret
        self.auth_alipay_private_key = auth_alipay_private_key
        # Domain AuthCName
        self.auth_cname = auth_cname
        # 登录相关信息
        self.auth_config = auth_config
        # 钉钉 App Id
        self.auth_dingding_app_id = auth_dingding_app_id
        # 钉钉 App Secret
        self.auth_dingding_app_secret = auth_dingding_app_secret
        # 是否开启了钉钉认证
        self.auth_dingding_enable = auth_dingding_enable
        self.auth_endpoint_enable = auth_endpoint_enable
        # RAM App Id
        self.auth_ram_app_id = auth_ram_app_id
        # RAM App Secret
        self.auth_ram_app_secret = auth_ram_app_secret
        # 是否开启了 RAM 认证
        self.auth_ram_enable = auth_ram_enable
        # Domain 创建时间
        self.created_at = created_at
        # 数据 Hash 算法
        self.data_hash_name = data_hash_name
        # Domain 描述
        self.description = description
        # Domain ID
        self.domain_id = domain_id
        # Domain 描述
        self.domain_name = domain_name
        # 事件通知 MNS 匹配文件名
        self.event_filename_matches = event_filename_matches
        # 事件通知 MNS Endpoint
        self.event_mns_endpoint = event_mns_endpoint
        # 事件通知 MNS Topic
        self.event_mns_topic = event_mns_topic
        # 事件名列表
        self.event_names = event_names
        # 事件通知 Role Arn
        self.event_role_arn = event_role_arn
        # 是否开启了自动初始化 Drive
        self.init_drive_enable = init_drive_enable
        # 自动初始化 Drive 大小
        self.init_drive_size = init_drive_size
        # 自动初始化 Drive 所用 Store ID
        self.init_drive_store_id = init_drive_store_id
        # Domain 类型
        self.mode = mode
        # Domain 类型
        self.path_type = path_type
        self.published_app_access_strategy = published_app_access_strategy
        # 是否开启了分享
        self.sharable = sharable
        # 存储级别
        self.store_level = store_level
        # 存储 Region 列表
        self.store_region_list = store_region_list
        # Domain 更新时间
        self.updated_at = updated_at

    def validate(self):
        if self.published_app_access_strategy:
            self.published_app_access_strategy.validate()

    def to_map(self):
        result = dict()
        if self.api_cname is not None:
            result['api_cname'] = self.api_cname
        if self.app_cname is not None:
            result['app_cname'] = self.app_cname
        if self.auth_alipay_app_id is not None:
            result['auth_alipay_app_id'] = self.auth_alipay_app_id
        if self.auth_alipay_enable is not None:
            result['auth_alipay_enable'] = self.auth_alipay_enable
        if self.auth_alipay_private_key is not None:
            result['auth_alipay_private_key'] = self.auth_alipay_private_key
        if self.auth_cname is not None:
            result['auth_cname'] = self.auth_cname
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('api_cname') is not None:
            self.api_cname = m.get('api_cname')
        if m.get('app_cname') is not None:
            self.app_cname = m.get('app_cname')
        if m.get('auth_alipay_app_id') is not None:
            self.auth_alipay_app_id = m.get('auth_alipay_app_id')
        if m.get('auth_alipay_enable') is not None:
            self.auth_alipay_enable = m.get('auth_alipay_enable')
        if m.get('auth_alipay_private_key') is not None:
            self.auth_alipay_private_key = m.get('auth_alipay_private_key')
        if m.get('auth_cname') is not None:
            self.auth_cname = m.get('auth_cname')
        if m.get('auth_config') is not None:
            self.auth_config = m.get('auth_config')
        if m.get('auth_dingding_app_id') is not None:
            self.auth_dingding_app_id = m.get('auth_dingding_app_id')
        if m.get('auth_dingding_app_secret') is not None:
            self.auth_dingding_app_secret = m.get('auth_dingding_app_secret')
        if m.get('auth_dingding_enable') is not None:
            self.auth_dingding_enable = m.get('auth_dingding_enable')
        if m.get('auth_endpoint_enable') is not None:
            self.auth_endpoint_enable = m.get('auth_endpoint_enable')
        if m.get('auth_ram_app_id') is not None:
            self.auth_ram_app_id = m.get('auth_ram_app_id')
        if m.get('auth_ram_app_secret') is not None:
            self.auth_ram_app_secret = m.get('auth_ram_app_secret')
        if m.get('auth_ram_enable') is not None:
            self.auth_ram_enable = m.get('auth_ram_enable')
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('data_hash_name') is not None:
            self.data_hash_name = m.get('data_hash_name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('domain_name') is not None:
            self.domain_name = m.get('domain_name')
        if m.get('event_filename_matches') is not None:
            self.event_filename_matches = m.get('event_filename_matches')
        if m.get('event_mns_endpoint') is not None:
            self.event_mns_endpoint = m.get('event_mns_endpoint')
        if m.get('event_mns_topic') is not None:
            self.event_mns_topic = m.get('event_mns_topic')
        if m.get('event_names') is not None:
            self.event_names = m.get('event_names')
        if m.get('event_role_arn') is not None:
            self.event_role_arn = m.get('event_role_arn')
        if m.get('init_drive_enable') is not None:
            self.init_drive_enable = m.get('init_drive_enable')
        if m.get('init_drive_size') is not None:
            self.init_drive_size = m.get('init_drive_size')
        if m.get('init_drive_store_id') is not None:
            self.init_drive_store_id = m.get('init_drive_store_id')
        if m.get('mode') is not None:
            self.mode = m.get('mode')
        if m.get('path_type') is not None:
            self.path_type = m.get('path_type')
        if m.get('published_app_access_strategy') is not None:
            temp_model = AppAccessStrategy()
            self.published_app_access_strategy = temp_model.from_map(m['published_app_access_strategy'])
        if m.get('sharable') is not None:
            self.sharable = m.get('sharable')
        if m.get('store_level') is not None:
            self.store_level = m.get('store_level')
        if m.get('store_region_list') is not None:
            self.store_region_list = m.get('store_region_list')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        return self


class GetSubdomainRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        subdomain_id: str = None,
    ):
        self.headers = headers
        # 用以唯一标识subdomain
        self.subdomain_id = subdomain_id

    def validate(self):
        self.validate_required(self.subdomain_id, 'subdomain_id')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.subdomain_id is not None:
            result['subdomain_id'] = self.subdomain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('subdomain_id') is not None:
            self.subdomain_id = m.get('subdomain_id')
        return self


class GetUserAccessTokenRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        subdomain_id: str = None,
        user_id: str = None,
    ):
        self.headers = headers
        # subdomain ID
        self.subdomain_id = subdomain_id
        # 用户 ID
        self.user_id = user_id

    def validate(self):
        self.validate_required(self.user_id, 'user_id')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.subdomain_id is not None:
            result['subdomain_id'] = self.subdomain_id
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('subdomain_id') is not None:
            self.subdomain_id = m.get('subdomain_id')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class ListAppsResponse(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        items: List[GetAppResponse] = None,
        next_marker: str = None,
    ):
        # App 列表
        self.items = items
        # App 分批查询游标
        self.next_marker = next_marker

    def validate(self):
        self.validate_required(self.items, 'items')
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = GetAppResponse()
                self.items.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        return self


class ListDomainCORSRuleResponse(TeaModel):
    """
    list domain cors response
    """
    def __init__(
        self,
        cors_rule_list: List[CorsRule] = None,
        domain_id: str = None,
    ):
        # cors rule 列表
        self.cors_rule_list = cors_rule_list
        # Domain ID
        self.domain_id = domain_id

    def validate(self):
        if self.cors_rule_list:
            for k in self.cors_rule_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['cors_rule_list'] = []
        if self.cors_rule_list is not None:
            for k in self.cors_rule_list:
                result['cors_rule_list'].append(k.to_map() if k else None)
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cors_rule_list = []
        if m.get('cors_rule_list') is not None:
            for k in m.get('cors_rule_list'):
                temp_model = CorsRule()
                self.cors_rule_list.append(temp_model.from_map(k))
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        return self


class ListDomainsResponse(TeaModel):
    """
    list domain response
    """
    def __init__(
        self,
        items: List[BaseDomainResponse] = None,
        next_marker: str = None,
    ):
        # domain 列表
        self.items = items
        # 下次分页查询游标
        self.next_marker = next_marker

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = BaseDomainResponse()
                self.items.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        return self


class ListSubdomainsRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        limit: int = None,
        marker: str = None,
    ):
        self.headers = headers
        # 数量，默认为50
        self.limit = limit
        # 分页游标，可从 response 中获取
        self.marker = marker

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        return self


class SetBizCNameCertResponse(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        biz_cname: str = None,
        cert_name: str = None,
        cname_type: str = None,
        domain_id: str = None,
        is_vpc: bool = None,
    ):
        # biz cname
        self.biz_cname = biz_cname
        # cert name
        self.cert_name = cert_name
        # cname type
        self.cname_type = cname_type
        # domain ID
        self.domain_id = domain_id
        # is vpc
        self.is_vpc = is_vpc

    def validate(self):
        self.validate_required(self.domain_id, 'domain_id')

    def to_map(self):
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('biz_cname') is not None:
            self.biz_cname = m.get('biz_cname')
        if m.get('cert_name') is not None:
            self.cert_name = m.get('cert_name')
        if m.get('cname_type') is not None:
            self.cname_type = m.get('cname_type')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('is_vpc') is not None:
            self.is_vpc = m.get('is_vpc')
        return self


class SetBizCNameResponse(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        biz_cname: str = None,
        cname_status: CNameStatus = None,
        cname_type: str = None,
        domain_id: str = None,
        is_vpc: bool = None,
    ):
        # biz cname
        self.biz_cname = biz_cname
        self.cname_status = cname_status
        # cname type
        self.cname_type = cname_type
        # domain ID
        self.domain_id = domain_id
        # is vpc
        self.is_vpc = is_vpc

    def validate(self):
        if self.cname_status:
            self.cname_status.validate()
        self.validate_required(self.domain_id, 'domain_id')

    def to_map(self):
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('biz_cname') is not None:
            self.biz_cname = m.get('biz_cname')
        if m.get('cname_status') is not None:
            temp_model = CNameStatus()
            self.cname_status = temp_model.from_map(m['cname_status'])
        if m.get('cname_type') is not None:
            self.cname_type = m.get('cname_type')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('is_vpc') is not None:
            self.is_vpc = m.get('is_vpc')
        return self


class SetDataCNameResponse(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        data_cname: str = None,
        domain_id: str = None,
        location: str = None,
    ):
        # datacname
        self.data_cname = data_cname
        # domain ID
        self.domain_id = domain_id
        # data location
        self.location = location

    def validate(self):
        self.validate_required(self.data_cname, 'data_cname')
        self.validate_required(self.domain_id, 'domain_id')
        self.validate_required(self.location, 'location')

    def to_map(self):
        result = dict()
        if self.data_cname is not None:
            result['data_cname'] = self.data_cname
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.location is not None:
            result['location'] = self.location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data_cname') is not None:
            self.data_cname = m.get('data_cname')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('location') is not None:
            self.location = m.get('location')
        return self


class UpdateDomainResponse(TeaModel):
    """
    create domain response
    """
    def __init__(
        self,
        api_cname: str = None,
        app_cname: str = None,
        auth_alipay_app_id: str = None,
        auth_alipay_enable: bool = None,
        auth_alipay_private_key: str = None,
        auth_cname: str = None,
        auth_config: dict = None,
        auth_dingding_app_id: str = None,
        auth_dingding_app_secret: str = None,
        auth_dingding_enable: bool = None,
        auth_endpoint_enable: bool = None,
        auth_ram_app_id: str = None,
        auth_ram_app_secret: str = None,
        auth_ram_enable: bool = None,
        created_at: str = None,
        data_hash_name: str = None,
        description: str = None,
        domain_id: str = None,
        domain_name: str = None,
        event_filename_matches: str = None,
        event_mns_endpoint: str = None,
        event_mns_topic: str = None,
        event_names: List[str] = None,
        event_role_arn: str = None,
        init_drive_enable: bool = None,
        init_drive_size: int = None,
        init_drive_store_id: str = None,
        mode: str = None,
        path_type: str = None,
        published_app_access_strategy: AppAccessStrategy = None,
        sharable: bool = None,
        store_level: str = None,
        store_region_list: List[str] = None,
        updated_at: str = None,
    ):
        # Domain APICName
        self.api_cname = api_cname
        # Domain AppCName
        self.app_cname = app_cname
        # 支付宝 App Id
        self.auth_alipay_app_id = auth_alipay_app_id
        # 是否开启了支付宝认证
        self.auth_alipay_enable = auth_alipay_enable
        # 支付宝 App Secret
        self.auth_alipay_private_key = auth_alipay_private_key
        # Domain AuthCName
        self.auth_cname = auth_cname
        # 登录相关信息
        self.auth_config = auth_config
        # 钉钉 App Id
        self.auth_dingding_app_id = auth_dingding_app_id
        # 钉钉 App Secret
        self.auth_dingding_app_secret = auth_dingding_app_secret
        # 是否开启了钉钉认证
        self.auth_dingding_enable = auth_dingding_enable
        self.auth_endpoint_enable = auth_endpoint_enable
        # RAM App Id
        self.auth_ram_app_id = auth_ram_app_id
        # RAM App Secret
        self.auth_ram_app_secret = auth_ram_app_secret
        # 是否开启了 RAM 认证
        self.auth_ram_enable = auth_ram_enable
        # Domain 创建时间
        self.created_at = created_at
        # 数据 Hash 算法
        self.data_hash_name = data_hash_name
        # Domain 描述
        self.description = description
        # Domain ID
        self.domain_id = domain_id
        # Domain 描述
        self.domain_name = domain_name
        # 事件通知 MNS 匹配文件名
        self.event_filename_matches = event_filename_matches
        # 事件通知 MNS Endpoint
        self.event_mns_endpoint = event_mns_endpoint
        # 事件通知 MNS Topic
        self.event_mns_topic = event_mns_topic
        # 事件名列表
        self.event_names = event_names
        # 事件通知 Role Arn
        self.event_role_arn = event_role_arn
        # 是否开启了自动初始化 Drive
        self.init_drive_enable = init_drive_enable
        # 自动初始化 Drive 大小
        self.init_drive_size = init_drive_size
        # 自动初始化 Drive 所用 Store ID
        self.init_drive_store_id = init_drive_store_id
        # Domain 类型
        self.mode = mode
        # Domain 类型
        self.path_type = path_type
        self.published_app_access_strategy = published_app_access_strategy
        # 是否开启了分享
        self.sharable = sharable
        # 存储级别
        self.store_level = store_level
        # 存储 Region 列表
        self.store_region_list = store_region_list
        # Domain 更新时间
        self.updated_at = updated_at

    def validate(self):
        if self.published_app_access_strategy:
            self.published_app_access_strategy.validate()

    def to_map(self):
        result = dict()
        if self.api_cname is not None:
            result['api_cname'] = self.api_cname
        if self.app_cname is not None:
            result['app_cname'] = self.app_cname
        if self.auth_alipay_app_id is not None:
            result['auth_alipay_app_id'] = self.auth_alipay_app_id
        if self.auth_alipay_enable is not None:
            result['auth_alipay_enable'] = self.auth_alipay_enable
        if self.auth_alipay_private_key is not None:
            result['auth_alipay_private_key'] = self.auth_alipay_private_key
        if self.auth_cname is not None:
            result['auth_cname'] = self.auth_cname
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('api_cname') is not None:
            self.api_cname = m.get('api_cname')
        if m.get('app_cname') is not None:
            self.app_cname = m.get('app_cname')
        if m.get('auth_alipay_app_id') is not None:
            self.auth_alipay_app_id = m.get('auth_alipay_app_id')
        if m.get('auth_alipay_enable') is not None:
            self.auth_alipay_enable = m.get('auth_alipay_enable')
        if m.get('auth_alipay_private_key') is not None:
            self.auth_alipay_private_key = m.get('auth_alipay_private_key')
        if m.get('auth_cname') is not None:
            self.auth_cname = m.get('auth_cname')
        if m.get('auth_config') is not None:
            self.auth_config = m.get('auth_config')
        if m.get('auth_dingding_app_id') is not None:
            self.auth_dingding_app_id = m.get('auth_dingding_app_id')
        if m.get('auth_dingding_app_secret') is not None:
            self.auth_dingding_app_secret = m.get('auth_dingding_app_secret')
        if m.get('auth_dingding_enable') is not None:
            self.auth_dingding_enable = m.get('auth_dingding_enable')
        if m.get('auth_endpoint_enable') is not None:
            self.auth_endpoint_enable = m.get('auth_endpoint_enable')
        if m.get('auth_ram_app_id') is not None:
            self.auth_ram_app_id = m.get('auth_ram_app_id')
        if m.get('auth_ram_app_secret') is not None:
            self.auth_ram_app_secret = m.get('auth_ram_app_secret')
        if m.get('auth_ram_enable') is not None:
            self.auth_ram_enable = m.get('auth_ram_enable')
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('data_hash_name') is not None:
            self.data_hash_name = m.get('data_hash_name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('domain_name') is not None:
            self.domain_name = m.get('domain_name')
        if m.get('event_filename_matches') is not None:
            self.event_filename_matches = m.get('event_filename_matches')
        if m.get('event_mns_endpoint') is not None:
            self.event_mns_endpoint = m.get('event_mns_endpoint')
        if m.get('event_mns_topic') is not None:
            self.event_mns_topic = m.get('event_mns_topic')
        if m.get('event_names') is not None:
            self.event_names = m.get('event_names')
        if m.get('event_role_arn') is not None:
            self.event_role_arn = m.get('event_role_arn')
        if m.get('init_drive_enable') is not None:
            self.init_drive_enable = m.get('init_drive_enable')
        if m.get('init_drive_size') is not None:
            self.init_drive_size = m.get('init_drive_size')
        if m.get('init_drive_store_id') is not None:
            self.init_drive_store_id = m.get('init_drive_store_id')
        if m.get('mode') is not None:
            self.mode = m.get('mode')
        if m.get('path_type') is not None:
            self.path_type = m.get('path_type')
        if m.get('published_app_access_strategy') is not None:
            temp_model = AppAccessStrategy()
            self.published_app_access_strategy = temp_model.from_map(m['published_app_access_strategy'])
        if m.get('sharable') is not None:
            self.sharable = m.get('sharable')
        if m.get('store_level') is not None:
            self.store_level = m.get('store_level')
        if m.get('store_region_list') is not None:
            self.store_region_list = m.get('store_region_list')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        return self


class UpdateSubdomainRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        description: str = None,
        name: str = None,
        subdomain_id: str = None,
        total_size: int = None,
        user_quota: int = None,
    ):
        self.headers = headers
        # 描述
        self.description = description
        # 名称
        self.name = name
        # 用以唯一标识subdomain
        self.subdomain_id = subdomain_id
        # 逻辑空间quota，-1表示无限制，单位为字节
        self.total_size = total_size
        # 用户数quota，-1表示无限制
        self.user_quota = user_quota

    def validate(self):
        self.validate_required(self.subdomain_id, 'subdomain_id')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.subdomain_id is not None:
            result['subdomain_id'] = self.subdomain_id
        if self.total_size is not None:
            result['total_size'] = self.total_size
        if self.user_quota is not None:
            result['user_quota'] = self.user_quota
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('subdomain_id') is not None:
            self.subdomain_id = m.get('subdomain_id')
        if m.get('total_size') is not None:
            self.total_size = m.get('total_size')
        if m.get('user_quota') is not None:
            self.user_quota = m.get('user_quota')
        return self


class GetAsyncTaskInfoModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAsyncTaskResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAsyncTaskResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchOperationModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = BatchResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDriveModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDriveResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateDriveResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDriveModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class GetDriveModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDriveResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetDriveResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDefaultDriveModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDriveResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetDriveResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDrivesModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDriveResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDriveResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMyDrivesModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDriveResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDriveResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDriveModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateDriveResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateDriveResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class CompleteFileModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CompleteFileResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CompleteFileResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class CopyFileModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CopyFileResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CopyFileResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFileModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateFileResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateFileResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFileModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteFileResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteFileResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFileModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetFileResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetFileResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFileByPathModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetFileByPathResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetFileByPathResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDownloadUrlModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDownloadUrlResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetDownloadUrlResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLastCursorModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetLastCursorResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetLastCursorResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMediaPlayUrlModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetMediaPlayURLResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetMediaPlayURLResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOfficeEditUrlModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetOfficeEditUrlResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetOfficeEditUrlResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOfficePreviewUrlModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetOfficePreviewUrlResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetOfficePreviewUrlResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUploadUrlModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetUploadUrlResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetUploadUrlResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVideoPreviewSpriteUrlModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetVideoPreviewSpriteURLResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetVideoPreviewSpriteURLResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVideoPreviewUrlModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetVideoPreviewURLResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetVideoPreviewURLResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFileModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListFileResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListFileResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFileByAnonymousModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListByAnonymousResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListByAnonymousResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFileByCustomIndexKeyModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListFileResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListFileResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFileDeltaModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListFileDeltaResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListFileDeltaResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUploadedPartsModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListUploadedPartResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListUploadedPartResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class MoveFileModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: MoveFileResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = MoveFileResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class TokenModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RefreshOfficeEditTokenResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RefreshOfficeEditTokenResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class ScanFileMetaModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ScanFileMetaResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ScanFileMetaResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchFileModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SearchFileResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SearchFileResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFileModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateFileMetaResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateFileMetaResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateShareModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateShareResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateShareResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteShareModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class GetShareModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetShareResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetShareResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class ListShareModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListShareResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListShareResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateShareModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateShareResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateShareResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelShareLinkModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class CreateShareLinkModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateShareLinkResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateShareLinkResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class GetShareByAnonymousModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetShareLinkByAnonymousResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetShareLinkByAnonymousResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class GetShareIdModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetShareLinkIDResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetShareLinkIDResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class GetShareTokenModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetShareLinkTokenResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetShareLinkTokenResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class ListShareLinkModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListShareLinkResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListShareLinkResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateShareLinkModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateShareLinkResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateShareLinkResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class BaseCompleteFileRequest(TeaModel):
    """
    complete file request
    """
    def __init__(
        self,
        addition_data: dict = None,
        drive_id: str = None,
        part_info_list: List[UploadPartInfo] = None,
        share_id: str = None,
        upload_id: str = None,
    ):
        # addition_data
        self.addition_data = addition_data
        # drive_id
        self.drive_id = drive_id
        # part_info_list
        self.part_info_list = part_info_list
        self.share_id = share_id
        # upload_id
        self.upload_id = upload_id

    def validate(self):
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.part_info_list:
            for k in self.part_info_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.addition_data is not None:
            result['addition_data'] = self.addition_data
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k in self.part_info_list:
                result['part_info_list'].append(k.to_map() if k else None)
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.upload_id is not None:
            result['upload_id'] = self.upload_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('addition_data') is not None:
            self.addition_data = m.get('addition_data')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        self.part_info_list = []
        if m.get('part_info_list') is not None:
            for k in m.get('part_info_list'):
                temp_model = UploadPartInfo()
                self.part_info_list.append(temp_model.from_map(k))
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('upload_id') is not None:
            self.upload_id = m.get('upload_id')
        return self


class BaseCreateFileRequest(TeaModel):
    """
    create file request
    """
    def __init__(
        self,
        addition_data: dict = None,
        content_md_5: str = None,
        content_type: str = None,
        name: str = None,
        part_info_list: List[UploadPartInfo] = None,
        size: int = None,
        type: str = None,
    ):
        # addition_data
        self.addition_data = addition_data
        # ContentMd5
        self.content_md_5 = content_md_5
        # ContentType
        self.content_type = content_type
        # Name
        self.name = name
        # part_info_list
        self.part_info_list = part_info_list
        # Size
        self.size = size
        # Type
        self.type = type

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
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('addition_data') is not None:
            self.addition_data = m.get('addition_data')
        if m.get('content_md5') is not None:
            self.content_md_5 = m.get('content_md5')
        if m.get('content_type') is not None:
            self.content_type = m.get('content_type')
        if m.get('name') is not None:
            self.name = m.get('name')
        self.part_info_list = []
        if m.get('part_info_list') is not None:
            for k in m.get('part_info_list'):
                temp_model = UploadPartInfo()
                self.part_info_list.append(temp_model.from_map(k))
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class BaseFileProcessRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        image_cropping_aspect_ratios: List[str] = None,
        image_thumbnail_process: str = None,
        image_url_process: str = None,
        video_thumbnail_process: str = None,
    ):
        self.image_cropping_aspect_ratios = image_cropping_aspect_ratios
        # image_thumbnail_process
        self.image_thumbnail_process = image_thumbnail_process
        # image_url_process
        self.image_url_process = image_url_process
        # video_thumbnail_process
        # type:string
        self.video_thumbnail_process = video_thumbnail_process

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_cropping_aspect_ratios is not None:
            result['image_cropping_aspect_ratios'] = self.image_cropping_aspect_ratios
        if self.image_thumbnail_process is not None:
            result['image_thumbnail_process'] = self.image_thumbnail_process
        if self.image_url_process is not None:
            result['image_url_process'] = self.image_url_process
        if self.video_thumbnail_process is not None:
            result['video_thumbnail_process'] = self.video_thumbnail_process
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('image_cropping_aspect_ratios') is not None:
            self.image_cropping_aspect_ratios = m.get('image_cropping_aspect_ratios')
        if m.get('image_thumbnail_process') is not None:
            self.image_thumbnail_process = m.get('image_thumbnail_process')
        if m.get('image_url_process') is not None:
            self.image_url_process = m.get('image_url_process')
        if m.get('video_thumbnail_process') is not None:
            self.video_thumbnail_process = m.get('video_thumbnail_process')
        return self


class BaseFileRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        addition_data: dict = None,
    ):
        # addition_data
        self.addition_data = addition_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.addition_data is not None:
            result['addition_data'] = self.addition_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('addition_data') is not None:
            self.addition_data = m.get('addition_data')
        return self


class BaseGetUploadUrlRequest(TeaModel):
    """
    获取文件上传URL
    """
    def __init__(
        self,
        content_md_5: str = None,
        drive_id: str = None,
        part_info_list: List[UploadPartInfo] = None,
        share_id: str = None,
        upload_id: str = None,
    ):
        # content_md5
        self.content_md_5 = content_md_5
        # drive_id
        self.drive_id = drive_id
        # upload_part_list
        self.part_info_list = part_info_list
        self.share_id = share_id
        # upload_id
        self.upload_id = upload_id

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
        result = dict()
        if self.content_md_5 is not None:
            result['content_md5'] = self.content_md_5
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k in self.part_info_list:
                result['part_info_list'].append(k.to_map() if k else None)
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.upload_id is not None:
            result['upload_id'] = self.upload_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content_md5') is not None:
            self.content_md_5 = m.get('content_md5')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        self.part_info_list = []
        if m.get('part_info_list') is not None:
            for k in m.get('part_info_list'):
                temp_model = UploadPartInfo()
                self.part_info_list.append(temp_model.from_map(k))
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('upload_id') is not None:
            self.upload_id = m.get('upload_id')
        return self


class BaseImageProcessRequest(TeaModel):
    """
    Base image process
    """
    def __init__(
        self,
        image_thumbnail_process: str = None,
        image_url_process: str = None,
        video_thumbnail_process: str = None,
    ):
        # image_thumbnail_process
        self.image_thumbnail_process = image_thumbnail_process
        # image_url_process
        self.image_url_process = image_url_process
        # video_thumbnail_process
        # type:string
        self.video_thumbnail_process = video_thumbnail_process

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_thumbnail_process is not None:
            result['image_thumbnail_process'] = self.image_thumbnail_process
        if self.image_url_process is not None:
            result['image_url_process'] = self.image_url_process
        if self.video_thumbnail_process is not None:
            result['video_thumbnail_process'] = self.video_thumbnail_process
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('image_thumbnail_process') is not None:
            self.image_thumbnail_process = m.get('image_thumbnail_process')
        if m.get('image_url_process') is not None:
            self.image_url_process = m.get('image_url_process')
        if m.get('video_thumbnail_process') is not None:
            self.video_thumbnail_process = m.get('video_thumbnail_process')
        return self


class BaseListFileRequest(TeaModel):
    """
    list file request
    """
    def __init__(
        self,
        addition_data: dict = None,
        drive_id: str = None,
        image_cropping_aspect_ratios: List[str] = None,
        image_thumbnail_process: str = None,
        image_url_process: str = None,
        limit: int = None,
        marker: str = None,
        referer: str = None,
        share_id: str = None,
        sign_token: str = None,
        video_thumbnail_process: str = None,
    ):
        # addition_data
        self.addition_data = addition_data
        # drive_id
        self.drive_id = drive_id
        self.image_cropping_aspect_ratios = image_cropping_aspect_ratios
        # image_thumbnail_process
        self.image_thumbnail_process = image_thumbnail_process
        # image_url_process
        self.image_url_process = image_url_process
        # limit
        self.limit = limit
        # marker
        self.marker = marker
        self.referer = referer
        # share_id, either share_id or drive_id is required
        self.share_id = share_id
        self.sign_token = sign_token
        # video_thumbnail_process
        # type:string
        self.video_thumbnail_process = video_thumbnail_process

    def validate(self):
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.limit is not None:
            self.validate_maximum(self.limit, 'limit', 100)
            self.validate_minimum(self.limit, 'limit', 0)

    def to_map(self):
        result = dict()
        if self.addition_data is not None:
            result['addition_data'] = self.addition_data
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.image_cropping_aspect_ratios is not None:
            result['image_cropping_aspect_ratios'] = self.image_cropping_aspect_ratios
        if self.image_thumbnail_process is not None:
            result['image_thumbnail_process'] = self.image_thumbnail_process
        if self.image_url_process is not None:
            result['image_url_process'] = self.image_url_process
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        if self.referer is not None:
            result['referer'] = self.referer
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.sign_token is not None:
            result['sign_token'] = self.sign_token
        if self.video_thumbnail_process is not None:
            result['video_thumbnail_process'] = self.video_thumbnail_process
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('addition_data') is not None:
            self.addition_data = m.get('addition_data')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('image_cropping_aspect_ratios') is not None:
            self.image_cropping_aspect_ratios = m.get('image_cropping_aspect_ratios')
        if m.get('image_thumbnail_process') is not None:
            self.image_thumbnail_process = m.get('image_thumbnail_process')
        if m.get('image_url_process') is not None:
            self.image_url_process = m.get('image_url_process')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('referer') is not None:
            self.referer = m.get('referer')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('sign_token') is not None:
            self.sign_token = m.get('sign_token')
        if m.get('video_thumbnail_process') is not None:
            self.video_thumbnail_process = m.get('video_thumbnail_process')
        return self


class BaseMoveFileRequest(TeaModel):
    """
    文件移动请求
    """
    def __init__(
        self,
        drive_id: str = None,
        new_name: str = None,
        share_id: str = None,
    ):
        # drive_id
        self.drive_id = drive_id
        # new_name
        self.new_name = new_name
        self.share_id = share_id

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.new_name is not None:
            self.validate_max_length(self.new_name, 'new_name', 1024)

    def to_map(self):
        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.new_name is not None:
            result['new_name'] = self.new_name
        if self.share_id is not None:
            result['share_id'] = self.share_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('new_name') is not None:
            self.new_name = m.get('new_name')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        return self


class BatchSubRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        body: dict = None,
        headers: dict = None,
        id: str = None,
        method: str = None,
        url: str = None,
    ):
        # body 子请求的请求参数 json 字符串，可参考对于子请求文档, 当指定了body 必须传headers ： "Content-Type" 对应的类型，目前子请求入参是"application/json"
        self.body = body
        # headers 请求头，表示body传入数据的类型
        self.headers = headers
        # id 用于request 和 response关联， 不允许重复
        self.id = id
        # method
        self.method = method
        # url 子请求的api path路径， 可参考对于子请求文档
        self.url = url

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.method, 'method')
        self.validate_required(self.url, 'url')

    def to_map(self):
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('method') is not None:
            self.method = m.get('method')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class BatchRequest(TeaModel):
    """
    批处理
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        requests: List[BatchSubRequest] = None,
        resource: str = None,
    ):
        self.headers = headers
        # Requests 请求合集
        self.requests = requests
        # 支持的资源类型
        self.resource = resource

    def validate(self):
        self.validate_required(self.requests, 'requests')
        if self.requests:
            for k in self.requests:
                if k:
                    k.validate()
        self.validate_required(self.resource, 'resource')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        result['requests'] = []
        if self.requests is not None:
            for k in self.requests:
                result['requests'].append(k.to_map() if k else None)
        if self.resource is not None:
            result['resource'] = self.resource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        self.requests = []
        if m.get('requests') is not None:
            for k in m.get('requests'):
                temp_model = BatchSubRequest()
                self.requests.append(temp_model.from_map(k))
        if m.get('resource') is not None:
            self.resource = m.get('resource')
        return self


class CCPGetDirSizeInfoRequest(TeaModel):
    """
    获取文件夹size信息
    """
    def __init__(
        self,
        drive_id: str = None,
        file_id: str = None,
        share_id: str = None,
    ):
        # drive_id
        self.drive_id = drive_id
        # file_id
        self.file_id = file_id
        # share_id, either share_id or drive_id is required
        self.share_id = share_id

    def validate(self):
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_id, 'file_id')
        if self.file_id is not None:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9.-_]{1,50}')

    def to_map(self):
        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.share_id is not None:
            result['share_id'] = self.share_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        return self


class CancelShareLinkRequest(TeaModel):
    """
    cancel_share_link request
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        share_id: str = None,
    ):
        self.headers = headers
        # share_id
        self.share_id = share_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.share_id is not None:
            result['share_id'] = self.share_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        return self


class CompleteFileRequest(TeaModel):
    """
    合并文件上传任务
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        addition_data: dict = None,
        drive_id: str = None,
        file_id: str = None,
        part_info_list: List[UploadPartInfo] = None,
        share_id: str = None,
        upload_id: str = None,
    ):
        self.headers = headers
        # addition_data
        self.addition_data = addition_data
        # drive_id
        self.drive_id = drive_id
        # file_id
        self.file_id = file_id
        # part_info_list
        self.part_info_list = part_info_list
        self.share_id = share_id
        # upload_id
        self.upload_id = upload_id

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
        result = dict()
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
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.upload_id is not None:
            result['upload_id'] = self.upload_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('addition_data') is not None:
            self.addition_data = m.get('addition_data')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        self.part_info_list = []
        if m.get('part_info_list') is not None:
            for k in m.get('part_info_list'):
                temp_model = UploadPartInfo()
                self.part_info_list.append(temp_model.from_map(k))
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('upload_id') is not None:
            self.upload_id = m.get('upload_id')
        return self


class CopyFileRequest(TeaModel):
    """
    文件拷贝
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        auto_rename: bool = None,
        drive_id: str = None,
        file_id: str = None,
        file_id_path: str = None,
        new_name: str = None,
        share_id: str = None,
        to_drive_id: str = None,
        to_parent_file_id: str = None,
        to_share_id: str = None,
    ):
        self.headers = headers
        # auto_rename
        # type: boolean
        self.auto_rename = auto_rename
        # drive_id
        self.drive_id = drive_id
        # file_id
        self.file_id = file_id
        self.file_id_path = file_id_path
        # new_name
        self.new_name = new_name
        # share_id, either share_id or drive_id is required
        self.share_id = share_id
        # to_drive_id
        self.to_drive_id = to_drive_id
        # to_parent_file_id
        self.to_parent_file_id = to_parent_file_id
        # to_drive_id
        self.to_share_id = to_share_id

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
        if self.to_share_id is not None:
            self.validate_pattern(self.to_share_id, 'to_share_id', '[0-9]+')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.auto_rename is not None:
            result['auto_rename'] = self.auto_rename
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.file_id_path is not None:
            result['file_id_path'] = self.file_id_path
        if self.new_name is not None:
            result['new_name'] = self.new_name
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.to_drive_id is not None:
            result['to_drive_id'] = self.to_drive_id
        if self.to_parent_file_id is not None:
            result['to_parent_file_id'] = self.to_parent_file_id
        if self.to_share_id is not None:
            result['to_share_id'] = self.to_share_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('auto_rename') is not None:
            self.auto_rename = m.get('auto_rename')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('file_id_path') is not None:
            self.file_id_path = m.get('file_id_path')
        if m.get('new_name') is not None:
            self.new_name = m.get('new_name')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('to_drive_id') is not None:
            self.to_drive_id = m.get('to_drive_id')
        if m.get('to_parent_file_id') is not None:
            self.to_parent_file_id = m.get('to_parent_file_id')
        if m.get('to_share_id') is not None:
            self.to_share_id = m.get('to_share_id')
        return self


class CreateDriveRequest(TeaModel):
    """
    create drive request
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        default: bool = None,
        description: str = None,
        drive_name: str = None,
        drive_type: str = None,
        encrypt_mode: str = None,
        location: str = None,
        owner: str = None,
        owner_type: str = None,
        relative_path: str = None,
        status: str = None,
        store_id: str = None,
        subdomain_id: str = None,
        total_size: int = None,
    ):
        self.headers = headers
        # 是否默认drive, 只允许设置一个默认drive
        self.default = default
        # 描述信息
        self.description = description
        # Drive 名称
        self.drive_name = drive_name
        # Drive类型
        self.drive_type = drive_type
        self.encrypt_mode = encrypt_mode
        # location
        self.location = location
        # 所属者
        self.owner = owner
        # 所属者
        self.owner_type = owner_type
        # domain的PathType为OSSPath时必选。 Drive存储基于store的相对路径
        self.relative_path = relative_path
        # 状态
        self.status = status
        # StoreID , domain的PathType为OSSPath时必选
        self.store_id = store_id
        # Subdomain ID
        self.subdomain_id = subdomain_id
        # 总大小,单位Byte [如果设置 -1 代表不限制]
        self.total_size = total_size

    def validate(self):
        if self.description is not None:
            self.validate_max_length(self.description, 'description', 1024)
        self.validate_required(self.drive_name, 'drive_name')
        if self.drive_name is not None:
            self.validate_max_length(self.drive_name, 'drive_name', 1024)
        self.validate_required(self.owner, 'owner')
        self.validate_required(self.owner_type, 'owner_type')

    def to_map(self):
        result = dict()
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
        if self.location is not None:
            result['location'] = self.location
        if self.owner is not None:
            result['owner'] = self.owner
        if self.owner_type is not None:
            result['owner_type'] = self.owner_type
        if self.relative_path is not None:
            result['relative_path'] = self.relative_path
        if self.status is not None:
            result['status'] = self.status
        if self.store_id is not None:
            result['store_id'] = self.store_id
        if self.subdomain_id is not None:
            result['subdomain_id'] = self.subdomain_id
        if self.total_size is not None:
            result['total_size'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('default') is not None:
            self.default = m.get('default')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('drive_name') is not None:
            self.drive_name = m.get('drive_name')
        if m.get('drive_type') is not None:
            self.drive_type = m.get('drive_type')
        if m.get('encrypt_mode') is not None:
            self.encrypt_mode = m.get('encrypt_mode')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('owner_type') is not None:
            self.owner_type = m.get('owner_type')
        if m.get('relative_path') is not None:
            self.relative_path = m.get('relative_path')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('store_id') is not None:
            self.store_id = m.get('store_id')
        if m.get('subdomain_id') is not None:
            self.subdomain_id = m.get('subdomain_id')
        if m.get('total_size') is not None:
            self.total_size = m.get('total_size')
        return self


class ImageMediaMetadata(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        height: int = None,
        width: int = None,
    ):
        # height
        self.height = height
        # width：
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.height is not None:
            result['height'] = self.height
        if self.width is not None:
            result['width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('height') is not None:
            self.height = m.get('height')
        if m.get('width') is not None:
            self.width = m.get('width')
        return self


class VideoMediaMetadata(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        duration: str = None,
    ):
        # Duration
        self.duration = duration

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.duration is not None:
            result['duration'] = self.duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        return self


class CreateFileRequest(TeaModel):
    """
    创建文件
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        addition_data: dict = None,
        auto_rename: bool = None,
        check_name_mode: str = None,
        content_hash: str = None,
        content_hash_name: str = None,
        content_md_5: str = None,
        content_type: str = None,
        description: str = None,
        drive_id: str = None,
        encrypt_mode: str = None,
        file_id: str = None,
        force_upload_to_location: bool = None,
        hidden: bool = None,
        image_media_metadata: ImageMediaMetadata = None,
        labels: List[str] = None,
        last_updated_at: str = None,
        location: str = None,
        meta: str = None,
        name: str = None,
        parent_file_id: str = None,
        parent_file_id_path: str = None,
        part_info_list: List[UploadPartInfo] = None,
        pre_hash: str = None,
        share_id: str = None,
        size: int = None,
        streams_info: dict = None,
        type: str = None,
        user_meta: str = None,
        video_media_metadata: VideoMediaMetadata = None,
    ):
        self.headers = headers
        # addition_data
        self.addition_data = addition_data
        self.auto_rename = auto_rename
        # check_name_mode
        self.check_name_mode = check_name_mode
        # content_hash
        self.content_hash = content_hash
        # content_hash_name
        self.content_hash_name = content_hash_name
        # ContentMd5
        self.content_md_5 = content_md_5
        # ContentType
        self.content_type = content_type
        # description
        self.description = description
        # drive_id
        self.drive_id = drive_id
        # encrypt_mode
        self.encrypt_mode = encrypt_mode
        # file_id
        self.file_id = file_id
        # force_upload_to_location
        self.force_upload_to_location = force_upload_to_location
        # hidden
        self.hidden = hidden
        self.image_media_metadata = image_media_metadata
        # labels
        self.labels = labels
        # last_updated_at
        self.last_updated_at = last_updated_at
        # location
        self.location = location
        self.meta = meta
        # Name
        self.name = name
        # parent_file_id
        self.parent_file_id = parent_file_id
        self.parent_file_id_path = parent_file_id_path
        # part_info_list
        self.part_info_list = part_info_list
        # pre_hash
        self.pre_hash = pre_hash
        # share_id
        # example
        self.share_id = share_id
        # Size
        self.size = size
        # streams_info
        self.streams_info = streams_info
        # Type
        self.type = type
        # user_meta
        self.user_meta = user_meta
        self.video_media_metadata = video_media_metadata

    def validate(self):
        if self.description is not None:
            self.validate_max_length(self.description, 'description', 1024)
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
        result = dict()
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
        if self.force_upload_to_location is not None:
            result['force_upload_to_location'] = self.force_upload_to_location
        if self.hidden is not None:
            result['hidden'] = self.hidden
        if self.image_media_metadata is not None:
            result['image_media_metadata'] = self.image_media_metadata.to_map()
        if self.labels is not None:
            result['labels'] = self.labels
        if self.last_updated_at is not None:
            result['last_updated_at'] = self.last_updated_at
        if self.location is not None:
            result['location'] = self.location
        if self.meta is not None:
            result['meta'] = self.meta
        if self.name is not None:
            result['name'] = self.name
        if self.parent_file_id is not None:
            result['parent_file_id'] = self.parent_file_id
        if self.parent_file_id_path is not None:
            result['parent_file_id_path'] = self.parent_file_id_path
        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k in self.part_info_list:
                result['part_info_list'].append(k.to_map() if k else None)
        if self.pre_hash is not None:
            result['pre_hash'] = self.pre_hash
        if self.share_id is not None:
            result['share_id'] = self.share_id
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('addition_data') is not None:
            self.addition_data = m.get('addition_data')
        if m.get('auto_rename') is not None:
            self.auto_rename = m.get('auto_rename')
        if m.get('check_name_mode') is not None:
            self.check_name_mode = m.get('check_name_mode')
        if m.get('content_hash') is not None:
            self.content_hash = m.get('content_hash')
        if m.get('content_hash_name') is not None:
            self.content_hash_name = m.get('content_hash_name')
        if m.get('content_md5') is not None:
            self.content_md_5 = m.get('content_md5')
        if m.get('content_type') is not None:
            self.content_type = m.get('content_type')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('encrypt_mode') is not None:
            self.encrypt_mode = m.get('encrypt_mode')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('force_upload_to_location') is not None:
            self.force_upload_to_location = m.get('force_upload_to_location')
        if m.get('hidden') is not None:
            self.hidden = m.get('hidden')
        if m.get('image_media_metadata') is not None:
            temp_model = ImageMediaMetadata()
            self.image_media_metadata = temp_model.from_map(m['image_media_metadata'])
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('last_updated_at') is not None:
            self.last_updated_at = m.get('last_updated_at')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('meta') is not None:
            self.meta = m.get('meta')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parent_file_id') is not None:
            self.parent_file_id = m.get('parent_file_id')
        if m.get('parent_file_id_path') is not None:
            self.parent_file_id_path = m.get('parent_file_id_path')
        self.part_info_list = []
        if m.get('part_info_list') is not None:
            for k in m.get('part_info_list'):
                temp_model = UploadPartInfo()
                self.part_info_list.append(temp_model.from_map(k))
        if m.get('pre_hash') is not None:
            self.pre_hash = m.get('pre_hash')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('streams_info') is not None:
            self.streams_info = m.get('streams_info')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('user_meta') is not None:
            self.user_meta = m.get('user_meta')
        if m.get('video_media_metadata') is not None:
            temp_model = VideoMediaMetadata()
            self.video_media_metadata = temp_model.from_map(m['video_media_metadata'])
        return self


class CreateShareLinkRequest(TeaModel):
    """
    create_share_link request
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        description: str = None,
        drive_id: str = None,
        expiration: str = None,
        file_id: str = None,
        file_id_list: List[str] = None,
        file_path_list: List[str] = None,
        share_name: str = None,
        share_pwd: str = None,
    ):
        self.headers = headers
        # description
        self.description = description
        # drive_id
        self.drive_id = drive_id
        # expiration
        self.expiration = expiration
        # file_id
        self.file_id = file_id
        # file_id_list
        self.file_id_list = file_id_list
        # file_path_list
        self.file_path_list = file_path_list
        # share_name
        self.share_name = share_name
        # share_pwd
        self.share_pwd = share_pwd

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.expiration, 'expiration')
        self.validate_required(self.file_id, 'file_id')
        self.validate_required(self.file_id_list, 'file_id_list')
        if self.file_id_list is not None:
            self.validate_maximum(self.file_id_list, 'file_id_list', 50)
            self.validate_minimum(self.file_id_list, 'file_id_list', 1)
        self.validate_required(self.file_path_list, 'file_path_list')
        if self.file_path_list is not None:
            self.validate_maximum(self.file_path_list, 'file_path_list', 50)
            self.validate_minimum(self.file_path_list, 'file_path_list', 1)
        if self.share_pwd is not None:
            self.validate_maximum(self.share_pwd, 'share_pwd', 64)
            self.validate_minimum(self.share_pwd, 'share_pwd', 0)

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.description is not None:
            result['description'] = self.description
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.expiration is not None:
            result['expiration'] = self.expiration
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.file_id_list is not None:
            result['file_id_list'] = self.file_id_list
        if self.file_path_list is not None:
            result['file_path_list'] = self.file_path_list
        if self.share_name is not None:
            result['share_name'] = self.share_name
        if self.share_pwd is not None:
            result['share_pwd'] = self.share_pwd
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('expiration') is not None:
            self.expiration = m.get('expiration')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('file_id_list') is not None:
            self.file_id_list = m.get('file_id_list')
        if m.get('file_path_list') is not None:
            self.file_path_list = m.get('file_path_list')
        if m.get('share_name') is not None:
            self.share_name = m.get('share_name')
        if m.get('share_pwd') is not None:
            self.share_pwd = m.get('share_pwd')
        return self


class CreateShareRequest(TeaModel):
    """
    create share request
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        description: str = None,
        drive_id: str = None,
        expiration: str = None,
        owner: str = None,
        owner_type: str = None,
        permissions: List[str] = None,
        share_file_id: str = None,
        share_file_path: str = None,
        share_name: str = None,
        share_policy: List[SharePermissionPolicy] = None,
        status: str = None,
    ):
        self.headers = headers
        # description
        self.description = description
        # drive_id
        self.drive_id = drive_id
        # expiration
        self.expiration = expiration
        # owner
        self.owner = owner
        # owner_type
        self.owner_type = owner_type
        # permissions
        self.permissions = permissions
        # share_file_id
        self.share_file_id = share_file_id
        # share_file_path
        self.share_file_path = share_file_path
        # share_name
        self.share_name = share_name
        # share create policy
        # 
        # share_policy
        self.share_policy = share_policy
        # status
        self.status = status

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.owner, 'owner')
        if self.share_policy:
            for k in self.share_policy:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.description is not None:
            result['description'] = self.description
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.expiration is not None:
            result['expiration'] = self.expiration
        if self.owner is not None:
            result['owner'] = self.owner
        if self.owner_type is not None:
            result['owner_type'] = self.owner_type
        if self.permissions is not None:
            result['permissions'] = self.permissions
        if self.share_file_id is not None:
            result['share_file_id'] = self.share_file_id
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('expiration') is not None:
            self.expiration = m.get('expiration')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('owner_type') is not None:
            self.owner_type = m.get('owner_type')
        if m.get('permissions') is not None:
            self.permissions = m.get('permissions')
        if m.get('share_file_id') is not None:
            self.share_file_id = m.get('share_file_id')
        if m.get('share_file_path') is not None:
            self.share_file_path = m.get('share_file_path')
        if m.get('share_name') is not None:
            self.share_name = m.get('share_name')
        self.share_policy = []
        if m.get('share_policy') is not None:
            for k in m.get('share_policy'):
                temp_model = SharePermissionPolicy()
                self.share_policy.append(temp_model.from_map(k))
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class DeleteDriveRequest(TeaModel):
    """
    Delete drive request
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        drive_id: str = None,
        subdomain_id: str = None,
    ):
        self.headers = headers
        # Drive ID
        self.drive_id = drive_id
        # Subdomain ID
        self.subdomain_id = subdomain_id

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.subdomain_id is not None:
            result['subdomain_id'] = self.subdomain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('subdomain_id') is not None:
            self.subdomain_id = m.get('subdomain_id')
        return self


class DeleteFileRequest(TeaModel):
    """
    删除文件请求
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        drive_id: str = None,
        file_id: str = None,
        file_id_path: str = None,
        permanently: bool = None,
        share_id: str = None,
    ):
        self.headers = headers
        # drive_id
        self.drive_id = drive_id
        self.file_id = file_id
        self.file_id_path = file_id_path
        # permanently
        # type: false
        self.permanently = permanently
        self.share_id = share_id

    def validate(self):
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.file_id_path is not None:
            result['file_id_path'] = self.file_id_path
        if self.permanently is not None:
            result['permanently'] = self.permanently
        if self.share_id is not None:
            result['share_id'] = self.share_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('file_id_path') is not None:
            self.file_id_path = m.get('file_id_path')
        if m.get('permanently') is not None:
            self.permanently = m.get('permanently')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        return self


class DeleteFilesRequest(TeaModel):
    """
    批量删除文件请求
    """
    def __init__(
        self,
        drive_id: str = None,
        file_id_list: List[str] = None,
        share_id: str = None,
    ):
        # drive_id
        self.drive_id = drive_id
        # file_id_list
        self.file_id_list = file_id_list
        # share_id
        self.share_id = share_id

    def validate(self):
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_id_list, 'file_id_list')

    def to_map(self):
        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id_list is not None:
            result['file_id_list'] = self.file_id_list
        if self.share_id is not None:
            result['share_id'] = self.share_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id_list') is not None:
            self.file_id_list = m.get('file_id_list')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        return self


class DeleteShareRequest(TeaModel):
    """
    delete share request
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        share_id: str = None,
    ):
        self.headers = headers
        # share_id
        self.share_id = share_id

    def validate(self):
        self.validate_required(self.share_id, 'share_id')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.share_id is not None:
            result['share_id'] = self.share_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        return self


class DownloadRequest(TeaModel):
    """
    下载文件请求body
    """
    def __init__(
        self,
        drive_id: str = None,
        file_id: str = None,
        image_thumbnail_process: str = None,
        share_id: str = None,
        video_thumbnail_process: str = None,
        file_id_path: str = None,
        location: str = None,
        referer: str = None,
        sign_token: str = None,
    ):
        # drive id
        self.drive_id = drive_id
        # file id
        self.file_id = file_id
        # in: query
        # image_thumbnail_process
        self.image_thumbnail_process = image_thumbnail_process
        # share_id, either share_id or drive_id is required
        self.share_id = share_id
        # video_thumbnail_process
        # type:string
        self.video_thumbnail_process = video_thumbnail_process
        self.file_id_path = file_id_path
        # location
        self.location = location
        self.referer = referer
        self.sign_token = sign_token

    def validate(self):
        self.validate_required(self.file_id, 'file_id')

    def to_map(self):
        result = dict()
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
        if self.file_id_path is not None:
            result['file_id_path'] = self.file_id_path
        if self.location is not None:
            result['location'] = self.location
        if self.referer is not None:
            result['referer'] = self.referer
        if self.sign_token is not None:
            result['sign_token'] = self.sign_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DriveID') is not None:
            self.drive_id = m.get('DriveID')
        if m.get('FileID') is not None:
            self.file_id = m.get('FileID')
        if m.get('ImageThumbnailProcess') is not None:
            self.image_thumbnail_process = m.get('ImageThumbnailProcess')
        if m.get('ShareID') is not None:
            self.share_id = m.get('ShareID')
        if m.get('VideoThumbnailProcess') is not None:
            self.video_thumbnail_process = m.get('VideoThumbnailProcess')
        if m.get('file_id_path') is not None:
            self.file_id_path = m.get('file_id_path')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('referer') is not None:
            self.referer = m.get('referer')
        if m.get('sign_token') is not None:
            self.sign_token = m.get('sign_token')
        return self


class GetAsyncTaskRequest(TeaModel):
    """
    获取异步人去信息
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        async_task_id: str = None,
    ):
        self.headers = headers
        # async_task_id
        # type:string
        self.async_task_id = async_task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.async_task_id is not None:
            result['async_task_id'] = self.async_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('async_task_id') is not None:
            self.async_task_id = m.get('async_task_id')
        return self


class GetDefaultDriveRequest(TeaModel):
    """
    Get default drive request
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        subdomain_id: str = None,
        user_id: str = None,
    ):
        self.headers = headers
        # Subdomain ID
        self.subdomain_id = subdomain_id
        # 用户ID
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.subdomain_id is not None:
            result['subdomain_id'] = self.subdomain_id
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('subdomain_id') is not None:
            self.subdomain_id = m.get('subdomain_id')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class GetDownloadUrlRequest(TeaModel):
    """
    获取文件下载地址的请求body
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        addition_data: dict = None,
        drive_id: str = None,
        expire_sec: int = None,
        file_id: str = None,
        file_id_path: str = None,
        file_name: str = None,
        location: str = None,
        referer: str = None,
        share_id: str = None,
        sign_token: str = None,
    ):
        self.headers = headers
        # addition_data
        self.addition_data = addition_data
        # drive_id
        self.drive_id = drive_id
        # expire_sec
        self.expire_sec = expire_sec
        # file_id
        self.file_id = file_id
        self.file_id_path = file_id_path
        # file_name
        self.file_name = file_name
        # location
        self.location = location
        self.referer = referer
        # share_id, either share_id or drive_id is required
        self.share_id = share_id
        self.sign_token = sign_token

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.expire_sec is not None:
            self.validate_maximum(self.expire_sec, 'expire_sec', 14400)
            self.validate_minimum(self.expire_sec, 'expire_sec', 1)
        self.validate_required(self.file_id, 'file_id')
        if self.file_id is not None:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9.-_]{1,50}')
        if self.file_name is not None:
            self.validate_max_length(self.file_name, 'file_name', 1024)

    def to_map(self):
        result = dict()
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
        if self.file_id_path is not None:
            result['file_id_path'] = self.file_id_path
        if self.file_name is not None:
            result['file_name'] = self.file_name
        if self.location is not None:
            result['location'] = self.location
        if self.referer is not None:
            result['referer'] = self.referer
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.sign_token is not None:
            result['sign_token'] = self.sign_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('addition_data') is not None:
            self.addition_data = m.get('addition_data')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('expire_sec') is not None:
            self.expire_sec = m.get('expire_sec')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('file_id_path') is not None:
            self.file_id_path = m.get('file_id_path')
        if m.get('file_name') is not None:
            self.file_name = m.get('file_name')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('referer') is not None:
            self.referer = m.get('referer')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('sign_token') is not None:
            self.sign_token = m.get('sign_token')
        return self


class GetDriveRequest(TeaModel):
    """
    Get drive request
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        drive_id: str = None,
        subdomain_id: str = None,
    ):
        self.headers = headers
        # Drive ID
        self.drive_id = drive_id
        # Subdomain ID
        self.subdomain_id = subdomain_id

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.subdomain_id is not None:
            result['subdomain_id'] = self.subdomain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('subdomain_id') is not None:
            self.subdomain_id = m.get('subdomain_id')
        return self


class GetFileByPathRequest(TeaModel):
    """
    根据路径获取 File 接口 body
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        addition_data: dict = None,
        drive_id: str = None,
        file_path: str = None,
        image_cropping_aspect_ratios: List[str] = None,
        image_thumbnail_process: str = None,
        image_url_process: str = None,
        referer: str = None,
        sign_token: str = None,
        url_expire_sec: int = None,
        video_thumbnail_process: str = None,
    ):
        self.headers = headers
        # addition_data
        self.addition_data = addition_data
        # drive_id
        self.drive_id = drive_id
        # file_path
        self.file_path = file_path
        self.image_cropping_aspect_ratios = image_cropping_aspect_ratios
        # image_thumbnail_process
        self.image_thumbnail_process = image_thumbnail_process
        # image_url_process
        self.image_url_process = image_url_process
        self.referer = referer
        self.sign_token = sign_token
        # url_expire_sec
        self.url_expire_sec = url_expire_sec
        # video_thumbnail_process
        # type:string
        self.video_thumbnail_process = video_thumbnail_process

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.url_expire_sec is not None:
            self.validate_maximum(self.url_expire_sec, 'url_expire_sec', 14400)
            self.validate_minimum(self.url_expire_sec, 'url_expire_sec', 10)

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.addition_data is not None:
            result['addition_data'] = self.addition_data
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_path is not None:
            result['file_path'] = self.file_path
        if self.image_cropping_aspect_ratios is not None:
            result['image_cropping_aspect_ratios'] = self.image_cropping_aspect_ratios
        if self.image_thumbnail_process is not None:
            result['image_thumbnail_process'] = self.image_thumbnail_process
        if self.image_url_process is not None:
            result['image_url_process'] = self.image_url_process
        if self.referer is not None:
            result['referer'] = self.referer
        if self.sign_token is not None:
            result['sign_token'] = self.sign_token
        if self.url_expire_sec is not None:
            result['url_expire_sec'] = self.url_expire_sec
        if self.video_thumbnail_process is not None:
            result['video_thumbnail_process'] = self.video_thumbnail_process
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('addition_data') is not None:
            self.addition_data = m.get('addition_data')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_path') is not None:
            self.file_path = m.get('file_path')
        if m.get('image_cropping_aspect_ratios') is not None:
            self.image_cropping_aspect_ratios = m.get('image_cropping_aspect_ratios')
        if m.get('image_thumbnail_process') is not None:
            self.image_thumbnail_process = m.get('image_thumbnail_process')
        if m.get('image_url_process') is not None:
            self.image_url_process = m.get('image_url_process')
        if m.get('referer') is not None:
            self.referer = m.get('referer')
        if m.get('sign_token') is not None:
            self.sign_token = m.get('sign_token')
        if m.get('url_expire_sec') is not None:
            self.url_expire_sec = m.get('url_expire_sec')
        if m.get('video_thumbnail_process') is not None:
            self.video_thumbnail_process = m.get('video_thumbnail_process')
        return self


class GetFileRequest(TeaModel):
    """
    获取文件元数据
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        addition_data: dict = None,
        drive_id: str = None,
        fields: str = None,
        file_id: str = None,
        file_id_path: str = None,
        image_cropping_aspect_ratios: List[str] = None,
        image_thumbnail_process: str = None,
        image_url_process: str = None,
        location: str = None,
        referer: str = None,
        share_id: str = None,
        sign_token: str = None,
        url_expire_sec: int = None,
        video_thumbnail_process: str = None,
    ):
        self.headers = headers
        # addition_data
        self.addition_data = addition_data
        # drive_id
        self.drive_id = drive_id
        # fields
        self.fields = fields
        # file_id
        self.file_id = file_id
        self.file_id_path = file_id_path
        self.image_cropping_aspect_ratios = image_cropping_aspect_ratios
        # image_thumbnail_process
        self.image_thumbnail_process = image_thumbnail_process
        # image_url_process
        self.image_url_process = image_url_process
        # location
        self.location = location
        self.referer = referer
        # share_id, either share_id or drive_id is required
        self.share_id = share_id
        self.sign_token = sign_token
        # url_expire_sec
        self.url_expire_sec = url_expire_sec
        # video_thumbnail_process
        # type:string
        self.video_thumbnail_process = video_thumbnail_process

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
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.addition_data is not None:
            result['addition_data'] = self.addition_data
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.fields is not None:
            result['fields'] = self.fields
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.file_id_path is not None:
            result['file_id_path'] = self.file_id_path
        if self.image_cropping_aspect_ratios is not None:
            result['image_cropping_aspect_ratios'] = self.image_cropping_aspect_ratios
        if self.image_thumbnail_process is not None:
            result['image_thumbnail_process'] = self.image_thumbnail_process
        if self.image_url_process is not None:
            result['image_url_process'] = self.image_url_process
        if self.location is not None:
            result['location'] = self.location
        if self.referer is not None:
            result['referer'] = self.referer
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.sign_token is not None:
            result['sign_token'] = self.sign_token
        if self.url_expire_sec is not None:
            result['url_expire_sec'] = self.url_expire_sec
        if self.video_thumbnail_process is not None:
            result['video_thumbnail_process'] = self.video_thumbnail_process
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('addition_data') is not None:
            self.addition_data = m.get('addition_data')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('fields') is not None:
            self.fields = m.get('fields')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('file_id_path') is not None:
            self.file_id_path = m.get('file_id_path')
        if m.get('image_cropping_aspect_ratios') is not None:
            self.image_cropping_aspect_ratios = m.get('image_cropping_aspect_ratios')
        if m.get('image_thumbnail_process') is not None:
            self.image_thumbnail_process = m.get('image_thumbnail_process')
        if m.get('image_url_process') is not None:
            self.image_url_process = m.get('image_url_process')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('referer') is not None:
            self.referer = m.get('referer')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('sign_token') is not None:
            self.sign_token = m.get('sign_token')
        if m.get('url_expire_sec') is not None:
            self.url_expire_sec = m.get('url_expire_sec')
        if m.get('video_thumbnail_process') is not None:
            self.video_thumbnail_process = m.get('video_thumbnail_process')
        return self


class GetLastCursorRequest(TeaModel):
    """
    获取最新游标
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        drive_id: str = None,
    ):
        self.headers = headers
        # drive_id
        self.drive_id = drive_id

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        return self


class GetMediaPlayURLRequest(TeaModel):
    """
    get_media_play_url request
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        drive_id: str = None,
        file_id: str = None,
    ):
        self.headers = headers
        # drive_id
        self.drive_id = drive_id
        # file_id
        self.file_id = file_id

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_id, 'file_id')
        if self.file_id is not None:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9.-_]{1,50}')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        return self


class GetOfficeEditUrlRequest(TeaModel):
    """
    获取office文档在线编辑地址
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        addition_data: dict = None,
        drive_id: str = None,
        file_id: str = None,
    ):
        self.headers = headers
        # addition_data
        self.addition_data = addition_data
        # drive_id
        self.drive_id = drive_id
        # file_id
        self.file_id = file_id

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_id, 'file_id')
        if self.file_id is not None:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9.-_]{1,50}')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.addition_data is not None:
            result['addition_data'] = self.addition_data
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('addition_data') is not None:
            self.addition_data = m.get('addition_data')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        return self


class GetOfficePreviewUrlRequest(TeaModel):
    """
    获取office文档预览地址
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        addition_data: dict = None,
        drive_id: str = None,
        file_id: str = None,
        share_id: str = None,
    ):
        self.headers = headers
        # addition_data
        self.addition_data = addition_data
        # drive_id
        self.drive_id = drive_id
        # file_id
        self.file_id = file_id
        # share_id, either share_id or drive_id is required
        self.share_id = share_id

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_id, 'file_id')
        if self.file_id is not None:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9.-_]{1,50}')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.addition_data is not None:
            result['addition_data'] = self.addition_data
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.share_id is not None:
            result['share_id'] = self.share_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('addition_data') is not None:
            self.addition_data = m.get('addition_data')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        return self


class GetShareLinkByAnonymousRequest(TeaModel):
    """
    get_share_link_by_anonymous request
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        share_id: str = None,
    ):
        self.headers = headers
        # share_id
        self.share_id = share_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.share_id is not None:
            result['share_id'] = self.share_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        return self


class GetShareLinkIDRequest(TeaModel):
    """
    get_share_id request
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        share_msg: str = None,
    ):
        self.headers = headers
        # share_msg
        self.share_msg = share_msg

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.share_msg is not None:
            result['share_msg'] = self.share_msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('share_msg') is not None:
            self.share_msg = m.get('share_msg')
        return self


class GetShareLinkTokenRequest(TeaModel):
    """
    get_share_token request
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        share_id: str = None,
        share_pwd: str = None,
    ):
        self.headers = headers
        # share_id
        self.share_id = share_id
        # share_pwd
        self.share_pwd = share_pwd

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.share_pwd is not None:
            result['share_pwd'] = self.share_pwd
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('share_pwd') is not None:
            self.share_pwd = m.get('share_pwd')
        return self


class GetShareRequest(TeaModel):
    """
    get share request
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        share_id: str = None,
    ):
        self.headers = headers
        # share_id
        self.share_id = share_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.share_id is not None:
            result['share_id'] = self.share_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        return self


class GetUploadUrlRequest(TeaModel):
    """
    获取文件上传URL
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        content_md_5: str = None,
        drive_id: str = None,
        file_id: str = None,
        part_info_list: List[UploadPartInfo] = None,
        share_id: str = None,
        upload_id: str = None,
    ):
        self.headers = headers
        # content_md5
        self.content_md_5 = content_md_5
        # drive_id
        self.drive_id = drive_id
        # file_id
        self.file_id = file_id
        # upload_part_list
        self.part_info_list = part_info_list
        self.share_id = share_id
        # upload_id
        self.upload_id = upload_id

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
        result = dict()
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
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.upload_id is not None:
            result['upload_id'] = self.upload_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('content_md5') is not None:
            self.content_md_5 = m.get('content_md5')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        self.part_info_list = []
        if m.get('part_info_list') is not None:
            for k in m.get('part_info_list'):
                temp_model = UploadPartInfo()
                self.part_info_list.append(temp_model.from_map(k))
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('upload_id') is not None:
            self.upload_id = m.get('upload_id')
        return self


class GetVideoPreviewSpriteURLRequest(TeaModel):
    """
    获取视频雪碧图地址的请求body
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        drive_id: str = None,
        expire_sec: int = None,
        file_id: str = None,
        share_id: str = None,
    ):
        self.headers = headers
        # drive_id
        self.drive_id = drive_id
        # expire_sec
        self.expire_sec = expire_sec
        # file_id
        self.file_id = file_id
        # share_id, either share_id or drive_id is required
        self.share_id = share_id

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.expire_sec is not None:
            self.validate_maximum(self.expire_sec, 'expire_sec', 14400)
            self.validate_minimum(self.expire_sec, 'expire_sec', 1)
        self.validate_required(self.file_id, 'file_id')
        if self.file_id is not None:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9.-_]{1,50}')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.expire_sec is not None:
            result['expire_sec'] = self.expire_sec
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.share_id is not None:
            result['share_id'] = self.share_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('expire_sec') is not None:
            self.expire_sec = m.get('expire_sec')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        return self


class GetVideoPreviewURLRequest(TeaModel):
    """
    获取视频文件播放地址的请求body
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        addition_data: dict = None,
        audio_template_id: str = None,
        drive_id: str = None,
        expire_sec: int = None,
        file_id: str = None,
        share_id: str = None,
        template_id: str = None,
    ):
        self.headers = headers
        # addition_data
        self.addition_data = addition_data
        # audio_template_id
        self.audio_template_id = audio_template_id
        # drive_id
        self.drive_id = drive_id
        # expire_sec
        self.expire_sec = expire_sec
        # file_id
        self.file_id = file_id
        # share_id, either share_id or drive_id is required
        self.share_id = share_id
        # template_id
        self.template_id = template_id

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.expire_sec is not None:
            self.validate_maximum(self.expire_sec, 'expire_sec', 14400)
            self.validate_minimum(self.expire_sec, 'expire_sec', 1)
        self.validate_required(self.file_id, 'file_id')
        if self.file_id is not None:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9.-_]{1,50}')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.addition_data is not None:
            result['addition_data'] = self.addition_data
        if self.audio_template_id is not None:
            result['audio_template_id'] = self.audio_template_id
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.expire_sec is not None:
            result['expire_sec'] = self.expire_sec
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.template_id is not None:
            result['template_id'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('addition_data') is not None:
            self.addition_data = m.get('addition_data')
        if m.get('audio_template_id') is not None:
            self.audio_template_id = m.get('audio_template_id')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('expire_sec') is not None:
            self.expire_sec = m.get('expire_sec')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('template_id') is not None:
            self.template_id = m.get('template_id')
        return self


class HostingCompleteFileRequest(TeaModel):
    """
    complete file request
    """
    def __init__(
        self,
        addition_data: dict = None,
        drive_id: str = None,
        file_path: str = None,
        forbid_overwrite: bool = None,
        part_info_list: List[UploadPartInfo] = None,
        share_id: str = None,
        upload_id: str = None,
    ):
        # addition_data
        self.addition_data = addition_data
        # drive_id
        self.drive_id = drive_id
        self.file_path = file_path
        # forbid_overwrite
        # type: boolean
        self.forbid_overwrite = forbid_overwrite
        # part_info_list
        self.part_info_list = part_info_list
        self.share_id = share_id
        # upload_id
        self.upload_id = upload_id

    def validate(self):
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.part_info_list:
            for k in self.part_info_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('addition_data') is not None:
            self.addition_data = m.get('addition_data')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_path') is not None:
            self.file_path = m.get('file_path')
        if m.get('forbid_overwrite') is not None:
            self.forbid_overwrite = m.get('forbid_overwrite')
        self.part_info_list = []
        if m.get('part_info_list') is not None:
            for k in m.get('part_info_list'):
                temp_model = UploadPartInfo()
                self.part_info_list.append(temp_model.from_map(k))
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('upload_id') is not None:
            self.upload_id = m.get('upload_id')
        return self


class HostingCopyFileRequest(TeaModel):
    """
    copy file request
    """
    def __init__(
        self,
        drive_id: str = None,
        file_path: str = None,
        new_name: str = None,
        overwrite: bool = None,
        share_id: str = None,
        to_drive_id: str = None,
        to_parent_file_path: str = None,
        to_share_id: str = None,
    ):
        # drive_id
        self.drive_id = drive_id
        # file_path
        self.file_path = file_path
        # new_name
        self.new_name = new_name
        # overwrite
        # type: boolean
        self.overwrite = overwrite
        # share_id
        self.share_id = share_id
        # to_drive_id
        self.to_drive_id = to_drive_id
        # to_parent_file_path
        self.to_parent_file_path = to_parent_file_path
        # share_id
        self.to_share_id = to_share_id

    def validate(self):
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_path, 'file_path')
        if self.new_name is not None:
            self.validate_max_length(self.new_name, 'new_name', 1024)
        if self.share_id is not None:
            self.validate_pattern(self.share_id, 'share_id', '[0-9a-zA-Z-]+')
        if self.to_drive_id is not None:
            self.validate_pattern(self.to_drive_id, 'to_drive_id', '[0-9]+')
        self.validate_required(self.to_parent_file_path, 'to_parent_file_path')

    def to_map(self):
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_path') is not None:
            self.file_path = m.get('file_path')
        if m.get('new_name') is not None:
            self.new_name = m.get('new_name')
        if m.get('overwrite') is not None:
            self.overwrite = m.get('overwrite')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('to_drive_id') is not None:
            self.to_drive_id = m.get('to_drive_id')
        if m.get('to_parent_file_path') is not None:
            self.to_parent_file_path = m.get('to_parent_file_path')
        if m.get('to_share_id') is not None:
            self.to_share_id = m.get('to_share_id')
        return self


class HostingCreateFileRequest(TeaModel):
    """
    create file request
    """
    def __init__(
        self,
        addition_data: dict = None,
        content_md_5: str = None,
        content_type: str = None,
        drive_id: str = None,
        forbid_overwrite: bool = None,
        name: str = None,
        parent_file_path: str = None,
        part_info_list: List[UploadPartInfo] = None,
        share_id: str = None,
        size: int = None,
        type: str = None,
    ):
        # addition_data
        self.addition_data = addition_data
        # ContentMd5
        self.content_md_5 = content_md_5
        # ContentType
        self.content_type = content_type
        # drive_id
        self.drive_id = drive_id
        # forbid_overwrite
        # type: boolean
        self.forbid_overwrite = forbid_overwrite
        # Name
        self.name = name
        # parent_file_path
        self.parent_file_path = parent_file_path
        # part_info_list
        self.part_info_list = part_info_list
        # share_id
        self.share_id = share_id
        # Size
        self.size = size
        # Type
        self.type = type

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
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('addition_data') is not None:
            self.addition_data = m.get('addition_data')
        if m.get('content_md5') is not None:
            self.content_md_5 = m.get('content_md5')
        if m.get('content_type') is not None:
            self.content_type = m.get('content_type')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('forbid_overwrite') is not None:
            self.forbid_overwrite = m.get('forbid_overwrite')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parent_file_path') is not None:
            self.parent_file_path = m.get('parent_file_path')
        self.part_info_list = []
        if m.get('part_info_list') is not None:
            for k in m.get('part_info_list'):
                temp_model = UploadPartInfo()
                self.part_info_list.append(temp_model.from_map(k))
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class HostingDeleteFileRequest(TeaModel):
    """
    删除文件请求
    """
    def __init__(
        self,
        drive_id: str = None,
        file_path: str = None,
        permanently: bool = None,
        share_id: str = None,
    ):
        # drive_id
        self.drive_id = drive_id
        # file_path
        self.file_path = file_path
        # permanently
        # type: false
        self.permanently = permanently
        # share_id
        self.share_id = share_id

    def validate(self):
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_path, 'file_path')
        if self.file_path is not None:
            self.validate_max_length(self.file_path, 'file_path', 1000)
        if self.share_id is not None:
            self.validate_pattern(self.share_id, 'share_id', '[0-9a-zA-Z-]+')

    def to_map(self):
        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_path is not None:
            result['file_path'] = self.file_path
        if self.permanently is not None:
            result['permanently'] = self.permanently
        if self.share_id is not None:
            result['share_id'] = self.share_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_path') is not None:
            self.file_path = m.get('file_path')
        if m.get('permanently') is not None:
            self.permanently = m.get('permanently')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        return self


class HostingGetDownloadUrlRequest(TeaModel):
    """
    获取文件下载地址的请求body
    """
    def __init__(
        self,
        drive_id: str = None,
        expire_sec: int = None,
        file_name: str = None,
        file_path: str = None,
        referer: str = None,
        share_id: str = None,
        sign_token: str = None,
    ):
        # drive_id
        self.drive_id = drive_id
        # expire_sec
        self.expire_sec = expire_sec
        # file_name
        self.file_name = file_name
        # file_path
        self.file_path = file_path
        self.referer = referer
        # share_id
        self.share_id = share_id
        self.sign_token = sign_token

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
        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.expire_sec is not None:
            result['expire_sec'] = self.expire_sec
        if self.file_name is not None:
            result['file_name'] = self.file_name
        if self.file_path is not None:
            result['file_path'] = self.file_path
        if self.referer is not None:
            result['referer'] = self.referer
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.sign_token is not None:
            result['sign_token'] = self.sign_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('expire_sec') is not None:
            self.expire_sec = m.get('expire_sec')
        if m.get('file_name') is not None:
            self.file_name = m.get('file_name')
        if m.get('file_path') is not None:
            self.file_path = m.get('file_path')
        if m.get('referer') is not None:
            self.referer = m.get('referer')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('sign_token') is not None:
            self.sign_token = m.get('sign_token')
        return self


class HostingGetFileRequest(TeaModel):
    """
    获取文件元数据
    """
    def __init__(
        self,
        drive_id: str = None,
        file_path: str = None,
        image_thumbnail_process: str = None,
        image_url_process: str = None,
        referer: str = None,
        share_id: str = None,
        sign_token: str = None,
        url_expire_sec: int = None,
        video_thumbnail_process: str = None,
    ):
        # drive_id
        self.drive_id = drive_id
        # file_id
        self.file_path = file_path
        # image_thumbnail_process
        self.image_thumbnail_process = image_thumbnail_process
        # image_url_process
        self.image_url_process = image_url_process
        self.referer = referer
        # share_id
        self.share_id = share_id
        self.sign_token = sign_token
        # url_expire_sec
        self.url_expire_sec = url_expire_sec
        # video_thumbnail_process
        # type:string
        self.video_thumbnail_process = video_thumbnail_process

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
        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_path is not None:
            result['file_path'] = self.file_path
        if self.image_thumbnail_process is not None:
            result['image_thumbnail_process'] = self.image_thumbnail_process
        if self.image_url_process is not None:
            result['image_url_process'] = self.image_url_process
        if self.referer is not None:
            result['referer'] = self.referer
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.sign_token is not None:
            result['sign_token'] = self.sign_token
        if self.url_expire_sec is not None:
            result['url_expire_sec'] = self.url_expire_sec
        if self.video_thumbnail_process is not None:
            result['video_thumbnail_process'] = self.video_thumbnail_process
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_path') is not None:
            self.file_path = m.get('file_path')
        if m.get('image_thumbnail_process') is not None:
            self.image_thumbnail_process = m.get('image_thumbnail_process')
        if m.get('image_url_process') is not None:
            self.image_url_process = m.get('image_url_process')
        if m.get('referer') is not None:
            self.referer = m.get('referer')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('sign_token') is not None:
            self.sign_token = m.get('sign_token')
        if m.get('url_expire_sec') is not None:
            self.url_expire_sec = m.get('url_expire_sec')
        if m.get('video_thumbnail_process') is not None:
            self.video_thumbnail_process = m.get('video_thumbnail_process')
        return self


class HostingGetSecureUrlRequest(TeaModel):
    """
    获取文件安全地址的请求body
    """
    def __init__(
        self,
        drive_id: str = None,
        expire_sec: int = None,
        file_path: str = None,
        secure_ip: str = None,
        share_id: str = None,
    ):
        # drive_id
        self.drive_id = drive_id
        # expire_sec 单位秒
        self.expire_sec = expire_sec
        # file_path
        self.file_path = file_path
        # secure_ip
        self.secure_ip = secure_ip
        # share_id
        self.share_id = share_id

    def validate(self):
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_path, 'file_path')
        if self.file_path is not None:
            self.validate_max_length(self.file_path, 'file_path', 1000)
        if self.share_id is not None:
            self.validate_pattern(self.share_id, 'share_id', '[0-9a-zA-Z-]+')

    def to_map(self):
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('expire_sec') is not None:
            self.expire_sec = m.get('expire_sec')
        if m.get('file_path') is not None:
            self.file_path = m.get('file_path')
        if m.get('secure_ip') is not None:
            self.secure_ip = m.get('secure_ip')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        return self


class HostingGetUploadUrlRequest(TeaModel):
    """
    获取文件上传URL
    """
    def __init__(
        self,
        content_md_5: str = None,
        drive_id: str = None,
        file_path: str = None,
        part_info_list: List[UploadPartInfo] = None,
        share_id: str = None,
        upload_id: str = None,
    ):
        # content_md5
        self.content_md_5 = content_md_5
        # drive_id
        self.drive_id = drive_id
        # file_path
        self.file_path = file_path
        # upload_part_list
        self.part_info_list = part_info_list
        # share_id
        self.share_id = share_id
        # upload_id
        self.upload_id = upload_id

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
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content_md5') is not None:
            self.content_md_5 = m.get('content_md5')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_path') is not None:
            self.file_path = m.get('file_path')
        self.part_info_list = []
        if m.get('part_info_list') is not None:
            for k in m.get('part_info_list'):
                temp_model = UploadPartInfo()
                self.part_info_list.append(temp_model.from_map(k))
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('upload_id') is not None:
            self.upload_id = m.get('upload_id')
        return self


class HostingListFileRequest(TeaModel):
    """
    list file request
    """
    def __init__(
        self,
        addition_data: dict = None,
        drive_id: str = None,
        image_cropping_aspect_ratios: List[str] = None,
        image_thumbnail_process: str = None,
        image_url_process: str = None,
        limit: int = None,
        marker: str = None,
        parent_file_path: str = None,
        referer: str = None,
        share_id: str = None,
        sign_token: str = None,
        url_expire_sec: int = None,
        video_thumbnail_process: str = None,
    ):
        # addition_data
        self.addition_data = addition_data
        # drive_id
        self.drive_id = drive_id
        self.image_cropping_aspect_ratios = image_cropping_aspect_ratios
        # image_thumbnail_process
        self.image_thumbnail_process = image_thumbnail_process
        # image_url_process
        self.image_url_process = image_url_process
        # limit
        self.limit = limit
        # marker
        self.marker = marker
        # ParentFilePath
        self.parent_file_path = parent_file_path
        self.referer = referer
        # share_id
        self.share_id = share_id
        self.sign_token = sign_token
        # url_expire_sec
        self.url_expire_sec = url_expire_sec
        # video_thumbnail_process
        # type:string
        self.video_thumbnail_process = video_thumbnail_process

    def validate(self):
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.limit is not None:
            self.validate_maximum(self.limit, 'limit', 100)
            self.validate_minimum(self.limit, 'limit', 0)
        self.validate_required(self.parent_file_path, 'parent_file_path')
        if self.share_id is not None:
            self.validate_pattern(self.share_id, 'share_id', '[0-9a-zA-Z-]+')
        if self.url_expire_sec is not None:
            self.validate_maximum(self.url_expire_sec, 'url_expire_sec', 14400)
            self.validate_minimum(self.url_expire_sec, 'url_expire_sec', 10)

    def to_map(self):
        result = dict()
        if self.addition_data is not None:
            result['addition_data'] = self.addition_data
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.image_cropping_aspect_ratios is not None:
            result['image_cropping_aspect_ratios'] = self.image_cropping_aspect_ratios
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
        if self.referer is not None:
            result['referer'] = self.referer
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.sign_token is not None:
            result['sign_token'] = self.sign_token
        if self.url_expire_sec is not None:
            result['url_expire_sec'] = self.url_expire_sec
        if self.video_thumbnail_process is not None:
            result['video_thumbnail_process'] = self.video_thumbnail_process
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('addition_data') is not None:
            self.addition_data = m.get('addition_data')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('image_cropping_aspect_ratios') is not None:
            self.image_cropping_aspect_ratios = m.get('image_cropping_aspect_ratios')
        if m.get('image_thumbnail_process') is not None:
            self.image_thumbnail_process = m.get('image_thumbnail_process')
        if m.get('image_url_process') is not None:
            self.image_url_process = m.get('image_url_process')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('parent_file_path') is not None:
            self.parent_file_path = m.get('parent_file_path')
        if m.get('referer') is not None:
            self.referer = m.get('referer')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('sign_token') is not None:
            self.sign_token = m.get('sign_token')
        if m.get('url_expire_sec') is not None:
            self.url_expire_sec = m.get('url_expire_sec')
        if m.get('video_thumbnail_process') is not None:
            self.video_thumbnail_process = m.get('video_thumbnail_process')
        return self


class HostingListUploadedPartRequest(TeaModel):
    """
    列举uploadID对应的已上传分片
    """
    def __init__(
        self,
        drive_id: str = None,
        file_path: str = None,
        limit: int = None,
        part_number_marker: int = None,
        share_id: str = None,
        upload_id: str = None,
    ):
        # drive_id
        self.drive_id = drive_id
        # file_path
        self.file_path = file_path
        # limit
        self.limit = limit
        # part_number_marker
        self.part_number_marker = part_number_marker
        # share_id
        self.share_id = share_id
        # upload_id
        self.upload_id = upload_id

    def validate(self):
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_path, 'file_path')
        if self.limit is not None:
            self.validate_maximum(self.limit, 'limit', 1000)
            self.validate_minimum(self.limit, 'limit', 1)
        if self.part_number_marker is not None:
            self.validate_minimum(self.part_number_marker, 'part_number_marker', 1)
        if self.share_id is not None:
            self.validate_pattern(self.share_id, 'share_id', '[0-9a-zA-Z-]+')

    def to_map(self):
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_path') is not None:
            self.file_path = m.get('file_path')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('part_number_marker') is not None:
            self.part_number_marker = m.get('part_number_marker')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('upload_id') is not None:
            self.upload_id = m.get('upload_id')
        return self


class HostingMoveFileRequest(TeaModel):
    """
    文件移动请求
    """
    def __init__(
        self,
        drive_id: str = None,
        file_path: str = None,
        new_name: str = None,
        overwrite: bool = None,
        share_id: str = None,
        to_parent_file_path: str = None,
    ):
        # drive_id
        self.drive_id = drive_id
        # file_path
        self.file_path = file_path
        # new_name
        self.new_name = new_name
        # overwrite
        # type: boolean
        self.overwrite = overwrite
        # share_id
        self.share_id = share_id
        # file_path
        self.to_parent_file_path = to_parent_file_path

    def validate(self):
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.share_id is not None:
            self.validate_pattern(self.share_id, 'share_id', '[0-9a-zA-Z-]+')

    def to_map(self):
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_path') is not None:
            self.file_path = m.get('file_path')
        if m.get('new_name') is not None:
            self.new_name = m.get('new_name')
        if m.get('overwrite') is not None:
            self.overwrite = m.get('overwrite')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('to_parent_file_path') is not None:
            self.to_parent_file_path = m.get('to_parent_file_path')
        return self


class HostingVideoDRMLicenseRequest(TeaModel):
    """
    获取视频DRM License
    """
    def __init__(
        self,
        drm_type: str = None,
        license_request: str = None,
    ):
        # drmType
        self.drm_type = drm_type
        # licenseRequest
        self.license_request = license_request

    def validate(self):
        self.validate_required(self.drm_type, 'drm_type')
        self.validate_required(self.license_request, 'license_request')

    def to_map(self):
        result = dict()
        if self.drm_type is not None:
            result['drmType'] = self.drm_type
        if self.license_request is not None:
            result['licenseRequest'] = self.license_request
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drmType') is not None:
            self.drm_type = m.get('drmType')
        if m.get('licenseRequest') is not None:
            self.license_request = m.get('licenseRequest')
        return self


class HostingVideoDefinitionRequest(TeaModel):
    """
    获取视频分辨率列表
    """
    def __init__(
        self,
        drive_id: str = None,
        file_path: str = None,
        protection_scheme: str = None,
        share_id: str = None,
    ):
        # drive_id
        self.drive_id = drive_id
        # file_path
        self.file_path = file_path
        # protection_scheme
        self.protection_scheme = protection_scheme
        # share_id
        self.share_id = share_id

    def validate(self):
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_path, 'file_path')
        if self.file_path is not None:
            self.validate_max_length(self.file_path, 'file_path', 1000)
        if self.share_id is not None:
            self.validate_pattern(self.share_id, 'share_id', '[0-9a-zA-Z-]+')

    def to_map(self):
        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_path is not None:
            result['file_path'] = self.file_path
        if self.protection_scheme is not None:
            result['protection_scheme'] = self.protection_scheme
        if self.share_id is not None:
            result['share_id'] = self.share_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_path') is not None:
            self.file_path = m.get('file_path')
        if m.get('protection_scheme') is not None:
            self.protection_scheme = m.get('protection_scheme')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        return self


class HostingVideoM3U8Request(TeaModel):
    """
    获取视频的m3u8文件
    """
    def __init__(
        self,
        definition: str = None,
        drive_id: str = None,
        expire_sec: int = None,
        file_path: str = None,
        protection_scheme: str = None,
        share_id: str = None,
        sign_token: str = None,
    ):
        # definition
        self.definition = definition
        # drive_id
        self.drive_id = drive_id
        # expire_sec
        self.expire_sec = expire_sec
        # file_path
        self.file_path = file_path
        # protection_scheme
        self.protection_scheme = protection_scheme
        # share_id
        self.share_id = share_id
        # sign_token
        self.sign_token = sign_token

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
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('definition') is not None:
            self.definition = m.get('definition')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('expire_sec') is not None:
            self.expire_sec = m.get('expire_sec')
        if m.get('file_path') is not None:
            self.file_path = m.get('file_path')
        if m.get('protection_scheme') is not None:
            self.protection_scheme = m.get('protection_scheme')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('sign_token') is not None:
            self.sign_token = m.get('sign_token')
        return self


class HostingVideoTranscodeRequest(TeaModel):
    """
    启动视频转码请求
    """
    def __init__(
        self,
        drive_id: str = None,
        file_path: str = None,
        hls_time: int = None,
        protection_scheme: str = None,
        remarks: str = None,
        share_id: str = None,
        transcode: bool = None,
    ):
        # drive_id
        self.drive_id = drive_id
        # file_path
        self.file_path = file_path
        # hls_time
        self.hls_time = hls_time
        # protection_scheme
        self.protection_scheme = protection_scheme
        # remarks
        self.remarks = remarks
        # share_id
        self.share_id = share_id
        # transcode
        self.transcode = transcode

    def validate(self):
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_path, 'file_path')
        if self.file_path is not None:
            self.validate_max_length(self.file_path, 'file_path', 1000)
        if self.share_id is not None:
            self.validate_pattern(self.share_id, 'share_id', '[0-9a-zA-Z-]+')

    def to_map(self):
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_path') is not None:
            self.file_path = m.get('file_path')
        if m.get('hls_time') is not None:
            self.hls_time = m.get('hls_time')
        if m.get('protection_scheme') is not None:
            self.protection_scheme = m.get('protection_scheme')
        if m.get('remarks') is not None:
            self.remarks = m.get('remarks')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('transcode') is not None:
            self.transcode = m.get('transcode')
        return self


class ListByAnonymousRequest(TeaModel):
    """
    list_file_by_anonymous request
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        image_thumbnail_process: str = None,
        image_url_process: str = None,
        limit: int = None,
        marker: str = None,
        parent_file_id: str = None,
        referer: str = None,
        share_id: str = None,
        sign_token: str = None,
        video_thumbnail_process: str = None,
    ):
        self.headers = headers
        # image_thumbnail_process
        self.image_thumbnail_process = image_thumbnail_process
        # image_url_process
        self.image_url_process = image_url_process
        # limit
        self.limit = limit
        # marker
        self.marker = marker
        # parent_file_id
        self.parent_file_id = parent_file_id
        self.referer = referer
        # share_id
        self.share_id = share_id
        self.sign_token = sign_token
        # video_thumbnail_process
        # type:string
        self.video_thumbnail_process = video_thumbnail_process

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
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.image_thumbnail_process is not None:
            result['image_thumbnail_process'] = self.image_thumbnail_process
        if self.image_url_process is not None:
            result['image_url_process'] = self.image_url_process
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        if self.parent_file_id is not None:
            result['parent_file_id'] = self.parent_file_id
        if self.referer is not None:
            result['referer'] = self.referer
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.sign_token is not None:
            result['sign_token'] = self.sign_token
        if self.video_thumbnail_process is not None:
            result['video_thumbnail_process'] = self.video_thumbnail_process
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('image_thumbnail_process') is not None:
            self.image_thumbnail_process = m.get('image_thumbnail_process')
        if m.get('image_url_process') is not None:
            self.image_url_process = m.get('image_url_process')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('parent_file_id') is not None:
            self.parent_file_id = m.get('parent_file_id')
        if m.get('referer') is not None:
            self.referer = m.get('referer')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('sign_token') is not None:
            self.sign_token = m.get('sign_token')
        if m.get('video_thumbnail_process') is not None:
            self.video_thumbnail_process = m.get('video_thumbnail_process')
        return self


class ListDriveRequest(TeaModel):
    """
    List drive request
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        limit: int = None,
        marker: str = None,
        owner: str = None,
        owner_type: str = None,
        subdomain_id: str = None,
    ):
        self.headers = headers
        # 每页大小限制
        self.limit = limit
        # 翻页标记, 接口返回的标记值
        self.marker = marker
        # 所属者
        self.owner = owner
        # owner_type
        # 所述者类型
        self.owner_type = owner_type
        # Subdomain ID
        self.subdomain_id = subdomain_id

    def validate(self):
        if self.limit is not None:
            self.validate_maximum(self.limit, 'limit', 100)
            self.validate_minimum(self.limit, 'limit', 1)

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        if self.owner is not None:
            result['owner'] = self.owner
        if self.owner_type is not None:
            result['owner_type'] = self.owner_type
        if self.subdomain_id is not None:
            result['subdomain_id'] = self.subdomain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('owner_type') is not None:
            self.owner_type = m.get('owner_type')
        if m.get('subdomain_id') is not None:
            self.subdomain_id = m.get('subdomain_id')
        return self


class ListFileByCustomIndexKeyRequest(TeaModel):
    """
    列举文件
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        starred: bool = None,
        addition_data: dict = None,
        category: str = None,
        custom_index_key: str = None,
        drive_id: str = None,
        encrypt_mode: str = None,
        fields: str = None,
        image_cropping_aspect_ratios: List[str] = None,
        image_thumbnail_process: str = None,
        image_url_process: str = None,
        limit: int = None,
        marker: str = None,
        order_direction: str = None,
        referer: str = None,
        share_id: str = None,
        sign_token: str = None,
        status: str = None,
        type: str = None,
        url_expire_sec: int = None,
        video_thumbnail_process: str = None,
    ):
        self.headers = headers
        # starred
        self.starred = starred
        # addition_data
        self.addition_data = addition_data
        # category
        self.category = category
        # custom_index_key
        self.custom_index_key = custom_index_key
        # drive_id
        self.drive_id = drive_id
        # encrypt_mode
        self.encrypt_mode = encrypt_mode
        # fields
        self.fields = fields
        self.image_cropping_aspect_ratios = image_cropping_aspect_ratios
        # image_thumbnail_process
        self.image_thumbnail_process = image_thumbnail_process
        # image_url_process
        self.image_url_process = image_url_process
        # limit
        self.limit = limit
        # marker
        self.marker = marker
        # order_direction
        self.order_direction = order_direction
        self.referer = referer
        # share_id, either share_id or drive_id is required
        self.share_id = share_id
        self.sign_token = sign_token
        # status
        self.status = status
        # type
        self.type = type
        # url_expire_sec
        self.url_expire_sec = url_expire_sec
        # video_thumbnail_process
        # type:string
        self.video_thumbnail_process = video_thumbnail_process

    def validate(self):
        self.validate_required(self.custom_index_key, 'custom_index_key')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.limit is not None:
            self.validate_maximum(self.limit, 'limit', 100)
            self.validate_minimum(self.limit, 'limit', 0)
        if self.url_expire_sec is not None:
            self.validate_maximum(self.url_expire_sec, 'url_expire_sec', 14400)
            self.validate_minimum(self.url_expire_sec, 'url_expire_sec', 10)

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.starred is not None:
            result['Starred'] = self.starred
        if self.addition_data is not None:
            result['addition_data'] = self.addition_data
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
        if self.image_cropping_aspect_ratios is not None:
            result['image_cropping_aspect_ratios'] = self.image_cropping_aspect_ratios
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
        if self.referer is not None:
            result['referer'] = self.referer
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.sign_token is not None:
            result['sign_token'] = self.sign_token
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        if self.url_expire_sec is not None:
            result['url_expire_sec'] = self.url_expire_sec
        if self.video_thumbnail_process is not None:
            result['video_thumbnail_process'] = self.video_thumbnail_process
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('Starred') is not None:
            self.starred = m.get('Starred')
        if m.get('addition_data') is not None:
            self.addition_data = m.get('addition_data')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('custom_index_key') is not None:
            self.custom_index_key = m.get('custom_index_key')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('encrypt_mode') is not None:
            self.encrypt_mode = m.get('encrypt_mode')
        if m.get('fields') is not None:
            self.fields = m.get('fields')
        if m.get('image_cropping_aspect_ratios') is not None:
            self.image_cropping_aspect_ratios = m.get('image_cropping_aspect_ratios')
        if m.get('image_thumbnail_process') is not None:
            self.image_thumbnail_process = m.get('image_thumbnail_process')
        if m.get('image_url_process') is not None:
            self.image_url_process = m.get('image_url_process')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('order_direction') is not None:
            self.order_direction = m.get('order_direction')
        if m.get('referer') is not None:
            self.referer = m.get('referer')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('sign_token') is not None:
            self.sign_token = m.get('sign_token')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('url_expire_sec') is not None:
            self.url_expire_sec = m.get('url_expire_sec')
        if m.get('video_thumbnail_process') is not None:
            self.video_thumbnail_process = m.get('video_thumbnail_process')
        return self


class ListFileDeltaRequest(TeaModel):
    """
    获取增量文件操作记录
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        cursor: str = None,
        drive_id: str = None,
        image_cropping_aspect_ratios: List[str] = None,
        image_thumbnail_process: str = None,
        image_url_process: str = None,
        limit: int = None,
        video_thumbnail_process: str = None,
    ):
        self.headers = headers
        # cursor 游标
        self.cursor = cursor
        # drive_id
        self.drive_id = drive_id
        self.image_cropping_aspect_ratios = image_cropping_aspect_ratios
        # image_thumbnail_process
        self.image_thumbnail_process = image_thumbnail_process
        # image_url_process
        self.image_url_process = image_url_process
        # limit
        # default 100
        self.limit = limit
        # video_thumbnail_process
        # type:string
        self.video_thumbnail_process = video_thumbnail_process

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.cursor is not None:
            result['cursor'] = self.cursor
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.image_cropping_aspect_ratios is not None:
            result['image_cropping_aspect_ratios'] = self.image_cropping_aspect_ratios
        if self.image_thumbnail_process is not None:
            result['image_thumbnail_process'] = self.image_thumbnail_process
        if self.image_url_process is not None:
            result['image_url_process'] = self.image_url_process
        if self.limit is not None:
            result['limit'] = self.limit
        if self.video_thumbnail_process is not None:
            result['video_thumbnail_process'] = self.video_thumbnail_process
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('cursor') is not None:
            self.cursor = m.get('cursor')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('image_cropping_aspect_ratios') is not None:
            self.image_cropping_aspect_ratios = m.get('image_cropping_aspect_ratios')
        if m.get('image_thumbnail_process') is not None:
            self.image_thumbnail_process = m.get('image_thumbnail_process')
        if m.get('image_url_process') is not None:
            self.image_url_process = m.get('image_url_process')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('video_thumbnail_process') is not None:
            self.video_thumbnail_process = m.get('video_thumbnail_process')
        return self


class ListFileRequest(TeaModel):
    """
    列举文件
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        addition_data: dict = None,
        all: bool = None,
        category: str = None,
        drive_id: str = None,
        fields: str = None,
        image_cropping_aspect_ratios: List[str] = None,
        image_thumbnail_process: str = None,
        image_url_process: str = None,
        limit: int = None,
        location: str = None,
        marker: str = None,
        order_by: str = None,
        order_direction: str = None,
        parent_file_id: str = None,
        parent_file_id_path: str = None,
        referer: str = None,
        share_id: str = None,
        sign_token: str = None,
        starred: bool = None,
        status: str = None,
        type: str = None,
        url_expire_sec: int = None,
        video_thumbnail_process: str = None,
    ):
        self.headers = headers
        # addition_data
        self.addition_data = addition_data
        # all
        self.all = all
        # category
        self.category = category
        # drive_id
        self.drive_id = drive_id
        # fields
        self.fields = fields
        self.image_cropping_aspect_ratios = image_cropping_aspect_ratios
        # image_thumbnail_process
        self.image_thumbnail_process = image_thumbnail_process
        # image_url_process
        self.image_url_process = image_url_process
        # limit
        self.limit = limit
        # location
        self.location = location
        # marker
        self.marker = marker
        # order_by
        self.order_by = order_by
        # order_direction
        self.order_direction = order_direction
        # ParentFileID
        self.parent_file_id = parent_file_id
        self.parent_file_id_path = parent_file_id_path
        self.referer = referer
        # share_id, either share_id or drive_id is required
        self.share_id = share_id
        self.sign_token = sign_token
        # starred
        self.starred = starred
        # status
        self.status = status
        # type
        self.type = type
        # url_expire_sec
        self.url_expire_sec = url_expire_sec
        # video_thumbnail_process
        # type:string
        self.video_thumbnail_process = video_thumbnail_process

    def validate(self):
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.limit is not None:
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
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.addition_data is not None:
            result['addition_data'] = self.addition_data
        if self.all is not None:
            result['all'] = self.all
        if self.category is not None:
            result['category'] = self.category
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.fields is not None:
            result['fields'] = self.fields
        if self.image_cropping_aspect_ratios is not None:
            result['image_cropping_aspect_ratios'] = self.image_cropping_aspect_ratios
        if self.image_thumbnail_process is not None:
            result['image_thumbnail_process'] = self.image_thumbnail_process
        if self.image_url_process is not None:
            result['image_url_process'] = self.image_url_process
        if self.limit is not None:
            result['limit'] = self.limit
        if self.location is not None:
            result['location'] = self.location
        if self.marker is not None:
            result['marker'] = self.marker
        if self.order_by is not None:
            result['order_by'] = self.order_by
        if self.order_direction is not None:
            result['order_direction'] = self.order_direction
        if self.parent_file_id is not None:
            result['parent_file_id'] = self.parent_file_id
        if self.parent_file_id_path is not None:
            result['parent_file_id_path'] = self.parent_file_id_path
        if self.referer is not None:
            result['referer'] = self.referer
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.sign_token is not None:
            result['sign_token'] = self.sign_token
        if self.starred is not None:
            result['starred'] = self.starred
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        if self.url_expire_sec is not None:
            result['url_expire_sec'] = self.url_expire_sec
        if self.video_thumbnail_process is not None:
            result['video_thumbnail_process'] = self.video_thumbnail_process
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('addition_data') is not None:
            self.addition_data = m.get('addition_data')
        if m.get('all') is not None:
            self.all = m.get('all')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('fields') is not None:
            self.fields = m.get('fields')
        if m.get('image_cropping_aspect_ratios') is not None:
            self.image_cropping_aspect_ratios = m.get('image_cropping_aspect_ratios')
        if m.get('image_thumbnail_process') is not None:
            self.image_thumbnail_process = m.get('image_thumbnail_process')
        if m.get('image_url_process') is not None:
            self.image_url_process = m.get('image_url_process')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('order_by') is not None:
            self.order_by = m.get('order_by')
        if m.get('order_direction') is not None:
            self.order_direction = m.get('order_direction')
        if m.get('parent_file_id') is not None:
            self.parent_file_id = m.get('parent_file_id')
        if m.get('parent_file_id_path') is not None:
            self.parent_file_id_path = m.get('parent_file_id_path')
        if m.get('referer') is not None:
            self.referer = m.get('referer')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('sign_token') is not None:
            self.sign_token = m.get('sign_token')
        if m.get('starred') is not None:
            self.starred = m.get('starred')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('url_expire_sec') is not None:
            self.url_expire_sec = m.get('url_expire_sec')
        if m.get('video_thumbnail_process') is not None:
            self.video_thumbnail_process = m.get('video_thumbnail_process')
        return self


class ListMyDriveRequest(TeaModel):
    """
    List my drive request
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        limit: int = None,
        marker: str = None,
    ):
        self.headers = headers
        # 每页大小限制
        self.limit = limit
        # 翻页标记, 接口返回的标记值
        self.marker = marker

    def validate(self):
        if self.limit is not None:
            self.validate_maximum(self.limit, 'limit', 100)
            self.validate_minimum(self.limit, 'limit', 1)

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        return self


class ListShareLinkRequest(TeaModel):
    """
    list_share_link request
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        creator: str = None,
        limit: int = None,
        marker: str = None,
        order_by: str = None,
        order_direction: str = None,
    ):
        self.headers = headers
        # creator
        self.creator = creator
        # limit
        self.limit = limit
        # marker
        self.marker = marker
        # order_by
        self.order_by = order_by
        # order_direction
        self.order_direction = order_direction

    def validate(self):
        if self.limit is not None:
            self.validate_maximum(self.limit, 'limit', 100)
            self.validate_minimum(self.limit, 'limit', 1)

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.creator is not None:
            result['creator'] = self.creator
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        if self.order_by is not None:
            result['order_by'] = self.order_by
        if self.order_direction is not None:
            result['order_direction'] = self.order_direction
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('order_by') is not None:
            self.order_by = m.get('order_by')
        if m.get('order_direction') is not None:
            self.order_direction = m.get('order_direction')
        return self


class ListShareRequest(TeaModel):
    """
    list share request
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        creator: str = None,
        drive_id: str = None,
        limit: int = None,
        marker: str = None,
        owner: str = None,
        owner_type: str = None,
        share_file_path: str = None,
    ):
        self.headers = headers
        # creator
        self.creator = creator
        self.drive_id = drive_id
        # limit
        self.limit = limit
        # marker
        self.marker = marker
        # Owner
        self.owner = owner
        # owner_type
        self.owner_type = owner_type
        # share_file_path
        self.share_file_path = share_file_path

    def validate(self):
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.limit is not None:
            self.validate_maximum(self.limit, 'limit', 100)
            self.validate_minimum(self.limit, 'limit', 1)

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
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
        if self.owner_type is not None:
            result['owner_type'] = self.owner_type
        if self.share_file_path is not None:
            result['share_file_path'] = self.share_file_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('owner_type') is not None:
            self.owner_type = m.get('owner_type')
        if m.get('share_file_path') is not None:
            self.share_file_path = m.get('share_file_path')
        return self


class ListStoreFileRequest(TeaModel):
    """
    list store file
    """
    def __init__(
        self,
        limit: int = None,
        marker: str = None,
        parent_file_path: str = None,
        store_id: str = None,
        type: str = None,
    ):
        # limit
        self.limit = limit
        # marker
        self.marker = marker
        # parent_file_path
        self.parent_file_path = parent_file_path
        # store_id
        self.store_id = store_id
        # type
        self.type = type

    def validate(self):
        if self.limit is not None:
            self.validate_maximum(self.limit, 'limit', 1000)
            self.validate_minimum(self.limit, 'limit', 1)

    def to_map(self):
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('parent_file_path') is not None:
            self.parent_file_path = m.get('parent_file_path')
        if m.get('store_id') is not None:
            self.store_id = m.get('store_id')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListStoreRequest(TeaModel):
    """
    list storage file
    """
    def __init__(
        self,
        domain_id: str = None,
    ):
        # domain_id
        self.domain_id = domain_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        return self


class ListUploadedPartRequest(TeaModel):
    """
    列举uploadID对应的已上传分片
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        drive_id: str = None,
        file_id: str = None,
        file_id_path: str = None,
        limit: int = None,
        part_number_marker: int = None,
        share_id: str = None,
        upload_id: str = None,
    ):
        self.headers = headers
        # drive_id
        self.drive_id = drive_id
        # file_id
        self.file_id = file_id
        self.file_id_path = file_id_path
        # limit
        self.limit = limit
        # part_number_marker
        self.part_number_marker = part_number_marker
        self.share_id = share_id
        # upload_id
        self.upload_id = upload_id

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_id, 'file_id')
        if self.file_id is not None:
            self.validate_max_length(self.file_id, 'file_id', 50)
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9.-_]{1,50}')
        if self.limit is not None:
            self.validate_maximum(self.limit, 'limit', 1000)
            self.validate_minimum(self.limit, 'limit', 1)
        if self.part_number_marker is not None:
            self.validate_minimum(self.part_number_marker, 'part_number_marker', 1)

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.file_id_path is not None:
            result['file_id_path'] = self.file_id_path
        if self.limit is not None:
            result['limit'] = self.limit
        if self.part_number_marker is not None:
            result['part_number_marker'] = self.part_number_marker
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.upload_id is not None:
            result['upload_id'] = self.upload_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('file_id_path') is not None:
            self.file_id_path = m.get('file_id_path')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('part_number_marker') is not None:
            self.part_number_marker = m.get('part_number_marker')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('upload_id') is not None:
            self.upload_id = m.get('upload_id')
        return self


class MoveFileRequest(TeaModel):
    """
    文件移动请求
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        auto_rename: bool = None,
        drive_id: str = None,
        file_id: str = None,
        file_id_path: str = None,
        new_name: str = None,
        share_id: str = None,
        to_drive_id: str = None,
        to_parent_file_id: str = None,
        to_share_id: str = None,
    ):
        self.headers = headers
        # auto_rename
        self.auto_rename = auto_rename
        # drive_id
        self.drive_id = drive_id
        # file_id
        self.file_id = file_id
        self.file_id_path = file_id_path
        # new_name
        self.new_name = new_name
        self.share_id = share_id
        # to_drive_id
        self.to_drive_id = to_drive_id
        # to_parent_file_id
        self.to_parent_file_id = to_parent_file_id
        self.to_share_id = to_share_id

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
        if self.to_drive_id is not None:
            self.validate_pattern(self.to_drive_id, 'to_drive_id', '[0-9]+')
        self.validate_required(self.to_parent_file_id, 'to_parent_file_id')
        if self.to_parent_file_id is not None:
            self.validate_max_length(self.to_parent_file_id, 'to_parent_file_id', 50)
        if self.to_share_id is not None:
            self.validate_pattern(self.to_share_id, 'to_share_id', '[0-9]+')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.auto_rename is not None:
            result['auto_rename'] = self.auto_rename
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.file_id_path is not None:
            result['file_id_path'] = self.file_id_path
        if self.new_name is not None:
            result['new_name'] = self.new_name
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.to_drive_id is not None:
            result['to_drive_id'] = self.to_drive_id
        if self.to_parent_file_id is not None:
            result['to_parent_file_id'] = self.to_parent_file_id
        if self.to_share_id is not None:
            result['to_share_id'] = self.to_share_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('auto_rename') is not None:
            self.auto_rename = m.get('auto_rename')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('file_id_path') is not None:
            self.file_id_path = m.get('file_id_path')
        if m.get('new_name') is not None:
            self.new_name = m.get('new_name')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('to_drive_id') is not None:
            self.to_drive_id = m.get('to_drive_id')
        if m.get('to_parent_file_id') is not None:
            self.to_parent_file_id = m.get('to_parent_file_id')
        if m.get('to_share_id') is not None:
            self.to_share_id = m.get('to_share_id')
        return self


class PlayMediaRequest(TeaModel):
    """
    play_media request
    """
    def __init__(
        self,
        auth_key: str = None,
        drive_id: str = None,
        file_id: str = None,
    ):
        # auth_key
        self.auth_key = auth_key
        # drive_id
        self.drive_id = drive_id
        # file_id
        self.file_id = file_id

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
        result = dict()
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        if self.drive_id is not None:
            result['DriveID'] = self.drive_id
        if self.file_id is not None:
            result['FileID'] = self.file_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        if m.get('DriveID') is not None:
            self.drive_id = m.get('DriveID')
        if m.get('FileID') is not None:
            self.file_id = m.get('FileID')
        return self


class RefreshOfficeEditTokenRequest(TeaModel):
    """
    刷新office文档在线编辑凭证
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        addition_data: dict = None,
        location: str = None,
        office_access_token: str = None,
        office_refresh_token: str = None,
    ):
        self.headers = headers
        # addition_data
        self.addition_data = addition_data
        # location
        self.location = location
        # AccessToken
        self.office_access_token = office_access_token
        # RefreshToken
        self.office_refresh_token = office_refresh_token

    def validate(self):
        self.validate_required(self.office_access_token, 'office_access_token')
        self.validate_required(self.office_refresh_token, 'office_refresh_token')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.addition_data is not None:
            result['addition_data'] = self.addition_data
        if self.location is not None:
            result['location'] = self.location
        if self.office_access_token is not None:
            result['office_access_token'] = self.office_access_token
        if self.office_refresh_token is not None:
            result['office_refresh_token'] = self.office_refresh_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('addition_data') is not None:
            self.addition_data = m.get('addition_data')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('office_access_token') is not None:
            self.office_access_token = m.get('office_access_token')
        if m.get('office_refresh_token') is not None:
            self.office_refresh_token = m.get('office_refresh_token')
        return self


class ScanFileMetaRequest(TeaModel):
    """
    全量获取file元信息的请求body
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        addition_data: dict = None,
        category: str = None,
        drive_id: str = None,
        image_cropping_aspect_ratios: List[str] = None,
        image_thumbnail_process: str = None,
        image_url_process: str = None,
        limit: int = None,
        marker: str = None,
        video_thumbnail_process: str = None,
    ):
        self.headers = headers
        # addition_data
        self.addition_data = addition_data
        # category
        self.category = category
        # drive_id
        self.drive_id = drive_id
        self.image_cropping_aspect_ratios = image_cropping_aspect_ratios
        # image_thumbnail_process
        self.image_thumbnail_process = image_thumbnail_process
        # image_url_process
        self.image_url_process = image_url_process
        # limit
        self.limit = limit
        # marker
        self.marker = marker
        # video_thumbnail_process
        # type:string
        self.video_thumbnail_process = video_thumbnail_process

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.limit is not None:
            self.validate_maximum(self.limit, 'limit', 5000)
            self.validate_minimum(self.limit, 'limit', 1)

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.addition_data is not None:
            result['addition_data'] = self.addition_data
        if self.category is not None:
            result['category'] = self.category
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.image_cropping_aspect_ratios is not None:
            result['image_cropping_aspect_ratios'] = self.image_cropping_aspect_ratios
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('addition_data') is not None:
            self.addition_data = m.get('addition_data')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('image_cropping_aspect_ratios') is not None:
            self.image_cropping_aspect_ratios = m.get('image_cropping_aspect_ratios')
        if m.get('image_thumbnail_process') is not None:
            self.image_thumbnail_process = m.get('image_thumbnail_process')
        if m.get('image_url_process') is not None:
            self.image_url_process = m.get('image_url_process')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('video_thumbnail_process') is not None:
            self.video_thumbnail_process = m.get('video_thumbnail_process')
        return self


class SearchFileRequest(TeaModel):
    """
    搜索文件元数据
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        addition_data: dict = None,
        drive_id: str = None,
        image_cropping_aspect_ratios: List[str] = None,
        image_thumbnail_process: str = None,
        image_url_process: str = None,
        limit: int = None,
        location: str = None,
        marker: str = None,
        order_by: str = None,
        query: str = None,
        referer: str = None,
        return_total_count: bool = None,
        sign_token: str = None,
        url_expire_sec: int = None,
        video_thumbnail_process: str = None,
    ):
        self.headers = headers
        # addition_data
        self.addition_data = addition_data
        # drive_id
        self.drive_id = drive_id
        self.image_cropping_aspect_ratios = image_cropping_aspect_ratios
        # image_thumbnail_process
        self.image_thumbnail_process = image_thumbnail_process
        # image_url_process
        self.image_url_process = image_url_process
        # limit
        self.limit = limit
        # location
        self.location = location
        # Marker
        self.marker = marker
        # order_by
        self.order_by = order_by
        # query
        self.query = query
        # referer
        self.referer = referer
        # return_total_count 是否返回查询总数
        self.return_total_count = return_total_count
        # sign_token
        self.sign_token = sign_token
        # url_expire_sec
        self.url_expire_sec = url_expire_sec
        # video_thumbnail_process
        # type:string
        self.video_thumbnail_process = video_thumbnail_process

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
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.addition_data is not None:
            result['addition_data'] = self.addition_data
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.image_cropping_aspect_ratios is not None:
            result['image_cropping_aspect_ratios'] = self.image_cropping_aspect_ratios
        if self.image_thumbnail_process is not None:
            result['image_thumbnail_process'] = self.image_thumbnail_process
        if self.image_url_process is not None:
            result['image_url_process'] = self.image_url_process
        if self.limit is not None:
            result['limit'] = self.limit
        if self.location is not None:
            result['location'] = self.location
        if self.marker is not None:
            result['marker'] = self.marker
        if self.order_by is not None:
            result['order_by'] = self.order_by
        if self.query is not None:
            result['query'] = self.query
        if self.referer is not None:
            result['referer'] = self.referer
        if self.return_total_count is not None:
            result['return_total_count'] = self.return_total_count
        if self.sign_token is not None:
            result['sign_token'] = self.sign_token
        if self.url_expire_sec is not None:
            result['url_expire_sec'] = self.url_expire_sec
        if self.video_thumbnail_process is not None:
            result['video_thumbnail_process'] = self.video_thumbnail_process
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('addition_data') is not None:
            self.addition_data = m.get('addition_data')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('image_cropping_aspect_ratios') is not None:
            self.image_cropping_aspect_ratios = m.get('image_cropping_aspect_ratios')
        if m.get('image_thumbnail_process') is not None:
            self.image_thumbnail_process = m.get('image_thumbnail_process')
        if m.get('image_url_process') is not None:
            self.image_url_process = m.get('image_url_process')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('order_by') is not None:
            self.order_by = m.get('order_by')
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('referer') is not None:
            self.referer = m.get('referer')
        if m.get('return_total_count') is not None:
            self.return_total_count = m.get('return_total_count')
        if m.get('sign_token') is not None:
            self.sign_token = m.get('sign_token')
        if m.get('url_expire_sec') is not None:
            self.url_expire_sec = m.get('url_expire_sec')
        if m.get('video_thumbnail_process') is not None:
            self.video_thumbnail_process = m.get('video_thumbnail_process')
        return self


class UCGetObjectInfoByObjectKeyRequest(TeaModel):
    """
    UCGetObjectInfoByObjectKeyRequest
    """
    def __init__(
        self,
        object_key: str = None,
    ):
        self.object_key = object_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.object_key is not None:
            result['object_key'] = self.object_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('object_key') is not None:
            self.object_key = m.get('object_key')
        return self


class UCGetObjectInfoBySha1Request(TeaModel):
    """
    UCGetObjectInfoBySha1Request
    """
    def __init__(
        self,
        sha_1: str = None,
    ):
        self.sha_1 = sha_1

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.sha_1 is not None:
            result['sha1'] = self.sha_1
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sha1') is not None:
            self.sha_1 = m.get('sha1')
        return self


class UpdateDriveRequest(TeaModel):
    """
    Update drive request
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        description: str = None,
        drive_id: str = None,
        drive_name: str = None,
        encrypt_data_access: bool = None,
        encrypt_mode: str = None,
        status: str = None,
        subdomain_id: str = None,
        total_size: int = None,
    ):
        self.headers = headers
        # 描述信息
        self.description = description
        # Drive ID
        self.drive_id = drive_id
        # Drive 名称
        self.drive_name = drive_name
        # 授权访问加密数据
        self.encrypt_data_access = encrypt_data_access
        # 加密模式
        self.encrypt_mode = encrypt_mode
        # 状态
        self.status = status
        # Subdomain ID
        self.subdomain_id = subdomain_id
        # 总大小,单位Byte [如果设置 -1 代表不限制]
        self.total_size = total_size

    def validate(self):
        if self.description is not None:
            self.validate_max_length(self.description, 'description', 1024)
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_name is not None:
            self.validate_max_length(self.drive_name, 'drive_name', 1024)

    def to_map(self):
        result = dict()
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
        if self.subdomain_id is not None:
            result['subdomain_id'] = self.subdomain_id
        if self.total_size is not None:
            result['total_size'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('drive_name') is not None:
            self.drive_name = m.get('drive_name')
        if m.get('encrypt_data_access') is not None:
            self.encrypt_data_access = m.get('encrypt_data_access')
        if m.get('encrypt_mode') is not None:
            self.encrypt_mode = m.get('encrypt_mode')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('subdomain_id') is not None:
            self.subdomain_id = m.get('subdomain_id')
        if m.get('total_size') is not None:
            self.total_size = m.get('total_size')
        return self


class UpdateFileMetaRequest(TeaModel):
    """
    更新文件元数据
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        check_name_mode: str = None,
        custom_index_key: str = None,
        description: str = None,
        drive_id: str = None,
        encrypt_mode: str = None,
        file_id: str = None,
        file_id_path: str = None,
        hidden: bool = None,
        labels: List[str] = None,
        meta: str = None,
        name: str = None,
        referer: str = None,
        share_id: str = None,
        sign_token: str = None,
        starred: bool = None,
        user_meta: str = None,
    ):
        self.headers = headers
        # check_name_mode
        self.check_name_mode = check_name_mode
        self.custom_index_key = custom_index_key
        # description
        # type: string
        self.description = description
        # drive_id
        self.drive_id = drive_id
        self.encrypt_mode = encrypt_mode
        # file_id
        self.file_id = file_id
        self.file_id_path = file_id_path
        # hidden
        # type: boolean
        self.hidden = hidden
        # labels
        self.labels = labels
        self.meta = meta
        # name
        self.name = name
        self.referer = referer
        self.share_id = share_id
        self.sign_token = sign_token
        # starred
        # type: boolean
        self.starred = starred
        # user_meta
        self.user_meta = user_meta

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
        result = dict()
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
        if self.file_id_path is not None:
            result['file_id_path'] = self.file_id_path
        if self.hidden is not None:
            result['hidden'] = self.hidden
        if self.labels is not None:
            result['labels'] = self.labels
        if self.meta is not None:
            result['meta'] = self.meta
        if self.name is not None:
            result['name'] = self.name
        if self.referer is not None:
            result['referer'] = self.referer
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.sign_token is not None:
            result['sign_token'] = self.sign_token
        if self.starred is not None:
            result['starred'] = self.starred
        if self.user_meta is not None:
            result['user_meta'] = self.user_meta
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('check_name_mode') is not None:
            self.check_name_mode = m.get('check_name_mode')
        if m.get('custom_index_key') is not None:
            self.custom_index_key = m.get('custom_index_key')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('encrypt_mode') is not None:
            self.encrypt_mode = m.get('encrypt_mode')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('file_id_path') is not None:
            self.file_id_path = m.get('file_id_path')
        if m.get('hidden') is not None:
            self.hidden = m.get('hidden')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('meta') is not None:
            self.meta = m.get('meta')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('referer') is not None:
            self.referer = m.get('referer')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('sign_token') is not None:
            self.sign_token = m.get('sign_token')
        if m.get('starred') is not None:
            self.starred = m.get('starred')
        if m.get('user_meta') is not None:
            self.user_meta = m.get('user_meta')
        return self


class UpdateShareLinkRequest(TeaModel):
    """
    update_share_link request
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        description: str = None,
        expiration: str = None,
        share_id: str = None,
        share_name: str = None,
        share_pwd: str = None,
    ):
        self.headers = headers
        # description
        self.description = description
        # expiration
        self.expiration = expiration
        # share_id
        self.share_id = share_id
        # share_name
        self.share_name = share_name
        # share_pwd
        self.share_pwd = share_pwd

    def validate(self):
        if self.share_pwd is not None:
            self.validate_maximum(self.share_pwd, 'share_pwd', 64)
            self.validate_minimum(self.share_pwd, 'share_pwd', 0)

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.description is not None:
            result['description'] = self.description
        if self.expiration is not None:
            result['expiration'] = self.expiration
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.share_name is not None:
            result['share_name'] = self.share_name
        if self.share_pwd is not None:
            result['share_pwd'] = self.share_pwd
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('expiration') is not None:
            self.expiration = m.get('expiration')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('share_name') is not None:
            self.share_name = m.get('share_name')
        if m.get('share_pwd') is not None:
            self.share_pwd = m.get('share_pwd')
        return self


class UpdateShareRequest(TeaModel):
    """
    update share request
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        description: str = None,
        expiration: str = None,
        permissions: List[str] = None,
        share_id: str = None,
        share_name: str = None,
        share_policy: List[SharePermissionPolicy] = None,
        status: str = None,
    ):
        self.headers = headers
        # description
        self.description = description
        # expiration
        self.expiration = expiration
        # permissions
        self.permissions = permissions
        # share_id
        self.share_id = share_id
        # share_name
        self.share_name = share_name
        # share_policy
        self.share_policy = share_policy
        # status
        self.status = status

    def validate(self):
        if self.description is not None:
            self.validate_max_length(self.description, 'description', 1024)
        self.validate_required(self.share_id, 'share_id')
        if self.share_policy:
            for k in self.share_policy:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('expiration') is not None:
            self.expiration = m.get('expiration')
        if m.get('permissions') is not None:
            self.permissions = m.get('permissions')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('share_name') is not None:
            self.share_name = m.get('share_name')
        self.share_policy = []
        if m.get('share_policy') is not None:
            for k in m.get('share_policy'):
                temp_model = SharePermissionPolicy()
                self.share_policy.append(temp_model.from_map(k))
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class CreateGroupResponse(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        created_at: int = None,
        description: str = None,
        domain_id: str = None,
        group_id: str = None,
        group_name: str = None,
        updated_at: int = None,
    ):
        # created_at
        self.created_at = created_at
        # description
        self.description = description
        # domain id
        self.domain_id = domain_id
        # group id
        self.group_id = group_id
        # group name
        self.group_name = group_name
        # updated_at
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.group_id is not None:
            result['group_id'] = self.group_id
        if self.group_name is not None:
            result['group_name'] = self.group_name
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')
        if m.get('group_name') is not None:
            self.group_name = m.get('group_name')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        return self


class CreateGroupModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateGroupResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateGroupResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGroupResponse(TeaModel):
    """
    *\
    """
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteGroupModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteGroupResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteGroupResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGroupResponse(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        created_at: int = None,
        description: str = None,
        domain_id: str = None,
        group_id: str = None,
        group_name: str = None,
        updated_at: int = None,
    ):
        # created_at
        self.created_at = created_at
        # description
        self.description = description
        # domain id
        self.domain_id = domain_id
        # group id
        self.group_id = group_id
        # group name
        self.group_name = group_name
        # updated_at
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.group_id is not None:
            result['group_id'] = self.group_id
        if self.group_name is not None:
            result['group_name'] = self.group_name
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')
        if m.get('group_name') is not None:
            self.group_name = m.get('group_name')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        return self


class GetGroupModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetGroupResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetGroupResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class BaseGroupResponse(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        created_at: int = None,
        description: str = None,
        domain_id: str = None,
        group_id: str = None,
        group_name: str = None,
        updated_at: int = None,
    ):
        # created_at
        self.created_at = created_at
        # description
        self.description = description
        # domain id
        self.domain_id = domain_id
        # group id
        self.group_id = group_id
        # group name
        self.group_name = group_name
        # updated_at
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.group_id is not None:
            result['group_id'] = self.group_id
        if self.group_name is not None:
            result['group_name'] = self.group_name
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')
        if m.get('group_name') is not None:
            self.group_name = m.get('group_name')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        return self


class ListGroupResponse(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        items: List[BaseGroupResponse] = None,
        next_marker: str = None,
    ):
        # items
        self.items = items
        # 翻页标记
        self.next_marker = next_marker

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = BaseGroupResponse()
                self.items.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        return self


class ListGroupModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListGroupResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListGroupResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchGroupResponse(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        items: List[BaseGroupResponse] = None,
        next_marker: str = None,
    ):
        # items
        self.items = items
        # next_marker
        self.next_marker = next_marker

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = BaseGroupResponse()
                self.items.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        return self


class SearchGroupModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SearchGroupResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SearchGroupResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGroupResponse(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        created_at: int = None,
        description: str = None,
        domain_id: str = None,
        group_id: str = None,
        group_name: str = None,
        updated_at: int = None,
    ):
        # created_at
        self.created_at = created_at
        # description
        self.description = description
        # domain id
        self.domain_id = domain_id
        # group id
        self.group_id = group_id
        # group name
        self.group_name = group_name
        # updated_at
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.group_id is not None:
            result['group_id'] = self.group_id
        if self.group_name is not None:
            result['group_name'] = self.group_name
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')
        if m.get('group_name') is not None:
            self.group_name = m.get('group_name')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        return self


class UpdateGroupModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateGroupResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateGroupResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMembershipResponse(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        created_at: int = None,
        description: str = None,
        domain_id: str = None,
        group_id: str = None,
        member_role: str = None,
        member_type: str = None,
        sub_group_id: str = None,
        updated_at: int = None,
        user_id: str = None,
    ):
        # created_at
        self.created_at = created_at
        # 描述
        self.description = description
        # domain id
        self.domain_id = domain_id
        # group id
        self.group_id = group_id
        # 角色， member or admin
        self.member_role = member_role
        self.member_type = member_type
        self.sub_group_id = sub_group_id
        # updated_at
        self.updated_at = updated_at
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.group_id is not None:
            result['group_id'] = self.group_id
        if self.member_role is not None:
            result['member_role'] = self.member_role
        if self.member_type is not None:
            result['member_type'] = self.member_type
        if self.sub_group_id is not None:
            result['sub_group_id'] = self.sub_group_id
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')
        if m.get('member_role') is not None:
            self.member_role = m.get('member_role')
        if m.get('member_type') is not None:
            self.member_type = m.get('member_type')
        if m.get('sub_group_id') is not None:
            self.sub_group_id = m.get('sub_group_id')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class CreateMembershipModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateMembershipResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateMembershipResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMembershipResponse(TeaModel):
    """
    *\
    """
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteMembershipModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteMembershipResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteMembershipResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMembershipResponse(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        created_at: int = None,
        description: str = None,
        domain_id: str = None,
        group_id: str = None,
        member_role: str = None,
        member_type: str = None,
        sub_group_id: str = None,
        updated_at: int = None,
        user_id: str = None,
    ):
        # created_at
        self.created_at = created_at
        # 描述
        self.description = description
        # domain id
        self.domain_id = domain_id
        # group id
        self.group_id = group_id
        # 角色， member or admin
        self.member_role = member_role
        self.member_type = member_type
        self.sub_group_id = sub_group_id
        # updated_at
        self.updated_at = updated_at
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.group_id is not None:
            result['group_id'] = self.group_id
        if self.member_role is not None:
            result['member_role'] = self.member_role
        if self.member_type is not None:
            result['member_type'] = self.member_type
        if self.sub_group_id is not None:
            result['sub_group_id'] = self.sub_group_id
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')
        if m.get('member_role') is not None:
            self.member_role = m.get('member_role')
        if m.get('member_type') is not None:
            self.member_type = m.get('member_type')
        if m.get('sub_group_id') is not None:
            self.sub_group_id = m.get('sub_group_id')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class GetMembershipModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetMembershipResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetMembershipResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class HasMembershipResponse(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        result: bool = None,
    ):
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class HasMemberModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: HasMembershipResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = HasMembershipResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class BaseMembershipResponse(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        created_at: int = None,
        description: str = None,
        domain_id: str = None,
        group_id: str = None,
        member_role: str = None,
        member_type: str = None,
        sub_group_id: str = None,
        updated_at: int = None,
        user_id: str = None,
    ):
        # created_at
        self.created_at = created_at
        # 描述
        self.description = description
        # domain id
        self.domain_id = domain_id
        # group id
        self.group_id = group_id
        # 角色， member or admin
        self.member_role = member_role
        self.member_type = member_type
        self.sub_group_id = sub_group_id
        # updated_at
        self.updated_at = updated_at
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.group_id is not None:
            result['group_id'] = self.group_id
        if self.member_role is not None:
            result['member_role'] = self.member_role
        if self.member_type is not None:
            result['member_type'] = self.member_type
        if self.sub_group_id is not None:
            result['sub_group_id'] = self.sub_group_id
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')
        if m.get('member_role') is not None:
            self.member_role = m.get('member_role')
        if m.get('member_type') is not None:
            self.member_type = m.get('member_type')
        if m.get('sub_group_id') is not None:
            self.sub_group_id = m.get('sub_group_id')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class ListDirectChildMembershipsResponse(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        items: List[BaseMembershipResponse] = None,
        next_marker: str = None,
    ):
        # items
        self.items = items
        # 翻页标记
        self.next_marker = next_marker

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = BaseMembershipResponse()
                self.items.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        return self


class ListDirectChildMembershipsModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDirectChildMembershipsResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDirectChildMembershipsResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDirectParentMembershipsResponse(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        items: List[BaseMembershipResponse] = None,
        next_marker: str = None,
    ):
        # items
        self.items = items
        # 翻页标记
        self.next_marker = next_marker

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = BaseMembershipResponse()
                self.items.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        return self


class ListDirectMembershipsModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDirectParentMembershipsResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDirectParentMembershipsResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDirectParentMembershipsModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDirectParentMembershipsResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDirectParentMembershipsResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateMembershipResponse(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        created_at: int = None,
        description: str = None,
        domain_id: str = None,
        group_id: str = None,
        member_role: str = None,
        member_type: str = None,
        sub_group_id: str = None,
        updated_at: int = None,
        user_id: str = None,
    ):
        # created_at
        self.created_at = created_at
        # 描述
        self.description = description
        # domain id
        self.domain_id = domain_id
        # group id
        self.group_id = group_id
        # 角色， member or admin
        self.member_role = member_role
        self.member_type = member_type
        self.sub_group_id = sub_group_id
        # updated_at
        self.updated_at = updated_at
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.group_id is not None:
            result['group_id'] = self.group_id
        if self.member_role is not None:
            result['member_role'] = self.member_role
        if self.member_type is not None:
            result['member_type'] = self.member_type
        if self.sub_group_id is not None:
            result['sub_group_id'] = self.sub_group_id
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')
        if m.get('member_role') is not None:
            self.member_role = m.get('member_role')
        if m.get('member_type') is not None:
            self.member_type = m.get('member_type')
        if m.get('sub_group_id') is not None:
            self.sub_group_id = m.get('sub_group_id')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class UpdateMembershipModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateMembershipResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateMembershipResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class AddUserToSubdomainModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class CreateUserResponse(TeaModel):
    """
    Create user response
    """
    def __init__(
        self,
        avatar: str = None,
        created_at: int = None,
        default_drive_id: str = None,
        description: str = None,
        domain_id: str = None,
        email: str = None,
        nick_name: str = None,
        phone: str = None,
        role: str = None,
        status: str = None,
        updated_at: int = None,
        user_data: dict = None,
        user_id: str = None,
        user_name: str = None,
    ):
        # 头像
        self.avatar = avatar
        # 用户创建时间
        self.created_at = created_at
        # 默认 Drive ID
        self.default_drive_id = default_drive_id
        # 用户备注信息
        self.description = description
        # Domain ID
        self.domain_id = domain_id
        # 邮箱
        self.email = email
        # 昵称
        self.nick_name = nick_name
        # 电话
        self.phone = phone
        # 角色
        self.role = role
        # 用户状态
        self.status = status
        # 用户修改时间
        self.updated_at = updated_at
        # 用户自定义数据，格式为json，可用于配置项、少量临时数据等存储，不超过1K
        self.user_data = user_data
        # 用户 ID
        self.user_id = user_id
        # 用户名称
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('avatar') is not None:
            self.avatar = m.get('avatar')
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('default_drive_id') is not None:
            self.default_drive_id = m.get('default_drive_id')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('nick_name') is not None:
            self.nick_name = m.get('nick_name')
        if m.get('phone') is not None:
            self.phone = m.get('phone')
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        if m.get('user_data') is not None:
            self.user_data = m.get('user_data')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')
        return self


class CreateUserModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateUserResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateUserResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class GetUserResponse(TeaModel):
    """
    Get user response
    """
    def __init__(
        self,
        avatar: str = None,
        created_at: int = None,
        default_drive_id: str = None,
        description: str = None,
        domain_id: str = None,
        email: str = None,
        nick_name: str = None,
        phone: str = None,
        role: str = None,
        status: str = None,
        updated_at: int = None,
        user_data: dict = None,
        user_id: str = None,
        user_name: str = None,
    ):
        # 头像
        self.avatar = avatar
        # 用户创建时间
        self.created_at = created_at
        # 默认 Drive ID
        self.default_drive_id = default_drive_id
        # 用户备注信息
        self.description = description
        # Domain ID
        self.domain_id = domain_id
        # 邮箱
        self.email = email
        # 昵称
        self.nick_name = nick_name
        # 电话
        self.phone = phone
        # 角色
        self.role = role
        # 用户状态
        self.status = status
        # 用户修改时间
        self.updated_at = updated_at
        # 用户自定义数据，格式为json，可用于配置项、少量临时数据等存储，不超过1K
        self.user_data = user_data
        # 用户 ID
        self.user_id = user_id
        # 用户名称
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('avatar') is not None:
            self.avatar = m.get('avatar')
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('default_drive_id') is not None:
            self.default_drive_id = m.get('default_drive_id')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('nick_name') is not None:
            self.nick_name = m.get('nick_name')
        if m.get('phone') is not None:
            self.phone = m.get('phone')
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        if m.get('user_data') is not None:
            self.user_data = m.get('user_data')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')
        return self


class GetUserModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetUserResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetUserResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class BaseUserResponse(TeaModel):
    """
    Base user response
    """
    def __init__(
        self,
        avatar: str = None,
        created_at: int = None,
        default_drive_id: str = None,
        description: str = None,
        domain_id: str = None,
        email: str = None,
        nick_name: str = None,
        phone: str = None,
        role: str = None,
        status: str = None,
        updated_at: int = None,
        user_data: dict = None,
        user_id: str = None,
        user_name: str = None,
    ):
        # 头像
        self.avatar = avatar
        # 用户创建时间
        self.created_at = created_at
        # 默认 Drive ID
        self.default_drive_id = default_drive_id
        # 用户备注信息
        self.description = description
        # Domain ID
        self.domain_id = domain_id
        # 邮箱
        self.email = email
        # 昵称
        self.nick_name = nick_name
        # 电话
        self.phone = phone
        # 角色
        self.role = role
        # 用户状态
        self.status = status
        # 用户修改时间
        self.updated_at = updated_at
        # 用户自定义数据，格式为json，可用于配置项、少量临时数据等存储，不超过1K
        self.user_data = user_data
        # 用户 ID
        self.user_id = user_id
        # 用户名称
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('avatar') is not None:
            self.avatar = m.get('avatar')
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('default_drive_id') is not None:
            self.default_drive_id = m.get('default_drive_id')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('nick_name') is not None:
            self.nick_name = m.get('nick_name')
        if m.get('phone') is not None:
            self.phone = m.get('phone')
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        if m.get('user_data') is not None:
            self.user_data = m.get('user_data')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')
        return self


class ListUserResponse(TeaModel):
    """
    List user response
    """
    def __init__(
        self,
        items: List[BaseUserResponse] = None,
        next_marker: str = None,
    ):
        self.items = items
        # 翻页标记
        self.next_marker = next_marker

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = BaseUserResponse()
                self.items.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        return self


class ListUsersModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListUserResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListUserResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveUserFromSubdomainModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class SearchUserModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListUserResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListUserResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserResponse(TeaModel):
    """
    Update user response
    """
    def __init__(
        self,
        avatar: str = None,
        created_at: int = None,
        default_drive_id: str = None,
        description: str = None,
        domain_id: str = None,
        email: str = None,
        nick_name: str = None,
        phone: str = None,
        role: str = None,
        status: str = None,
        updated_at: int = None,
        user_data: dict = None,
        user_id: str = None,
        user_name: str = None,
    ):
        # 头像
        self.avatar = avatar
        # 用户创建时间
        self.created_at = created_at
        # 默认 Drive ID
        self.default_drive_id = default_drive_id
        # 用户备注信息
        self.description = description
        # Domain ID
        self.domain_id = domain_id
        # 邮箱
        self.email = email
        # 昵称
        self.nick_name = nick_name
        # 电话
        self.phone = phone
        # 角色
        self.role = role
        # 用户状态
        self.status = status
        # 用户修改时间
        self.updated_at = updated_at
        # 用户自定义数据，格式为json，可用于配置项、少量临时数据等存储，不超过1K
        self.user_data = user_data
        # 用户 ID
        self.user_id = user_id
        # 用户名称
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('avatar') is not None:
            self.avatar = m.get('avatar')
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('default_drive_id') is not None:
            self.default_drive_id = m.get('default_drive_id')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('nick_name') is not None:
            self.nick_name = m.get('nick_name')
        if m.get('phone') is not None:
            self.phone = m.get('phone')
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        if m.get('user_data') is not None:
            self.user_data = m.get('user_data')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')
        return self


class UpdateUserModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateUserResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateUserResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class AddUserToSubdomainRequest(TeaModel):
    """
    Add user to subdomain request
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        subdomain_id: str = None,
        user_id: str = None,
    ):
        self.headers = headers
        # subdomain id
        self.subdomain_id = subdomain_id
        # 用户 ID
        self.user_id = user_id

    def validate(self):
        self.validate_required(self.user_id, 'user_id')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.subdomain_id is not None:
            result['subdomain_id'] = self.subdomain_id
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('subdomain_id') is not None:
            self.subdomain_id = m.get('subdomain_id')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class BaseGroupIDRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        group_id: str = None,
        subdomain_id: str = None,
    ):
        # group id
        self.group_id = group_id
        # subdomain id
        self.subdomain_id = subdomain_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.group_id is not None:
            result['group_id'] = self.group_id
        if self.subdomain_id is not None:
            result['subdomain_id'] = self.subdomain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')
        if m.get('subdomain_id') is not None:
            self.subdomain_id = m.get('subdomain_id')
        return self


class BaseGroupRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        description: str = None,
        group_name: str = None,
        is_root: bool = None,
    ):
        # 描述
        self.description = description
        # 名称
        self.group_name = group_name
        # 是否是根group
        self.is_root = is_root

    def validate(self):
        self.validate_required(self.group_name, 'group_name')

    def to_map(self):
        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.group_name is not None:
            result['group_name'] = self.group_name
        if self.is_root is not None:
            result['is_root'] = self.is_root
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('group_name') is not None:
            self.group_name = m.get('group_name')
        if m.get('is_root') is not None:
            self.is_root = m.get('is_root')
        return self


class CreateGroupRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        description: str = None,
        group_name: str = None,
        is_root: bool = None,
        subdomain_id: str = None,
    ):
        self.headers = headers
        # 描述
        self.description = description
        # 名称
        self.group_name = group_name
        # 是否是根group
        self.is_root = is_root
        # subdomain id
        self.subdomain_id = subdomain_id

    def validate(self):
        self.validate_required(self.group_name, 'group_name')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.description is not None:
            result['description'] = self.description
        if self.group_name is not None:
            result['group_name'] = self.group_name
        if self.is_root is not None:
            result['is_root'] = self.is_root
        if self.subdomain_id is not None:
            result['subdomain_id'] = self.subdomain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('group_name') is not None:
            self.group_name = m.get('group_name')
        if m.get('is_root') is not None:
            self.is_root = m.get('is_root')
        if m.get('subdomain_id') is not None:
            self.subdomain_id = m.get('subdomain_id')
        return self


class CreateMembershipRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        description: str = None,
        group_id: str = None,
        member_role: str = None,
        member_type: str = None,
        sub_group_id: str = None,
        subdomain_id: str = None,
        user_id: str = None,
    ):
        self.headers = headers
        # 描述
        self.description = description
        # group id
        self.group_id = group_id
        # 角色， member or admin
        self.member_role = member_role
        self.member_type = member_type
        self.sub_group_id = sub_group_id
        self.subdomain_id = subdomain_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.description is not None:
            result['description'] = self.description
        if self.group_id is not None:
            result['group_id'] = self.group_id
        if self.member_role is not None:
            result['member_role'] = self.member_role
        if self.member_type is not None:
            result['member_type'] = self.member_type
        if self.sub_group_id is not None:
            result['sub_group_id'] = self.sub_group_id
        if self.subdomain_id is not None:
            result['subdomain_id'] = self.subdomain_id
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')
        if m.get('member_role') is not None:
            self.member_role = m.get('member_role')
        if m.get('member_type') is not None:
            self.member_type = m.get('member_type')
        if m.get('sub_group_id') is not None:
            self.sub_group_id = m.get('sub_group_id')
        if m.get('subdomain_id') is not None:
            self.subdomain_id = m.get('subdomain_id')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class CreateUserRequest(TeaModel):
    """
    Create user request
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        avatar: str = None,
        description: str = None,
        email: str = None,
        location: str = None,
        nick_name: str = None,
        phone: str = None,
        role: str = None,
        status: str = None,
        subdomain_id: str = None,
        user_data: dict = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.headers = headers
        # 头像
        self.avatar = avatar
        # 描述信息
        self.description = description
        # 邮箱
        self.email = email
        # 用户地域
        self.location = location
        # 昵称
        self.nick_name = nick_name
        # 电话号码
        self.phone = phone
        # 角色
        self.role = role
        # 状态
        self.status = status
        # subdomain id
        self.subdomain_id = subdomain_id
        # 用户自定义数据，格式为json，可用于配置项、少量临时数据等存储，不超过1K
        self.user_data = user_data
        # 用户 ID
        self.user_id = user_id
        # 用户名称
        self.user_name = user_name

    def validate(self):
        if self.description is not None:
            self.validate_max_length(self.description, 'description', 1024)
        self.validate_required(self.user_id, 'user_id')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.avatar is not None:
            result['avatar'] = self.avatar
        if self.description is not None:
            result['description'] = self.description
        if self.email is not None:
            result['email'] = self.email
        if self.location is not None:
            result['location'] = self.location
        if self.nick_name is not None:
            result['nick_name'] = self.nick_name
        if self.phone is not None:
            result['phone'] = self.phone
        if self.role is not None:
            result['role'] = self.role
        if self.status is not None:
            result['status'] = self.status
        if self.subdomain_id is not None:
            result['subdomain_id'] = self.subdomain_id
        if self.user_data is not None:
            result['user_data'] = self.user_data
        if self.user_id is not None:
            result['user_id'] = self.user_id
        if self.user_name is not None:
            result['user_name'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('avatar') is not None:
            self.avatar = m.get('avatar')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('nick_name') is not None:
            self.nick_name = m.get('nick_name')
        if m.get('phone') is not None:
            self.phone = m.get('phone')
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('subdomain_id') is not None:
            self.subdomain_id = m.get('subdomain_id')
        if m.get('user_data') is not None:
            self.user_data = m.get('user_data')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')
        return self


class DeleteGroupRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        group_id: str = None,
        subdomain_id: str = None,
    ):
        self.headers = headers
        # group id
        self.group_id = group_id
        # subdomain id
        self.subdomain_id = subdomain_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.group_id is not None:
            result['group_id'] = self.group_id
        if self.subdomain_id is not None:
            result['subdomain_id'] = self.subdomain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')
        if m.get('subdomain_id') is not None:
            self.subdomain_id = m.get('subdomain_id')
        return self


class DeleteMembershipRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        group_id: str = None,
        member_type: str = None,
        sub_group_id: str = None,
        subdomain_id: str = None,
        user_id: str = None,
    ):
        self.headers = headers
        # group id
        self.group_id = group_id
        self.member_type = member_type
        self.sub_group_id = sub_group_id
        # subdomain id
        self.subdomain_id = subdomain_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.group_id is not None:
            result['group_id'] = self.group_id
        if self.member_type is not None:
            result['member_type'] = self.member_type
        if self.sub_group_id is not None:
            result['sub_group_id'] = self.sub_group_id
        if self.subdomain_id is not None:
            result['subdomain_id'] = self.subdomain_id
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')
        if m.get('member_type') is not None:
            self.member_type = m.get('member_type')
        if m.get('sub_group_id') is not None:
            self.sub_group_id = m.get('sub_group_id')
        if m.get('subdomain_id') is not None:
            self.subdomain_id = m.get('subdomain_id')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class DeleteUserRequest(TeaModel):
    """
    Delete user request
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        user_id: str = None,
    ):
        self.headers = headers
        # 用户 ID
        self.user_id = user_id

    def validate(self):
        self.validate_required(self.user_id, 'user_id')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
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
        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetGroupRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        group_id: str = None,
        subdomain_id: str = None,
    ):
        self.headers = headers
        # group id
        self.group_id = group_id
        # subdomain id
        self.subdomain_id = subdomain_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.group_id is not None:
            result['group_id'] = self.group_id
        if self.subdomain_id is not None:
            result['subdomain_id'] = self.subdomain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')
        if m.get('subdomain_id') is not None:
            self.subdomain_id = m.get('subdomain_id')
        return self


class GetMembershipRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        group_id: str = None,
        member_type: str = None,
        sub_group_id: str = None,
        subdomain_id: str = None,
        user_id: str = None,
    ):
        self.headers = headers
        # group id
        self.group_id = group_id
        self.member_type = member_type
        self.sub_group_id = sub_group_id
        # subdomain id
        self.subdomain_id = subdomain_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.group_id is not None:
            result['group_id'] = self.group_id
        if self.member_type is not None:
            result['member_type'] = self.member_type
        if self.sub_group_id is not None:
            result['sub_group_id'] = self.sub_group_id
        if self.subdomain_id is not None:
            result['subdomain_id'] = self.subdomain_id
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')
        if m.get('member_type') is not None:
            self.member_type = m.get('member_type')
        if m.get('sub_group_id') is not None:
            self.sub_group_id = m.get('sub_group_id')
        if m.get('subdomain_id') is not None:
            self.subdomain_id = m.get('subdomain_id')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class GetUserRequest(TeaModel):
    """
    Get user request
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        user_id: str = None,
    ):
        self.headers = headers
        # 用户 ID, 使用ak方式访问，该项必传, access_token访问如果不传，默认取自己的user信息
        # example
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class HasMemberRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        group_id: str = None,
        member_type: str = None,
        sub_group_id: str = None,
        subdomain_id: str = None,
        user_id: str = None,
    ):
        self.headers = headers
        # group id
        self.group_id = group_id
        self.member_type = member_type
        self.sub_group_id = sub_group_id
        # subdomain id
        self.subdomain_id = subdomain_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.group_id is not None:
            result['group_id'] = self.group_id
        if self.member_type is not None:
            result['member_type'] = self.member_type
        if self.sub_group_id is not None:
            result['sub_group_id'] = self.sub_group_id
        if self.subdomain_id is not None:
            result['subdomain_id'] = self.subdomain_id
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')
        if m.get('member_type') is not None:
            self.member_type = m.get('member_type')
        if m.get('sub_group_id') is not None:
            self.sub_group_id = m.get('sub_group_id')
        if m.get('subdomain_id') is not None:
            self.subdomain_id = m.get('subdomain_id')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class ListDirectChildMembershipsRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        group_id: str = None,
        limit: int = None,
        marker: str = None,
        member_type: str = None,
        subdomain_id: str = None,
    ):
        self.headers = headers
        # group id
        self.group_id = group_id
        # 分页获取的数量，默认为100
        self.limit = limit
        # 游标
        self.marker = marker
        # 角色，可选值，["", "member", "admin"], ""表示获取所有类型
        self.member_type = member_type
        # subdomain id
        self.subdomain_id = subdomain_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.group_id is not None:
            result['group_id'] = self.group_id
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        if self.member_type is not None:
            result['member_type'] = self.member_type
        if self.subdomain_id is not None:
            result['subdomain_id'] = self.subdomain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('member_type') is not None:
            self.member_type = m.get('member_type')
        if m.get('subdomain_id') is not None:
            self.subdomain_id = m.get('subdomain_id')
        return self


class ListDirectParentMembershipsRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        limit: int = None,
        marker: str = None,
        member_type: str = None,
        sub_group_id: str = None,
        subdomain_id: str = None,
        user_id: str = None,
    ):
        self.headers = headers
        # 分页获取的数量，默认为100
        self.limit = limit
        # 游标
        self.marker = marker
        self.member_type = member_type
        self.sub_group_id = sub_group_id
        # subdomain id
        self.subdomain_id = subdomain_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        if self.member_type is not None:
            result['member_type'] = self.member_type
        if self.sub_group_id is not None:
            result['sub_group_id'] = self.sub_group_id
        if self.subdomain_id is not None:
            result['subdomain_id'] = self.subdomain_id
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('member_type') is not None:
            self.member_type = m.get('member_type')
        if m.get('sub_group_id') is not None:
            self.sub_group_id = m.get('sub_group_id')
        if m.get('subdomain_id') is not None:
            self.subdomain_id = m.get('subdomain_id')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class ListGroupRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        limit: int = None,
        marker: str = None,
        subdomain_id: str = None,
    ):
        self.headers = headers
        # 分页获取的数量，默认为100
        self.limit = limit
        # 游标
        self.marker = marker
        # 列举 subdomain 下的group
        self.subdomain_id = subdomain_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        if self.subdomain_id is not None:
            result['subdomain_id'] = self.subdomain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('subdomain_id') is not None:
            self.subdomain_id = m.get('subdomain_id')
        return self


class ListUserRequest(TeaModel):
    """
    List user request
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        limit: int = None,
        marker: str = None,
        subdomain_id: str = None,
    ):
        self.headers = headers
        # 每页大小限制
        self.limit = limit
        # 翻页标记
        self.marker = marker
        # subdomain id
        self.subdomain_id = subdomain_id

    def validate(self):
        if self.limit is not None:
            self.validate_maximum(self.limit, 'limit', 100)
            self.validate_minimum(self.limit, 'limit', 1)

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        if self.subdomain_id is not None:
            result['subdomain_id'] = self.subdomain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('subdomain_id') is not None:
            self.subdomain_id = m.get('subdomain_id')
        return self


class MemberIDInfo(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        member_type: str = None,
        sub_group_id: str = None,
        user_id: str = None,
    ):
        self.member_type = member_type
        self.sub_group_id = sub_group_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.member_type is not None:
            result['member_type'] = self.member_type
        if self.sub_group_id is not None:
            result['sub_group_id'] = self.sub_group_id
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('member_type') is not None:
            self.member_type = m.get('member_type')
        if m.get('sub_group_id') is not None:
            self.sub_group_id = m.get('sub_group_id')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class RemoveUserFromSubdomainRequest(TeaModel):
    """
    Remove user to subdomain request
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        subdomain_id: str = None,
        user_id: str = None,
    ):
        self.headers = headers
        # subdomain id
        self.subdomain_id = subdomain_id
        # 用户 ID
        self.user_id = user_id

    def validate(self):
        self.validate_required(self.user_id, 'user_id')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.subdomain_id is not None:
            result['subdomain_id'] = self.subdomain_id
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('subdomain_id') is not None:
            self.subdomain_id = m.get('subdomain_id')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class SearchGroupRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        group_name: str = None,
        limit: int = None,
        marker: str = None,
        subdomain_id: str = None,
    ):
        self.headers = headers
        # group_name
        self.group_name = group_name
        # 分页获取的数量，默认为100
        self.limit = limit
        # 游标
        self.marker = marker
        # 列举 subdomain 下的group
        self.subdomain_id = subdomain_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.group_name is not None:
            result['group_name'] = self.group_name
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        if self.subdomain_id is not None:
            result['subdomain_id'] = self.subdomain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('group_name') is not None:
            self.group_name = m.get('group_name')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('subdomain_id') is not None:
            self.subdomain_id = m.get('subdomain_id')
        return self


class SearchUserRequest(TeaModel):
    """
    Search user request
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        email: str = None,
        limit: int = None,
        marker: str = None,
        nick_name: str = None,
        phone: str = None,
        role: str = None,
        status: str = None,
        subdomain_id: str = None,
        user_name: str = None,
    ):
        self.headers = headers
        # 邮箱
        self.email = email
        # 每页大小限制
        self.limit = limit
        # 翻页标记
        self.marker = marker
        # 昵称
        self.nick_name = nick_name
        # 电话号码
        self.phone = phone
        # 角色
        self.role = role
        # 状态
        self.status = status
        # subdomain id
        self.subdomain_id = subdomain_id
        # 用户名
        self.user_name = user_name

    def validate(self):
        if self.limit is not None:
            self.validate_maximum(self.limit, 'limit', 100)
            self.validate_minimum(self.limit, 'limit', 1)

    def to_map(self):
        result = dict()
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
        if self.subdomain_id is not None:
            result['subdomain_id'] = self.subdomain_id
        if self.user_name is not None:
            result['user_name'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('nick_name') is not None:
            self.nick_name = m.get('nick_name')
        if m.get('phone') is not None:
            self.phone = m.get('phone')
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('subdomain_id') is not None:
            self.subdomain_id = m.get('subdomain_id')
        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')
        return self


class UpdateGroupRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        description: str = None,
        group_id: str = None,
        group_name: str = None,
        is_root: bool = None,
        subdomain_id: str = None,
    ):
        self.headers = headers
        # 描述
        self.description = description
        # group id
        self.group_id = group_id
        # 名称
        self.group_name = group_name
        # 是否是根group
        self.is_root = is_root
        # subdomain id
        self.subdomain_id = subdomain_id

    def validate(self):
        self.validate_required(self.group_name, 'group_name')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.description is not None:
            result['description'] = self.description
        if self.group_id is not None:
            result['group_id'] = self.group_id
        if self.group_name is not None:
            result['group_name'] = self.group_name
        if self.is_root is not None:
            result['is_root'] = self.is_root
        if self.subdomain_id is not None:
            result['subdomain_id'] = self.subdomain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')
        if m.get('group_name') is not None:
            self.group_name = m.get('group_name')
        if m.get('is_root') is not None:
            self.is_root = m.get('is_root')
        if m.get('subdomain_id') is not None:
            self.subdomain_id = m.get('subdomain_id')
        return self


class UpdateMembershipRequest(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        description: str = None,
        group_id: str = None,
        member_role: str = None,
        member_type: str = None,
        sub_group_id: str = None,
        subdomain_id: str = None,
        user_id: str = None,
    ):
        self.headers = headers
        # 描述
        self.description = description
        # group id
        self.group_id = group_id
        # 角色， member or admin
        self.member_role = member_role
        self.member_type = member_type
        self.sub_group_id = sub_group_id
        # subdomain id
        self.subdomain_id = subdomain_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.description is not None:
            result['description'] = self.description
        if self.group_id is not None:
            result['group_id'] = self.group_id
        if self.member_role is not None:
            result['member_role'] = self.member_role
        if self.member_type is not None:
            result['member_type'] = self.member_type
        if self.sub_group_id is not None:
            result['sub_group_id'] = self.sub_group_id
        if self.subdomain_id is not None:
            result['subdomain_id'] = self.subdomain_id
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')
        if m.get('member_role') is not None:
            self.member_role = m.get('member_role')
        if m.get('member_type') is not None:
            self.member_type = m.get('member_type')
        if m.get('sub_group_id') is not None:
            self.sub_group_id = m.get('sub_group_id')
        if m.get('subdomain_id') is not None:
            self.subdomain_id = m.get('subdomain_id')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class UpdateUserRequest(TeaModel):
    """
    Update user request
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        avatar: str = None,
        description: str = None,
        email: str = None,
        nick_name: str = None,
        phone: str = None,
        role: str = None,
        status: str = None,
        user_data: dict = None,
        user_id: str = None,
    ):
        self.headers = headers
        # 头像
        self.avatar = avatar
        # 描述信息
        self.description = description
        # 邮箱
        self.email = email
        # 昵称
        self.nick_name = nick_name
        # 电话号码
        self.phone = phone
        # 角色
        self.role = role
        # 状态
        self.status = status
        # 用户自定义数据，格式为json，可用于配置项、少量临时数据等存储，不超过1K
        self.user_data = user_data
        # 用户 ID
        self.user_id = user_id

    def validate(self):
        if self.description is not None:
            self.validate_max_length(self.description, 'description', 1024)
        self.validate_required(self.user_id, 'user_id')

    def to_map(self):
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('avatar') is not None:
            self.avatar = m.get('avatar')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('nick_name') is not None:
            self.nick_name = m.get('nick_name')
        if m.get('phone') is not None:
            self.phone = m.get('phone')
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('user_data') is not None:
            self.user_data = m.get('user_data')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class CreateStoryResponse(TeaModel):
    """
    生成故事
    """
    def __init__(
        self,
        drive_id: str = None,
    ):
        self.drive_id = drive_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        return self


class CreateStoryModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateStoryResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateStoryResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class GetImageCountResponse(TeaModel):
    """
    获取云照片个数结果
    """
    def __init__(
        self,
        image_count: int = None,
    ):
        # image_count
        self.image_count = image_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_count is not None:
            result['image_count'] = self.image_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('image_count') is not None:
            self.image_count = m.get('image_count')
        return self


class GetPhotoCountModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetImageCountResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetImageCountResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStoryDetailResponse(TeaModel):
    """
    故事详情
    """
    def __init__(
        self,
        cover_file_id: str = None,
        created_at: str = None,
        items: List[BaseCCPFileResponse] = None,
        score: float = None,
        story_id: str = None,
        story_images_date_range: List[int] = None,
        sub_title: str = None,
        title: str = None,
        updated_at: str = None,
        video_status: str = None,
        video_url: str = None,
    ):
        # cover_file_id
        self.cover_file_id = cover_file_id
        # created_at
        self.created_at = created_at
        # items
        self.items = items
        # score
        self.score = score
        # story_id
        self.story_id = story_id
        # story_images_date_range
        self.story_images_date_range = story_images_date_range
        # sub_title
        self.sub_title = sub_title
        # title
        self.title = title
        # updated_at
        self.updated_at = updated_at
        # video_status
        self.video_status = video_status
        # video_url
        self.video_url = video_url

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cover_file_id') is not None:
            self.cover_file_id = m.get('cover_file_id')
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = BaseCCPFileResponse()
                self.items.append(temp_model.from_map(k))
        if m.get('score') is not None:
            self.score = m.get('score')
        if m.get('story_id') is not None:
            self.story_id = m.get('story_id')
        if m.get('story_images_date_range') is not None:
            self.story_images_date_range = m.get('story_images_date_range')
        if m.get('sub_title') is not None:
            self.sub_title = m.get('sub_title')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        if m.get('video_status') is not None:
            self.video_status = m.get('video_status')
        if m.get('video_url') is not None:
            self.video_url = m.get('video_url')
        return self


class GetStoryDetailModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetStoryDetailResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetStoryDetailResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class Address(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        city: str = None,
        country: str = None,
        district: str = None,
        province: str = None,
        township: str = None,
    ):
        self.city = city
        self.country = country
        self.district = district
        self.province = province
        self.township = township

    def validate(self):
        pass

    def to_map(self):
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('city') is not None:
            self.city = m.get('city')
        if m.get('country') is not None:
            self.country = m.get('country')
        if m.get('district') is not None:
            self.district = m.get('district')
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('township') is not None:
            self.township = m.get('township')
        return self


class ImageAddressResponse(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        address_detail: Address = None,
        count: int = None,
        cover_file_id: str = None,
        cover_url: str = None,
        location: str = None,
        name: str = None,
    ):
        self.address_detail = address_detail
        # 聚类地点计数
        self.count = count
        # cover_file_id
        self.cover_file_id = cover_file_id
        # 聚类地点封面图片地址
        self.cover_url = cover_url
        # 经纬度
        self.location = location
        # 聚类地点名称
        self.name = name

    def validate(self):
        if self.address_detail:
            self.address_detail.validate()

    def to_map(self):
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address_detail') is not None:
            temp_model = Address()
            self.address_detail = temp_model.from_map(m['address_detail'])
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('cover_file_id') is not None:
            self.cover_file_id = m.get('cover_file_id')
        if m.get('cover_url') is not None:
            self.cover_url = m.get('cover_url')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListImageAddressGroupsResponse(TeaModel):
    """
    展示地点分组集合
    """
    def __init__(
        self,
        items: List[ImageAddressResponse] = None,
        next_marker: str = None,
    ):
        self.items = items
        self.next_marker = next_marker

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = ImageAddressResponse()
                self.items.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        return self


class ListAddressGroupsModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListImageAddressGroupsResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListImageAddressGroupsResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class ImageFaceGroupResponse(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        created_at: str = None,
        face_count: int = None,
        group_cover_url: str = None,
        group_id: str = None,
        group_name: str = None,
        image_count: int = None,
        updated_at: str = None,
    ):
        # 人脸分组生成时间
        self.created_at = created_at
        # 人脸个数
        self.face_count = face_count
        # 人脸分组封面头像地址
        self.group_cover_url = group_cover_url
        # 人脸分组 ID
        self.group_id = group_id
        # 人脸分组名称
        self.group_name = group_name
        # 照片个数
        self.image_count = image_count
        # 人脸分组修改时间
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('face_count') is not None:
            self.face_count = m.get('face_count')
        if m.get('group_cover_url') is not None:
            self.group_cover_url = m.get('group_cover_url')
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')
        if m.get('group_name') is not None:
            self.group_name = m.get('group_name')
        if m.get('image_count') is not None:
            self.image_count = m.get('image_count')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        return self


class ListImageFaceGroupsResponse(TeaModel):
    """
    展示人脸分组集合
    """
    def __init__(
        self,
        items: List[ImageFaceGroupResponse] = None,
        next_marker: str = None,
    ):
        self.items = items
        self.next_marker = next_marker

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = ImageFaceGroupResponse()
                self.items.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        return self


class ListFacegroupsModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListImageFaceGroupsResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListImageFaceGroupsResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class StoryResponse(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        cover_file_id: str = None,
        created_at: str = None,
        score: float = None,
        story_id: str = None,
        story_images_date_range: List[int] = None,
        sub_title: str = None,
        title: str = None,
        updated_at: str = None,
        video_status: str = None,
        video_url: str = None,
    ):
        # cover_file_id
        self.cover_file_id = cover_file_id
        # created_at
        self.created_at = created_at
        # score
        self.score = score
        # story_id
        self.story_id = story_id
        # story_images_date_range
        self.story_images_date_range = story_images_date_range
        # sub_title
        self.sub_title = sub_title
        # title
        self.title = title
        # updated_at
        self.updated_at = updated_at
        # video_status
        self.video_status = video_status
        # video_url
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cover_file_id') is not None:
            self.cover_file_id = m.get('cover_file_id')
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('score') is not None:
            self.score = m.get('score')
        if m.get('story_id') is not None:
            self.story_id = m.get('story_id')
        if m.get('story_images_date_range') is not None:
            self.story_images_date_range = m.get('story_images_date_range')
        if m.get('sub_title') is not None:
            self.sub_title = m.get('sub_title')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        if m.get('video_status') is not None:
            self.video_status = m.get('video_status')
        if m.get('video_url') is not None:
            self.video_url = m.get('video_url')
        return self


class ListStoryResponse(TeaModel):
    """
    故事列表
    """
    def __init__(
        self,
        items: List[StoryResponse] = None,
        next_marker: str = None,
    ):
        # items
        self.items = items
        # next_marker
        self.next_marker = next_marker

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = StoryResponse()
                self.items.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        return self


class ListStoryModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListStoryResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListStoryResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class ImageTagResponse(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        count: int = None,
        cover_file_id: str = None,
        cover_url: str = None,
        name: str = None,
    ):
        # 聚类标签计数
        self.count = count
        # cover_file_id
        self.cover_file_id = cover_file_id
        # 聚类标签封面图片地址
        self.cover_url = cover_url
        # 聚类标签名称
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.cover_file_id is not None:
            result['cover_file_id'] = self.cover_file_id
        if self.cover_url is not None:
            result['cover_url'] = self.cover_url
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('cover_file_id') is not None:
            self.cover_file_id = m.get('cover_file_id')
        if m.get('cover_url') is not None:
            self.cover_url = m.get('cover_url')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListImageTagsResponse(TeaModel):
    """
    展示标签集合
    """
    def __init__(
        self,
        tags: List[ImageTagResponse] = None,
    ):
        self.tags = tags

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = ImageTagResponse()
                self.tags.append(temp_model.from_map(k))
        return self


class ListTagsModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListImageTagsResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListImageTagsResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class TimeRange(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        end: str = None,
        start: str = None,
    ):
        self.end = end
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end is not None:
            result['end'] = self.end
        if self.start is not None:
            result['start'] = self.start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('end') is not None:
            self.end = m.get('end')
        if m.get('start') is not None:
            self.start = m.get('start')
        return self


class ParseKeywordsResponse(TeaModel):
    """
    Parse keywords response
    """
    def __init__(
        self,
        address_line: str = None,
        tags: List[SystemTag] = None,
        time_range: TimeRange = None,
    ):
        # AddressLine
        self.address_line = address_line
        self.tags = tags
        self.time_range = time_range

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.time_range:
            self.time_range.validate()

    def to_map(self):
        result = dict()
        if self.address_line is not None:
            result['address_line'] = self.address_line
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.time_range is not None:
            result['time_range'] = self.time_range.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address_line') is not None:
            self.address_line = m.get('address_line')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = SystemTag()
                self.tags.append(temp_model.from_map(k))
        if m.get('time_range') is not None:
            temp_model = TimeRange()
            self.time_range = temp_model.from_map(m['time_range'])
        return self


class ParseKeywordsModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ParseKeywordsResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ParseKeywordsResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveStoryImagesResultItem(TeaModel):
    """
    *\
    """
    def __init__(
        self,
        code: str = None,
        file_id: str = None,
        is_succeed: bool = None,
        message: str = None,
    ):
        # code
        self.code = code
        # file_id
        self.file_id = file_id
        # is_succeed
        self.is_succeed = is_succeed
        # message
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.is_succeed is not None:
            result['is_succeed'] = self.is_succeed
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('is_succeed') is not None:
            self.is_succeed = m.get('is_succeed')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class RemoveStoryImagesResponse(TeaModel):
    """
    Remove story images response
    """
    def __init__(
        self,
        drive_id: str = None,
        file_ids: List[str] = None,
        results: List[RemoveStoryImagesResultItem] = None,
        story_id: str = None,
        success_file_ids: List[str] = None,
    ):
        # drive_id
        self.drive_id = drive_id
        # file_ids
        self.file_ids = file_ids
        self.results = results
        # story_id
        self.story_id = story_id
        # success_file_ids
        self.success_file_ids = success_file_ids

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_ids is not None:
            result['file_ids'] = self.file_ids
        result['results'] = []
        if self.results is not None:
            for k in self.results:
                result['results'].append(k.to_map() if k else None)
        if self.story_id is not None:
            result['story_id'] = self.story_id
        if self.success_file_ids is not None:
            result['success_file_ids'] = self.success_file_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_ids') is not None:
            self.file_ids = m.get('file_ids')
        self.results = []
        if m.get('results') is not None:
            for k in m.get('results'):
                temp_model = RemoveStoryImagesResultItem()
                self.results.append(temp_model.from_map(k))
        if m.get('story_id') is not None:
            self.story_id = m.get('story_id')
        if m.get('success_file_ids') is not None:
            self.success_file_ids = m.get('success_file_ids')
        return self


class RemoveStoryImagesModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveStoryImagesResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RemoveStoryImagesResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchImageAddressGroupsResponse(TeaModel):
    """
    展示地点分组列表
    """
    def __init__(
        self,
        items: List[ImageAddressResponse] = None,
    ):
        self.items = items

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = ImageAddressResponse()
                self.items.append(temp_model.from_map(k))
        return self


class SearchAddressGroupsModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SearchImageAddressGroupsResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SearchImageAddressGroupsResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFaceGroupInfoResponse(TeaModel):
    """
    更新人脸分组信息结果
    """
    def __init__(
        self,
        drive_id: str = None,
        group_id: str = None,
    ):
        # drive_id
        self.drive_id = drive_id
        # group_id
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.group_id is not None:
            result['group_id'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')
        return self


class UpdateFacegroupInfoModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateFaceGroupInfoResponse = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateFaceGroupInfoResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateStoryRequest(TeaModel):
    """
    Create story request
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        drive_id: str = None,
    ):
        self.headers = headers
        # drive_id
        self.drive_id = drive_id

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        return self


class GetImageCountRequest(TeaModel):
    """
    Get photo count request
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        drive_id: str = None,
    ):
        self.headers = headers
        # drive_id
        self.drive_id = drive_id

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        return self


class GetStoryDetailRequest(TeaModel):
    """
    Get story detail request
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        drive_id: str = None,
        story_id: str = None,
        video_url_expire_sec: int = None,
    ):
        self.headers = headers
        # drive_id
        self.drive_id = drive_id
        # story_id
        self.story_id = story_id
        # url_expire_sec
        self.video_url_expire_sec = video_url_expire_sec

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.story_id, 'story_id')
        if self.video_url_expire_sec is not None:
            self.validate_maximum(self.video_url_expire_sec, 'video_url_expire_sec', 14400)
            self.validate_minimum(self.video_url_expire_sec, 'video_url_expire_sec', 10)

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.story_id is not None:
            result['story_id'] = self.story_id
        if self.video_url_expire_sec is not None:
            result['video_url_expire_sec'] = self.video_url_expire_sec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('story_id') is not None:
            self.story_id = m.get('story_id')
        if m.get('video_url_expire_sec') is not None:
            self.video_url_expire_sec = m.get('video_url_expire_sec')
        return self


class ListImageAddressGroupsRequest(TeaModel):
    """
    List image address groups request
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        drive_id: str = None,
        image_thumbnail_process: str = None,
        limit: int = None,
        marker: str = None,
        video_thumbnail_process: str = None,
    ):
        self.headers = headers
        # Drive ID
        self.drive_id = drive_id
        # image_thumbnail_process
        self.image_thumbnail_process = image_thumbnail_process
        # 每页大小限制
        self.limit = limit
        # 翻页标记
        self.marker = marker
        # video_thumbnail_process
        self.video_thumbnail_process = video_thumbnail_process

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.limit is not None:
            self.validate_maximum(self.limit, 'limit', 100)
            self.validate_minimum(self.limit, 'limit', 1)

    def to_map(self):
        result = dict()
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
        if self.video_thumbnail_process is not None:
            result['video_thumbnail_process'] = self.video_thumbnail_process
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('image_thumbnail_process') is not None:
            self.image_thumbnail_process = m.get('image_thumbnail_process')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('video_thumbnail_process') is not None:
            self.video_thumbnail_process = m.get('video_thumbnail_process')
        return self


class ListImageFaceGroupsRequest(TeaModel):
    """
    List image face groups request
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        drive_id: str = None,
        limit: int = None,
        marker: str = None,
    ):
        self.headers = headers
        # Drive ID
        self.drive_id = drive_id
        # 每页大小限制
        self.limit = limit
        # 翻页标记
        self.marker = marker

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.limit is not None:
            self.validate_maximum(self.limit, 'limit', 100)
            self.validate_minimum(self.limit, 'limit', 1)

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        return self


class ListImageTagsRequest(TeaModel):
    """
    List image tags request
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        drive_id: str = None,
        image_thumbnail_process: str = None,
        video_thumbnail_process: str = None,
    ):
        self.headers = headers
        # Drive ID
        self.drive_id = drive_id
        # image_thumbnail_process
        self.image_thumbnail_process = image_thumbnail_process
        # video_thumbnail_process
        # type:string
        self.video_thumbnail_process = video_thumbnail_process

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.image_thumbnail_process is not None:
            result['image_thumbnail_process'] = self.image_thumbnail_process
        if self.video_thumbnail_process is not None:
            result['video_thumbnail_process'] = self.video_thumbnail_process
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('image_thumbnail_process') is not None:
            self.image_thumbnail_process = m.get('image_thumbnail_process')
        if m.get('video_thumbnail_process') is not None:
            self.video_thumbnail_process = m.get('video_thumbnail_process')
        return self


class ListStoryRequest(TeaModel):
    """
    List story request
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        drive_id: str = None,
        limit: int = None,
        marker: str = None,
    ):
        self.headers = headers
        # drive_id
        self.drive_id = drive_id
        # 每页大小限制
        self.limit = limit
        # 翻页标记
        self.marker = marker

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.limit is not None:
            self.validate_maximum(self.limit, 'limit', 100)
            self.validate_minimum(self.limit, 'limit', 1)

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        return self


class ParseKeywordsRequest(TeaModel):
    """
    Parse keywords request
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        keywords: str = None,
    ):
        self.headers = headers
        self.keywords = keywords

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.keywords is not None:
            result['keywords'] = self.keywords
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('keywords') is not None:
            self.keywords = m.get('keywords')
        return self


class RemoveStoryImagesRequest(TeaModel):
    """
    Remove story images request
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        drive_id: str = None,
        file_ids: List[str] = None,
        story_id: str = None,
    ):
        self.headers = headers
        self.drive_id = drive_id
        self.file_ids = file_ids
        self.story_id = story_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_ids is not None:
            result['file_ids'] = self.file_ids
        if self.story_id is not None:
            result['story_id'] = self.story_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_ids') is not None:
            self.file_ids = m.get('file_ids')
        if m.get('story_id') is not None:
            self.story_id = m.get('story_id')
        return self


class SearchImageAddressGroupsRequest(TeaModel):
    """
    Search image address groups request
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        address_level: str = None,
        address_names: List[str] = None,
        br_geo_point: str = None,
        drive_id: str = None,
        image_thumbnail_process: str = None,
        tl_geo_point: str = None,
        video_thumbnail_process: str = None,
    ):
        self.headers = headers
        # 查询的地点级别
        self.address_level = address_level
        # 查询的地点数组
        self.address_names = address_names
        # br_geo_point
        self.br_geo_point = br_geo_point
        # Drive ID
        self.drive_id = drive_id
        # image_thumbnail_process
        self.image_thumbnail_process = image_thumbnail_process
        # tl_geo_point
        self.tl_geo_point = tl_geo_point
        # video_thumbnail_process
        self.video_thumbnail_process = video_thumbnail_process

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')

    def to_map(self):
        result = dict()
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
        if self.video_thumbnail_process is not None:
            result['video_thumbnail_process'] = self.video_thumbnail_process
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('address_level') is not None:
            self.address_level = m.get('address_level')
        if m.get('address_names') is not None:
            self.address_names = m.get('address_names')
        if m.get('br_geo_point') is not None:
            self.br_geo_point = m.get('br_geo_point')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('image_thumbnail_process') is not None:
            self.image_thumbnail_process = m.get('image_thumbnail_process')
        if m.get('tl_geo_point') is not None:
            self.tl_geo_point = m.get('tl_geo_point')
        if m.get('video_thumbnail_process') is not None:
            self.video_thumbnail_process = m.get('video_thumbnail_process')
        return self


class UpdateFaceGroupInfoRequest(TeaModel):
    """
    Update face group info request
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        drive_id: str = None,
        group_id: str = None,
        group_name: str = None,
    ):
        self.headers = headers
        # drive_id
        self.drive_id = drive_id
        # group_id 列举人脸分组接口中获取
        self.group_id = group_id
        # group_name
        self.group_name = group_name

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id is not None:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.group_id, 'group_id')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.group_id is not None:
            result['group_id'] = self.group_id
        if self.group_name is not None:
            result['group_name'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')
        if m.get('group_name') is not None:
            self.group_name = m.get('group_name')
        return self


