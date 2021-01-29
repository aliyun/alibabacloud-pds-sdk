// This file is auto-generated, don't edit it. Thanks.

#include <alibabacloud/pds.hpp>
#include <alibabacloud/access_token_credential.hpp>
#include <alibabacloud/credential.hpp>
#include <alibabacloud/roautil.hpp>
#include <boost/any.hpp>
#include <boost/throw_exception.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>
#include <vector>

using namespace std;

using namespace Alibabacloud_Pds;

Alibabacloud_Pds::Client::Client(const shared_ptr<Config>& config) {
  if (Darabonba_Util::Client::isUnset<Config>(config)) {
    BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, string>({
      {"name", "ParameterMissing"},
      {"message", "'config' can not be unset"}
    })));
  }
  Darabonba_Util::Client::validateModel(config);
  if (!Darabonba_Util::Client::empty(config->accessToken) || !Darabonba_Util::Client::empty(config->refreshToken)) {
    shared_ptr<Alibabacloud_AccessTokenCredential::Config> accessConfig = make_shared<Alibabacloud_AccessTokenCredential::Config>(map<string, boost::any>({
      {"accessToken", !config->accessToken ? boost::any() : boost::any(*config->accessToken)},
      {"endpoint", !config->endpoint ? boost::any() : boost::any(*config->endpoint)},
      {"domainId", !config->domainId ? boost::any() : boost::any(*config->domainId)},
      {"clientId", !config->clientId ? boost::any() : boost::any(*config->clientId)},
      {"refreshToken", !config->refreshToken ? boost::any() : boost::any(*config->refreshToken)},
      {"clientSecret", !config->clientSecret ? boost::any() : boost::any(*config->clientSecret)},
      {"expireTime", !config->expireTime ? boost::any() : boost::any(*config->expireTime)}
    }));
    _accessTokenCredential = make_shared<Alibabacloud_AccessTokenCredential::Client>(accessConfig);
  }
  if (!Darabonba_Util::Client::empty(config->accessKeyId)) {
    if (Darabonba_Util::Client::empty(config->type)) {
      config->type = make_shared<string>("access_key");
    }
    shared_ptr<Alibabacloud_Credential::Config> credentialConfig = make_shared<Alibabacloud_Credential::Config>(map<string, boost::any>({
      {"accessKeyId", !config->accessKeyId ? boost::any() : boost::any(*config->accessKeyId)},
      {"type", !config->type ? boost::any() : boost::any(*config->type)},
      {"accessKeySecret", !config->accessKeySecret ? boost::any() : boost::any(*config->accessKeySecret)},
      {"securityToken", !config->securityToken ? boost::any() : boost::any(*config->securityToken)}
    }));
    _credential = make_shared<Alibabacloud_Credential::Client>(credentialConfig);
  }
  _endpoint = config->endpoint;
  _protocol = config->protocol;
  _userAgent = config->userAgent;
  _nickname = config->nickname;
  _domainId = config->domainId;
};

