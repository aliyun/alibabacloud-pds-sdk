// This file is auto-generated, don't edit it. Thanks.

#ifndef ALIBABACLOUD_ACCESSTOKENCREDENTIAL_H_
#define ALIBABACLOUD_ACCESSTOKENCREDENTIAL_H_

#include <boost/throw_exception.hpp>
#include <darabonba/core.hpp>
#include <iostream>

using namespace std;

namespace Alibabacloud_AccessTokenCredential {
class Config : public Darabonba::Model {
public:
  shared_ptr<string> endpoint{};
  shared_ptr<string> domainId{};
  shared_ptr<string> clientId{};
  shared_ptr<string> refreshToken{};
  shared_ptr<string> clientSecret{};
  shared_ptr<string> accessToken{};
  shared_ptr<string> expireTime{};

  Config() {}

  explicit Config(const std::map<string, boost::any> &config)
      : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!domainId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(
          std::runtime_error("domainId is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (endpoint) {
      res["endpoint"] = boost::any(*endpoint);
    }
    if (domainId) {
      res["domainId"] = boost::any(*domainId);
    }
    if (clientId) {
      res["clientId"] = boost::any(*clientId);
    }
    if (refreshToken) {
      res["refreshToken"] = boost::any(*refreshToken);
    }
    if (clientSecret) {
      res["clientSecret"] = boost::any(*clientSecret);
    }
    if (accessToken) {
      res["accessToken"] = boost::any(*accessToken);
    }
    if (expireTime) {
      res["expireTime"] = boost::any(*expireTime);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("endpoint") != m.end() && !m["endpoint"].empty()) {
      endpoint = make_shared<string>(boost::any_cast<string>(m["endpoint"]));
    }
    if (m.find("domainId") != m.end() && !m["domainId"].empty()) {
      domainId = make_shared<string>(boost::any_cast<string>(m["domainId"]));
    }
    if (m.find("clientId") != m.end() && !m["clientId"].empty()) {
      clientId = make_shared<string>(boost::any_cast<string>(m["clientId"]));
    }
    if (m.find("refreshToken") != m.end() && !m["refreshToken"].empty()) {
      refreshToken =
          make_shared<string>(boost::any_cast<string>(m["refreshToken"]));
    }
    if (m.find("clientSecret") != m.end() && !m["clientSecret"].empty()) {
      clientSecret =
          make_shared<string>(boost::any_cast<string>(m["clientSecret"]));
    }
    if (m.find("accessToken") != m.end() && !m["accessToken"].empty()) {
      accessToken =
          make_shared<string>(boost::any_cast<string>(m["accessToken"]));
    }
    if (m.find("expireTime") != m.end() && !m["expireTime"].empty()) {
      expireTime =
          make_shared<string>(boost::any_cast<string>(m["expireTime"]));
    }
  }

  virtual ~Config() = default;
};
class Client {
public:
  shared_ptr<string> _endpoint{};
  shared_ptr<string> _domainId{};
  shared_ptr<string> _clientId{};
  shared_ptr<string> _refreshToken{};
  shared_ptr<string> _clientSecret{};
  shared_ptr<string> _accessToken{};
  shared_ptr<string> _expireTime{};
  explicit Client(const shared_ptr<Config> &config);
  void setExpireTime(shared_ptr<string> expireTime);
  string getExpireTime();
  string getRefreshToken();
  void setRefreshToken(shared_ptr<string> refreshToken);
  void setAccessToken(shared_ptr<string> accessToken);
  string getAccessToken();

  virtual ~Client() = default;
};
} // namespace Alibabacloud_AccessTokenCredential

#endif
