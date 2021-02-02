# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import time

from Tea.exceptions import TeaException, UnretryableException
from Tea.request import TeaRequest
from Tea.core import TeaCore

from alibabacloud_pds_credentials.client import Client as AccessTokenCredentialClient
from alibabacloud_credentials.client import Client as CredentialClient
from alibabacloud_pds_hosting_sdk import models as hosting_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_pds_credentials import models as access_token_credential_models
from alibabacloud_credentials import models as credential_models
from alibabacloud_roa_util.client import Client as ROAUtilClient


class Client:
    """
    *\
    """
    _domain_id: str = None
    _access_token_credential: AccessTokenCredentialClient = None
    _endpoint: str = None
    _protocol: str = None
    _nickname: str = None
    _user_agent: str = None
    _credential: CredentialClient = None

    def __init__(
        self, 
        config: hosting_models.Config,
    ):
        if UtilClient.is_unset(config):
            raise TeaException({
                'name': 'ParameterMissing',
                'message': "'config' can not be unset"
            })
        UtilClient.validate_model(config)
        if not UtilClient.empty(config.access_token) or not UtilClient.empty(config.refresh_token):
            access_config = access_token_credential_models.Config(
                access_token=config.access_token,
                endpoint=config.endpoint,
                domain_id=config.domain_id,
                client_id=config.client_id,
                refresh_token=config.refresh_token,
                client_secret=config.client_secret,
                expire_time=config.expire_time
            )
            self._access_token_credential = AccessTokenCredentialClient(access_config)
        if not UtilClient.empty(config.access_key_id):
            if UtilClient.empty(config.type):
                config.type = 'access_key'
            credential_config = credential_models.Config(
                access_key_id=config.access_key_id,
                type=config.type,
                access_key_secret=config.access_key_secret,
                security_token=config.security_token
            )
            self._credential = CredentialClient(credential_config)
        self._endpoint = config.endpoint
        self._protocol = config.protocol
        self._user_agent = config.user_agent
        self._nickname = config.nickname
        self._domain_id = config.domain_id

    def cancel_link_ex(
        self,
        request: hosting_models.CancelLinkRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.CancelLinkModel:
        """
        取消绑定关系，生成新用户，返回访问令牌
        @tags account
        @error InvalidParameterMissing The input parameter {parameter_name} is missing.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error InternalError The request has been failed due to some unknown error.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = self.get_access_key_id()
                access_key_secret = self.get_access_key_secret()
                security_token = self.get_security_token()
                access_token = self.get_access_token()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/account/cancel_link')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.auth.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = UtilClient.read_as_json(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.CancelLinkModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = UtilClient.read_as_json(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def cancel_link_ex_async(
        self,
        request: hosting_models.CancelLinkRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.CancelLinkModel:
        """
        取消绑定关系，生成新用户，返回访问令牌
        @tags account
        @error InvalidParameterMissing The input parameter {parameter_name} is missing.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error InternalError The request has been failed due to some unknown error.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = await self.get_access_key_id_async()
                access_key_secret = await self.get_access_key_secret_async()
                security_token = await self.get_security_token_async()
                access_token = await self.get_access_token_async()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/account/cancel_link')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.auth.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = await UtilClient.read_as_json_async(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.CancelLinkModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = await UtilClient.read_as_json_async(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def confirm_link_ex(
        self,
        request: hosting_models.ConfirmLinkRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.ConfirmLinkModel:
        """
        确认绑定关系, 成功后返回访问令牌
        @tags account
        @error InvalidParameterMissing The input parameter {parameter_name} is missing.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = self.get_access_key_id()
                access_key_secret = self.get_access_key_secret()
                security_token = self.get_security_token()
                access_token = self.get_access_token()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/account/confirm_link')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.auth.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = UtilClient.read_as_json(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.ConfirmLinkModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = UtilClient.read_as_json(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def confirm_link_ex_async(
        self,
        request: hosting_models.ConfirmLinkRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.ConfirmLinkModel:
        """
        确认绑定关系, 成功后返回访问令牌
        @tags account
        @error InvalidParameterMissing The input parameter {parameter_name} is missing.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = await self.get_access_key_id_async()
                access_key_secret = await self.get_access_key_secret_async()
                security_token = await self.get_security_token_async()
                access_token = await self.get_access_token_async()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/account/confirm_link')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.auth.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = await UtilClient.read_as_json_async(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.ConfirmLinkModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = await UtilClient.read_as_json_async(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def change_password_ex(
        self,
        request: hosting_models.DefaultChangePasswordRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.ChangePasswordModel:
        """
        修改手机登录密码，密码必须包含数字和字母，长度8-20个字符
        @tags account
        @error InvalidParameterMissing The input parameter {parameter_name} is missing.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = self.get_access_key_id()
                access_key_secret = self.get_access_key_secret()
                security_token = self.get_security_token()
                access_token = self.get_access_token()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/account/default/change_password')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.auth.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = UtilClient.read_as_json(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.ChangePasswordModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = UtilClient.read_as_json(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def change_password_ex_async(
        self,
        request: hosting_models.DefaultChangePasswordRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.ChangePasswordModel:
        """
        修改手机登录密码，密码必须包含数字和字母，长度8-20个字符
        @tags account
        @error InvalidParameterMissing The input parameter {parameter_name} is missing.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = await self.get_access_key_id_async()
                access_key_secret = await self.get_access_key_secret_async()
                security_token = await self.get_security_token_async()
                access_token = await self.get_access_token_async()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/account/default/change_password')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.auth.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = await UtilClient.read_as_json_async(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.ChangePasswordModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = await UtilClient.read_as_json_async(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def set_password_ex(
        self,
        request: hosting_models.DefaultSetPasswordRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.SetPasswordModel:
        """
        设置手机登录密码，密码必须包含数字和字母，长度8-20个字符
        @tags account
        @error InvalidParameterMissing The input parameter {parameter_name} is missing.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = self.get_access_key_id()
                access_key_secret = self.get_access_key_secret()
                security_token = self.get_security_token()
                access_token = self.get_access_token()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/account/default/set_password')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.auth.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 204):
                    return hosting_models.SetPasswordModel().from_map(
                        {
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = UtilClient.read_as_json(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def set_password_ex_async(
        self,
        request: hosting_models.DefaultSetPasswordRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.SetPasswordModel:
        """
        设置手机登录密码，密码必须包含数字和字母，长度8-20个字符
        @tags account
        @error InvalidParameterMissing The input parameter {parameter_name} is missing.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = await self.get_access_key_id_async()
                access_key_secret = await self.get_access_key_secret_async()
                security_token = await self.get_security_token_async()
                access_token = await self.get_access_token_async()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/account/default/set_password')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.auth.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 204):
                    return hosting_models.SetPasswordModel().from_map(
                        {
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = await UtilClient.read_as_json_async(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def verify_code_ex(
        self,
        request: hosting_models.VerifyCodeRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.VerifyCodeModel:
        """
        校验手机短信验证码，用于重置密码时校验手机，通过校验后返回state，可通过state重新设置密码
        @tags account
        @error InvalidParameterMissing The input parameter {parameter_name} is missing.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = self.get_access_key_id()
                access_key_secret = self.get_access_key_secret()
                security_token = self.get_security_token()
                access_token = self.get_access_token()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/account/default/verify_code')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.auth.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = UtilClient.read_as_json(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.VerifyCodeModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = UtilClient.read_as_json(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def verify_code_ex_async(
        self,
        request: hosting_models.VerifyCodeRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.VerifyCodeModel:
        """
        校验手机短信验证码，用于重置密码时校验手机，通过校验后返回state，可通过state重新设置密码
        @tags account
        @error InvalidParameterMissing The input parameter {parameter_name} is missing.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = await self.get_access_key_id_async()
                access_key_secret = await self.get_access_key_secret_async()
                security_token = await self.get_security_token_async()
                access_token = await self.get_access_token_async()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/account/default/verify_code')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.auth.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = await UtilClient.read_as_json_async(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.VerifyCodeModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = await UtilClient.read_as_json_async(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def get_access_token_by_link_info_ex(
        self,
        request: hosting_models.GetAccessTokenByLinkInfoRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.GetAccessTokenByLinkInfoModel:
        """
        管理员通过账号信息直接获取用户的访问令牌
        @tags account
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = self.get_access_key_id()
                access_key_secret = self.get_access_key_secret()
                security_token = self.get_security_token()
                access_token = self.get_access_token()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/account/get_access_token_by_link_info')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.auth.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = UtilClient.read_as_json(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.GetAccessTokenByLinkInfoModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = UtilClient.read_as_json(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def get_access_token_by_link_info_ex_async(
        self,
        request: hosting_models.GetAccessTokenByLinkInfoRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.GetAccessTokenByLinkInfoModel:
        """
        管理员通过账号信息直接获取用户的访问令牌
        @tags account
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = await self.get_access_key_id_async()
                access_key_secret = await self.get_access_key_secret_async()
                security_token = await self.get_security_token_async()
                access_token = await self.get_access_token_async()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/account/get_access_token_by_link_info')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.auth.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = await UtilClient.read_as_json_async(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.GetAccessTokenByLinkInfoModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = await UtilClient.read_as_json_async(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def get_captcha_ex(
        self,
        request: hosting_models.GetCaptchaRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.GetCaptchaModel:
        """
        获取图片验证码，用于人机校验，默认不需要
        @tags account
        @error InvalidParameterMissing The input parameter {parameter_name} is missing.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = self.get_access_key_id()
                access_key_secret = self.get_access_key_secret()
                security_token = self.get_security_token()
                access_token = self.get_access_token()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/account/get_captcha')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.auth.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = UtilClient.read_as_json(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.GetCaptchaModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = UtilClient.read_as_json(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def get_captcha_ex_async(
        self,
        request: hosting_models.GetCaptchaRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.GetCaptchaModel:
        """
        获取图片验证码，用于人机校验，默认不需要
        @tags account
        @error InvalidParameterMissing The input parameter {parameter_name} is missing.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = await self.get_access_key_id_async()
                access_key_secret = await self.get_access_key_secret_async()
                security_token = await self.get_security_token_async()
                access_token = await self.get_access_token_async()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/account/get_captcha')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.auth.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = await UtilClient.read_as_json_async(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.GetCaptchaModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = await UtilClient.read_as_json_async(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def get_link_info_ex(
        self,
        request: hosting_models.GetByLinkInfoRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.GetLinkInfoModel:
        """
        获取用户认证方式详情
        @tags account
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = self.get_access_key_id()
                access_key_secret = self.get_access_key_secret()
                security_token = self.get_security_token()
                access_token = self.get_access_token()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/account/get_link_info')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.auth.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = UtilClient.read_as_json(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.GetLinkInfoModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = UtilClient.read_as_json(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def get_link_info_ex_async(
        self,
        request: hosting_models.GetByLinkInfoRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.GetLinkInfoModel:
        """
        获取用户认证方式详情
        @tags account
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = await self.get_access_key_id_async()
                access_key_secret = await self.get_access_key_secret_async()
                security_token = await self.get_security_token_async()
                access_token = await self.get_access_token_async()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/account/get_link_info')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.auth.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = await UtilClient.read_as_json_async(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.GetLinkInfoModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = await UtilClient.read_as_json_async(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def get_link_info_by_user_id_ex(
        self,
        request: hosting_models.GetLinkInfoByUserIDRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.GetLinkInfoByUserIdModel:
        """
        获取用户的所有绑定信息
        @tags account
        @error InvalidParameterMissing The input parameter {parameter_name} is missing.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error InternalError The request has been failed due to some unknown error.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = self.get_access_key_id()
                access_key_secret = self.get_access_key_secret()
                security_token = self.get_security_token()
                access_token = self.get_access_token()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/account/get_link_info_by_user_id')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.auth.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = UtilClient.read_as_json(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.GetLinkInfoByUserIdModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = UtilClient.read_as_json(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def get_link_info_by_user_id_ex_async(
        self,
        request: hosting_models.GetLinkInfoByUserIDRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.GetLinkInfoByUserIdModel:
        """
        获取用户的所有绑定信息
        @tags account
        @error InvalidParameterMissing The input parameter {parameter_name} is missing.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error InternalError The request has been failed due to some unknown error.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = await self.get_access_key_id_async()
                access_key_secret = await self.get_access_key_secret_async()
                security_token = await self.get_security_token_async()
                access_token = await self.get_access_token_async()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/account/get_link_info_by_user_id')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.auth.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = await UtilClient.read_as_json_async(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.GetLinkInfoByUserIdModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = await UtilClient.read_as_json_async(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def get_public_key_ex(
        self,
        request: hosting_models.GetPublicKeyRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.GetPublicKeyModel:
        """
        获取公钥，用于加密对称密钥
        @tags account
        @error InvalidParameterMissing The input parameter {parameter_name} is missing.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = self.get_access_key_id()
                access_key_secret = self.get_access_key_secret()
                security_token = self.get_security_token()
                access_token = self.get_access_token()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/account/get_public_key')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.auth.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = UtilClient.read_as_json(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.GetPublicKeyModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = UtilClient.read_as_json(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def get_public_key_ex_async(
        self,
        request: hosting_models.GetPublicKeyRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.GetPublicKeyModel:
        """
        获取公钥，用于加密对称密钥
        @tags account
        @error InvalidParameterMissing The input parameter {parameter_name} is missing.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = await self.get_access_key_id_async()
                access_key_secret = await self.get_access_key_secret_async()
                security_token = await self.get_security_token_async()
                access_token = await self.get_access_token_async()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/account/get_public_key')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.auth.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = await UtilClient.read_as_json_async(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.GetPublicKeyModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = await UtilClient.read_as_json_async(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def link_ex(
        self,
        request: hosting_models.AccountLinkRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.LinkModel:
        """
        绑定用户认证方式
        @tags account
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error AlreadyExist {resource} has already exists. {extra_msg}
        @error InternalError The request has been failed due to some unknown error.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = self.get_access_key_id()
                access_key_secret = self.get_access_key_secret()
                security_token = self.get_security_token()
                access_token = self.get_access_token()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/account/link')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.auth.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = UtilClient.read_as_json(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.LinkModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = UtilClient.read_as_json(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def link_ex_async(
        self,
        request: hosting_models.AccountLinkRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.LinkModel:
        """
        绑定用户认证方式
        @tags account
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error AlreadyExist {resource} has already exists. {extra_msg}
        @error InternalError The request has been failed due to some unknown error.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = await self.get_access_key_id_async()
                access_key_secret = await self.get_access_key_secret_async()
                security_token = await self.get_security_token_async()
                access_token = await self.get_access_token_async()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/account/link')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.auth.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = await UtilClient.read_as_json_async(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.LinkModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = await UtilClient.read_as_json_async(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def check_exist_ex(
        self,
        request: hosting_models.MobileCheckExistRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.CheckExistModel:
        """
        查询手机号是否已被注册
        @tags account
        @error InvalidParameterMissing The input parameter {parameter_name} is missing.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = self.get_access_key_id()
                access_key_secret = self.get_access_key_secret()
                security_token = self.get_security_token()
                access_token = self.get_access_token()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/account/mobile/check_exist')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.auth.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = UtilClient.read_as_json(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.CheckExistModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = UtilClient.read_as_json(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def check_exist_ex_async(
        self,
        request: hosting_models.MobileCheckExistRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.CheckExistModel:
        """
        查询手机号是否已被注册
        @tags account
        @error InvalidParameterMissing The input parameter {parameter_name} is missing.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = await self.get_access_key_id_async()
                access_key_secret = await self.get_access_key_secret_async()
                security_token = await self.get_security_token_async()
                access_token = await self.get_access_token_async()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/account/mobile/check_exist')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.auth.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = await UtilClient.read_as_json_async(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.CheckExistModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = await UtilClient.read_as_json_async(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def login_ex(
        self,
        request: hosting_models.MobileLoginRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.LoginModel:
        """
        通过手机号+短信或密码登录，返回刷新令牌和访问令牌
        @tags account
        @error InvalidParameterMissing The input parameter {parameter_name} is missing.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = self.get_access_key_id()
                access_key_secret = self.get_access_key_secret()
                security_token = self.get_security_token()
                access_token = self.get_access_token()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/account/mobile/login')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.auth.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = UtilClient.read_as_json(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.LoginModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = UtilClient.read_as_json(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def login_ex_async(
        self,
        request: hosting_models.MobileLoginRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.LoginModel:
        """
        通过手机号+短信或密码登录，返回刷新令牌和访问令牌
        @tags account
        @error InvalidParameterMissing The input parameter {parameter_name} is missing.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = await self.get_access_key_id_async()
                access_key_secret = await self.get_access_key_secret_async()
                security_token = await self.get_security_token_async()
                access_token = await self.get_access_token_async()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/account/mobile/login')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.auth.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = await UtilClient.read_as_json_async(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.LoginModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = await UtilClient.read_as_json_async(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def register_ex(
        self,
        request: hosting_models.MobileRegisterRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.RegisterModel:
        """
        通过手机号+短信验证码注册账号
        @tags account
        @error InvalidParameterMissing The input parameter {parameter_name} is missing.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error AlreadyExist {resource} has already exists. {extra_msg}
        @error InternalError The request has been failed due to some unknown error.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = self.get_access_key_id()
                access_key_secret = self.get_access_key_secret()
                security_token = self.get_security_token()
                access_token = self.get_access_token()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/account/mobile/register')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.auth.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = UtilClient.read_as_json(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.RegisterModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = UtilClient.read_as_json(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def register_ex_async(
        self,
        request: hosting_models.MobileRegisterRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.RegisterModel:
        """
        通过手机号+短信验证码注册账号
        @tags account
        @error InvalidParameterMissing The input parameter {parameter_name} is missing.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error AlreadyExist {resource} has already exists. {extra_msg}
        @error InternalError The request has been failed due to some unknown error.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = await self.get_access_key_id_async()
                access_key_secret = await self.get_access_key_secret_async()
                security_token = await self.get_security_token_async()
                access_token = await self.get_access_token_async()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/account/mobile/register')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.auth.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = await UtilClient.read_as_json_async(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.RegisterModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = await UtilClient.read_as_json_async(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def mobile_send_sms_code_ex(
        self,
        request: hosting_models.MobileSendSmsCodeRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.MobileSendSmsCodeModel:
        """
        发送短信验证码，用于登录、注册、修改密码、绑定等
        @tags account
        @error InvalidParameterMissing The input parameter {parameter_name} is missing.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = self.get_access_key_id()
                access_key_secret = self.get_access_key_secret()
                security_token = self.get_security_token()
                access_token = self.get_access_token()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/account/mobile/send_sms_code')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.auth.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = UtilClient.read_as_json(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.MobileSendSmsCodeModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = UtilClient.read_as_json(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def mobile_send_sms_code_ex_async(
        self,
        request: hosting_models.MobileSendSmsCodeRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.MobileSendSmsCodeModel:
        """
        发送短信验证码，用于登录、注册、修改密码、绑定等
        @tags account
        @error InvalidParameterMissing The input parameter {parameter_name} is missing.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = await self.get_access_key_id_async()
                access_key_secret = await self.get_access_key_secret_async()
                security_token = await self.get_security_token_async()
                access_token = await self.get_access_token_async()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/account/mobile/send_sms_code')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.auth.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = await UtilClient.read_as_json_async(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.MobileSendSmsCodeModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = await UtilClient.read_as_json_async(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def account_revoke_ex(
        self,
        request: hosting_models.RevokeRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.AccountRevokeModel:
        """
        用户退出登录
        @tags account
        @error InvalidParameterMissing The input parameter {parameter_name} is missing.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = self.get_access_key_id()
                access_key_secret = self.get_access_key_secret()
                security_token = self.get_security_token()
                access_token = self.get_access_token()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/account/revoke')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.auth.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 204):
                    return hosting_models.AccountRevokeModel().from_map(
                        {
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = UtilClient.read_as_json(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def account_revoke_ex_async(
        self,
        request: hosting_models.RevokeRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.AccountRevokeModel:
        """
        用户退出登录
        @tags account
        @error InvalidParameterMissing The input parameter {parameter_name} is missing.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = await self.get_access_key_id_async()
                access_key_secret = await self.get_access_key_secret_async()
                security_token = await self.get_security_token_async()
                access_token = await self.get_access_token_async()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/account/revoke')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.auth.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 204):
                    return hosting_models.AccountRevokeModel().from_map(
                        {
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = await UtilClient.read_as_json_async(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def account_token_ex(
        self,
        request: hosting_models.AccountTokenRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.AccountTokenModel:
        """
        用户通过刷新令牌（refresh_token）获取访问令牌（access_token）
        @tags account
        @error InvalidParameterMissing The input parameter {parameter_name} is missing.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = self.get_access_key_id()
                access_key_secret = self.get_access_key_secret()
                security_token = self.get_security_token()
                access_token = self.get_access_token()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/account/token')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.auth.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = UtilClient.read_as_json(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.AccountTokenModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = UtilClient.read_as_json(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def account_token_ex_async(
        self,
        request: hosting_models.AccountTokenRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.AccountTokenModel:
        """
        用户通过刷新令牌（refresh_token）获取访问令牌（access_token）
        @tags account
        @error InvalidParameterMissing The input parameter {parameter_name} is missing.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = await self.get_access_key_id_async()
                access_key_secret = await self.get_access_key_secret_async()
                security_token = await self.get_security_token_async()
                access_token = await self.get_access_token_async()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/account/token')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.auth.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = await UtilClient.read_as_json_async(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.AccountTokenModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = await UtilClient.read_as_json_async(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def admin_list_stores_ex(
        self,
        request: hosting_models.AdminListStoresRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.AdminListStoresModel:
        """
        列举Store列表
        @tags admin
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error InternalError The request has been failed due to some unknown error.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = self.get_access_key_id()
                access_key_secret = self.get_access_key_secret()
                security_token = self.get_security_token()
                access_token = self.get_access_token()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/domain/list_stores')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = UtilClient.read_as_json(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.AdminListStoresModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = UtilClient.read_as_json(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def admin_list_stores_ex_async(
        self,
        request: hosting_models.AdminListStoresRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.AdminListStoresModel:
        """
        列举Store列表
        @tags admin
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error InternalError The request has been failed due to some unknown error.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = await self.get_access_key_id_async()
                access_key_secret = await self.get_access_key_secret_async()
                security_token = await self.get_security_token_async()
                access_token = await self.get_access_token_async()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/domain/list_stores')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = await UtilClient.read_as_json_async(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.AdminListStoresModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = await UtilClient.read_as_json_async(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def get_user_access_token_ex(
        self,
        request: hosting_models.GetUserAccessTokenRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.GetUserAccessTokenModel:
        """
        获取用户的accessToken
        @tags admin
        @error undefined undefined
        @error undefined undefined
        @error undefined undefined
        @error undefined undefined
        @error undefined undefined
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = self.get_access_key_id()
                access_key_secret = self.get_access_key_secret()
                security_token = self.get_security_token()
                access_token = self.get_access_token()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/user/get_access_token')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = UtilClient.read_as_json(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.GetUserAccessTokenModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = UtilClient.read_as_json(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def get_user_access_token_ex_async(
        self,
        request: hosting_models.GetUserAccessTokenRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.GetUserAccessTokenModel:
        """
        获取用户的accessToken
        @tags admin
        @error undefined undefined
        @error undefined undefined
        @error undefined undefined
        @error undefined undefined
        @error undefined undefined
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = await self.get_access_key_id_async()
                access_key_secret = await self.get_access_key_secret_async()
                security_token = await self.get_security_token_async()
                access_token = await self.get_access_token_async()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/user/get_access_token')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = await UtilClient.read_as_json_async(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.GetUserAccessTokenModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = await UtilClient.read_as_json_async(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def create_drive_ex(
        self,
        request: hosting_models.CreateDriveRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.CreateDriveModel:
        """
        支持normal和large两种drive，
        large类型的drive用于文件数多的场景，不支持list操作，
        当drive的文件数量大于1亿时，建议使用large类型。
        @tags drive
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = self.get_access_key_id()
                access_key_secret = self.get_access_key_secret()
                security_token = self.get_security_token()
                access_token = self.get_access_token()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/drive/create')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 201):
                    obj = UtilClient.read_as_json(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.CreateDriveModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = UtilClient.read_as_json(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def create_drive_ex_async(
        self,
        request: hosting_models.CreateDriveRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.CreateDriveModel:
        """
        支持normal和large两种drive，
        large类型的drive用于文件数多的场景，不支持list操作，
        当drive的文件数量大于1亿时，建议使用large类型。
        @tags drive
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = await self.get_access_key_id_async()
                access_key_secret = await self.get_access_key_secret_async()
                security_token = await self.get_security_token_async()
                access_token = await self.get_access_token_async()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/drive/create')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 201):
                    obj = await UtilClient.read_as_json_async(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.CreateDriveModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = await UtilClient.read_as_json_async(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def delete_drive_ex(
        self,
        request: hosting_models.DeleteDriveRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.DeleteDriveModel:
        """
        删除指定drive_id对应的Drive
        @tags drive
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = self.get_access_key_id()
                access_key_secret = self.get_access_key_secret()
                security_token = self.get_security_token()
                access_token = self.get_access_token()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/drive/delete')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 204):
                    return hosting_models.DeleteDriveModel().from_map(
                        {
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = UtilClient.read_as_json(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def delete_drive_ex_async(
        self,
        request: hosting_models.DeleteDriveRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.DeleteDriveModel:
        """
        删除指定drive_id对应的Drive
        @tags drive
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = await self.get_access_key_id_async()
                access_key_secret = await self.get_access_key_secret_async()
                security_token = await self.get_security_token_async()
                access_token = await self.get_access_token_async()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/drive/delete')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 204):
                    return hosting_models.DeleteDriveModel().from_map(
                        {
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = await UtilClient.read_as_json_async(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def get_drive_ex(
        self,
        request: hosting_models.GetDriveRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.GetDriveModel:
        """
        获取指定drive_id对应的Drive详细信息。
        @tags drive
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = self.get_access_key_id()
                access_key_secret = self.get_access_key_secret()
                security_token = self.get_security_token()
                access_token = self.get_access_token()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/drive/get')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = UtilClient.read_as_json(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.GetDriveModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = UtilClient.read_as_json(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def get_drive_ex_async(
        self,
        request: hosting_models.GetDriveRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.GetDriveModel:
        """
        获取指定drive_id对应的Drive详细信息。
        @tags drive
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = await self.get_access_key_id_async()
                access_key_secret = await self.get_access_key_secret_async()
                security_token = await self.get_security_token_async()
                access_token = await self.get_access_token_async()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/drive/get')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = await UtilClient.read_as_json_async(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.GetDriveModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = await UtilClient.read_as_json_async(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def get_default_drive_ex(
        self,
        request: hosting_models.GetDefaultDriveRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.GetDefaultDriveModel:
        """
        一个用户可拥有多个drive，在创建drive时通过参数指定是否为这个用户的默认drive，
        每个用户只能设置一个默认drive。
        @tags drive
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = self.get_access_key_id()
                access_key_secret = self.get_access_key_secret()
                security_token = self.get_security_token()
                access_token = self.get_access_token()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/drive/get_default_drive')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = UtilClient.read_as_json(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.GetDefaultDriveModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = UtilClient.read_as_json(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def get_default_drive_ex_async(
        self,
        request: hosting_models.GetDefaultDriveRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.GetDefaultDriveModel:
        """
        一个用户可拥有多个drive，在创建drive时通过参数指定是否为这个用户的默认drive，
        每个用户只能设置一个默认drive。
        @tags drive
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = await self.get_access_key_id_async()
                access_key_secret = await self.get_access_key_secret_async()
                security_token = await self.get_security_token_async()
                access_token = await self.get_access_token_async()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/drive/get_default_drive')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = await UtilClient.read_as_json_async(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.GetDefaultDriveModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = await UtilClient.read_as_json_async(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def list_drives_ex(
        self,
        request: hosting_models.ListDriveRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.ListDrivesModel:
        """
        管理员列举指定用户的Drive
        @tags drive
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = self.get_access_key_id()
                access_key_secret = self.get_access_key_secret()
                security_token = self.get_security_token()
                access_token = self.get_access_token()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/drive/list')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = UtilClient.read_as_json(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.ListDrivesModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = UtilClient.read_as_json(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def list_drives_ex_async(
        self,
        request: hosting_models.ListDriveRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.ListDrivesModel:
        """
        管理员列举指定用户的Drive
        @tags drive
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = await self.get_access_key_id_async()
                access_key_secret = await self.get_access_key_secret_async()
                security_token = await self.get_security_token_async()
                access_token = await self.get_access_token_async()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/drive/list')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = await UtilClient.read_as_json_async(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.ListDrivesModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = await UtilClient.read_as_json_async(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def list_my_drives_ex(
        self,
        request: hosting_models.ListMyDriveRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.ListMyDrivesModel:
        """
        列举当前用户（访问令牌）的Drive
        @tags drive
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = self.get_access_key_id()
                access_key_secret = self.get_access_key_secret()
                security_token = self.get_security_token()
                access_token = self.get_access_token()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/drive/list_my_drives')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = UtilClient.read_as_json(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.ListMyDrivesModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = UtilClient.read_as_json(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def list_my_drives_ex_async(
        self,
        request: hosting_models.ListMyDriveRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.ListMyDrivesModel:
        """
        列举当前用户（访问令牌）的Drive
        @tags drive
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = await self.get_access_key_id_async()
                access_key_secret = await self.get_access_key_secret_async()
                security_token = await self.get_security_token_async()
                access_token = await self.get_access_token_async()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/drive/list_my_drives')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = await UtilClient.read_as_json_async(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.ListMyDrivesModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = await UtilClient.read_as_json_async(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def update_drive_ex(
        self,
        request: hosting_models.UpdateDriveRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.UpdateDriveModel:
        """
        更新指定drive_id的Drive信息
        @tags drive
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = self.get_access_key_id()
                access_key_secret = self.get_access_key_secret()
                security_token = self.get_security_token()
                access_token = self.get_access_token()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/drive/update')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = UtilClient.read_as_json(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.UpdateDriveModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = UtilClient.read_as_json(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def update_drive_ex_async(
        self,
        request: hosting_models.UpdateDriveRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.UpdateDriveModel:
        """
        更新指定drive_id的Drive信息
        @tags drive
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = await self.get_access_key_id_async()
                access_key_secret = await self.get_access_key_secret_async()
                security_token = await self.get_security_token_async()
                access_token = await self.get_access_token_async()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/drive/update')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = await UtilClient.read_as_json_async(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.UpdateDriveModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = await UtilClient.read_as_json_async(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def complete_file_ex(
        self,
        request: hosting_models.HostingCompleteFileRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.CompleteFileModel:
        """
        完成文件上传
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = self.get_access_key_id()
                access_key_secret = self.get_access_key_secret()
                security_token = self.get_security_token()
                access_token = self.get_access_token()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/hosting/file/complete')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = UtilClient.read_as_json(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.CompleteFileModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = UtilClient.read_as_json(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def complete_file_ex_async(
        self,
        request: hosting_models.HostingCompleteFileRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.CompleteFileModel:
        """
        完成文件上传
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = await self.get_access_key_id_async()
                access_key_secret = await self.get_access_key_secret_async()
                security_token = await self.get_security_token_async()
                access_token = await self.get_access_token_async()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/hosting/file/complete')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = await UtilClient.read_as_json_async(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.CompleteFileModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = await UtilClient.read_as_json_async(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def copy_file_ex(
        self,
        request: hosting_models.HostingCopyFileRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.CopyFileModel:
        """
        指定源文件或文件夹路径，拷贝到指定的文件夹。
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = self.get_access_key_id()
                access_key_secret = self.get_access_key_secret()
                security_token = self.get_security_token()
                access_token = self.get_access_token()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/hosting/file/copy')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 201):
                    obj = UtilClient.read_as_json(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.CopyFileModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = UtilClient.read_as_json(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def copy_file_ex_async(
        self,
        request: hosting_models.HostingCopyFileRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.CopyFileModel:
        """
        指定源文件或文件夹路径，拷贝到指定的文件夹。
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = await self.get_access_key_id_async()
                access_key_secret = await self.get_access_key_secret_async()
                security_token = await self.get_security_token_async()
                access_token = await self.get_access_token_async()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/hosting/file/copy')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 201):
                    obj = await UtilClient.read_as_json_async(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.CopyFileModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = await UtilClient.read_as_json_async(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def create_file_ex(
        self,
        request: hosting_models.HostingCreateFileRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.CreateFileModel:
        """
        创建文件或者文件夹。
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error AlreadyExist {resource} has already exists. {extra_msg}
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = self.get_access_key_id()
                access_key_secret = self.get_access_key_secret()
                security_token = self.get_security_token()
                access_token = self.get_access_token()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/hosting/file/create')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 201):
                    obj = UtilClient.read_as_json(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.CreateFileModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = UtilClient.read_as_json(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def create_file_ex_async(
        self,
        request: hosting_models.HostingCreateFileRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.CreateFileModel:
        """
        创建文件或者文件夹。
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error AlreadyExist {resource} has already exists. {extra_msg}
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = await self.get_access_key_id_async()
                access_key_secret = await self.get_access_key_secret_async()
                security_token = await self.get_security_token_async()
                access_token = await self.get_access_token_async()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/hosting/file/create')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 201):
                    obj = await UtilClient.read_as_json_async(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.CreateFileModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = await UtilClient.read_as_json_async(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def delete_file_ex(
        self,
        request: hosting_models.HostingDeleteFileRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.DeleteFileModel:
        """
        指定文件或文件夹路径，删除文件或文件夹
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = self.get_access_key_id()
                access_key_secret = self.get_access_key_secret()
                security_token = self.get_security_token()
                access_token = self.get_access_token()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/hosting/file/delete')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 204):
                    return hosting_models.DeleteFileModel().from_map(
                        {
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = UtilClient.read_as_json(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def delete_file_ex_async(
        self,
        request: hosting_models.HostingDeleteFileRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.DeleteFileModel:
        """
        指定文件或文件夹路径，删除文件或文件夹
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = await self.get_access_key_id_async()
                access_key_secret = await self.get_access_key_secret_async()
                security_token = await self.get_security_token_async()
                access_token = await self.get_access_token_async()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/hosting/file/delete')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 204):
                    return hosting_models.DeleteFileModel().from_map(
                        {
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = await UtilClient.read_as_json_async(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def get_file_ex(
        self,
        request: hosting_models.HostingGetFileRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.GetFileModel:
        """
        获取指定文件或文件夹路径，获取文件或文件夹信息。
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = self.get_access_key_id()
                access_key_secret = self.get_access_key_secret()
                security_token = self.get_security_token()
                access_token = self.get_access_token()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/hosting/file/get')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = UtilClient.read_as_json(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.GetFileModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = UtilClient.read_as_json(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def get_file_ex_async(
        self,
        request: hosting_models.HostingGetFileRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.GetFileModel:
        """
        获取指定文件或文件夹路径，获取文件或文件夹信息。
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = await self.get_access_key_id_async()
                access_key_secret = await self.get_access_key_secret_async()
                security_token = await self.get_security_token_async()
                access_token = await self.get_access_token_async()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/hosting/file/get')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = await UtilClient.read_as_json_async(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.GetFileModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = await UtilClient.read_as_json_async(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def get_download_url_ex(
        self,
        request: hosting_models.HostingGetDownloadUrlRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.GetDownloadUrlModel:
        """
        指定文件路径，获取文件下载地址
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = self.get_access_key_id()
                access_key_secret = self.get_access_key_secret()
                security_token = self.get_security_token()
                access_token = self.get_access_token()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/hosting/file/get_download_url')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = UtilClient.read_as_json(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.GetDownloadUrlModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = UtilClient.read_as_json(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def get_download_url_ex_async(
        self,
        request: hosting_models.HostingGetDownloadUrlRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.GetDownloadUrlModel:
        """
        指定文件路径，获取文件下载地址
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = await self.get_access_key_id_async()
                access_key_secret = await self.get_access_key_secret_async()
                security_token = await self.get_security_token_async()
                access_token = await self.get_access_token_async()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/hosting/file/get_download_url')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = await UtilClient.read_as_json_async(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.GetDownloadUrlModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = await UtilClient.read_as_json_async(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def get_secure_url_ex(
        self,
        request: hosting_models.HostingGetSecureUrlRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.GetSecureUrlModel:
        """
        指定文件路径，获取文件安全地址
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = self.get_access_key_id()
                access_key_secret = self.get_access_key_secret()
                security_token = self.get_security_token()
                access_token = self.get_access_token()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/hosting/file/get_secure_url')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = UtilClient.read_as_json(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.GetSecureUrlModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = UtilClient.read_as_json(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def get_secure_url_ex_async(
        self,
        request: hosting_models.HostingGetSecureUrlRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.GetSecureUrlModel:
        """
        指定文件路径，获取文件安全地址
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = await self.get_access_key_id_async()
                access_key_secret = await self.get_access_key_secret_async()
                security_token = await self.get_security_token_async()
                access_token = await self.get_access_token_async()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/hosting/file/get_secure_url')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = await UtilClient.read_as_json_async(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.GetSecureUrlModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = await UtilClient.read_as_json_async(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def get_upload_url_ex(
        self,
        request: hosting_models.HostingGetUploadUrlRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.GetUploadUrlModel:
        """
        可指定分片信息，一次获取多个分片的上传地址。
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = self.get_access_key_id()
                access_key_secret = self.get_access_key_secret()
                security_token = self.get_security_token()
                access_token = self.get_access_token()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/hosting/file/get_upload_url')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = UtilClient.read_as_json(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.GetUploadUrlModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = UtilClient.read_as_json(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def get_upload_url_ex_async(
        self,
        request: hosting_models.HostingGetUploadUrlRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.GetUploadUrlModel:
        """
        可指定分片信息，一次获取多个分片的上传地址。
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = await self.get_access_key_id_async()
                access_key_secret = await self.get_access_key_secret_async()
                security_token = await self.get_security_token_async()
                access_token = await self.get_access_token_async()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/hosting/file/get_upload_url')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = await UtilClient.read_as_json_async(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.GetUploadUrlModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = await UtilClient.read_as_json_async(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def list_file_ex(
        self,
        request: hosting_models.HostingListFileRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.ListFileModel:
        """
        指定父文件夹路径，列举文件夹下的文件或者文件夹
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = self.get_access_key_id()
                access_key_secret = self.get_access_key_secret()
                security_token = self.get_security_token()
                access_token = self.get_access_token()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/hosting/file/list')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = UtilClient.read_as_json(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.ListFileModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = UtilClient.read_as_json(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def list_file_ex_async(
        self,
        request: hosting_models.HostingListFileRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.ListFileModel:
        """
        指定父文件夹路径，列举文件夹下的文件或者文件夹
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = await self.get_access_key_id_async()
                access_key_secret = await self.get_access_key_secret_async()
                security_token = await self.get_security_token_async()
                access_token = await self.get_access_token_async()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/hosting/file/list')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = await UtilClient.read_as_json_async(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.ListFileModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = await UtilClient.read_as_json_async(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def list_uploaded_parts_ex(
        self,
        request: hosting_models.HostingListUploadedPartRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.ListUploadedPartsModel:
        """
        列举UploadID对应的已上传分片。
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = self.get_access_key_id()
                access_key_secret = self.get_access_key_secret()
                security_token = self.get_security_token()
                access_token = self.get_access_token()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/hosting/file/list_uploaded_parts')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = UtilClient.read_as_json(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.ListUploadedPartsModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = UtilClient.read_as_json(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def list_uploaded_parts_ex_async(
        self,
        request: hosting_models.HostingListUploadedPartRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.ListUploadedPartsModel:
        """
        列举UploadID对应的已上传分片。
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = await self.get_access_key_id_async()
                access_key_secret = await self.get_access_key_secret_async()
                security_token = await self.get_security_token_async()
                access_token = await self.get_access_token_async()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/hosting/file/list_uploaded_parts')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = await UtilClient.read_as_json_async(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.ListUploadedPartsModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = await UtilClient.read_as_json_async(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def move_file_ex(
        self,
        request: hosting_models.HostingMoveFileRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.MoveFileModel:
        """
        指定源文件或文件夹路径，移动到指定的文件夹。
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = self.get_access_key_id()
                access_key_secret = self.get_access_key_secret()
                security_token = self.get_security_token()
                access_token = self.get_access_token()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/hosting/file/move')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = UtilClient.read_as_json(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.MoveFileModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = UtilClient.read_as_json(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def move_file_ex_async(
        self,
        request: hosting_models.HostingMoveFileRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.MoveFileModel:
        """
        指定源文件或文件夹路径，移动到指定的文件夹。
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = await self.get_access_key_id_async()
                access_key_secret = await self.get_access_key_secret_async()
                security_token = await self.get_security_token_async()
                access_token = await self.get_access_token_async()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/hosting/file/move')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = await UtilClient.read_as_json_async(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.MoveFileModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = await UtilClient.read_as_json_async(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def video_definition_ex(
        self,
        request: hosting_models.HostingVideoDefinitionRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.VideoDefinitionModel:
        """
        获取视频支持的分辨率
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = self.get_access_key_id()
                access_key_secret = self.get_access_key_secret()
                security_token = self.get_security_token()
                access_token = self.get_access_token()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/hosting/file/video_definition')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = UtilClient.read_as_json(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.VideoDefinitionModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = UtilClient.read_as_json(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def video_definition_ex_async(
        self,
        request: hosting_models.HostingVideoDefinitionRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.VideoDefinitionModel:
        """
        获取视频支持的分辨率
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = await self.get_access_key_id_async()
                access_key_secret = await self.get_access_key_secret_async()
                security_token = await self.get_security_token_async()
                access_token = await self.get_access_token_async()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/hosting/file/video_definition')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = await UtilClient.read_as_json_async(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.VideoDefinitionModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = await UtilClient.read_as_json_async(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def video_license_ex(
        self,
        request: hosting_models.HostingVideoDRMLicenseRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.VideoLicenseModel:
        """
        获取视频的DRM License
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = self.get_access_key_id()
                access_key_secret = self.get_access_key_secret()
                security_token = self.get_security_token()
                access_token = self.get_access_token()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/hosting/file/video_license')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = UtilClient.read_as_json(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.VideoLicenseModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = UtilClient.read_as_json(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def video_license_ex_async(
        self,
        request: hosting_models.HostingVideoDRMLicenseRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.VideoLicenseModel:
        """
        获取视频的DRM License
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = await self.get_access_key_id_async()
                access_key_secret = await self.get_access_key_secret_async()
                security_token = await self.get_security_token_async()
                access_token = await self.get_access_token_async()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/hosting/file/video_license')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = await UtilClient.read_as_json_async(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.VideoLicenseModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = await UtilClient.read_as_json_async(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def video_m3u_8ex(
        self,
        request: hosting_models.HostingVideoM3U8Request,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.VideoM3u8Model:
        """
        获取视频转码后的m3u8文件
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = self.get_access_key_id()
                access_key_secret = self.get_access_key_secret()
                security_token = self.get_security_token()
                access_token = self.get_access_token()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/hosting/file/video_m3u8')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    byt = UtilClient.read_as_bytes(_response.body)
                    return hosting_models.VideoM3u8Model().from_map(
                        {
                            'body': byt,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = UtilClient.read_as_json(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def video_m3u_8ex_async(
        self,
        request: hosting_models.HostingVideoM3U8Request,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.VideoM3u8Model:
        """
        获取视频转码后的m3u8文件
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = await self.get_access_key_id_async()
                access_key_secret = await self.get_access_key_secret_async()
                security_token = await self.get_security_token_async()
                access_token = await self.get_access_token_async()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/hosting/file/video_m3u8')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    byt = await UtilClient.read_as_bytes_async(_response.body)
                    return hosting_models.VideoM3u8Model().from_map(
                        {
                            'body': byt,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = await UtilClient.read_as_json_async(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def video_transcode_ex(
        self,
        request: hosting_models.HostingVideoTranscodeRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.VideoTranscodeModel:
        """
        将mp4格式的视频文件，转为m3u8
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = self.get_access_key_id()
                access_key_secret = self.get_access_key_secret()
                security_token = self.get_security_token()
                access_token = self.get_access_token()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/hosting/file/video_transcode')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = UtilClient.read_as_json(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.VideoTranscodeModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if UtilClient.equal_number(_response.status_code, 204):
                    return hosting_models.VideoTranscodeModel().from_map(
                        {
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = UtilClient.read_as_json(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def video_transcode_ex_async(
        self,
        request: hosting_models.HostingVideoTranscodeRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.VideoTranscodeModel:
        """
        将mp4格式的视频文件，转为m3u8
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = await self.get_access_key_id_async()
                access_key_secret = await self.get_access_key_secret_async()
                security_token = await self.get_security_token_async()
                access_token = await self.get_access_token_async()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/hosting/file/video_transcode')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = await UtilClient.read_as_json_async(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.VideoTranscodeModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if UtilClient.equal_number(_response.status_code, 204):
                    return hosting_models.VideoTranscodeModel().from_map(
                        {
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = await UtilClient.read_as_json_async(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def create_share_ex(
        self,
        request: hosting_models.CreateShareRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.CreateShareModel:
        """
        创建共享。
        @tags share
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = self.get_access_key_id()
                access_key_secret = self.get_access_key_secret()
                security_token = self.get_security_token()
                access_token = self.get_access_token()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/hosting/share/create')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 201):
                    obj = UtilClient.read_as_json(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.CreateShareModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = UtilClient.read_as_json(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def create_share_ex_async(
        self,
        request: hosting_models.CreateShareRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.CreateShareModel:
        """
        创建共享。
        @tags share
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = await self.get_access_key_id_async()
                access_key_secret = await self.get_access_key_secret_async()
                security_token = await self.get_security_token_async()
                access_token = await self.get_access_token_async()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/hosting/share/create')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 201):
                    obj = await UtilClient.read_as_json_async(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.CreateShareModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = await UtilClient.read_as_json_async(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def delete_share_ex(
        self,
        request: hosting_models.DeleteShareRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.DeleteShareModel:
        """
        删除指定共享
        @tags share
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = self.get_access_key_id()
                access_key_secret = self.get_access_key_secret()
                security_token = self.get_security_token()
                access_token = self.get_access_token()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/hosting/share/delete')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 204):
                    return hosting_models.DeleteShareModel().from_map(
                        {
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = UtilClient.read_as_json(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def delete_share_ex_async(
        self,
        request: hosting_models.DeleteShareRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.DeleteShareModel:
        """
        删除指定共享
        @tags share
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = await self.get_access_key_id_async()
                access_key_secret = await self.get_access_key_secret_async()
                security_token = await self.get_security_token_async()
                access_token = await self.get_access_token_async()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/hosting/share/delete')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 204):
                    return hosting_models.DeleteShareModel().from_map(
                        {
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = await UtilClient.read_as_json_async(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def get_share_ex(
        self,
        request: hosting_models.GetShareRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.GetShareModel:
        """
        获取共享信息。
        @tags share
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = self.get_access_key_id()
                access_key_secret = self.get_access_key_secret()
                security_token = self.get_security_token()
                access_token = self.get_access_token()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/hosting/share/get')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = UtilClient.read_as_json(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.GetShareModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = UtilClient.read_as_json(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def get_share_ex_async(
        self,
        request: hosting_models.GetShareRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.GetShareModel:
        """
        获取共享信息。
        @tags share
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = await self.get_access_key_id_async()
                access_key_secret = await self.get_access_key_secret_async()
                security_token = await self.get_security_token_async()
                access_token = await self.get_access_token_async()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/hosting/share/get')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = await UtilClient.read_as_json_async(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.GetShareModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = await UtilClient.read_as_json_async(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def list_share_ex(
        self,
        request: hosting_models.ListShareRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.ListShareModel:
        """
        列举指定用户的共享
        @tags share
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = self.get_access_key_id()
                access_key_secret = self.get_access_key_secret()
                security_token = self.get_security_token()
                access_token = self.get_access_token()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/hosting/share/list')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = UtilClient.read_as_json(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.ListShareModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = UtilClient.read_as_json(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def list_share_ex_async(
        self,
        request: hosting_models.ListShareRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.ListShareModel:
        """
        列举指定用户的共享
        @tags share
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = await self.get_access_key_id_async()
                access_key_secret = await self.get_access_key_secret_async()
                security_token = await self.get_security_token_async()
                access_token = await self.get_access_token_async()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/hosting/share/list')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = await UtilClient.read_as_json_async(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.ListShareModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = await UtilClient.read_as_json_async(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def update_share_ex(
        self,
        request: hosting_models.UpdateShareRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.UpdateShareModel:
        """
        修改指定共享
        @tags share
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = self.get_access_key_id()
                access_key_secret = self.get_access_key_secret()
                security_token = self.get_security_token()
                access_token = self.get_access_token()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/hosting/share/update')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = UtilClient.read_as_json(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.UpdateShareModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = UtilClient.read_as_json(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def update_share_ex_async(
        self,
        request: hosting_models.UpdateShareRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.UpdateShareModel:
        """
        修改指定共享
        @tags share
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = await self.get_access_key_id_async()
                access_key_secret = await self.get_access_key_secret_async()
                security_token = await self.get_security_token_async()
                access_token = await self.get_access_token_async()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/hosting/share/update')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = await UtilClient.read_as_json_async(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.UpdateShareModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = await UtilClient.read_as_json_async(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def list_storefile_ex(
        self,
        request: hosting_models.ListStoreFileRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.ListStorefileModel:
        """
        列举指定store下的所有文件。
        @tags store
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = self.get_access_key_id()
                access_key_secret = self.get_access_key_secret()
                security_token = self.get_security_token()
                access_token = self.get_access_token()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/hosting/store_file/list')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = UtilClient.read_as_json(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.ListStorefileModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = UtilClient.read_as_json(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def list_storefile_ex_async(
        self,
        request: hosting_models.ListStoreFileRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.ListStorefileModel:
        """
        列举指定store下的所有文件。
        @tags store
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = await self.get_access_key_id_async()
                access_key_secret = await self.get_access_key_secret_async()
                security_token = await self.get_security_token_async()
                access_token = await self.get_access_token_async()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/hosting/store_file/list')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = await UtilClient.read_as_json_async(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.ListStorefileModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = await UtilClient.read_as_json_async(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def create_user_ex(
        self,
        request: hosting_models.CreateUserRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.CreateUserModel:
        """
        创建用户，只有管理员可以调用
        @tags user
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = self.get_access_key_id()
                access_key_secret = self.get_access_key_secret()
                security_token = self.get_security_token()
                access_token = self.get_access_token()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/user/create')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 201):
                    obj = UtilClient.read_as_json(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.CreateUserModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = UtilClient.read_as_json(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def create_user_ex_async(
        self,
        request: hosting_models.CreateUserRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.CreateUserModel:
        """
        创建用户，只有管理员可以调用
        @tags user
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = await self.get_access_key_id_async()
                access_key_secret = await self.get_access_key_secret_async()
                security_token = await self.get_security_token_async()
                access_token = await self.get_access_token_async()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/user/create')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 201):
                    obj = await UtilClient.read_as_json_async(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.CreateUserModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = await UtilClient.read_as_json_async(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def delete_user_ex(
        self,
        request: hosting_models.DeleteUserRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.DeleteUserModel:
        """
        只有管理员可以调用
        @tags user
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = self.get_access_key_id()
                access_key_secret = self.get_access_key_secret()
                security_token = self.get_security_token()
                access_token = self.get_access_token()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/user/delete')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 204):
                    return hosting_models.DeleteUserModel().from_map(
                        {
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = UtilClient.read_as_json(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def delete_user_ex_async(
        self,
        request: hosting_models.DeleteUserRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.DeleteUserModel:
        """
        只有管理员可以调用
        @tags user
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = await self.get_access_key_id_async()
                access_key_secret = await self.get_access_key_secret_async()
                security_token = await self.get_security_token_async()
                access_token = await self.get_access_token_async()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/user/delete')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 204):
                    return hosting_models.DeleteUserModel().from_map(
                        {
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = await UtilClient.read_as_json_async(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def get_user_ex(
        self,
        request: hosting_models.GetUserRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.GetUserModel:
        """
        获取用户详细信息，普通用户只能获取自己的信息，管理员可以获取任意用户的信息。
        @tags user
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = self.get_access_key_id()
                access_key_secret = self.get_access_key_secret()
                security_token = self.get_security_token()
                access_token = self.get_access_token()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/user/get')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = UtilClient.read_as_json(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.GetUserModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = UtilClient.read_as_json(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def get_user_ex_async(
        self,
        request: hosting_models.GetUserRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.GetUserModel:
        """
        获取用户详细信息，普通用户只能获取自己的信息，管理员可以获取任意用户的信息。
        @tags user
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = await self.get_access_key_id_async()
                access_key_secret = await self.get_access_key_secret_async()
                security_token = await self.get_security_token_async()
                access_token = await self.get_access_token_async()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/user/get')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = await UtilClient.read_as_json_async(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.GetUserModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = await UtilClient.read_as_json_async(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def list_users_ex(
        self,
        request: hosting_models.ListUserRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.ListUsersModel:
        """
        只有管理员可以调用
        @tags user
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = self.get_access_key_id()
                access_key_secret = self.get_access_key_secret()
                security_token = self.get_security_token()
                access_token = self.get_access_token()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/user/list')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = UtilClient.read_as_json(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.ListUsersModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = UtilClient.read_as_json(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def list_users_ex_async(
        self,
        request: hosting_models.ListUserRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.ListUsersModel:
        """
        只有管理员可以调用
        @tags user
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = await self.get_access_key_id_async()
                access_key_secret = await self.get_access_key_secret_async()
                security_token = await self.get_security_token_async()
                access_token = await self.get_access_token_async()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/user/list')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = await UtilClient.read_as_json_async(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.ListUsersModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = await UtilClient.read_as_json_async(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def search_user_ex(
        self,
        request: hosting_models.SearchUserRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.SearchUserModel:
        """
        该接口将会根据条件查询用户，只有管理员可以调用
        @tags user
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = self.get_access_key_id()
                access_key_secret = self.get_access_key_secret()
                security_token = self.get_security_token()
                access_token = self.get_access_token()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/user/search')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = UtilClient.read_as_json(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.SearchUserModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = UtilClient.read_as_json(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def search_user_ex_async(
        self,
        request: hosting_models.SearchUserRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.SearchUserModel:
        """
        该接口将会根据条件查询用户，只有管理员可以调用
        @tags user
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = await self.get_access_key_id_async()
                access_key_secret = await self.get_access_key_secret_async()
                security_token = await self.get_security_token_async()
                access_token = await self.get_access_token_async()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/user/search')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = await UtilClient.read_as_json_async(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.SearchUserModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = await UtilClient.read_as_json_async(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def update_user_ex(
        self,
        request: hosting_models.UpdateUserRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.UpdateUserModel:
        """
        用户可以修改自己的description，nick_name，avatar；
        管理员在用户基础上还可修改status（可以修改任意用户）；
        超级管理员在管理员基础上还可修改role（可以修改任意用户）。
        @tags user
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = self.get_access_key_id()
                access_key_secret = self.get_access_key_secret()
                security_token = self.get_security_token()
                access_token = self.get_access_token()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/user/update')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = UtilClient.read_as_json(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.UpdateUserModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = UtilClient.read_as_json(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def update_user_ex_async(
        self,
        request: hosting_models.UpdateUserRequest,
        runtime: hosting_models.RuntimeOptions,
    ) -> hosting_models.UpdateUserModel:
        """
        用户可以修改自己的description，nick_name，avatar；
        管理员在用户基础上还可修改status（可以修改任意用户）；
        超级管理员在管理员基础上还可修改role（可以修改任意用户）。
        @tags user
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'localAddr': runtime.local_addr,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'socks5Proxy': runtime.socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                accesskey_id = await self.get_access_key_id_async()
                access_key_secret = await self.get_access_key_secret_async()
                security_token = await self.get_security_token_async()
                access_token = await self.get_access_token_async()
                real_req = UtilClient.to_map(request)
                _request.protocol = UtilClient.default_string(self._protocol, 'https')
                _request.method = 'POST'
                _request.pathname = self.get_pathname(self._nickname, f'/v2/user/update')
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._domain_id}.api.aliyunpds.com'),
                    'content-type': 'application/json; charset=utf-8'
                }, request.headers)
                real_req['headers'] = None
                if not UtilClient.empty(access_token):
                    _request.headers['authorization'] = f'Bearer {access_token}'
                elif not UtilClient.empty(accesskey_id) and not UtilClient.empty(access_key_secret):
                    if not UtilClient.empty(security_token):
                        _request.headers['x-acs-security-token'] = security_token
                    _request.headers['date'] = UtilClient.get_date_utcstring()
                    _request.headers['accept'] = 'application/json'
                    _request.headers['x-acs-signature-method'] = 'HMAC-SHA1'
                    _request.headers['x-acs-signature-version'] = '1.0'
                    string_to_sign = ROAUtilClient.get_string_to_sign(_request)
                    _request.headers['authorization'] = f'acs {accesskey_id}:{ROAUtilClient.get_signature(string_to_sign, access_key_secret)}'
                _request.body = UtilClient.to_jsonstring(real_req)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                resp_map = None
                obj = None
                if UtilClient.equal_number(_response.status_code, 200):
                    obj = await UtilClient.read_as_json_async(_response.body)
                    resp_map = UtilClient.assert_as_map(obj)
                    return hosting_models.UpdateUserModel().from_map(
                        {
                            'body': resp_map,
                            'headers': _response.headers
                        }
                    )
                if not UtilClient.empty(_response.headers.get('x-ca-error-message')):
                    raise TeaException({
                        'data': {
                            'requestId': _response.headers.get('x-ca-request-id'),
                            'statusCode': _response.status_code,
                            'statusMessage': _response.status_message
                        },
                        'message': _response.headers.get('x-ca-error-message')
                    })
                obj = await UtilClient.read_as_json_async(_response.body)
                resp_map = UtilClient.assert_as_map(obj)
                raise TeaException(TeaCore.merge({
                    'data': {
                        'requestId': _response.headers.get('x-ca-request-id'),
                        'statusCode': _response.status_code,
                        'statusMessage': _response.status_message
                    }
                }, resp_map))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def cancel_link(
        self,
        request: hosting_models.CancelLinkRequest,
    ) -> hosting_models.CancelLinkModel:
        """
        取消绑定关系，生成新用户，返回访问令牌
        @tags account
        @error InvalidParameterMissing The input parameter {parameter_name} is missing.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error InternalError The request has been failed due to some unknown error.
        """
        runtime = hosting_models.RuntimeOptions()
        return self.cancel_link_ex(request, runtime)

    async def cancel_link_async(
        self,
        request: hosting_models.CancelLinkRequest,
    ) -> hosting_models.CancelLinkModel:
        """
        取消绑定关系，生成新用户，返回访问令牌
        @tags account
        @error InvalidParameterMissing The input parameter {parameter_name} is missing.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error InternalError The request has been failed due to some unknown error.
        """
        runtime = hosting_models.RuntimeOptions()
        return await self.cancel_link_ex_async(request, runtime)

    def confirm_link(
        self,
        request: hosting_models.ConfirmLinkRequest,
    ) -> hosting_models.ConfirmLinkModel:
        """
        确认绑定关系, 成功后返回访问令牌
        @tags account
        @error InvalidParameterMissing The input parameter {parameter_name} is missing.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        """
        runtime = hosting_models.RuntimeOptions()
        return self.confirm_link_ex(request, runtime)

    async def confirm_link_async(
        self,
        request: hosting_models.ConfirmLinkRequest,
    ) -> hosting_models.ConfirmLinkModel:
        """
        确认绑定关系, 成功后返回访问令牌
        @tags account
        @error InvalidParameterMissing The input parameter {parameter_name} is missing.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        """
        runtime = hosting_models.RuntimeOptions()
        return await self.confirm_link_ex_async(request, runtime)

    def change_password(
        self,
        request: hosting_models.DefaultChangePasswordRequest,
    ) -> hosting_models.ChangePasswordModel:
        """
        修改手机登录密码，密码必须包含数字和字母，长度8-20个字符
        @tags account
        @error InvalidParameterMissing The input parameter {parameter_name} is missing.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        """
        runtime = hosting_models.RuntimeOptions()
        return self.change_password_ex(request, runtime)

    async def change_password_async(
        self,
        request: hosting_models.DefaultChangePasswordRequest,
    ) -> hosting_models.ChangePasswordModel:
        """
        修改手机登录密码，密码必须包含数字和字母，长度8-20个字符
        @tags account
        @error InvalidParameterMissing The input parameter {parameter_name} is missing.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        """
        runtime = hosting_models.RuntimeOptions()
        return await self.change_password_ex_async(request, runtime)

    def set_password(
        self,
        request: hosting_models.DefaultSetPasswordRequest,
    ) -> hosting_models.SetPasswordModel:
        """
        设置手机登录密码，密码必须包含数字和字母，长度8-20个字符
        @tags account
        @error InvalidParameterMissing The input parameter {parameter_name} is missing.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        """
        runtime = hosting_models.RuntimeOptions()
        return self.set_password_ex(request, runtime)

    async def set_password_async(
        self,
        request: hosting_models.DefaultSetPasswordRequest,
    ) -> hosting_models.SetPasswordModel:
        """
        设置手机登录密码，密码必须包含数字和字母，长度8-20个字符
        @tags account
        @error InvalidParameterMissing The input parameter {parameter_name} is missing.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        """
        runtime = hosting_models.RuntimeOptions()
        return await self.set_password_ex_async(request, runtime)

    def verify_code(
        self,
        request: hosting_models.VerifyCodeRequest,
    ) -> hosting_models.VerifyCodeModel:
        """
        校验手机短信验证码，用于重置密码时校验手机，通过校验后返回state，可通过state重新设置密码
        @tags account
        @error InvalidParameterMissing The input parameter {parameter_name} is missing.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        """
        runtime = hosting_models.RuntimeOptions()
        return self.verify_code_ex(request, runtime)

    async def verify_code_async(
        self,
        request: hosting_models.VerifyCodeRequest,
    ) -> hosting_models.VerifyCodeModel:
        """
        校验手机短信验证码，用于重置密码时校验手机，通过校验后返回state，可通过state重新设置密码
        @tags account
        @error InvalidParameterMissing The input parameter {parameter_name} is missing.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        """
        runtime = hosting_models.RuntimeOptions()
        return await self.verify_code_ex_async(request, runtime)

    def get_access_token_by_link_info(
        self,
        request: hosting_models.GetAccessTokenByLinkInfoRequest,
    ) -> hosting_models.GetAccessTokenByLinkInfoModel:
        """
        管理员通过账号信息直接获取用户的访问令牌
        @tags account
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        """
        runtime = hosting_models.RuntimeOptions()
        return self.get_access_token_by_link_info_ex(request, runtime)

    async def get_access_token_by_link_info_async(
        self,
        request: hosting_models.GetAccessTokenByLinkInfoRequest,
    ) -> hosting_models.GetAccessTokenByLinkInfoModel:
        """
        管理员通过账号信息直接获取用户的访问令牌
        @tags account
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        """
        runtime = hosting_models.RuntimeOptions()
        return await self.get_access_token_by_link_info_ex_async(request, runtime)

    def get_captcha(
        self,
        request: hosting_models.GetCaptchaRequest,
    ) -> hosting_models.GetCaptchaModel:
        """
        获取图片验证码，用于人机校验，默认不需要
        @tags account
        @error InvalidParameterMissing The input parameter {parameter_name} is missing.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        """
        runtime = hosting_models.RuntimeOptions()
        return self.get_captcha_ex(request, runtime)

    async def get_captcha_async(
        self,
        request: hosting_models.GetCaptchaRequest,
    ) -> hosting_models.GetCaptchaModel:
        """
        获取图片验证码，用于人机校验，默认不需要
        @tags account
        @error InvalidParameterMissing The input parameter {parameter_name} is missing.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        """
        runtime = hosting_models.RuntimeOptions()
        return await self.get_captcha_ex_async(request, runtime)

    def get_link_info(
        self,
        request: hosting_models.GetByLinkInfoRequest,
    ) -> hosting_models.GetLinkInfoModel:
        """
        获取用户认证方式详情
        @tags account
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        """
        runtime = hosting_models.RuntimeOptions()
        return self.get_link_info_ex(request, runtime)

    async def get_link_info_async(
        self,
        request: hosting_models.GetByLinkInfoRequest,
    ) -> hosting_models.GetLinkInfoModel:
        """
        获取用户认证方式详情
        @tags account
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        """
        runtime = hosting_models.RuntimeOptions()
        return await self.get_link_info_ex_async(request, runtime)

    def get_link_info_by_user_id(
        self,
        request: hosting_models.GetLinkInfoByUserIDRequest,
    ) -> hosting_models.GetLinkInfoByUserIdModel:
        """
        获取用户的所有绑定信息
        @tags account
        @error InvalidParameterMissing The input parameter {parameter_name} is missing.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error InternalError The request has been failed due to some unknown error.
        """
        runtime = hosting_models.RuntimeOptions()
        return self.get_link_info_by_user_id_ex(request, runtime)

    async def get_link_info_by_user_id_async(
        self,
        request: hosting_models.GetLinkInfoByUserIDRequest,
    ) -> hosting_models.GetLinkInfoByUserIdModel:
        """
        获取用户的所有绑定信息
        @tags account
        @error InvalidParameterMissing The input parameter {parameter_name} is missing.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error InternalError The request has been failed due to some unknown error.
        """
        runtime = hosting_models.RuntimeOptions()
        return await self.get_link_info_by_user_id_ex_async(request, runtime)

    def get_public_key(
        self,
        request: hosting_models.GetPublicKeyRequest,
    ) -> hosting_models.GetPublicKeyModel:
        """
        获取公钥，用于加密对称密钥
        @tags account
        @error InvalidParameterMissing The input parameter {parameter_name} is missing.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        """
        runtime = hosting_models.RuntimeOptions()
        return self.get_public_key_ex(request, runtime)

    async def get_public_key_async(
        self,
        request: hosting_models.GetPublicKeyRequest,
    ) -> hosting_models.GetPublicKeyModel:
        """
        获取公钥，用于加密对称密钥
        @tags account
        @error InvalidParameterMissing The input parameter {parameter_name} is missing.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        """
        runtime = hosting_models.RuntimeOptions()
        return await self.get_public_key_ex_async(request, runtime)

    def link(
        self,
        request: hosting_models.AccountLinkRequest,
    ) -> hosting_models.LinkModel:
        """
        绑定用户认证方式
        @tags account
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error AlreadyExist {resource} has already exists. {extra_msg}
        @error InternalError The request has been failed due to some unknown error.
        """
        runtime = hosting_models.RuntimeOptions()
        return self.link_ex(request, runtime)

    async def link_async(
        self,
        request: hosting_models.AccountLinkRequest,
    ) -> hosting_models.LinkModel:
        """
        绑定用户认证方式
        @tags account
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error AlreadyExist {resource} has already exists. {extra_msg}
        @error InternalError The request has been failed due to some unknown error.
        """
        runtime = hosting_models.RuntimeOptions()
        return await self.link_ex_async(request, runtime)

    def check_exist(
        self,
        request: hosting_models.MobileCheckExistRequest,
    ) -> hosting_models.CheckExistModel:
        """
        查询手机号是否已被注册
        @tags account
        @error InvalidParameterMissing The input parameter {parameter_name} is missing.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        """
        runtime = hosting_models.RuntimeOptions()
        return self.check_exist_ex(request, runtime)

    async def check_exist_async(
        self,
        request: hosting_models.MobileCheckExistRequest,
    ) -> hosting_models.CheckExistModel:
        """
        查询手机号是否已被注册
        @tags account
        @error InvalidParameterMissing The input parameter {parameter_name} is missing.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        """
        runtime = hosting_models.RuntimeOptions()
        return await self.check_exist_ex_async(request, runtime)

    def login(
        self,
        request: hosting_models.MobileLoginRequest,
    ) -> hosting_models.LoginModel:
        """
        通过手机号+短信或密码登录，返回刷新令牌和访问令牌
        @tags account
        @error InvalidParameterMissing The input parameter {parameter_name} is missing.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        """
        runtime = hosting_models.RuntimeOptions()
        return self.login_ex(request, runtime)

    async def login_async(
        self,
        request: hosting_models.MobileLoginRequest,
    ) -> hosting_models.LoginModel:
        """
        通过手机号+短信或密码登录，返回刷新令牌和访问令牌
        @tags account
        @error InvalidParameterMissing The input parameter {parameter_name} is missing.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        """
        runtime = hosting_models.RuntimeOptions()
        return await self.login_ex_async(request, runtime)

    def register(
        self,
        request: hosting_models.MobileRegisterRequest,
    ) -> hosting_models.RegisterModel:
        """
        通过手机号+短信验证码注册账号
        @tags account
        @error InvalidParameterMissing The input parameter {parameter_name} is missing.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error AlreadyExist {resource} has already exists. {extra_msg}
        @error InternalError The request has been failed due to some unknown error.
        """
        runtime = hosting_models.RuntimeOptions()
        return self.register_ex(request, runtime)

    async def register_async(
        self,
        request: hosting_models.MobileRegisterRequest,
    ) -> hosting_models.RegisterModel:
        """
        通过手机号+短信验证码注册账号
        @tags account
        @error InvalidParameterMissing The input parameter {parameter_name} is missing.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error AlreadyExist {resource} has already exists. {extra_msg}
        @error InternalError The request has been failed due to some unknown error.
        """
        runtime = hosting_models.RuntimeOptions()
        return await self.register_ex_async(request, runtime)

    def mobile_send_sms_code(
        self,
        request: hosting_models.MobileSendSmsCodeRequest,
    ) -> hosting_models.MobileSendSmsCodeModel:
        """
        发送短信验证码，用于登录、注册、修改密码、绑定等
        @tags account
        @error InvalidParameterMissing The input parameter {parameter_name} is missing.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        """
        runtime = hosting_models.RuntimeOptions()
        return self.mobile_send_sms_code_ex(request, runtime)

    async def mobile_send_sms_code_async(
        self,
        request: hosting_models.MobileSendSmsCodeRequest,
    ) -> hosting_models.MobileSendSmsCodeModel:
        """
        发送短信验证码，用于登录、注册、修改密码、绑定等
        @tags account
        @error InvalidParameterMissing The input parameter {parameter_name} is missing.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        """
        runtime = hosting_models.RuntimeOptions()
        return await self.mobile_send_sms_code_ex_async(request, runtime)

    def account_revoke(
        self,
        request: hosting_models.RevokeRequest,
    ) -> hosting_models.AccountRevokeModel:
        """
        用户退出登录
        @tags account
        @error InvalidParameterMissing The input parameter {parameter_name} is missing.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        """
        runtime = hosting_models.RuntimeOptions()
        return self.account_revoke_ex(request, runtime)

    async def account_revoke_async(
        self,
        request: hosting_models.RevokeRequest,
    ) -> hosting_models.AccountRevokeModel:
        """
        用户退出登录
        @tags account
        @error InvalidParameterMissing The input parameter {parameter_name} is missing.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        """
        runtime = hosting_models.RuntimeOptions()
        return await self.account_revoke_ex_async(request, runtime)

    def account_token(
        self,
        request: hosting_models.AccountTokenRequest,
    ) -> hosting_models.AccountTokenModel:
        """
        用户通过刷新令牌（refresh_token）获取访问令牌（access_token）
        @tags account
        @error InvalidParameterMissing The input parameter {parameter_name} is missing.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        """
        runtime = hosting_models.RuntimeOptions()
        return self.account_token_ex(request, runtime)

    async def account_token_async(
        self,
        request: hosting_models.AccountTokenRequest,
    ) -> hosting_models.AccountTokenModel:
        """
        用户通过刷新令牌（refresh_token）获取访问令牌（access_token）
        @tags account
        @error InvalidParameterMissing The input parameter {parameter_name} is missing.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        """
        runtime = hosting_models.RuntimeOptions()
        return await self.account_token_ex_async(request, runtime)

    def admin_list_stores(
        self,
        request: hosting_models.AdminListStoresRequest,
    ) -> hosting_models.AdminListStoresModel:
        """
        列举Store列表
        @tags admin
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error InternalError The request has been failed due to some unknown error.
        """
        runtime = hosting_models.RuntimeOptions()
        return self.admin_list_stores_ex(request, runtime)

    async def admin_list_stores_async(
        self,
        request: hosting_models.AdminListStoresRequest,
    ) -> hosting_models.AdminListStoresModel:
        """
        列举Store列表
        @tags admin
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error Forbidden User not authorized to operate on the specified APIs.
        @error InternalError The request has been failed due to some unknown error.
        """
        runtime = hosting_models.RuntimeOptions()
        return await self.admin_list_stores_ex_async(request, runtime)

    def get_user_access_token(
        self,
        request: hosting_models.GetUserAccessTokenRequest,
    ) -> hosting_models.GetUserAccessTokenModel:
        """
        获取用户的accessToken
        @tags admin
        @error undefined undefined
        @error undefined undefined
        @error undefined undefined
        @error undefined undefined
        @error undefined undefined
        """
        runtime = hosting_models.RuntimeOptions()
        return self.get_user_access_token_ex(request, runtime)

    async def get_user_access_token_async(
        self,
        request: hosting_models.GetUserAccessTokenRequest,
    ) -> hosting_models.GetUserAccessTokenModel:
        """
        获取用户的accessToken
        @tags admin
        @error undefined undefined
        @error undefined undefined
        @error undefined undefined
        @error undefined undefined
        @error undefined undefined
        """
        runtime = hosting_models.RuntimeOptions()
        return await self.get_user_access_token_ex_async(request, runtime)

    def create_drive(
        self,
        request: hosting_models.CreateDriveRequest,
    ) -> hosting_models.CreateDriveModel:
        """
        支持normal和large两种drive，
        large类型的drive用于文件数多的场景，不支持list操作，
        当drive的文件数量大于1亿时，建议使用large类型。
        @tags drive
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return self.create_drive_ex(request, runtime)

    async def create_drive_async(
        self,
        request: hosting_models.CreateDriveRequest,
    ) -> hosting_models.CreateDriveModel:
        """
        支持normal和large两种drive，
        large类型的drive用于文件数多的场景，不支持list操作，
        当drive的文件数量大于1亿时，建议使用large类型。
        @tags drive
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return await self.create_drive_ex_async(request, runtime)

    def delete_drive(
        self,
        request: hosting_models.DeleteDriveRequest,
    ) -> hosting_models.DeleteDriveModel:
        """
        删除指定drive_id对应的Drive
        @tags drive
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return self.delete_drive_ex(request, runtime)

    async def delete_drive_async(
        self,
        request: hosting_models.DeleteDriveRequest,
    ) -> hosting_models.DeleteDriveModel:
        """
        删除指定drive_id对应的Drive
        @tags drive
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return await self.delete_drive_ex_async(request, runtime)

    def get_drive(
        self,
        request: hosting_models.GetDriveRequest,
    ) -> hosting_models.GetDriveModel:
        """
        获取指定drive_id对应的Drive详细信息。
        @tags drive
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return self.get_drive_ex(request, runtime)

    async def get_drive_async(
        self,
        request: hosting_models.GetDriveRequest,
    ) -> hosting_models.GetDriveModel:
        """
        获取指定drive_id对应的Drive详细信息。
        @tags drive
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return await self.get_drive_ex_async(request, runtime)

    def get_default_drive(
        self,
        request: hosting_models.GetDefaultDriveRequest,
    ) -> hosting_models.GetDefaultDriveModel:
        """
        一个用户可拥有多个drive，在创建drive时通过参数指定是否为这个用户的默认drive，
        每个用户只能设置一个默认drive。
        @tags drive
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return self.get_default_drive_ex(request, runtime)

    async def get_default_drive_async(
        self,
        request: hosting_models.GetDefaultDriveRequest,
    ) -> hosting_models.GetDefaultDriveModel:
        """
        一个用户可拥有多个drive，在创建drive时通过参数指定是否为这个用户的默认drive，
        每个用户只能设置一个默认drive。
        @tags drive
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return await self.get_default_drive_ex_async(request, runtime)

    def list_drives(
        self,
        request: hosting_models.ListDriveRequest,
    ) -> hosting_models.ListDrivesModel:
        """
        管理员列举指定用户的Drive
        @tags drive
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return self.list_drives_ex(request, runtime)

    async def list_drives_async(
        self,
        request: hosting_models.ListDriveRequest,
    ) -> hosting_models.ListDrivesModel:
        """
        管理员列举指定用户的Drive
        @tags drive
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return await self.list_drives_ex_async(request, runtime)

    def list_my_drives(
        self,
        request: hosting_models.ListMyDriveRequest,
    ) -> hosting_models.ListMyDrivesModel:
        """
        列举当前用户（访问令牌）的Drive
        @tags drive
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return self.list_my_drives_ex(request, runtime)

    async def list_my_drives_async(
        self,
        request: hosting_models.ListMyDriveRequest,
    ) -> hosting_models.ListMyDrivesModel:
        """
        列举当前用户（访问令牌）的Drive
        @tags drive
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return await self.list_my_drives_ex_async(request, runtime)

    def update_drive(
        self,
        request: hosting_models.UpdateDriveRequest,
    ) -> hosting_models.UpdateDriveModel:
        """
        更新指定drive_id的Drive信息
        @tags drive
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return self.update_drive_ex(request, runtime)

    async def update_drive_async(
        self,
        request: hosting_models.UpdateDriveRequest,
    ) -> hosting_models.UpdateDriveModel:
        """
        更新指定drive_id的Drive信息
        @tags drive
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return await self.update_drive_ex_async(request, runtime)

    def complete_file(
        self,
        request: hosting_models.HostingCompleteFileRequest,
    ) -> hosting_models.CompleteFileModel:
        """
        完成文件上传
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return self.complete_file_ex(request, runtime)

    async def complete_file_async(
        self,
        request: hosting_models.HostingCompleteFileRequest,
    ) -> hosting_models.CompleteFileModel:
        """
        完成文件上传
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return await self.complete_file_ex_async(request, runtime)

    def copy_file(
        self,
        request: hosting_models.HostingCopyFileRequest,
    ) -> hosting_models.CopyFileModel:
        """
        指定源文件或文件夹路径，拷贝到指定的文件夹。
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return self.copy_file_ex(request, runtime)

    async def copy_file_async(
        self,
        request: hosting_models.HostingCopyFileRequest,
    ) -> hosting_models.CopyFileModel:
        """
        指定源文件或文件夹路径，拷贝到指定的文件夹。
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return await self.copy_file_ex_async(request, runtime)

    def create_file(
        self,
        request: hosting_models.HostingCreateFileRequest,
    ) -> hosting_models.CreateFileModel:
        """
        创建文件或者文件夹。
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error AlreadyExist {resource} has already exists. {extra_msg}
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return self.create_file_ex(request, runtime)

    async def create_file_async(
        self,
        request: hosting_models.HostingCreateFileRequest,
    ) -> hosting_models.CreateFileModel:
        """
        创建文件或者文件夹。
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error AlreadyExist {resource} has already exists. {extra_msg}
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return await self.create_file_ex_async(request, runtime)

    def delete_file(
        self,
        request: hosting_models.HostingDeleteFileRequest,
    ) -> hosting_models.DeleteFileModel:
        """
        指定文件或文件夹路径，删除文件或文件夹
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return self.delete_file_ex(request, runtime)

    async def delete_file_async(
        self,
        request: hosting_models.HostingDeleteFileRequest,
    ) -> hosting_models.DeleteFileModel:
        """
        指定文件或文件夹路径，删除文件或文件夹
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return await self.delete_file_ex_async(request, runtime)

    def get_file(
        self,
        request: hosting_models.HostingGetFileRequest,
    ) -> hosting_models.GetFileModel:
        """
        获取指定文件或文件夹路径，获取文件或文件夹信息。
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return self.get_file_ex(request, runtime)

    async def get_file_async(
        self,
        request: hosting_models.HostingGetFileRequest,
    ) -> hosting_models.GetFileModel:
        """
        获取指定文件或文件夹路径，获取文件或文件夹信息。
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return await self.get_file_ex_async(request, runtime)

    def get_download_url(
        self,
        request: hosting_models.HostingGetDownloadUrlRequest,
    ) -> hosting_models.GetDownloadUrlModel:
        """
        指定文件路径，获取文件下载地址
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return self.get_download_url_ex(request, runtime)

    async def get_download_url_async(
        self,
        request: hosting_models.HostingGetDownloadUrlRequest,
    ) -> hosting_models.GetDownloadUrlModel:
        """
        指定文件路径，获取文件下载地址
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return await self.get_download_url_ex_async(request, runtime)

    def get_secure_url(
        self,
        request: hosting_models.HostingGetSecureUrlRequest,
    ) -> hosting_models.GetSecureUrlModel:
        """
        指定文件路径，获取文件安全地址
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return self.get_secure_url_ex(request, runtime)

    async def get_secure_url_async(
        self,
        request: hosting_models.HostingGetSecureUrlRequest,
    ) -> hosting_models.GetSecureUrlModel:
        """
        指定文件路径，获取文件安全地址
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return await self.get_secure_url_ex_async(request, runtime)

    def get_upload_url(
        self,
        request: hosting_models.HostingGetUploadUrlRequest,
    ) -> hosting_models.GetUploadUrlModel:
        """
        可指定分片信息，一次获取多个分片的上传地址。
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return self.get_upload_url_ex(request, runtime)

    async def get_upload_url_async(
        self,
        request: hosting_models.HostingGetUploadUrlRequest,
    ) -> hosting_models.GetUploadUrlModel:
        """
        可指定分片信息，一次获取多个分片的上传地址。
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return await self.get_upload_url_ex_async(request, runtime)

    def list_file(
        self,
        request: hosting_models.HostingListFileRequest,
    ) -> hosting_models.ListFileModel:
        """
        指定父文件夹路径，列举文件夹下的文件或者文件夹
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return self.list_file_ex(request, runtime)

    async def list_file_async(
        self,
        request: hosting_models.HostingListFileRequest,
    ) -> hosting_models.ListFileModel:
        """
        指定父文件夹路径，列举文件夹下的文件或者文件夹
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return await self.list_file_ex_async(request, runtime)

    def list_uploaded_parts(
        self,
        request: hosting_models.HostingListUploadedPartRequest,
    ) -> hosting_models.ListUploadedPartsModel:
        """
        列举UploadID对应的已上传分片。
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return self.list_uploaded_parts_ex(request, runtime)

    async def list_uploaded_parts_async(
        self,
        request: hosting_models.HostingListUploadedPartRequest,
    ) -> hosting_models.ListUploadedPartsModel:
        """
        列举UploadID对应的已上传分片。
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return await self.list_uploaded_parts_ex_async(request, runtime)

    def move_file(
        self,
        request: hosting_models.HostingMoveFileRequest,
    ) -> hosting_models.MoveFileModel:
        """
        指定源文件或文件夹路径，移动到指定的文件夹。
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return self.move_file_ex(request, runtime)

    async def move_file_async(
        self,
        request: hosting_models.HostingMoveFileRequest,
    ) -> hosting_models.MoveFileModel:
        """
        指定源文件或文件夹路径，移动到指定的文件夹。
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return await self.move_file_ex_async(request, runtime)

    def video_definition(
        self,
        request: hosting_models.HostingVideoDefinitionRequest,
    ) -> hosting_models.VideoDefinitionModel:
        """
        获取视频支持的分辨率
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return self.video_definition_ex(request, runtime)

    async def video_definition_async(
        self,
        request: hosting_models.HostingVideoDefinitionRequest,
    ) -> hosting_models.VideoDefinitionModel:
        """
        获取视频支持的分辨率
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return await self.video_definition_ex_async(request, runtime)

    def video_license(
        self,
        request: hosting_models.HostingVideoDRMLicenseRequest,
    ) -> hosting_models.VideoLicenseModel:
        """
        获取视频的DRM License
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return self.video_license_ex(request, runtime)

    async def video_license_async(
        self,
        request: hosting_models.HostingVideoDRMLicenseRequest,
    ) -> hosting_models.VideoLicenseModel:
        """
        获取视频的DRM License
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return await self.video_license_ex_async(request, runtime)

    def video_m3u_8(
        self,
        request: hosting_models.HostingVideoM3U8Request,
    ) -> hosting_models.VideoM3u8Model:
        """
        获取视频转码后的m3u8文件
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return self.video_m3u_8ex(request, runtime)

    async def video_m3u_8_async(
        self,
        request: hosting_models.HostingVideoM3U8Request,
    ) -> hosting_models.VideoM3u8Model:
        """
        获取视频转码后的m3u8文件
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return await self.video_m3u_8ex_async(request, runtime)

    def video_transcode(
        self,
        request: hosting_models.HostingVideoTranscodeRequest,
    ) -> hosting_models.VideoTranscodeModel:
        """
        将mp4格式的视频文件，转为m3u8
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return self.video_transcode_ex(request, runtime)

    async def video_transcode_async(
        self,
        request: hosting_models.HostingVideoTranscodeRequest,
    ) -> hosting_models.VideoTranscodeModel:
        """
        将mp4格式的视频文件，转为m3u8
        @tags file
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return await self.video_transcode_ex_async(request, runtime)

    def create_share(
        self,
        request: hosting_models.CreateShareRequest,
    ) -> hosting_models.CreateShareModel:
        """
        创建共享。
        @tags share
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return self.create_share_ex(request, runtime)

    async def create_share_async(
        self,
        request: hosting_models.CreateShareRequest,
    ) -> hosting_models.CreateShareModel:
        """
        创建共享。
        @tags share
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return await self.create_share_ex_async(request, runtime)

    def delete_share(
        self,
        request: hosting_models.DeleteShareRequest,
    ) -> hosting_models.DeleteShareModel:
        """
        删除指定共享
        @tags share
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return self.delete_share_ex(request, runtime)

    async def delete_share_async(
        self,
        request: hosting_models.DeleteShareRequest,
    ) -> hosting_models.DeleteShareModel:
        """
        删除指定共享
        @tags share
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return await self.delete_share_ex_async(request, runtime)

    def get_share(
        self,
        request: hosting_models.GetShareRequest,
    ) -> hosting_models.GetShareModel:
        """
        获取共享信息。
        @tags share
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return self.get_share_ex(request, runtime)

    async def get_share_async(
        self,
        request: hosting_models.GetShareRequest,
    ) -> hosting_models.GetShareModel:
        """
        获取共享信息。
        @tags share
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return await self.get_share_ex_async(request, runtime)

    def list_share(
        self,
        request: hosting_models.ListShareRequest,
    ) -> hosting_models.ListShareModel:
        """
        列举指定用户的共享
        @tags share
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return self.list_share_ex(request, runtime)

    async def list_share_async(
        self,
        request: hosting_models.ListShareRequest,
    ) -> hosting_models.ListShareModel:
        """
        列举指定用户的共享
        @tags share
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return await self.list_share_ex_async(request, runtime)

    def update_share(
        self,
        request: hosting_models.UpdateShareRequest,
    ) -> hosting_models.UpdateShareModel:
        """
        修改指定共享
        @tags share
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return self.update_share_ex(request, runtime)

    async def update_share_async(
        self,
        request: hosting_models.UpdateShareRequest,
    ) -> hosting_models.UpdateShareModel:
        """
        修改指定共享
        @tags share
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return await self.update_share_ex_async(request, runtime)

    def list_storefile(
        self,
        request: hosting_models.ListStoreFileRequest,
    ) -> hosting_models.ListStorefileModel:
        """
        列举指定store下的所有文件。
        @tags store
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return self.list_storefile_ex(request, runtime)

    async def list_storefile_async(
        self,
        request: hosting_models.ListStoreFileRequest,
    ) -> hosting_models.ListStorefileModel:
        """
        列举指定store下的所有文件。
        @tags store
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return await self.list_storefile_ex_async(request, runtime)

    def create_user(
        self,
        request: hosting_models.CreateUserRequest,
    ) -> hosting_models.CreateUserModel:
        """
        创建用户，只有管理员可以调用
        @tags user
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return self.create_user_ex(request, runtime)

    async def create_user_async(
        self,
        request: hosting_models.CreateUserRequest,
    ) -> hosting_models.CreateUserModel:
        """
        创建用户，只有管理员可以调用
        @tags user
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return await self.create_user_ex_async(request, runtime)

    def delete_user(
        self,
        request: hosting_models.DeleteUserRequest,
    ) -> hosting_models.DeleteUserModel:
        """
        只有管理员可以调用
        @tags user
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return self.delete_user_ex(request, runtime)

    async def delete_user_async(
        self,
        request: hosting_models.DeleteUserRequest,
    ) -> hosting_models.DeleteUserModel:
        """
        只有管理员可以调用
        @tags user
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return await self.delete_user_ex_async(request, runtime)

    def get_user(
        self,
        request: hosting_models.GetUserRequest,
    ) -> hosting_models.GetUserModel:
        """
        获取用户详细信息，普通用户只能获取自己的信息，管理员可以获取任意用户的信息。
        @tags user
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return self.get_user_ex(request, runtime)

    async def get_user_async(
        self,
        request: hosting_models.GetUserRequest,
    ) -> hosting_models.GetUserModel:
        """
        获取用户详细信息，普通用户只能获取自己的信息，管理员可以获取任意用户的信息。
        @tags user
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return await self.get_user_ex_async(request, runtime)

    def list_users(
        self,
        request: hosting_models.ListUserRequest,
    ) -> hosting_models.ListUsersModel:
        """
        只有管理员可以调用
        @tags user
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return self.list_users_ex(request, runtime)

    async def list_users_async(
        self,
        request: hosting_models.ListUserRequest,
    ) -> hosting_models.ListUsersModel:
        """
        只有管理员可以调用
        @tags user
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return await self.list_users_ex_async(request, runtime)

    def search_user(
        self,
        request: hosting_models.SearchUserRequest,
    ) -> hosting_models.SearchUserModel:
        """
        该接口将会根据条件查询用户，只有管理员可以调用
        @tags user
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return self.search_user_ex(request, runtime)

    async def search_user_async(
        self,
        request: hosting_models.SearchUserRequest,
    ) -> hosting_models.SearchUserModel:
        """
        该接口将会根据条件查询用户，只有管理员可以调用
        @tags user
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return await self.search_user_ex_async(request, runtime)

    def update_user(
        self,
        request: hosting_models.UpdateUserRequest,
    ) -> hosting_models.UpdateUserModel:
        """
        用户可以修改自己的description，nick_name，avatar；
        管理员在用户基础上还可修改status（可以修改任意用户）；
        超级管理员在管理员基础上还可修改role（可以修改任意用户）。
        @tags user
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return self.update_user_ex(request, runtime)

    async def update_user_async(
        self,
        request: hosting_models.UpdateUserRequest,
    ) -> hosting_models.UpdateUserModel:
        """
        用户可以修改自己的description，nick_name，avatar；
        管理员在用户基础上还可修改status（可以修改任意用户）；
        超级管理员在管理员基础上还可修改role（可以修改任意用户）。
        @tags user
        @error InvalidParameter The input parameter {parameter_name} is not valid.
        @error AccessTokenInvalid AccessToken is invalid. {message}
        @error ForbiddenNoPermission No Permission to access resource {resource_name}.
        @error NotFound The resource {resource_name} cannot be found. Please check.
        @error InternalError The request has been failed due to some unknown error.
        @error ServiceUnavailable The request has failed due to a temporary failure of the server.
        """
        runtime = hosting_models.RuntimeOptions()
        return await self.update_user_ex_async(request, runtime)

    def get_pathname(
        self,
        nickname: str,
        path: str,
    ) -> str:
        if UtilClient.empty(nickname):
            return path
        return f'/{nickname}{path}'

    def set_expire_time(
        self,
        expire_time: str,
    ) -> None:
        if UtilClient.is_unset(self._access_token_credential):
            return
        self._access_token_credential.set_expire_time(expire_time)

    async def set_expire_time_async(
        self,
        expire_time: str,
    ) -> None:
        if UtilClient.is_unset(self._access_token_credential):
            return
        self._access_token_credential.set_expire_time(expire_time)

    def get_expire_time(self) -> str:
        if UtilClient.is_unset(self._access_token_credential):
            return ''
        expire_time = self._access_token_credential.get_expire_time()
        return expire_time

    def set_refresh_token(
        self,
        token: str,
    ) -> None:
        if UtilClient.is_unset(self._access_token_credential):
            return
        self._access_token_credential.set_refresh_token(token)

    def get_refresh_token(self) -> str:
        if UtilClient.is_unset(self._access_token_credential):
            return ''
        token = self._access_token_credential.get_refresh_token()
        return token

    def set_access_token(
        self,
        token: str,
    ) -> None:
        if UtilClient.is_unset(self._access_token_credential):
            return
        self._access_token_credential.set_access_token(token)

    def get_access_token(self) -> str:
        if UtilClient.is_unset(self._access_token_credential):
            return ''
        token = self._access_token_credential.get_access_token()
        return token

    async def get_access_token_async(self) -> str:
        if UtilClient.is_unset(self._access_token_credential):
            return ''
        token = await self._access_token_credential.get_access_token_async()
        return token

    def set_user_agent(
        self,
        user_agent: str,
    ) -> None:
        self._user_agent = user_agent

    def append_user_agent(
        self,
        user_agent: str,
    ) -> None:
        self._user_agent = f'{self._user_agent} {user_agent}'

    def get_user_agent(self) -> str:
        user_agent = UtilClient.get_user_agent(self._user_agent)
        return user_agent

    def get_access_key_id(self) -> str:
        if UtilClient.is_unset(self._credential):
            return ''
        access_key_id = self._credential.get_access_key_id()
        return access_key_id

    async def get_access_key_id_async(self) -> str:
        if UtilClient.is_unset(self._credential):
            return ''
        access_key_id = await self._credential.get_access_key_id_async()
        return access_key_id

    def get_access_key_secret(self) -> str:
        if UtilClient.is_unset(self._credential):
            return ''
        secret = self._credential.get_access_key_secret()
        return secret

    async def get_access_key_secret_async(self) -> str:
        if UtilClient.is_unset(self._credential):
            return ''
        secret = await self._credential.get_access_key_secret_async()
        return secret

    def get_security_token(self) -> str:
        if UtilClient.is_unset(self._credential):
            return ''
        token = self._credential.get_security_token()
        return token

    async def get_security_token_async(self) -> str:
        if UtilClient.is_unset(self._credential):
            return ''
        token = await self._credential.get_security_token_async()
        return token
