// This file is auto-generated, don't edit it. Thanks.

#include <alibabacloud/access_token_credential.hpp>
#include <alibabacloud/credential.hpp>
#include <alibabacloud/hosting.hpp>
#include <alibabacloud/roautil.hpp>
#include <boost/any.hpp>
#include <boost/lexical_cast.hpp>
#include <boost/throw_exception.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>
#include <vector>

using namespace std;

using namespace Alibabacloud_Hosting;

Alibabacloud_Hosting::Client::Client(const shared_ptr<Config> &config) {
  if (Darabonba_Util::Client::isUnset<Config>(config)) {
    BOOST_THROW_EXCEPTION(Darabonba::Error(
        map<string, string>({{"name", "ParameterMissing"},
                             {"message", "'config' can not be unset"}})));
  }
  Darabonba_Util::Client::validateModel(config);
  if (!Darabonba_Util::Client::empty(config->accessToken) ||
      !Darabonba_Util::Client::empty(config->refreshToken)) {
    shared_ptr<Alibabacloud_AccessTokenCredential::Config> accessConfig =
        make_shared<Alibabacloud_AccessTokenCredential::Config>(map<string,
                                                                    boost::any>(
            {{"accessToken", !config->accessToken
                                 ? boost::any()
                                 : boost::any(*config->accessToken)},
             {"endpoint",
              !config->endpoint ? boost::any() : boost::any(*config->endpoint)},
             {"domainId",
              !config->domainId ? boost::any() : boost::any(*config->domainId)},
             {"clientId",
              !config->clientId ? boost::any() : boost::any(*config->clientId)},
             {"refreshToken", !config->refreshToken
                                  ? boost::any()
                                  : boost::any(*config->refreshToken)},
             {"clientSecret", !config->clientSecret
                                  ? boost::any()
                                  : boost::any(*config->clientSecret)},
             {"expireTime", !config->expireTime
                                ? boost::any()
                                : boost::any(*config->expireTime)}}));
    _accessTokenCredential =
        make_shared<Alibabacloud_AccessTokenCredential::Client>(accessConfig);
  }
  if (!Darabonba_Util::Client::empty(config->accessKeyId)) {
    if (Darabonba_Util::Client::empty(config->type)) {
      config->type = make_shared<string>("access_key");
    }
    shared_ptr<Alibabacloud_Credential::Config> credentialConfig =
        make_shared<Alibabacloud_Credential::Config>(map<string, boost::any>(
            {{"accessKeyId", !config->accessKeyId
                                 ? boost::any()
                                 : boost::any(*config->accessKeyId)},
             {"type", !config->type ? boost::any() : boost::any(*config->type)},
             {"accessKeySecret", !config->accessKeySecret
                                     ? boost::any()
                                     : boost::any(*config->accessKeySecret)},
             {"securityToken", !config->securityToken
                                   ? boost::any()
                                   : boost::any(*config->securityToken)}}));
    _credential =
        make_shared<Alibabacloud_Credential::Client>(credentialConfig);
  }
  _endpoint = config->endpoint;
  _protocol = config->protocol;
  _userAgent = config->userAgent;
  _nickname = config->nickname;
  _domainId = config->domainId;
};