CancelLinkModel Alibabacloud_Pds::Client::cancelLinkEx(shared_ptr<CancelLinkRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/account/cancel_link")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".auth.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return CancelLinkModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

ConfirmLinkModel Alibabacloud_Pds::Client::confirmLinkEx(shared_ptr<ConfirmLinkRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/account/confirm_link")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".auth.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return ConfirmLinkModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

ChangePasswordModel Alibabacloud_Pds::Client::changePasswordEx(shared_ptr<DefaultChangePasswordRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/account/default/change_password")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".auth.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return ChangePasswordModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

SetPasswordModel Alibabacloud_Pds::Client::setPasswordEx(shared_ptr<DefaultSetPasswordRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/account/default/set_password")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".auth.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(204))) {
        return SetPasswordModel({
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

VerifyCodeModel Alibabacloud_Pds::Client::verifyCodeEx(shared_ptr<VerifyCodeRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/account/default/verify_code")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".auth.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return VerifyCodeModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

GetAccessTokenByLinkInfoModel Alibabacloud_Pds::Client::getAccessTokenByLinkInfoEx(shared_ptr<GetAccessTokenByLinkInfoRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/account/get_access_token_by_link_info")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".auth.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return GetAccessTokenByLinkInfoModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

GetCaptchaModel Alibabacloud_Pds::Client::getCaptchaEx(shared_ptr<GetCaptchaRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/account/get_captcha")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".auth.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return GetCaptchaModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

GetLinkInfoModel Alibabacloud_Pds::Client::getLinkInfoEx(shared_ptr<GetByLinkInfoRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/account/get_link_info")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".auth.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return GetLinkInfoModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

GetLinkInfoByUserIdModel Alibabacloud_Pds::Client::getLinkInfoByUserIdEx(shared_ptr<GetLinkInfoByUserIDRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/account/get_link_info_by_user_id")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".auth.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return GetLinkInfoByUserIdModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

GetPublicKeyModel Alibabacloud_Pds::Client::getPublicKeyEx(shared_ptr<GetPublicKeyRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/account/get_public_key")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".auth.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return GetPublicKeyModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

LinkModel Alibabacloud_Pds::Client::linkEx(shared_ptr<AccountLinkRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/account/link")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".auth.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return LinkModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

CheckExistModel Alibabacloud_Pds::Client::checkExistEx(shared_ptr<MobileCheckExistRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/account/mobile/check_exist")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".auth.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return CheckExistModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

LoginModel Alibabacloud_Pds::Client::loginEx(shared_ptr<MobileLoginRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/account/mobile/login")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".auth.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return LoginModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

RegisterModel Alibabacloud_Pds::Client::registerEx(shared_ptr<MobileRegisterRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/account/mobile/register")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".auth.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return RegisterModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

MobileSendSmsCodeModel Alibabacloud_Pds::Client::mobileSendSmsCodeEx(shared_ptr<MobileSendSmsCodeRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/account/mobile/send_sms_code")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".auth.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return MobileSendSmsCodeModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

AccountRevokeModel Alibabacloud_Pds::Client::accountRevokeEx(shared_ptr<RevokeRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/account/revoke")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".auth.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(204))) {
        return AccountRevokeModel({
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

AccountTokenModel Alibabacloud_Pds::Client::accountTokenEx(shared_ptr<TokenRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/account/token")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".auth.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return AccountTokenModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

AdminListStoresModel Alibabacloud_Pds::Client::adminListStoresEx(shared_ptr<AdminListStoresRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/domain/list_stores")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return AdminListStoresModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

GetUserAccessTokenModel Alibabacloud_Pds::Client::getUserAccessTokenEx(shared_ptr<GetUserAccessTokenRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/user/get_access_token")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return GetUserAccessTokenModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

GetAsyncTaskInfoModel Alibabacloud_Pds::Client::getAsyncTaskInfoEx(shared_ptr<GetAsyncTaskRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/async_task/get")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return GetAsyncTaskInfoModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

BatchOperationModel Alibabacloud_Pds::Client::batchOperationEx(shared_ptr<BatchRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/batch")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return BatchOperationModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

CreateDriveModel Alibabacloud_Pds::Client::createDriveEx(shared_ptr<CreateDriveRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/drive/create")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(201))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return CreateDriveModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

DeleteDriveModel Alibabacloud_Pds::Client::deleteDriveEx(shared_ptr<DeleteDriveRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/drive/delete")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(204))) {
        return DeleteDriveModel({
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

GetDriveModel Alibabacloud_Pds::Client::getDriveEx(shared_ptr<GetDriveRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/drive/get")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return GetDriveModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

GetDefaultDriveModel Alibabacloud_Pds::Client::getDefaultDriveEx(shared_ptr<GetDefaultDriveRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/drive/get_default_drive")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return GetDefaultDriveModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

ListDrivesModel Alibabacloud_Pds::Client::listDrivesEx(shared_ptr<ListDriveRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/drive/list")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return ListDrivesModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

ListMyDrivesModel Alibabacloud_Pds::Client::listMyDrivesEx(shared_ptr<ListMyDriveRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/drive/list_my_drives")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return ListMyDrivesModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

UpdateDriveModel Alibabacloud_Pds::Client::updateDriveEx(shared_ptr<UpdateDriveRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/drive/update")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return UpdateDriveModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

CompleteFileModel Alibabacloud_Pds::Client::completeFileEx(shared_ptr<CompleteFileRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/file/complete")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return CompleteFileModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

CopyFileModel Alibabacloud_Pds::Client::copyFileEx(shared_ptr<CopyFileRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/file/copy")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(201))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return CopyFileModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(202))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return CopyFileModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

CreateFileModel Alibabacloud_Pds::Client::createFileEx(shared_ptr<CreateFileRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/file/create")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(201))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return CreateFileModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

DeleteFileModel Alibabacloud_Pds::Client::deleteFileEx(shared_ptr<DeleteFileRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/file/delete")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(202))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return DeleteFileModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(204))) {
        return DeleteFileModel({
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

GetFileModel Alibabacloud_Pds::Client::getFileEx(shared_ptr<GetFileRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/file/get")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return GetFileModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

GetFileByPathModel Alibabacloud_Pds::Client::getFileByPathEx(shared_ptr<GetFileByPathRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/file/get_by_path")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return GetFileByPathModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

GetDownloadUrlModel Alibabacloud_Pds::Client::getDownloadUrlEx(shared_ptr<GetDownloadUrlRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/file/get_download_url")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return GetDownloadUrlModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

GetLastCursorModel Alibabacloud_Pds::Client::getLastCursorEx(shared_ptr<GetLastCursorRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/file/get_last_cursor")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return GetLastCursorModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

GetMediaPlayUrlModel Alibabacloud_Pds::Client::getMediaPlayUrlEx(shared_ptr<GetMediaPlayURLRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/file/get_media_play_url")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return GetMediaPlayUrlModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

GetOfficeEditUrlModel Alibabacloud_Pds::Client::getOfficeEditUrlEx(shared_ptr<GetOfficeEditUrlRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/file/get_office_edit_url")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return GetOfficeEditUrlModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

GetOfficePreviewUrlModel Alibabacloud_Pds::Client::getOfficePreviewUrlEx(shared_ptr<GetOfficePreviewUrlRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/file/get_office_preview_url")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return GetOfficePreviewUrlModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

GetUploadUrlModel Alibabacloud_Pds::Client::getUploadUrlEx(shared_ptr<GetUploadUrlRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/file/get_upload_url")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return GetUploadUrlModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

GetVideoPreviewSpriteUrlModel Alibabacloud_Pds::Client::getVideoPreviewSpriteUrlEx(shared_ptr<GetVideoPreviewSpriteURLRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/file/get_video_preview_sprite_url")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return GetVideoPreviewSpriteUrlModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

GetVideoPreviewUrlModel Alibabacloud_Pds::Client::getVideoPreviewUrlEx(shared_ptr<GetVideoPreviewURLRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/file/get_video_preview_url")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return GetVideoPreviewUrlModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

ListFileModel Alibabacloud_Pds::Client::listFileEx(shared_ptr<ListFileRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/file/list")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return ListFileModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

ListFileByAnonymousModel Alibabacloud_Pds::Client::listFileByAnonymousEx(shared_ptr<ListByAnonymousRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/file/list_by_anonymous")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return ListFileByAnonymousModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

ListFileByCustomIndexKeyModel Alibabacloud_Pds::Client::listFileByCustomIndexKeyEx(shared_ptr<ListFileByCustomIndexKeyRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/file/list_by_custom_index_key")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return ListFileByCustomIndexKeyModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

ListFileDeltaModel Alibabacloud_Pds::Client::listFileDeltaEx(shared_ptr<ListFileDeltaRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/file/list_delta")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return ListFileDeltaModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

ListUploadedPartsModel Alibabacloud_Pds::Client::listUploadedPartsEx(shared_ptr<ListUploadedPartRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/file/list_uploaded_parts")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return ListUploadedPartsModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

MoveFileModel Alibabacloud_Pds::Client::moveFileEx(shared_ptr<MoveFileRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/file/move")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return MoveFileModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

TokenModel Alibabacloud_Pds::Client::tokenEx(shared_ptr<RefreshOfficeEditTokenRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/file/refresh_office_edit_token")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return TokenModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

ScanFileMetaModel Alibabacloud_Pds::Client::scanFileMetaEx(shared_ptr<ScanFileMetaRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/file/scan")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return ScanFileMetaModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

SearchFileModel Alibabacloud_Pds::Client::searchFileEx(shared_ptr<SearchFileRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/file/search")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return SearchFileModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

UpdateFileModel Alibabacloud_Pds::Client::updateFileEx(shared_ptr<UpdateFileMetaRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/file/update")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return UpdateFileModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

CreateShareModel Alibabacloud_Pds::Client::createShareEx(shared_ptr<CreateShareRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/share/create")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(201))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return CreateShareModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

DeleteShareModel Alibabacloud_Pds::Client::deleteShareEx(shared_ptr<DeleteShareRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/share/delete")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(204))) {
        return DeleteShareModel({
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

GetShareModel Alibabacloud_Pds::Client::getShareEx(shared_ptr<GetShareRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/share/get")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return GetShareModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

ListShareModel Alibabacloud_Pds::Client::listShareEx(shared_ptr<ListShareRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/share/list")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return ListShareModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

UpdateShareModel Alibabacloud_Pds::Client::updateShareEx(shared_ptr<UpdateShareRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/share/update")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return UpdateShareModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

CancelShareLinkModel Alibabacloud_Pds::Client::cancelShareLinkEx(shared_ptr<CancelShareLinkRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/share_link/cancel")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(204))) {
        return CancelShareLinkModel({
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

CreateShareLinkModel Alibabacloud_Pds::Client::createShareLinkEx(shared_ptr<CreateShareLinkRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/share_link/create")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(201))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return CreateShareLinkModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

GetShareByAnonymousModel Alibabacloud_Pds::Client::getShareByAnonymousEx(shared_ptr<GetShareLinkByAnonymousRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/share_link/get_by_anonymous")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return GetShareByAnonymousModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

GetShareIdModel Alibabacloud_Pds::Client::getShareIdEx(shared_ptr<GetShareLinkIDRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/share_link/get_share_id")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return GetShareIdModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

GetShareTokenModel Alibabacloud_Pds::Client::getShareTokenEx(shared_ptr<GetShareLinkTokenRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/share_link/get_share_token")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return GetShareTokenModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

ListShareLinkModel Alibabacloud_Pds::Client::listShareLinkEx(shared_ptr<ListShareLinkRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/share_link/list")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return ListShareLinkModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

CreateUserModel Alibabacloud_Pds::Client::createUserEx(shared_ptr<CreateUserRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/user/create")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(201))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return CreateUserModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

DeleteUserModel Alibabacloud_Pds::Client::deleteUserEx(shared_ptr<DeleteUserRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/user/delete")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(204))) {
        return DeleteUserModel({
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

GetUserModel Alibabacloud_Pds::Client::getUserEx(shared_ptr<GetUserRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/user/get")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return GetUserModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

ListUsersModel Alibabacloud_Pds::Client::listUsersEx(shared_ptr<ListUserRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/user/list")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return ListUsersModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

SearchUserModel Alibabacloud_Pds::Client::searchUserEx(shared_ptr<SearchUserRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/user/search")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return SearchUserModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

UpdateUserModel Alibabacloud_Pds::Client::updateUserEx(shared_ptr<UpdateUserRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/user/update")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return UpdateUserModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

CreateStoryModel Alibabacloud_Pds::Client::createStoryEx(shared_ptr<CreateStoryRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/image/create_story")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return CreateStoryModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

GetPhotoCountModel Alibabacloud_Pds::Client::getPhotoCountEx(shared_ptr<GetImageCountRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/image/get_photo_count")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return GetPhotoCountModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

GetStoryDetailModel Alibabacloud_Pds::Client::getStoryDetailEx(shared_ptr<GetStoryDetailRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/image/get_story_detail")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return GetStoryDetailModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

ListAddressGroupsModel Alibabacloud_Pds::Client::listAddressGroupsEx(shared_ptr<ListImageAddressGroupsRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/image/list_address_groups")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return ListAddressGroupsModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

ListFaceGroupsModel Alibabacloud_Pds::Client::listFaceGroupsEx(shared_ptr<ListImageFaceGroupsRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/image/list_face_groups")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return ListFaceGroupsModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

ListStoryModel Alibabacloud_Pds::Client::listStoryEx(shared_ptr<ListStoryRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/image/list_story")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return ListStoryModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

ListTagsModel Alibabacloud_Pds::Client::listTagsEx(shared_ptr<ListImageTagsRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/image/list_tags")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return ListTagsModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

ParseKeywordsModel Alibabacloud_Pds::Client::parseKeywordsEx(shared_ptr<ParseKeywordsRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/image/parse_keywords")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return ParseKeywordsModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

RemoveStoryImagesModel Alibabacloud_Pds::Client::removeStoryImagesEx(shared_ptr<RemoveStoryImagesRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/image/remove_story_images")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return RemoveStoryImagesModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

SearchAddressGroupsModel Alibabacloud_Pds::Client::searchAddressGroupsEx(shared_ptr<SearchImageAddressGroupsRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/image/search_address_groups")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return SearchAddressGroupsModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

UpdateFacegroupInfoModel Alibabacloud_Pds::Client::updateFacegroupInfoEx(shared_ptr<UpdateFaceGroupInfoRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<map<string, boost::any>>(map<string, boost::any>({
    {"timeouted", boost::any(string("retry"))},
    {"readTimeout", !runtime->readTimeout ? boost::any() : boost::any(*runtime->readTimeout)},
    {"connectTimeout", !runtime->connectTimeout ? boost::any() : boost::any(*runtime->connectTimeout)},
    {"localAddr", !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
    {"httpProxy", !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
    {"httpsProxy", !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
    {"noProxy", !runtime->noProxy ? boost::any() : boost::any(*runtime->noProxy)},
    {"maxIdleConns", !runtime->maxIdleConns ? boost::any() : boost::any(*runtime->maxIdleConns)},
    {"socks5Proxy", !runtime->socks5Proxy ? boost::any() : boost::any(*runtime->socks5Proxy)},
    {"socks5NetWork", !runtime->socks5NetWork ? boost::any() : boost::any(*runtime->socks5NetWork)},
    {"retry", boost::any(map<string, boost::any>({
      {"retryable", !runtime->autoretry ? boost::any() : boost::any(*runtime->autoretry)},
      {"maxAttempts", boost::any(Darabonba_Util::Client::defaultNumber(runtime->maxAttempts, make_shared<int>(3)))}
    }))},
    {"backoff", boost::any(map<string, boost::any>({
      {"policy", boost::any(string(Darabonba_Util::Client::defaultString(runtime->backoffPolicy, make_shared<string>("no"))))},
      {"period", boost::any(Darabonba_Util::Client::defaultNumber(runtime->backoffPeriod, make_shared<int>(1)))}
    }))},
    {"ignoreSSL", !runtime->ignoreSSL ? boost::any() : boost::any(*runtime->ignoreSSL)}
  })
);
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime = make_shared<int>(Darabonba::Core::getBackoffTime(make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ = make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret = make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken = make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq = make_shared<map<string, boost::any>>(Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(_protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(_nickname, make_shared<string>(string("/v2/image/update_facegroup_info")));
      request_->headers = Darabonba::Converter::merge(map<string, string>({
        {"user-agent", getUserAgent()},
        {"host", Darabonba_Util::Client::defaultString(_endpoint, make_shared<string>(string(*_domainId) + string(".api.aliyunpds.com")))},
        {"content-type", "application/json; charset=utf-8"}
      }), !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>("authorization", string("Bearer ") + string(*accessToken)));
      }
      else if (!Darabonba_Util::Client::empty(accesskeyId) && !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>("date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(pair<string, string>("accept", "application/json"));
        request_->headers.insert(pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>("authorization", string("acs ") + string(*accesskeyId) + string(":") + string(Alibabacloud_ROAUtil::Client::getSignature(stringToSign, accessKeySecret))));
      }
      request_->body = Darabonba::Converter::toStream(Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ = make_shared<Darabonba::Response>(Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
        return UpdateFacegroupInfoModel({
          {"body", !respMap ? boost::any() : boost::any(*respMap)},
          {"headers", boost::any(response_->headers)}
        });
      }
      if (!Darabonba_Util::Client::empty(make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>({
          {"data", boost::any(map<string, boost::any>({
            {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
            {"statusCode", boost::any(response_->statusCode)},
            {"statusMessage", boost::any(string(response_->statusMessage))}
          }))},
          {"message", boost::any(string(response_->headers["x-ca-error-message"]))}
        })));
      }
      obj = make_shared<boost::any>(Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(map<string, boost::any>({
        {"data", boost::any(map<string, boost::any>({
          {"requestId", boost::any(string(response_->headers["x-ca-request-id"]))},
          {"statusCode", boost::any(response_->statusCode)},
          {"statusMessage", boost::any(string(response_->statusMessage))}
        }))}
      }), !respMap ? map<string, boost::any>() : *respMap))));
    }
    catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(Darabonba::UnretryableError(_lastRequest, _lastException));
}

CancelLinkModel Alibabacloud_Pds::Client::cancelLink(shared_ptr<CancelLinkRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return cancelLinkEx(request, runtime);
}

ConfirmLinkModel Alibabacloud_Pds::Client::confirmLink(shared_ptr<ConfirmLinkRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return confirmLinkEx(request, runtime);
}

ChangePasswordModel Alibabacloud_Pds::Client::changePassword(shared_ptr<DefaultChangePasswordRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return changePasswordEx(request, runtime);
}

SetPasswordModel Alibabacloud_Pds::Client::setPassword(shared_ptr<DefaultSetPasswordRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return setPasswordEx(request, runtime);
}

VerifyCodeModel Alibabacloud_Pds::Client::verifyCode(shared_ptr<VerifyCodeRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return verifyCodeEx(request, runtime);
}

GetAccessTokenByLinkInfoModel Alibabacloud_Pds::Client::getAccessTokenByLinkInfo(shared_ptr<GetAccessTokenByLinkInfoRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return getAccessTokenByLinkInfoEx(request, runtime);
}

GetCaptchaModel Alibabacloud_Pds::Client::getCaptcha(shared_ptr<GetCaptchaRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return getCaptchaEx(request, runtime);
}

GetLinkInfoModel Alibabacloud_Pds::Client::getLinkInfo(shared_ptr<GetByLinkInfoRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return getLinkInfoEx(request, runtime);
}

GetLinkInfoByUserIdModel Alibabacloud_Pds::Client::getLinkInfoByUserId(shared_ptr<GetLinkInfoByUserIDRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return getLinkInfoByUserIdEx(request, runtime);
}

GetPublicKeyModel Alibabacloud_Pds::Client::getPublicKey(shared_ptr<GetPublicKeyRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return getPublicKeyEx(request, runtime);
}

LinkModel Alibabacloud_Pds::Client::link(shared_ptr<AccountLinkRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return linkEx(request, runtime);
}

CheckExistModel Alibabacloud_Pds::Client::checkExist(shared_ptr<MobileCheckExistRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return checkExistEx(request, runtime);
}

LoginModel Alibabacloud_Pds::Client::login(shared_ptr<MobileLoginRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return loginEx(request, runtime);
}

RegisterModel Alibabacloud_Pds::Client::register_(shared_ptr<MobileRegisterRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return registerEx(request, runtime);
}

MobileSendSmsCodeModel Alibabacloud_Pds::Client::mobileSendSmsCode(shared_ptr<MobileSendSmsCodeRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return mobileSendSmsCodeEx(request, runtime);
}

AccountRevokeModel Alibabacloud_Pds::Client::accountRevoke(shared_ptr<RevokeRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return accountRevokeEx(request, runtime);
}

AccountTokenModel Alibabacloud_Pds::Client::accountToken(shared_ptr<TokenRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return accountTokenEx(request, runtime);
}

AdminListStoresModel Alibabacloud_Pds::Client::adminListStores(shared_ptr<AdminListStoresRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return adminListStoresEx(request, runtime);
}

GetUserAccessTokenModel Alibabacloud_Pds::Client::getUserAccessToken(shared_ptr<GetUserAccessTokenRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return getUserAccessTokenEx(request, runtime);
}

GetAsyncTaskInfoModel Alibabacloud_Pds::Client::getAsyncTaskInfo(shared_ptr<GetAsyncTaskRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return getAsyncTaskInfoEx(request, runtime);
}

BatchOperationModel Alibabacloud_Pds::Client::batchOperation(shared_ptr<BatchRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return batchOperationEx(request, runtime);
}

CreateDriveModel Alibabacloud_Pds::Client::createDrive(shared_ptr<CreateDriveRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return createDriveEx(request, runtime);
}

DeleteDriveModel Alibabacloud_Pds::Client::deleteDrive(shared_ptr<DeleteDriveRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return deleteDriveEx(request, runtime);
}

GetDriveModel Alibabacloud_Pds::Client::getDrive(shared_ptr<GetDriveRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return getDriveEx(request, runtime);
}

GetDefaultDriveModel Alibabacloud_Pds::Client::getDefaultDrive(shared_ptr<GetDefaultDriveRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return getDefaultDriveEx(request, runtime);
}

ListDrivesModel Alibabacloud_Pds::Client::listDrives(shared_ptr<ListDriveRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return listDrivesEx(request, runtime);
}

ListMyDrivesModel Alibabacloud_Pds::Client::listMyDrives(shared_ptr<ListMyDriveRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return listMyDrivesEx(request, runtime);
}

UpdateDriveModel Alibabacloud_Pds::Client::updateDrive(shared_ptr<UpdateDriveRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return updateDriveEx(request, runtime);
}

CompleteFileModel Alibabacloud_Pds::Client::completeFile(shared_ptr<CompleteFileRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return completeFileEx(request, runtime);
}

CopyFileModel Alibabacloud_Pds::Client::copyFile(shared_ptr<CopyFileRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return copyFileEx(request, runtime);
}

CreateFileModel Alibabacloud_Pds::Client::createFile(shared_ptr<CreateFileRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return createFileEx(request, runtime);
}

DeleteFileModel Alibabacloud_Pds::Client::deleteFile(shared_ptr<DeleteFileRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return deleteFileEx(request, runtime);
}

GetFileModel Alibabacloud_Pds::Client::getFile(shared_ptr<GetFileRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return getFileEx(request, runtime);
}

GetFileByPathModel Alibabacloud_Pds::Client::getFileByPath(shared_ptr<GetFileByPathRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return getFileByPathEx(request, runtime);
}

GetDownloadUrlModel Alibabacloud_Pds::Client::getDownloadUrl(shared_ptr<GetDownloadUrlRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return getDownloadUrlEx(request, runtime);
}

GetLastCursorModel Alibabacloud_Pds::Client::getLastCursor(shared_ptr<GetLastCursorRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return getLastCursorEx(request, runtime);
}

GetMediaPlayUrlModel Alibabacloud_Pds::Client::getMediaPlayUrl(shared_ptr<GetMediaPlayURLRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return getMediaPlayUrlEx(request, runtime);
}

GetOfficeEditUrlModel Alibabacloud_Pds::Client::getOfficeEditUrl(shared_ptr<GetOfficeEditUrlRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return getOfficeEditUrlEx(request, runtime);
}

GetOfficePreviewUrlModel Alibabacloud_Pds::Client::getOfficePreviewUrl(shared_ptr<GetOfficePreviewUrlRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return getOfficePreviewUrlEx(request, runtime);
}

GetUploadUrlModel Alibabacloud_Pds::Client::getUploadUrl(shared_ptr<GetUploadUrlRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return getUploadUrlEx(request, runtime);
}

GetVideoPreviewSpriteUrlModel Alibabacloud_Pds::Client::getVideoPreviewSpriteUrl(shared_ptr<GetVideoPreviewSpriteURLRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return getVideoPreviewSpriteUrlEx(request, runtime);
}

GetVideoPreviewUrlModel Alibabacloud_Pds::Client::getVideoPreviewUrl(shared_ptr<GetVideoPreviewURLRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return getVideoPreviewUrlEx(request, runtime);
}

ListFileModel Alibabacloud_Pds::Client::listFile(shared_ptr<ListFileRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return listFileEx(request, runtime);
}

ListFileByAnonymousModel Alibabacloud_Pds::Client::listFileByAnonymous(shared_ptr<ListByAnonymousRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return listFileByAnonymousEx(request, runtime);
}

ListFileByCustomIndexKeyModel Alibabacloud_Pds::Client::listFileByCustomIndexKey(shared_ptr<ListFileByCustomIndexKeyRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return listFileByCustomIndexKeyEx(request, runtime);
}

ListFileDeltaModel Alibabacloud_Pds::Client::listFileDelta(shared_ptr<ListFileDeltaRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return listFileDeltaEx(request, runtime);
}

ListUploadedPartsModel Alibabacloud_Pds::Client::listUploadedParts(shared_ptr<ListUploadedPartRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return listUploadedPartsEx(request, runtime);
}

MoveFileModel Alibabacloud_Pds::Client::moveFile(shared_ptr<MoveFileRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return moveFileEx(request, runtime);
}

TokenModel Alibabacloud_Pds::Client::token(shared_ptr<RefreshOfficeEditTokenRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return tokenEx(request, runtime);
}

ScanFileMetaModel Alibabacloud_Pds::Client::scanFileMeta(shared_ptr<ScanFileMetaRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return scanFileMetaEx(request, runtime);
}

SearchFileModel Alibabacloud_Pds::Client::searchFile(shared_ptr<SearchFileRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return searchFileEx(request, runtime);
}

UpdateFileModel Alibabacloud_Pds::Client::updateFile(shared_ptr<UpdateFileMetaRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return updateFileEx(request, runtime);
}

CreateShareModel Alibabacloud_Pds::Client::createShare(shared_ptr<CreateShareRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return createShareEx(request, runtime);
}

DeleteShareModel Alibabacloud_Pds::Client::deleteShare(shared_ptr<DeleteShareRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return deleteShareEx(request, runtime);
}

GetShareModel Alibabacloud_Pds::Client::getShare(shared_ptr<GetShareRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return getShareEx(request, runtime);
}

ListShareModel Alibabacloud_Pds::Client::listShare(shared_ptr<ListShareRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return listShareEx(request, runtime);
}

UpdateShareModel Alibabacloud_Pds::Client::updateShare(shared_ptr<UpdateShareRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return updateShareEx(request, runtime);
}

CancelShareLinkModel Alibabacloud_Pds::Client::cancelShareLink(shared_ptr<CancelShareLinkRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return cancelShareLinkEx(request, runtime);
}

CreateShareLinkModel Alibabacloud_Pds::Client::createShareLink(shared_ptr<CreateShareLinkRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return createShareLinkEx(request, runtime);
}

GetShareByAnonymousModel Alibabacloud_Pds::Client::getShareByAnonymous(shared_ptr<GetShareLinkByAnonymousRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return getShareByAnonymousEx(request, runtime);
}

GetShareIdModel Alibabacloud_Pds::Client::getShareId(shared_ptr<GetShareLinkIDRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return getShareIdEx(request, runtime);
}

GetShareTokenModel Alibabacloud_Pds::Client::getShareToken(shared_ptr<GetShareLinkTokenRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return getShareTokenEx(request, runtime);
}

ListShareLinkModel Alibabacloud_Pds::Client::listShareLink(shared_ptr<ListShareLinkRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return listShareLinkEx(request, runtime);
}

CreateUserModel Alibabacloud_Pds::Client::createUser(shared_ptr<CreateUserRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return createUserEx(request, runtime);
}

DeleteUserModel Alibabacloud_Pds::Client::deleteUser(shared_ptr<DeleteUserRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return deleteUserEx(request, runtime);
}

GetUserModel Alibabacloud_Pds::Client::getUser(shared_ptr<GetUserRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return getUserEx(request, runtime);
}

ListUsersModel Alibabacloud_Pds::Client::listUsers(shared_ptr<ListUserRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return listUsersEx(request, runtime);
}

SearchUserModel Alibabacloud_Pds::Client::searchUser(shared_ptr<SearchUserRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return searchUserEx(request, runtime);
}

UpdateUserModel Alibabacloud_Pds::Client::updateUser(shared_ptr<UpdateUserRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return updateUserEx(request, runtime);
}

CreateStoryModel Alibabacloud_Pds::Client::createStory(shared_ptr<CreateStoryRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return createStoryEx(request, runtime);
}

GetPhotoCountModel Alibabacloud_Pds::Client::getPhotoCount(shared_ptr<GetImageCountRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return getPhotoCountEx(request, runtime);
}

GetStoryDetailModel Alibabacloud_Pds::Client::getStoryDetail(shared_ptr<GetStoryDetailRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return getStoryDetailEx(request, runtime);
}

ListAddressGroupsModel Alibabacloud_Pds::Client::listAddressGroups(shared_ptr<ListImageAddressGroupsRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return listAddressGroupsEx(request, runtime);
}

ListFaceGroupsModel Alibabacloud_Pds::Client::listFaceGroups(shared_ptr<ListImageFaceGroupsRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return listFaceGroupsEx(request, runtime);
}

ListStoryModel Alibabacloud_Pds::Client::listStory(shared_ptr<ListStoryRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return listStoryEx(request, runtime);
}

ListTagsModel Alibabacloud_Pds::Client::listTags(shared_ptr<ListImageTagsRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return listTagsEx(request, runtime);
}

ParseKeywordsModel Alibabacloud_Pds::Client::parseKeywords(shared_ptr<ParseKeywordsRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return parseKeywordsEx(request, runtime);
}

RemoveStoryImagesModel Alibabacloud_Pds::Client::removeStoryImages(shared_ptr<RemoveStoryImagesRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return removeStoryImagesEx(request, runtime);
}

SearchAddressGroupsModel Alibabacloud_Pds::Client::searchAddressGroups(shared_ptr<SearchImageAddressGroupsRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return searchAddressGroupsEx(request, runtime);
}

UpdateFacegroupInfoModel Alibabacloud_Pds::Client::updateFacegroupInfo(shared_ptr<UpdateFaceGroupInfoRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return updateFacegroupInfoEx(request, runtime);
}

string Alibabacloud_Pds::Client::getPathname(shared_ptr<string> nickname, shared_ptr<string> path) {
  if (Darabonba_Util::Client::empty(nickname)) {
    return *path;
  }
  return string("/") + string(*nickname) + string(*path);
}

void Alibabacloud_Pds::Client::setExpireTime(shared_ptr<string> expireTime) {
  if (Darabonba_Util::Client::isUnset<Alibabacloud_AccessTokenCredential::Client>(_accessTokenCredential)) {
    return;
  }
  _accessTokenCredential->setExpireTime(expireTime);
}

string Alibabacloud_Pds::Client::getExpireTime() {
  if (Darabonba_Util::Client::isUnset<Alibabacloud_AccessTokenCredential::Client>(_accessTokenCredential)) {
    return string("");
  }
  shared_ptr<string> expireTime = make_shared<string>(_accessTokenCredential->getExpireTime());
  return *expireTime;
}

void Alibabacloud_Pds::Client::setRefreshToken(shared_ptr<string> token) {
  if (Darabonba_Util::Client::isUnset<Alibabacloud_AccessTokenCredential::Client>(_accessTokenCredential)) {
    return;
  }
  _accessTokenCredential->setRefreshToken(token);
}

string Alibabacloud_Pds::Client::getRefreshToken() {
  if (Darabonba_Util::Client::isUnset<Alibabacloud_AccessTokenCredential::Client>(_accessTokenCredential)) {
    return string("");
  }
  shared_ptr<string> token = make_shared<string>(_accessTokenCredential->getRefreshToken());
  return *token;
}

void Alibabacloud_Pds::Client::setAccessToken(shared_ptr<string> token) {
  if (Darabonba_Util::Client::isUnset<Alibabacloud_AccessTokenCredential::Client>(_accessTokenCredential)) {
    return;
  }
  _accessTokenCredential->setAccessToken(token);
}

string Alibabacloud_Pds::Client::getAccessToken() {
  if (Darabonba_Util::Client::isUnset<Alibabacloud_AccessTokenCredential::Client>(_accessTokenCredential)) {
    return string("");
  }
  shared_ptr<string> token = make_shared<string>(_accessTokenCredential->getAccessToken());
  return *token;
}

void Alibabacloud_Pds::Client::setUserAgent(shared_ptr<string> userAgent) {
  _userAgent = userAgent;
}

void Alibabacloud_Pds::Client::appendUserAgent(shared_ptr<string> userAgent) {
  _userAgent = make_shared<string>(string(*_userAgent) + string(" ") + string(*userAgent));
}

string Alibabacloud_Pds::Client::getUserAgent() {
  shared_ptr<string> userAgent = make_shared<string>(Darabonba_Util::Client::getUserAgent(_userAgent));
  return *userAgent;
}

string Alibabacloud_Pds::Client::getAccessKeyId() {
  if (Darabonba_Util::Client::isUnset<Alibabacloud_Credential::Client>(_credential)) {
    return string("");
  }
  shared_ptr<string> accessKeyId = make_shared<string>(_credential->getAccessKeyId());
  return *accessKeyId;
}

string Alibabacloud_Pds::Client::getAccessKeySecret() {
  if (Darabonba_Util::Client::isUnset<Alibabacloud_Credential::Client>(_credential)) {
    return string("");
  }
  shared_ptr<string> secret = make_shared<string>(_credential->getAccessKeySecret());
  return *secret;
}

string Alibabacloud_Pds::Client::getSecurityToken() {
  if (Darabonba_Util::Client::isUnset<Alibabacloud_Credential::Client>(_credential)) {
    return string("");
  }
  shared_ptr<string> token = make_shared<string>(_credential->getSecurityToken());
  return *token;
}

