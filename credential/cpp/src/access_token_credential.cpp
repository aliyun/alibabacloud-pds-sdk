// This file is auto-generated, don't edit it. Thanks.

#include <alibabacloud/access_token_credential.hpp>
#include <boost/throw_exception.hpp>
#include <darabonba/core.hpp>
#include <iostream>

using namespace std;

using namespace Alibabacloud_AccessTokenCredential;

Alibabacloud_AccessTokenCredential::Client::Client(
    const shared_ptr<Config> &config) {
  _endpoint = config->endpoint;
  _domainId = config->domainId;
  _clientId = config->clientId;
  _refreshToken = config->refreshToken;
  _clientSecret = config->clientSecret;
  _accessToken = config->accessToken;
  _expireTime = config->expireTime;
};

void Alibabacloud_AccessTokenCredential::Client::setExpireTime(
    shared_ptr<string> expireTime) {
  _expireTime = expireTime;
}

string Alibabacloud_AccessTokenCredential::Client::getExpireTime() {
  return *_expireTime;
}

string Alibabacloud_AccessTokenCredential::Client::getRefreshToken() {
  return *_refreshToken;
}

void Alibabacloud_AccessTokenCredential::Client::setRefreshToken(
    shared_ptr<string> refreshToken) {
  _refreshToken = refreshToken;
}

void Alibabacloud_AccessTokenCredential::Client::setAccessToken(
    shared_ptr<string> accessToken) {
  _accessToken = accessToken;
}

string Alibabacloud_AccessTokenCredential::Client::getAccessToken() {
  BOOST_THROW_EXCEPTION(std::runtime_error("Un-implemented"));
}
