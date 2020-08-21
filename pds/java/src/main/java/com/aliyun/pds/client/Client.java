// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client;

import com.aliyun.tea.*;
import com.aliyun.pds.client.models.*;

public class Client {

    public String _domainId;
    public com.aliyun.pdscredentials.Client _accessTokenCredential;
    public String _endpoint;
    public String _protocol;
    public String _nickname;
    public String _userAgent;
    public com.aliyun.credentials.Client _credential;
    public Client(Config config) throws Exception {
        if (com.aliyun.teautil.Common.isUnset(TeaModel.buildMap(config))) {
            throw new TeaException(TeaConverter.buildMap(
                new TeaPair("name", "ParameterMissing"),
                new TeaPair("message", "'config' can not be unset")
            ));
        }

        com.aliyun.teautil.Common.validateModel(config);
        if (!com.aliyun.teautil.Common.empty(config.accessToken) || !com.aliyun.teautil.Common.empty(config.refreshToken)) {
            com.aliyun.pdscredentials.models.Config accessConfig = com.aliyun.pdscredentials.models.Config.build(TeaConverter.buildMap(
                new TeaPair("accessToken", config.accessToken),
                new TeaPair("endpoint", config.endpoint),
                new TeaPair("domainId", config.domainId),
                new TeaPair("clientId", config.clientId),
                new TeaPair("refreshToken", config.refreshToken),
                new TeaPair("clientSecret", config.clientSecret),
                new TeaPair("expireTime", config.expireTime)
            ));
            this._accessTokenCredential = new com.aliyun.pdscredentials.Client(accessConfig);
        }

        if (!com.aliyun.teautil.Common.empty(config.accessKeyId)) {
            if (com.aliyun.teautil.Common.empty(config.type)) {
                config.type = "access_key";
            }

            com.aliyun.credentials.models.Config credentialConfig = com.aliyun.credentials.models.Config.build(TeaConverter.buildMap(
                new TeaPair("accessKeyId", config.accessKeyId),
                new TeaPair("type", config.type),
                new TeaPair("accessKeySecret", config.accessKeySecret),
                new TeaPair("securityToken", config.securityToken)
            ));
            this._credential = new com.aliyun.credentials.Client(credentialConfig);
        }

        this._endpoint = config.endpoint;
        this._protocol = config.protocol;
        this._userAgent = config.userAgent;
        this._nickname = config.nickname;
        this._domainId = config.domainId;
    }