CancelLinkModel Alibabacloud_Hosting::Client::cancelLinkEx(
    shared_ptr<CancelLinkRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<
      map<string, boost::any>>(map<string, boost::any>(
      {{"timeouted", boost::any(string("retry"))},
       {"readTimeout", !runtime->readTimeout
                           ? boost::any()
                           : boost::any(*runtime->readTimeout)},
       {"connectTimeout", !runtime->connectTimeout
                              ? boost::any()
                              : boost::any(*runtime->connectTimeout)},
       {"localAddr",
        !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
       {"httpProxy",
        !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
       {"httpsProxy",
        !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
       {"noProxy", !runtime->noProxy ? boost::any()
                                     : boost::any(*runtime->noProxy)},
       {"maxIdleConns", !runtime->maxIdleConns
                            ? boost::any()
                            : boost::any(*runtime->maxIdleConns)},
       {"socks5Proxy", !runtime->socks5Proxy
                           ? boost::any()
                           : boost::any(*runtime->socks5Proxy)},
       {"socks5NetWork", !runtime->socks5NetWork
                             ? boost::any()
                             : boost::any(*runtime->socks5NetWork)},
       {"retry", boost::any(map<string, boost::any>(
                     {{"retryable", !runtime->autoretry
                                        ? boost::any()
                                        : boost::any(*runtime->autoretry)},
                      {"maxAttempts",
                       boost::any(Darabonba_Util::Client::defaultNumber(
                           runtime->maxAttempts, make_shared<int>(3)))}}))},
       {"backoff",
        boost::any(map<string, boost::any>(
            {{"policy",
              boost::any(string(Darabonba_Util::Client::defaultString(
                  runtime->backoffPolicy, make_shared<string>("no"))))},
             {"period", boost::any(Darabonba_Util::Client::defaultNumber(
                            runtime->backoffPeriod, make_shared<int>(1)))}}))},
       {"ignoreSSL", !runtime->ignoreSSL ? boost::any()
                                         : boost::any(*runtime->ignoreSSL)}}));
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(
      make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime =
          make_shared<int>(Darabonba::Core::getBackoffTime(
              make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ =
          make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret =
          make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken =
          make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq =
          make_shared<map<string, boost::any>>(
              Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(
          _protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(
          _nickname, make_shared<string>(string("/v2/account/cancel_link")));
      request_->headers = Darabonba::Converter::merge(
          map<string, string>(
              {{"user-agent", getUserAgent()},
               {"host",
                Darabonba_Util::Client::defaultString(
                    _endpoint, make_shared<string>(string(
                                   "" + *_domainId + ".auth.aliyunpds.com")))},
               {"content-type", "application/json; charset=utf-8"}}),
          !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>(
            "authorization", string("Bearer " + *accessToken + "")));
      } else if (!Darabonba_Util::Client::empty(accesskeyId) &&
                 !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(
              pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>(
            "date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(
            pair<string, string>("accept", "application/json"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(
            Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>(
            "authorization", string("acs " + *accesskeyId + ":" +
                                    Alibabacloud_ROAUtil::Client::getSignature(
                                        stringToSign, accessKeySecret) +
                                    "")));
      }
      request_->body = Darabonba::Converter::toStream(
          Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ =
          make_shared<Darabonba::Response>(
              Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(
              make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(
            Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(
            Darabonba_Util::Client::assertAsMap(obj));
        return CancelLinkModel(
            {{"body", !respMap ? boost::any() : boost::any(*respMap)},
             {"headers", boost::any(response_->headers)}});
      }
      if (!Darabonba_Util::Client::empty(
              make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(
            {{"data",
              boost::any(map<string, boost::any>(
                  {{"requestId",
                    boost::any(string(response_->headers["x-ca-request-id"]))},
                   {"statusCode", boost::any(response_->statusCode)},
                   {"statusMessage",
                    boost::any(string(response_->statusMessage))}}))},
             {"message",
              boost::any(string(response_->headers["x-ca-error-message"]))}})));
      }
      obj = make_shared<boost::any>(
          Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(
          Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(
          Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(
              map<string, boost::any>(
                  {{"data",
                    boost::any(map<string, boost::any>(
                        {{"requestId",
                          boost::any(
                              string(response_->headers["x-ca-request-id"]))},
                         {"statusCode", boost::any(response_->statusCode)},
                         {"statusMessage",
                          boost::any(string(response_->statusMessage))}}))}}),
              !respMap ? map<string, boost::any>() : *respMap))));
    } catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(
      Darabonba::UnretryableError(_lastRequest, _lastException));
}

ConfirmLinkModel Alibabacloud_Hosting::Client::confirmLinkEx(
    shared_ptr<ConfirmLinkRequest> request,
    shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<
      map<string, boost::any>>(map<string, boost::any>(
      {{"timeouted", boost::any(string("retry"))},
       {"readTimeout", !runtime->readTimeout
                           ? boost::any()
                           : boost::any(*runtime->readTimeout)},
       {"connectTimeout", !runtime->connectTimeout
                              ? boost::any()
                              : boost::any(*runtime->connectTimeout)},
       {"localAddr",
        !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
       {"httpProxy",
        !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
       {"httpsProxy",
        !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
       {"noProxy", !runtime->noProxy ? boost::any()
                                     : boost::any(*runtime->noProxy)},
       {"maxIdleConns", !runtime->maxIdleConns
                            ? boost::any()
                            : boost::any(*runtime->maxIdleConns)},
       {"socks5Proxy", !runtime->socks5Proxy
                           ? boost::any()
                           : boost::any(*runtime->socks5Proxy)},
       {"socks5NetWork", !runtime->socks5NetWork
                             ? boost::any()
                             : boost::any(*runtime->socks5NetWork)},
       {"retry", boost::any(map<string, boost::any>(
                     {{"retryable", !runtime->autoretry
                                        ? boost::any()
                                        : boost::any(*runtime->autoretry)},
                      {"maxAttempts",
                       boost::any(Darabonba_Util::Client::defaultNumber(
                           runtime->maxAttempts, make_shared<int>(3)))}}))},
       {"backoff",
        boost::any(map<string, boost::any>(
            {{"policy",
              boost::any(string(Darabonba_Util::Client::defaultString(
                  runtime->backoffPolicy, make_shared<string>("no"))))},
             {"period", boost::any(Darabonba_Util::Client::defaultNumber(
                            runtime->backoffPeriod, make_shared<int>(1)))}}))},
       {"ignoreSSL", !runtime->ignoreSSL ? boost::any()
                                         : boost::any(*runtime->ignoreSSL)}}));
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(
      make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime =
          make_shared<int>(Darabonba::Core::getBackoffTime(
              make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ =
          make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret =
          make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken =
          make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq =
          make_shared<map<string, boost::any>>(
              Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(
          _protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(
          _nickname, make_shared<string>(string("/v2/account/confirm_link")));
      request_->headers = Darabonba::Converter::merge(
          map<string, string>(
              {{"user-agent", getUserAgent()},
               {"host",
                Darabonba_Util::Client::defaultString(
                    _endpoint, make_shared<string>(string(
                                   "" + *_domainId + ".auth.aliyunpds.com")))},
               {"content-type", "application/json; charset=utf-8"}}),
          !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>(
            "authorization", string("Bearer " + *accessToken + "")));
      } else if (!Darabonba_Util::Client::empty(accesskeyId) &&
                 !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(
              pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>(
            "date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(
            pair<string, string>("accept", "application/json"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(
            Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>(
            "authorization", string("acs " + *accesskeyId + ":" +
                                    Alibabacloud_ROAUtil::Client::getSignature(
                                        stringToSign, accessKeySecret) +
                                    "")));
      }
      request_->body = Darabonba::Converter::toStream(
          Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ =
          make_shared<Darabonba::Response>(
              Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(
              make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(
            Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(
            Darabonba_Util::Client::assertAsMap(obj));
        return ConfirmLinkModel(
            {{"body", !respMap ? boost::any() : boost::any(*respMap)},
             {"headers", boost::any(response_->headers)}});
      }
      if (!Darabonba_Util::Client::empty(
              make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(
            {{"data",
              boost::any(map<string, boost::any>(
                  {{"requestId",
                    boost::any(string(response_->headers["x-ca-request-id"]))},
                   {"statusCode", boost::any(response_->statusCode)},
                   {"statusMessage",
                    boost::any(string(response_->statusMessage))}}))},
             {"message",
              boost::any(string(response_->headers["x-ca-error-message"]))}})));
      }
      obj = make_shared<boost::any>(
          Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(
          Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(
          Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(
              map<string, boost::any>(
                  {{"data",
                    boost::any(map<string, boost::any>(
                        {{"requestId",
                          boost::any(
                              string(response_->headers["x-ca-request-id"]))},
                         {"statusCode", boost::any(response_->statusCode)},
                         {"statusMessage",
                          boost::any(string(response_->statusMessage))}}))}}),
              !respMap ? map<string, boost::any>() : *respMap))));
    } catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(
      Darabonba::UnretryableError(_lastRequest, _lastException));
}

ChangePasswordModel Alibabacloud_Hosting::Client::changePasswordEx(
    shared_ptr<DefaultChangePasswordRequest> request,
    shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<
      map<string, boost::any>>(map<string, boost::any>(
      {{"timeouted", boost::any(string("retry"))},
       {"readTimeout", !runtime->readTimeout
                           ? boost::any()
                           : boost::any(*runtime->readTimeout)},
       {"connectTimeout", !runtime->connectTimeout
                              ? boost::any()
                              : boost::any(*runtime->connectTimeout)},
       {"localAddr",
        !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
       {"httpProxy",
        !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
       {"httpsProxy",
        !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
       {"noProxy", !runtime->noProxy ? boost::any()
                                     : boost::any(*runtime->noProxy)},
       {"maxIdleConns", !runtime->maxIdleConns
                            ? boost::any()
                            : boost::any(*runtime->maxIdleConns)},
       {"socks5Proxy", !runtime->socks5Proxy
                           ? boost::any()
                           : boost::any(*runtime->socks5Proxy)},
       {"socks5NetWork", !runtime->socks5NetWork
                             ? boost::any()
                             : boost::any(*runtime->socks5NetWork)},
       {"retry", boost::any(map<string, boost::any>(
                     {{"retryable", !runtime->autoretry
                                        ? boost::any()
                                        : boost::any(*runtime->autoretry)},
                      {"maxAttempts",
                       boost::any(Darabonba_Util::Client::defaultNumber(
                           runtime->maxAttempts, make_shared<int>(3)))}}))},
       {"backoff",
        boost::any(map<string, boost::any>(
            {{"policy",
              boost::any(string(Darabonba_Util::Client::defaultString(
                  runtime->backoffPolicy, make_shared<string>("no"))))},
             {"period", boost::any(Darabonba_Util::Client::defaultNumber(
                            runtime->backoffPeriod, make_shared<int>(1)))}}))},
       {"ignoreSSL", !runtime->ignoreSSL ? boost::any()
                                         : boost::any(*runtime->ignoreSSL)}}));
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(
      make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime =
          make_shared<int>(Darabonba::Core::getBackoffTime(
              make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ =
          make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret =
          make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken =
          make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq =
          make_shared<map<string, boost::any>>(
              Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(
          _protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(
          _nickname,
          make_shared<string>(string("/v2/account/default/change_password")));
      request_->headers = Darabonba::Converter::merge(
          map<string, string>(
              {{"user-agent", getUserAgent()},
               {"host",
                Darabonba_Util::Client::defaultString(
                    _endpoint, make_shared<string>(string(
                                   "" + *_domainId + ".auth.aliyunpds.com")))},
               {"content-type", "application/json; charset=utf-8"}}),
          !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>(
            "authorization", string("Bearer " + *accessToken + "")));
      } else if (!Darabonba_Util::Client::empty(accesskeyId) &&
                 !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(
              pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>(
            "date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(
            pair<string, string>("accept", "application/json"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(
            Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>(
            "authorization", string("acs " + *accesskeyId + ":" +
                                    Alibabacloud_ROAUtil::Client::getSignature(
                                        stringToSign, accessKeySecret) +
                                    "")));
      }
      request_->body = Darabonba::Converter::toStream(
          Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ =
          make_shared<Darabonba::Response>(
              Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(
              make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(
            Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(
            Darabonba_Util::Client::assertAsMap(obj));
        return ChangePasswordModel(
            {{"body", !respMap ? boost::any() : boost::any(*respMap)},
             {"headers", boost::any(response_->headers)}});
      }
      if (!Darabonba_Util::Client::empty(
              make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(
            {{"data",
              boost::any(map<string, boost::any>(
                  {{"requestId",
                    boost::any(string(response_->headers["x-ca-request-id"]))},
                   {"statusCode", boost::any(response_->statusCode)},
                   {"statusMessage",
                    boost::any(string(response_->statusMessage))}}))},
             {"message",
              boost::any(string(response_->headers["x-ca-error-message"]))}})));
      }
      obj = make_shared<boost::any>(
          Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(
          Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(
          Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(
              map<string, boost::any>(
                  {{"data",
                    boost::any(map<string, boost::any>(
                        {{"requestId",
                          boost::any(
                              string(response_->headers["x-ca-request-id"]))},
                         {"statusCode", boost::any(response_->statusCode)},
                         {"statusMessage",
                          boost::any(string(response_->statusMessage))}}))}}),
              !respMap ? map<string, boost::any>() : *respMap))));
    } catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(
      Darabonba::UnretryableError(_lastRequest, _lastException));
}

SetPasswordModel Alibabacloud_Hosting::Client::setPasswordEx(
    shared_ptr<DefaultSetPasswordRequest> request,
    shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<
      map<string, boost::any>>(map<string, boost::any>(
      {{"timeouted", boost::any(string("retry"))},
       {"readTimeout", !runtime->readTimeout
                           ? boost::any()
                           : boost::any(*runtime->readTimeout)},
       {"connectTimeout", !runtime->connectTimeout
                              ? boost::any()
                              : boost::any(*runtime->connectTimeout)},
       {"localAddr",
        !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
       {"httpProxy",
        !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
       {"httpsProxy",
        !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
       {"noProxy", !runtime->noProxy ? boost::any()
                                     : boost::any(*runtime->noProxy)},
       {"maxIdleConns", !runtime->maxIdleConns
                            ? boost::any()
                            : boost::any(*runtime->maxIdleConns)},
       {"socks5Proxy", !runtime->socks5Proxy
                           ? boost::any()
                           : boost::any(*runtime->socks5Proxy)},
       {"socks5NetWork", !runtime->socks5NetWork
                             ? boost::any()
                             : boost::any(*runtime->socks5NetWork)},
       {"retry", boost::any(map<string, boost::any>(
                     {{"retryable", !runtime->autoretry
                                        ? boost::any()
                                        : boost::any(*runtime->autoretry)},
                      {"maxAttempts",
                       boost::any(Darabonba_Util::Client::defaultNumber(
                           runtime->maxAttempts, make_shared<int>(3)))}}))},
       {"backoff",
        boost::any(map<string, boost::any>(
            {{"policy",
              boost::any(string(Darabonba_Util::Client::defaultString(
                  runtime->backoffPolicy, make_shared<string>("no"))))},
             {"period", boost::any(Darabonba_Util::Client::defaultNumber(
                            runtime->backoffPeriod, make_shared<int>(1)))}}))},
       {"ignoreSSL", !runtime->ignoreSSL ? boost::any()
                                         : boost::any(*runtime->ignoreSSL)}}));
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(
      make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime =
          make_shared<int>(Darabonba::Core::getBackoffTime(
              make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ =
          make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret =
          make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken =
          make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq =
          make_shared<map<string, boost::any>>(
              Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(
          _protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(
          _nickname,
          make_shared<string>(string("/v2/account/default/set_password")));
      request_->headers = Darabonba::Converter::merge(
          map<string, string>(
              {{"user-agent", getUserAgent()},
               {"host",
                Darabonba_Util::Client::defaultString(
                    _endpoint, make_shared<string>(string(
                                   "" + *_domainId + ".auth.aliyunpds.com")))},
               {"content-type", "application/json; charset=utf-8"}}),
          !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>(
            "authorization", string("Bearer " + *accessToken + "")));
      } else if (!Darabonba_Util::Client::empty(accesskeyId) &&
                 !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(
              pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>(
            "date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(
            pair<string, string>("accept", "application/json"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(
            Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>(
            "authorization", string("acs " + *accesskeyId + ":" +
                                    Alibabacloud_ROAUtil::Client::getSignature(
                                        stringToSign, accessKeySecret) +
                                    "")));
      }
      request_->body = Darabonba::Converter::toStream(
          Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ =
          make_shared<Darabonba::Response>(
              Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(
              make_shared<int>(response_->statusCode), make_shared<int>(204))) {
        return SetPasswordModel({{"headers", boost::any(response_->headers)}});
      }
      if (!Darabonba_Util::Client::empty(
              make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(
            {{"data",
              boost::any(map<string, boost::any>(
                  {{"requestId",
                    boost::any(string(response_->headers["x-ca-request-id"]))},
                   {"statusCode", boost::any(response_->statusCode)},
                   {"statusMessage",
                    boost::any(string(response_->statusMessage))}}))},
             {"message",
              boost::any(string(response_->headers["x-ca-error-message"]))}})));
      }
      obj = make_shared<boost::any>(
          Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(
          Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(
          Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(
              map<string, boost::any>(
                  {{"data",
                    boost::any(map<string, boost::any>(
                        {{"requestId",
                          boost::any(
                              string(response_->headers["x-ca-request-id"]))},
                         {"statusCode", boost::any(response_->statusCode)},
                         {"statusMessage",
                          boost::any(string(response_->statusMessage))}}))}}),
              !respMap ? map<string, boost::any>() : *respMap))));
    } catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(
      Darabonba::UnretryableError(_lastRequest, _lastException));
}

VerifyCodeModel Alibabacloud_Hosting::Client::verifyCodeEx(
    shared_ptr<VerifyCodeRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<
      map<string, boost::any>>(map<string, boost::any>(
      {{"timeouted", boost::any(string("retry"))},
       {"readTimeout", !runtime->readTimeout
                           ? boost::any()
                           : boost::any(*runtime->readTimeout)},
       {"connectTimeout", !runtime->connectTimeout
                              ? boost::any()
                              : boost::any(*runtime->connectTimeout)},
       {"localAddr",
        !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
       {"httpProxy",
        !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
       {"httpsProxy",
        !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
       {"noProxy", !runtime->noProxy ? boost::any()
                                     : boost::any(*runtime->noProxy)},
       {"maxIdleConns", !runtime->maxIdleConns
                            ? boost::any()
                            : boost::any(*runtime->maxIdleConns)},
       {"socks5Proxy", !runtime->socks5Proxy
                           ? boost::any()
                           : boost::any(*runtime->socks5Proxy)},
       {"socks5NetWork", !runtime->socks5NetWork
                             ? boost::any()
                             : boost::any(*runtime->socks5NetWork)},
       {"retry", boost::any(map<string, boost::any>(
                     {{"retryable", !runtime->autoretry
                                        ? boost::any()
                                        : boost::any(*runtime->autoretry)},
                      {"maxAttempts",
                       boost::any(Darabonba_Util::Client::defaultNumber(
                           runtime->maxAttempts, make_shared<int>(3)))}}))},
       {"backoff",
        boost::any(map<string, boost::any>(
            {{"policy",
              boost::any(string(Darabonba_Util::Client::defaultString(
                  runtime->backoffPolicy, make_shared<string>("no"))))},
             {"period", boost::any(Darabonba_Util::Client::defaultNumber(
                            runtime->backoffPeriod, make_shared<int>(1)))}}))},
       {"ignoreSSL", !runtime->ignoreSSL ? boost::any()
                                         : boost::any(*runtime->ignoreSSL)}}));
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(
      make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime =
          make_shared<int>(Darabonba::Core::getBackoffTime(
              make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ =
          make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret =
          make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken =
          make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq =
          make_shared<map<string, boost::any>>(
              Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(
          _protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(
          _nickname,
          make_shared<string>(string("/v2/account/default/verify_code")));
      request_->headers = Darabonba::Converter::merge(
          map<string, string>(
              {{"user-agent", getUserAgent()},
               {"host",
                Darabonba_Util::Client::defaultString(
                    _endpoint, make_shared<string>(string(
                                   "" + *_domainId + ".auth.aliyunpds.com")))},
               {"content-type", "application/json; charset=utf-8"}}),
          !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>(
            "authorization", string("Bearer " + *accessToken + "")));
      } else if (!Darabonba_Util::Client::empty(accesskeyId) &&
                 !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(
              pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>(
            "date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(
            pair<string, string>("accept", "application/json"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(
            Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>(
            "authorization", string("acs " + *accesskeyId + ":" +
                                    Alibabacloud_ROAUtil::Client::getSignature(
                                        stringToSign, accessKeySecret) +
                                    "")));
      }
      request_->body = Darabonba::Converter::toStream(
          Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ =
          make_shared<Darabonba::Response>(
              Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(
              make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(
            Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(
            Darabonba_Util::Client::assertAsMap(obj));
        return VerifyCodeModel(
            {{"body", !respMap ? boost::any() : boost::any(*respMap)},
             {"headers", boost::any(response_->headers)}});
      }
      if (!Darabonba_Util::Client::empty(
              make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(
            {{"data",
              boost::any(map<string, boost::any>(
                  {{"requestId",
                    boost::any(string(response_->headers["x-ca-request-id"]))},
                   {"statusCode", boost::any(response_->statusCode)},
                   {"statusMessage",
                    boost::any(string(response_->statusMessage))}}))},
             {"message",
              boost::any(string(response_->headers["x-ca-error-message"]))}})));
      }
      obj = make_shared<boost::any>(
          Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(
          Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(
          Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(
              map<string, boost::any>(
                  {{"data",
                    boost::any(map<string, boost::any>(
                        {{"requestId",
                          boost::any(
                              string(response_->headers["x-ca-request-id"]))},
                         {"statusCode", boost::any(response_->statusCode)},
                         {"statusMessage",
                          boost::any(string(response_->statusMessage))}}))}}),
              !respMap ? map<string, boost::any>() : *respMap))));
    } catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(
      Darabonba::UnretryableError(_lastRequest, _lastException));
}

GetAccessTokenByLinkInfoModel
Alibabacloud_Hosting::Client::getAccessTokenByLinkInfoEx(
    shared_ptr<GetAccessTokenByLinkInfoRequest> request,
    shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<
      map<string, boost::any>>(map<string, boost::any>(
      {{"timeouted", boost::any(string("retry"))},
       {"readTimeout", !runtime->readTimeout
                           ? boost::any()
                           : boost::any(*runtime->readTimeout)},
       {"connectTimeout", !runtime->connectTimeout
                              ? boost::any()
                              : boost::any(*runtime->connectTimeout)},
       {"localAddr",
        !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
       {"httpProxy",
        !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
       {"httpsProxy",
        !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
       {"noProxy", !runtime->noProxy ? boost::any()
                                     : boost::any(*runtime->noProxy)},
       {"maxIdleConns", !runtime->maxIdleConns
                            ? boost::any()
                            : boost::any(*runtime->maxIdleConns)},
       {"socks5Proxy", !runtime->socks5Proxy
                           ? boost::any()
                           : boost::any(*runtime->socks5Proxy)},
       {"socks5NetWork", !runtime->socks5NetWork
                             ? boost::any()
                             : boost::any(*runtime->socks5NetWork)},
       {"retry", boost::any(map<string, boost::any>(
                     {{"retryable", !runtime->autoretry
                                        ? boost::any()
                                        : boost::any(*runtime->autoretry)},
                      {"maxAttempts",
                       boost::any(Darabonba_Util::Client::defaultNumber(
                           runtime->maxAttempts, make_shared<int>(3)))}}))},
       {"backoff",
        boost::any(map<string, boost::any>(
            {{"policy",
              boost::any(string(Darabonba_Util::Client::defaultString(
                  runtime->backoffPolicy, make_shared<string>("no"))))},
             {"period", boost::any(Darabonba_Util::Client::defaultNumber(
                            runtime->backoffPeriod, make_shared<int>(1)))}}))},
       {"ignoreSSL", !runtime->ignoreSSL ? boost::any()
                                         : boost::any(*runtime->ignoreSSL)}}));
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(
      make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime =
          make_shared<int>(Darabonba::Core::getBackoffTime(
              make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ =
          make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret =
          make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken =
          make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq =
          make_shared<map<string, boost::any>>(
              Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(
          _protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(
          _nickname, make_shared<string>(
                         string("/v2/account/get_access_token_by_link_info")));
      request_->headers = Darabonba::Converter::merge(
          map<string, string>(
              {{"user-agent", getUserAgent()},
               {"host",
                Darabonba_Util::Client::defaultString(
                    _endpoint, make_shared<string>(string(
                                   "" + *_domainId + ".auth.aliyunpds.com")))},
               {"content-type", "application/json; charset=utf-8"}}),
          !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>(
            "authorization", string("Bearer " + *accessToken + "")));
      } else if (!Darabonba_Util::Client::empty(accesskeyId) &&
                 !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(
              pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>(
            "date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(
            pair<string, string>("accept", "application/json"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(
            Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>(
            "authorization", string("acs " + *accesskeyId + ":" +
                                    Alibabacloud_ROAUtil::Client::getSignature(
                                        stringToSign, accessKeySecret) +
                                    "")));
      }
      request_->body = Darabonba::Converter::toStream(
          Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ =
          make_shared<Darabonba::Response>(
              Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(
              make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(
            Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(
            Darabonba_Util::Client::assertAsMap(obj));
        return GetAccessTokenByLinkInfoModel(
            {{"body", !respMap ? boost::any() : boost::any(*respMap)},
             {"headers", boost::any(response_->headers)}});
      }
      if (!Darabonba_Util::Client::empty(
              make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(
            {{"data",
              boost::any(map<string, boost::any>(
                  {{"requestId",
                    boost::any(string(response_->headers["x-ca-request-id"]))},
                   {"statusCode", boost::any(response_->statusCode)},
                   {"statusMessage",
                    boost::any(string(response_->statusMessage))}}))},
             {"message",
              boost::any(string(response_->headers["x-ca-error-message"]))}})));
      }
      obj = make_shared<boost::any>(
          Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(
          Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(
          Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(
              map<string, boost::any>(
                  {{"data",
                    boost::any(map<string, boost::any>(
                        {{"requestId",
                          boost::any(
                              string(response_->headers["x-ca-request-id"]))},
                         {"statusCode", boost::any(response_->statusCode)},
                         {"statusMessage",
                          boost::any(string(response_->statusMessage))}}))}}),
              !respMap ? map<string, boost::any>() : *respMap))));
    } catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(
      Darabonba::UnretryableError(_lastRequest, _lastException));
}

GetCaptchaModel Alibabacloud_Hosting::Client::getCaptchaEx(
    shared_ptr<GetCaptchaRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<
      map<string, boost::any>>(map<string, boost::any>(
      {{"timeouted", boost::any(string("retry"))},
       {"readTimeout", !runtime->readTimeout
                           ? boost::any()
                           : boost::any(*runtime->readTimeout)},
       {"connectTimeout", !runtime->connectTimeout
                              ? boost::any()
                              : boost::any(*runtime->connectTimeout)},
       {"localAddr",
        !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
       {"httpProxy",
        !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
       {"httpsProxy",
        !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
       {"noProxy", !runtime->noProxy ? boost::any()
                                     : boost::any(*runtime->noProxy)},
       {"maxIdleConns", !runtime->maxIdleConns
                            ? boost::any()
                            : boost::any(*runtime->maxIdleConns)},
       {"socks5Proxy", !runtime->socks5Proxy
                           ? boost::any()
                           : boost::any(*runtime->socks5Proxy)},
       {"socks5NetWork", !runtime->socks5NetWork
                             ? boost::any()
                             : boost::any(*runtime->socks5NetWork)},
       {"retry", boost::any(map<string, boost::any>(
                     {{"retryable", !runtime->autoretry
                                        ? boost::any()
                                        : boost::any(*runtime->autoretry)},
                      {"maxAttempts",
                       boost::any(Darabonba_Util::Client::defaultNumber(
                           runtime->maxAttempts, make_shared<int>(3)))}}))},
       {"backoff",
        boost::any(map<string, boost::any>(
            {{"policy",
              boost::any(string(Darabonba_Util::Client::defaultString(
                  runtime->backoffPolicy, make_shared<string>("no"))))},
             {"period", boost::any(Darabonba_Util::Client::defaultNumber(
                            runtime->backoffPeriod, make_shared<int>(1)))}}))},
       {"ignoreSSL", !runtime->ignoreSSL ? boost::any()
                                         : boost::any(*runtime->ignoreSSL)}}));
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(
      make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime =
          make_shared<int>(Darabonba::Core::getBackoffTime(
              make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ =
          make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret =
          make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken =
          make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq =
          make_shared<map<string, boost::any>>(
              Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(
          _protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(
          _nickname, make_shared<string>(string("/v2/account/get_captcha")));
      request_->headers = Darabonba::Converter::merge(
          map<string, string>(
              {{"user-agent", getUserAgent()},
               {"host",
                Darabonba_Util::Client::defaultString(
                    _endpoint, make_shared<string>(string(
                                   "" + *_domainId + ".auth.aliyunpds.com")))},
               {"content-type", "application/json; charset=utf-8"}}),
          !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>(
            "authorization", string("Bearer " + *accessToken + "")));
      } else if (!Darabonba_Util::Client::empty(accesskeyId) &&
                 !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(
              pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>(
            "date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(
            pair<string, string>("accept", "application/json"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(
            Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>(
            "authorization", string("acs " + *accesskeyId + ":" +
                                    Alibabacloud_ROAUtil::Client::getSignature(
                                        stringToSign, accessKeySecret) +
                                    "")));
      }
      request_->body = Darabonba::Converter::toStream(
          Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ =
          make_shared<Darabonba::Response>(
              Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(
              make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(
            Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(
            Darabonba_Util::Client::assertAsMap(obj));
        return GetCaptchaModel(
            {{"body", !respMap ? boost::any() : boost::any(*respMap)},
             {"headers", boost::any(response_->headers)}});
      }
      if (!Darabonba_Util::Client::empty(
              make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(
            {{"data",
              boost::any(map<string, boost::any>(
                  {{"requestId",
                    boost::any(string(response_->headers["x-ca-request-id"]))},
                   {"statusCode", boost::any(response_->statusCode)},
                   {"statusMessage",
                    boost::any(string(response_->statusMessage))}}))},
             {"message",
              boost::any(string(response_->headers["x-ca-error-message"]))}})));
      }
      obj = make_shared<boost::any>(
          Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(
          Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(
          Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(
              map<string, boost::any>(
                  {{"data",
                    boost::any(map<string, boost::any>(
                        {{"requestId",
                          boost::any(
                              string(response_->headers["x-ca-request-id"]))},
                         {"statusCode", boost::any(response_->statusCode)},
                         {"statusMessage",
                          boost::any(string(response_->statusMessage))}}))}}),
              !respMap ? map<string, boost::any>() : *respMap))));
    } catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(
      Darabonba::UnretryableError(_lastRequest, _lastException));
}

GetLinkInfoModel Alibabacloud_Hosting::Client::getLinkInfoEx(
    shared_ptr<GetByLinkInfoRequest> request,
    shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<
      map<string, boost::any>>(map<string, boost::any>(
      {{"timeouted", boost::any(string("retry"))},
       {"readTimeout", !runtime->readTimeout
                           ? boost::any()
                           : boost::any(*runtime->readTimeout)},
       {"connectTimeout", !runtime->connectTimeout
                              ? boost::any()
                              : boost::any(*runtime->connectTimeout)},
       {"localAddr",
        !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
       {"httpProxy",
        !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
       {"httpsProxy",
        !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
       {"noProxy", !runtime->noProxy ? boost::any()
                                     : boost::any(*runtime->noProxy)},
       {"maxIdleConns", !runtime->maxIdleConns
                            ? boost::any()
                            : boost::any(*runtime->maxIdleConns)},
       {"socks5Proxy", !runtime->socks5Proxy
                           ? boost::any()
                           : boost::any(*runtime->socks5Proxy)},
       {"socks5NetWork", !runtime->socks5NetWork
                             ? boost::any()
                             : boost::any(*runtime->socks5NetWork)},
       {"retry", boost::any(map<string, boost::any>(
                     {{"retryable", !runtime->autoretry
                                        ? boost::any()
                                        : boost::any(*runtime->autoretry)},
                      {"maxAttempts",
                       boost::any(Darabonba_Util::Client::defaultNumber(
                           runtime->maxAttempts, make_shared<int>(3)))}}))},
       {"backoff",
        boost::any(map<string, boost::any>(
            {{"policy",
              boost::any(string(Darabonba_Util::Client::defaultString(
                  runtime->backoffPolicy, make_shared<string>("no"))))},
             {"period", boost::any(Darabonba_Util::Client::defaultNumber(
                            runtime->backoffPeriod, make_shared<int>(1)))}}))},
       {"ignoreSSL", !runtime->ignoreSSL ? boost::any()
                                         : boost::any(*runtime->ignoreSSL)}}));
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(
      make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime =
          make_shared<int>(Darabonba::Core::getBackoffTime(
              make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ =
          make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret =
          make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken =
          make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq =
          make_shared<map<string, boost::any>>(
              Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(
          _protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(
          _nickname, make_shared<string>(string("/v2/account/get_link_info")));
      request_->headers = Darabonba::Converter::merge(
          map<string, string>(
              {{"user-agent", getUserAgent()},
               {"host",
                Darabonba_Util::Client::defaultString(
                    _endpoint, make_shared<string>(string(
                                   "" + *_domainId + ".auth.aliyunpds.com")))},
               {"content-type", "application/json; charset=utf-8"}}),
          !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>(
            "authorization", string("Bearer " + *accessToken + "")));
      } else if (!Darabonba_Util::Client::empty(accesskeyId) &&
                 !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(
              pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>(
            "date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(
            pair<string, string>("accept", "application/json"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(
            Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>(
            "authorization", string("acs " + *accesskeyId + ":" +
                                    Alibabacloud_ROAUtil::Client::getSignature(
                                        stringToSign, accessKeySecret) +
                                    "")));
      }
      request_->body = Darabonba::Converter::toStream(
          Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ =
          make_shared<Darabonba::Response>(
              Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(
              make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(
            Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(
            Darabonba_Util::Client::assertAsMap(obj));
        return GetLinkInfoModel(
            {{"body", !respMap ? boost::any() : boost::any(*respMap)},
             {"headers", boost::any(response_->headers)}});
      }
      if (!Darabonba_Util::Client::empty(
              make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(
            {{"data",
              boost::any(map<string, boost::any>(
                  {{"requestId",
                    boost::any(string(response_->headers["x-ca-request-id"]))},
                   {"statusCode", boost::any(response_->statusCode)},
                   {"statusMessage",
                    boost::any(string(response_->statusMessage))}}))},
             {"message",
              boost::any(string(response_->headers["x-ca-error-message"]))}})));
      }
      obj = make_shared<boost::any>(
          Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(
          Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(
          Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(
              map<string, boost::any>(
                  {{"data",
                    boost::any(map<string, boost::any>(
                        {{"requestId",
                          boost::any(
                              string(response_->headers["x-ca-request-id"]))},
                         {"statusCode", boost::any(response_->statusCode)},
                         {"statusMessage",
                          boost::any(string(response_->statusMessage))}}))}}),
              !respMap ? map<string, boost::any>() : *respMap))));
    } catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(
      Darabonba::UnretryableError(_lastRequest, _lastException));
}

GetLinkInfoByUserIdModel Alibabacloud_Hosting::Client::getLinkInfoByUserIdEx(
    shared_ptr<GetLinkInfoByUserIDRequest> request,
    shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<
      map<string, boost::any>>(map<string, boost::any>(
      {{"timeouted", boost::any(string("retry"))},
       {"readTimeout", !runtime->readTimeout
                           ? boost::any()
                           : boost::any(*runtime->readTimeout)},
       {"connectTimeout", !runtime->connectTimeout
                              ? boost::any()
                              : boost::any(*runtime->connectTimeout)},
       {"localAddr",
        !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
       {"httpProxy",
        !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
       {"httpsProxy",
        !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
       {"noProxy", !runtime->noProxy ? boost::any()
                                     : boost::any(*runtime->noProxy)},
       {"maxIdleConns", !runtime->maxIdleConns
                            ? boost::any()
                            : boost::any(*runtime->maxIdleConns)},
       {"socks5Proxy", !runtime->socks5Proxy
                           ? boost::any()
                           : boost::any(*runtime->socks5Proxy)},
       {"socks5NetWork", !runtime->socks5NetWork
                             ? boost::any()
                             : boost::any(*runtime->socks5NetWork)},
       {"retry", boost::any(map<string, boost::any>(
                     {{"retryable", !runtime->autoretry
                                        ? boost::any()
                                        : boost::any(*runtime->autoretry)},
                      {"maxAttempts",
                       boost::any(Darabonba_Util::Client::defaultNumber(
                           runtime->maxAttempts, make_shared<int>(3)))}}))},
       {"backoff",
        boost::any(map<string, boost::any>(
            {{"policy",
              boost::any(string(Darabonba_Util::Client::defaultString(
                  runtime->backoffPolicy, make_shared<string>("no"))))},
             {"period", boost::any(Darabonba_Util::Client::defaultNumber(
                            runtime->backoffPeriod, make_shared<int>(1)))}}))},
       {"ignoreSSL", !runtime->ignoreSSL ? boost::any()
                                         : boost::any(*runtime->ignoreSSL)}}));
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(
      make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime =
          make_shared<int>(Darabonba::Core::getBackoffTime(
              make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ =
          make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret =
          make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken =
          make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq =
          make_shared<map<string, boost::any>>(
              Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(
          _protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(
          _nickname,
          make_shared<string>(string("/v2/account/get_link_info_by_user_id")));
      request_->headers = Darabonba::Converter::merge(
          map<string, string>(
              {{"user-agent", getUserAgent()},
               {"host",
                Darabonba_Util::Client::defaultString(
                    _endpoint, make_shared<string>(string(
                                   "" + *_domainId + ".auth.aliyunpds.com")))},
               {"content-type", "application/json; charset=utf-8"}}),
          !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>(
            "authorization", string("Bearer " + *accessToken + "")));
      } else if (!Darabonba_Util::Client::empty(accesskeyId) &&
                 !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(
              pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>(
            "date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(
            pair<string, string>("accept", "application/json"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(
            Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>(
            "authorization", string("acs " + *accesskeyId + ":" +
                                    Alibabacloud_ROAUtil::Client::getSignature(
                                        stringToSign, accessKeySecret) +
                                    "")));
      }
      request_->body = Darabonba::Converter::toStream(
          Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ =
          make_shared<Darabonba::Response>(
              Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(
              make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(
            Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(
            Darabonba_Util::Client::assertAsMap(obj));
        return GetLinkInfoByUserIdModel(
            {{"body", !respMap ? boost::any() : boost::any(*respMap)},
             {"headers", boost::any(response_->headers)}});
      }
      if (!Darabonba_Util::Client::empty(
              make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(
            {{"data",
              boost::any(map<string, boost::any>(
                  {{"requestId",
                    boost::any(string(response_->headers["x-ca-request-id"]))},
                   {"statusCode", boost::any(response_->statusCode)},
                   {"statusMessage",
                    boost::any(string(response_->statusMessage))}}))},
             {"message",
              boost::any(string(response_->headers["x-ca-error-message"]))}})));
      }
      obj = make_shared<boost::any>(
          Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(
          Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(
          Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(
              map<string, boost::any>(
                  {{"data",
                    boost::any(map<string, boost::any>(
                        {{"requestId",
                          boost::any(
                              string(response_->headers["x-ca-request-id"]))},
                         {"statusCode", boost::any(response_->statusCode)},
                         {"statusMessage",
                          boost::any(string(response_->statusMessage))}}))}}),
              !respMap ? map<string, boost::any>() : *respMap))));
    } catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(
      Darabonba::UnretryableError(_lastRequest, _lastException));
}

GetPublicKeyModel Alibabacloud_Hosting::Client::getPublicKeyEx(
    shared_ptr<GetAppPublicKeyRequest> request,
    shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<
      map<string, boost::any>>(map<string, boost::any>(
      {{"timeouted", boost::any(string("retry"))},
       {"readTimeout", !runtime->readTimeout
                           ? boost::any()
                           : boost::any(*runtime->readTimeout)},
       {"connectTimeout", !runtime->connectTimeout
                              ? boost::any()
                              : boost::any(*runtime->connectTimeout)},
       {"localAddr",
        !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
       {"httpProxy",
        !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
       {"httpsProxy",
        !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
       {"noProxy", !runtime->noProxy ? boost::any()
                                     : boost::any(*runtime->noProxy)},
       {"maxIdleConns", !runtime->maxIdleConns
                            ? boost::any()
                            : boost::any(*runtime->maxIdleConns)},
       {"socks5Proxy", !runtime->socks5Proxy
                           ? boost::any()
                           : boost::any(*runtime->socks5Proxy)},
       {"socks5NetWork", !runtime->socks5NetWork
                             ? boost::any()
                             : boost::any(*runtime->socks5NetWork)},
       {"retry", boost::any(map<string, boost::any>(
                     {{"retryable", !runtime->autoretry
                                        ? boost::any()
                                        : boost::any(*runtime->autoretry)},
                      {"maxAttempts",
                       boost::any(Darabonba_Util::Client::defaultNumber(
                           runtime->maxAttempts, make_shared<int>(3)))}}))},
       {"backoff",
        boost::any(map<string, boost::any>(
            {{"policy",
              boost::any(string(Darabonba_Util::Client::defaultString(
                  runtime->backoffPolicy, make_shared<string>("no"))))},
             {"period", boost::any(Darabonba_Util::Client::defaultNumber(
                            runtime->backoffPeriod, make_shared<int>(1)))}}))},
       {"ignoreSSL", !runtime->ignoreSSL ? boost::any()
                                         : boost::any(*runtime->ignoreSSL)}}));
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(
      make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime =
          make_shared<int>(Darabonba::Core::getBackoffTime(
              make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ =
          make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret =
          make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken =
          make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq =
          make_shared<map<string, boost::any>>(
              Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(
          _protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(
          _nickname, make_shared<string>(string("/v2/account/get_public_key")));
      request_->headers = Darabonba::Converter::merge(
          map<string, string>(
              {{"user-agent", getUserAgent()},
               {"host",
                Darabonba_Util::Client::defaultString(
                    _endpoint, make_shared<string>(string(
                                   "" + *_domainId + ".auth.aliyunpds.com")))},
               {"content-type", "application/json; charset=utf-8"}}),
          !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>(
            "authorization", string("Bearer " + *accessToken + "")));
      } else if (!Darabonba_Util::Client::empty(accesskeyId) &&
                 !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(
              pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>(
            "date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(
            pair<string, string>("accept", "application/json"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(
            Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>(
            "authorization", string("acs " + *accesskeyId + ":" +
                                    Alibabacloud_ROAUtil::Client::getSignature(
                                        stringToSign, accessKeySecret) +
                                    "")));
      }
      request_->body = Darabonba::Converter::toStream(
          Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ =
          make_shared<Darabonba::Response>(
              Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(
              make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(
            Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(
            Darabonba_Util::Client::assertAsMap(obj));
        return GetPublicKeyModel(
            {{"body", !respMap ? boost::any() : boost::any(*respMap)},
             {"headers", boost::any(response_->headers)}});
      }
      if (!Darabonba_Util::Client::empty(
              make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(
            {{"data",
              boost::any(map<string, boost::any>(
                  {{"requestId",
                    boost::any(string(response_->headers["x-ca-request-id"]))},
                   {"statusCode", boost::any(response_->statusCode)},
                   {"statusMessage",
                    boost::any(string(response_->statusMessage))}}))},
             {"message",
              boost::any(string(response_->headers["x-ca-error-message"]))}})));
      }
      obj = make_shared<boost::any>(
          Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(
          Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(
          Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(
              map<string, boost::any>(
                  {{"data",
                    boost::any(map<string, boost::any>(
                        {{"requestId",
                          boost::any(
                              string(response_->headers["x-ca-request-id"]))},
                         {"statusCode", boost::any(response_->statusCode)},
                         {"statusMessage",
                          boost::any(string(response_->statusMessage))}}))}}),
              !respMap ? map<string, boost::any>() : *respMap))));
    } catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(
      Darabonba::UnretryableError(_lastRequest, _lastException));
}

LinkModel
Alibabacloud_Hosting::Client::linkEx(shared_ptr<AccountLinkRequest> request,
                                     shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<
      map<string, boost::any>>(map<string, boost::any>(
      {{"timeouted", boost::any(string("retry"))},
       {"readTimeout", !runtime->readTimeout
                           ? boost::any()
                           : boost::any(*runtime->readTimeout)},
       {"connectTimeout", !runtime->connectTimeout
                              ? boost::any()
                              : boost::any(*runtime->connectTimeout)},
       {"localAddr",
        !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
       {"httpProxy",
        !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
       {"httpsProxy",
        !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
       {"noProxy", !runtime->noProxy ? boost::any()
                                     : boost::any(*runtime->noProxy)},
       {"maxIdleConns", !runtime->maxIdleConns
                            ? boost::any()
                            : boost::any(*runtime->maxIdleConns)},
       {"socks5Proxy", !runtime->socks5Proxy
                           ? boost::any()
                           : boost::any(*runtime->socks5Proxy)},
       {"socks5NetWork", !runtime->socks5NetWork
                             ? boost::any()
                             : boost::any(*runtime->socks5NetWork)},
       {"retry", boost::any(map<string, boost::any>(
                     {{"retryable", !runtime->autoretry
                                        ? boost::any()
                                        : boost::any(*runtime->autoretry)},
                      {"maxAttempts",
                       boost::any(Darabonba_Util::Client::defaultNumber(
                           runtime->maxAttempts, make_shared<int>(3)))}}))},
       {"backoff",
        boost::any(map<string, boost::any>(
            {{"policy",
              boost::any(string(Darabonba_Util::Client::defaultString(
                  runtime->backoffPolicy, make_shared<string>("no"))))},
             {"period", boost::any(Darabonba_Util::Client::defaultNumber(
                            runtime->backoffPeriod, make_shared<int>(1)))}}))},
       {"ignoreSSL", !runtime->ignoreSSL ? boost::any()
                                         : boost::any(*runtime->ignoreSSL)}}));
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(
      make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime =
          make_shared<int>(Darabonba::Core::getBackoffTime(
              make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ =
          make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret =
          make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken =
          make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq =
          make_shared<map<string, boost::any>>(
              Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(
          _protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(
          _nickname, make_shared<string>(string("/v2/account/link")));
      request_->headers = Darabonba::Converter::merge(
          map<string, string>(
              {{"user-agent", getUserAgent()},
               {"host",
                Darabonba_Util::Client::defaultString(
                    _endpoint, make_shared<string>(string(
                                   "" + *_domainId + ".auth.aliyunpds.com")))},
               {"content-type", "application/json; charset=utf-8"}}),
          !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>(
            "authorization", string("Bearer " + *accessToken + "")));
      } else if (!Darabonba_Util::Client::empty(accesskeyId) &&
                 !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(
              pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>(
            "date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(
            pair<string, string>("accept", "application/json"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(
            Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>(
            "authorization", string("acs " + *accesskeyId + ":" +
                                    Alibabacloud_ROAUtil::Client::getSignature(
                                        stringToSign, accessKeySecret) +
                                    "")));
      }
      request_->body = Darabonba::Converter::toStream(
          Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ =
          make_shared<Darabonba::Response>(
              Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(
              make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(
            Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(
            Darabonba_Util::Client::assertAsMap(obj));
        return LinkModel(
            {{"body", !respMap ? boost::any() : boost::any(*respMap)},
             {"headers", boost::any(response_->headers)}});
      }
      if (!Darabonba_Util::Client::empty(
              make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(
            {{"data",
              boost::any(map<string, boost::any>(
                  {{"requestId",
                    boost::any(string(response_->headers["x-ca-request-id"]))},
                   {"statusCode", boost::any(response_->statusCode)},
                   {"statusMessage",
                    boost::any(string(response_->statusMessage))}}))},
             {"message",
              boost::any(string(response_->headers["x-ca-error-message"]))}})));
      }
      obj = make_shared<boost::any>(
          Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(
          Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(
          Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(
              map<string, boost::any>(
                  {{"data",
                    boost::any(map<string, boost::any>(
                        {{"requestId",
                          boost::any(
                              string(response_->headers["x-ca-request-id"]))},
                         {"statusCode", boost::any(response_->statusCode)},
                         {"statusMessage",
                          boost::any(string(response_->statusMessage))}}))}}),
              !respMap ? map<string, boost::any>() : *respMap))));
    } catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(
      Darabonba::UnretryableError(_lastRequest, _lastException));
}

CheckExistModel Alibabacloud_Hosting::Client::checkExistEx(
    shared_ptr<MobileCheckExistRequest> request,
    shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<
      map<string, boost::any>>(map<string, boost::any>(
      {{"timeouted", boost::any(string("retry"))},
       {"readTimeout", !runtime->readTimeout
                           ? boost::any()
                           : boost::any(*runtime->readTimeout)},
       {"connectTimeout", !runtime->connectTimeout
                              ? boost::any()
                              : boost::any(*runtime->connectTimeout)},
       {"localAddr",
        !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
       {"httpProxy",
        !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
       {"httpsProxy",
        !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
       {"noProxy", !runtime->noProxy ? boost::any()
                                     : boost::any(*runtime->noProxy)},
       {"maxIdleConns", !runtime->maxIdleConns
                            ? boost::any()
                            : boost::any(*runtime->maxIdleConns)},
       {"socks5Proxy", !runtime->socks5Proxy
                           ? boost::any()
                           : boost::any(*runtime->socks5Proxy)},
       {"socks5NetWork", !runtime->socks5NetWork
                             ? boost::any()
                             : boost::any(*runtime->socks5NetWork)},
       {"retry", boost::any(map<string, boost::any>(
                     {{"retryable", !runtime->autoretry
                                        ? boost::any()
                                        : boost::any(*runtime->autoretry)},
                      {"maxAttempts",
                       boost::any(Darabonba_Util::Client::defaultNumber(
                           runtime->maxAttempts, make_shared<int>(3)))}}))},
       {"backoff",
        boost::any(map<string, boost::any>(
            {{"policy",
              boost::any(string(Darabonba_Util::Client::defaultString(
                  runtime->backoffPolicy, make_shared<string>("no"))))},
             {"period", boost::any(Darabonba_Util::Client::defaultNumber(
                            runtime->backoffPeriod, make_shared<int>(1)))}}))},
       {"ignoreSSL", !runtime->ignoreSSL ? boost::any()
                                         : boost::any(*runtime->ignoreSSL)}}));
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(
      make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime =
          make_shared<int>(Darabonba::Core::getBackoffTime(
              make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ =
          make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret =
          make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken =
          make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq =
          make_shared<map<string, boost::any>>(
              Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(
          _protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(
          _nickname,
          make_shared<string>(string("/v2/account/mobile/check_exist")));
      request_->headers = Darabonba::Converter::merge(
          map<string, string>(
              {{"user-agent", getUserAgent()},
               {"host",
                Darabonba_Util::Client::defaultString(
                    _endpoint, make_shared<string>(string(
                                   "" + *_domainId + ".auth.aliyunpds.com")))},
               {"content-type", "application/json; charset=utf-8"}}),
          !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>(
            "authorization", string("Bearer " + *accessToken + "")));
      } else if (!Darabonba_Util::Client::empty(accesskeyId) &&
                 !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(
              pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>(
            "date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(
            pair<string, string>("accept", "application/json"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(
            Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>(
            "authorization", string("acs " + *accesskeyId + ":" +
                                    Alibabacloud_ROAUtil::Client::getSignature(
                                        stringToSign, accessKeySecret) +
                                    "")));
      }
      request_->body = Darabonba::Converter::toStream(
          Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ =
          make_shared<Darabonba::Response>(
              Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(
              make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(
            Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(
            Darabonba_Util::Client::assertAsMap(obj));
        return CheckExistModel(
            {{"body", !respMap ? boost::any() : boost::any(*respMap)},
             {"headers", boost::any(response_->headers)}});
      }
      if (!Darabonba_Util::Client::empty(
              make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(
            {{"data",
              boost::any(map<string, boost::any>(
                  {{"requestId",
                    boost::any(string(response_->headers["x-ca-request-id"]))},
                   {"statusCode", boost::any(response_->statusCode)},
                   {"statusMessage",
                    boost::any(string(response_->statusMessage))}}))},
             {"message",
              boost::any(string(response_->headers["x-ca-error-message"]))}})));
      }
      obj = make_shared<boost::any>(
          Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(
          Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(
          Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(
              map<string, boost::any>(
                  {{"data",
                    boost::any(map<string, boost::any>(
                        {{"requestId",
                          boost::any(
                              string(response_->headers["x-ca-request-id"]))},
                         {"statusCode", boost::any(response_->statusCode)},
                         {"statusMessage",
                          boost::any(string(response_->statusMessage))}}))}}),
              !respMap ? map<string, boost::any>() : *respMap))));
    } catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(
      Darabonba::UnretryableError(_lastRequest, _lastException));
}

LoginModel
Alibabacloud_Hosting::Client::loginEx(shared_ptr<MobileLoginRequest> request,
                                      shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<
      map<string, boost::any>>(map<string, boost::any>(
      {{"timeouted", boost::any(string("retry"))},
       {"readTimeout", !runtime->readTimeout
                           ? boost::any()
                           : boost::any(*runtime->readTimeout)},
       {"connectTimeout", !runtime->connectTimeout
                              ? boost::any()
                              : boost::any(*runtime->connectTimeout)},
       {"localAddr",
        !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
       {"httpProxy",
        !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
       {"httpsProxy",
        !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
       {"noProxy", !runtime->noProxy ? boost::any()
                                     : boost::any(*runtime->noProxy)},
       {"maxIdleConns", !runtime->maxIdleConns
                            ? boost::any()
                            : boost::any(*runtime->maxIdleConns)},
       {"socks5Proxy", !runtime->socks5Proxy
                           ? boost::any()
                           : boost::any(*runtime->socks5Proxy)},
       {"socks5NetWork", !runtime->socks5NetWork
                             ? boost::any()
                             : boost::any(*runtime->socks5NetWork)},
       {"retry", boost::any(map<string, boost::any>(
                     {{"retryable", !runtime->autoretry
                                        ? boost::any()
                                        : boost::any(*runtime->autoretry)},
                      {"maxAttempts",
                       boost::any(Darabonba_Util::Client::defaultNumber(
                           runtime->maxAttempts, make_shared<int>(3)))}}))},
       {"backoff",
        boost::any(map<string, boost::any>(
            {{"policy",
              boost::any(string(Darabonba_Util::Client::defaultString(
                  runtime->backoffPolicy, make_shared<string>("no"))))},
             {"period", boost::any(Darabonba_Util::Client::defaultNumber(
                            runtime->backoffPeriod, make_shared<int>(1)))}}))},
       {"ignoreSSL", !runtime->ignoreSSL ? boost::any()
                                         : boost::any(*runtime->ignoreSSL)}}));
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(
      make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime =
          make_shared<int>(Darabonba::Core::getBackoffTime(
              make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ =
          make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret =
          make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken =
          make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq =
          make_shared<map<string, boost::any>>(
              Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(
          _protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(
          _nickname, make_shared<string>(string("/v2/account/mobile/login")));
      request_->headers = Darabonba::Converter::merge(
          map<string, string>(
              {{"user-agent", getUserAgent()},
               {"host",
                Darabonba_Util::Client::defaultString(
                    _endpoint, make_shared<string>(string(
                                   "" + *_domainId + ".auth.aliyunpds.com")))},
               {"content-type", "application/json; charset=utf-8"}}),
          !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>(
            "authorization", string("Bearer " + *accessToken + "")));
      } else if (!Darabonba_Util::Client::empty(accesskeyId) &&
                 !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(
              pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>(
            "date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(
            pair<string, string>("accept", "application/json"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(
            Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>(
            "authorization", string("acs " + *accesskeyId + ":" +
                                    Alibabacloud_ROAUtil::Client::getSignature(
                                        stringToSign, accessKeySecret) +
                                    "")));
      }
      request_->body = Darabonba::Converter::toStream(
          Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ =
          make_shared<Darabonba::Response>(
              Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(
              make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(
            Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(
            Darabonba_Util::Client::assertAsMap(obj));
        return LoginModel(
            {{"body", !respMap ? boost::any() : boost::any(*respMap)},
             {"headers", boost::any(response_->headers)}});
      }
      if (!Darabonba_Util::Client::empty(
              make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(
            {{"data",
              boost::any(map<string, boost::any>(
                  {{"requestId",
                    boost::any(string(response_->headers["x-ca-request-id"]))},
                   {"statusCode", boost::any(response_->statusCode)},
                   {"statusMessage",
                    boost::any(string(response_->statusMessage))}}))},
             {"message",
              boost::any(string(response_->headers["x-ca-error-message"]))}})));
      }
      obj = make_shared<boost::any>(
          Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(
          Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(
          Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(
              map<string, boost::any>(
                  {{"data",
                    boost::any(map<string, boost::any>(
                        {{"requestId",
                          boost::any(
                              string(response_->headers["x-ca-request-id"]))},
                         {"statusCode", boost::any(response_->statusCode)},
                         {"statusMessage",
                          boost::any(string(response_->statusMessage))}}))}}),
              !respMap ? map<string, boost::any>() : *respMap))));
    } catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(
      Darabonba::UnretryableError(_lastRequest, _lastException));
}

RegisterModel Alibabacloud_Hosting::Client::registerEx(
    shared_ptr<MobileRegisterRequest> request,
    shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<
      map<string, boost::any>>(map<string, boost::any>(
      {{"timeouted", boost::any(string("retry"))},
       {"readTimeout", !runtime->readTimeout
                           ? boost::any()
                           : boost::any(*runtime->readTimeout)},
       {"connectTimeout", !runtime->connectTimeout
                              ? boost::any()
                              : boost::any(*runtime->connectTimeout)},
       {"localAddr",
        !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
       {"httpProxy",
        !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
       {"httpsProxy",
        !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
       {"noProxy", !runtime->noProxy ? boost::any()
                                     : boost::any(*runtime->noProxy)},
       {"maxIdleConns", !runtime->maxIdleConns
                            ? boost::any()
                            : boost::any(*runtime->maxIdleConns)},
       {"socks5Proxy", !runtime->socks5Proxy
                           ? boost::any()
                           : boost::any(*runtime->socks5Proxy)},
       {"socks5NetWork", !runtime->socks5NetWork
                             ? boost::any()
                             : boost::any(*runtime->socks5NetWork)},
       {"retry", boost::any(map<string, boost::any>(
                     {{"retryable", !runtime->autoretry
                                        ? boost::any()
                                        : boost::any(*runtime->autoretry)},
                      {"maxAttempts",
                       boost::any(Darabonba_Util::Client::defaultNumber(
                           runtime->maxAttempts, make_shared<int>(3)))}}))},
       {"backoff",
        boost::any(map<string, boost::any>(
            {{"policy",
              boost::any(string(Darabonba_Util::Client::defaultString(
                  runtime->backoffPolicy, make_shared<string>("no"))))},
             {"period", boost::any(Darabonba_Util::Client::defaultNumber(
                            runtime->backoffPeriod, make_shared<int>(1)))}}))},
       {"ignoreSSL", !runtime->ignoreSSL ? boost::any()
                                         : boost::any(*runtime->ignoreSSL)}}));
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(
      make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime =
          make_shared<int>(Darabonba::Core::getBackoffTime(
              make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ =
          make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret =
          make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken =
          make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq =
          make_shared<map<string, boost::any>>(
              Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(
          _protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(
          _nickname,
          make_shared<string>(string("/v2/account/mobile/register")));
      request_->headers = Darabonba::Converter::merge(
          map<string, string>(
              {{"user-agent", getUserAgent()},
               {"host",
                Darabonba_Util::Client::defaultString(
                    _endpoint, make_shared<string>(string(
                                   "" + *_domainId + ".auth.aliyunpds.com")))},
               {"content-type", "application/json; charset=utf-8"}}),
          !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>(
            "authorization", string("Bearer " + *accessToken + "")));
      } else if (!Darabonba_Util::Client::empty(accesskeyId) &&
                 !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(
              pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>(
            "date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(
            pair<string, string>("accept", "application/json"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(
            Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>(
            "authorization", string("acs " + *accesskeyId + ":" +
                                    Alibabacloud_ROAUtil::Client::getSignature(
                                        stringToSign, accessKeySecret) +
                                    "")));
      }
      request_->body = Darabonba::Converter::toStream(
          Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ =
          make_shared<Darabonba::Response>(
              Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(
              make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(
            Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(
            Darabonba_Util::Client::assertAsMap(obj));
        return RegisterModel(
            {{"body", !respMap ? boost::any() : boost::any(*respMap)},
             {"headers", boost::any(response_->headers)}});
      }
      if (!Darabonba_Util::Client::empty(
              make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(
            {{"data",
              boost::any(map<string, boost::any>(
                  {{"requestId",
                    boost::any(string(response_->headers["x-ca-request-id"]))},
                   {"statusCode", boost::any(response_->statusCode)},
                   {"statusMessage",
                    boost::any(string(response_->statusMessage))}}))},
             {"message",
              boost::any(string(response_->headers["x-ca-error-message"]))}})));
      }
      obj = make_shared<boost::any>(
          Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(
          Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(
          Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(
              map<string, boost::any>(
                  {{"data",
                    boost::any(map<string, boost::any>(
                        {{"requestId",
                          boost::any(
                              string(response_->headers["x-ca-request-id"]))},
                         {"statusCode", boost::any(response_->statusCode)},
                         {"statusMessage",
                          boost::any(string(response_->statusMessage))}}))}}),
              !respMap ? map<string, boost::any>() : *respMap))));
    } catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(
      Darabonba::UnretryableError(_lastRequest, _lastException));
}

MobileSendSmsCodeModel Alibabacloud_Hosting::Client::mobileSendSmsCodeEx(
    shared_ptr<MobileSendSmsCodeRequest> request,
    shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<
      map<string, boost::any>>(map<string, boost::any>(
      {{"timeouted", boost::any(string("retry"))},
       {"readTimeout", !runtime->readTimeout
                           ? boost::any()
                           : boost::any(*runtime->readTimeout)},
       {"connectTimeout", !runtime->connectTimeout
                              ? boost::any()
                              : boost::any(*runtime->connectTimeout)},
       {"localAddr",
        !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
       {"httpProxy",
        !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
       {"httpsProxy",
        !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
       {"noProxy", !runtime->noProxy ? boost::any()
                                     : boost::any(*runtime->noProxy)},
       {"maxIdleConns", !runtime->maxIdleConns
                            ? boost::any()
                            : boost::any(*runtime->maxIdleConns)},
       {"socks5Proxy", !runtime->socks5Proxy
                           ? boost::any()
                           : boost::any(*runtime->socks5Proxy)},
       {"socks5NetWork", !runtime->socks5NetWork
                             ? boost::any()
                             : boost::any(*runtime->socks5NetWork)},
       {"retry", boost::any(map<string, boost::any>(
                     {{"retryable", !runtime->autoretry
                                        ? boost::any()
                                        : boost::any(*runtime->autoretry)},
                      {"maxAttempts",
                       boost::any(Darabonba_Util::Client::defaultNumber(
                           runtime->maxAttempts, make_shared<int>(3)))}}))},
       {"backoff",
        boost::any(map<string, boost::any>(
            {{"policy",
              boost::any(string(Darabonba_Util::Client::defaultString(
                  runtime->backoffPolicy, make_shared<string>("no"))))},
             {"period", boost::any(Darabonba_Util::Client::defaultNumber(
                            runtime->backoffPeriod, make_shared<int>(1)))}}))},
       {"ignoreSSL", !runtime->ignoreSSL ? boost::any()
                                         : boost::any(*runtime->ignoreSSL)}}));
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(
      make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime =
          make_shared<int>(Darabonba::Core::getBackoffTime(
              make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ =
          make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret =
          make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken =
          make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq =
          make_shared<map<string, boost::any>>(
              Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(
          _protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(
          _nickname,
          make_shared<string>(string("/v2/account/mobile/send_sms_code")));
      request_->headers = Darabonba::Converter::merge(
          map<string, string>(
              {{"user-agent", getUserAgent()},
               {"host",
                Darabonba_Util::Client::defaultString(
                    _endpoint, make_shared<string>(string(
                                   "" + *_domainId + ".auth.aliyunpds.com")))},
               {"content-type", "application/json; charset=utf-8"}}),
          !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>(
            "authorization", string("Bearer " + *accessToken + "")));
      } else if (!Darabonba_Util::Client::empty(accesskeyId) &&
                 !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(
              pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>(
            "date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(
            pair<string, string>("accept", "application/json"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(
            Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>(
            "authorization", string("acs " + *accesskeyId + ":" +
                                    Alibabacloud_ROAUtil::Client::getSignature(
                                        stringToSign, accessKeySecret) +
                                    "")));
      }
      request_->body = Darabonba::Converter::toStream(
          Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ =
          make_shared<Darabonba::Response>(
              Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(
              make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(
            Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(
            Darabonba_Util::Client::assertAsMap(obj));
        return MobileSendSmsCodeModel(
            {{"body", !respMap ? boost::any() : boost::any(*respMap)},
             {"headers", boost::any(response_->headers)}});
      }
      if (!Darabonba_Util::Client::empty(
              make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(
            {{"data",
              boost::any(map<string, boost::any>(
                  {{"requestId",
                    boost::any(string(response_->headers["x-ca-request-id"]))},
                   {"statusCode", boost::any(response_->statusCode)},
                   {"statusMessage",
                    boost::any(string(response_->statusMessage))}}))},
             {"message",
              boost::any(string(response_->headers["x-ca-error-message"]))}})));
      }
      obj = make_shared<boost::any>(
          Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(
          Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(
          Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(
              map<string, boost::any>(
                  {{"data",
                    boost::any(map<string, boost::any>(
                        {{"requestId",
                          boost::any(
                              string(response_->headers["x-ca-request-id"]))},
                         {"statusCode", boost::any(response_->statusCode)},
                         {"statusMessage",
                          boost::any(string(response_->statusMessage))}}))}}),
              !respMap ? map<string, boost::any>() : *respMap))));
    } catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(
      Darabonba::UnretryableError(_lastRequest, _lastException));
}

AccountRevokeModel Alibabacloud_Hosting::Client::accountRevokeEx(
    shared_ptr<RevokeRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<
      map<string, boost::any>>(map<string, boost::any>(
      {{"timeouted", boost::any(string("retry"))},
       {"readTimeout", !runtime->readTimeout
                           ? boost::any()
                           : boost::any(*runtime->readTimeout)},
       {"connectTimeout", !runtime->connectTimeout
                              ? boost::any()
                              : boost::any(*runtime->connectTimeout)},
       {"localAddr",
        !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
       {"httpProxy",
        !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
       {"httpsProxy",
        !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
       {"noProxy", !runtime->noProxy ? boost::any()
                                     : boost::any(*runtime->noProxy)},
       {"maxIdleConns", !runtime->maxIdleConns
                            ? boost::any()
                            : boost::any(*runtime->maxIdleConns)},
       {"socks5Proxy", !runtime->socks5Proxy
                           ? boost::any()
                           : boost::any(*runtime->socks5Proxy)},
       {"socks5NetWork", !runtime->socks5NetWork
                             ? boost::any()
                             : boost::any(*runtime->socks5NetWork)},
       {"retry", boost::any(map<string, boost::any>(
                     {{"retryable", !runtime->autoretry
                                        ? boost::any()
                                        : boost::any(*runtime->autoretry)},
                      {"maxAttempts",
                       boost::any(Darabonba_Util::Client::defaultNumber(
                           runtime->maxAttempts, make_shared<int>(3)))}}))},
       {"backoff",
        boost::any(map<string, boost::any>(
            {{"policy",
              boost::any(string(Darabonba_Util::Client::defaultString(
                  runtime->backoffPolicy, make_shared<string>("no"))))},
             {"period", boost::any(Darabonba_Util::Client::defaultNumber(
                            runtime->backoffPeriod, make_shared<int>(1)))}}))},
       {"ignoreSSL", !runtime->ignoreSSL ? boost::any()
                                         : boost::any(*runtime->ignoreSSL)}}));
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(
      make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime =
          make_shared<int>(Darabonba::Core::getBackoffTime(
              make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ =
          make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret =
          make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken =
          make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq =
          make_shared<map<string, boost::any>>(
              Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(
          _protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(
          _nickname, make_shared<string>(string("/v2/account/revoke")));
      request_->headers = Darabonba::Converter::merge(
          map<string, string>(
              {{"user-agent", getUserAgent()},
               {"host",
                Darabonba_Util::Client::defaultString(
                    _endpoint, make_shared<string>(string(
                                   "" + *_domainId + ".auth.aliyunpds.com")))},
               {"content-type", "application/json; charset=utf-8"}}),
          !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>(
            "authorization", string("Bearer " + *accessToken + "")));
      } else if (!Darabonba_Util::Client::empty(accesskeyId) &&
                 !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(
              pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>(
            "date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(
            pair<string, string>("accept", "application/json"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(
            Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>(
            "authorization", string("acs " + *accesskeyId + ":" +
                                    Alibabacloud_ROAUtil::Client::getSignature(
                                        stringToSign, accessKeySecret) +
                                    "")));
      }
      request_->body = Darabonba::Converter::toStream(
          Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ =
          make_shared<Darabonba::Response>(
              Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(
              make_shared<int>(response_->statusCode), make_shared<int>(204))) {
        return AccountRevokeModel(
            {{"headers", boost::any(response_->headers)}});
      }
      if (!Darabonba_Util::Client::empty(
              make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(
            {{"data",
              boost::any(map<string, boost::any>(
                  {{"requestId",
                    boost::any(string(response_->headers["x-ca-request-id"]))},
                   {"statusCode", boost::any(response_->statusCode)},
                   {"statusMessage",
                    boost::any(string(response_->statusMessage))}}))},
             {"message",
              boost::any(string(response_->headers["x-ca-error-message"]))}})));
      }
      obj = make_shared<boost::any>(
          Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(
          Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(
          Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(
              map<string, boost::any>(
                  {{"data",
                    boost::any(map<string, boost::any>(
                        {{"requestId",
                          boost::any(
                              string(response_->headers["x-ca-request-id"]))},
                         {"statusCode", boost::any(response_->statusCode)},
                         {"statusMessage",
                          boost::any(string(response_->statusMessage))}}))}}),
              !respMap ? map<string, boost::any>() : *respMap))));
    } catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(
      Darabonba::UnretryableError(_lastRequest, _lastException));
}

AccountTokenModel Alibabacloud_Hosting::Client::accountTokenEx(
    shared_ptr<TokenRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<
      map<string, boost::any>>(map<string, boost::any>(
      {{"timeouted", boost::any(string("retry"))},
       {"readTimeout", !runtime->readTimeout
                           ? boost::any()
                           : boost::any(*runtime->readTimeout)},
       {"connectTimeout", !runtime->connectTimeout
                              ? boost::any()
                              : boost::any(*runtime->connectTimeout)},
       {"localAddr",
        !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
       {"httpProxy",
        !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
       {"httpsProxy",
        !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
       {"noProxy", !runtime->noProxy ? boost::any()
                                     : boost::any(*runtime->noProxy)},
       {"maxIdleConns", !runtime->maxIdleConns
                            ? boost::any()
                            : boost::any(*runtime->maxIdleConns)},
       {"socks5Proxy", !runtime->socks5Proxy
                           ? boost::any()
                           : boost::any(*runtime->socks5Proxy)},
       {"socks5NetWork", !runtime->socks5NetWork
                             ? boost::any()
                             : boost::any(*runtime->socks5NetWork)},
       {"retry", boost::any(map<string, boost::any>(
                     {{"retryable", !runtime->autoretry
                                        ? boost::any()
                                        : boost::any(*runtime->autoretry)},
                      {"maxAttempts",
                       boost::any(Darabonba_Util::Client::defaultNumber(
                           runtime->maxAttempts, make_shared<int>(3)))}}))},
       {"backoff",
        boost::any(map<string, boost::any>(
            {{"policy",
              boost::any(string(Darabonba_Util::Client::defaultString(
                  runtime->backoffPolicy, make_shared<string>("no"))))},
             {"period", boost::any(Darabonba_Util::Client::defaultNumber(
                            runtime->backoffPeriod, make_shared<int>(1)))}}))},
       {"ignoreSSL", !runtime->ignoreSSL ? boost::any()
                                         : boost::any(*runtime->ignoreSSL)}}));
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(
      make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime =
          make_shared<int>(Darabonba::Core::getBackoffTime(
              make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ =
          make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret =
          make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken =
          make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq =
          make_shared<map<string, boost::any>>(
              Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(
          _protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(
          _nickname, make_shared<string>(string("/v2/account/token")));
      request_->headers = Darabonba::Converter::merge(
          map<string, string>(
              {{"user-agent", getUserAgent()},
               {"host",
                Darabonba_Util::Client::defaultString(
                    _endpoint, make_shared<string>(string(
                                   "" + *_domainId + ".auth.aliyunpds.com")))},
               {"content-type", "application/json; charset=utf-8"}}),
          !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>(
            "authorization", string("Bearer " + *accessToken + "")));
      } else if (!Darabonba_Util::Client::empty(accesskeyId) &&
                 !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(
              pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>(
            "date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(
            pair<string, string>("accept", "application/json"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(
            Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>(
            "authorization", string("acs " + *accesskeyId + ":" +
                                    Alibabacloud_ROAUtil::Client::getSignature(
                                        stringToSign, accessKeySecret) +
                                    "")));
      }
      request_->body = Darabonba::Converter::toStream(
          Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ =
          make_shared<Darabonba::Response>(
              Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(
              make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(
            Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(
            Darabonba_Util::Client::assertAsMap(obj));
        return AccountTokenModel(
            {{"body", !respMap ? boost::any() : boost::any(*respMap)},
             {"headers", boost::any(response_->headers)}});
      }
      if (!Darabonba_Util::Client::empty(
              make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(
            {{"data",
              boost::any(map<string, boost::any>(
                  {{"requestId",
                    boost::any(string(response_->headers["x-ca-request-id"]))},
                   {"statusCode", boost::any(response_->statusCode)},
                   {"statusMessage",
                    boost::any(string(response_->statusMessage))}}))},
             {"message",
              boost::any(string(response_->headers["x-ca-error-message"]))}})));
      }
      obj = make_shared<boost::any>(
          Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(
          Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(
          Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(
              map<string, boost::any>(
                  {{"data",
                    boost::any(map<string, boost::any>(
                        {{"requestId",
                          boost::any(
                              string(response_->headers["x-ca-request-id"]))},
                         {"statusCode", boost::any(response_->statusCode)},
                         {"statusMessage",
                          boost::any(string(response_->statusMessage))}}))}}),
              !respMap ? map<string, boost::any>() : *respMap))));
    } catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(
      Darabonba::UnretryableError(_lastRequest, _lastException));
}

AdminListStoresModel Alibabacloud_Hosting::Client::adminListStoresEx(
    shared_ptr<AdminListStoresRequest> request,
    shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<
      map<string, boost::any>>(map<string, boost::any>(
      {{"timeouted", boost::any(string("retry"))},
       {"readTimeout", !runtime->readTimeout
                           ? boost::any()
                           : boost::any(*runtime->readTimeout)},
       {"connectTimeout", !runtime->connectTimeout
                              ? boost::any()
                              : boost::any(*runtime->connectTimeout)},
       {"localAddr",
        !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
       {"httpProxy",
        !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
       {"httpsProxy",
        !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
       {"noProxy", !runtime->noProxy ? boost::any()
                                     : boost::any(*runtime->noProxy)},
       {"maxIdleConns", !runtime->maxIdleConns
                            ? boost::any()
                            : boost::any(*runtime->maxIdleConns)},
       {"socks5Proxy", !runtime->socks5Proxy
                           ? boost::any()
                           : boost::any(*runtime->socks5Proxy)},
       {"socks5NetWork", !runtime->socks5NetWork
                             ? boost::any()
                             : boost::any(*runtime->socks5NetWork)},
       {"retry", boost::any(map<string, boost::any>(
                     {{"retryable", !runtime->autoretry
                                        ? boost::any()
                                        : boost::any(*runtime->autoretry)},
                      {"maxAttempts",
                       boost::any(Darabonba_Util::Client::defaultNumber(
                           runtime->maxAttempts, make_shared<int>(3)))}}))},
       {"backoff",
        boost::any(map<string, boost::any>(
            {{"policy",
              boost::any(string(Darabonba_Util::Client::defaultString(
                  runtime->backoffPolicy, make_shared<string>("no"))))},
             {"period", boost::any(Darabonba_Util::Client::defaultNumber(
                            runtime->backoffPeriod, make_shared<int>(1)))}}))},
       {"ignoreSSL", !runtime->ignoreSSL ? boost::any()
                                         : boost::any(*runtime->ignoreSSL)}}));
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(
      make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime =
          make_shared<int>(Darabonba::Core::getBackoffTime(
              make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ =
          make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret =
          make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken =
          make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq =
          make_shared<map<string, boost::any>>(
              Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(
          _protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(
          _nickname, make_shared<string>(string("/v2/domain/list_stores")));
      request_->headers = Darabonba::Converter::merge(
          map<string, string>(
              {{"user-agent", getUserAgent()},
               {"host",
                Darabonba_Util::Client::defaultString(
                    _endpoint, make_shared<string>(string(
                                   "" + *_domainId + ".api.aliyunpds.com")))},
               {"content-type", "application/json; charset=utf-8"}}),
          !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>(
            "authorization", string("Bearer " + *accessToken + "")));
      } else if (!Darabonba_Util::Client::empty(accesskeyId) &&
                 !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(
              pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>(
            "date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(
            pair<string, string>("accept", "application/json"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(
            Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>(
            "authorization", string("acs " + *accesskeyId + ":" +
                                    Alibabacloud_ROAUtil::Client::getSignature(
                                        stringToSign, accessKeySecret) +
                                    "")));
      }
      request_->body = Darabonba::Converter::toStream(
          Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ =
          make_shared<Darabonba::Response>(
              Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(
              make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(
            Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(
            Darabonba_Util::Client::assertAsMap(obj));
        return AdminListStoresModel(
            {{"body", !respMap ? boost::any() : boost::any(*respMap)},
             {"headers", boost::any(response_->headers)}});
      }
      if (!Darabonba_Util::Client::empty(
              make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(
            {{"data",
              boost::any(map<string, boost::any>(
                  {{"requestId",
                    boost::any(string(response_->headers["x-ca-request-id"]))},
                   {"statusCode", boost::any(response_->statusCode)},
                   {"statusMessage",
                    boost::any(string(response_->statusMessage))}}))},
             {"message",
              boost::any(string(response_->headers["x-ca-error-message"]))}})));
      }
      obj = make_shared<boost::any>(
          Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(
          Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(
          Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(
              map<string, boost::any>(
                  {{"data",
                    boost::any(map<string, boost::any>(
                        {{"requestId",
                          boost::any(
                              string(response_->headers["x-ca-request-id"]))},
                         {"statusCode", boost::any(response_->statusCode)},
                         {"statusMessage",
                          boost::any(string(response_->statusMessage))}}))}}),
              !respMap ? map<string, boost::any>() : *respMap))));
    } catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(
      Darabonba::UnretryableError(_lastRequest, _lastException));
}

GetUserAccessTokenModel Alibabacloud_Hosting::Client::getUserAccessTokenEx(
    shared_ptr<GetUserAccessTokenRequest> request,
    shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<
      map<string, boost::any>>(map<string, boost::any>(
      {{"timeouted", boost::any(string("retry"))},
       {"readTimeout", !runtime->readTimeout
                           ? boost::any()
                           : boost::any(*runtime->readTimeout)},
       {"connectTimeout", !runtime->connectTimeout
                              ? boost::any()
                              : boost::any(*runtime->connectTimeout)},
       {"localAddr",
        !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
       {"httpProxy",
        !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
       {"httpsProxy",
        !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
       {"noProxy", !runtime->noProxy ? boost::any()
                                     : boost::any(*runtime->noProxy)},
       {"maxIdleConns", !runtime->maxIdleConns
                            ? boost::any()
                            : boost::any(*runtime->maxIdleConns)},
       {"socks5Proxy", !runtime->socks5Proxy
                           ? boost::any()
                           : boost::any(*runtime->socks5Proxy)},
       {"socks5NetWork", !runtime->socks5NetWork
                             ? boost::any()
                             : boost::any(*runtime->socks5NetWork)},
       {"retry", boost::any(map<string, boost::any>(
                     {{"retryable", !runtime->autoretry
                                        ? boost::any()
                                        : boost::any(*runtime->autoretry)},
                      {"maxAttempts",
                       boost::any(Darabonba_Util::Client::defaultNumber(
                           runtime->maxAttempts, make_shared<int>(3)))}}))},
       {"backoff",
        boost::any(map<string, boost::any>(
            {{"policy",
              boost::any(string(Darabonba_Util::Client::defaultString(
                  runtime->backoffPolicy, make_shared<string>("no"))))},
             {"period", boost::any(Darabonba_Util::Client::defaultNumber(
                            runtime->backoffPeriod, make_shared<int>(1)))}}))},
       {"ignoreSSL", !runtime->ignoreSSL ? boost::any()
                                         : boost::any(*runtime->ignoreSSL)}}));
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(
      make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime =
          make_shared<int>(Darabonba::Core::getBackoffTime(
              make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ =
          make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret =
          make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken =
          make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq =
          make_shared<map<string, boost::any>>(
              Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(
          _protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(
          _nickname, make_shared<string>(string("/v2/user/get_access_token")));
      request_->headers = Darabonba::Converter::merge(
          map<string, string>(
              {{"user-agent", getUserAgent()},
               {"host",
                Darabonba_Util::Client::defaultString(
                    _endpoint, make_shared<string>(string(
                                   "" + *_domainId + ".api.aliyunpds.com")))},
               {"content-type", "application/json; charset=utf-8"}}),
          !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>(
            "authorization", string("Bearer " + *accessToken + "")));
      } else if (!Darabonba_Util::Client::empty(accesskeyId) &&
                 !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(
              pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>(
            "date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(
            pair<string, string>("accept", "application/json"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(
            Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>(
            "authorization", string("acs " + *accesskeyId + ":" +
                                    Alibabacloud_ROAUtil::Client::getSignature(
                                        stringToSign, accessKeySecret) +
                                    "")));
      }
      request_->body = Darabonba::Converter::toStream(
          Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ =
          make_shared<Darabonba::Response>(
              Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(
              make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(
            Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(
            Darabonba_Util::Client::assertAsMap(obj));
        return GetUserAccessTokenModel(
            {{"body", !respMap ? boost::any() : boost::any(*respMap)},
             {"headers", boost::any(response_->headers)}});
      }
      if (!Darabonba_Util::Client::empty(
              make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(
            {{"data",
              boost::any(map<string, boost::any>(
                  {{"requestId",
                    boost::any(string(response_->headers["x-ca-request-id"]))},
                   {"statusCode", boost::any(response_->statusCode)},
                   {"statusMessage",
                    boost::any(string(response_->statusMessage))}}))},
             {"message",
              boost::any(string(response_->headers["x-ca-error-message"]))}})));
      }
      obj = make_shared<boost::any>(
          Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(
          Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(
          Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(
              map<string, boost::any>(
                  {{"data",
                    boost::any(map<string, boost::any>(
                        {{"requestId",
                          boost::any(
                              string(response_->headers["x-ca-request-id"]))},
                         {"statusCode", boost::any(response_->statusCode)},
                         {"statusMessage",
                          boost::any(string(response_->statusMessage))}}))}}),
              !respMap ? map<string, boost::any>() : *respMap))));
    } catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(
      Darabonba::UnretryableError(_lastRequest, _lastException));
}

CreateDriveModel Alibabacloud_Hosting::Client::createDriveEx(
    shared_ptr<CreateDriveRequest> request,
    shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<
      map<string, boost::any>>(map<string, boost::any>(
      {{"timeouted", boost::any(string("retry"))},
       {"readTimeout", !runtime->readTimeout
                           ? boost::any()
                           : boost::any(*runtime->readTimeout)},
       {"connectTimeout", !runtime->connectTimeout
                              ? boost::any()
                              : boost::any(*runtime->connectTimeout)},
       {"localAddr",
        !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
       {"httpProxy",
        !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
       {"httpsProxy",
        !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
       {"noProxy", !runtime->noProxy ? boost::any()
                                     : boost::any(*runtime->noProxy)},
       {"maxIdleConns", !runtime->maxIdleConns
                            ? boost::any()
                            : boost::any(*runtime->maxIdleConns)},
       {"socks5Proxy", !runtime->socks5Proxy
                           ? boost::any()
                           : boost::any(*runtime->socks5Proxy)},
       {"socks5NetWork", !runtime->socks5NetWork
                             ? boost::any()
                             : boost::any(*runtime->socks5NetWork)},
       {"retry", boost::any(map<string, boost::any>(
                     {{"retryable", !runtime->autoretry
                                        ? boost::any()
                                        : boost::any(*runtime->autoretry)},
                      {"maxAttempts",
                       boost::any(Darabonba_Util::Client::defaultNumber(
                           runtime->maxAttempts, make_shared<int>(3)))}}))},
       {"backoff",
        boost::any(map<string, boost::any>(
            {{"policy",
              boost::any(string(Darabonba_Util::Client::defaultString(
                  runtime->backoffPolicy, make_shared<string>("no"))))},
             {"period", boost::any(Darabonba_Util::Client::defaultNumber(
                            runtime->backoffPeriod, make_shared<int>(1)))}}))},
       {"ignoreSSL", !runtime->ignoreSSL ? boost::any()
                                         : boost::any(*runtime->ignoreSSL)}}));
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(
      make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime =
          make_shared<int>(Darabonba::Core::getBackoffTime(
              make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ =
          make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret =
          make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken =
          make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq =
          make_shared<map<string, boost::any>>(
              Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(
          _protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(
          _nickname, make_shared<string>(string("/v2/drive/create")));
      request_->headers = Darabonba::Converter::merge(
          map<string, string>(
              {{"user-agent", getUserAgent()},
               {"host",
                Darabonba_Util::Client::defaultString(
                    _endpoint, make_shared<string>(string(
                                   "" + *_domainId + ".api.aliyunpds.com")))},
               {"content-type", "application/json; charset=utf-8"}}),
          !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>(
            "authorization", string("Bearer " + *accessToken + "")));
      } else if (!Darabonba_Util::Client::empty(accesskeyId) &&
                 !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(
              pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>(
            "date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(
            pair<string, string>("accept", "application/json"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(
            Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>(
            "authorization", string("acs " + *accesskeyId + ":" +
                                    Alibabacloud_ROAUtil::Client::getSignature(
                                        stringToSign, accessKeySecret) +
                                    "")));
      }
      request_->body = Darabonba::Converter::toStream(
          Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ =
          make_shared<Darabonba::Response>(
              Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(
              make_shared<int>(response_->statusCode), make_shared<int>(201))) {
        obj = make_shared<boost::any>(
            Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(
            Darabonba_Util::Client::assertAsMap(obj));
        return CreateDriveModel(
            {{"body", !respMap ? boost::any() : boost::any(*respMap)},
             {"headers", boost::any(response_->headers)}});
      }
      if (!Darabonba_Util::Client::empty(
              make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(
            {{"data",
              boost::any(map<string, boost::any>(
                  {{"requestId",
                    boost::any(string(response_->headers["x-ca-request-id"]))},
                   {"statusCode", boost::any(response_->statusCode)},
                   {"statusMessage",
                    boost::any(string(response_->statusMessage))}}))},
             {"message",
              boost::any(string(response_->headers["x-ca-error-message"]))}})));
      }
      obj = make_shared<boost::any>(
          Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(
          Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(
          Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(
              map<string, boost::any>(
                  {{"data",
                    boost::any(map<string, boost::any>(
                        {{"requestId",
                          boost::any(
                              string(response_->headers["x-ca-request-id"]))},
                         {"statusCode", boost::any(response_->statusCode)},
                         {"statusMessage",
                          boost::any(string(response_->statusMessage))}}))}}),
              !respMap ? map<string, boost::any>() : *respMap))));
    } catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(
      Darabonba::UnretryableError(_lastRequest, _lastException));
}

DeleteDriveModel Alibabacloud_Hosting::Client::deleteDriveEx(
    shared_ptr<DeleteDriveRequest> request,
    shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<
      map<string, boost::any>>(map<string, boost::any>(
      {{"timeouted", boost::any(string("retry"))},
       {"readTimeout", !runtime->readTimeout
                           ? boost::any()
                           : boost::any(*runtime->readTimeout)},
       {"connectTimeout", !runtime->connectTimeout
                              ? boost::any()
                              : boost::any(*runtime->connectTimeout)},
       {"localAddr",
        !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
       {"httpProxy",
        !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
       {"httpsProxy",
        !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
       {"noProxy", !runtime->noProxy ? boost::any()
                                     : boost::any(*runtime->noProxy)},
       {"maxIdleConns", !runtime->maxIdleConns
                            ? boost::any()
                            : boost::any(*runtime->maxIdleConns)},
       {"socks5Proxy", !runtime->socks5Proxy
                           ? boost::any()
                           : boost::any(*runtime->socks5Proxy)},
       {"socks5NetWork", !runtime->socks5NetWork
                             ? boost::any()
                             : boost::any(*runtime->socks5NetWork)},
       {"retry", boost::any(map<string, boost::any>(
                     {{"retryable", !runtime->autoretry
                                        ? boost::any()
                                        : boost::any(*runtime->autoretry)},
                      {"maxAttempts",
                       boost::any(Darabonba_Util::Client::defaultNumber(
                           runtime->maxAttempts, make_shared<int>(3)))}}))},
       {"backoff",
        boost::any(map<string, boost::any>(
            {{"policy",
              boost::any(string(Darabonba_Util::Client::defaultString(
                  runtime->backoffPolicy, make_shared<string>("no"))))},
             {"period", boost::any(Darabonba_Util::Client::defaultNumber(
                            runtime->backoffPeriod, make_shared<int>(1)))}}))},
       {"ignoreSSL", !runtime->ignoreSSL ? boost::any()
                                         : boost::any(*runtime->ignoreSSL)}}));
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(
      make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime =
          make_shared<int>(Darabonba::Core::getBackoffTime(
              make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ =
          make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret =
          make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken =
          make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq =
          make_shared<map<string, boost::any>>(
              Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(
          _protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(
          _nickname, make_shared<string>(string("/v2/drive/delete")));
      request_->headers = Darabonba::Converter::merge(
          map<string, string>(
              {{"user-agent", getUserAgent()},
               {"host",
                Darabonba_Util::Client::defaultString(
                    _endpoint, make_shared<string>(string(
                                   "" + *_domainId + ".api.aliyunpds.com")))},
               {"content-type", "application/json; charset=utf-8"}}),
          !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>(
            "authorization", string("Bearer " + *accessToken + "")));
      } else if (!Darabonba_Util::Client::empty(accesskeyId) &&
                 !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(
              pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>(
            "date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(
            pair<string, string>("accept", "application/json"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(
            Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>(
            "authorization", string("acs " + *accesskeyId + ":" +
                                    Alibabacloud_ROAUtil::Client::getSignature(
                                        stringToSign, accessKeySecret) +
                                    "")));
      }
      request_->body = Darabonba::Converter::toStream(
          Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ =
          make_shared<Darabonba::Response>(
              Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(
              make_shared<int>(response_->statusCode), make_shared<int>(204))) {
        return DeleteDriveModel({{"headers", boost::any(response_->headers)}});
      }
      if (!Darabonba_Util::Client::empty(
              make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(
            {{"data",
              boost::any(map<string, boost::any>(
                  {{"requestId",
                    boost::any(string(response_->headers["x-ca-request-id"]))},
                   {"statusCode", boost::any(response_->statusCode)},
                   {"statusMessage",
                    boost::any(string(response_->statusMessage))}}))},
             {"message",
              boost::any(string(response_->headers["x-ca-error-message"]))}})));
      }
      obj = make_shared<boost::any>(
          Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(
          Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(
          Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(
              map<string, boost::any>(
                  {{"data",
                    boost::any(map<string, boost::any>(
                        {{"requestId",
                          boost::any(
                              string(response_->headers["x-ca-request-id"]))},
                         {"statusCode", boost::any(response_->statusCode)},
                         {"statusMessage",
                          boost::any(string(response_->statusMessage))}}))}}),
              !respMap ? map<string, boost::any>() : *respMap))));
    } catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(
      Darabonba::UnretryableError(_lastRequest, _lastException));
}

GetDriveModel
Alibabacloud_Hosting::Client::getDriveEx(shared_ptr<GetDriveRequest> request,
                                         shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<
      map<string, boost::any>>(map<string, boost::any>(
      {{"timeouted", boost::any(string("retry"))},
       {"readTimeout", !runtime->readTimeout
                           ? boost::any()
                           : boost::any(*runtime->readTimeout)},
       {"connectTimeout", !runtime->connectTimeout
                              ? boost::any()
                              : boost::any(*runtime->connectTimeout)},
       {"localAddr",
        !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
       {"httpProxy",
        !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
       {"httpsProxy",
        !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
       {"noProxy", !runtime->noProxy ? boost::any()
                                     : boost::any(*runtime->noProxy)},
       {"maxIdleConns", !runtime->maxIdleConns
                            ? boost::any()
                            : boost::any(*runtime->maxIdleConns)},
       {"socks5Proxy", !runtime->socks5Proxy
                           ? boost::any()
                           : boost::any(*runtime->socks5Proxy)},
       {"socks5NetWork", !runtime->socks5NetWork
                             ? boost::any()
                             : boost::any(*runtime->socks5NetWork)},
       {"retry", boost::any(map<string, boost::any>(
                     {{"retryable", !runtime->autoretry
                                        ? boost::any()
                                        : boost::any(*runtime->autoretry)},
                      {"maxAttempts",
                       boost::any(Darabonba_Util::Client::defaultNumber(
                           runtime->maxAttempts, make_shared<int>(3)))}}))},
       {"backoff",
        boost::any(map<string, boost::any>(
            {{"policy",
              boost::any(string(Darabonba_Util::Client::defaultString(
                  runtime->backoffPolicy, make_shared<string>("no"))))},
             {"period", boost::any(Darabonba_Util::Client::defaultNumber(
                            runtime->backoffPeriod, make_shared<int>(1)))}}))},
       {"ignoreSSL", !runtime->ignoreSSL ? boost::any()
                                         : boost::any(*runtime->ignoreSSL)}}));
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(
      make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime =
          make_shared<int>(Darabonba::Core::getBackoffTime(
              make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ =
          make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret =
          make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken =
          make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq =
          make_shared<map<string, boost::any>>(
              Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(
          _protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname =
          getPathname(_nickname, make_shared<string>(string("/v2/drive/get")));
      request_->headers = Darabonba::Converter::merge(
          map<string, string>(
              {{"user-agent", getUserAgent()},
               {"host",
                Darabonba_Util::Client::defaultString(
                    _endpoint, make_shared<string>(string(
                                   "" + *_domainId + ".api.aliyunpds.com")))},
               {"content-type", "application/json; charset=utf-8"}}),
          !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>(
            "authorization", string("Bearer " + *accessToken + "")));
      } else if (!Darabonba_Util::Client::empty(accesskeyId) &&
                 !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(
              pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>(
            "date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(
            pair<string, string>("accept", "application/json"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(
            Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>(
            "authorization", string("acs " + *accesskeyId + ":" +
                                    Alibabacloud_ROAUtil::Client::getSignature(
                                        stringToSign, accessKeySecret) +
                                    "")));
      }
      request_->body = Darabonba::Converter::toStream(
          Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ =
          make_shared<Darabonba::Response>(
              Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(
              make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(
            Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(
            Darabonba_Util::Client::assertAsMap(obj));
        return GetDriveModel(
            {{"body", !respMap ? boost::any() : boost::any(*respMap)},
             {"headers", boost::any(response_->headers)}});
      }
      if (!Darabonba_Util::Client::empty(
              make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(
            {{"data",
              boost::any(map<string, boost::any>(
                  {{"requestId",
                    boost::any(string(response_->headers["x-ca-request-id"]))},
                   {"statusCode", boost::any(response_->statusCode)},
                   {"statusMessage",
                    boost::any(string(response_->statusMessage))}}))},
             {"message",
              boost::any(string(response_->headers["x-ca-error-message"]))}})));
      }
      obj = make_shared<boost::any>(
          Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(
          Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(
          Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(
              map<string, boost::any>(
                  {{"data",
                    boost::any(map<string, boost::any>(
                        {{"requestId",
                          boost::any(
                              string(response_->headers["x-ca-request-id"]))},
                         {"statusCode", boost::any(response_->statusCode)},
                         {"statusMessage",
                          boost::any(string(response_->statusMessage))}}))}}),
              !respMap ? map<string, boost::any>() : *respMap))));
    } catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(
      Darabonba::UnretryableError(_lastRequest, _lastException));
}

GetDefaultDriveModel Alibabacloud_Hosting::Client::getDefaultDriveEx(
    shared_ptr<GetDefaultDriveRequest> request,
    shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<
      map<string, boost::any>>(map<string, boost::any>(
      {{"timeouted", boost::any(string("retry"))},
       {"readTimeout", !runtime->readTimeout
                           ? boost::any()
                           : boost::any(*runtime->readTimeout)},
       {"connectTimeout", !runtime->connectTimeout
                              ? boost::any()
                              : boost::any(*runtime->connectTimeout)},
       {"localAddr",
        !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
       {"httpProxy",
        !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
       {"httpsProxy",
        !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
       {"noProxy", !runtime->noProxy ? boost::any()
                                     : boost::any(*runtime->noProxy)},
       {"maxIdleConns", !runtime->maxIdleConns
                            ? boost::any()
                            : boost::any(*runtime->maxIdleConns)},
       {"socks5Proxy", !runtime->socks5Proxy
                           ? boost::any()
                           : boost::any(*runtime->socks5Proxy)},
       {"socks5NetWork", !runtime->socks5NetWork
                             ? boost::any()
                             : boost::any(*runtime->socks5NetWork)},
       {"retry", boost::any(map<string, boost::any>(
                     {{"retryable", !runtime->autoretry
                                        ? boost::any()
                                        : boost::any(*runtime->autoretry)},
                      {"maxAttempts",
                       boost::any(Darabonba_Util::Client::defaultNumber(
                           runtime->maxAttempts, make_shared<int>(3)))}}))},
       {"backoff",
        boost::any(map<string, boost::any>(
            {{"policy",
              boost::any(string(Darabonba_Util::Client::defaultString(
                  runtime->backoffPolicy, make_shared<string>("no"))))},
             {"period", boost::any(Darabonba_Util::Client::defaultNumber(
                            runtime->backoffPeriod, make_shared<int>(1)))}}))},
       {"ignoreSSL", !runtime->ignoreSSL ? boost::any()
                                         : boost::any(*runtime->ignoreSSL)}}));
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(
      make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime =
          make_shared<int>(Darabonba::Core::getBackoffTime(
              make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ =
          make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret =
          make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken =
          make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq =
          make_shared<map<string, boost::any>>(
              Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(
          _protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(
          _nickname,
          make_shared<string>(string("/v2/drive/get_default_drive")));
      request_->headers = Darabonba::Converter::merge(
          map<string, string>(
              {{"user-agent", getUserAgent()},
               {"host",
                Darabonba_Util::Client::defaultString(
                    _endpoint, make_shared<string>(string(
                                   "" + *_domainId + ".api.aliyunpds.com")))},
               {"content-type", "application/json; charset=utf-8"}}),
          !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>(
            "authorization", string("Bearer " + *accessToken + "")));
      } else if (!Darabonba_Util::Client::empty(accesskeyId) &&
                 !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(
              pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>(
            "date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(
            pair<string, string>("accept", "application/json"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(
            Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>(
            "authorization", string("acs " + *accesskeyId + ":" +
                                    Alibabacloud_ROAUtil::Client::getSignature(
                                        stringToSign, accessKeySecret) +
                                    "")));
      }
      request_->body = Darabonba::Converter::toStream(
          Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ =
          make_shared<Darabonba::Response>(
              Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(
              make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(
            Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(
            Darabonba_Util::Client::assertAsMap(obj));
        return GetDefaultDriveModel(
            {{"body", !respMap ? boost::any() : boost::any(*respMap)},
             {"headers", boost::any(response_->headers)}});
      }
      if (!Darabonba_Util::Client::empty(
              make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(
            {{"data",
              boost::any(map<string, boost::any>(
                  {{"requestId",
                    boost::any(string(response_->headers["x-ca-request-id"]))},
                   {"statusCode", boost::any(response_->statusCode)},
                   {"statusMessage",
                    boost::any(string(response_->statusMessage))}}))},
             {"message",
              boost::any(string(response_->headers["x-ca-error-message"]))}})));
      }
      obj = make_shared<boost::any>(
          Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(
          Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(
          Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(
              map<string, boost::any>(
                  {{"data",
                    boost::any(map<string, boost::any>(
                        {{"requestId",
                          boost::any(
                              string(response_->headers["x-ca-request-id"]))},
                         {"statusCode", boost::any(response_->statusCode)},
                         {"statusMessage",
                          boost::any(string(response_->statusMessage))}}))}}),
              !respMap ? map<string, boost::any>() : *respMap))));
    } catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(
      Darabonba::UnretryableError(_lastRequest, _lastException));
}

ListDrivesModel
Alibabacloud_Hosting::Client::listDrivesEx(shared_ptr<ListDriveRequest> request,
                                           shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<
      map<string, boost::any>>(map<string, boost::any>(
      {{"timeouted", boost::any(string("retry"))},
       {"readTimeout", !runtime->readTimeout
                           ? boost::any()
                           : boost::any(*runtime->readTimeout)},
       {"connectTimeout", !runtime->connectTimeout
                              ? boost::any()
                              : boost::any(*runtime->connectTimeout)},
       {"localAddr",
        !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
       {"httpProxy",
        !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
       {"httpsProxy",
        !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
       {"noProxy", !runtime->noProxy ? boost::any()
                                     : boost::any(*runtime->noProxy)},
       {"maxIdleConns", !runtime->maxIdleConns
                            ? boost::any()
                            : boost::any(*runtime->maxIdleConns)},
       {"socks5Proxy", !runtime->socks5Proxy
                           ? boost::any()
                           : boost::any(*runtime->socks5Proxy)},
       {"socks5NetWork", !runtime->socks5NetWork
                             ? boost::any()
                             : boost::any(*runtime->socks5NetWork)},
       {"retry", boost::any(map<string, boost::any>(
                     {{"retryable", !runtime->autoretry
                                        ? boost::any()
                                        : boost::any(*runtime->autoretry)},
                      {"maxAttempts",
                       boost::any(Darabonba_Util::Client::defaultNumber(
                           runtime->maxAttempts, make_shared<int>(3)))}}))},
       {"backoff",
        boost::any(map<string, boost::any>(
            {{"policy",
              boost::any(string(Darabonba_Util::Client::defaultString(
                  runtime->backoffPolicy, make_shared<string>("no"))))},
             {"period", boost::any(Darabonba_Util::Client::defaultNumber(
                            runtime->backoffPeriod, make_shared<int>(1)))}}))},
       {"ignoreSSL", !runtime->ignoreSSL ? boost::any()
                                         : boost::any(*runtime->ignoreSSL)}}));
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(
      make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime =
          make_shared<int>(Darabonba::Core::getBackoffTime(
              make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ =
          make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret =
          make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken =
          make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq =
          make_shared<map<string, boost::any>>(
              Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(
          _protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname =
          getPathname(_nickname, make_shared<string>(string("/v2/drive/list")));
      request_->headers = Darabonba::Converter::merge(
          map<string, string>(
              {{"user-agent", getUserAgent()},
               {"host",
                Darabonba_Util::Client::defaultString(
                    _endpoint, make_shared<string>(string(
                                   "" + *_domainId + ".api.aliyunpds.com")))},
               {"content-type", "application/json; charset=utf-8"}}),
          !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>(
            "authorization", string("Bearer " + *accessToken + "")));
      } else if (!Darabonba_Util::Client::empty(accesskeyId) &&
                 !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(
              pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>(
            "date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(
            pair<string, string>("accept", "application/json"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(
            Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>(
            "authorization", string("acs " + *accesskeyId + ":" +
                                    Alibabacloud_ROAUtil::Client::getSignature(
                                        stringToSign, accessKeySecret) +
                                    "")));
      }
      request_->body = Darabonba::Converter::toStream(
          Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ =
          make_shared<Darabonba::Response>(
              Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(
              make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(
            Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(
            Darabonba_Util::Client::assertAsMap(obj));
        return ListDrivesModel(
            {{"body", !respMap ? boost::any() : boost::any(*respMap)},
             {"headers", boost::any(response_->headers)}});
      }
      if (!Darabonba_Util::Client::empty(
              make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(
            {{"data",
              boost::any(map<string, boost::any>(
                  {{"requestId",
                    boost::any(string(response_->headers["x-ca-request-id"]))},
                   {"statusCode", boost::any(response_->statusCode)},
                   {"statusMessage",
                    boost::any(string(response_->statusMessage))}}))},
             {"message",
              boost::any(string(response_->headers["x-ca-error-message"]))}})));
      }
      obj = make_shared<boost::any>(
          Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(
          Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(
          Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(
              map<string, boost::any>(
                  {{"data",
                    boost::any(map<string, boost::any>(
                        {{"requestId",
                          boost::any(
                              string(response_->headers["x-ca-request-id"]))},
                         {"statusCode", boost::any(response_->statusCode)},
                         {"statusMessage",
                          boost::any(string(response_->statusMessage))}}))}}),
              !respMap ? map<string, boost::any>() : *respMap))));
    } catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(
      Darabonba::UnretryableError(_lastRequest, _lastException));
}

ListMyDrivesModel Alibabacloud_Hosting::Client::listMyDrivesEx(
    shared_ptr<ListMyDriveRequest> request,
    shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<
      map<string, boost::any>>(map<string, boost::any>(
      {{"timeouted", boost::any(string("retry"))},
       {"readTimeout", !runtime->readTimeout
                           ? boost::any()
                           : boost::any(*runtime->readTimeout)},
       {"connectTimeout", !runtime->connectTimeout
                              ? boost::any()
                              : boost::any(*runtime->connectTimeout)},
       {"localAddr",
        !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
       {"httpProxy",
        !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
       {"httpsProxy",
        !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
       {"noProxy", !runtime->noProxy ? boost::any()
                                     : boost::any(*runtime->noProxy)},
       {"maxIdleConns", !runtime->maxIdleConns
                            ? boost::any()
                            : boost::any(*runtime->maxIdleConns)},
       {"socks5Proxy", !runtime->socks5Proxy
                           ? boost::any()
                           : boost::any(*runtime->socks5Proxy)},
       {"socks5NetWork", !runtime->socks5NetWork
                             ? boost::any()
                             : boost::any(*runtime->socks5NetWork)},
       {"retry", boost::any(map<string, boost::any>(
                     {{"retryable", !runtime->autoretry
                                        ? boost::any()
                                        : boost::any(*runtime->autoretry)},
                      {"maxAttempts",
                       boost::any(Darabonba_Util::Client::defaultNumber(
                           runtime->maxAttempts, make_shared<int>(3)))}}))},
       {"backoff",
        boost::any(map<string, boost::any>(
            {{"policy",
              boost::any(string(Darabonba_Util::Client::defaultString(
                  runtime->backoffPolicy, make_shared<string>("no"))))},
             {"period", boost::any(Darabonba_Util::Client::defaultNumber(
                            runtime->backoffPeriod, make_shared<int>(1)))}}))},
       {"ignoreSSL", !runtime->ignoreSSL ? boost::any()
                                         : boost::any(*runtime->ignoreSSL)}}));
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(
      make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime =
          make_shared<int>(Darabonba::Core::getBackoffTime(
              make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ =
          make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret =
          make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken =
          make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq =
          make_shared<map<string, boost::any>>(
              Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(
          _protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(
          _nickname, make_shared<string>(string("/v2/drive/list_my_drives")));
      request_->headers = Darabonba::Converter::merge(
          map<string, string>(
              {{"user-agent", getUserAgent()},
               {"host",
                Darabonba_Util::Client::defaultString(
                    _endpoint, make_shared<string>(string(
                                   "" + *_domainId + ".api.aliyunpds.com")))},
               {"content-type", "application/json; charset=utf-8"}}),
          !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>(
            "authorization", string("Bearer " + *accessToken + "")));
      } else if (!Darabonba_Util::Client::empty(accesskeyId) &&
                 !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(
              pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>(
            "date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(
            pair<string, string>("accept", "application/json"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(
            Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>(
            "authorization", string("acs " + *accesskeyId + ":" +
                                    Alibabacloud_ROAUtil::Client::getSignature(
                                        stringToSign, accessKeySecret) +
                                    "")));
      }
      request_->body = Darabonba::Converter::toStream(
          Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ =
          make_shared<Darabonba::Response>(
              Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(
              make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(
            Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(
            Darabonba_Util::Client::assertAsMap(obj));
        return ListMyDrivesModel(
            {{"body", !respMap ? boost::any() : boost::any(*respMap)},
             {"headers", boost::any(response_->headers)}});
      }
      if (!Darabonba_Util::Client::empty(
              make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(
            {{"data",
              boost::any(map<string, boost::any>(
                  {{"requestId",
                    boost::any(string(response_->headers["x-ca-request-id"]))},
                   {"statusCode", boost::any(response_->statusCode)},
                   {"statusMessage",
                    boost::any(string(response_->statusMessage))}}))},
             {"message",
              boost::any(string(response_->headers["x-ca-error-message"]))}})));
      }
      obj = make_shared<boost::any>(
          Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(
          Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(
          Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(
              map<string, boost::any>(
                  {{"data",
                    boost::any(map<string, boost::any>(
                        {{"requestId",
                          boost::any(
                              string(response_->headers["x-ca-request-id"]))},
                         {"statusCode", boost::any(response_->statusCode)},
                         {"statusMessage",
                          boost::any(string(response_->statusMessage))}}))}}),
              !respMap ? map<string, boost::any>() : *respMap))));
    } catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(
      Darabonba::UnretryableError(_lastRequest, _lastException));
}

UpdateDriveModel Alibabacloud_Hosting::Client::updateDriveEx(
    shared_ptr<UpdateDriveRequest> request,
    shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<
      map<string, boost::any>>(map<string, boost::any>(
      {{"timeouted", boost::any(string("retry"))},
       {"readTimeout", !runtime->readTimeout
                           ? boost::any()
                           : boost::any(*runtime->readTimeout)},
       {"connectTimeout", !runtime->connectTimeout
                              ? boost::any()
                              : boost::any(*runtime->connectTimeout)},
       {"localAddr",
        !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
       {"httpProxy",
        !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
       {"httpsProxy",
        !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
       {"noProxy", !runtime->noProxy ? boost::any()
                                     : boost::any(*runtime->noProxy)},
       {"maxIdleConns", !runtime->maxIdleConns
                            ? boost::any()
                            : boost::any(*runtime->maxIdleConns)},
       {"socks5Proxy", !runtime->socks5Proxy
                           ? boost::any()
                           : boost::any(*runtime->socks5Proxy)},
       {"socks5NetWork", !runtime->socks5NetWork
                             ? boost::any()
                             : boost::any(*runtime->socks5NetWork)},
       {"retry", boost::any(map<string, boost::any>(
                     {{"retryable", !runtime->autoretry
                                        ? boost::any()
                                        : boost::any(*runtime->autoretry)},
                      {"maxAttempts",
                       boost::any(Darabonba_Util::Client::defaultNumber(
                           runtime->maxAttempts, make_shared<int>(3)))}}))},
       {"backoff",
        boost::any(map<string, boost::any>(
            {{"policy",
              boost::any(string(Darabonba_Util::Client::defaultString(
                  runtime->backoffPolicy, make_shared<string>("no"))))},
             {"period", boost::any(Darabonba_Util::Client::defaultNumber(
                            runtime->backoffPeriod, make_shared<int>(1)))}}))},
       {"ignoreSSL", !runtime->ignoreSSL ? boost::any()
                                         : boost::any(*runtime->ignoreSSL)}}));
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(
      make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime =
          make_shared<int>(Darabonba::Core::getBackoffTime(
              make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ =
          make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret =
          make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken =
          make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq =
          make_shared<map<string, boost::any>>(
              Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(
          _protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(
          _nickname, make_shared<string>(string("/v2/drive/update")));
      request_->headers = Darabonba::Converter::merge(
          map<string, string>(
              {{"user-agent", getUserAgent()},
               {"host",
                Darabonba_Util::Client::defaultString(
                    _endpoint, make_shared<string>(string(
                                   "" + *_domainId + ".api.aliyunpds.com")))},
               {"content-type", "application/json; charset=utf-8"}}),
          !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>(
            "authorization", string("Bearer " + *accessToken + "")));
      } else if (!Darabonba_Util::Client::empty(accesskeyId) &&
                 !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(
              pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>(
            "date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(
            pair<string, string>("accept", "application/json"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(
            Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>(
            "authorization", string("acs " + *accesskeyId + ":" +
                                    Alibabacloud_ROAUtil::Client::getSignature(
                                        stringToSign, accessKeySecret) +
                                    "")));
      }
      request_->body = Darabonba::Converter::toStream(
          Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ =
          make_shared<Darabonba::Response>(
              Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(
              make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(
            Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(
            Darabonba_Util::Client::assertAsMap(obj));
        return UpdateDriveModel(
            {{"body", !respMap ? boost::any() : boost::any(*respMap)},
             {"headers", boost::any(response_->headers)}});
      }
      if (!Darabonba_Util::Client::empty(
              make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(
            {{"data",
              boost::any(map<string, boost::any>(
                  {{"requestId",
                    boost::any(string(response_->headers["x-ca-request-id"]))},
                   {"statusCode", boost::any(response_->statusCode)},
                   {"statusMessage",
                    boost::any(string(response_->statusMessage))}}))},
             {"message",
              boost::any(string(response_->headers["x-ca-error-message"]))}})));
      }
      obj = make_shared<boost::any>(
          Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(
          Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(
          Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(
              map<string, boost::any>(
                  {{"data",
                    boost::any(map<string, boost::any>(
                        {{"requestId",
                          boost::any(
                              string(response_->headers["x-ca-request-id"]))},
                         {"statusCode", boost::any(response_->statusCode)},
                         {"statusMessage",
                          boost::any(string(response_->statusMessage))}}))}}),
              !respMap ? map<string, boost::any>() : *respMap))));
    } catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(
      Darabonba::UnretryableError(_lastRequest, _lastException));
}

CompleteFileModel Alibabacloud_Hosting::Client::completeFileEx(
    shared_ptr<HostingCompleteFileRequest> request,
    shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<
      map<string, boost::any>>(map<string, boost::any>(
      {{"timeouted", boost::any(string("retry"))},
       {"readTimeout", !runtime->readTimeout
                           ? boost::any()
                           : boost::any(*runtime->readTimeout)},
       {"connectTimeout", !runtime->connectTimeout
                              ? boost::any()
                              : boost::any(*runtime->connectTimeout)},
       {"localAddr",
        !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
       {"httpProxy",
        !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
       {"httpsProxy",
        !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
       {"noProxy", !runtime->noProxy ? boost::any()
                                     : boost::any(*runtime->noProxy)},
       {"maxIdleConns", !runtime->maxIdleConns
                            ? boost::any()
                            : boost::any(*runtime->maxIdleConns)},
       {"socks5Proxy", !runtime->socks5Proxy
                           ? boost::any()
                           : boost::any(*runtime->socks5Proxy)},
       {"socks5NetWork", !runtime->socks5NetWork
                             ? boost::any()
                             : boost::any(*runtime->socks5NetWork)},
       {"retry", boost::any(map<string, boost::any>(
                     {{"retryable", !runtime->autoretry
                                        ? boost::any()
                                        : boost::any(*runtime->autoretry)},
                      {"maxAttempts",
                       boost::any(Darabonba_Util::Client::defaultNumber(
                           runtime->maxAttempts, make_shared<int>(3)))}}))},
       {"backoff",
        boost::any(map<string, boost::any>(
            {{"policy",
              boost::any(string(Darabonba_Util::Client::defaultString(
                  runtime->backoffPolicy, make_shared<string>("no"))))},
             {"period", boost::any(Darabonba_Util::Client::defaultNumber(
                            runtime->backoffPeriod, make_shared<int>(1)))}}))},
       {"ignoreSSL", !runtime->ignoreSSL ? boost::any()
                                         : boost::any(*runtime->ignoreSSL)}}));
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(
      make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime =
          make_shared<int>(Darabonba::Core::getBackoffTime(
              make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ =
          make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret =
          make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken =
          make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq =
          make_shared<map<string, boost::any>>(
              Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(
          _protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(
          _nickname, make_shared<string>(string("/v2/hosting/file/complete")));
      request_->headers = Darabonba::Converter::merge(
          map<string, string>(
              {{"user-agent", getUserAgent()},
               {"host",
                Darabonba_Util::Client::defaultString(
                    _endpoint, make_shared<string>(string(
                                   "" + *_domainId + ".api.aliyunpds.com")))},
               {"content-type", "application/json; charset=utf-8"}}),
          !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>(
            "authorization", string("Bearer " + *accessToken + "")));
      } else if (!Darabonba_Util::Client::empty(accesskeyId) &&
                 !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(
              pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>(
            "date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(
            pair<string, string>("accept", "application/json"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(
            Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>(
            "authorization", string("acs " + *accesskeyId + ":" +
                                    Alibabacloud_ROAUtil::Client::getSignature(
                                        stringToSign, accessKeySecret) +
                                    "")));
      }
      request_->body = Darabonba::Converter::toStream(
          Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ =
          make_shared<Darabonba::Response>(
              Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(
              make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(
            Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(
            Darabonba_Util::Client::assertAsMap(obj));
        return CompleteFileModel(
            {{"body", !respMap ? boost::any() : boost::any(*respMap)},
             {"headers", boost::any(response_->headers)}});
      }
      if (!Darabonba_Util::Client::empty(
              make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(
            {{"data",
              boost::any(map<string, boost::any>(
                  {{"requestId",
                    boost::any(string(response_->headers["x-ca-request-id"]))},
                   {"statusCode", boost::any(response_->statusCode)},
                   {"statusMessage",
                    boost::any(string(response_->statusMessage))}}))},
             {"message",
              boost::any(string(response_->headers["x-ca-error-message"]))}})));
      }
      obj = make_shared<boost::any>(
          Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(
          Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(
          Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(
              map<string, boost::any>(
                  {{"data",
                    boost::any(map<string, boost::any>(
                        {{"requestId",
                          boost::any(
                              string(response_->headers["x-ca-request-id"]))},
                         {"statusCode", boost::any(response_->statusCode)},
                         {"statusMessage",
                          boost::any(string(response_->statusMessage))}}))}}),
              !respMap ? map<string, boost::any>() : *respMap))));
    } catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(
      Darabonba::UnretryableError(_lastRequest, _lastException));
}

CopyFileModel Alibabacloud_Hosting::Client::copyFileEx(
    shared_ptr<HostingCopyFileRequest> request,
    shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<
      map<string, boost::any>>(map<string, boost::any>(
      {{"timeouted", boost::any(string("retry"))},
       {"readTimeout", !runtime->readTimeout
                           ? boost::any()
                           : boost::any(*runtime->readTimeout)},
       {"connectTimeout", !runtime->connectTimeout
                              ? boost::any()
                              : boost::any(*runtime->connectTimeout)},
       {"localAddr",
        !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
       {"httpProxy",
        !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
       {"httpsProxy",
        !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
       {"noProxy", !runtime->noProxy ? boost::any()
                                     : boost::any(*runtime->noProxy)},
       {"maxIdleConns", !runtime->maxIdleConns
                            ? boost::any()
                            : boost::any(*runtime->maxIdleConns)},
       {"socks5Proxy", !runtime->socks5Proxy
                           ? boost::any()
                           : boost::any(*runtime->socks5Proxy)},
       {"socks5NetWork", !runtime->socks5NetWork
                             ? boost::any()
                             : boost::any(*runtime->socks5NetWork)},
       {"retry", boost::any(map<string, boost::any>(
                     {{"retryable", !runtime->autoretry
                                        ? boost::any()
                                        : boost::any(*runtime->autoretry)},
                      {"maxAttempts",
                       boost::any(Darabonba_Util::Client::defaultNumber(
                           runtime->maxAttempts, make_shared<int>(3)))}}))},
       {"backoff",
        boost::any(map<string, boost::any>(
            {{"policy",
              boost::any(string(Darabonba_Util::Client::defaultString(
                  runtime->backoffPolicy, make_shared<string>("no"))))},
             {"period", boost::any(Darabonba_Util::Client::defaultNumber(
                            runtime->backoffPeriod, make_shared<int>(1)))}}))},
       {"ignoreSSL", !runtime->ignoreSSL ? boost::any()
                                         : boost::any(*runtime->ignoreSSL)}}));
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(
      make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime =
          make_shared<int>(Darabonba::Core::getBackoffTime(
              make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ =
          make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret =
          make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken =
          make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq =
          make_shared<map<string, boost::any>>(
              Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(
          _protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(
          _nickname, make_shared<string>(string("/v2/hosting/file/copy")));
      request_->headers = Darabonba::Converter::merge(
          map<string, string>(
              {{"user-agent", getUserAgent()},
               {"host",
                Darabonba_Util::Client::defaultString(
                    _endpoint, make_shared<string>(string(
                                   "" + *_domainId + ".api.aliyunpds.com")))},
               {"content-type", "application/json; charset=utf-8"}}),
          !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>(
            "authorization", string("Bearer " + *accessToken + "")));
      } else if (!Darabonba_Util::Client::empty(accesskeyId) &&
                 !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(
              pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>(
            "date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(
            pair<string, string>("accept", "application/json"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(
            Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>(
            "authorization", string("acs " + *accesskeyId + ":" +
                                    Alibabacloud_ROAUtil::Client::getSignature(
                                        stringToSign, accessKeySecret) +
                                    "")));
      }
      request_->body = Darabonba::Converter::toStream(
          Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ =
          make_shared<Darabonba::Response>(
              Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(
              make_shared<int>(response_->statusCode), make_shared<int>(201))) {
        obj = make_shared<boost::any>(
            Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(
            Darabonba_Util::Client::assertAsMap(obj));
        return CopyFileModel(
            {{"body", !respMap ? boost::any() : boost::any(*respMap)},
             {"headers", boost::any(response_->headers)}});
      }
      if (!Darabonba_Util::Client::empty(
              make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(
            {{"data",
              boost::any(map<string, boost::any>(
                  {{"requestId",
                    boost::any(string(response_->headers["x-ca-request-id"]))},
                   {"statusCode", boost::any(response_->statusCode)},
                   {"statusMessage",
                    boost::any(string(response_->statusMessage))}}))},
             {"message",
              boost::any(string(response_->headers["x-ca-error-message"]))}})));
      }
      obj = make_shared<boost::any>(
          Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(
          Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(
          Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(
              map<string, boost::any>(
                  {{"data",
                    boost::any(map<string, boost::any>(
                        {{"requestId",
                          boost::any(
                              string(response_->headers["x-ca-request-id"]))},
                         {"statusCode", boost::any(response_->statusCode)},
                         {"statusMessage",
                          boost::any(string(response_->statusMessage))}}))}}),
              !respMap ? map<string, boost::any>() : *respMap))));
    } catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(
      Darabonba::UnretryableError(_lastRequest, _lastException));
}

CreateFileModel Alibabacloud_Hosting::Client::createFileEx(
    shared_ptr<HostingCreateFileRequest> request,
    shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<
      map<string, boost::any>>(map<string, boost::any>(
      {{"timeouted", boost::any(string("retry"))},
       {"readTimeout", !runtime->readTimeout
                           ? boost::any()
                           : boost::any(*runtime->readTimeout)},
       {"connectTimeout", !runtime->connectTimeout
                              ? boost::any()
                              : boost::any(*runtime->connectTimeout)},
       {"localAddr",
        !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
       {"httpProxy",
        !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
       {"httpsProxy",
        !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
       {"noProxy", !runtime->noProxy ? boost::any()
                                     : boost::any(*runtime->noProxy)},
       {"maxIdleConns", !runtime->maxIdleConns
                            ? boost::any()
                            : boost::any(*runtime->maxIdleConns)},
       {"socks5Proxy", !runtime->socks5Proxy
                           ? boost::any()
                           : boost::any(*runtime->socks5Proxy)},
       {"socks5NetWork", !runtime->socks5NetWork
                             ? boost::any()
                             : boost::any(*runtime->socks5NetWork)},
       {"retry", boost::any(map<string, boost::any>(
                     {{"retryable", !runtime->autoretry
                                        ? boost::any()
                                        : boost::any(*runtime->autoretry)},
                      {"maxAttempts",
                       boost::any(Darabonba_Util::Client::defaultNumber(
                           runtime->maxAttempts, make_shared<int>(3)))}}))},
       {"backoff",
        boost::any(map<string, boost::any>(
            {{"policy",
              boost::any(string(Darabonba_Util::Client::defaultString(
                  runtime->backoffPolicy, make_shared<string>("no"))))},
             {"period", boost::any(Darabonba_Util::Client::defaultNumber(
                            runtime->backoffPeriod, make_shared<int>(1)))}}))},
       {"ignoreSSL", !runtime->ignoreSSL ? boost::any()
                                         : boost::any(*runtime->ignoreSSL)}}));
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(
      make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime =
          make_shared<int>(Darabonba::Core::getBackoffTime(
              make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ =
          make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret =
          make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken =
          make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq =
          make_shared<map<string, boost::any>>(
              Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(
          _protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(
          _nickname, make_shared<string>(string("/v2/hosting/file/create")));
      request_->headers = Darabonba::Converter::merge(
          map<string, string>(
              {{"user-agent", getUserAgent()},
               {"host",
                Darabonba_Util::Client::defaultString(
                    _endpoint, make_shared<string>(string(
                                   "" + *_domainId + ".api.aliyunpds.com")))},
               {"content-type", "application/json; charset=utf-8"}}),
          !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>(
            "authorization", string("Bearer " + *accessToken + "")));
      } else if (!Darabonba_Util::Client::empty(accesskeyId) &&
                 !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(
              pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>(
            "date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(
            pair<string, string>("accept", "application/json"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(
            Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>(
            "authorization", string("acs " + *accesskeyId + ":" +
                                    Alibabacloud_ROAUtil::Client::getSignature(
                                        stringToSign, accessKeySecret) +
                                    "")));
      }
      request_->body = Darabonba::Converter::toStream(
          Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ =
          make_shared<Darabonba::Response>(
              Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(
              make_shared<int>(response_->statusCode), make_shared<int>(201))) {
        obj = make_shared<boost::any>(
            Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(
            Darabonba_Util::Client::assertAsMap(obj));
        return CreateFileModel(
            {{"body", !respMap ? boost::any() : boost::any(*respMap)},
             {"headers", boost::any(response_->headers)}});
      }
      if (!Darabonba_Util::Client::empty(
              make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(
            {{"data",
              boost::any(map<string, boost::any>(
                  {{"requestId",
                    boost::any(string(response_->headers["x-ca-request-id"]))},
                   {"statusCode", boost::any(response_->statusCode)},
                   {"statusMessage",
                    boost::any(string(response_->statusMessage))}}))},
             {"message",
              boost::any(string(response_->headers["x-ca-error-message"]))}})));
      }
      obj = make_shared<boost::any>(
          Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(
          Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(
          Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(
              map<string, boost::any>(
                  {{"data",
                    boost::any(map<string, boost::any>(
                        {{"requestId",
                          boost::any(
                              string(response_->headers["x-ca-request-id"]))},
                         {"statusCode", boost::any(response_->statusCode)},
                         {"statusMessage",
                          boost::any(string(response_->statusMessage))}}))}}),
              !respMap ? map<string, boost::any>() : *respMap))));
    } catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(
      Darabonba::UnretryableError(_lastRequest, _lastException));
}

DeleteFileModel Alibabacloud_Hosting::Client::deleteFileEx(
    shared_ptr<HostingDeleteFileRequest> request,
    shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<
      map<string, boost::any>>(map<string, boost::any>(
      {{"timeouted", boost::any(string("retry"))},
       {"readTimeout", !runtime->readTimeout
                           ? boost::any()
                           : boost::any(*runtime->readTimeout)},
       {"connectTimeout", !runtime->connectTimeout
                              ? boost::any()
                              : boost::any(*runtime->connectTimeout)},
       {"localAddr",
        !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
       {"httpProxy",
        !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
       {"httpsProxy",
        !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
       {"noProxy", !runtime->noProxy ? boost::any()
                                     : boost::any(*runtime->noProxy)},
       {"maxIdleConns", !runtime->maxIdleConns
                            ? boost::any()
                            : boost::any(*runtime->maxIdleConns)},
       {"socks5Proxy", !runtime->socks5Proxy
                           ? boost::any()
                           : boost::any(*runtime->socks5Proxy)},
       {"socks5NetWork", !runtime->socks5NetWork
                             ? boost::any()
                             : boost::any(*runtime->socks5NetWork)},
       {"retry", boost::any(map<string, boost::any>(
                     {{"retryable", !runtime->autoretry
                                        ? boost::any()
                                        : boost::any(*runtime->autoretry)},
                      {"maxAttempts",
                       boost::any(Darabonba_Util::Client::defaultNumber(
                           runtime->maxAttempts, make_shared<int>(3)))}}))},
       {"backoff",
        boost::any(map<string, boost::any>(
            {{"policy",
              boost::any(string(Darabonba_Util::Client::defaultString(
                  runtime->backoffPolicy, make_shared<string>("no"))))},
             {"period", boost::any(Darabonba_Util::Client::defaultNumber(
                            runtime->backoffPeriod, make_shared<int>(1)))}}))},
       {"ignoreSSL", !runtime->ignoreSSL ? boost::any()
                                         : boost::any(*runtime->ignoreSSL)}}));
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(
      make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime =
          make_shared<int>(Darabonba::Core::getBackoffTime(
              make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ =
          make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret =
          make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken =
          make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq =
          make_shared<map<string, boost::any>>(
              Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(
          _protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(
          _nickname, make_shared<string>(string("/v2/hosting/file/delete")));
      request_->headers = Darabonba::Converter::merge(
          map<string, string>(
              {{"user-agent", getUserAgent()},
               {"host",
                Darabonba_Util::Client::defaultString(
                    _endpoint, make_shared<string>(string(
                                   "" + *_domainId + ".api.aliyunpds.com")))},
               {"content-type", "application/json; charset=utf-8"}}),
          !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>(
            "authorization", string("Bearer " + *accessToken + "")));
      } else if (!Darabonba_Util::Client::empty(accesskeyId) &&
                 !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(
              pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>(
            "date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(
            pair<string, string>("accept", "application/json"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(
            Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>(
            "authorization", string("acs " + *accesskeyId + ":" +
                                    Alibabacloud_ROAUtil::Client::getSignature(
                                        stringToSign, accessKeySecret) +
                                    "")));
      }
      request_->body = Darabonba::Converter::toStream(
          Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ =
          make_shared<Darabonba::Response>(
              Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(
              make_shared<int>(response_->statusCode), make_shared<int>(204))) {
        return DeleteFileModel({{"headers", boost::any(response_->headers)}});
      }
      if (!Darabonba_Util::Client::empty(
              make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(
            {{"data",
              boost::any(map<string, boost::any>(
                  {{"requestId",
                    boost::any(string(response_->headers["x-ca-request-id"]))},
                   {"statusCode", boost::any(response_->statusCode)},
                   {"statusMessage",
                    boost::any(string(response_->statusMessage))}}))},
             {"message",
              boost::any(string(response_->headers["x-ca-error-message"]))}})));
      }
      obj = make_shared<boost::any>(
          Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(
          Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(
          Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(
              map<string, boost::any>(
                  {{"data",
                    boost::any(map<string, boost::any>(
                        {{"requestId",
                          boost::any(
                              string(response_->headers["x-ca-request-id"]))},
                         {"statusCode", boost::any(response_->statusCode)},
                         {"statusMessage",
                          boost::any(string(response_->statusMessage))}}))}}),
              !respMap ? map<string, boost::any>() : *respMap))));
    } catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(
      Darabonba::UnretryableError(_lastRequest, _lastException));
}

GetFileModel Alibabacloud_Hosting::Client::getFileEx(
    shared_ptr<HostingGetFileRequest> request,
    shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<
      map<string, boost::any>>(map<string, boost::any>(
      {{"timeouted", boost::any(string("retry"))},
       {"readTimeout", !runtime->readTimeout
                           ? boost::any()
                           : boost::any(*runtime->readTimeout)},
       {"connectTimeout", !runtime->connectTimeout
                              ? boost::any()
                              : boost::any(*runtime->connectTimeout)},
       {"localAddr",
        !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
       {"httpProxy",
        !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
       {"httpsProxy",
        !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
       {"noProxy", !runtime->noProxy ? boost::any()
                                     : boost::any(*runtime->noProxy)},
       {"maxIdleConns", !runtime->maxIdleConns
                            ? boost::any()
                            : boost::any(*runtime->maxIdleConns)},
       {"socks5Proxy", !runtime->socks5Proxy
                           ? boost::any()
                           : boost::any(*runtime->socks5Proxy)},
       {"socks5NetWork", !runtime->socks5NetWork
                             ? boost::any()
                             : boost::any(*runtime->socks5NetWork)},
       {"retry", boost::any(map<string, boost::any>(
                     {{"retryable", !runtime->autoretry
                                        ? boost::any()
                                        : boost::any(*runtime->autoretry)},
                      {"maxAttempts",
                       boost::any(Darabonba_Util::Client::defaultNumber(
                           runtime->maxAttempts, make_shared<int>(3)))}}))},
       {"backoff",
        boost::any(map<string, boost::any>(
            {{"policy",
              boost::any(string(Darabonba_Util::Client::defaultString(
                  runtime->backoffPolicy, make_shared<string>("no"))))},
             {"period", boost::any(Darabonba_Util::Client::defaultNumber(
                            runtime->backoffPeriod, make_shared<int>(1)))}}))},
       {"ignoreSSL", !runtime->ignoreSSL ? boost::any()
                                         : boost::any(*runtime->ignoreSSL)}}));
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(
      make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime =
          make_shared<int>(Darabonba::Core::getBackoffTime(
              make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ =
          make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret =
          make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken =
          make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq =
          make_shared<map<string, boost::any>>(
              Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(
          _protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(
          _nickname, make_shared<string>(string("/v2/hosting/file/get")));
      request_->headers = Darabonba::Converter::merge(
          map<string, string>(
              {{"user-agent", getUserAgent()},
               {"host",
                Darabonba_Util::Client::defaultString(
                    _endpoint, make_shared<string>(string(
                                   "" + *_domainId + ".api.aliyunpds.com")))},
               {"content-type", "application/json; charset=utf-8"}}),
          !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>(
            "authorization", string("Bearer " + *accessToken + "")));
      } else if (!Darabonba_Util::Client::empty(accesskeyId) &&
                 !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(
              pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>(
            "date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(
            pair<string, string>("accept", "application/json"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(
            Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>(
            "authorization", string("acs " + *accesskeyId + ":" +
                                    Alibabacloud_ROAUtil::Client::getSignature(
                                        stringToSign, accessKeySecret) +
                                    "")));
      }
      request_->body = Darabonba::Converter::toStream(
          Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ =
          make_shared<Darabonba::Response>(
              Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(
              make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(
            Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(
            Darabonba_Util::Client::assertAsMap(obj));
        return GetFileModel(
            {{"body", !respMap ? boost::any() : boost::any(*respMap)},
             {"headers", boost::any(response_->headers)}});
      }
      if (!Darabonba_Util::Client::empty(
              make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(
            {{"data",
              boost::any(map<string, boost::any>(
                  {{"requestId",
                    boost::any(string(response_->headers["x-ca-request-id"]))},
                   {"statusCode", boost::any(response_->statusCode)},
                   {"statusMessage",
                    boost::any(string(response_->statusMessage))}}))},
             {"message",
              boost::any(string(response_->headers["x-ca-error-message"]))}})));
      }
      obj = make_shared<boost::any>(
          Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(
          Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(
          Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(
              map<string, boost::any>(
                  {{"data",
                    boost::any(map<string, boost::any>(
                        {{"requestId",
                          boost::any(
                              string(response_->headers["x-ca-request-id"]))},
                         {"statusCode", boost::any(response_->statusCode)},
                         {"statusMessage",
                          boost::any(string(response_->statusMessage))}}))}}),
              !respMap ? map<string, boost::any>() : *respMap))));
    } catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(
      Darabonba::UnretryableError(_lastRequest, _lastException));
}

GetDownloadUrlModel Alibabacloud_Hosting::Client::getDownloadUrlEx(
    shared_ptr<HostingGetDownloadUrlRequest> request,
    shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<
      map<string, boost::any>>(map<string, boost::any>(
      {{"timeouted", boost::any(string("retry"))},
       {"readTimeout", !runtime->readTimeout
                           ? boost::any()
                           : boost::any(*runtime->readTimeout)},
       {"connectTimeout", !runtime->connectTimeout
                              ? boost::any()
                              : boost::any(*runtime->connectTimeout)},
       {"localAddr",
        !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
       {"httpProxy",
        !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
       {"httpsProxy",
        !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
       {"noProxy", !runtime->noProxy ? boost::any()
                                     : boost::any(*runtime->noProxy)},
       {"maxIdleConns", !runtime->maxIdleConns
                            ? boost::any()
                            : boost::any(*runtime->maxIdleConns)},
       {"socks5Proxy", !runtime->socks5Proxy
                           ? boost::any()
                           : boost::any(*runtime->socks5Proxy)},
       {"socks5NetWork", !runtime->socks5NetWork
                             ? boost::any()
                             : boost::any(*runtime->socks5NetWork)},
       {"retry", boost::any(map<string, boost::any>(
                     {{"retryable", !runtime->autoretry
                                        ? boost::any()
                                        : boost::any(*runtime->autoretry)},
                      {"maxAttempts",
                       boost::any(Darabonba_Util::Client::defaultNumber(
                           runtime->maxAttempts, make_shared<int>(3)))}}))},
       {"backoff",
        boost::any(map<string, boost::any>(
            {{"policy",
              boost::any(string(Darabonba_Util::Client::defaultString(
                  runtime->backoffPolicy, make_shared<string>("no"))))},
             {"period", boost::any(Darabonba_Util::Client::defaultNumber(
                            runtime->backoffPeriod, make_shared<int>(1)))}}))},
       {"ignoreSSL", !runtime->ignoreSSL ? boost::any()
                                         : boost::any(*runtime->ignoreSSL)}}));
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(
      make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime =
          make_shared<int>(Darabonba::Core::getBackoffTime(
              make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ =
          make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret =
          make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken =
          make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq =
          make_shared<map<string, boost::any>>(
              Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(
          _protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(
          _nickname,
          make_shared<string>(string("/v2/hosting/file/get_download_url")));
      request_->headers = Darabonba::Converter::merge(
          map<string, string>(
              {{"user-agent", getUserAgent()},
               {"host",
                Darabonba_Util::Client::defaultString(
                    _endpoint, make_shared<string>(string(
                                   "" + *_domainId + ".api.aliyunpds.com")))},
               {"content-type", "application/json; charset=utf-8"}}),
          !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>(
            "authorization", string("Bearer " + *accessToken + "")));
      } else if (!Darabonba_Util::Client::empty(accesskeyId) &&
                 !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(
              pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>(
            "date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(
            pair<string, string>("accept", "application/json"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(
            Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>(
            "authorization", string("acs " + *accesskeyId + ":" +
                                    Alibabacloud_ROAUtil::Client::getSignature(
                                        stringToSign, accessKeySecret) +
                                    "")));
      }
      request_->body = Darabonba::Converter::toStream(
          Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ =
          make_shared<Darabonba::Response>(
              Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(
              make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(
            Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(
            Darabonba_Util::Client::assertAsMap(obj));
        return GetDownloadUrlModel(
            {{"body", !respMap ? boost::any() : boost::any(*respMap)},
             {"headers", boost::any(response_->headers)}});
      }
      if (!Darabonba_Util::Client::empty(
              make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(
            {{"data",
              boost::any(map<string, boost::any>(
                  {{"requestId",
                    boost::any(string(response_->headers["x-ca-request-id"]))},
                   {"statusCode", boost::any(response_->statusCode)},
                   {"statusMessage",
                    boost::any(string(response_->statusMessage))}}))},
             {"message",
              boost::any(string(response_->headers["x-ca-error-message"]))}})));
      }
      obj = make_shared<boost::any>(
          Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(
          Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(
          Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(
              map<string, boost::any>(
                  {{"data",
                    boost::any(map<string, boost::any>(
                        {{"requestId",
                          boost::any(
                              string(response_->headers["x-ca-request-id"]))},
                         {"statusCode", boost::any(response_->statusCode)},
                         {"statusMessage",
                          boost::any(string(response_->statusMessage))}}))}}),
              !respMap ? map<string, boost::any>() : *respMap))));
    } catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(
      Darabonba::UnretryableError(_lastRequest, _lastException));
}

GetSecureUrlModel Alibabacloud_Hosting::Client::getSecureUrlEx(
    shared_ptr<HostingGetSecureUrlRequest> request,
    shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<
      map<string, boost::any>>(map<string, boost::any>(
      {{"timeouted", boost::any(string("retry"))},
       {"readTimeout", !runtime->readTimeout
                           ? boost::any()
                           : boost::any(*runtime->readTimeout)},
       {"connectTimeout", !runtime->connectTimeout
                              ? boost::any()
                              : boost::any(*runtime->connectTimeout)},
       {"localAddr",
        !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
       {"httpProxy",
        !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
       {"httpsProxy",
        !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
       {"noProxy", !runtime->noProxy ? boost::any()
                                     : boost::any(*runtime->noProxy)},
       {"maxIdleConns", !runtime->maxIdleConns
                            ? boost::any()
                            : boost::any(*runtime->maxIdleConns)},
       {"socks5Proxy", !runtime->socks5Proxy
                           ? boost::any()
                           : boost::any(*runtime->socks5Proxy)},
       {"socks5NetWork", !runtime->socks5NetWork
                             ? boost::any()
                             : boost::any(*runtime->socks5NetWork)},
       {"retry", boost::any(map<string, boost::any>(
                     {{"retryable", !runtime->autoretry
                                        ? boost::any()
                                        : boost::any(*runtime->autoretry)},
                      {"maxAttempts",
                       boost::any(Darabonba_Util::Client::defaultNumber(
                           runtime->maxAttempts, make_shared<int>(3)))}}))},
       {"backoff",
        boost::any(map<string, boost::any>(
            {{"policy",
              boost::any(string(Darabonba_Util::Client::defaultString(
                  runtime->backoffPolicy, make_shared<string>("no"))))},
             {"period", boost::any(Darabonba_Util::Client::defaultNumber(
                            runtime->backoffPeriod, make_shared<int>(1)))}}))},
       {"ignoreSSL", !runtime->ignoreSSL ? boost::any()
                                         : boost::any(*runtime->ignoreSSL)}}));
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(
      make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime =
          make_shared<int>(Darabonba::Core::getBackoffTime(
              make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ =
          make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret =
          make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken =
          make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq =
          make_shared<map<string, boost::any>>(
              Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(
          _protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(
          _nickname,
          make_shared<string>(string("/v2/hosting/file/get_secure_url")));
      request_->headers = Darabonba::Converter::merge(
          map<string, string>(
              {{"user-agent", getUserAgent()},
               {"host",
                Darabonba_Util::Client::defaultString(
                    _endpoint, make_shared<string>(string(
                                   "" + *_domainId + ".api.aliyunpds.com")))},
               {"content-type", "application/json; charset=utf-8"}}),
          !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>(
            "authorization", string("Bearer " + *accessToken + "")));
      } else if (!Darabonba_Util::Client::empty(accesskeyId) &&
                 !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(
              pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>(
            "date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(
            pair<string, string>("accept", "application/json"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(
            Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>(
            "authorization", string("acs " + *accesskeyId + ":" +
                                    Alibabacloud_ROAUtil::Client::getSignature(
                                        stringToSign, accessKeySecret) +
                                    "")));
      }
      request_->body = Darabonba::Converter::toStream(
          Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ =
          make_shared<Darabonba::Response>(
              Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(
              make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(
            Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(
            Darabonba_Util::Client::assertAsMap(obj));
        return GetSecureUrlModel(
            {{"body", !respMap ? boost::any() : boost::any(*respMap)},
             {"headers", boost::any(response_->headers)}});
      }
      if (!Darabonba_Util::Client::empty(
              make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(
            {{"data",
              boost::any(map<string, boost::any>(
                  {{"requestId",
                    boost::any(string(response_->headers["x-ca-request-id"]))},
                   {"statusCode", boost::any(response_->statusCode)},
                   {"statusMessage",
                    boost::any(string(response_->statusMessage))}}))},
             {"message",
              boost::any(string(response_->headers["x-ca-error-message"]))}})));
      }
      obj = make_shared<boost::any>(
          Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(
          Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(
          Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(
              map<string, boost::any>(
                  {{"data",
                    boost::any(map<string, boost::any>(
                        {{"requestId",
                          boost::any(
                              string(response_->headers["x-ca-request-id"]))},
                         {"statusCode", boost::any(response_->statusCode)},
                         {"statusMessage",
                          boost::any(string(response_->statusMessage))}}))}}),
              !respMap ? map<string, boost::any>() : *respMap))));
    } catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(
      Darabonba::UnretryableError(_lastRequest, _lastException));
}

GetUploadUrlModel Alibabacloud_Hosting::Client::getUploadUrlEx(
    shared_ptr<HostingGetUploadUrlRequest> request,
    shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<
      map<string, boost::any>>(map<string, boost::any>(
      {{"timeouted", boost::any(string("retry"))},
       {"readTimeout", !runtime->readTimeout
                           ? boost::any()
                           : boost::any(*runtime->readTimeout)},
       {"connectTimeout", !runtime->connectTimeout
                              ? boost::any()
                              : boost::any(*runtime->connectTimeout)},
       {"localAddr",
        !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
       {"httpProxy",
        !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
       {"httpsProxy",
        !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
       {"noProxy", !runtime->noProxy ? boost::any()
                                     : boost::any(*runtime->noProxy)},
       {"maxIdleConns", !runtime->maxIdleConns
                            ? boost::any()
                            : boost::any(*runtime->maxIdleConns)},
       {"socks5Proxy", !runtime->socks5Proxy
                           ? boost::any()
                           : boost::any(*runtime->socks5Proxy)},
       {"socks5NetWork", !runtime->socks5NetWork
                             ? boost::any()
                             : boost::any(*runtime->socks5NetWork)},
       {"retry", boost::any(map<string, boost::any>(
                     {{"retryable", !runtime->autoretry
                                        ? boost::any()
                                        : boost::any(*runtime->autoretry)},
                      {"maxAttempts",
                       boost::any(Darabonba_Util::Client::defaultNumber(
                           runtime->maxAttempts, make_shared<int>(3)))}}))},
       {"backoff",
        boost::any(map<string, boost::any>(
            {{"policy",
              boost::any(string(Darabonba_Util::Client::defaultString(
                  runtime->backoffPolicy, make_shared<string>("no"))))},
             {"period", boost::any(Darabonba_Util::Client::defaultNumber(
                            runtime->backoffPeriod, make_shared<int>(1)))}}))},
       {"ignoreSSL", !runtime->ignoreSSL ? boost::any()
                                         : boost::any(*runtime->ignoreSSL)}}));
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(
      make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime =
          make_shared<int>(Darabonba::Core::getBackoffTime(
              make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ =
          make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret =
          make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken =
          make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq =
          make_shared<map<string, boost::any>>(
              Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(
          _protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(
          _nickname,
          make_shared<string>(string("/v2/hosting/file/get_upload_url")));
      request_->headers = Darabonba::Converter::merge(
          map<string, string>(
              {{"user-agent", getUserAgent()},
               {"host",
                Darabonba_Util::Client::defaultString(
                    _endpoint, make_shared<string>(string(
                                   "" + *_domainId + ".api.aliyunpds.com")))},
               {"content-type", "application/json; charset=utf-8"}}),
          !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>(
            "authorization", string("Bearer " + *accessToken + "")));
      } else if (!Darabonba_Util::Client::empty(accesskeyId) &&
                 !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(
              pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>(
            "date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(
            pair<string, string>("accept", "application/json"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(
            Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>(
            "authorization", string("acs " + *accesskeyId + ":" +
                                    Alibabacloud_ROAUtil::Client::getSignature(
                                        stringToSign, accessKeySecret) +
                                    "")));
      }
      request_->body = Darabonba::Converter::toStream(
          Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ =
          make_shared<Darabonba::Response>(
              Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(
              make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(
            Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(
            Darabonba_Util::Client::assertAsMap(obj));
        return GetUploadUrlModel(
            {{"body", !respMap ? boost::any() : boost::any(*respMap)},
             {"headers", boost::any(response_->headers)}});
      }
      if (!Darabonba_Util::Client::empty(
              make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(
            {{"data",
              boost::any(map<string, boost::any>(
                  {{"requestId",
                    boost::any(string(response_->headers["x-ca-request-id"]))},
                   {"statusCode", boost::any(response_->statusCode)},
                   {"statusMessage",
                    boost::any(string(response_->statusMessage))}}))},
             {"message",
              boost::any(string(response_->headers["x-ca-error-message"]))}})));
      }
      obj = make_shared<boost::any>(
          Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(
          Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(
          Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(
              map<string, boost::any>(
                  {{"data",
                    boost::any(map<string, boost::any>(
                        {{"requestId",
                          boost::any(
                              string(response_->headers["x-ca-request-id"]))},
                         {"statusCode", boost::any(response_->statusCode)},
                         {"statusMessage",
                          boost::any(string(response_->statusMessage))}}))}}),
              !respMap ? map<string, boost::any>() : *respMap))));
    } catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(
      Darabonba::UnretryableError(_lastRequest, _lastException));
}

ListFileModel Alibabacloud_Hosting::Client::listFileEx(
    shared_ptr<HostingListFileRequest> request,
    shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<
      map<string, boost::any>>(map<string, boost::any>(
      {{"timeouted", boost::any(string("retry"))},
       {"readTimeout", !runtime->readTimeout
                           ? boost::any()
                           : boost::any(*runtime->readTimeout)},
       {"connectTimeout", !runtime->connectTimeout
                              ? boost::any()
                              : boost::any(*runtime->connectTimeout)},
       {"localAddr",
        !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
       {"httpProxy",
        !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
       {"httpsProxy",
        !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
       {"noProxy", !runtime->noProxy ? boost::any()
                                     : boost::any(*runtime->noProxy)},
       {"maxIdleConns", !runtime->maxIdleConns
                            ? boost::any()
                            : boost::any(*runtime->maxIdleConns)},
       {"socks5Proxy", !runtime->socks5Proxy
                           ? boost::any()
                           : boost::any(*runtime->socks5Proxy)},
       {"socks5NetWork", !runtime->socks5NetWork
                             ? boost::any()
                             : boost::any(*runtime->socks5NetWork)},
       {"retry", boost::any(map<string, boost::any>(
                     {{"retryable", !runtime->autoretry
                                        ? boost::any()
                                        : boost::any(*runtime->autoretry)},
                      {"maxAttempts",
                       boost::any(Darabonba_Util::Client::defaultNumber(
                           runtime->maxAttempts, make_shared<int>(3)))}}))},
       {"backoff",
        boost::any(map<string, boost::any>(
            {{"policy",
              boost::any(string(Darabonba_Util::Client::defaultString(
                  runtime->backoffPolicy, make_shared<string>("no"))))},
             {"period", boost::any(Darabonba_Util::Client::defaultNumber(
                            runtime->backoffPeriod, make_shared<int>(1)))}}))},
       {"ignoreSSL", !runtime->ignoreSSL ? boost::any()
                                         : boost::any(*runtime->ignoreSSL)}}));
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(
      make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime =
          make_shared<int>(Darabonba::Core::getBackoffTime(
              make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ =
          make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret =
          make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken =
          make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq =
          make_shared<map<string, boost::any>>(
              Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(
          _protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(
          _nickname, make_shared<string>(string("/v2/hosting/file/list")));
      request_->headers = Darabonba::Converter::merge(
          map<string, string>(
              {{"user-agent", getUserAgent()},
               {"host",
                Darabonba_Util::Client::defaultString(
                    _endpoint, make_shared<string>(string(
                                   "" + *_domainId + ".api.aliyunpds.com")))},
               {"content-type", "application/json; charset=utf-8"}}),
          !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>(
            "authorization", string("Bearer " + *accessToken + "")));
      } else if (!Darabonba_Util::Client::empty(accesskeyId) &&
                 !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(
              pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>(
            "date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(
            pair<string, string>("accept", "application/json"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(
            Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>(
            "authorization", string("acs " + *accesskeyId + ":" +
                                    Alibabacloud_ROAUtil::Client::getSignature(
                                        stringToSign, accessKeySecret) +
                                    "")));
      }
      request_->body = Darabonba::Converter::toStream(
          Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ =
          make_shared<Darabonba::Response>(
              Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(
              make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(
            Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(
            Darabonba_Util::Client::assertAsMap(obj));
        return ListFileModel(
            {{"body", !respMap ? boost::any() : boost::any(*respMap)},
             {"headers", boost::any(response_->headers)}});
      }
      if (!Darabonba_Util::Client::empty(
              make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(
            {{"data",
              boost::any(map<string, boost::any>(
                  {{"requestId",
                    boost::any(string(response_->headers["x-ca-request-id"]))},
                   {"statusCode", boost::any(response_->statusCode)},
                   {"statusMessage",
                    boost::any(string(response_->statusMessage))}}))},
             {"message",
              boost::any(string(response_->headers["x-ca-error-message"]))}})));
      }
      obj = make_shared<boost::any>(
          Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(
          Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(
          Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(
              map<string, boost::any>(
                  {{"data",
                    boost::any(map<string, boost::any>(
                        {{"requestId",
                          boost::any(
                              string(response_->headers["x-ca-request-id"]))},
                         {"statusCode", boost::any(response_->statusCode)},
                         {"statusMessage",
                          boost::any(string(response_->statusMessage))}}))}}),
              !respMap ? map<string, boost::any>() : *respMap))));
    } catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(
      Darabonba::UnretryableError(_lastRequest, _lastException));
}

ListUploadedPartsModel Alibabacloud_Hosting::Client::listUploadedPartsEx(
    shared_ptr<HostingListUploadedPartRequest> request,
    shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<
      map<string, boost::any>>(map<string, boost::any>(
      {{"timeouted", boost::any(string("retry"))},
       {"readTimeout", !runtime->readTimeout
                           ? boost::any()
                           : boost::any(*runtime->readTimeout)},
       {"connectTimeout", !runtime->connectTimeout
                              ? boost::any()
                              : boost::any(*runtime->connectTimeout)},
       {"localAddr",
        !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
       {"httpProxy",
        !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
       {"httpsProxy",
        !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
       {"noProxy", !runtime->noProxy ? boost::any()
                                     : boost::any(*runtime->noProxy)},
       {"maxIdleConns", !runtime->maxIdleConns
                            ? boost::any()
                            : boost::any(*runtime->maxIdleConns)},
       {"socks5Proxy", !runtime->socks5Proxy
                           ? boost::any()
                           : boost::any(*runtime->socks5Proxy)},
       {"socks5NetWork", !runtime->socks5NetWork
                             ? boost::any()
                             : boost::any(*runtime->socks5NetWork)},
       {"retry", boost::any(map<string, boost::any>(
                     {{"retryable", !runtime->autoretry
                                        ? boost::any()
                                        : boost::any(*runtime->autoretry)},
                      {"maxAttempts",
                       boost::any(Darabonba_Util::Client::defaultNumber(
                           runtime->maxAttempts, make_shared<int>(3)))}}))},
       {"backoff",
        boost::any(map<string, boost::any>(
            {{"policy",
              boost::any(string(Darabonba_Util::Client::defaultString(
                  runtime->backoffPolicy, make_shared<string>("no"))))},
             {"period", boost::any(Darabonba_Util::Client::defaultNumber(
                            runtime->backoffPeriod, make_shared<int>(1)))}}))},
       {"ignoreSSL", !runtime->ignoreSSL ? boost::any()
                                         : boost::any(*runtime->ignoreSSL)}}));
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(
      make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime =
          make_shared<int>(Darabonba::Core::getBackoffTime(
              make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ =
          make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret =
          make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken =
          make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq =
          make_shared<map<string, boost::any>>(
              Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(
          _protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(
          _nickname,
          make_shared<string>(string("/v2/hosting/file/list_uploaded_parts")));
      request_->headers = Darabonba::Converter::merge(
          map<string, string>(
              {{"user-agent", getUserAgent()},
               {"host",
                Darabonba_Util::Client::defaultString(
                    _endpoint, make_shared<string>(string(
                                   "" + *_domainId + ".api.aliyunpds.com")))},
               {"content-type", "application/json; charset=utf-8"}}),
          !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>(
            "authorization", string("Bearer " + *accessToken + "")));
      } else if (!Darabonba_Util::Client::empty(accesskeyId) &&
                 !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(
              pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>(
            "date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(
            pair<string, string>("accept", "application/json"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(
            Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>(
            "authorization", string("acs " + *accesskeyId + ":" +
                                    Alibabacloud_ROAUtil::Client::getSignature(
                                        stringToSign, accessKeySecret) +
                                    "")));
      }
      request_->body = Darabonba::Converter::toStream(
          Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ =
          make_shared<Darabonba::Response>(
              Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(
              make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(
            Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(
            Darabonba_Util::Client::assertAsMap(obj));
        return ListUploadedPartsModel(
            {{"body", !respMap ? boost::any() : boost::any(*respMap)},
             {"headers", boost::any(response_->headers)}});
      }
      if (!Darabonba_Util::Client::empty(
              make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(
            {{"data",
              boost::any(map<string, boost::any>(
                  {{"requestId",
                    boost::any(string(response_->headers["x-ca-request-id"]))},
                   {"statusCode", boost::any(response_->statusCode)},
                   {"statusMessage",
                    boost::any(string(response_->statusMessage))}}))},
             {"message",
              boost::any(string(response_->headers["x-ca-error-message"]))}})));
      }
      obj = make_shared<boost::any>(
          Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(
          Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(
          Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(
              map<string, boost::any>(
                  {{"data",
                    boost::any(map<string, boost::any>(
                        {{"requestId",
                          boost::any(
                              string(response_->headers["x-ca-request-id"]))},
                         {"statusCode", boost::any(response_->statusCode)},
                         {"statusMessage",
                          boost::any(string(response_->statusMessage))}}))}}),
              !respMap ? map<string, boost::any>() : *respMap))));
    } catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(
      Darabonba::UnretryableError(_lastRequest, _lastException));
}

MoveFileModel Alibabacloud_Hosting::Client::moveFileEx(
    shared_ptr<HostingMoveFileRequest> request,
    shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<
      map<string, boost::any>>(map<string, boost::any>(
      {{"timeouted", boost::any(string("retry"))},
       {"readTimeout", !runtime->readTimeout
                           ? boost::any()
                           : boost::any(*runtime->readTimeout)},
       {"connectTimeout", !runtime->connectTimeout
                              ? boost::any()
                              : boost::any(*runtime->connectTimeout)},
       {"localAddr",
        !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
       {"httpProxy",
        !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
       {"httpsProxy",
        !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
       {"noProxy", !runtime->noProxy ? boost::any()
                                     : boost::any(*runtime->noProxy)},
       {"maxIdleConns", !runtime->maxIdleConns
                            ? boost::any()
                            : boost::any(*runtime->maxIdleConns)},
       {"socks5Proxy", !runtime->socks5Proxy
                           ? boost::any()
                           : boost::any(*runtime->socks5Proxy)},
       {"socks5NetWork", !runtime->socks5NetWork
                             ? boost::any()
                             : boost::any(*runtime->socks5NetWork)},
       {"retry", boost::any(map<string, boost::any>(
                     {{"retryable", !runtime->autoretry
                                        ? boost::any()
                                        : boost::any(*runtime->autoretry)},
                      {"maxAttempts",
                       boost::any(Darabonba_Util::Client::defaultNumber(
                           runtime->maxAttempts, make_shared<int>(3)))}}))},
       {"backoff",
        boost::any(map<string, boost::any>(
            {{"policy",
              boost::any(string(Darabonba_Util::Client::defaultString(
                  runtime->backoffPolicy, make_shared<string>("no"))))},
             {"period", boost::any(Darabonba_Util::Client::defaultNumber(
                            runtime->backoffPeriod, make_shared<int>(1)))}}))},
       {"ignoreSSL", !runtime->ignoreSSL ? boost::any()
                                         : boost::any(*runtime->ignoreSSL)}}));
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(
      make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime =
          make_shared<int>(Darabonba::Core::getBackoffTime(
              make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ =
          make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret =
          make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken =
          make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq =
          make_shared<map<string, boost::any>>(
              Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(
          _protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(
          _nickname, make_shared<string>(string("/v2/hosting/file/move")));
      request_->headers = Darabonba::Converter::merge(
          map<string, string>(
              {{"user-agent", getUserAgent()},
               {"host",
                Darabonba_Util::Client::defaultString(
                    _endpoint, make_shared<string>(string(
                                   "" + *_domainId + ".api.aliyunpds.com")))},
               {"content-type", "application/json; charset=utf-8"}}),
          !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>(
            "authorization", string("Bearer " + *accessToken + "")));
      } else if (!Darabonba_Util::Client::empty(accesskeyId) &&
                 !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(
              pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>(
            "date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(
            pair<string, string>("accept", "application/json"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(
            Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>(
            "authorization", string("acs " + *accesskeyId + ":" +
                                    Alibabacloud_ROAUtil::Client::getSignature(
                                        stringToSign, accessKeySecret) +
                                    "")));
      }
      request_->body = Darabonba::Converter::toStream(
          Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ =
          make_shared<Darabonba::Response>(
              Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(
              make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(
            Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(
            Darabonba_Util::Client::assertAsMap(obj));
        return MoveFileModel(
            {{"body", !respMap ? boost::any() : boost::any(*respMap)},
             {"headers", boost::any(response_->headers)}});
      }
      if (!Darabonba_Util::Client::empty(
              make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(
            {{"data",
              boost::any(map<string, boost::any>(
                  {{"requestId",
                    boost::any(string(response_->headers["x-ca-request-id"]))},
                   {"statusCode", boost::any(response_->statusCode)},
                   {"statusMessage",
                    boost::any(string(response_->statusMessage))}}))},
             {"message",
              boost::any(string(response_->headers["x-ca-error-message"]))}})));
      }
      obj = make_shared<boost::any>(
          Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(
          Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(
          Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(
              map<string, boost::any>(
                  {{"data",
                    boost::any(map<string, boost::any>(
                        {{"requestId",
                          boost::any(
                              string(response_->headers["x-ca-request-id"]))},
                         {"statusCode", boost::any(response_->statusCode)},
                         {"statusMessage",
                          boost::any(string(response_->statusMessage))}}))}}),
              !respMap ? map<string, boost::any>() : *respMap))));
    } catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(
      Darabonba::UnretryableError(_lastRequest, _lastException));
}

VideoDefinitionModel Alibabacloud_Hosting::Client::videoDefinitionEx(
    shared_ptr<HostingVideoDefinitionRequest> request,
    shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<
      map<string, boost::any>>(map<string, boost::any>(
      {{"timeouted", boost::any(string("retry"))},
       {"readTimeout", !runtime->readTimeout
                           ? boost::any()
                           : boost::any(*runtime->readTimeout)},
       {"connectTimeout", !runtime->connectTimeout
                              ? boost::any()
                              : boost::any(*runtime->connectTimeout)},
       {"localAddr",
        !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
       {"httpProxy",
        !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
       {"httpsProxy",
        !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
       {"noProxy", !runtime->noProxy ? boost::any()
                                     : boost::any(*runtime->noProxy)},
       {"maxIdleConns", !runtime->maxIdleConns
                            ? boost::any()
                            : boost::any(*runtime->maxIdleConns)},
       {"socks5Proxy", !runtime->socks5Proxy
                           ? boost::any()
                           : boost::any(*runtime->socks5Proxy)},
       {"socks5NetWork", !runtime->socks5NetWork
                             ? boost::any()
                             : boost::any(*runtime->socks5NetWork)},
       {"retry", boost::any(map<string, boost::any>(
                     {{"retryable", !runtime->autoretry
                                        ? boost::any()
                                        : boost::any(*runtime->autoretry)},
                      {"maxAttempts",
                       boost::any(Darabonba_Util::Client::defaultNumber(
                           runtime->maxAttempts, make_shared<int>(3)))}}))},
       {"backoff",
        boost::any(map<string, boost::any>(
            {{"policy",
              boost::any(string(Darabonba_Util::Client::defaultString(
                  runtime->backoffPolicy, make_shared<string>("no"))))},
             {"period", boost::any(Darabonba_Util::Client::defaultNumber(
                            runtime->backoffPeriod, make_shared<int>(1)))}}))},
       {"ignoreSSL", !runtime->ignoreSSL ? boost::any()
                                         : boost::any(*runtime->ignoreSSL)}}));
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(
      make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime =
          make_shared<int>(Darabonba::Core::getBackoffTime(
              make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ =
          make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret =
          make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken =
          make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq =
          make_shared<map<string, boost::any>>(
              Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(
          _protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(
          _nickname,
          make_shared<string>(string("/v2/hosting/file/video_definition")));
      request_->headers = Darabonba::Converter::merge(
          map<string, string>(
              {{"user-agent", getUserAgent()},
               {"host",
                Darabonba_Util::Client::defaultString(
                    _endpoint, make_shared<string>(string(
                                   "" + *_domainId + ".api.aliyunpds.com")))},
               {"content-type", "application/json; charset=utf-8"}}),
          !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>(
            "authorization", string("Bearer " + *accessToken + "")));
      } else if (!Darabonba_Util::Client::empty(accesskeyId) &&
                 !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(
              pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>(
            "date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(
            pair<string, string>("accept", "application/json"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(
            Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>(
            "authorization", string("acs " + *accesskeyId + ":" +
                                    Alibabacloud_ROAUtil::Client::getSignature(
                                        stringToSign, accessKeySecret) +
                                    "")));
      }
      request_->body = Darabonba::Converter::toStream(
          Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ =
          make_shared<Darabonba::Response>(
              Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(
              make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(
            Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(
            Darabonba_Util::Client::assertAsMap(obj));
        return VideoDefinitionModel(
            {{"body", !respMap ? boost::any() : boost::any(*respMap)},
             {"headers", boost::any(response_->headers)}});
      }
      if (!Darabonba_Util::Client::empty(
              make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(
            {{"data",
              boost::any(map<string, boost::any>(
                  {{"requestId",
                    boost::any(string(response_->headers["x-ca-request-id"]))},
                   {"statusCode", boost::any(response_->statusCode)},
                   {"statusMessage",
                    boost::any(string(response_->statusMessage))}}))},
             {"message",
              boost::any(string(response_->headers["x-ca-error-message"]))}})));
      }
      obj = make_shared<boost::any>(
          Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(
          Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(
          Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(
              map<string, boost::any>(
                  {{"data",
                    boost::any(map<string, boost::any>(
                        {{"requestId",
                          boost::any(
                              string(response_->headers["x-ca-request-id"]))},
                         {"statusCode", boost::any(response_->statusCode)},
                         {"statusMessage",
                          boost::any(string(response_->statusMessage))}}))}}),
              !respMap ? map<string, boost::any>() : *respMap))));
    } catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(
      Darabonba::UnretryableError(_lastRequest, _lastException));
}

VideoLicenseModel Alibabacloud_Hosting::Client::videoLicenseEx(
    shared_ptr<HostingVideoDRMLicenseRequest> request,
    shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<
      map<string, boost::any>>(map<string, boost::any>(
      {{"timeouted", boost::any(string("retry"))},
       {"readTimeout", !runtime->readTimeout
                           ? boost::any()
                           : boost::any(*runtime->readTimeout)},
       {"connectTimeout", !runtime->connectTimeout
                              ? boost::any()
                              : boost::any(*runtime->connectTimeout)},
       {"localAddr",
        !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
       {"httpProxy",
        !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
       {"httpsProxy",
        !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
       {"noProxy", !runtime->noProxy ? boost::any()
                                     : boost::any(*runtime->noProxy)},
       {"maxIdleConns", !runtime->maxIdleConns
                            ? boost::any()
                            : boost::any(*runtime->maxIdleConns)},
       {"socks5Proxy", !runtime->socks5Proxy
                           ? boost::any()
                           : boost::any(*runtime->socks5Proxy)},
       {"socks5NetWork", !runtime->socks5NetWork
                             ? boost::any()
                             : boost::any(*runtime->socks5NetWork)},
       {"retry", boost::any(map<string, boost::any>(
                     {{"retryable", !runtime->autoretry
                                        ? boost::any()
                                        : boost::any(*runtime->autoretry)},
                      {"maxAttempts",
                       boost::any(Darabonba_Util::Client::defaultNumber(
                           runtime->maxAttempts, make_shared<int>(3)))}}))},
       {"backoff",
        boost::any(map<string, boost::any>(
            {{"policy",
              boost::any(string(Darabonba_Util::Client::defaultString(
                  runtime->backoffPolicy, make_shared<string>("no"))))},
             {"period", boost::any(Darabonba_Util::Client::defaultNumber(
                            runtime->backoffPeriod, make_shared<int>(1)))}}))},
       {"ignoreSSL", !runtime->ignoreSSL ? boost::any()
                                         : boost::any(*runtime->ignoreSSL)}}));
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(
      make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime =
          make_shared<int>(Darabonba::Core::getBackoffTime(
              make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ =
          make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret =
          make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken =
          make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq =
          make_shared<map<string, boost::any>>(
              Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(
          _protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(
          _nickname,
          make_shared<string>(string("/v2/hosting/file/video_license")));
      request_->headers = Darabonba::Converter::merge(
          map<string, string>(
              {{"user-agent", getUserAgent()},
               {"host",
                Darabonba_Util::Client::defaultString(
                    _endpoint, make_shared<string>(string(
                                   "" + *_domainId + ".api.aliyunpds.com")))},
               {"content-type", "application/json; charset=utf-8"}}),
          !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>(
            "authorization", string("Bearer " + *accessToken + "")));
      } else if (!Darabonba_Util::Client::empty(accesskeyId) &&
                 !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(
              pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>(
            "date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(
            pair<string, string>("accept", "application/json"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(
            Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>(
            "authorization", string("acs " + *accesskeyId + ":" +
                                    Alibabacloud_ROAUtil::Client::getSignature(
                                        stringToSign, accessKeySecret) +
                                    "")));
      }
      request_->body = Darabonba::Converter::toStream(
          Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ =
          make_shared<Darabonba::Response>(
              Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(
              make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(
            Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(
            Darabonba_Util::Client::assertAsMap(obj));
        return VideoLicenseModel(
            {{"body", !respMap ? boost::any() : boost::any(*respMap)},
             {"headers", boost::any(response_->headers)}});
      }
      if (!Darabonba_Util::Client::empty(
              make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(
            {{"data",
              boost::any(map<string, boost::any>(
                  {{"requestId",
                    boost::any(string(response_->headers["x-ca-request-id"]))},
                   {"statusCode", boost::any(response_->statusCode)},
                   {"statusMessage",
                    boost::any(string(response_->statusMessage))}}))},
             {"message",
              boost::any(string(response_->headers["x-ca-error-message"]))}})));
      }
      obj = make_shared<boost::any>(
          Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(
          Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(
          Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(
              map<string, boost::any>(
                  {{"data",
                    boost::any(map<string, boost::any>(
                        {{"requestId",
                          boost::any(
                              string(response_->headers["x-ca-request-id"]))},
                         {"statusCode", boost::any(response_->statusCode)},
                         {"statusMessage",
                          boost::any(string(response_->statusMessage))}}))}}),
              !respMap ? map<string, boost::any>() : *respMap))));
    } catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(
      Darabonba::UnretryableError(_lastRequest, _lastException));
}

VideoM3u8Model Alibabacloud_Hosting::Client::videoM3u8Ex(
    shared_ptr<HostingVideoM3U8Request> request,
    shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<
      map<string, boost::any>>(map<string, boost::any>(
      {{"timeouted", boost::any(string("retry"))},
       {"readTimeout", !runtime->readTimeout
                           ? boost::any()
                           : boost::any(*runtime->readTimeout)},
       {"connectTimeout", !runtime->connectTimeout
                              ? boost::any()
                              : boost::any(*runtime->connectTimeout)},
       {"localAddr",
        !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
       {"httpProxy",
        !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
       {"httpsProxy",
        !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
       {"noProxy", !runtime->noProxy ? boost::any()
                                     : boost::any(*runtime->noProxy)},
       {"maxIdleConns", !runtime->maxIdleConns
                            ? boost::any()
                            : boost::any(*runtime->maxIdleConns)},
       {"socks5Proxy", !runtime->socks5Proxy
                           ? boost::any()
                           : boost::any(*runtime->socks5Proxy)},
       {"socks5NetWork", !runtime->socks5NetWork
                             ? boost::any()
                             : boost::any(*runtime->socks5NetWork)},
       {"retry", boost::any(map<string, boost::any>(
                     {{"retryable", !runtime->autoretry
                                        ? boost::any()
                                        : boost::any(*runtime->autoretry)},
                      {"maxAttempts",
                       boost::any(Darabonba_Util::Client::defaultNumber(
                           runtime->maxAttempts, make_shared<int>(3)))}}))},
       {"backoff",
        boost::any(map<string, boost::any>(
            {{"policy",
              boost::any(string(Darabonba_Util::Client::defaultString(
                  runtime->backoffPolicy, make_shared<string>("no"))))},
             {"period", boost::any(Darabonba_Util::Client::defaultNumber(
                            runtime->backoffPeriod, make_shared<int>(1)))}}))},
       {"ignoreSSL", !runtime->ignoreSSL ? boost::any()
                                         : boost::any(*runtime->ignoreSSL)}}));
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(
      make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime =
          make_shared<int>(Darabonba::Core::getBackoffTime(
              make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ =
          make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret =
          make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken =
          make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq =
          make_shared<map<string, boost::any>>(
              Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(
          _protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(
          _nickname,
          make_shared<string>(string("/v2/hosting/file/video_m3u8")));
      request_->headers = Darabonba::Converter::merge(
          map<string, string>(
              {{"user-agent", getUserAgent()},
               {"host",
                Darabonba_Util::Client::defaultString(
                    _endpoint, make_shared<string>(string(
                                   "" + *_domainId + ".api.aliyunpds.com")))},
               {"content-type", "application/json; charset=utf-8"}}),
          !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>(
            "authorization", string("Bearer " + *accessToken + "")));
      } else if (!Darabonba_Util::Client::empty(accesskeyId) &&
                 !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(
              pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>(
            "date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(
            pair<string, string>("accept", "application/json"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(
            Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>(
            "authorization", string("acs " + *accesskeyId + ":" +
                                    Alibabacloud_ROAUtil::Client::getSignature(
                                        stringToSign, accessKeySecret) +
                                    "")));
      }
      request_->body = Darabonba::Converter::toStream(
          Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ =
          make_shared<Darabonba::Response>(
              Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(
              make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        shared_ptr<vector<uint8_t>> byt = make_shared<vector<uint8_t>>(
            Darabonba_Util::Client::readAsBytes(response_->body));
        return VideoM3u8Model({{"body", !byt ? boost::any() : boost::any(*byt)},
                               {"headers", boost::any(response_->headers)}});
      }
      if (!Darabonba_Util::Client::empty(
              make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(
            {{"data",
              boost::any(map<string, boost::any>(
                  {{"requestId",
                    boost::any(string(response_->headers["x-ca-request-id"]))},
                   {"statusCode", boost::any(response_->statusCode)},
                   {"statusMessage",
                    boost::any(string(response_->statusMessage))}}))},
             {"message",
              boost::any(string(response_->headers["x-ca-error-message"]))}})));
      }
      obj = make_shared<boost::any>(
          Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(
          Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(
          Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(
              map<string, boost::any>(
                  {{"data",
                    boost::any(map<string, boost::any>(
                        {{"requestId",
                          boost::any(
                              string(response_->headers["x-ca-request-id"]))},
                         {"statusCode", boost::any(response_->statusCode)},
                         {"statusMessage",
                          boost::any(string(response_->statusMessage))}}))}}),
              !respMap ? map<string, boost::any>() : *respMap))));
    } catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(
      Darabonba::UnretryableError(_lastRequest, _lastException));
}

VideoTranscodeModel Alibabacloud_Hosting::Client::videoTranscodeEx(
    shared_ptr<HostingVideoTranscodeRequest> request,
    shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<
      map<string, boost::any>>(map<string, boost::any>(
      {{"timeouted", boost::any(string("retry"))},
       {"readTimeout", !runtime->readTimeout
                           ? boost::any()
                           : boost::any(*runtime->readTimeout)},
       {"connectTimeout", !runtime->connectTimeout
                              ? boost::any()
                              : boost::any(*runtime->connectTimeout)},
       {"localAddr",
        !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
       {"httpProxy",
        !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
       {"httpsProxy",
        !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
       {"noProxy", !runtime->noProxy ? boost::any()
                                     : boost::any(*runtime->noProxy)},
       {"maxIdleConns", !runtime->maxIdleConns
                            ? boost::any()
                            : boost::any(*runtime->maxIdleConns)},
       {"socks5Proxy", !runtime->socks5Proxy
                           ? boost::any()
                           : boost::any(*runtime->socks5Proxy)},
       {"socks5NetWork", !runtime->socks5NetWork
                             ? boost::any()
                             : boost::any(*runtime->socks5NetWork)},
       {"retry", boost::any(map<string, boost::any>(
                     {{"retryable", !runtime->autoretry
                                        ? boost::any()
                                        : boost::any(*runtime->autoretry)},
                      {"maxAttempts",
                       boost::any(Darabonba_Util::Client::defaultNumber(
                           runtime->maxAttempts, make_shared<int>(3)))}}))},
       {"backoff",
        boost::any(map<string, boost::any>(
            {{"policy",
              boost::any(string(Darabonba_Util::Client::defaultString(
                  runtime->backoffPolicy, make_shared<string>("no"))))},
             {"period", boost::any(Darabonba_Util::Client::defaultNumber(
                            runtime->backoffPeriod, make_shared<int>(1)))}}))},
       {"ignoreSSL", !runtime->ignoreSSL ? boost::any()
                                         : boost::any(*runtime->ignoreSSL)}}));
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(
      make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime =
          make_shared<int>(Darabonba::Core::getBackoffTime(
              make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ =
          make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret =
          make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken =
          make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq =
          make_shared<map<string, boost::any>>(
              Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(
          _protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(
          _nickname,
          make_shared<string>(string("/v2/hosting/file/video_transcode")));
      request_->headers = Darabonba::Converter::merge(
          map<string, string>(
              {{"user-agent", getUserAgent()},
               {"host",
                Darabonba_Util::Client::defaultString(
                    _endpoint, make_shared<string>(string(
                                   "" + *_domainId + ".api.aliyunpds.com")))},
               {"content-type", "application/json; charset=utf-8"}}),
          !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>(
            "authorization", string("Bearer " + *accessToken + "")));
      } else if (!Darabonba_Util::Client::empty(accesskeyId) &&
                 !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(
              pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>(
            "date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(
            pair<string, string>("accept", "application/json"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(
            Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>(
            "authorization", string("acs " + *accesskeyId + ":" +
                                    Alibabacloud_ROAUtil::Client::getSignature(
                                        stringToSign, accessKeySecret) +
                                    "")));
      }
      request_->body = Darabonba::Converter::toStream(
          Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ =
          make_shared<Darabonba::Response>(
              Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(
              make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(
            Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(
            Darabonba_Util::Client::assertAsMap(obj));
        return VideoTranscodeModel(
            {{"body", !respMap ? boost::any() : boost::any(*respMap)},
             {"headers", boost::any(response_->headers)}});
      }
      if (Darabonba_Util::Client::equalNumber(
              make_shared<int>(response_->statusCode), make_shared<int>(204))) {
        return VideoTranscodeModel(
            {{"headers", boost::any(response_->headers)}});
      }
      if (!Darabonba_Util::Client::empty(
              make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(
            {{"data",
              boost::any(map<string, boost::any>(
                  {{"requestId",
                    boost::any(string(response_->headers["x-ca-request-id"]))},
                   {"statusCode", boost::any(response_->statusCode)},
                   {"statusMessage",
                    boost::any(string(response_->statusMessage))}}))},
             {"message",
              boost::any(string(response_->headers["x-ca-error-message"]))}})));
      }
      obj = make_shared<boost::any>(
          Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(
          Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(
          Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(
              map<string, boost::any>(
                  {{"data",
                    boost::any(map<string, boost::any>(
                        {{"requestId",
                          boost::any(
                              string(response_->headers["x-ca-request-id"]))},
                         {"statusCode", boost::any(response_->statusCode)},
                         {"statusMessage",
                          boost::any(string(response_->statusMessage))}}))}}),
              !respMap ? map<string, boost::any>() : *respMap))));
    } catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(
      Darabonba::UnretryableError(_lastRequest, _lastException));
}

CreateShareModel Alibabacloud_Hosting::Client::createShareEx(
    shared_ptr<CreateShareRequest> request,
    shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<
      map<string, boost::any>>(map<string, boost::any>(
      {{"timeouted", boost::any(string("retry"))},
       {"readTimeout", !runtime->readTimeout
                           ? boost::any()
                           : boost::any(*runtime->readTimeout)},
       {"connectTimeout", !runtime->connectTimeout
                              ? boost::any()
                              : boost::any(*runtime->connectTimeout)},
       {"localAddr",
        !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
       {"httpProxy",
        !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
       {"httpsProxy",
        !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
       {"noProxy", !runtime->noProxy ? boost::any()
                                     : boost::any(*runtime->noProxy)},
       {"maxIdleConns", !runtime->maxIdleConns
                            ? boost::any()
                            : boost::any(*runtime->maxIdleConns)},
       {"socks5Proxy", !runtime->socks5Proxy
                           ? boost::any()
                           : boost::any(*runtime->socks5Proxy)},
       {"socks5NetWork", !runtime->socks5NetWork
                             ? boost::any()
                             : boost::any(*runtime->socks5NetWork)},
       {"retry", boost::any(map<string, boost::any>(
                     {{"retryable", !runtime->autoretry
                                        ? boost::any()
                                        : boost::any(*runtime->autoretry)},
                      {"maxAttempts",
                       boost::any(Darabonba_Util::Client::defaultNumber(
                           runtime->maxAttempts, make_shared<int>(3)))}}))},
       {"backoff",
        boost::any(map<string, boost::any>(
            {{"policy",
              boost::any(string(Darabonba_Util::Client::defaultString(
                  runtime->backoffPolicy, make_shared<string>("no"))))},
             {"period", boost::any(Darabonba_Util::Client::defaultNumber(
                            runtime->backoffPeriod, make_shared<int>(1)))}}))},
       {"ignoreSSL", !runtime->ignoreSSL ? boost::any()
                                         : boost::any(*runtime->ignoreSSL)}}));
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(
      make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime =
          make_shared<int>(Darabonba::Core::getBackoffTime(
              make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ =
          make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret =
          make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken =
          make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq =
          make_shared<map<string, boost::any>>(
              Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(
          _protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(
          _nickname, make_shared<string>(string("/v2/hosting/share/create")));
      request_->headers = Darabonba::Converter::merge(
          map<string, string>(
              {{"user-agent", getUserAgent()},
               {"host",
                Darabonba_Util::Client::defaultString(
                    _endpoint, make_shared<string>(string(
                                   "" + *_domainId + ".api.aliyunpds.com")))},
               {"content-type", "application/json; charset=utf-8"}}),
          !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>(
            "authorization", string("Bearer " + *accessToken + "")));
      } else if (!Darabonba_Util::Client::empty(accesskeyId) &&
                 !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(
              pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>(
            "date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(
            pair<string, string>("accept", "application/json"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(
            Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>(
            "authorization", string("acs " + *accesskeyId + ":" +
                                    Alibabacloud_ROAUtil::Client::getSignature(
                                        stringToSign, accessKeySecret) +
                                    "")));
      }
      request_->body = Darabonba::Converter::toStream(
          Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ =
          make_shared<Darabonba::Response>(
              Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(
              make_shared<int>(response_->statusCode), make_shared<int>(201))) {
        obj = make_shared<boost::any>(
            Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(
            Darabonba_Util::Client::assertAsMap(obj));
        return CreateShareModel(
            {{"body", !respMap ? boost::any() : boost::any(*respMap)},
             {"headers", boost::any(response_->headers)}});
      }
      if (!Darabonba_Util::Client::empty(
              make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(
            {{"data",
              boost::any(map<string, boost::any>(
                  {{"requestId",
                    boost::any(string(response_->headers["x-ca-request-id"]))},
                   {"statusCode", boost::any(response_->statusCode)},
                   {"statusMessage",
                    boost::any(string(response_->statusMessage))}}))},
             {"message",
              boost::any(string(response_->headers["x-ca-error-message"]))}})));
      }
      obj = make_shared<boost::any>(
          Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(
          Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(
          Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(
              map<string, boost::any>(
                  {{"data",
                    boost::any(map<string, boost::any>(
                        {{"requestId",
                          boost::any(
                              string(response_->headers["x-ca-request-id"]))},
                         {"statusCode", boost::any(response_->statusCode)},
                         {"statusMessage",
                          boost::any(string(response_->statusMessage))}}))}}),
              !respMap ? map<string, boost::any>() : *respMap))));
    } catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(
      Darabonba::UnretryableError(_lastRequest, _lastException));
}

DeleteShareModel Alibabacloud_Hosting::Client::deleteShareEx(
    shared_ptr<DeleteShareRequest> request,
    shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<
      map<string, boost::any>>(map<string, boost::any>(
      {{"timeouted", boost::any(string("retry"))},
       {"readTimeout", !runtime->readTimeout
                           ? boost::any()
                           : boost::any(*runtime->readTimeout)},
       {"connectTimeout", !runtime->connectTimeout
                              ? boost::any()
                              : boost::any(*runtime->connectTimeout)},
       {"localAddr",
        !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
       {"httpProxy",
        !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
       {"httpsProxy",
        !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
       {"noProxy", !runtime->noProxy ? boost::any()
                                     : boost::any(*runtime->noProxy)},
       {"maxIdleConns", !runtime->maxIdleConns
                            ? boost::any()
                            : boost::any(*runtime->maxIdleConns)},
       {"socks5Proxy", !runtime->socks5Proxy
                           ? boost::any()
                           : boost::any(*runtime->socks5Proxy)},
       {"socks5NetWork", !runtime->socks5NetWork
                             ? boost::any()
                             : boost::any(*runtime->socks5NetWork)},
       {"retry", boost::any(map<string, boost::any>(
                     {{"retryable", !runtime->autoretry
                                        ? boost::any()
                                        : boost::any(*runtime->autoretry)},
                      {"maxAttempts",
                       boost::any(Darabonba_Util::Client::defaultNumber(
                           runtime->maxAttempts, make_shared<int>(3)))}}))},
       {"backoff",
        boost::any(map<string, boost::any>(
            {{"policy",
              boost::any(string(Darabonba_Util::Client::defaultString(
                  runtime->backoffPolicy, make_shared<string>("no"))))},
             {"period", boost::any(Darabonba_Util::Client::defaultNumber(
                            runtime->backoffPeriod, make_shared<int>(1)))}}))},
       {"ignoreSSL", !runtime->ignoreSSL ? boost::any()
                                         : boost::any(*runtime->ignoreSSL)}}));
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(
      make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime =
          make_shared<int>(Darabonba::Core::getBackoffTime(
              make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ =
          make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret =
          make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken =
          make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq =
          make_shared<map<string, boost::any>>(
              Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(
          _protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(
          _nickname, make_shared<string>(string("/v2/hosting/share/delete")));
      request_->headers = Darabonba::Converter::merge(
          map<string, string>(
              {{"user-agent", getUserAgent()},
               {"host",
                Darabonba_Util::Client::defaultString(
                    _endpoint, make_shared<string>(string(
                                   "" + *_domainId + ".api.aliyunpds.com")))},
               {"content-type", "application/json; charset=utf-8"}}),
          !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>(
            "authorization", string("Bearer " + *accessToken + "")));
      } else if (!Darabonba_Util::Client::empty(accesskeyId) &&
                 !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(
              pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>(
            "date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(
            pair<string, string>("accept", "application/json"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(
            Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>(
            "authorization", string("acs " + *accesskeyId + ":" +
                                    Alibabacloud_ROAUtil::Client::getSignature(
                                        stringToSign, accessKeySecret) +
                                    "")));
      }
      request_->body = Darabonba::Converter::toStream(
          Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ =
          make_shared<Darabonba::Response>(
              Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(
              make_shared<int>(response_->statusCode), make_shared<int>(204))) {
        return DeleteShareModel({{"headers", boost::any(response_->headers)}});
      }
      if (!Darabonba_Util::Client::empty(
              make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(
            {{"data",
              boost::any(map<string, boost::any>(
                  {{"requestId",
                    boost::any(string(response_->headers["x-ca-request-id"]))},
                   {"statusCode", boost::any(response_->statusCode)},
                   {"statusMessage",
                    boost::any(string(response_->statusMessage))}}))},
             {"message",
              boost::any(string(response_->headers["x-ca-error-message"]))}})));
      }
      obj = make_shared<boost::any>(
          Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(
          Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(
          Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(
              map<string, boost::any>(
                  {{"data",
                    boost::any(map<string, boost::any>(
                        {{"requestId",
                          boost::any(
                              string(response_->headers["x-ca-request-id"]))},
                         {"statusCode", boost::any(response_->statusCode)},
                         {"statusMessage",
                          boost::any(string(response_->statusMessage))}}))}}),
              !respMap ? map<string, boost::any>() : *respMap))));
    } catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(
      Darabonba::UnretryableError(_lastRequest, _lastException));
}

GetShareModel
Alibabacloud_Hosting::Client::getShareEx(shared_ptr<GetShareRequest> request,
                                         shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<
      map<string, boost::any>>(map<string, boost::any>(
      {{"timeouted", boost::any(string("retry"))},
       {"readTimeout", !runtime->readTimeout
                           ? boost::any()
                           : boost::any(*runtime->readTimeout)},
       {"connectTimeout", !runtime->connectTimeout
                              ? boost::any()
                              : boost::any(*runtime->connectTimeout)},
       {"localAddr",
        !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
       {"httpProxy",
        !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
       {"httpsProxy",
        !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
       {"noProxy", !runtime->noProxy ? boost::any()
                                     : boost::any(*runtime->noProxy)},
       {"maxIdleConns", !runtime->maxIdleConns
                            ? boost::any()
                            : boost::any(*runtime->maxIdleConns)},
       {"socks5Proxy", !runtime->socks5Proxy
                           ? boost::any()
                           : boost::any(*runtime->socks5Proxy)},
       {"socks5NetWork", !runtime->socks5NetWork
                             ? boost::any()
                             : boost::any(*runtime->socks5NetWork)},
       {"retry", boost::any(map<string, boost::any>(
                     {{"retryable", !runtime->autoretry
                                        ? boost::any()
                                        : boost::any(*runtime->autoretry)},
                      {"maxAttempts",
                       boost::any(Darabonba_Util::Client::defaultNumber(
                           runtime->maxAttempts, make_shared<int>(3)))}}))},
       {"backoff",
        boost::any(map<string, boost::any>(
            {{"policy",
              boost::any(string(Darabonba_Util::Client::defaultString(
                  runtime->backoffPolicy, make_shared<string>("no"))))},
             {"period", boost::any(Darabonba_Util::Client::defaultNumber(
                            runtime->backoffPeriod, make_shared<int>(1)))}}))},
       {"ignoreSSL", !runtime->ignoreSSL ? boost::any()
                                         : boost::any(*runtime->ignoreSSL)}}));
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(
      make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime =
          make_shared<int>(Darabonba::Core::getBackoffTime(
              make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ =
          make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret =
          make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken =
          make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq =
          make_shared<map<string, boost::any>>(
              Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(
          _protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(
          _nickname, make_shared<string>(string("/v2/hosting/share/get")));
      request_->headers = Darabonba::Converter::merge(
          map<string, string>(
              {{"user-agent", getUserAgent()},
               {"host",
                Darabonba_Util::Client::defaultString(
                    _endpoint, make_shared<string>(string(
                                   "" + *_domainId + ".api.aliyunpds.com")))},
               {"content-type", "application/json; charset=utf-8"}}),
          !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>(
            "authorization", string("Bearer " + *accessToken + "")));
      } else if (!Darabonba_Util::Client::empty(accesskeyId) &&
                 !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(
              pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>(
            "date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(
            pair<string, string>("accept", "application/json"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(
            Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>(
            "authorization", string("acs " + *accesskeyId + ":" +
                                    Alibabacloud_ROAUtil::Client::getSignature(
                                        stringToSign, accessKeySecret) +
                                    "")));
      }
      request_->body = Darabonba::Converter::toStream(
          Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ =
          make_shared<Darabonba::Response>(
              Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(
              make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(
            Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(
            Darabonba_Util::Client::assertAsMap(obj));
        return GetShareModel(
            {{"body", !respMap ? boost::any() : boost::any(*respMap)},
             {"headers", boost::any(response_->headers)}});
      }
      if (!Darabonba_Util::Client::empty(
              make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(
            {{"data",
              boost::any(map<string, boost::any>(
                  {{"requestId",
                    boost::any(string(response_->headers["x-ca-request-id"]))},
                   {"statusCode", boost::any(response_->statusCode)},
                   {"statusMessage",
                    boost::any(string(response_->statusMessage))}}))},
             {"message",
              boost::any(string(response_->headers["x-ca-error-message"]))}})));
      }
      obj = make_shared<boost::any>(
          Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(
          Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(
          Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(
              map<string, boost::any>(
                  {{"data",
                    boost::any(map<string, boost::any>(
                        {{"requestId",
                          boost::any(
                              string(response_->headers["x-ca-request-id"]))},
                         {"statusCode", boost::any(response_->statusCode)},
                         {"statusMessage",
                          boost::any(string(response_->statusMessage))}}))}}),
              !respMap ? map<string, boost::any>() : *respMap))));
    } catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(
      Darabonba::UnretryableError(_lastRequest, _lastException));
}

ListShareModel
Alibabacloud_Hosting::Client::listShareEx(shared_ptr<ListShareRequest> request,
                                          shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<
      map<string, boost::any>>(map<string, boost::any>(
      {{"timeouted", boost::any(string("retry"))},
       {"readTimeout", !runtime->readTimeout
                           ? boost::any()
                           : boost::any(*runtime->readTimeout)},
       {"connectTimeout", !runtime->connectTimeout
                              ? boost::any()
                              : boost::any(*runtime->connectTimeout)},
       {"localAddr",
        !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
       {"httpProxy",
        !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
       {"httpsProxy",
        !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
       {"noProxy", !runtime->noProxy ? boost::any()
                                     : boost::any(*runtime->noProxy)},
       {"maxIdleConns", !runtime->maxIdleConns
                            ? boost::any()
                            : boost::any(*runtime->maxIdleConns)},
       {"socks5Proxy", !runtime->socks5Proxy
                           ? boost::any()
                           : boost::any(*runtime->socks5Proxy)},
       {"socks5NetWork", !runtime->socks5NetWork
                             ? boost::any()
                             : boost::any(*runtime->socks5NetWork)},
       {"retry", boost::any(map<string, boost::any>(
                     {{"retryable", !runtime->autoretry
                                        ? boost::any()
                                        : boost::any(*runtime->autoretry)},
                      {"maxAttempts",
                       boost::any(Darabonba_Util::Client::defaultNumber(
                           runtime->maxAttempts, make_shared<int>(3)))}}))},
       {"backoff",
        boost::any(map<string, boost::any>(
            {{"policy",
              boost::any(string(Darabonba_Util::Client::defaultString(
                  runtime->backoffPolicy, make_shared<string>("no"))))},
             {"period", boost::any(Darabonba_Util::Client::defaultNumber(
                            runtime->backoffPeriod, make_shared<int>(1)))}}))},
       {"ignoreSSL", !runtime->ignoreSSL ? boost::any()
                                         : boost::any(*runtime->ignoreSSL)}}));
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(
      make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime =
          make_shared<int>(Darabonba::Core::getBackoffTime(
              make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ =
          make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret =
          make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken =
          make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq =
          make_shared<map<string, boost::any>>(
              Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(
          _protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(
          _nickname, make_shared<string>(string("/v2/hosting/share/list")));
      request_->headers = Darabonba::Converter::merge(
          map<string, string>(
              {{"user-agent", getUserAgent()},
               {"host",
                Darabonba_Util::Client::defaultString(
                    _endpoint, make_shared<string>(string(
                                   "" + *_domainId + ".api.aliyunpds.com")))},
               {"content-type", "application/json; charset=utf-8"}}),
          !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>(
            "authorization", string("Bearer " + *accessToken + "")));
      } else if (!Darabonba_Util::Client::empty(accesskeyId) &&
                 !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(
              pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>(
            "date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(
            pair<string, string>("accept", "application/json"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(
            Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>(
            "authorization", string("acs " + *accesskeyId + ":" +
                                    Alibabacloud_ROAUtil::Client::getSignature(
                                        stringToSign, accessKeySecret) +
                                    "")));
      }
      request_->body = Darabonba::Converter::toStream(
          Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ =
          make_shared<Darabonba::Response>(
              Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(
              make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(
            Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(
            Darabonba_Util::Client::assertAsMap(obj));
        return ListShareModel(
            {{"body", !respMap ? boost::any() : boost::any(*respMap)},
             {"headers", boost::any(response_->headers)}});
      }
      if (!Darabonba_Util::Client::empty(
              make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(
            {{"data",
              boost::any(map<string, boost::any>(
                  {{"requestId",
                    boost::any(string(response_->headers["x-ca-request-id"]))},
                   {"statusCode", boost::any(response_->statusCode)},
                   {"statusMessage",
                    boost::any(string(response_->statusMessage))}}))},
             {"message",
              boost::any(string(response_->headers["x-ca-error-message"]))}})));
      }
      obj = make_shared<boost::any>(
          Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(
          Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(
          Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(
              map<string, boost::any>(
                  {{"data",
                    boost::any(map<string, boost::any>(
                        {{"requestId",
                          boost::any(
                              string(response_->headers["x-ca-request-id"]))},
                         {"statusCode", boost::any(response_->statusCode)},
                         {"statusMessage",
                          boost::any(string(response_->statusMessage))}}))}}),
              !respMap ? map<string, boost::any>() : *respMap))));
    } catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(
      Darabonba::UnretryableError(_lastRequest, _lastException));
}

UpdateShareModel Alibabacloud_Hosting::Client::updateShareEx(
    shared_ptr<UpdateShareRequest> request,
    shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<
      map<string, boost::any>>(map<string, boost::any>(
      {{"timeouted", boost::any(string("retry"))},
       {"readTimeout", !runtime->readTimeout
                           ? boost::any()
                           : boost::any(*runtime->readTimeout)},
       {"connectTimeout", !runtime->connectTimeout
                              ? boost::any()
                              : boost::any(*runtime->connectTimeout)},
       {"localAddr",
        !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
       {"httpProxy",
        !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
       {"httpsProxy",
        !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
       {"noProxy", !runtime->noProxy ? boost::any()
                                     : boost::any(*runtime->noProxy)},
       {"maxIdleConns", !runtime->maxIdleConns
                            ? boost::any()
                            : boost::any(*runtime->maxIdleConns)},
       {"socks5Proxy", !runtime->socks5Proxy
                           ? boost::any()
                           : boost::any(*runtime->socks5Proxy)},
       {"socks5NetWork", !runtime->socks5NetWork
                             ? boost::any()
                             : boost::any(*runtime->socks5NetWork)},
       {"retry", boost::any(map<string, boost::any>(
                     {{"retryable", !runtime->autoretry
                                        ? boost::any()
                                        : boost::any(*runtime->autoretry)},
                      {"maxAttempts",
                       boost::any(Darabonba_Util::Client::defaultNumber(
                           runtime->maxAttempts, make_shared<int>(3)))}}))},
       {"backoff",
        boost::any(map<string, boost::any>(
            {{"policy",
              boost::any(string(Darabonba_Util::Client::defaultString(
                  runtime->backoffPolicy, make_shared<string>("no"))))},
             {"period", boost::any(Darabonba_Util::Client::defaultNumber(
                            runtime->backoffPeriod, make_shared<int>(1)))}}))},
       {"ignoreSSL", !runtime->ignoreSSL ? boost::any()
                                         : boost::any(*runtime->ignoreSSL)}}));
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(
      make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime =
          make_shared<int>(Darabonba::Core::getBackoffTime(
              make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ =
          make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret =
          make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken =
          make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq =
          make_shared<map<string, boost::any>>(
              Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(
          _protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(
          _nickname, make_shared<string>(string("/v2/hosting/share/update")));
      request_->headers = Darabonba::Converter::merge(
          map<string, string>(
              {{"user-agent", getUserAgent()},
               {"host",
                Darabonba_Util::Client::defaultString(
                    _endpoint, make_shared<string>(string(
                                   "" + *_domainId + ".api.aliyunpds.com")))},
               {"content-type", "application/json; charset=utf-8"}}),
          !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>(
            "authorization", string("Bearer " + *accessToken + "")));
      } else if (!Darabonba_Util::Client::empty(accesskeyId) &&
                 !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(
              pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>(
            "date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(
            pair<string, string>("accept", "application/json"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(
            Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>(
            "authorization", string("acs " + *accesskeyId + ":" +
                                    Alibabacloud_ROAUtil::Client::getSignature(
                                        stringToSign, accessKeySecret) +
                                    "")));
      }
      request_->body = Darabonba::Converter::toStream(
          Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ =
          make_shared<Darabonba::Response>(
              Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(
              make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(
            Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(
            Darabonba_Util::Client::assertAsMap(obj));
        return UpdateShareModel(
            {{"body", !respMap ? boost::any() : boost::any(*respMap)},
             {"headers", boost::any(response_->headers)}});
      }
      if (!Darabonba_Util::Client::empty(
              make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(
            {{"data",
              boost::any(map<string, boost::any>(
                  {{"requestId",
                    boost::any(string(response_->headers["x-ca-request-id"]))},
                   {"statusCode", boost::any(response_->statusCode)},
                   {"statusMessage",
                    boost::any(string(response_->statusMessage))}}))},
             {"message",
              boost::any(string(response_->headers["x-ca-error-message"]))}})));
      }
      obj = make_shared<boost::any>(
          Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(
          Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(
          Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(
              map<string, boost::any>(
                  {{"data",
                    boost::any(map<string, boost::any>(
                        {{"requestId",
                          boost::any(
                              string(response_->headers["x-ca-request-id"]))},
                         {"statusCode", boost::any(response_->statusCode)},
                         {"statusMessage",
                          boost::any(string(response_->statusMessage))}}))}}),
              !respMap ? map<string, boost::any>() : *respMap))));
    } catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(
      Darabonba::UnretryableError(_lastRequest, _lastException));
}

ListStorefileModel Alibabacloud_Hosting::Client::listStorefileEx(
    shared_ptr<ListStoreFileRequest> request,
    shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<
      map<string, boost::any>>(map<string, boost::any>(
      {{"timeouted", boost::any(string("retry"))},
       {"readTimeout", !runtime->readTimeout
                           ? boost::any()
                           : boost::any(*runtime->readTimeout)},
       {"connectTimeout", !runtime->connectTimeout
                              ? boost::any()
                              : boost::any(*runtime->connectTimeout)},
       {"localAddr",
        !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
       {"httpProxy",
        !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
       {"httpsProxy",
        !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
       {"noProxy", !runtime->noProxy ? boost::any()
                                     : boost::any(*runtime->noProxy)},
       {"maxIdleConns", !runtime->maxIdleConns
                            ? boost::any()
                            : boost::any(*runtime->maxIdleConns)},
       {"socks5Proxy", !runtime->socks5Proxy
                           ? boost::any()
                           : boost::any(*runtime->socks5Proxy)},
       {"socks5NetWork", !runtime->socks5NetWork
                             ? boost::any()
                             : boost::any(*runtime->socks5NetWork)},
       {"retry", boost::any(map<string, boost::any>(
                     {{"retryable", !runtime->autoretry
                                        ? boost::any()
                                        : boost::any(*runtime->autoretry)},
                      {"maxAttempts",
                       boost::any(Darabonba_Util::Client::defaultNumber(
                           runtime->maxAttempts, make_shared<int>(3)))}}))},
       {"backoff",
        boost::any(map<string, boost::any>(
            {{"policy",
              boost::any(string(Darabonba_Util::Client::defaultString(
                  runtime->backoffPolicy, make_shared<string>("no"))))},
             {"period", boost::any(Darabonba_Util::Client::defaultNumber(
                            runtime->backoffPeriod, make_shared<int>(1)))}}))},
       {"ignoreSSL", !runtime->ignoreSSL ? boost::any()
                                         : boost::any(*runtime->ignoreSSL)}}));
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(
      make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime =
          make_shared<int>(Darabonba::Core::getBackoffTime(
              make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ =
          make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret =
          make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken =
          make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq =
          make_shared<map<string, boost::any>>(
              Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(
          _protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(
          _nickname,
          make_shared<string>(string("/v2/hosting/store_file/list")));
      request_->headers = Darabonba::Converter::merge(
          map<string, string>(
              {{"user-agent", getUserAgent()},
               {"host",
                Darabonba_Util::Client::defaultString(
                    _endpoint, make_shared<string>(string(
                                   "" + *_domainId + ".api.aliyunpds.com")))},
               {"content-type", "application/json; charset=utf-8"}}),
          !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>(
            "authorization", string("Bearer " + *accessToken + "")));
      } else if (!Darabonba_Util::Client::empty(accesskeyId) &&
                 !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(
              pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>(
            "date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(
            pair<string, string>("accept", "application/json"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(
            Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>(
            "authorization", string("acs " + *accesskeyId + ":" +
                                    Alibabacloud_ROAUtil::Client::getSignature(
                                        stringToSign, accessKeySecret) +
                                    "")));
      }
      request_->body = Darabonba::Converter::toStream(
          Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ =
          make_shared<Darabonba::Response>(
              Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(
              make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(
            Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(
            Darabonba_Util::Client::assertAsMap(obj));
        return ListStorefileModel(
            {{"body", !respMap ? boost::any() : boost::any(*respMap)},
             {"headers", boost::any(response_->headers)}});
      }
      if (!Darabonba_Util::Client::empty(
              make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(
            {{"data",
              boost::any(map<string, boost::any>(
                  {{"requestId",
                    boost::any(string(response_->headers["x-ca-request-id"]))},
                   {"statusCode", boost::any(response_->statusCode)},
                   {"statusMessage",
                    boost::any(string(response_->statusMessage))}}))},
             {"message",
              boost::any(string(response_->headers["x-ca-error-message"]))}})));
      }
      obj = make_shared<boost::any>(
          Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(
          Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(
          Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(
              map<string, boost::any>(
                  {{"data",
                    boost::any(map<string, boost::any>(
                        {{"requestId",
                          boost::any(
                              string(response_->headers["x-ca-request-id"]))},
                         {"statusCode", boost::any(response_->statusCode)},
                         {"statusMessage",
                          boost::any(string(response_->statusMessage))}}))}}),
              !respMap ? map<string, boost::any>() : *respMap))));
    } catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(
      Darabonba::UnretryableError(_lastRequest, _lastException));
}

CreateUserModel Alibabacloud_Hosting::Client::createUserEx(
    shared_ptr<CreateUserRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<
      map<string, boost::any>>(map<string, boost::any>(
      {{"timeouted", boost::any(string("retry"))},
       {"readTimeout", !runtime->readTimeout
                           ? boost::any()
                           : boost::any(*runtime->readTimeout)},
       {"connectTimeout", !runtime->connectTimeout
                              ? boost::any()
                              : boost::any(*runtime->connectTimeout)},
       {"localAddr",
        !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
       {"httpProxy",
        !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
       {"httpsProxy",
        !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
       {"noProxy", !runtime->noProxy ? boost::any()
                                     : boost::any(*runtime->noProxy)},
       {"maxIdleConns", !runtime->maxIdleConns
                            ? boost::any()
                            : boost::any(*runtime->maxIdleConns)},
       {"socks5Proxy", !runtime->socks5Proxy
                           ? boost::any()
                           : boost::any(*runtime->socks5Proxy)},
       {"socks5NetWork", !runtime->socks5NetWork
                             ? boost::any()
                             : boost::any(*runtime->socks5NetWork)},
       {"retry", boost::any(map<string, boost::any>(
                     {{"retryable", !runtime->autoretry
                                        ? boost::any()
                                        : boost::any(*runtime->autoretry)},
                      {"maxAttempts",
                       boost::any(Darabonba_Util::Client::defaultNumber(
                           runtime->maxAttempts, make_shared<int>(3)))}}))},
       {"backoff",
        boost::any(map<string, boost::any>(
            {{"policy",
              boost::any(string(Darabonba_Util::Client::defaultString(
                  runtime->backoffPolicy, make_shared<string>("no"))))},
             {"period", boost::any(Darabonba_Util::Client::defaultNumber(
                            runtime->backoffPeriod, make_shared<int>(1)))}}))},
       {"ignoreSSL", !runtime->ignoreSSL ? boost::any()
                                         : boost::any(*runtime->ignoreSSL)}}));
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(
      make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime =
          make_shared<int>(Darabonba::Core::getBackoffTime(
              make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ =
          make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret =
          make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken =
          make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq =
          make_shared<map<string, boost::any>>(
              Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(
          _protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(
          _nickname, make_shared<string>(string("/v2/user/create")));
      request_->headers = Darabonba::Converter::merge(
          map<string, string>(
              {{"user-agent", getUserAgent()},
               {"host",
                Darabonba_Util::Client::defaultString(
                    _endpoint, make_shared<string>(string(
                                   "" + *_domainId + ".api.aliyunpds.com")))},
               {"content-type", "application/json; charset=utf-8"}}),
          !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>(
            "authorization", string("Bearer " + *accessToken + "")));
      } else if (!Darabonba_Util::Client::empty(accesskeyId) &&
                 !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(
              pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>(
            "date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(
            pair<string, string>("accept", "application/json"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(
            Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>(
            "authorization", string("acs " + *accesskeyId + ":" +
                                    Alibabacloud_ROAUtil::Client::getSignature(
                                        stringToSign, accessKeySecret) +
                                    "")));
      }
      request_->body = Darabonba::Converter::toStream(
          Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ =
          make_shared<Darabonba::Response>(
              Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(
              make_shared<int>(response_->statusCode), make_shared<int>(201))) {
        obj = make_shared<boost::any>(
            Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(
            Darabonba_Util::Client::assertAsMap(obj));
        return CreateUserModel(
            {{"body", !respMap ? boost::any() : boost::any(*respMap)},
             {"headers", boost::any(response_->headers)}});
      }
      if (!Darabonba_Util::Client::empty(
              make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(
            {{"data",
              boost::any(map<string, boost::any>(
                  {{"requestId",
                    boost::any(string(response_->headers["x-ca-request-id"]))},
                   {"statusCode", boost::any(response_->statusCode)},
                   {"statusMessage",
                    boost::any(string(response_->statusMessage))}}))},
             {"message",
              boost::any(string(response_->headers["x-ca-error-message"]))}})));
      }
      obj = make_shared<boost::any>(
          Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(
          Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(
          Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(
              map<string, boost::any>(
                  {{"data",
                    boost::any(map<string, boost::any>(
                        {{"requestId",
                          boost::any(
                              string(response_->headers["x-ca-request-id"]))},
                         {"statusCode", boost::any(response_->statusCode)},
                         {"statusMessage",
                          boost::any(string(response_->statusMessage))}}))}}),
              !respMap ? map<string, boost::any>() : *respMap))));
    } catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(
      Darabonba::UnretryableError(_lastRequest, _lastException));
}

DeleteUserModel Alibabacloud_Hosting::Client::deleteUserEx(
    shared_ptr<DeleteUserRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<
      map<string, boost::any>>(map<string, boost::any>(
      {{"timeouted", boost::any(string("retry"))},
       {"readTimeout", !runtime->readTimeout
                           ? boost::any()
                           : boost::any(*runtime->readTimeout)},
       {"connectTimeout", !runtime->connectTimeout
                              ? boost::any()
                              : boost::any(*runtime->connectTimeout)},
       {"localAddr",
        !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
       {"httpProxy",
        !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
       {"httpsProxy",
        !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
       {"noProxy", !runtime->noProxy ? boost::any()
                                     : boost::any(*runtime->noProxy)},
       {"maxIdleConns", !runtime->maxIdleConns
                            ? boost::any()
                            : boost::any(*runtime->maxIdleConns)},
       {"socks5Proxy", !runtime->socks5Proxy
                           ? boost::any()
                           : boost::any(*runtime->socks5Proxy)},
       {"socks5NetWork", !runtime->socks5NetWork
                             ? boost::any()
                             : boost::any(*runtime->socks5NetWork)},
       {"retry", boost::any(map<string, boost::any>(
                     {{"retryable", !runtime->autoretry
                                        ? boost::any()
                                        : boost::any(*runtime->autoretry)},
                      {"maxAttempts",
                       boost::any(Darabonba_Util::Client::defaultNumber(
                           runtime->maxAttempts, make_shared<int>(3)))}}))},
       {"backoff",
        boost::any(map<string, boost::any>(
            {{"policy",
              boost::any(string(Darabonba_Util::Client::defaultString(
                  runtime->backoffPolicy, make_shared<string>("no"))))},
             {"period", boost::any(Darabonba_Util::Client::defaultNumber(
                            runtime->backoffPeriod, make_shared<int>(1)))}}))},
       {"ignoreSSL", !runtime->ignoreSSL ? boost::any()
                                         : boost::any(*runtime->ignoreSSL)}}));
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(
      make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime =
          make_shared<int>(Darabonba::Core::getBackoffTime(
              make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ =
          make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret =
          make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken =
          make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq =
          make_shared<map<string, boost::any>>(
              Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(
          _protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(
          _nickname, make_shared<string>(string("/v2/user/delete")));
      request_->headers = Darabonba::Converter::merge(
          map<string, string>(
              {{"user-agent", getUserAgent()},
               {"host",
                Darabonba_Util::Client::defaultString(
                    _endpoint, make_shared<string>(string(
                                   "" + *_domainId + ".api.aliyunpds.com")))},
               {"content-type", "application/json; charset=utf-8"}}),
          !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>(
            "authorization", string("Bearer " + *accessToken + "")));
      } else if (!Darabonba_Util::Client::empty(accesskeyId) &&
                 !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(
              pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>(
            "date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(
            pair<string, string>("accept", "application/json"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(
            Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>(
            "authorization", string("acs " + *accesskeyId + ":" +
                                    Alibabacloud_ROAUtil::Client::getSignature(
                                        stringToSign, accessKeySecret) +
                                    "")));
      }
      request_->body = Darabonba::Converter::toStream(
          Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ =
          make_shared<Darabonba::Response>(
              Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(
              make_shared<int>(response_->statusCode), make_shared<int>(204))) {
        return DeleteUserModel({{"headers", boost::any(response_->headers)}});
      }
      if (!Darabonba_Util::Client::empty(
              make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(
            {{"data",
              boost::any(map<string, boost::any>(
                  {{"requestId",
                    boost::any(string(response_->headers["x-ca-request-id"]))},
                   {"statusCode", boost::any(response_->statusCode)},
                   {"statusMessage",
                    boost::any(string(response_->statusMessage))}}))},
             {"message",
              boost::any(string(response_->headers["x-ca-error-message"]))}})));
      }
      obj = make_shared<boost::any>(
          Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(
          Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(
          Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(
              map<string, boost::any>(
                  {{"data",
                    boost::any(map<string, boost::any>(
                        {{"requestId",
                          boost::any(
                              string(response_->headers["x-ca-request-id"]))},
                         {"statusCode", boost::any(response_->statusCode)},
                         {"statusMessage",
                          boost::any(string(response_->statusMessage))}}))}}),
              !respMap ? map<string, boost::any>() : *respMap))));
    } catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(
      Darabonba::UnretryableError(_lastRequest, _lastException));
}

GetUserModel
Alibabacloud_Hosting::Client::getUserEx(shared_ptr<GetUserRequest> request,
                                        shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<
      map<string, boost::any>>(map<string, boost::any>(
      {{"timeouted", boost::any(string("retry"))},
       {"readTimeout", !runtime->readTimeout
                           ? boost::any()
                           : boost::any(*runtime->readTimeout)},
       {"connectTimeout", !runtime->connectTimeout
                              ? boost::any()
                              : boost::any(*runtime->connectTimeout)},
       {"localAddr",
        !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
       {"httpProxy",
        !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
       {"httpsProxy",
        !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
       {"noProxy", !runtime->noProxy ? boost::any()
                                     : boost::any(*runtime->noProxy)},
       {"maxIdleConns", !runtime->maxIdleConns
                            ? boost::any()
                            : boost::any(*runtime->maxIdleConns)},
       {"socks5Proxy", !runtime->socks5Proxy
                           ? boost::any()
                           : boost::any(*runtime->socks5Proxy)},
       {"socks5NetWork", !runtime->socks5NetWork
                             ? boost::any()
                             : boost::any(*runtime->socks5NetWork)},
       {"retry", boost::any(map<string, boost::any>(
                     {{"retryable", !runtime->autoretry
                                        ? boost::any()
                                        : boost::any(*runtime->autoretry)},
                      {"maxAttempts",
                       boost::any(Darabonba_Util::Client::defaultNumber(
                           runtime->maxAttempts, make_shared<int>(3)))}}))},
       {"backoff",
        boost::any(map<string, boost::any>(
            {{"policy",
              boost::any(string(Darabonba_Util::Client::defaultString(
                  runtime->backoffPolicy, make_shared<string>("no"))))},
             {"period", boost::any(Darabonba_Util::Client::defaultNumber(
                            runtime->backoffPeriod, make_shared<int>(1)))}}))},
       {"ignoreSSL", !runtime->ignoreSSL ? boost::any()
                                         : boost::any(*runtime->ignoreSSL)}}));
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(
      make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime =
          make_shared<int>(Darabonba::Core::getBackoffTime(
              make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ =
          make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret =
          make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken =
          make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq =
          make_shared<map<string, boost::any>>(
              Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(
          _protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname =
          getPathname(_nickname, make_shared<string>(string("/v2/user/get")));
      request_->headers = Darabonba::Converter::merge(
          map<string, string>(
              {{"user-agent", getUserAgent()},
               {"host",
                Darabonba_Util::Client::defaultString(
                    _endpoint, make_shared<string>(string(
                                   "" + *_domainId + ".api.aliyunpds.com")))},
               {"content-type", "application/json; charset=utf-8"}}),
          !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>(
            "authorization", string("Bearer " + *accessToken + "")));
      } else if (!Darabonba_Util::Client::empty(accesskeyId) &&
                 !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(
              pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>(
            "date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(
            pair<string, string>("accept", "application/json"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(
            Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>(
            "authorization", string("acs " + *accesskeyId + ":" +
                                    Alibabacloud_ROAUtil::Client::getSignature(
                                        stringToSign, accessKeySecret) +
                                    "")));
      }
      request_->body = Darabonba::Converter::toStream(
          Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ =
          make_shared<Darabonba::Response>(
              Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(
              make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(
            Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(
            Darabonba_Util::Client::assertAsMap(obj));
        return GetUserModel(
            {{"body", !respMap ? boost::any() : boost::any(*respMap)},
             {"headers", boost::any(response_->headers)}});
      }
      if (!Darabonba_Util::Client::empty(
              make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(
            {{"data",
              boost::any(map<string, boost::any>(
                  {{"requestId",
                    boost::any(string(response_->headers["x-ca-request-id"]))},
                   {"statusCode", boost::any(response_->statusCode)},
                   {"statusMessage",
                    boost::any(string(response_->statusMessage))}}))},
             {"message",
              boost::any(string(response_->headers["x-ca-error-message"]))}})));
      }
      obj = make_shared<boost::any>(
          Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(
          Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(
          Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(
              map<string, boost::any>(
                  {{"data",
                    boost::any(map<string, boost::any>(
                        {{"requestId",
                          boost::any(
                              string(response_->headers["x-ca-request-id"]))},
                         {"statusCode", boost::any(response_->statusCode)},
                         {"statusMessage",
                          boost::any(string(response_->statusMessage))}}))}}),
              !respMap ? map<string, boost::any>() : *respMap))));
    } catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(
      Darabonba::UnretryableError(_lastRequest, _lastException));
}

ListUsersModel
Alibabacloud_Hosting::Client::listUsersEx(shared_ptr<ListUserRequest> request,
                                          shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<
      map<string, boost::any>>(map<string, boost::any>(
      {{"timeouted", boost::any(string("retry"))},
       {"readTimeout", !runtime->readTimeout
                           ? boost::any()
                           : boost::any(*runtime->readTimeout)},
       {"connectTimeout", !runtime->connectTimeout
                              ? boost::any()
                              : boost::any(*runtime->connectTimeout)},
       {"localAddr",
        !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
       {"httpProxy",
        !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
       {"httpsProxy",
        !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
       {"noProxy", !runtime->noProxy ? boost::any()
                                     : boost::any(*runtime->noProxy)},
       {"maxIdleConns", !runtime->maxIdleConns
                            ? boost::any()
                            : boost::any(*runtime->maxIdleConns)},
       {"socks5Proxy", !runtime->socks5Proxy
                           ? boost::any()
                           : boost::any(*runtime->socks5Proxy)},
       {"socks5NetWork", !runtime->socks5NetWork
                             ? boost::any()
                             : boost::any(*runtime->socks5NetWork)},
       {"retry", boost::any(map<string, boost::any>(
                     {{"retryable", !runtime->autoretry
                                        ? boost::any()
                                        : boost::any(*runtime->autoretry)},
                      {"maxAttempts",
                       boost::any(Darabonba_Util::Client::defaultNumber(
                           runtime->maxAttempts, make_shared<int>(3)))}}))},
       {"backoff",
        boost::any(map<string, boost::any>(
            {{"policy",
              boost::any(string(Darabonba_Util::Client::defaultString(
                  runtime->backoffPolicy, make_shared<string>("no"))))},
             {"period", boost::any(Darabonba_Util::Client::defaultNumber(
                            runtime->backoffPeriod, make_shared<int>(1)))}}))},
       {"ignoreSSL", !runtime->ignoreSSL ? boost::any()
                                         : boost::any(*runtime->ignoreSSL)}}));
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(
      make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime =
          make_shared<int>(Darabonba::Core::getBackoffTime(
              make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ =
          make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret =
          make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken =
          make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq =
          make_shared<map<string, boost::any>>(
              Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(
          _protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname =
          getPathname(_nickname, make_shared<string>(string("/v2/user/list")));
      request_->headers = Darabonba::Converter::merge(
          map<string, string>(
              {{"user-agent", getUserAgent()},
               {"host",
                Darabonba_Util::Client::defaultString(
                    _endpoint, make_shared<string>(string(
                                   "" + *_domainId + ".api.aliyunpds.com")))},
               {"content-type", "application/json; charset=utf-8"}}),
          !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>(
            "authorization", string("Bearer " + *accessToken + "")));
      } else if (!Darabonba_Util::Client::empty(accesskeyId) &&
                 !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(
              pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>(
            "date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(
            pair<string, string>("accept", "application/json"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(
            Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>(
            "authorization", string("acs " + *accesskeyId + ":" +
                                    Alibabacloud_ROAUtil::Client::getSignature(
                                        stringToSign, accessKeySecret) +
                                    "")));
      }
      request_->body = Darabonba::Converter::toStream(
          Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ =
          make_shared<Darabonba::Response>(
              Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(
              make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(
            Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(
            Darabonba_Util::Client::assertAsMap(obj));
        return ListUsersModel(
            {{"body", !respMap ? boost::any() : boost::any(*respMap)},
             {"headers", boost::any(response_->headers)}});
      }
      if (!Darabonba_Util::Client::empty(
              make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(
            {{"data",
              boost::any(map<string, boost::any>(
                  {{"requestId",
                    boost::any(string(response_->headers["x-ca-request-id"]))},
                   {"statusCode", boost::any(response_->statusCode)},
                   {"statusMessage",
                    boost::any(string(response_->statusMessage))}}))},
             {"message",
              boost::any(string(response_->headers["x-ca-error-message"]))}})));
      }
      obj = make_shared<boost::any>(
          Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(
          Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(
          Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(
              map<string, boost::any>(
                  {{"data",
                    boost::any(map<string, boost::any>(
                        {{"requestId",
                          boost::any(
                              string(response_->headers["x-ca-request-id"]))},
                         {"statusCode", boost::any(response_->statusCode)},
                         {"statusMessage",
                          boost::any(string(response_->statusMessage))}}))}}),
              !respMap ? map<string, boost::any>() : *respMap))));
    } catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(
      Darabonba::UnretryableError(_lastRequest, _lastException));
}

SearchUserModel Alibabacloud_Hosting::Client::searchUserEx(
    shared_ptr<SearchUserRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<
      map<string, boost::any>>(map<string, boost::any>(
      {{"timeouted", boost::any(string("retry"))},
       {"readTimeout", !runtime->readTimeout
                           ? boost::any()
                           : boost::any(*runtime->readTimeout)},
       {"connectTimeout", !runtime->connectTimeout
                              ? boost::any()
                              : boost::any(*runtime->connectTimeout)},
       {"localAddr",
        !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
       {"httpProxy",
        !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
       {"httpsProxy",
        !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
       {"noProxy", !runtime->noProxy ? boost::any()
                                     : boost::any(*runtime->noProxy)},
       {"maxIdleConns", !runtime->maxIdleConns
                            ? boost::any()
                            : boost::any(*runtime->maxIdleConns)},
       {"socks5Proxy", !runtime->socks5Proxy
                           ? boost::any()
                           : boost::any(*runtime->socks5Proxy)},
       {"socks5NetWork", !runtime->socks5NetWork
                             ? boost::any()
                             : boost::any(*runtime->socks5NetWork)},
       {"retry", boost::any(map<string, boost::any>(
                     {{"retryable", !runtime->autoretry
                                        ? boost::any()
                                        : boost::any(*runtime->autoretry)},
                      {"maxAttempts",
                       boost::any(Darabonba_Util::Client::defaultNumber(
                           runtime->maxAttempts, make_shared<int>(3)))}}))},
       {"backoff",
        boost::any(map<string, boost::any>(
            {{"policy",
              boost::any(string(Darabonba_Util::Client::defaultString(
                  runtime->backoffPolicy, make_shared<string>("no"))))},
             {"period", boost::any(Darabonba_Util::Client::defaultNumber(
                            runtime->backoffPeriod, make_shared<int>(1)))}}))},
       {"ignoreSSL", !runtime->ignoreSSL ? boost::any()
                                         : boost::any(*runtime->ignoreSSL)}}));
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(
      make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime =
          make_shared<int>(Darabonba::Core::getBackoffTime(
              make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ =
          make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret =
          make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken =
          make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq =
          make_shared<map<string, boost::any>>(
              Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(
          _protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(
          _nickname, make_shared<string>(string("/v2/user/search")));
      request_->headers = Darabonba::Converter::merge(
          map<string, string>(
              {{"user-agent", getUserAgent()},
               {"host",
                Darabonba_Util::Client::defaultString(
                    _endpoint, make_shared<string>(string(
                                   "" + *_domainId + ".api.aliyunpds.com")))},
               {"content-type", "application/json; charset=utf-8"}}),
          !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>(
            "authorization", string("Bearer " + *accessToken + "")));
      } else if (!Darabonba_Util::Client::empty(accesskeyId) &&
                 !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(
              pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>(
            "date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(
            pair<string, string>("accept", "application/json"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(
            Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>(
            "authorization", string("acs " + *accesskeyId + ":" +
                                    Alibabacloud_ROAUtil::Client::getSignature(
                                        stringToSign, accessKeySecret) +
                                    "")));
      }
      request_->body = Darabonba::Converter::toStream(
          Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ =
          make_shared<Darabonba::Response>(
              Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(
              make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(
            Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(
            Darabonba_Util::Client::assertAsMap(obj));
        return SearchUserModel(
            {{"body", !respMap ? boost::any() : boost::any(*respMap)},
             {"headers", boost::any(response_->headers)}});
      }
      if (!Darabonba_Util::Client::empty(
              make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(
            {{"data",
              boost::any(map<string, boost::any>(
                  {{"requestId",
                    boost::any(string(response_->headers["x-ca-request-id"]))},
                   {"statusCode", boost::any(response_->statusCode)},
                   {"statusMessage",
                    boost::any(string(response_->statusMessage))}}))},
             {"message",
              boost::any(string(response_->headers["x-ca-error-message"]))}})));
      }
      obj = make_shared<boost::any>(
          Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(
          Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(
          Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(
              map<string, boost::any>(
                  {{"data",
                    boost::any(map<string, boost::any>(
                        {{"requestId",
                          boost::any(
                              string(response_->headers["x-ca-request-id"]))},
                         {"statusCode", boost::any(response_->statusCode)},
                         {"statusMessage",
                          boost::any(string(response_->statusMessage))}}))}}),
              !respMap ? map<string, boost::any>() : *respMap))));
    } catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(
      Darabonba::UnretryableError(_lastRequest, _lastException));
}

UpdateUserModel Alibabacloud_Hosting::Client::updateUserEx(
    shared_ptr<UpdateUserRequest> request, shared_ptr<RuntimeOptions> runtime) {
  request->validate();
  runtime->validate();
  shared_ptr<map<string, boost::any>> runtime_ = make_shared<
      map<string, boost::any>>(map<string, boost::any>(
      {{"timeouted", boost::any(string("retry"))},
       {"readTimeout", !runtime->readTimeout
                           ? boost::any()
                           : boost::any(*runtime->readTimeout)},
       {"connectTimeout", !runtime->connectTimeout
                              ? boost::any()
                              : boost::any(*runtime->connectTimeout)},
       {"localAddr",
        !runtime->localAddr ? boost::any() : boost::any(*runtime->localAddr)},
       {"httpProxy",
        !runtime->httpProxy ? boost::any() : boost::any(*runtime->httpProxy)},
       {"httpsProxy",
        !runtime->httpsProxy ? boost::any() : boost::any(*runtime->httpsProxy)},
       {"noProxy", !runtime->noProxy ? boost::any()
                                     : boost::any(*runtime->noProxy)},
       {"maxIdleConns", !runtime->maxIdleConns
                            ? boost::any()
                            : boost::any(*runtime->maxIdleConns)},
       {"socks5Proxy", !runtime->socks5Proxy
                           ? boost::any()
                           : boost::any(*runtime->socks5Proxy)},
       {"socks5NetWork", !runtime->socks5NetWork
                             ? boost::any()
                             : boost::any(*runtime->socks5NetWork)},
       {"retry", boost::any(map<string, boost::any>(
                     {{"retryable", !runtime->autoretry
                                        ? boost::any()
                                        : boost::any(*runtime->autoretry)},
                      {"maxAttempts",
                       boost::any(Darabonba_Util::Client::defaultNumber(
                           runtime->maxAttempts, make_shared<int>(3)))}}))},
       {"backoff",
        boost::any(map<string, boost::any>(
            {{"policy",
              boost::any(string(Darabonba_Util::Client::defaultString(
                  runtime->backoffPolicy, make_shared<string>("no"))))},
             {"period", boost::any(Darabonba_Util::Client::defaultNumber(
                            runtime->backoffPeriod, make_shared<int>(1)))}}))},
       {"ignoreSSL", !runtime->ignoreSSL ? boost::any()
                                         : boost::any(*runtime->ignoreSSL)}}));
  shared_ptr<Darabonba::Request> _lastRequest;
  shared_ptr<std::exception> _lastException;
  shared_ptr<int> _now = make_shared<int>(0);
  shared_ptr<int> _retryTimes = make_shared<int>(0);
  while (Darabonba::Core::allowRetry(
      make_shared<boost::any>((*runtime_)["retry"]), _retryTimes, _now)) {
    if (*_retryTimes > 0) {
      shared_ptr<int> _backoffTime =
          make_shared<int>(Darabonba::Core::getBackoffTime(
              make_shared<boost::any>((*runtime_)["backoff"]), _retryTimes));
      if (*_backoffTime > 0) {
        Darabonba::Core::sleep(_backoffTime);
      }
    }
    _retryTimes = make_shared<int>(*_retryTimes + 1);
    try {
      shared_ptr<Darabonba::Request> request_ =
          make_shared<Darabonba::Request>();
      shared_ptr<string> accesskeyId = make_shared<string>(getAccessKeyId());
      shared_ptr<string> accessKeySecret =
          make_shared<string>(getAccessKeySecret());
      shared_ptr<string> securityToken =
          make_shared<string>(getSecurityToken());
      shared_ptr<string> accessToken = make_shared<string>(getAccessToken());
      shared_ptr<map<string, boost::any>> realReq =
          make_shared<map<string, boost::any>>(
              Darabonba_Util::Client::toMap(request));
      request_->protocol = Darabonba_Util::Client::defaultString(
          _protocol, make_shared<string>("https"));
      request_->method = "POST";
      request_->pathname = getPathname(
          _nickname, make_shared<string>(string("/v2/user/update")));
      request_->headers = Darabonba::Converter::merge(
          map<string, string>(
              {{"user-agent", getUserAgent()},
               {"host",
                Darabonba_Util::Client::defaultString(
                    _endpoint, make_shared<string>(string(
                                   "" + *_domainId + ".api.aliyunpds.com")))},
               {"content-type", "application/json; charset=utf-8"}}),
          !request->headers ? map<string, string>() : *request->headers);
      (*realReq)["headers"] = nullptr;
      if (!Darabonba_Util::Client::empty(accessToken)) {
        request_->headers.insert(pair<string, string>(
            "authorization", string("Bearer " + *accessToken + "")));
      } else if (!Darabonba_Util::Client::empty(accesskeyId) &&
                 !Darabonba_Util::Client::empty(accessKeySecret)) {
        if (!Darabonba_Util::Client::empty(securityToken)) {
          request_->headers.insert(
              pair<string, string>("x-acs-security-token", *securityToken));
        }
        request_->headers.insert(pair<string, string>(
            "date", Darabonba_Util::Client::getDateUTCString()));
        request_->headers.insert(
            pair<string, string>("accept", "application/json"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-method", "HMAC-SHA1"));
        request_->headers.insert(
            pair<string, string>("x-acs-signature-version", "1.0"));
        shared_ptr<string> stringToSign = make_shared<string>(
            Alibabacloud_ROAUtil::Client::getStringToSign(request_));
        request_->headers.insert(pair<string, string>(
            "authorization", string("acs " + *accesskeyId + ":" +
                                    Alibabacloud_ROAUtil::Client::getSignature(
                                        stringToSign, accessKeySecret) +
                                    "")));
      }
      request_->body = Darabonba::Converter::toStream(
          Darabonba_Util::Client::toJSONString(realReq));
      _lastRequest = request_;
      shared_ptr<Darabonba::Response> response_ =
          make_shared<Darabonba::Response>(
              Darabonba::Core::doAction(request_, runtime_));
      shared_ptr<map<string, boost::any>> respMap;
      shared_ptr<boost::any> obj;
      if (Darabonba_Util::Client::equalNumber(
              make_shared<int>(response_->statusCode), make_shared<int>(200))) {
        obj = make_shared<boost::any>(
            Darabonba_Util::Client::readAsJSON(response_->body));
        respMap = make_shared<map<string, boost::any>>(
            Darabonba_Util::Client::assertAsMap(obj));
        return UpdateUserModel(
            {{"body", !respMap ? boost::any() : boost::any(*respMap)},
             {"headers", boost::any(response_->headers)}});
      }
      if (!Darabonba_Util::Client::empty(
              make_shared<string>(response_->headers["x-ca-error-message"]))) {
        BOOST_THROW_EXCEPTION(Darabonba::Error(map<string, boost::any>(
            {{"data",
              boost::any(map<string, boost::any>(
                  {{"requestId",
                    boost::any(string(response_->headers["x-ca-request-id"]))},
                   {"statusCode", boost::any(response_->statusCode)},
                   {"statusMessage",
                    boost::any(string(response_->statusMessage))}}))},
             {"message",
              boost::any(string(response_->headers["x-ca-error-message"]))}})));
      }
      obj = make_shared<boost::any>(
          Darabonba_Util::Client::readAsJSON(response_->body));
      respMap = make_shared<map<string, boost::any>>(
          Darabonba_Util::Client::assertAsMap(obj));
      BOOST_THROW_EXCEPTION(
          Darabonba::Error(map<string, boost::any>(Darabonba::Converter::merge(
              map<string, boost::any>(
                  {{"data",
                    boost::any(map<string, boost::any>(
                        {{"requestId",
                          boost::any(
                              string(response_->headers["x-ca-request-id"]))},
                         {"statusCode", boost::any(response_->statusCode)},
                         {"statusMessage",
                          boost::any(string(response_->statusMessage))}}))}}),
              !respMap ? map<string, boost::any>() : *respMap))));
    } catch (std::exception &e) {
      if (Darabonba::Core::isRetryable(e)) {
        _lastException = make_shared<std::exception>(e);
        continue;
      }
      BOOST_THROW_EXCEPTION(e);
    }
  }
  BOOST_THROW_EXCEPTION(
      Darabonba::UnretryableError(_lastRequest, _lastException));
}

CancelLinkModel Alibabacloud_Hosting::Client::cancelLink(
    shared_ptr<CancelLinkRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return cancelLinkEx(request, runtime);
}

ConfirmLinkModel Alibabacloud_Hosting::Client::confirmLink(
    shared_ptr<ConfirmLinkRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return confirmLinkEx(request, runtime);
}

ChangePasswordModel Alibabacloud_Hosting::Client::changePassword(
    shared_ptr<DefaultChangePasswordRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return changePasswordEx(request, runtime);
}

SetPasswordModel Alibabacloud_Hosting::Client::setPassword(
    shared_ptr<DefaultSetPasswordRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return setPasswordEx(request, runtime);
}

VerifyCodeModel Alibabacloud_Hosting::Client::verifyCode(
    shared_ptr<VerifyCodeRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return verifyCodeEx(request, runtime);
}

GetAccessTokenByLinkInfoModel
Alibabacloud_Hosting::Client::getAccessTokenByLinkInfo(
    shared_ptr<GetAccessTokenByLinkInfoRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return getAccessTokenByLinkInfoEx(request, runtime);
}

GetCaptchaModel Alibabacloud_Hosting::Client::getCaptcha(
    shared_ptr<GetCaptchaRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return getCaptchaEx(request, runtime);
}

GetLinkInfoModel Alibabacloud_Hosting::Client::getLinkInfo(
    shared_ptr<GetByLinkInfoRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return getLinkInfoEx(request, runtime);
}

GetLinkInfoByUserIdModel Alibabacloud_Hosting::Client::getLinkInfoByUserId(
    shared_ptr<GetLinkInfoByUserIDRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return getLinkInfoByUserIdEx(request, runtime);
}

GetPublicKeyModel Alibabacloud_Hosting::Client::getPublicKey(
    shared_ptr<GetAppPublicKeyRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return getPublicKeyEx(request, runtime);
}

LinkModel
Alibabacloud_Hosting::Client::link(shared_ptr<AccountLinkRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return linkEx(request, runtime);
}

CheckExistModel Alibabacloud_Hosting::Client::checkExist(
    shared_ptr<MobileCheckExistRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return checkExistEx(request, runtime);
}

LoginModel
Alibabacloud_Hosting::Client::login(shared_ptr<MobileLoginRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return loginEx(request, runtime);
}

RegisterModel Alibabacloud_Hosting::Client::register_(
    shared_ptr<MobileRegisterRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return registerEx(request, runtime);
}

MobileSendSmsCodeModel Alibabacloud_Hosting::Client::mobileSendSmsCode(
    shared_ptr<MobileSendSmsCodeRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return mobileSendSmsCodeEx(request, runtime);
}

AccountRevokeModel
Alibabacloud_Hosting::Client::accountRevoke(shared_ptr<RevokeRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return accountRevokeEx(request, runtime);
}

AccountTokenModel
Alibabacloud_Hosting::Client::accountToken(shared_ptr<TokenRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return accountTokenEx(request, runtime);
}

AdminListStoresModel Alibabacloud_Hosting::Client::adminListStores(
    shared_ptr<AdminListStoresRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return adminListStoresEx(request, runtime);
}

GetUserAccessTokenModel Alibabacloud_Hosting::Client::getUserAccessToken(
    shared_ptr<GetUserAccessTokenRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return getUserAccessTokenEx(request, runtime);
}

CreateDriveModel Alibabacloud_Hosting::Client::createDrive(
    shared_ptr<CreateDriveRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return createDriveEx(request, runtime);
}

DeleteDriveModel Alibabacloud_Hosting::Client::deleteDrive(
    shared_ptr<DeleteDriveRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return deleteDriveEx(request, runtime);
}

GetDriveModel
Alibabacloud_Hosting::Client::getDrive(shared_ptr<GetDriveRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return getDriveEx(request, runtime);
}

GetDefaultDriveModel Alibabacloud_Hosting::Client::getDefaultDrive(
    shared_ptr<GetDefaultDriveRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return getDefaultDriveEx(request, runtime);
}

ListDrivesModel
Alibabacloud_Hosting::Client::listDrives(shared_ptr<ListDriveRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return listDrivesEx(request, runtime);
}

ListMyDrivesModel Alibabacloud_Hosting::Client::listMyDrives(
    shared_ptr<ListMyDriveRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return listMyDrivesEx(request, runtime);
}

UpdateDriveModel Alibabacloud_Hosting::Client::updateDrive(
    shared_ptr<UpdateDriveRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return updateDriveEx(request, runtime);
}

CompleteFileModel Alibabacloud_Hosting::Client::completeFile(
    shared_ptr<HostingCompleteFileRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return completeFileEx(request, runtime);
}

CopyFileModel Alibabacloud_Hosting::Client::copyFile(
    shared_ptr<HostingCopyFileRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return copyFileEx(request, runtime);
}

CreateFileModel Alibabacloud_Hosting::Client::createFile(
    shared_ptr<HostingCreateFileRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return createFileEx(request, runtime);
}

DeleteFileModel Alibabacloud_Hosting::Client::deleteFile(
    shared_ptr<HostingDeleteFileRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return deleteFileEx(request, runtime);
}

GetFileModel Alibabacloud_Hosting::Client::getFile(
    shared_ptr<HostingGetFileRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return getFileEx(request, runtime);
}

GetDownloadUrlModel Alibabacloud_Hosting::Client::getDownloadUrl(
    shared_ptr<HostingGetDownloadUrlRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return getDownloadUrlEx(request, runtime);
}

GetSecureUrlModel Alibabacloud_Hosting::Client::getSecureUrl(
    shared_ptr<HostingGetSecureUrlRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return getSecureUrlEx(request, runtime);
}

GetUploadUrlModel Alibabacloud_Hosting::Client::getUploadUrl(
    shared_ptr<HostingGetUploadUrlRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return getUploadUrlEx(request, runtime);
}

ListFileModel Alibabacloud_Hosting::Client::listFile(
    shared_ptr<HostingListFileRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return listFileEx(request, runtime);
}

ListUploadedPartsModel Alibabacloud_Hosting::Client::listUploadedParts(
    shared_ptr<HostingListUploadedPartRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return listUploadedPartsEx(request, runtime);
}

MoveFileModel Alibabacloud_Hosting::Client::moveFile(
    shared_ptr<HostingMoveFileRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return moveFileEx(request, runtime);
}

VideoDefinitionModel Alibabacloud_Hosting::Client::videoDefinition(
    shared_ptr<HostingVideoDefinitionRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return videoDefinitionEx(request, runtime);
}

VideoLicenseModel Alibabacloud_Hosting::Client::videoLicense(
    shared_ptr<HostingVideoDRMLicenseRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return videoLicenseEx(request, runtime);
}

VideoM3u8Model Alibabacloud_Hosting::Client::videoM3u8(
    shared_ptr<HostingVideoM3U8Request> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return videoM3u8Ex(request, runtime);
}

VideoTranscodeModel Alibabacloud_Hosting::Client::videoTranscode(
    shared_ptr<HostingVideoTranscodeRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return videoTranscodeEx(request, runtime);
}

CreateShareModel Alibabacloud_Hosting::Client::createShare(
    shared_ptr<CreateShareRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return createShareEx(request, runtime);
}

DeleteShareModel Alibabacloud_Hosting::Client::deleteShare(
    shared_ptr<DeleteShareRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return deleteShareEx(request, runtime);
}

GetShareModel
Alibabacloud_Hosting::Client::getShare(shared_ptr<GetShareRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return getShareEx(request, runtime);
}

ListShareModel
Alibabacloud_Hosting::Client::listShare(shared_ptr<ListShareRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return listShareEx(request, runtime);
}

UpdateShareModel Alibabacloud_Hosting::Client::updateShare(
    shared_ptr<UpdateShareRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return updateShareEx(request, runtime);
}

ListStorefileModel Alibabacloud_Hosting::Client::listStorefile(
    shared_ptr<ListStoreFileRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return listStorefileEx(request, runtime);
}

CreateUserModel Alibabacloud_Hosting::Client::createUser(
    shared_ptr<CreateUserRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return createUserEx(request, runtime);
}

DeleteUserModel Alibabacloud_Hosting::Client::deleteUser(
    shared_ptr<DeleteUserRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return deleteUserEx(request, runtime);
}

GetUserModel
Alibabacloud_Hosting::Client::getUser(shared_ptr<GetUserRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return getUserEx(request, runtime);
}

ListUsersModel
Alibabacloud_Hosting::Client::listUsers(shared_ptr<ListUserRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return listUsersEx(request, runtime);
}

SearchUserModel Alibabacloud_Hosting::Client::searchUser(
    shared_ptr<SearchUserRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return searchUserEx(request, runtime);
}

UpdateUserModel Alibabacloud_Hosting::Client::updateUser(
    shared_ptr<UpdateUserRequest> request) {
  shared_ptr<RuntimeOptions> runtime = make_shared<RuntimeOptions>();
  return updateUserEx(request, runtime);
}

string Alibabacloud_Hosting::Client::getPathname(shared_ptr<string> nickname,
                                                 shared_ptr<string> path) {
  if (Darabonba_Util::Client::empty(nickname)) {
    return *path;
  }
  return string("/" + *nickname + "" + *path + "");
}

void Alibabacloud_Hosting::Client::setExpireTime(
    shared_ptr<string> expireTime) {
  if (Darabonba_Util::Client::isUnset<
          Alibabacloud_AccessTokenCredential::Client>(_accessTokenCredential)) {
    return;
  }
  _accessTokenCredential->setExpireTime(expireTime);
}

string Alibabacloud_Hosting::Client::getExpireTime() {
  if (Darabonba_Util::Client::isUnset<
          Alibabacloud_AccessTokenCredential::Client>(_accessTokenCredential)) {
    return string("");
  }
  shared_ptr<string> expireTime =
      make_shared<string>(_accessTokenCredential->getExpireTime());
  return *expireTime;
}

void Alibabacloud_Hosting::Client::setRefreshToken(shared_ptr<string> token) {
  if (Darabonba_Util::Client::isUnset<
          Alibabacloud_AccessTokenCredential::Client>(_accessTokenCredential)) {
    return;
  }
  _accessTokenCredential->setRefreshToken(token);
}

string Alibabacloud_Hosting::Client::getRefreshToken() {
  if (Darabonba_Util::Client::isUnset<
          Alibabacloud_AccessTokenCredential::Client>(_accessTokenCredential)) {
    return string("");
  }
  shared_ptr<string> token =
      make_shared<string>(_accessTokenCredential->getRefreshToken());
  return *token;
}

void Alibabacloud_Hosting::Client::setAccessToken(shared_ptr<string> token) {
  if (Darabonba_Util::Client::isUnset<
          Alibabacloud_AccessTokenCredential::Client>(_accessTokenCredential)) {
    return;
  }
  _accessTokenCredential->setAccessToken(token);
}

string Alibabacloud_Hosting::Client::getAccessToken() {
  if (Darabonba_Util::Client::isUnset<
          Alibabacloud_AccessTokenCredential::Client>(_accessTokenCredential)) {
    return string("");
  }
  shared_ptr<string> token =
      make_shared<string>(_accessTokenCredential->getAccessToken());
  return *token;
}

void Alibabacloud_Hosting::Client::setUserAgent(shared_ptr<string> userAgent) {
  _userAgent = userAgent;
}

void Alibabacloud_Hosting::Client::appendUserAgent(
    shared_ptr<string> userAgent) {
  _userAgent =
      make_shared<string>(string("" + *_userAgent + " " + *userAgent + ""));
}

string Alibabacloud_Hosting::Client::getUserAgent() {
  shared_ptr<string> userAgent =
      make_shared<string>(Darabonba_Util::Client::getUserAgent(_userAgent));
  return *userAgent;
}

string Alibabacloud_Hosting::Client::getAccessKeyId() {
  if (Darabonba_Util::Client::isUnset<Alibabacloud_Credential::Client>(
          _credential)) {
    return string("");
  }
  shared_ptr<string> accessKeyId =
      make_shared<string>(_credential->getAccessKeyId());
  return *accessKeyId;
}

string Alibabacloud_Hosting::Client::getAccessKeySecret() {
  if (Darabonba_Util::Client::isUnset<Alibabacloud_Credential::Client>(
          _credential)) {
    return string("");
  }
  shared_ptr<string> secret =
      make_shared<string>(_credential->getAccessKeySecret());
  return *secret;
}

string Alibabacloud_Hosting::Client::getSecurityToken() {
  if (Darabonba_Util::Client::isUnset<Alibabacloud_Credential::Client>(
          _credential)) {
    return string("");
  }
  shared_ptr<string> token =
      make_shared<string>(_credential->getSecurityToken());
  return *token;
}