    public CancelLinkModel cancelLinkEx(CancelLinkRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/account/cancel_link");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".auth.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new CancelLinkModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public ConfirmLinkModel confirmLinkEx(ConfirmLinkRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/account/confirm_link");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".auth.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new ConfirmLinkModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public ChangePasswordModel changePasswordEx(DefaultChangePasswordRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/account/default/change_password");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".auth.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new ChangePasswordModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public SetPasswordModel setPasswordEx(DefaultSetPasswordRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/account/default/set_password");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".auth.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 204)) {
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("headers", response_.headers)
                    ), new SetPasswordModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public VerifyCodeModel verifyCodeEx(VerifyCodeRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/account/default/verify_code");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".auth.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new VerifyCodeModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public GetAccessTokenByLinkInfoModel getAccessTokenByLinkInfoEx(GetAccessTokenByLinkInfoRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/account/get_access_token_by_link_info");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".auth.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new GetAccessTokenByLinkInfoModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public GetCaptchaModel getCaptchaEx(GetCaptchaRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/account/get_captcha");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".auth.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new GetCaptchaModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public GetLinkInfoModel getLinkInfoEx(GetByLinkInfoRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/account/get_link_info");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".auth.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new GetLinkInfoModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public GetLinkInfoByUserIdModel getLinkInfoByUserIdEx(GetLinkInfoByUserIDRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/account/get_link_info_by_user_id");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".auth.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new GetLinkInfoByUserIdModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public GetPublicKeyModel getPublicKeyEx(GetAppPublicKeyRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/account/get_public_key");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".auth.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new GetPublicKeyModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public LinkModel linkEx(AccountLinkRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/account/link");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".auth.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new LinkModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public CheckExistModel checkExistEx(MobileCheckExistRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/account/mobile/check_exist");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".auth.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new CheckExistModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public LoginModel loginEx(MobileLoginRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/account/mobile/login");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".auth.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new LoginModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public RegisterModel registerEx(MobileRegisterRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/account/mobile/register");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".auth.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new RegisterModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public MobileSendSmsCodeModel mobileSendSmsCodeEx(MobileSendSmsCodeRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/account/mobile/send_sms_code");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".auth.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new MobileSendSmsCodeModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public AccountRevokeModel accountRevokeEx(RevokeRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/account/revoke");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".auth.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 204)) {
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("headers", response_.headers)
                    ), new AccountRevokeModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public AccountTokenModel accountTokenEx(TokenRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/account/token");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".auth.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new AccountTokenModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public AdminListStoresModel adminListStoresEx(AdminListStoresRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/domain/list_stores");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".api.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new AdminListStoresModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public GetUserAccessTokenModel getUserAccessTokenEx(GetUserAccessTokenRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/user/get_access_token");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".api.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new GetUserAccessTokenModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public GetAsyncTaskInfoModel getAsyncTaskInfoEx(GetAsyncTaskRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/async_task/get");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".api.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new GetAsyncTaskInfoModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public BatchOperationModel batchOperationEx(BatchRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/batch");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".api.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new BatchOperationModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public CreateDriveModel createDriveEx(CreateDriveRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/drive/create");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".api.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 201)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new CreateDriveModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public DeleteDriveModel deleteDriveEx(DeleteDriveRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/drive/delete");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".api.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 204)) {
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("headers", response_.headers)
                    ), new DeleteDriveModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public GetDriveModel getDriveEx(GetDriveRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/drive/get");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".api.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new GetDriveModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public GetDefaultDriveModel getDefaultDriveEx(GetDefaultDriveRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/drive/get_default_drive");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".api.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new GetDefaultDriveModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public ListDrivesModel listDrivesEx(ListDriveRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/drive/list");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".api.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new ListDrivesModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public ListMyDrivesModel listMyDrivesEx(ListMyDriveRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/drive/list_my_drives");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".api.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new ListMyDrivesModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public UpdateDriveModel updateDriveEx(UpdateDriveRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/drive/update");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".api.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new UpdateDriveModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public CompleteFileModel completeFileEx(CompleteFileRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/file/complete");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".api.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new CompleteFileModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public CopyFileModel copyFileEx(CopyFileRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/file/copy");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".api.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 201)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new CopyFileModel());
                }

                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 202)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new CopyFileModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public CreateFileModel createFileEx(CreateFileRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/file/create");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".api.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 201)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new CreateFileModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public DeleteFileModel deleteFileEx(DeleteFileRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/file/delete");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".api.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 202)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new DeleteFileModel());
                }

                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 204)) {
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("headers", response_.headers)
                    ), new DeleteFileModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public GetFileModel getFileEx(GetFileRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/file/get");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".api.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new GetFileModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public GetFileByPathModel getFileByPathEx(GetFileByPathRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/file/get_by_path");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".api.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new GetFileByPathModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public GetDownloadUrlModel getDownloadUrlEx(GetDownloadUrlRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/file/get_download_url");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".api.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new GetDownloadUrlModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public GetLastCursorModel getLastCursorEx(GetLastCursorRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/file/get_last_cursor");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".api.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new GetLastCursorModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public GetMediaPlayUrlModel getMediaPlayUrlEx(GetMediaPlayURLRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/file/get_media_play_url");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".api.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new GetMediaPlayUrlModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public GetOfficePreviewUrlModel getOfficePreviewUrlEx(GetOfficePreviewUrlRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/file/get_office_preview_url");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".api.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new GetOfficePreviewUrlModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public GetUploadUrlModel getUploadUrlEx(GetUploadUrlRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/file/get_upload_url");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".api.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new GetUploadUrlModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public GetVideoPreviewSpriteUrlModel getVideoPreviewSpriteUrlEx(GetVideoPreviewSpriteURLRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/file/get_video_preview_sprite_url");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".api.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new GetVideoPreviewSpriteUrlModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public GetVideoPreviewUrlModel getVideoPreviewUrlEx(GetVideoPreviewURLRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/file/get_video_preview_url");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".api.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new GetVideoPreviewUrlModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public ListFileModel listFileEx(ListFileRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/file/list");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".api.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new ListFileModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public ListFileByAnonymousModel listFileByAnonymousEx(ListByAnonymousRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/file/list_by_anonymous");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".api.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new ListFileByAnonymousModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public ListFileByCustomIndexKeyModel listFileByCustomIndexKeyEx(ListFileByCustomIndexKeyRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/file/list_by_custom_index_key");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".api.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new ListFileByCustomIndexKeyModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public ListFileDeltaModel listFileDeltaEx(ListFileDeltaRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/file/list_delta");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".api.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new ListFileDeltaModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public ListUploadedPartsModel listUploadedPartsEx(ListUploadedPartRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/file/list_uploaded_parts");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".api.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new ListUploadedPartsModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public MoveFileModel moveFileEx(MoveFileRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/file/move");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".api.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new MoveFileModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public ScanFileMetaModel scanFileMetaEx(ScanFileMetaRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/file/scan");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".api.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new ScanFileMetaModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public SearchFileModel searchFileEx(SearchFileRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/file/search");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".api.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new SearchFileModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public UpdateFileModel updateFileEx(UpdateFileMetaRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/file/update");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".api.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new UpdateFileModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public CancelShareLinkModel cancelShareLinkEx(CancelShareLinkRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/share_link/cancel");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".api.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 204)) {
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("headers", response_.headers)
                    ), new CancelShareLinkModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public CreateShareLinkModel createShareLinkEx(CreateShareLinkRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/share_link/create");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".api.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 201)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new CreateShareLinkModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public GetShareIdModel getShareIdEx(GetShareLinkIDRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/share_link/get_share_id");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".api.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new GetShareIdModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public GetShareTokenModel getShareTokenEx(GetShareLinkTokenRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/share_link/get_share_token");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".api.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new GetShareTokenModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public ListShareLinkModel listShareLinkEx(ListShareLinkRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/share_link/list");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".api.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new ListShareLinkModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public CreateUserModel createUserEx(CreateUserRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/user/create");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".api.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 201)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new CreateUserModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public DeleteUserModel deleteUserEx(DeleteUserRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/user/delete");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".api.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 204)) {
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("headers", response_.headers)
                    ), new DeleteUserModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public GetUserModel getUserEx(GetUserRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/user/get");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".api.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new GetUserModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public ListUsersModel listUsersEx(ListUserRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/user/list");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".api.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new ListUsersModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public SearchUserModel searchUserEx(SearchUserRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/user/search");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".api.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new SearchUserModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public UpdateUserModel updateUserEx(UpdateUserRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/user/update");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".api.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new UpdateUserModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public CreateStoryModel createStoryEx(CreateStoryRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/image/create_story");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".api.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new CreateStoryModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public GetPhotoCountModel getPhotoCountEx(GetImageCountRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/image/get_photo_count");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".api.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new GetPhotoCountModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public GetStoryDetailModel getStoryDetailEx(GetStoryDetailRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/image/get_story_detail");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".api.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new GetStoryDetailModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public GetStoryTaskModel getStoryTaskEx(GetStoryTaskRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/image/get_story_task");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".api.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new GetStoryTaskModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public ListAddressGroupsModel listAddressGroupsEx(ListImageAddressGroupsRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/image/list_address_groups");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".api.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new ListAddressGroupsModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public ListFaceGroupsModel listFaceGroupsEx(ListImageFaceGroupsRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/image/list_face_groups");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".api.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new ListFaceGroupsModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public ListStoryModel listStoryEx(ListStoryRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/image/list_story");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".api.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new ListStoryModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public ListTagsModel listTagsEx(ListImageTagsRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/image/list_tags");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".api.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new ListTagsModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public SearchAddressGroupsModel searchAddressGroupsEx(SearchImageAddressGroupsRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/image/search_address_groups");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".api.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new SearchAddressGroupsModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    public UpdateFacegroupInfoModel updateFacegroupInfoEx(UpdateFaceGroupInfoRequest request, RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(request, "request");
        TeaModel.validateParams(runtime, "runtime");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("localAddr", runtime.localAddr),
            new TeaPair("httpProxy", runtime.httpProxy),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("socks5Proxy", runtime.socks5Proxy),
            new TeaPair("socks5NetWork", runtime.socks5NetWork),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                String accesskeyId = this.getAccessKeyId();
                String accessKeySecret = this.getAccessKeySecret();
                String securityToken = this.getSecurityToken();
                String accessToken = this.getAccessToken();
                java.util.Map<String, Object> realReq = com.aliyun.teautil.Common.toMap(request);
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "https");
                request_.method = "POST";
                request_.pathname = this.getPathname(_nickname, "/v2/image/update_facegroup_info");
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _domainId + ".api.aliyunpds.com")),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    request.headers
                );
                realReq.put("headers", null);
                if (!com.aliyun.teautil.Common.empty(accessToken)) {
                    request_.headers.put("authorization", "Bearer " + accessToken + "");
                } else if (!com.aliyun.teautil.Common.empty(accesskeyId) && !com.aliyun.teautil.Common.empty(accessKeySecret)) {
                    if (!com.aliyun.teautil.Common.empty(securityToken)) {
                        request_.headers.put("x-acs-security-token", securityToken);
                    }

                    request_.headers.put("date", com.aliyun.teautil.Common.getDateUTCString());
                    request_.headers.put("accept", "application/json");
                    request_.headers.put("x-acs-signature-method", "HMAC-SHA1");
                    request_.headers.put("x-acs-signature-version", "1.0");
                    String stringToSign = com.aliyun.roautil.Client.getStringToSign(request_);
                    request_.headers.put("authorization", "acs " + accesskeyId + ":" + com.aliyun.roautil.Client.getSignature(stringToSign, accessKeySecret) + "");
                }

                request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(realReq));
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                java.util.Map<String, Object> respMap = null;
                Object obj = null;
                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 200)) {
                    obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                    return TeaModel.toModel(TeaConverter.buildMap(
                        new TeaPair("body", respMap),
                        new TeaPair("headers", response_.headers)
                    ), new UpdateFacegroupInfoModel());
                }

                if (!com.aliyun.teautil.Common.empty(response_.headers.get("x-ca-error-message"))) {
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        )),
                        new TeaPair("message", response_.headers.get("x-ca-error-message"))
                    ));
                }

                obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                respMap = com.aliyun.teautil.Common.assertAsMap(obj);
                throw new TeaException(TeaConverter.merge(Object.class,
                    TeaConverter.buildMap(
                        new TeaPair("data", TeaConverter.buildMap(
                            new TeaPair("requestId", response_.headers.get("x-ca-request-id")),
                            new TeaPair("statusCode", response_.statusCode),
                            new TeaPair("statusMessage", response_.statusMessage)
                        ))
                    ),
                    respMap
                ));
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    /**
     * 取消绑定关系，生成新用户，返回访问令牌
     * @tags account
     * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
     * @error Forbidden User not authorized to operate on the specified APIs.
     * @error InternalError The request has been failed due to some unknown error.
     */
    public CancelLinkModel cancelLink(CancelLinkRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.cancelLinkEx(request, runtime);
    }

    /**
     * 确认绑定关系, 成功后返回访问令牌
     * @tags account
     * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
     * @error AccessTokenInvalid AccessToken is invalid. {message}
     * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
     * @error NotFound The resource {resource_name} cannot be found. Please check.
     * @error InternalError The request has been failed due to some unknown error.
     */
    public ConfirmLinkModel confirmLink(ConfirmLinkRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.confirmLinkEx(request, runtime);
    }

    /**
     * 修改手机登录密码，密码必须包含数字和字母，长度8-20个字符
     * @tags account
     * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
     * @error Forbidden User not authorized to operate on the specified APIs.
     * @error NotFound The resource {resource_name} cannot be found. Please check.
     * @error InternalError The request has been failed due to some unknown error.
     */
    public ChangePasswordModel changePassword(DefaultChangePasswordRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.changePasswordEx(request, runtime);
    }

    /**
     * 设置手机登录密码，密码必须包含数字和字母，长度8-20个字符
     * @tags account
     * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
     * @error Forbidden User not authorized to operate on the specified APIs.
     * @error NotFound The resource {resource_name} cannot be found. Please check.
     * @error InternalError The request has been failed due to some unknown error.
     */
    public SetPasswordModel setPassword(DefaultSetPasswordRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.setPasswordEx(request, runtime);
    }

    /**
     * 校验手机短信验证码，用于重置密码时校验手机，通过校验后返回state，可通过state重新设置密码
     * @tags account
     * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
     * @error Forbidden User not authorized to operate on the specified APIs.
     * @error NotFound The resource {resource_name} cannot be found. Please check.
     * @error InternalError The request has been failed due to some unknown error.
     */
    public VerifyCodeModel verifyCode(VerifyCodeRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.verifyCodeEx(request, runtime);
    }

    /**
     * 管理员通过账号信息直接获取用户的访问令牌
     * @tags account
     * @error InvalidParameter The input parameter {parameter_name} is not valid.
     * @error Forbidden User not authorized to operate on the specified APIs.
     * @error NotFound The resource {resource_name} cannot be found. Please check.
     * @error InternalError The request has been failed due to some unknown error.
     */
    public GetAccessTokenByLinkInfoModel getAccessTokenByLinkInfo(GetAccessTokenByLinkInfoRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.getAccessTokenByLinkInfoEx(request, runtime);
    }

    /**
     * 获取图片验证码，用于人机校验，默认不需要
     * @tags account
     * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
     * @error Forbidden User not authorized to operate on the specified APIs.
     * @error NotFound The resource {resource_name} cannot be found. Please check.
     * @error InternalError The request has been failed due to some unknown error.
     */
    public GetCaptchaModel getCaptcha(GetCaptchaRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.getCaptchaEx(request, runtime);
    }

    /**
     * 获取用户认证方式详情
     * @tags account
     * @error InvalidParameter The input parameter {parameter_name} is not valid.
     * @error Forbidden User not authorized to operate on the specified APIs.
     * @error NotFound The resource {resource_name} cannot be found. Please check.
     * @error InternalError The request has been failed due to some unknown error.
     */
    public GetLinkInfoModel getLinkInfo(GetByLinkInfoRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.getLinkInfoEx(request, runtime);
    }

    /**
     * 获取用户的所有绑定信息
     * @tags account
     * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
     * @error Forbidden User not authorized to operate on the specified APIs.
     * @error InternalError The request has been failed due to some unknown error.
     */
    public GetLinkInfoByUserIdModel getLinkInfoByUserId(GetLinkInfoByUserIDRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.getLinkInfoByUserIdEx(request, runtime);
    }

    /**
     * 获取公钥，用于加密对称密钥
     * @tags account
     * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
     * @error Forbidden User not authorized to operate on the specified APIs.
     * @error NotFound The resource {resource_name} cannot be found. Please check.
     * @error InternalError The request has been failed due to some unknown error.
     */
    public GetPublicKeyModel getPublicKey(GetAppPublicKeyRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.getPublicKeyEx(request, runtime);
    }

    /**
     * 绑定用户认证方式
     * @tags account
     * @error InvalidParameter The input parameter {parameter_name} is not valid.
     * @error Forbidden User not authorized to operate on the specified APIs.
     * @error NotFound The resource {resource_name} cannot be found. Please check.
     * @error AlreadyExist {resource} has already exists. {extra_msg}
     * @error InternalError The request has been failed due to some unknown error.
     */
    public LinkModel link(AccountLinkRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.linkEx(request, runtime);
    }

    /**
     * 查询手机号是否已被注册
     * @tags account
     * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
     * @error Forbidden User not authorized to operate on the specified APIs.
     * @error NotFound The resource {resource_name} cannot be found. Please check.
     * @error InternalError The request has been failed due to some unknown error.
     */
    public CheckExistModel checkExist(MobileCheckExistRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.checkExistEx(request, runtime);
    }

    /**
     * 通过手机号+短信或密码登录，返回刷新令牌和访问令牌
     * @tags account
     * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
     * @error Forbidden User not authorized to operate on the specified APIs.
     * @error NotFound The resource {resource_name} cannot be found. Please check.
     * @error InternalError The request has been failed due to some unknown error.
     */
    public LoginModel login(MobileLoginRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.loginEx(request, runtime);
    }

    /**
     * 通过手机号+短信验证码注册账号
     * @tags account
     * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
     * @error Forbidden User not authorized to operate on the specified APIs.
     * @error NotFound The resource {resource_name} cannot be found. Please check.
     * @error AlreadyExist {resource} has already exists. {extra_msg}
     * @error InternalError The request has been failed due to some unknown error.
     */
    public RegisterModel register(MobileRegisterRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.registerEx(request, runtime);
    }

    /**
     * 发送短信验证码，用于登录、注册、修改密码、绑定等
     * @tags account
     * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
     * @error Forbidden User not authorized to operate on the specified APIs.
     * @error NotFound The resource {resource_name} cannot be found. Please check.
     * @error InternalError The request has been failed due to some unknown error.
     */
    public MobileSendSmsCodeModel mobileSendSmsCode(MobileSendSmsCodeRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.mobileSendSmsCodeEx(request, runtime);
    }

    /**
     * 用户退出登录
     * @tags account
     * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
     * @error Forbidden User not authorized to operate on the specified APIs.
     * @error NotFound The resource {resource_name} cannot be found. Please check.
     * @error InternalError The request has been failed due to some unknown error.
     */
    public AccountRevokeModel accountRevoke(RevokeRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.accountRevokeEx(request, runtime);
    }

    /**
     * 用户通过刷新令牌（refresh_token）获取访问令牌（access_token）
     * @tags account
     * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
     * @error Forbidden User not authorized to operate on the specified APIs.
     * @error NotFound The resource {resource_name} cannot be found. Please check.
     * @error InternalError The request has been failed due to some unknown error.
     */
    public AccountTokenModel accountToken(TokenRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.accountTokenEx(request, runtime);
    }

    /**
     * 列举Store列表
     * @tags admin
     * @error InvalidParameter The input parameter {parameter_name} is not valid.
     * @error Forbidden User not authorized to operate on the specified APIs.
     * @error InternalError The request has been failed due to some unknown error.
     */
    public AdminListStoresModel adminListStores(AdminListStoresRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.adminListStoresEx(request, runtime);
    }

    /**
     * 获取用户的accessToken
     * @tags admin
     * @error undefined undefined
     * @error undefined undefined
     * @error undefined undefined
     * @error undefined undefined
     * @error undefined undefined
     */
    public GetUserAccessTokenModel getUserAccessToken(GetUserAccessTokenRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.getUserAccessTokenEx(request, runtime);
    }

    /**
     * 如果目录拷贝、目录删除不能在限定时间内完成，将访问一个异步任务id，
     * 通过此接口获取异步任务的信息，以确定任务是否执行成功。
     * @tags async_task
     * @error InvalidParameter The input parameter {parameter_name} is not valid.
     * @error AccessTokenInvalid AccessToken is invalid. {message}
     * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
     * @error NotFound The resource {resource_name} cannot be found. Please check.
     * @error InternalError The request has been failed due to some unknown error.
     * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
     */
    public GetAsyncTaskInfoModel getAsyncTaskInfo(GetAsyncTaskRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.getAsyncTaskInfoEx(request, runtime);
    }

    /**
     * 对多个原子操作封装成一个批处理请求，服务端并行处理并打包返回每个操作的执行结果。
     * 支持对文件和文件夹的移动、删除、修改，每个批处理请求最多包含100个原则操作。
     * @tags batch
     * @error InvalidParameter The input parameter {parameter_name} is not valid.
     * @error AccessTokenInvalid AccessToken is invalid. {message}
     * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
     * @error InternalError The request has been failed due to some unknown error.
     * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
     */
    public BatchOperationModel batchOperation(BatchRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.batchOperationEx(request, runtime);
    }

    /**
     * 支持normal和large两种drive，
     * large类型的drive用于文件数多的场景，不支持list操作，
     * 当drive的文件数量大于1亿时，建议使用large类型。
     * @tags drive
     * @error InvalidParameter The input parameter {parameter_name} is not valid.
     * @error AccessTokenInvalid AccessToken is invalid. {message}
     * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
     * @error InternalError The request has been failed due to some unknown error.
     * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
     */
    public CreateDriveModel createDrive(CreateDriveRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.createDriveEx(request, runtime);
    }

    /**
     * 删除指定drive_id对应的Drive
     * @tags drive
     * @error InvalidParameter The input parameter {parameter_name} is not valid.
     * @error AccessTokenInvalid AccessToken is invalid. {message}
     * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
     * @error InternalError The request has been failed due to some unknown error.
     * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
     */
    public DeleteDriveModel deleteDrive(DeleteDriveRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.deleteDriveEx(request, runtime);
    }

    /**
     * 获取指定drive_id对应的Drive详细信息。
     * @tags drive
     * @error InvalidParameter The input parameter {parameter_name} is not valid.
     * @error AccessTokenInvalid AccessToken is invalid. {message}
     * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
     * @error NotFound The resource {resource_name} cannot be found. Please check.
     * @error InternalError The request has been failed due to some unknown error.
     * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
     */
    public GetDriveModel getDrive(GetDriveRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.getDriveEx(request, runtime);
    }

    /**
     * 一个用户可拥有多个drive，在创建drive时通过参数指定是否为这个用户的默认drive，
     * 每个用户只能设置一个默认drive。
     * @tags drive
     * @error InvalidParameter The input parameter {parameter_name} is not valid.
     * @error AccessTokenInvalid AccessToken is invalid. {message}
     * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
     * @error NotFound The resource {resource_name} cannot be found. Please check.
     * @error InternalError The request has been failed due to some unknown error.
     * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
     */
    public GetDefaultDriveModel getDefaultDrive(GetDefaultDriveRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.getDefaultDriveEx(request, runtime);
    }

    /**
     * 管理员列举指定用户的Drive
     * @tags drive
     * @error InvalidParameter The input parameter {parameter_name} is not valid.
     * @error AccessTokenInvalid AccessToken is invalid. {message}
     * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
     * @error InternalError The request has been failed due to some unknown error.
     * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
     */
    public ListDrivesModel listDrives(ListDriveRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.listDrivesEx(request, runtime);
    }

    /**
     * 列举当前用户（访问令牌）的Drive
     * @tags drive
     * @error InvalidParameter The input parameter {parameter_name} is not valid.
     * @error AccessTokenInvalid AccessToken is invalid. {message}
     * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
     * @error InternalError The request has been failed due to some unknown error.
     * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
     */
    public ListMyDrivesModel listMyDrives(ListMyDriveRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.listMyDrivesEx(request, runtime);
    }

    /**
     * 更新指定drive_id的Drive信息
     * @tags drive
     * @error InvalidParameter The input parameter {parameter_name} is not valid.
     * @error AccessTokenInvalid AccessToken is invalid. {message}
     * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
     * @error NotFound The resource {resource_name} cannot be found. Please check.
     * @error InternalError The request has been failed due to some unknown error.
     * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
     */
    public UpdateDriveModel updateDrive(UpdateDriveRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.updateDriveEx(request, runtime);
    }

    /**
     * 完成文件上传。
     * @tags file
     * @error InvalidParameter The input parameter {parameter_name} is not valid.
     * @error AccessTokenInvalid AccessToken is invalid. {message}
     * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
     * @error NotFound The resource {resource_name} cannot be found. Please check.
     * @error InternalError The request has been failed due to some unknown error.
     * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
     */
    public CompleteFileModel completeFile(CompleteFileRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.completeFileEx(request, runtime);
    }

    /**
     * 指定源文件或文件夹，拷贝到指定的文件夹。
     * @tags file
     * @error InvalidParameter The input parameter {parameter_name} is not valid.
     * @error AccessTokenInvalid AccessToken is invalid. {message}
     * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
     * @error NotFound The resource {resource_name} cannot be found. Please check.
     * @error InternalError The request has been failed due to some unknown error.
     * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
     */
    public CopyFileModel copyFile(CopyFileRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.copyFileEx(request, runtime);
    }

    /**
     * 在指定文件夹下创建文件或者文件夹，
     * 根文件夹用root表示，其他文件夹使用创建文件夹时返回的file_id。
     * @tags file
     * @error InvalidParameter The input parameter {parameter_name} is not valid.
     * @error AccessTokenInvalid AccessToken is invalid. {message}
     * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
     * @error NotFound The resource {resource_name} cannot be found. Please check.
     * @error AlreadyExist {resource} has already exists. {extra_msg}
     * @error InternalError The request has been failed due to some unknown error.
     * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
     */
    public CreateFileModel createFile(CreateFileRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.createFileEx(request, runtime);
    }

    /**
     * 指定文件或文件夹ID，删除文件或者文件夹。
     * @tags file
     * @error InvalidParameter The input parameter {parameter_name} is not valid.
     * @error AccessTokenInvalid AccessToken is invalid. {message}
     * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
     * @error NotFound The resource {resource_name} cannot be found. Please check.
     * @error InternalError The request has been failed due to some unknown error.
     * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
     */
    public DeleteFileModel deleteFile(DeleteFileRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.deleteFileEx(request, runtime);
    }

    /**
     * 获取指定文件或文件夹ID的信息。
     * @tags file
     * @error InvalidParameter The input parameter {parameter_name} is not valid.
     * @error AccessTokenInvalid AccessToken is invalid. {message}
     * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
     * @error NotFound The resource {resource_name} cannot be found. Please check.
     * @error InternalError The request has been failed due to some unknown error.
     * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
     */
    public GetFileModel getFile(GetFileRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.getFileEx(request, runtime);
    }

    /**
     * 根据路径获取指定文件或文件夹的信息。
     * @tags file
     * @error InvalidParameter The input parameter {parameter_name} is not valid.
     * @error AccessTokenInvalid AccessToken is invalid. {message}
     * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
     * @error NotFound The resource {resource_name} cannot be found. Please check.
     * @error InternalError The request has been failed due to some unknown error.
     * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
     */
    public GetFileByPathModel getFileByPath(GetFileByPathRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.getFileByPathEx(request, runtime);
    }

    /**
     * 获取文件的下载地址，调用者可自己设置range头并发下载。
     * @tags file
     * @error InvalidParameter The input parameter {parameter_name} is not valid.
     * @error AccessTokenInvalid AccessToken is invalid. {message}
     * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
     * @error NotFound The resource {resource_name} cannot be found. Please check.
     * @error InternalError The request has been failed due to some unknown error.
     * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
     */
    public GetDownloadUrlModel getDownloadUrl(GetDownloadUrlRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.getDownloadUrlEx(request, runtime);
    }

    /**
     * 获取drive内，增量数据最新的游标
     * @tags file_delta
     * @error InvalidParameter The input parameter {parameter_name} is not valid.
     * @error AccessTokenInvalid AccessToken is invalid. {message}
     * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
     * @error NotFound The resource {resource_name} cannot be found. Please check.
     * @error InternalError The request has been failed due to some unknown error.
     * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
     */
    public GetLastCursorModel getLastCursor(GetLastCursorRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.getLastCursorEx(request, runtime);
    }

    /**
     * 获取media文件播放URL地址（当前仅支持m3u8）
     * @tags file
     * @error InvalidParameter The input parameter {parameter_name} is not valid.
     * @error AccessTokenInvalid AccessToken is invalid. {message}
     * @error NotFound The resource {resource_name} cannot be found. Please check.
     * @error InternalError The request has been failed due to some unknown error.
     * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
     */
    public GetMediaPlayUrlModel getMediaPlayUrl(GetMediaPlayURLRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.getMediaPlayUrlEx(request, runtime);
    }

    /**
     * 获取文档的预览地址（office文档）
     * @tags file
     * @error InvalidParameter The input parameter {parameter_name} is not valid.
     * @error AccessTokenInvalid AccessToken is invalid. {message}
     * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
     * @error NotFound The resource {resource_name} cannot be found. Please check.
     * @error InternalError The request has been failed due to some unknown error.
     * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
     */
    public GetOfficePreviewUrlModel getOfficePreviewUrl(GetOfficePreviewUrlRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.getOfficePreviewUrlEx(request, runtime);
    }

    /**
     * 可指定分片信息，一次获取多个分片的上传地址。
     * @tags file
     * @error InvalidParameter The input parameter {parameter_name} is not valid.
     * @error AccessTokenInvalid AccessToken is invalid. {message}
     * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
     * @error NotFound The resource {resource_name} cannot be found. Please check.
     * @error InternalError The request has been failed due to some unknown error.
     * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
     */
    public GetUploadUrlModel getUploadUrl(GetUploadUrlRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.getUploadUrlEx(request, runtime);
    }

    /**
     * 获取视频雪碧图地址
     * @tags file
     * @error InvalidParameter The input parameter {parameter_name} is not valid.
     * @error AccessTokenInvalid AccessToken is invalid. {message}
     * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
     * @error NotFound The resource {resource_name} cannot be found. Please check.
     * @error InternalError The request has been failed due to some unknown error.
     * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
     */
    public GetVideoPreviewSpriteUrlModel getVideoPreviewSpriteUrl(GetVideoPreviewSpriteURLRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.getVideoPreviewSpriteUrlEx(request, runtime);
    }

    /**
     * 获取视频播放地址
     * @tags file
     * @error InvalidParameter The input parameter {parameter_name} is not valid.
     * @error AccessTokenInvalid AccessToken is invalid. {message}
     * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
     * @error NotFound The resource {resource_name} cannot be found. Please check.
     * @error InternalError The request has been failed due to some unknown error.
     * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
     */
    public GetVideoPreviewUrlModel getVideoPreviewUrl(GetVideoPreviewURLRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.getVideoPreviewUrlEx(request, runtime);
    }

    /**
     * 列举指定目录下的文件或文件夹。
     * @tags file
     * @error InvalidParameter The input parameter {parameter_name} is not valid.
     * @error AccessTokenInvalid AccessToken is invalid. {message}
     * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
     * @error NotFound The resource {resource_name} cannot be found. Please check.
     * @error InternalError The request has been failed due to some unknown error.
     * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
     */
    public ListFileModel listFile(ListFileRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.listFileEx(request, runtime);
    }

    /**
     * 查看分享中的文件列表
     * @tags share_link
     * @error InvalidParameter The input parameter {parameter_name} is not valid.
     * @error ShareLinkTokenInvalid ShareToken is invalid. {message}
     * @error NotFound The resource {resource_name} cannot be found. Please check.
     * @error InternalError The request has been failed due to some unknown error.
     * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
     */
    public ListFileByAnonymousModel listFileByAnonymous(ListByAnonymousRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.listFileByAnonymousEx(request, runtime);
    }

    /**
     * 根据自定义同步索引键列举文件或文件夹。
     * @tags file
     * @error InvalidParameter The input parameter {parameter_name} is not valid.
     * @error AccessTokenInvalid AccessToken is invalid. {message}
     * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
     * @error NotFound The resource {resource_name} cannot be found. Please check.
     * @error InternalError The request has been failed due to some unknown error.
     * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
     */
    public ListFileByCustomIndexKeyModel listFileByCustomIndexKey(ListFileByCustomIndexKeyRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.listFileByCustomIndexKeyEx(request, runtime);
    }

    /**
     * 获取drive内，增量数据列表
     * @tags file_delta
     * @error InvalidParameter The input parameter {parameter_name} is not valid.
     * @error AccessTokenInvalid AccessToken is invalid. {message}
     * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
     * @error NotFound The resource {resource_name} cannot be found. Please check.
     * @error InternalError The request has been failed due to some unknown error.
     * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
     */
    public ListFileDeltaModel listFileDelta(ListFileDeltaRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.listFileDeltaEx(request, runtime);
    }

    /**
     * 列举upload_id对应的已上传分片。
     * @tags file
     * @error InvalidParameter The input parameter {parameter_name} is not valid.
     * @error AccessTokenInvalid AccessToken is invalid. {message}
     * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
     * @error NotFound The resource {resource_name} cannot be found. Please check.
     * @error InternalError The request has been failed due to some unknown error.
     * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
     */
    public ListUploadedPartsModel listUploadedParts(ListUploadedPartRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.listUploadedPartsEx(request, runtime);
    }

    /**
     * 指定源文件或文件夹，移动到指定的文件夹。
     * @tags file
     * @error InvalidParameter The input parameter {parameter_name} is not valid.
     * @error AccessTokenInvalid AccessToken is invalid. {message}
     * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
     * @error NotFound The resource {resource_name} cannot be found. Please check.
     * @error InternalError The request has been failed due to some unknown error.
     * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
     */
    public MoveFileModel moveFile(MoveFileRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.moveFileEx(request, runtime);
    }

    /**
     * 在指定drive下全量获取文件元信息。
     * @tags file
     * @error InvalidParameter The input parameter {parameter_name} is not valid.
     * @error AccessTokenInvalid AccessToken is invalid. {message}
     * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
     * @error NotFound The resource {resource_name} cannot be found. Please check.
     * @error InternalError The request has been failed due to some unknown error.
     * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
     */
    public ScanFileMetaModel scanFileMeta(ScanFileMetaRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.scanFileMetaEx(request, runtime);
    }

    /**
     * 根据筛选条件，在指定drive下搜索文件。
     * @tags file
     * @error InvalidParameter The input parameter {parameter_name} is not valid.
     * @error AccessTokenInvalid AccessToken is invalid. {message}
     * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
     * @error NotFound The resource {resource_name} cannot be found. Please check.
     * @error InternalError The request has been failed due to some unknown error.
     * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
     */
    public SearchFileModel searchFile(SearchFileRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.searchFileEx(request, runtime);
    }

    /**
     * 对指定的文件或文件夹更新信息。
     * @tags file
     * @error InvalidParameter The input parameter {parameter_name} is not valid.
     * @error AccessTokenInvalid AccessToken is invalid. {message}
     * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
     * @error NotFound The resource {resource_name} cannot be found. Please check.
     * @error AlreadyExist {resource} has already exists. {extra_msg}
     * @error InternalError The request has been failed due to some unknown error.
     * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
     */
    public UpdateFileModel updateFile(UpdateFileMetaRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.updateFileEx(request, runtime);
    }

    /**
     * 取消指定分享
     * @tags share_link
     * @error InvalidParameter The input parameter {parameter_name} is not valid.
     * @error AccessTokenInvalid AccessToken is invalid. {message}
     * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
     * @error InternalError The request has been failed due to some unknown error.
     * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
     */
    public CancelShareLinkModel cancelShareLink(CancelShareLinkRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.cancelShareLinkEx(request, runtime);
    }

    /**
     * 创建分享。
     * @tags share_link
     * @error InvalidParameter The input parameter {parameter_name} is not valid.
     * @error AccessTokenInvalid AccessToken is invalid. {message}
     * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
     * @error NotFound The resource {resource_name} cannot be found. Please check.
     * @error InternalError The request has been failed due to some unknown error.
     * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
     */
    public CreateShareLinkModel createShareLink(CreateShareLinkRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.createShareLinkEx(request, runtime);
    }

    /**
     * 使用分享口令换取分享id
     * @tags share_link
     * @error InvalidParameter The input parameter {parameter_name} is not valid.
     * @error AccessTokenInvalid AccessToken is invalid. {message}
     * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
     * @error InternalError The request has been failed due to some unknown error.
     * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
     */
    public GetShareIdModel getShareId(GetShareLinkIDRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.getShareIdEx(request, runtime);
    }

    /**
     * 使用分享码+提取码换取分享token
     * @tags share_link
     * @error InvalidParameter The input parameter {parameter_name} is not valid.
     * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
     * @error InternalError The request has been failed due to some unknown error.
     * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
     */
    public GetShareTokenModel getShareToken(GetShareLinkTokenRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.getShareTokenEx(request, runtime);
    }

    /**
     * 列举指定用户的分享
     * @tags share_link
     * @error InvalidParameter The input parameter {parameter_name} is not valid.
     * @error AccessTokenInvalid AccessToken is invalid. {message}
     * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
     * @error InternalError The request has been failed due to some unknown error.
     * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
     */
    public ListShareLinkModel listShareLink(ListShareLinkRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.listShareLinkEx(request, runtime);
    }

    /**
     * 创建用户，只有管理员可以调用
     * @tags user
     * @error InvalidParameter The input parameter {parameter_name} is not valid.
     * @error AccessTokenInvalid AccessToken is invalid. {message}
     * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
     * @error InternalError The request has been failed due to some unknown error.
     * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
     */
    public CreateUserModel createUser(CreateUserRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.createUserEx(request, runtime);
    }

    /**
     * 只有管理员可以调用
     * @tags user
     * @error InvalidParameter The input parameter {parameter_name} is not valid.
     * @error AccessTokenInvalid AccessToken is invalid. {message}
     * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
     * @error InternalError The request has been failed due to some unknown error.
     * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
     */
    public DeleteUserModel deleteUser(DeleteUserRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.deleteUserEx(request, runtime);
    }

    /**
     * 获取用户详细信息，普通用户只能获取自己的信息，管理员可以获取任意用户的信息。
     * @tags user
     * @error InvalidParameter The input parameter {parameter_name} is not valid.
     * @error AccessTokenInvalid AccessToken is invalid. {message}
     * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
     * @error NotFound The resource {resource_name} cannot be found. Please check.
     * @error InternalError The request has been failed due to some unknown error.
     * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
     */
    public GetUserModel getUser(GetUserRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.getUserEx(request, runtime);
    }

    /**
     * 只有管理员可以调用
     * @tags user
     * @error InvalidParameter The input parameter {parameter_name} is not valid.
     * @error AccessTokenInvalid AccessToken is invalid. {message}
     * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
     * @error InternalError The request has been failed due to some unknown error.
     * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
     */
    public ListUsersModel listUsers(ListUserRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.listUsersEx(request, runtime);
    }

    /**
     * 该接口将会根据条件查询用户，只有管理员可以调用
     * @tags user
     * @error InvalidParameter The input parameter {parameter_name} is not valid.
     * @error AccessTokenInvalid AccessToken is invalid. {message}
     * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
     * @error InternalError The request has been failed due to some unknown error.
     * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
     */
    public SearchUserModel searchUser(SearchUserRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.searchUserEx(request, runtime);
    }

    /**
     * 用户可以修改自己的description，nick_name，avatar；
     * 管理员在用户基础上还可修改status（可以修改任意用户）；
     * 超级管理员在管理员基础上还可修改role（可以修改任意用户）。
     * @tags user
     * @error InvalidParameter The input parameter {parameter_name} is not valid.
     * @error AccessTokenInvalid AccessToken is invalid. {message}
     * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
     * @error NotFound The resource {resource_name} cannot be found. Please check.
     * @error InternalError The request has been failed due to some unknown error.
     * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
     */
    public UpdateUserModel updateUser(UpdateUserRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.updateUserEx(request, runtime);
    }

    /**
     * 该接口将会获取故事列表
     * @tags image
     * @error InvalidParameter The input parameter {parameter_name} is not valid.
     * @error AccessTokenInvalid AccessToken is invalid. {message}
     * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
     * @error NotFound The resource {resource_name} cannot be found. Please check.
     * @error InternalError The request has been failed due to some unknown error.
     * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
     */
    public CreateStoryModel createStory(CreateStoryRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.createStoryEx(request, runtime);
    }

    /**
     * 该接口将返回用户Drive下的云照片个数
     * @tags image
     * @error InvalidParameter The input parameter {parameter_name} is not valid.
     * @error AccessTokenInvalid AccessToken is invalid. {message}
     * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
     * @error NotFound The resource {resource_name} cannot be found. Please check.
     * @error InternalError The request has been failed due to some unknown error.
     * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
     */
    public GetPhotoCountModel getPhotoCount(GetImageCountRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.getPhotoCountEx(request, runtime);
    }

    /**
     * 该接口将会获取故事列表
     * @tags image
     * @error InvalidParameter The input parameter {parameter_name} is not valid.
     * @error AccessTokenInvalid AccessToken is invalid. {message}
     * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
     * @error NotFound The resource {resource_name} cannot be found. Please check.
     * @error InternalError The request has been failed due to some unknown error.
     * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
     */
    public GetStoryDetailModel getStoryDetail(GetStoryDetailRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.getStoryDetailEx(request, runtime);
    }

    /**
     * 该接口将会获取故事生成任务
     * @tags image
     * @error InvalidParameter The input parameter {parameter_name} is not valid.
     * @error AccessTokenInvalid AccessToken is invalid. {message}
     * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
     * @error NotFound The resource {resource_name} cannot be found. Please check.
     * @error InternalError The request has been failed due to some unknown error.
     * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
     */
    public GetStoryTaskModel getStoryTask(GetStoryTaskRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.getStoryTaskEx(request, runtime);
    }

    /**
     * 该接口将会展示用户图片的地点分组
     * @tags image
     * @error InvalidParameter The input parameter {parameter_name} is not valid.
     * @error AccessTokenInvalid AccessToken is invalid. {message}
     * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
     * @error NotFound The resource {resource_name} cannot be found. Please check.
     * @error InternalError The request has been failed due to some unknown error.
     * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
     */
    public ListAddressGroupsModel listAddressGroups(ListImageAddressGroupsRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.listAddressGroupsEx(request, runtime);
    }

    /**
     * 该接口将会列举人脸分组
     * @tags image
     * @error InvalidParameter The input parameter {parameter_name} is not valid.
     * @error AccessTokenInvalid AccessToken is invalid. {message}
     * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
     * @error NotFound The resource {resource_name} cannot be found. Please check.
     * @error InternalError The request has been failed due to some unknown error.
     * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
     */
    public ListFaceGroupsModel listFaceGroups(ListImageFaceGroupsRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.listFaceGroupsEx(request, runtime);
    }

    /**
     * 该接口将会获取故事列表
     * @tags image
     * @error InvalidParameter The input parameter {parameter_name} is not valid.
     * @error AccessTokenInvalid AccessToken is invalid. {message}
     * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
     * @error NotFound The resource {resource_name} cannot be found. Please check.
     * @error InternalError The request has been failed due to some unknown error.
     * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
     */
    public ListStoryModel listStory(ListStoryRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.listStoryEx(request, runtime);
    }

    /**
     * 该接口将会展示场景标记
     * @tags image
     * @error InvalidParameter The input parameter {parameter_name} is not valid.
     * @error AccessTokenInvalid AccessToken is invalid. {message}
     * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
     * @error NotFound The resource {resource_name} cannot be found. Please check.
     * @error InternalError The request has been failed due to some unknown error.
     * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
     */
    public ListTagsModel listTags(ListImageTagsRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.listTagsEx(request, runtime);
    }

    /**
     * 该接口将会展示用户图片的地点分组
     * @tags image
     * @error InvalidParameter The input parameter {parameter_name} is not valid.
     * @error AccessTokenInvalid AccessToken is invalid. {message}
     * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
     * @error NotFound The resource {resource_name} cannot be found. Please check.
     * @error InternalError The request has been failed due to some unknown error.
     * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
     */
    public SearchAddressGroupsModel searchAddressGroups(SearchImageAddressGroupsRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.searchAddressGroupsEx(request, runtime);
    }

    /**
     * 该接口将会更新人脸分组信息
     * @tags image
     * @error InvalidParameter The input parameter {parameter_name} is not valid.
     * @error AccessTokenInvalid AccessToken is invalid. {message}
     * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
     * @error NotFound The resource {resource_name} cannot be found. Please check.
     * @error InternalError The request has been failed due to some unknown error.
     * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
     */
    public UpdateFacegroupInfoModel updateFacegroupInfo(UpdateFaceGroupInfoRequest request) throws Exception {
        RuntimeOptions runtime = new RuntimeOptions();
        return this.updateFacegroupInfoEx(request, runtime);
    }

    public String getPathname(String nickname, String path) throws Exception {
        if (com.aliyun.teautil.Common.empty(nickname)) {
            return path;
        }

        return "/" + nickname + "" + path + "";
    }

    public void setExpireTime(String expireTime) throws Exception {
        if (com.aliyun.teautil.Common.isUnset(_accessTokenCredential)) {
            return ;
        }

        _accessTokenCredential.setExpireTime(expireTime);
    }

    public String getExpireTime() throws Exception {
        if (com.aliyun.teautil.Common.isUnset(_accessTokenCredential)) {
            return "";
        }

        String expireTime = _accessTokenCredential.getExpireTime();
        return expireTime;
    }

    public void setRefreshToken(String token) throws Exception {
        if (com.aliyun.teautil.Common.isUnset(_accessTokenCredential)) {
            return ;
        }

        _accessTokenCredential.setRefreshToken(token);
    }

    public String getRefreshToken() throws Exception {
        if (com.aliyun.teautil.Common.isUnset(_accessTokenCredential)) {
            return "";
        }

        String token = _accessTokenCredential.getRefreshToken();
        return token;
    }

    public void setAccessToken(String token) throws Exception {
        if (com.aliyun.teautil.Common.isUnset(_accessTokenCredential)) {
            return ;
        }

        _accessTokenCredential.setAccessToken(token);
    }

    public String getAccessToken() throws Exception {
        if (com.aliyun.teautil.Common.isUnset(_accessTokenCredential)) {
            return "";
        }

        String token = _accessTokenCredential.getAccessToken();
        return token;
    }

    public void setUserAgent(String userAgent) throws Exception {
        this._userAgent = userAgent;
    }

    public void appendUserAgent(String userAgent) throws Exception {
        this._userAgent = "" + _userAgent + " " + userAgent + "";
    }

    public String getUserAgent() throws Exception {
        String userAgent = com.aliyun.teautil.Common.getUserAgent(_userAgent);
        return userAgent;
    }

    public String getAccessKeyId() throws Exception {
        if (com.aliyun.teautil.Common.isUnset(_credential)) {
            return "";
        }

        String accessKeyId = _credential.getAccessKeyId();
        return accessKeyId;
    }

    public String getAccessKeySecret() throws Exception {
        if (com.aliyun.teautil.Common.isUnset(_credential)) {
            return "";
        }

        String secret = _credential.getAccessKeySecret();
        return secret;
    }

    public String getSecurityToken() throws Exception {
        if (com.aliyun.teautil.Common.isUnset(_credential)) {
            return "";
        }

        String token = _credential.getSecurityToken();
        return token;
    }
}
