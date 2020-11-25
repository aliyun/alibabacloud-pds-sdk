// This file is auto-generated, don't edit it. Thanks.

#ifndef ALIBABACLOUD_PDS_H_
#define ALIBABACLOUD_PDS_H_

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

namespace Alibabacloud_Pds {
class RuntimeOptions : public Darabonba::Model {
public:
  shared_ptr<bool> autoretry{};
  shared_ptr<bool> ignoreSSL{};
  shared_ptr<int> maxAttempts{};
  shared_ptr<string> backoffPolicy{};
  shared_ptr<int> backoffPeriod{};
  shared_ptr<int> readTimeout{};
  shared_ptr<int> connectTimeout{};
  shared_ptr<string> httpProxy{};
  shared_ptr<string> httpsProxy{};
  shared_ptr<string> noProxy{};
  shared_ptr<int> maxIdleConns{};
  shared_ptr<string> localAddr{};
  shared_ptr<string> socks5Proxy{};
  shared_ptr<string> socks5NetWork{};

  RuntimeOptions() {}

  explicit RuntimeOptions(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (autoretry) {
      res["autoretry"] = boost::any(*autoretry);
    }
    if (ignoreSSL) {
      res["ignoreSSL"] = boost::any(*ignoreSSL);
    }
    if (maxAttempts) {
      res["maxAttempts"] = boost::any(*maxAttempts);
    }
    if (backoffPolicy) {
      res["backoffPolicy"] = boost::any(*backoffPolicy);
    }
    if (backoffPeriod) {
      res["backoffPeriod"] = boost::any(*backoffPeriod);
    }
    if (readTimeout) {
      res["readTimeout"] = boost::any(*readTimeout);
    }
    if (connectTimeout) {
      res["connectTimeout"] = boost::any(*connectTimeout);
    }
    if (httpProxy) {
      res["httpProxy"] = boost::any(*httpProxy);
    }
    if (httpsProxy) {
      res["httpsProxy"] = boost::any(*httpsProxy);
    }
    if (noProxy) {
      res["noProxy"] = boost::any(*noProxy);
    }
    if (maxIdleConns) {
      res["maxIdleConns"] = boost::any(*maxIdleConns);
    }
    if (localAddr) {
      res["localAddr"] = boost::any(*localAddr);
    }
    if (socks5Proxy) {
      res["socks5Proxy"] = boost::any(*socks5Proxy);
    }
    if (socks5NetWork) {
      res["socks5NetWork"] = boost::any(*socks5NetWork);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("autoretry") != m.end() && !m["autoretry"].empty()) {
      autoretry = make_shared<bool>(boost::any_cast<bool>(m["autoretry"]));
    }
    if (m.find("ignoreSSL") != m.end() && !m["ignoreSSL"].empty()) {
      ignoreSSL = make_shared<bool>(boost::any_cast<bool>(m["ignoreSSL"]));
    }
    if (m.find("maxAttempts") != m.end() && !m["maxAttempts"].empty()) {
      maxAttempts = make_shared<int>(boost::any_cast<int>(m["maxAttempts"]));
    }
    if (m.find("backoffPolicy") != m.end() && !m["backoffPolicy"].empty()) {
      backoffPolicy = make_shared<string>(boost::any_cast<string>(m["backoffPolicy"]));
    }
    if (m.find("backoffPeriod") != m.end() && !m["backoffPeriod"].empty()) {
      backoffPeriod = make_shared<int>(boost::any_cast<int>(m["backoffPeriod"]));
    }
    if (m.find("readTimeout") != m.end() && !m["readTimeout"].empty()) {
      readTimeout = make_shared<int>(boost::any_cast<int>(m["readTimeout"]));
    }
    if (m.find("connectTimeout") != m.end() && !m["connectTimeout"].empty()) {
      connectTimeout = make_shared<int>(boost::any_cast<int>(m["connectTimeout"]));
    }
    if (m.find("httpProxy") != m.end() && !m["httpProxy"].empty()) {
      httpProxy = make_shared<string>(boost::any_cast<string>(m["httpProxy"]));
    }
    if (m.find("httpsProxy") != m.end() && !m["httpsProxy"].empty()) {
      httpsProxy = make_shared<string>(boost::any_cast<string>(m["httpsProxy"]));
    }
    if (m.find("noProxy") != m.end() && !m["noProxy"].empty()) {
      noProxy = make_shared<string>(boost::any_cast<string>(m["noProxy"]));
    }
    if (m.find("maxIdleConns") != m.end() && !m["maxIdleConns"].empty()) {
      maxIdleConns = make_shared<int>(boost::any_cast<int>(m["maxIdleConns"]));
    }
    if (m.find("localAddr") != m.end() && !m["localAddr"].empty()) {
      localAddr = make_shared<string>(boost::any_cast<string>(m["localAddr"]));
    }
    if (m.find("socks5Proxy") != m.end() && !m["socks5Proxy"].empty()) {
      socks5Proxy = make_shared<string>(boost::any_cast<string>(m["socks5Proxy"]));
    }
    if (m.find("socks5NetWork") != m.end() && !m["socks5NetWork"].empty()) {
      socks5NetWork = make_shared<string>(boost::any_cast<string>(m["socks5NetWork"]));
    }
  }


  ~RuntimeOptions() = default;
};
class Config : public Darabonba::Model {
public:
  shared_ptr<string> endpoint{};
  shared_ptr<string> domainId{};
  shared_ptr<string> clientId{};
  shared_ptr<string> refreshToken{};
  shared_ptr<string> clientSecret{};
  shared_ptr<string> accessToken{};
  shared_ptr<string> expireTime{};
  shared_ptr<string> protocol{};
  shared_ptr<string> type{};
  shared_ptr<string> securityToken{};
  shared_ptr<string> accessKeyId{};
  shared_ptr<string> accessKeySecret{};
  shared_ptr<string> nickname{};
  shared_ptr<string> userAgent{};

  Config() {}

  explicit Config(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    Darabonba::Model::validatePattern("domainId", domainId, "^[a-zA-Z0-9_-]+$");
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
    if (protocol) {
      res["protocol"] = boost::any(*protocol);
    }
    if (type) {
      res["type"] = boost::any(*type);
    }
    if (securityToken) {
      res["securityToken"] = boost::any(*securityToken);
    }
    if (accessKeyId) {
      res["accessKeyId"] = boost::any(*accessKeyId);
    }
    if (accessKeySecret) {
      res["accessKeySecret"] = boost::any(*accessKeySecret);
    }
    if (nickname) {
      res["nickname"] = boost::any(*nickname);
    }
    if (userAgent) {
      res["userAgent"] = boost::any(*userAgent);
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
      refreshToken = make_shared<string>(boost::any_cast<string>(m["refreshToken"]));
    }
    if (m.find("clientSecret") != m.end() && !m["clientSecret"].empty()) {
      clientSecret = make_shared<string>(boost::any_cast<string>(m["clientSecret"]));
    }
    if (m.find("accessToken") != m.end() && !m["accessToken"].empty()) {
      accessToken = make_shared<string>(boost::any_cast<string>(m["accessToken"]));
    }
    if (m.find("expireTime") != m.end() && !m["expireTime"].empty()) {
      expireTime = make_shared<string>(boost::any_cast<string>(m["expireTime"]));
    }
    if (m.find("protocol") != m.end() && !m["protocol"].empty()) {
      protocol = make_shared<string>(boost::any_cast<string>(m["protocol"]));
    }
    if (m.find("type") != m.end() && !m["type"].empty()) {
      type = make_shared<string>(boost::any_cast<string>(m["type"]));
    }
    if (m.find("securityToken") != m.end() && !m["securityToken"].empty()) {
      securityToken = make_shared<string>(boost::any_cast<string>(m["securityToken"]));
    }
    if (m.find("accessKeyId") != m.end() && !m["accessKeyId"].empty()) {
      accessKeyId = make_shared<string>(boost::any_cast<string>(m["accessKeyId"]));
    }
    if (m.find("accessKeySecret") != m.end() && !m["accessKeySecret"].empty()) {
      accessKeySecret = make_shared<string>(boost::any_cast<string>(m["accessKeySecret"]));
    }
    if (m.find("nickname") != m.end() && !m["nickname"].empty()) {
      nickname = make_shared<string>(boost::any_cast<string>(m["nickname"]));
    }
    if (m.find("userAgent") != m.end() && !m["userAgent"].empty()) {
      userAgent = make_shared<string>(boost::any_cast<string>(m["userAgent"]));
    }
  }


  ~Config() = default;
};
class LinkInfo : public Darabonba::Model {
public:
  shared_ptr<string> extra{};
  shared_ptr<string> identity{};
  shared_ptr<string> type{};

  LinkInfo() {}

  explicit LinkInfo(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (extra) {
      res["extra"] = boost::any(*extra);
    }
    if (identity) {
      res["identity"] = boost::any(*identity);
    }
    if (type) {
      res["type"] = boost::any(*type);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("extra") != m.end() && !m["extra"].empty()) {
      extra = make_shared<string>(boost::any_cast<string>(m["extra"]));
    }
    if (m.find("identity") != m.end() && !m["identity"].empty()) {
      identity = make_shared<string>(boost::any_cast<string>(m["identity"]));
    }
    if (m.find("type") != m.end() && !m["type"].empty()) {
      type = make_shared<string>(boost::any_cast<string>(m["type"]));
    }
  }


  ~LinkInfo() = default;
};
class AccountAccessTokenResponse : public Darabonba::Model {
public:
  shared_ptr<string> accessToken{};
  shared_ptr<string> avatar{};
  shared_ptr<bool> dataPinSaved{};
  shared_ptr<bool> dataPinSetup{};
  shared_ptr<string> defaultDriveId{};
  shared_ptr<vector<LinkInfo>> existLink{};
  shared_ptr<string> expireTime{};
  shared_ptr<long> expiresIn{};
  shared_ptr<bool> isFirstLogin{};
  shared_ptr<bool> needLink{};
  shared_ptr<string> nickName{};
  shared_ptr<string> refreshToken{};
  shared_ptr<string> role{};
  shared_ptr<string> state{};
  shared_ptr<string> tokenType{};
  shared_ptr<map<string, boost::any>> userData{};
  shared_ptr<string> userId{};
  shared_ptr<string> userName{};

  AccountAccessTokenResponse() {}

  explicit AccountAccessTokenResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!accessToken) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("accessToken is required.")));
    }
    if (!needLink) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("needLink is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (accessToken) {
      res["access_token"] = boost::any(*accessToken);
    }
    if (avatar) {
      res["avatar"] = boost::any(*avatar);
    }
    if (dataPinSaved) {
      res["data_pin_saved"] = boost::any(*dataPinSaved);
    }
    if (dataPinSetup) {
      res["data_pin_setup"] = boost::any(*dataPinSetup);
    }
    if (defaultDriveId) {
      res["default_drive_id"] = boost::any(*defaultDriveId);
    }
    if (existLink) {
      vector<boost::any> temp1;
      for(auto item1:*existLink){
        temp1.push_back(boost::any(item1.toMap()));
      }
      res["exist_link"] = boost::any(temp1);
    }
    if (expireTime) {
      res["expire_time"] = boost::any(*expireTime);
    }
    if (expiresIn) {
      res["expires_in"] = boost::any(*expiresIn);
    }
    if (isFirstLogin) {
      res["is_first_login"] = boost::any(*isFirstLogin);
    }
    if (needLink) {
      res["need_link"] = boost::any(*needLink);
    }
    if (nickName) {
      res["nick_name"] = boost::any(*nickName);
    }
    if (refreshToken) {
      res["refresh_token"] = boost::any(*refreshToken);
    }
    if (role) {
      res["role"] = boost::any(*role);
    }
    if (state) {
      res["state"] = boost::any(*state);
    }
    if (tokenType) {
      res["token_type"] = boost::any(*tokenType);
    }
    if (userData) {
      res["user_data"] = boost::any(*userData);
    }
    if (userId) {
      res["user_id"] = boost::any(*userId);
    }
    if (userName) {
      res["user_name"] = boost::any(*userName);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("access_token") != m.end() && !m["access_token"].empty()) {
      accessToken = make_shared<string>(boost::any_cast<string>(m["access_token"]));
    }
    if (m.find("avatar") != m.end() && !m["avatar"].empty()) {
      avatar = make_shared<string>(boost::any_cast<string>(m["avatar"]));
    }
    if (m.find("data_pin_saved") != m.end() && !m["data_pin_saved"].empty()) {
      dataPinSaved = make_shared<bool>(boost::any_cast<bool>(m["data_pin_saved"]));
    }
    if (m.find("data_pin_setup") != m.end() && !m["data_pin_setup"].empty()) {
      dataPinSetup = make_shared<bool>(boost::any_cast<bool>(m["data_pin_setup"]));
    }
    if (m.find("default_drive_id") != m.end() && !m["default_drive_id"].empty()) {
      defaultDriveId = make_shared<string>(boost::any_cast<string>(m["default_drive_id"]));
    }
    if (m.find("exist_link") != m.end() && !m["exist_link"].empty()) {
      if (typeid(vector<boost::any>).name() == m["exist_link"].type().name()) {
        vector<LinkInfo> expect1;
        for(auto item1:boost::any_cast<vector<boost::any>>(m["exist_link"])){
          if (typeid(map<string, boost::any>).name() == item1.type().name()) {
            LinkInfo model2;
            model2.fromMap(boost::any_cast<map<string, boost::any>>(item1));
            expect1.push_back(model2);
          }
        }
        existLink = make_shared<vector<LinkInfo>>(expect1);
      }
    }
    if (m.find("expire_time") != m.end() && !m["expire_time"].empty()) {
      expireTime = make_shared<string>(boost::any_cast<string>(m["expire_time"]));
    }
    if (m.find("expires_in") != m.end() && !m["expires_in"].empty()) {
      expiresIn = make_shared<long>(boost::any_cast<long>(m["expires_in"]));
    }
    if (m.find("is_first_login") != m.end() && !m["is_first_login"].empty()) {
      isFirstLogin = make_shared<bool>(boost::any_cast<bool>(m["is_first_login"]));
    }
    if (m.find("need_link") != m.end() && !m["need_link"].empty()) {
      needLink = make_shared<bool>(boost::any_cast<bool>(m["need_link"]));
    }
    if (m.find("nick_name") != m.end() && !m["nick_name"].empty()) {
      nickName = make_shared<string>(boost::any_cast<string>(m["nick_name"]));
    }
    if (m.find("refresh_token") != m.end() && !m["refresh_token"].empty()) {
      refreshToken = make_shared<string>(boost::any_cast<string>(m["refresh_token"]));
    }
    if (m.find("role") != m.end() && !m["role"].empty()) {
      role = make_shared<string>(boost::any_cast<string>(m["role"]));
    }
    if (m.find("state") != m.end() && !m["state"].empty()) {
      state = make_shared<string>(boost::any_cast<string>(m["state"]));
    }
    if (m.find("token_type") != m.end() && !m["token_type"].empty()) {
      tokenType = make_shared<string>(boost::any_cast<string>(m["token_type"]));
    }
    if (m.find("user_data") != m.end() && !m["user_data"].empty()) {
      map<string, boost::any> map1 = boost::any_cast<map<string, boost::any>>(m["user_data"]);
      map<string, boost::any> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      userData = make_shared<map<string, boost::any>>(toMap1);
    }
    if (m.find("user_id") != m.end() && !m["user_id"].empty()) {
      userId = make_shared<string>(boost::any_cast<string>(m["user_id"]));
    }
    if (m.find("user_name") != m.end() && !m["user_name"].empty()) {
      userName = make_shared<string>(boost::any_cast<string>(m["user_name"]));
    }
  }


  ~AccountAccessTokenResponse() = default;
};
class CancelLinkModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<AccountAccessTokenResponse> body{};

  CancelLinkModel() {}

  explicit CancelLinkModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        AccountAccessTokenResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<AccountAccessTokenResponse>(model1);
      }
    }
  }


  ~CancelLinkModel() = default;
};
class ConfirmLinkModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<AccountAccessTokenResponse> body{};

  ConfirmLinkModel() {}

  explicit ConfirmLinkModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        AccountAccessTokenResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<AccountAccessTokenResponse>(model1);
      }
    }
  }


  ~ConfirmLinkModel() = default;
};
class ChangePasswordModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<AccountAccessTokenResponse> body{};

  ChangePasswordModel() {}

  explicit ChangePasswordModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        AccountAccessTokenResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<AccountAccessTokenResponse>(model1);
      }
    }
  }


  ~ChangePasswordModel() = default;
};
class SetPasswordModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};

  SetPasswordModel() {}

  explicit SetPasswordModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
  }


  ~SetPasswordModel() = default;
};
class VerifyCodeResponse : public Darabonba::Model {
public:
  shared_ptr<string> state{};

  VerifyCodeResponse() {}

  explicit VerifyCodeResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!state) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("state is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (state) {
      res["state"] = boost::any(*state);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("state") != m.end() && !m["state"].empty()) {
      state = make_shared<string>(boost::any_cast<string>(m["state"]));
    }
  }


  ~VerifyCodeResponse() = default;
};
class VerifyCodeModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<VerifyCodeResponse> body{};

  VerifyCodeModel() {}

  explicit VerifyCodeModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        VerifyCodeResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<VerifyCodeResponse>(model1);
      }
    }
  }


  ~VerifyCodeModel() = default;
};
class GetAccessTokenByLinkInfoModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<AccountAccessTokenResponse> body{};

  GetAccessTokenByLinkInfoModel() {}

  explicit GetAccessTokenByLinkInfoModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        AccountAccessTokenResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<AccountAccessTokenResponse>(model1);
      }
    }
  }


  ~GetAccessTokenByLinkInfoModel() = default;
};
class Captcha : public Darabonba::Model {
public:
  shared_ptr<string> captcha{};
  shared_ptr<string> captchaFormat{};
  shared_ptr<string> captchaId{};

  Captcha() {}

  explicit Captcha(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!captcha) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("captcha is required.")));
    }
    if (!captchaFormat) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("captchaFormat is required.")));
    }
    if (!captchaId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("captchaId is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (captcha) {
      res["captcha"] = boost::any(*captcha);
    }
    if (captchaFormat) {
      res["captcha_format"] = boost::any(*captchaFormat);
    }
    if (captchaId) {
      res["captcha_id"] = boost::any(*captchaId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("captcha") != m.end() && !m["captcha"].empty()) {
      captcha = make_shared<string>(boost::any_cast<string>(m["captcha"]));
    }
    if (m.find("captcha_format") != m.end() && !m["captcha_format"].empty()) {
      captchaFormat = make_shared<string>(boost::any_cast<string>(m["captcha_format"]));
    }
    if (m.find("captcha_id") != m.end() && !m["captcha_id"].empty()) {
      captchaId = make_shared<string>(boost::any_cast<string>(m["captcha_id"]));
    }
  }


  ~Captcha() = default;
};
class GetCaptchaModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<Captcha> body{};

  GetCaptchaModel() {}

  explicit GetCaptchaModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        Captcha model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<Captcha>(model1);
      }
    }
  }


  ~GetCaptchaModel() = default;
};
class LinkInfoResponse : public Darabonba::Model {
public:
  shared_ptr<string> authenticationType{};
  shared_ptr<long> createdAt{};
  shared_ptr<string> domainId{};
  shared_ptr<string> extra{};
  shared_ptr<string> identity{};
  shared_ptr<long> lastLoginTime{};
  shared_ptr<string> status{};
  shared_ptr<string> userId{};

  LinkInfoResponse() {}

  explicit LinkInfoResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!authenticationType) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("authenticationType is required.")));
    }
    if (!createdAt) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("createdAt is required.")));
    }
    if (!domainId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("domainId is required.")));
    }
    if (!identity) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("identity is required.")));
    }
    if (!lastLoginTime) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("lastLoginTime is required.")));
    }
    if (!status) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("status is required.")));
    }
    if (!userId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("userId is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (authenticationType) {
      res["authentication_type"] = boost::any(*authenticationType);
    }
    if (createdAt) {
      res["created_at"] = boost::any(*createdAt);
    }
    if (domainId) {
      res["domain_id"] = boost::any(*domainId);
    }
    if (extra) {
      res["extra"] = boost::any(*extra);
    }
    if (identity) {
      res["identity"] = boost::any(*identity);
    }
    if (lastLoginTime) {
      res["last_login_time"] = boost::any(*lastLoginTime);
    }
    if (status) {
      res["status"] = boost::any(*status);
    }
    if (userId) {
      res["user_id"] = boost::any(*userId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("authentication_type") != m.end() && !m["authentication_type"].empty()) {
      authenticationType = make_shared<string>(boost::any_cast<string>(m["authentication_type"]));
    }
    if (m.find("created_at") != m.end() && !m["created_at"].empty()) {
      createdAt = make_shared<long>(boost::any_cast<long>(m["created_at"]));
    }
    if (m.find("domain_id") != m.end() && !m["domain_id"].empty()) {
      domainId = make_shared<string>(boost::any_cast<string>(m["domain_id"]));
    }
    if (m.find("extra") != m.end() && !m["extra"].empty()) {
      extra = make_shared<string>(boost::any_cast<string>(m["extra"]));
    }
    if (m.find("identity") != m.end() && !m["identity"].empty()) {
      identity = make_shared<string>(boost::any_cast<string>(m["identity"]));
    }
    if (m.find("last_login_time") != m.end() && !m["last_login_time"].empty()) {
      lastLoginTime = make_shared<long>(boost::any_cast<long>(m["last_login_time"]));
    }
    if (m.find("status") != m.end() && !m["status"].empty()) {
      status = make_shared<string>(boost::any_cast<string>(m["status"]));
    }
    if (m.find("user_id") != m.end() && !m["user_id"].empty()) {
      userId = make_shared<string>(boost::any_cast<string>(m["user_id"]));
    }
  }


  ~LinkInfoResponse() = default;
};
class GetLinkInfoModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<LinkInfoResponse> body{};

  GetLinkInfoModel() {}

  explicit GetLinkInfoModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        LinkInfoResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<LinkInfoResponse>(model1);
      }
    }
  }


  ~GetLinkInfoModel() = default;
};
class LinkInfoListResponse : public Darabonba::Model {
public:
  shared_ptr<vector<LinkInfoResponse>> items{};

  LinkInfoListResponse() {}

  explicit LinkInfoListResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!items) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("items is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (items) {
      vector<boost::any> temp1;
      for(auto item1:*items){
        temp1.push_back(boost::any(item1.toMap()));
      }
      res["items"] = boost::any(temp1);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("items") != m.end() && !m["items"].empty()) {
      if (typeid(vector<boost::any>).name() == m["items"].type().name()) {
        vector<LinkInfoResponse> expect1;
        for(auto item1:boost::any_cast<vector<boost::any>>(m["items"])){
          if (typeid(map<string, boost::any>).name() == item1.type().name()) {
            LinkInfoResponse model2;
            model2.fromMap(boost::any_cast<map<string, boost::any>>(item1));
            expect1.push_back(model2);
          }
        }
        items = make_shared<vector<LinkInfoResponse>>(expect1);
      }
    }
  }


  ~LinkInfoListResponse() = default;
};
class GetLinkInfoByUserIdModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<LinkInfoListResponse> body{};

  GetLinkInfoByUserIdModel() {}

  explicit GetLinkInfoByUserIdModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        LinkInfoListResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<LinkInfoListResponse>(model1);
      }
    }
  }


  ~GetLinkInfoByUserIdModel() = default;
};
class GetAppPublicKeyResponse : public Darabonba::Model {
public:
  shared_ptr<string> appId{};
  shared_ptr<string> publicKey{};

  GetAppPublicKeyResponse() {}

  explicit GetAppPublicKeyResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!appId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("appId is required.")));
    }
    if (!publicKey) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("publicKey is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (appId) {
      res["app_id"] = boost::any(*appId);
    }
    if (publicKey) {
      res["public_key"] = boost::any(*publicKey);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("app_id") != m.end() && !m["app_id"].empty()) {
      appId = make_shared<string>(boost::any_cast<string>(m["app_id"]));
    }
    if (m.find("public_key") != m.end() && !m["public_key"].empty()) {
      publicKey = make_shared<string>(boost::any_cast<string>(m["public_key"]));
    }
  }


  ~GetAppPublicKeyResponse() = default;
};
class GetPublicKeyModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<GetAppPublicKeyResponse> body{};

  GetPublicKeyModel() {}

  explicit GetPublicKeyModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        GetAppPublicKeyResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<GetAppPublicKeyResponse>(model1);
      }
    }
  }


  ~GetPublicKeyModel() = default;
};
class LinkModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<AccountAccessTokenResponse> body{};

  LinkModel() {}

  explicit LinkModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        AccountAccessTokenResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<AccountAccessTokenResponse>(model1);
      }
    }
  }


  ~LinkModel() = default;
};
class MobileCheckExistResponse : public Darabonba::Model {
public:
  shared_ptr<bool> isExist{};
  shared_ptr<string> phoneNumber{};
  shared_ptr<string> phoneRegion{};

  MobileCheckExistResponse() {}

  explicit MobileCheckExistResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!isExist) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("isExist is required.")));
    }
    if (!phoneNumber) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("phoneNumber is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (isExist) {
      res["is_exist"] = boost::any(*isExist);
    }
    if (phoneNumber) {
      res["phone_number"] = boost::any(*phoneNumber);
    }
    if (phoneRegion) {
      res["phone_region"] = boost::any(*phoneRegion);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("is_exist") != m.end() && !m["is_exist"].empty()) {
      isExist = make_shared<bool>(boost::any_cast<bool>(m["is_exist"]));
    }
    if (m.find("phone_number") != m.end() && !m["phone_number"].empty()) {
      phoneNumber = make_shared<string>(boost::any_cast<string>(m["phone_number"]));
    }
    if (m.find("phone_region") != m.end() && !m["phone_region"].empty()) {
      phoneRegion = make_shared<string>(boost::any_cast<string>(m["phone_region"]));
    }
  }


  ~MobileCheckExistResponse() = default;
};
class CheckExistModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<MobileCheckExistResponse> body{};

  CheckExistModel() {}

  explicit CheckExistModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        MobileCheckExistResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<MobileCheckExistResponse>(model1);
      }
    }
  }


  ~CheckExistModel() = default;
};
class LoginModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<AccountAccessTokenResponse> body{};

  LoginModel() {}

  explicit LoginModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        AccountAccessTokenResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<AccountAccessTokenResponse>(model1);
      }
    }
  }


  ~LoginModel() = default;
};
class RegisterModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<AccountAccessTokenResponse> body{};

  RegisterModel() {}

  explicit RegisterModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        AccountAccessTokenResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<AccountAccessTokenResponse>(model1);
      }
    }
  }


  ~RegisterModel() = default;
};
class MobileSendSmsCodeResponse : public Darabonba::Model {
public:
  shared_ptr<string> smsCodeId{};

  MobileSendSmsCodeResponse() {}

  explicit MobileSendSmsCodeResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!smsCodeId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("smsCodeId is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (smsCodeId) {
      res["sms_code_id"] = boost::any(*smsCodeId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("sms_code_id") != m.end() && !m["sms_code_id"].empty()) {
      smsCodeId = make_shared<string>(boost::any_cast<string>(m["sms_code_id"]));
    }
  }


  ~MobileSendSmsCodeResponse() = default;
};
class MobileSendSmsCodeModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<MobileSendSmsCodeResponse> body{};

  MobileSendSmsCodeModel() {}

  explicit MobileSendSmsCodeModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        MobileSendSmsCodeResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<MobileSendSmsCodeResponse>(model1);
      }
    }
  }


  ~MobileSendSmsCodeModel() = default;
};
class AccountRevokeModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};

  AccountRevokeModel() {}

  explicit AccountRevokeModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
  }


  ~AccountRevokeModel() = default;
};
class AccountTokenModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<AccountAccessTokenResponse> body{};

  AccountTokenModel() {}

  explicit AccountTokenModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        AccountAccessTokenResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<AccountAccessTokenResponse>(model1);
      }
    }
  }


  ~AccountTokenModel() = default;
};
class AccessTokenResponse : public Darabonba::Model {
public:
  shared_ptr<string> accessToken{};
  shared_ptr<string> defaultDriveId{};
  shared_ptr<string> expireTime{};
  shared_ptr<long> expiresIn{};
  shared_ptr<string> refreshToken{};
  shared_ptr<string> role{};
  shared_ptr<string> tokenType{};
  shared_ptr<string> userId{};

  AccessTokenResponse() {}

  explicit AccessTokenResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!accessToken) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("accessToken is required.")));
    }
    if (!defaultDriveId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("defaultDriveId is required.")));
    }
    if (!expireTime) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("expireTime is required.")));
    }
    if (!expiresIn) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("expiresIn is required.")));
    }
    if (!refreshToken) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("refreshToken is required.")));
    }
    if (!role) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("role is required.")));
    }
    if (!tokenType) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("tokenType is required.")));
    }
    if (!userId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("userId is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (accessToken) {
      res["access_token"] = boost::any(*accessToken);
    }
    if (defaultDriveId) {
      res["default_drive_id"] = boost::any(*defaultDriveId);
    }
    if (expireTime) {
      res["expire_time"] = boost::any(*expireTime);
    }
    if (expiresIn) {
      res["expires_in"] = boost::any(*expiresIn);
    }
    if (refreshToken) {
      res["refresh_token"] = boost::any(*refreshToken);
    }
    if (role) {
      res["role"] = boost::any(*role);
    }
    if (tokenType) {
      res["token_type"] = boost::any(*tokenType);
    }
    if (userId) {
      res["user_id"] = boost::any(*userId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("access_token") != m.end() && !m["access_token"].empty()) {
      accessToken = make_shared<string>(boost::any_cast<string>(m["access_token"]));
    }
    if (m.find("default_drive_id") != m.end() && !m["default_drive_id"].empty()) {
      defaultDriveId = make_shared<string>(boost::any_cast<string>(m["default_drive_id"]));
    }
    if (m.find("expire_time") != m.end() && !m["expire_time"].empty()) {
      expireTime = make_shared<string>(boost::any_cast<string>(m["expire_time"]));
    }
    if (m.find("expires_in") != m.end() && !m["expires_in"].empty()) {
      expiresIn = make_shared<long>(boost::any_cast<long>(m["expires_in"]));
    }
    if (m.find("refresh_token") != m.end() && !m["refresh_token"].empty()) {
      refreshToken = make_shared<string>(boost::any_cast<string>(m["refresh_token"]));
    }
    if (m.find("role") != m.end() && !m["role"].empty()) {
      role = make_shared<string>(boost::any_cast<string>(m["role"]));
    }
    if (m.find("token_type") != m.end() && !m["token_type"].empty()) {
      tokenType = make_shared<string>(boost::any_cast<string>(m["token_type"]));
    }
    if (m.find("user_id") != m.end() && !m["user_id"].empty()) {
      userId = make_shared<string>(boost::any_cast<string>(m["user_id"]));
    }
  }


  ~AccessTokenResponse() = default;
};
class AccountLinkRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<string> detail{};
  shared_ptr<string> extra{};
  shared_ptr<string> identity{};
  shared_ptr<string> status{};
  shared_ptr<string> type{};
  shared_ptr<string> userId{};

  AccountLinkRequest() {}

  explicit AccountLinkRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!identity) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("identity is required.")));
    }
    if (!type) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("type is required.")));
    }
    if (!userId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("userId is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (detail) {
      res["detail"] = boost::any(*detail);
    }
    if (extra) {
      res["extra"] = boost::any(*extra);
    }
    if (identity) {
      res["identity"] = boost::any(*identity);
    }
    if (status) {
      res["status"] = boost::any(*status);
    }
    if (type) {
      res["type"] = boost::any(*type);
    }
    if (userId) {
      res["user_id"] = boost::any(*userId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("detail") != m.end() && !m["detail"].empty()) {
      detail = make_shared<string>(boost::any_cast<string>(m["detail"]));
    }
    if (m.find("extra") != m.end() && !m["extra"].empty()) {
      extra = make_shared<string>(boost::any_cast<string>(m["extra"]));
    }
    if (m.find("identity") != m.end() && !m["identity"].empty()) {
      identity = make_shared<string>(boost::any_cast<string>(m["identity"]));
    }
    if (m.find("status") != m.end() && !m["status"].empty()) {
      status = make_shared<string>(boost::any_cast<string>(m["status"]));
    }
    if (m.find("type") != m.end() && !m["type"].empty()) {
      type = make_shared<string>(boost::any_cast<string>(m["type"]));
    }
    if (m.find("user_id") != m.end() && !m["user_id"].empty()) {
      userId = make_shared<string>(boost::any_cast<string>(m["user_id"]));
    }
  }


  ~AccountLinkRequest() = default;
};
class AuthorizeRequest : public Darabonba::Model {
public:
  shared_ptr<string> ClientID{};
  shared_ptr<string> LoginType{};
  shared_ptr<string> RedirectUri{};
  shared_ptr<string> ResponseType{};
  shared_ptr<vector<string>> Scope{};
  shared_ptr<string> State{};

  AuthorizeRequest() {}

  explicit AuthorizeRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!ClientID) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("ClientID is required.")));
    }
    if (!RedirectUri) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("RedirectUri is required.")));
    }
    if (!ResponseType) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("ResponseType is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (ClientID) {
      res["ClientID"] = boost::any(*ClientID);
    }
    if (LoginType) {
      res["LoginType"] = boost::any(*LoginType);
    }
    if (RedirectUri) {
      res["RedirectUri"] = boost::any(*RedirectUri);
    }
    if (ResponseType) {
      res["ResponseType"] = boost::any(*ResponseType);
    }
    if (Scope) {
      res["Scope"] = boost::any(*Scope);
    }
    if (State) {
      res["State"] = boost::any(*State);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("ClientID") != m.end() && !m["ClientID"].empty()) {
      ClientID = make_shared<string>(boost::any_cast<string>(m["ClientID"]));
    }
    if (m.find("LoginType") != m.end() && !m["LoginType"].empty()) {
      LoginType = make_shared<string>(boost::any_cast<string>(m["LoginType"]));
    }
    if (m.find("RedirectUri") != m.end() && !m["RedirectUri"].empty()) {
      RedirectUri = make_shared<string>(boost::any_cast<string>(m["RedirectUri"]));
    }
    if (m.find("ResponseType") != m.end() && !m["ResponseType"].empty()) {
      ResponseType = make_shared<string>(boost::any_cast<string>(m["ResponseType"]));
    }
    if (m.find("Scope") != m.end() && !m["Scope"].empty()) {
      vector<string> toVec1;
      if (typeid(vector<boost::any>).name() == m["Scope"].type().name()) {
        vector<boost::any> vec1 = boost::any_cast<vector<boost::any>>(m["Scope"]);
        for (auto item:vec1) {
           toVec1.push_back(boost::any_cast<string>(item));
        }
      }
      Scope = make_shared<vector<string>>(toVec1);
    }
    if (m.find("State") != m.end() && !m["State"].empty()) {
      State = make_shared<string>(boost::any_cast<string>(m["State"]));
    }
  }


  ~AuthorizeRequest() = default;
};
class BaseDriveResponse : public Darabonba::Model {
public:
  shared_ptr<string> creator{};
  shared_ptr<string> description{};
  shared_ptr<string> domainId{};
  shared_ptr<string> driveId{};
  shared_ptr<string> driveName{};
  shared_ptr<string> driveType{};
  shared_ptr<bool> encryptDataAccess{};
  shared_ptr<string> encryptMode{};
  shared_ptr<string> owner{};
  shared_ptr<string> relativePath{};
  shared_ptr<string> status{};
  shared_ptr<string> storeId{};
  shared_ptr<long> totalSize{};
  shared_ptr<long> usedSize{};

  BaseDriveResponse() {}

  explicit BaseDriveResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (creator) {
      res["creator"] = boost::any(*creator);
    }
    if (description) {
      res["description"] = boost::any(*description);
    }
    if (domainId) {
      res["domain_id"] = boost::any(*domainId);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (driveName) {
      res["drive_name"] = boost::any(*driveName);
    }
    if (driveType) {
      res["drive_type"] = boost::any(*driveType);
    }
    if (encryptDataAccess) {
      res["encrypt_data_access"] = boost::any(*encryptDataAccess);
    }
    if (encryptMode) {
      res["encrypt_mode"] = boost::any(*encryptMode);
    }
    if (owner) {
      res["owner"] = boost::any(*owner);
    }
    if (relativePath) {
      res["relative_path"] = boost::any(*relativePath);
    }
    if (status) {
      res["status"] = boost::any(*status);
    }
    if (storeId) {
      res["store_id"] = boost::any(*storeId);
    }
    if (totalSize) {
      res["total_size"] = boost::any(*totalSize);
    }
    if (usedSize) {
      res["used_size"] = boost::any(*usedSize);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("creator") != m.end() && !m["creator"].empty()) {
      creator = make_shared<string>(boost::any_cast<string>(m["creator"]));
    }
    if (m.find("description") != m.end() && !m["description"].empty()) {
      description = make_shared<string>(boost::any_cast<string>(m["description"]));
    }
    if (m.find("domain_id") != m.end() && !m["domain_id"].empty()) {
      domainId = make_shared<string>(boost::any_cast<string>(m["domain_id"]));
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("drive_name") != m.end() && !m["drive_name"].empty()) {
      driveName = make_shared<string>(boost::any_cast<string>(m["drive_name"]));
    }
    if (m.find("drive_type") != m.end() && !m["drive_type"].empty()) {
      driveType = make_shared<string>(boost::any_cast<string>(m["drive_type"]));
    }
    if (m.find("encrypt_data_access") != m.end() && !m["encrypt_data_access"].empty()) {
      encryptDataAccess = make_shared<bool>(boost::any_cast<bool>(m["encrypt_data_access"]));
    }
    if (m.find("encrypt_mode") != m.end() && !m["encrypt_mode"].empty()) {
      encryptMode = make_shared<string>(boost::any_cast<string>(m["encrypt_mode"]));
    }
    if (m.find("owner") != m.end() && !m["owner"].empty()) {
      owner = make_shared<string>(boost::any_cast<string>(m["owner"]));
    }
    if (m.find("relative_path") != m.end() && !m["relative_path"].empty()) {
      relativePath = make_shared<string>(boost::any_cast<string>(m["relative_path"]));
    }
    if (m.find("status") != m.end() && !m["status"].empty()) {
      status = make_shared<string>(boost::any_cast<string>(m["status"]));
    }
    if (m.find("store_id") != m.end() && !m["store_id"].empty()) {
      storeId = make_shared<string>(boost::any_cast<string>(m["store_id"]));
    }
    if (m.find("total_size") != m.end() && !m["total_size"].empty()) {
      totalSize = make_shared<long>(boost::any_cast<long>(m["total_size"]));
    }
    if (m.find("used_size") != m.end() && !m["used_size"].empty()) {
      usedSize = make_shared<long>(boost::any_cast<long>(m["used_size"]));
    }
  }


  ~BaseDriveResponse() = default;
};
class BaseFileAnonymousResponse : public Darabonba::Model {
public:
  shared_ptr<string> fileId{};
  shared_ptr<string> name{};
  shared_ptr<long> size{};
  shared_ptr<string> thumbnail{};
  shared_ptr<string> type{};
  shared_ptr<string> updatedAt{};

  BaseFileAnonymousResponse() {}

  explicit BaseFileAnonymousResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    Darabonba::Model::validateMaxLength("fileId", fileId, 50);
    Darabonba::Model::validateMinLength("fileId", fileId, 40);
    Darabonba::Model::validatePattern("fileId", fileId, "[a-z0-9]{1,50}");
    Darabonba::Model::validatePattern("name", name, "[a-zA-Z0-9.-]{1,1000}");
    if (size && *size > 53687091200) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("size is required.")));
    }
    if (size && *size < 0) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("size is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (fileId) {
      res["file_id"] = boost::any(*fileId);
    }
    if (name) {
      res["name"] = boost::any(*name);
    }
    if (size) {
      res["size"] = boost::any(*size);
    }
    if (thumbnail) {
      res["thumbnail"] = boost::any(*thumbnail);
    }
    if (type) {
      res["type"] = boost::any(*type);
    }
    if (updatedAt) {
      res["updated_at"] = boost::any(*updatedAt);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("file_id") != m.end() && !m["file_id"].empty()) {
      fileId = make_shared<string>(boost::any_cast<string>(m["file_id"]));
    }
    if (m.find("name") != m.end() && !m["name"].empty()) {
      name = make_shared<string>(boost::any_cast<string>(m["name"]));
    }
    if (m.find("size") != m.end() && !m["size"].empty()) {
      size = make_shared<long>(boost::any_cast<long>(m["size"]));
    }
    if (m.find("thumbnail") != m.end() && !m["thumbnail"].empty()) {
      thumbnail = make_shared<string>(boost::any_cast<string>(m["thumbnail"]));
    }
    if (m.find("type") != m.end() && !m["type"].empty()) {
      type = make_shared<string>(boost::any_cast<string>(m["type"]));
    }
    if (m.find("updated_at") != m.end() && !m["updated_at"].empty()) {
      updatedAt = make_shared<string>(boost::any_cast<string>(m["updated_at"]));
    }
  }


  ~BaseFileAnonymousResponse() = default;
};
class CroppingBoundary : public Darabonba::Model {
public:
  shared_ptr<long> height{};
  shared_ptr<long> left{};
  shared_ptr<long> top{};
  shared_ptr<long> width{};

  CroppingBoundary() {}

  explicit CroppingBoundary(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (height) {
      res["height"] = boost::any(*height);
    }
    if (left) {
      res["left"] = boost::any(*left);
    }
    if (top) {
      res["top"] = boost::any(*top);
    }
    if (width) {
      res["width"] = boost::any(*width);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("height") != m.end() && !m["height"].empty()) {
      height = make_shared<long>(boost::any_cast<long>(m["height"]));
    }
    if (m.find("left") != m.end() && !m["left"].empty()) {
      left = make_shared<long>(boost::any_cast<long>(m["left"]));
    }
    if (m.find("top") != m.end() && !m["top"].empty()) {
      top = make_shared<long>(boost::any_cast<long>(m["top"]));
    }
    if (m.find("width") != m.end() && !m["width"].empty()) {
      width = make_shared<long>(boost::any_cast<long>(m["width"]));
    }
  }


  ~CroppingBoundary() = default;
};
class CroppingSuggestionItem : public Darabonba::Model {
public:
  shared_ptr<string> aspectRatio{};
  shared_ptr<CroppingBoundary> croppingBoundary{};
  shared_ptr<double> score{};

  CroppingSuggestionItem() {}

  explicit CroppingSuggestionItem(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (aspectRatio) {
      res["aspect_ratio"] = boost::any(*aspectRatio);
    }
    if (croppingBoundary) {
      res["cropping_boundary"] = croppingBoundary ? boost::any(croppingBoundary->toMap()) : boost::any(map<string,boost::any>({}));
    }
    if (score) {
      res["score"] = boost::any(*score);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("aspect_ratio") != m.end() && !m["aspect_ratio"].empty()) {
      aspectRatio = make_shared<string>(boost::any_cast<string>(m["aspect_ratio"]));
    }
    if (m.find("cropping_boundary") != m.end() && !m["cropping_boundary"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["cropping_boundary"].type().name()) {
        CroppingBoundary model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["cropping_boundary"]));
        croppingBoundary = make_shared<CroppingBoundary>(model1);
      }
    }
    if (m.find("score") != m.end() && !m["score"].empty()) {
      score = make_shared<double>(boost::any_cast<double>(m["score"]));
    }
  }


  ~CroppingSuggestionItem() = default;
};
class ImageQuality : public Darabonba::Model {
public:
  shared_ptr<double> clarity{};
  shared_ptr<double> clarityScore{};
  shared_ptr<double> color{};
  shared_ptr<double> colorScore{};
  shared_ptr<double> compositionScore{};
  shared_ptr<double> contrast{};
  shared_ptr<double> contrastScore{};
  shared_ptr<double> exposure{};
  shared_ptr<double> exposureScore{};
  shared_ptr<double> overallScore{};

  ImageQuality() {}

  explicit ImageQuality(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (clarity) {
      res["clarity"] = boost::any(*clarity);
    }
    if (clarityScore) {
      res["clarity_score"] = boost::any(*clarityScore);
    }
    if (color) {
      res["color"] = boost::any(*color);
    }
    if (colorScore) {
      res["color_score"] = boost::any(*colorScore);
    }
    if (compositionScore) {
      res["composition_score"] = boost::any(*compositionScore);
    }
    if (contrast) {
      res["contrast"] = boost::any(*contrast);
    }
    if (contrastScore) {
      res["contrast_score"] = boost::any(*contrastScore);
    }
    if (exposure) {
      res["exposure"] = boost::any(*exposure);
    }
    if (exposureScore) {
      res["exposure_score"] = boost::any(*exposureScore);
    }
    if (overallScore) {
      res["overall_score"] = boost::any(*overallScore);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("clarity") != m.end() && !m["clarity"].empty()) {
      clarity = make_shared<double>(boost::any_cast<double>(m["clarity"]));
    }
    if (m.find("clarity_score") != m.end() && !m["clarity_score"].empty()) {
      clarityScore = make_shared<double>(boost::any_cast<double>(m["clarity_score"]));
    }
    if (m.find("color") != m.end() && !m["color"].empty()) {
      color = make_shared<double>(boost::any_cast<double>(m["color"]));
    }
    if (m.find("color_score") != m.end() && !m["color_score"].empty()) {
      colorScore = make_shared<double>(boost::any_cast<double>(m["color_score"]));
    }
    if (m.find("composition_score") != m.end() && !m["composition_score"].empty()) {
      compositionScore = make_shared<double>(boost::any_cast<double>(m["composition_score"]));
    }
    if (m.find("contrast") != m.end() && !m["contrast"].empty()) {
      contrast = make_shared<double>(boost::any_cast<double>(m["contrast"]));
    }
    if (m.find("contrast_score") != m.end() && !m["contrast_score"].empty()) {
      contrastScore = make_shared<double>(boost::any_cast<double>(m["contrast_score"]));
    }
    if (m.find("exposure") != m.end() && !m["exposure"].empty()) {
      exposure = make_shared<double>(boost::any_cast<double>(m["exposure"]));
    }
    if (m.find("exposure_score") != m.end() && !m["exposure_score"].empty()) {
      exposureScore = make_shared<double>(boost::any_cast<double>(m["exposure_score"]));
    }
    if (m.find("overall_score") != m.end() && !m["overall_score"].empty()) {
      overallScore = make_shared<double>(boost::any_cast<double>(m["overall_score"]));
    }
  }


  ~ImageQuality() = default;
};
class SystemTag : public Darabonba::Model {
public:
  shared_ptr<double> confidence{};
  shared_ptr<string> enName{};
  shared_ptr<string> name{};
  shared_ptr<string> parentEnName{};
  shared_ptr<string> parentName{};
  shared_ptr<bool> selected{};
  shared_ptr<long> tagLevel{};

  SystemTag() {}

  explicit SystemTag(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (confidence) {
      res["confidence"] = boost::any(*confidence);
    }
    if (enName) {
      res["en_name"] = boost::any(*enName);
    }
    if (name) {
      res["name"] = boost::any(*name);
    }
    if (parentEnName) {
      res["parent_en_name"] = boost::any(*parentEnName);
    }
    if (parentName) {
      res["parent_name"] = boost::any(*parentName);
    }
    if (selected) {
      res["selected"] = boost::any(*selected);
    }
    if (tagLevel) {
      res["tag_level"] = boost::any(*tagLevel);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("confidence") != m.end() && !m["confidence"].empty()) {
      confidence = make_shared<double>(boost::any_cast<double>(m["confidence"]));
    }
    if (m.find("en_name") != m.end() && !m["en_name"].empty()) {
      enName = make_shared<string>(boost::any_cast<string>(m["en_name"]));
    }
    if (m.find("name") != m.end() && !m["name"].empty()) {
      name = make_shared<string>(boost::any_cast<string>(m["name"]));
    }
    if (m.find("parent_en_name") != m.end() && !m["parent_en_name"].empty()) {
      parentEnName = make_shared<string>(boost::any_cast<string>(m["parent_en_name"]));
    }
    if (m.find("parent_name") != m.end() && !m["parent_name"].empty()) {
      parentName = make_shared<string>(boost::any_cast<string>(m["parent_name"]));
    }
    if (m.find("selected") != m.end() && !m["selected"].empty()) {
      selected = make_shared<bool>(boost::any_cast<bool>(m["selected"]));
    }
    if (m.find("tag_level") != m.end() && !m["tag_level"].empty()) {
      tagLevel = make_shared<long>(boost::any_cast<long>(m["tag_level"]));
    }
  }


  ~SystemTag() = default;
};
class ImageMediaResponse : public Darabonba::Model {
public:
  shared_ptr<string> addressLine{};
  shared_ptr<string> city{};
  shared_ptr<string> country{};
  shared_ptr<vector<CroppingSuggestionItem>> croppingSuggestion{};
  shared_ptr<string> district{};
  shared_ptr<string> exif{};
  shared_ptr<string> faces{};
  shared_ptr<long> height{};
  shared_ptr<ImageQuality> imageQuality{};
  shared_ptr<vector<SystemTag>> imageTags{};
  shared_ptr<string> location{};
  shared_ptr<string> province{};
  shared_ptr<double> storyImageScore{};
  shared_ptr<string> time{};
  shared_ptr<string> township{};
  shared_ptr<long> width{};

  ImageMediaResponse() {}

  explicit ImageMediaResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (addressLine) {
      res["address_line"] = boost::any(*addressLine);
    }
    if (city) {
      res["city"] = boost::any(*city);
    }
    if (country) {
      res["country"] = boost::any(*country);
    }
    if (croppingSuggestion) {
      vector<boost::any> temp1;
      for(auto item1:*croppingSuggestion){
        temp1.push_back(boost::any(item1.toMap()));
      }
      res["cropping_suggestion"] = boost::any(temp1);
    }
    if (district) {
      res["district"] = boost::any(*district);
    }
    if (exif) {
      res["exif"] = boost::any(*exif);
    }
    if (faces) {
      res["faces"] = boost::any(*faces);
    }
    if (height) {
      res["height"] = boost::any(*height);
    }
    if (imageQuality) {
      res["image_quality"] = imageQuality ? boost::any(imageQuality->toMap()) : boost::any(map<string,boost::any>({}));
    }
    if (imageTags) {
      vector<boost::any> temp1;
      for(auto item1:*imageTags){
        temp1.push_back(boost::any(item1.toMap()));
      }
      res["image_tags"] = boost::any(temp1);
    }
    if (location) {
      res["location"] = boost::any(*location);
    }
    if (province) {
      res["province"] = boost::any(*province);
    }
    if (storyImageScore) {
      res["story_image_score"] = boost::any(*storyImageScore);
    }
    if (time) {
      res["time"] = boost::any(*time);
    }
    if (township) {
      res["township"] = boost::any(*township);
    }
    if (width) {
      res["width"] = boost::any(*width);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("address_line") != m.end() && !m["address_line"].empty()) {
      addressLine = make_shared<string>(boost::any_cast<string>(m["address_line"]));
    }
    if (m.find("city") != m.end() && !m["city"].empty()) {
      city = make_shared<string>(boost::any_cast<string>(m["city"]));
    }
    if (m.find("country") != m.end() && !m["country"].empty()) {
      country = make_shared<string>(boost::any_cast<string>(m["country"]));
    }
    if (m.find("cropping_suggestion") != m.end() && !m["cropping_suggestion"].empty()) {
      if (typeid(vector<boost::any>).name() == m["cropping_suggestion"].type().name()) {
        vector<CroppingSuggestionItem> expect1;
        for(auto item1:boost::any_cast<vector<boost::any>>(m["cropping_suggestion"])){
          if (typeid(map<string, boost::any>).name() == item1.type().name()) {
            CroppingSuggestionItem model2;
            model2.fromMap(boost::any_cast<map<string, boost::any>>(item1));
            expect1.push_back(model2);
          }
        }
        croppingSuggestion = make_shared<vector<CroppingSuggestionItem>>(expect1);
      }
    }
    if (m.find("district") != m.end() && !m["district"].empty()) {
      district = make_shared<string>(boost::any_cast<string>(m["district"]));
    }
    if (m.find("exif") != m.end() && !m["exif"].empty()) {
      exif = make_shared<string>(boost::any_cast<string>(m["exif"]));
    }
    if (m.find("faces") != m.end() && !m["faces"].empty()) {
      faces = make_shared<string>(boost::any_cast<string>(m["faces"]));
    }
    if (m.find("height") != m.end() && !m["height"].empty()) {
      height = make_shared<long>(boost::any_cast<long>(m["height"]));
    }
    if (m.find("image_quality") != m.end() && !m["image_quality"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["image_quality"].type().name()) {
        ImageQuality model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["image_quality"]));
        imageQuality = make_shared<ImageQuality>(model1);
      }
    }
    if (m.find("image_tags") != m.end() && !m["image_tags"].empty()) {
      if (typeid(vector<boost::any>).name() == m["image_tags"].type().name()) {
        vector<SystemTag> expect1;
        for(auto item1:boost::any_cast<vector<boost::any>>(m["image_tags"])){
          if (typeid(map<string, boost::any>).name() == item1.type().name()) {
            SystemTag model2;
            model2.fromMap(boost::any_cast<map<string, boost::any>>(item1));
            expect1.push_back(model2);
          }
        }
        imageTags = make_shared<vector<SystemTag>>(expect1);
      }
    }
    if (m.find("location") != m.end() && !m["location"].empty()) {
      location = make_shared<string>(boost::any_cast<string>(m["location"]));
    }
    if (m.find("province") != m.end() && !m["province"].empty()) {
      province = make_shared<string>(boost::any_cast<string>(m["province"]));
    }
    if (m.find("story_image_score") != m.end() && !m["story_image_score"].empty()) {
      storyImageScore = make_shared<double>(boost::any_cast<double>(m["story_image_score"]));
    }
    if (m.find("time") != m.end() && !m["time"].empty()) {
      time = make_shared<string>(boost::any_cast<string>(m["time"]));
    }
    if (m.find("township") != m.end() && !m["township"].empty()) {
      township = make_shared<string>(boost::any_cast<string>(m["township"]));
    }
    if (m.find("width") != m.end() && !m["width"].empty()) {
      width = make_shared<long>(boost::any_cast<long>(m["width"]));
    }
  }


  ~ImageMediaResponse() = default;
};
class VideoMediaAudioStream : public Darabonba::Model {
public:
  shared_ptr<string> bitRate{};
  shared_ptr<string> channelLayout{};
  shared_ptr<long> channels{};
  shared_ptr<string> codeName{};
  shared_ptr<string> duration{};
  shared_ptr<string> sampleRate{};

  VideoMediaAudioStream() {}

  explicit VideoMediaAudioStream(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (bitRate) {
      res["bit_rate"] = boost::any(*bitRate);
    }
    if (channelLayout) {
      res["channel_layout"] = boost::any(*channelLayout);
    }
    if (channels) {
      res["channels"] = boost::any(*channels);
    }
    if (codeName) {
      res["code_name"] = boost::any(*codeName);
    }
    if (duration) {
      res["duration"] = boost::any(*duration);
    }
    if (sampleRate) {
      res["sample_rate"] = boost::any(*sampleRate);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("bit_rate") != m.end() && !m["bit_rate"].empty()) {
      bitRate = make_shared<string>(boost::any_cast<string>(m["bit_rate"]));
    }
    if (m.find("channel_layout") != m.end() && !m["channel_layout"].empty()) {
      channelLayout = make_shared<string>(boost::any_cast<string>(m["channel_layout"]));
    }
    if (m.find("channels") != m.end() && !m["channels"].empty()) {
      channels = make_shared<long>(boost::any_cast<long>(m["channels"]));
    }
    if (m.find("code_name") != m.end() && !m["code_name"].empty()) {
      codeName = make_shared<string>(boost::any_cast<string>(m["code_name"]));
    }
    if (m.find("duration") != m.end() && !m["duration"].empty()) {
      duration = make_shared<string>(boost::any_cast<string>(m["duration"]));
    }
    if (m.find("sample_rate") != m.end() && !m["sample_rate"].empty()) {
      sampleRate = make_shared<string>(boost::any_cast<string>(m["sample_rate"]));
    }
  }


  ~VideoMediaAudioStream() = default;
};
class VideoMediaVideoStream : public Darabonba::Model {
public:
  shared_ptr<string> bitrate{};
  shared_ptr<string> clarity{};
  shared_ptr<string> codeName{};
  shared_ptr<string> duration{};
  shared_ptr<string> fps{};

  VideoMediaVideoStream() {}

  explicit VideoMediaVideoStream(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (bitrate) {
      res["bitrate"] = boost::any(*bitrate);
    }
    if (clarity) {
      res["clarity"] = boost::any(*clarity);
    }
    if (codeName) {
      res["code_name"] = boost::any(*codeName);
    }
    if (duration) {
      res["duration"] = boost::any(*duration);
    }
    if (fps) {
      res["fps"] = boost::any(*fps);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("bitrate") != m.end() && !m["bitrate"].empty()) {
      bitrate = make_shared<string>(boost::any_cast<string>(m["bitrate"]));
    }
    if (m.find("clarity") != m.end() && !m["clarity"].empty()) {
      clarity = make_shared<string>(boost::any_cast<string>(m["clarity"]));
    }
    if (m.find("code_name") != m.end() && !m["code_name"].empty()) {
      codeName = make_shared<string>(boost::any_cast<string>(m["code_name"]));
    }
    if (m.find("duration") != m.end() && !m["duration"].empty()) {
      duration = make_shared<string>(boost::any_cast<string>(m["duration"]));
    }
    if (m.find("fps") != m.end() && !m["fps"].empty()) {
      fps = make_shared<string>(boost::any_cast<string>(m["fps"]));
    }
  }


  ~VideoMediaVideoStream() = default;
};
class VideoMediaResponse : public Darabonba::Model {
public:
  shared_ptr<string> addressLine{};
  shared_ptr<string> city{};
  shared_ptr<string> country{};
  shared_ptr<string> district{};
  shared_ptr<string> duration{};
  shared_ptr<long> height{};
  shared_ptr<string> location{};
  shared_ptr<string> province{};
  shared_ptr<string> time{};
  shared_ptr<string> township{};
  shared_ptr<vector<VideoMediaAudioStream>> videoMediaAudioStream{};
  shared_ptr<vector<VideoMediaVideoStream>> videoMediaVideoStream{};
  shared_ptr<long> width{};

  VideoMediaResponse() {}

  explicit VideoMediaResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (addressLine) {
      res["address_line"] = boost::any(*addressLine);
    }
    if (city) {
      res["city"] = boost::any(*city);
    }
    if (country) {
      res["country"] = boost::any(*country);
    }
    if (district) {
      res["district"] = boost::any(*district);
    }
    if (duration) {
      res["duration"] = boost::any(*duration);
    }
    if (height) {
      res["height"] = boost::any(*height);
    }
    if (location) {
      res["location"] = boost::any(*location);
    }
    if (province) {
      res["province"] = boost::any(*province);
    }
    if (time) {
      res["time"] = boost::any(*time);
    }
    if (township) {
      res["township"] = boost::any(*township);
    }
    if (videoMediaAudioStream) {
      vector<boost::any> temp1;
      for(auto item1:*videoMediaAudioStream){
        temp1.push_back(boost::any(item1.toMap()));
      }
      res["video_media_audio_stream"] = boost::any(temp1);
    }
    if (videoMediaVideoStream) {
      vector<boost::any> temp1;
      for(auto item1:*videoMediaVideoStream){
        temp1.push_back(boost::any(item1.toMap()));
      }
      res["video_media_video_stream"] = boost::any(temp1);
    }
    if (width) {
      res["width"] = boost::any(*width);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("address_line") != m.end() && !m["address_line"].empty()) {
      addressLine = make_shared<string>(boost::any_cast<string>(m["address_line"]));
    }
    if (m.find("city") != m.end() && !m["city"].empty()) {
      city = make_shared<string>(boost::any_cast<string>(m["city"]));
    }
    if (m.find("country") != m.end() && !m["country"].empty()) {
      country = make_shared<string>(boost::any_cast<string>(m["country"]));
    }
    if (m.find("district") != m.end() && !m["district"].empty()) {
      district = make_shared<string>(boost::any_cast<string>(m["district"]));
    }
    if (m.find("duration") != m.end() && !m["duration"].empty()) {
      duration = make_shared<string>(boost::any_cast<string>(m["duration"]));
    }
    if (m.find("height") != m.end() && !m["height"].empty()) {
      height = make_shared<long>(boost::any_cast<long>(m["height"]));
    }
    if (m.find("location") != m.end() && !m["location"].empty()) {
      location = make_shared<string>(boost::any_cast<string>(m["location"]));
    }
    if (m.find("province") != m.end() && !m["province"].empty()) {
      province = make_shared<string>(boost::any_cast<string>(m["province"]));
    }
    if (m.find("time") != m.end() && !m["time"].empty()) {
      time = make_shared<string>(boost::any_cast<string>(m["time"]));
    }
    if (m.find("township") != m.end() && !m["township"].empty()) {
      township = make_shared<string>(boost::any_cast<string>(m["township"]));
    }
    if (m.find("video_media_audio_stream") != m.end() && !m["video_media_audio_stream"].empty()) {
      if (typeid(vector<boost::any>).name() == m["video_media_audio_stream"].type().name()) {
        vector<VideoMediaAudioStream> expect1;
        for(auto item1:boost::any_cast<vector<boost::any>>(m["video_media_audio_stream"])){
          if (typeid(map<string, boost::any>).name() == item1.type().name()) {
            VideoMediaAudioStream model2;
            model2.fromMap(boost::any_cast<map<string, boost::any>>(item1));
            expect1.push_back(model2);
          }
        }
        videoMediaAudioStream = make_shared<vector<VideoMediaAudioStream>>(expect1);
      }
    }
    if (m.find("video_media_video_stream") != m.end() && !m["video_media_video_stream"].empty()) {
      if (typeid(vector<boost::any>).name() == m["video_media_video_stream"].type().name()) {
        vector<VideoMediaVideoStream> expect1;
        for(auto item1:boost::any_cast<vector<boost::any>>(m["video_media_video_stream"])){
          if (typeid(map<string, boost::any>).name() == item1.type().name()) {
            VideoMediaVideoStream model2;
            model2.fromMap(boost::any_cast<map<string, boost::any>>(item1));
            expect1.push_back(model2);
          }
        }
        videoMediaVideoStream = make_shared<vector<VideoMediaVideoStream>>(expect1);
      }
    }
    if (m.find("width") != m.end() && !m["width"].empty()) {
      width = make_shared<long>(boost::any_cast<long>(m["width"]));
    }
  }


  ~VideoMediaResponse() = default;
};
class VideoPreviewSprite : public Darabonba::Model {
public:
  shared_ptr<long> col{};
  shared_ptr<long> count{};
  shared_ptr<long> frameCount{};
  shared_ptr<long> frameHeight{};
  shared_ptr<long> frameWidth{};
  shared_ptr<long> row{};
  shared_ptr<string> status{};

  VideoPreviewSprite() {}

  explicit VideoPreviewSprite(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (col) {
      res["col"] = boost::any(*col);
    }
    if (count) {
      res["count"] = boost::any(*count);
    }
    if (frameCount) {
      res["frame_count"] = boost::any(*frameCount);
    }
    if (frameHeight) {
      res["frame_height"] = boost::any(*frameHeight);
    }
    if (frameWidth) {
      res["frame_width"] = boost::any(*frameWidth);
    }
    if (row) {
      res["row"] = boost::any(*row);
    }
    if (status) {
      res["status"] = boost::any(*status);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("col") != m.end() && !m["col"].empty()) {
      col = make_shared<long>(boost::any_cast<long>(m["col"]));
    }
    if (m.find("count") != m.end() && !m["count"].empty()) {
      count = make_shared<long>(boost::any_cast<long>(m["count"]));
    }
    if (m.find("frame_count") != m.end() && !m["frame_count"].empty()) {
      frameCount = make_shared<long>(boost::any_cast<long>(m["frame_count"]));
    }
    if (m.find("frame_height") != m.end() && !m["frame_height"].empty()) {
      frameHeight = make_shared<long>(boost::any_cast<long>(m["frame_height"]));
    }
    if (m.find("frame_width") != m.end() && !m["frame_width"].empty()) {
      frameWidth = make_shared<long>(boost::any_cast<long>(m["frame_width"]));
    }
    if (m.find("row") != m.end() && !m["row"].empty()) {
      row = make_shared<long>(boost::any_cast<long>(m["row"]));
    }
    if (m.find("status") != m.end() && !m["status"].empty()) {
      status = make_shared<string>(boost::any_cast<string>(m["status"]));
    }
  }


  ~VideoPreviewSprite() = default;
};
class VideoPreviewTranscode : public Darabonba::Model {
public:
  shared_ptr<string> status{};
  shared_ptr<string> templateId{};

  VideoPreviewTranscode() {}

  explicit VideoPreviewTranscode(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (status) {
      res["status"] = boost::any(*status);
    }
    if (templateId) {
      res["template_id"] = boost::any(*templateId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("status") != m.end() && !m["status"].empty()) {
      status = make_shared<string>(boost::any_cast<string>(m["status"]));
    }
    if (m.find("template_id") != m.end() && !m["template_id"].empty()) {
      templateId = make_shared<string>(boost::any_cast<string>(m["template_id"]));
    }
  }


  ~VideoPreviewTranscode() = default;
};
class VideoPreviewResponse : public Darabonba::Model {
public:
  shared_ptr<string> audioFormat{};
  shared_ptr<string> bitrate{};
  shared_ptr<string> duration{};
  shared_ptr<string> frameRate{};
  shared_ptr<long> height{};
  shared_ptr<VideoPreviewSprite> spriteInfo{};
  shared_ptr<vector<VideoPreviewTranscode>> templateList{};
  shared_ptr<string> thumbnail{};
  shared_ptr<string> videoFormat{};
  shared_ptr<long> width{};

  VideoPreviewResponse() {}

  explicit VideoPreviewResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (audioFormat) {
      res["audio_format"] = boost::any(*audioFormat);
    }
    if (bitrate) {
      res["bitrate"] = boost::any(*bitrate);
    }
    if (duration) {
      res["duration"] = boost::any(*duration);
    }
    if (frameRate) {
      res["frame_rate"] = boost::any(*frameRate);
    }
    if (height) {
      res["height"] = boost::any(*height);
    }
    if (spriteInfo) {
      res["sprite_info"] = spriteInfo ? boost::any(spriteInfo->toMap()) : boost::any(map<string,boost::any>({}));
    }
    if (templateList) {
      vector<boost::any> temp1;
      for(auto item1:*templateList){
        temp1.push_back(boost::any(item1.toMap()));
      }
      res["template_list"] = boost::any(temp1);
    }
    if (thumbnail) {
      res["thumbnail"] = boost::any(*thumbnail);
    }
    if (videoFormat) {
      res["video_format"] = boost::any(*videoFormat);
    }
    if (width) {
      res["width"] = boost::any(*width);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("audio_format") != m.end() && !m["audio_format"].empty()) {
      audioFormat = make_shared<string>(boost::any_cast<string>(m["audio_format"]));
    }
    if (m.find("bitrate") != m.end() && !m["bitrate"].empty()) {
      bitrate = make_shared<string>(boost::any_cast<string>(m["bitrate"]));
    }
    if (m.find("duration") != m.end() && !m["duration"].empty()) {
      duration = make_shared<string>(boost::any_cast<string>(m["duration"]));
    }
    if (m.find("frame_rate") != m.end() && !m["frame_rate"].empty()) {
      frameRate = make_shared<string>(boost::any_cast<string>(m["frame_rate"]));
    }
    if (m.find("height") != m.end() && !m["height"].empty()) {
      height = make_shared<long>(boost::any_cast<long>(m["height"]));
    }
    if (m.find("sprite_info") != m.end() && !m["sprite_info"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["sprite_info"].type().name()) {
        VideoPreviewSprite model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["sprite_info"]));
        spriteInfo = make_shared<VideoPreviewSprite>(model1);
      }
    }
    if (m.find("template_list") != m.end() && !m["template_list"].empty()) {
      if (typeid(vector<boost::any>).name() == m["template_list"].type().name()) {
        vector<VideoPreviewTranscode> expect1;
        for(auto item1:boost::any_cast<vector<boost::any>>(m["template_list"])){
          if (typeid(map<string, boost::any>).name() == item1.type().name()) {
            VideoPreviewTranscode model2;
            model2.fromMap(boost::any_cast<map<string, boost::any>>(item1));
            expect1.push_back(model2);
          }
        }
        templateList = make_shared<vector<VideoPreviewTranscode>>(expect1);
      }
    }
    if (m.find("thumbnail") != m.end() && !m["thumbnail"].empty()) {
      thumbnail = make_shared<string>(boost::any_cast<string>(m["thumbnail"]));
    }
    if (m.find("video_format") != m.end() && !m["video_format"].empty()) {
      videoFormat = make_shared<string>(boost::any_cast<string>(m["video_format"]));
    }
    if (m.find("width") != m.end() && !m["width"].empty()) {
      width = make_shared<long>(boost::any_cast<long>(m["width"]));
    }
  }


  ~VideoPreviewResponse() = default;
};
class BaseFileResponse : public Darabonba::Model {
public:
  shared_ptr<string> category{};
  shared_ptr<string> contentHash{};
  shared_ptr<string> contentHashName{};
  shared_ptr<string> contentType{};
  shared_ptr<string> crc64Hash{};
  shared_ptr<string> createdAt{};
  shared_ptr<string> description{};
  shared_ptr<string> domainId{};
  shared_ptr<string> downloadUrl{};
  shared_ptr<string> driveId{};
  shared_ptr<string> encryptMode{};
  shared_ptr<string> fileExtension{};
  shared_ptr<string> fileId{};
  shared_ptr<bool> hidden{};
  shared_ptr<ImageMediaResponse> imageMediaMetadata{};
  shared_ptr<vector<string>> labels{};
  shared_ptr<string> meta{};
  shared_ptr<string> name{};
  shared_ptr<string> parentFileId{};
  shared_ptr<int> punishFlag{};
  shared_ptr<long> size{};
  shared_ptr<bool> starred{};
  shared_ptr<string> status{};
  shared_ptr<map<string, boost::any>> streamsInfo{};
  shared_ptr<string> thumbnail{};
  shared_ptr<string> trashedAt{};
  shared_ptr<string> type{};
  shared_ptr<string> updatedAt{};
  shared_ptr<string> uploadId{};
  shared_ptr<string> url{};
  shared_ptr<string> userMeta{};
  shared_ptr<VideoMediaResponse> videoMediaMetadata{};
  shared_ptr<VideoPreviewResponse> videoPreviewMetadata{};

  BaseFileResponse() {}

  explicit BaseFileResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    Darabonba::Model::validatePattern("domainId", domainId, "[a-z0-9A-Z]+");
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    Darabonba::Model::validateMaxLength("fileId", fileId, 50);
    Darabonba::Model::validateMinLength("fileId", fileId, 40);
    Darabonba::Model::validatePattern("fileId", fileId, "[a-z0-9]{1,50}");
    if (!name) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("name is required.")));
    }
    Darabonba::Model::validatePattern("name", name, "[a-zA-Z0-9.-]{1,1000}");
    Darabonba::Model::validateMaxLength("parentFileId", parentFileId, 50);
    Darabonba::Model::validateMinLength("parentFileId", parentFileId, 40);
    Darabonba::Model::validatePattern("parentFileId", parentFileId, "[a-z0-9]{1,50}");
    if (size && *size > 53687091200) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("size is required.")));
    }
    if (size && *size < 0) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("size is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (category) {
      res["category"] = boost::any(*category);
    }
    if (contentHash) {
      res["content_hash"] = boost::any(*contentHash);
    }
    if (contentHashName) {
      res["content_hash_name"] = boost::any(*contentHashName);
    }
    if (contentType) {
      res["content_type"] = boost::any(*contentType);
    }
    if (crc64Hash) {
      res["crc64_hash"] = boost::any(*crc64Hash);
    }
    if (createdAt) {
      res["created_at"] = boost::any(*createdAt);
    }
    if (description) {
      res["description"] = boost::any(*description);
    }
    if (domainId) {
      res["domain_id"] = boost::any(*domainId);
    }
    if (downloadUrl) {
      res["download_url"] = boost::any(*downloadUrl);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (encryptMode) {
      res["encrypt_mode"] = boost::any(*encryptMode);
    }
    if (fileExtension) {
      res["file_extension"] = boost::any(*fileExtension);
    }
    if (fileId) {
      res["file_id"] = boost::any(*fileId);
    }
    if (hidden) {
      res["hidden"] = boost::any(*hidden);
    }
    if (imageMediaMetadata) {
      res["image_media_metadata"] = imageMediaMetadata ? boost::any(imageMediaMetadata->toMap()) : boost::any(map<string,boost::any>({}));
    }
    if (labels) {
      res["labels"] = boost::any(*labels);
    }
    if (meta) {
      res["meta"] = boost::any(*meta);
    }
    if (name) {
      res["name"] = boost::any(*name);
    }
    if (parentFileId) {
      res["parent_file_id"] = boost::any(*parentFileId);
    }
    if (punishFlag) {
      res["punish_flag"] = boost::any(*punishFlag);
    }
    if (size) {
      res["size"] = boost::any(*size);
    }
    if (starred) {
      res["starred"] = boost::any(*starred);
    }
    if (status) {
      res["status"] = boost::any(*status);
    }
    if (streamsInfo) {
      res["streams_info"] = boost::any(*streamsInfo);
    }
    if (thumbnail) {
      res["thumbnail"] = boost::any(*thumbnail);
    }
    if (trashedAt) {
      res["trashed_at"] = boost::any(*trashedAt);
    }
    if (type) {
      res["type"] = boost::any(*type);
    }
    if (updatedAt) {
      res["updated_at"] = boost::any(*updatedAt);
    }
    if (uploadId) {
      res["upload_id"] = boost::any(*uploadId);
    }
    if (url) {
      res["url"] = boost::any(*url);
    }
    if (userMeta) {
      res["user_meta"] = boost::any(*userMeta);
    }
    if (videoMediaMetadata) {
      res["video_media_metadata"] = videoMediaMetadata ? boost::any(videoMediaMetadata->toMap()) : boost::any(map<string,boost::any>({}));
    }
    if (videoPreviewMetadata) {
      res["video_preview_metadata"] = videoPreviewMetadata ? boost::any(videoPreviewMetadata->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("category") != m.end() && !m["category"].empty()) {
      category = make_shared<string>(boost::any_cast<string>(m["category"]));
    }
    if (m.find("content_hash") != m.end() && !m["content_hash"].empty()) {
      contentHash = make_shared<string>(boost::any_cast<string>(m["content_hash"]));
    }
    if (m.find("content_hash_name") != m.end() && !m["content_hash_name"].empty()) {
      contentHashName = make_shared<string>(boost::any_cast<string>(m["content_hash_name"]));
    }
    if (m.find("content_type") != m.end() && !m["content_type"].empty()) {
      contentType = make_shared<string>(boost::any_cast<string>(m["content_type"]));
    }
    if (m.find("crc64_hash") != m.end() && !m["crc64_hash"].empty()) {
      crc64Hash = make_shared<string>(boost::any_cast<string>(m["crc64_hash"]));
    }
    if (m.find("created_at") != m.end() && !m["created_at"].empty()) {
      createdAt = make_shared<string>(boost::any_cast<string>(m["created_at"]));
    }
    if (m.find("description") != m.end() && !m["description"].empty()) {
      description = make_shared<string>(boost::any_cast<string>(m["description"]));
    }
    if (m.find("domain_id") != m.end() && !m["domain_id"].empty()) {
      domainId = make_shared<string>(boost::any_cast<string>(m["domain_id"]));
    }
    if (m.find("download_url") != m.end() && !m["download_url"].empty()) {
      downloadUrl = make_shared<string>(boost::any_cast<string>(m["download_url"]));
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("encrypt_mode") != m.end() && !m["encrypt_mode"].empty()) {
      encryptMode = make_shared<string>(boost::any_cast<string>(m["encrypt_mode"]));
    }
    if (m.find("file_extension") != m.end() && !m["file_extension"].empty()) {
      fileExtension = make_shared<string>(boost::any_cast<string>(m["file_extension"]));
    }
    if (m.find("file_id") != m.end() && !m["file_id"].empty()) {
      fileId = make_shared<string>(boost::any_cast<string>(m["file_id"]));
    }
    if (m.find("hidden") != m.end() && !m["hidden"].empty()) {
      hidden = make_shared<bool>(boost::any_cast<bool>(m["hidden"]));
    }
    if (m.find("image_media_metadata") != m.end() && !m["image_media_metadata"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["image_media_metadata"].type().name()) {
        ImageMediaResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["image_media_metadata"]));
        imageMediaMetadata = make_shared<ImageMediaResponse>(model1);
      }
    }
    if (m.find("labels") != m.end() && !m["labels"].empty()) {
      vector<string> toVec1;
      if (typeid(vector<boost::any>).name() == m["labels"].type().name()) {
        vector<boost::any> vec1 = boost::any_cast<vector<boost::any>>(m["labels"]);
        for (auto item:vec1) {
           toVec1.push_back(boost::any_cast<string>(item));
        }
      }
      labels = make_shared<vector<string>>(toVec1);
    }
    if (m.find("meta") != m.end() && !m["meta"].empty()) {
      meta = make_shared<string>(boost::any_cast<string>(m["meta"]));
    }
    if (m.find("name") != m.end() && !m["name"].empty()) {
      name = make_shared<string>(boost::any_cast<string>(m["name"]));
    }
    if (m.find("parent_file_id") != m.end() && !m["parent_file_id"].empty()) {
      parentFileId = make_shared<string>(boost::any_cast<string>(m["parent_file_id"]));
    }
    if (m.find("punish_flag") != m.end() && !m["punish_flag"].empty()) {
      punishFlag = make_shared<int>(boost::any_cast<int>(m["punish_flag"]));
    }
    if (m.find("size") != m.end() && !m["size"].empty()) {
      size = make_shared<long>(boost::any_cast<long>(m["size"]));
    }
    if (m.find("starred") != m.end() && !m["starred"].empty()) {
      starred = make_shared<bool>(boost::any_cast<bool>(m["starred"]));
    }
    if (m.find("status") != m.end() && !m["status"].empty()) {
      status = make_shared<string>(boost::any_cast<string>(m["status"]));
    }
    if (m.find("streams_info") != m.end() && !m["streams_info"].empty()) {
      map<string, boost::any> map1 = boost::any_cast<map<string, boost::any>>(m["streams_info"]);
      map<string, boost::any> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      streamsInfo = make_shared<map<string, boost::any>>(toMap1);
    }
    if (m.find("thumbnail") != m.end() && !m["thumbnail"].empty()) {
      thumbnail = make_shared<string>(boost::any_cast<string>(m["thumbnail"]));
    }
    if (m.find("trashed_at") != m.end() && !m["trashed_at"].empty()) {
      trashedAt = make_shared<string>(boost::any_cast<string>(m["trashed_at"]));
    }
    if (m.find("type") != m.end() && !m["type"].empty()) {
      type = make_shared<string>(boost::any_cast<string>(m["type"]));
    }
    if (m.find("updated_at") != m.end() && !m["updated_at"].empty()) {
      updatedAt = make_shared<string>(boost::any_cast<string>(m["updated_at"]));
    }
    if (m.find("upload_id") != m.end() && !m["upload_id"].empty()) {
      uploadId = make_shared<string>(boost::any_cast<string>(m["upload_id"]));
    }
    if (m.find("url") != m.end() && !m["url"].empty()) {
      url = make_shared<string>(boost::any_cast<string>(m["url"]));
    }
    if (m.find("user_meta") != m.end() && !m["user_meta"].empty()) {
      userMeta = make_shared<string>(boost::any_cast<string>(m["user_meta"]));
    }
    if (m.find("video_media_metadata") != m.end() && !m["video_media_metadata"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["video_media_metadata"].type().name()) {
        VideoMediaResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["video_media_metadata"]));
        videoMediaMetadata = make_shared<VideoMediaResponse>(model1);
      }
    }
    if (m.find("video_preview_metadata") != m.end() && !m["video_preview_metadata"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["video_preview_metadata"].type().name()) {
        VideoPreviewResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["video_preview_metadata"]));
        videoPreviewMetadata = make_shared<VideoPreviewResponse>(model1);
      }
    }
  }


  ~BaseFileResponse() = default;
};
class BaseMediaResponse : public Darabonba::Model {
public:
  shared_ptr<string> addressLine{};
  shared_ptr<string> city{};
  shared_ptr<string> country{};
  shared_ptr<string> district{};
  shared_ptr<long> height{};
  shared_ptr<string> location{};
  shared_ptr<string> province{};
  shared_ptr<string> time{};
  shared_ptr<string> township{};
  shared_ptr<long> width{};

  BaseMediaResponse() {}

  explicit BaseMediaResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (addressLine) {
      res["address_line"] = boost::any(*addressLine);
    }
    if (city) {
      res["city"] = boost::any(*city);
    }
    if (country) {
      res["country"] = boost::any(*country);
    }
    if (district) {
      res["district"] = boost::any(*district);
    }
    if (height) {
      res["height"] = boost::any(*height);
    }
    if (location) {
      res["location"] = boost::any(*location);
    }
    if (province) {
      res["province"] = boost::any(*province);
    }
    if (time) {
      res["time"] = boost::any(*time);
    }
    if (township) {
      res["township"] = boost::any(*township);
    }
    if (width) {
      res["width"] = boost::any(*width);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("address_line") != m.end() && !m["address_line"].empty()) {
      addressLine = make_shared<string>(boost::any_cast<string>(m["address_line"]));
    }
    if (m.find("city") != m.end() && !m["city"].empty()) {
      city = make_shared<string>(boost::any_cast<string>(m["city"]));
    }
    if (m.find("country") != m.end() && !m["country"].empty()) {
      country = make_shared<string>(boost::any_cast<string>(m["country"]));
    }
    if (m.find("district") != m.end() && !m["district"].empty()) {
      district = make_shared<string>(boost::any_cast<string>(m["district"]));
    }
    if (m.find("height") != m.end() && !m["height"].empty()) {
      height = make_shared<long>(boost::any_cast<long>(m["height"]));
    }
    if (m.find("location") != m.end() && !m["location"].empty()) {
      location = make_shared<string>(boost::any_cast<string>(m["location"]));
    }
    if (m.find("province") != m.end() && !m["province"].empty()) {
      province = make_shared<string>(boost::any_cast<string>(m["province"]));
    }
    if (m.find("time") != m.end() && !m["time"].empty()) {
      time = make_shared<string>(boost::any_cast<string>(m["time"]));
    }
    if (m.find("township") != m.end() && !m["township"].empty()) {
      township = make_shared<string>(boost::any_cast<string>(m["township"]));
    }
    if (m.find("width") != m.end() && !m["width"].empty()) {
      width = make_shared<long>(boost::any_cast<long>(m["width"]));
    }
  }


  ~BaseMediaResponse() = default;
};
class BaseOSSFileResponse : public Darabonba::Model {
public:
  shared_ptr<string> contentHash{};
  shared_ptr<string> contentHashName{};
  shared_ptr<string> contentType{};
  shared_ptr<string> crc64Hash{};
  shared_ptr<string> createdAt{};
  shared_ptr<string> description{};
  shared_ptr<string> domainId{};
  shared_ptr<string> downloadUrl{};
  shared_ptr<string> driveId{};
  shared_ptr<string> fileExtension{};
  shared_ptr<string> filePath{};
  shared_ptr<string> name{};
  shared_ptr<string> parentFilePath{};
  shared_ptr<string> shareId{};
  shared_ptr<long> size{};
  shared_ptr<string> status{};
  shared_ptr<string> thumbnail{};
  shared_ptr<string> trashedAt{};
  shared_ptr<string> type{};
  shared_ptr<string> updatedAt{};
  shared_ptr<string> uploadId{};
  shared_ptr<string> url{};

  BaseOSSFileResponse() {}

  explicit BaseOSSFileResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    Darabonba::Model::validatePattern("domainId", domainId, "[a-z0-9A-Z]+");
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    if (!name) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("name is required.")));
    }
    Darabonba::Model::validatePattern("name", name, "[a-zA-Z0-9.-]{1,1000}");
    Darabonba::Model::validateMaxLength("parentFilePath", parentFilePath, 50);
    Darabonba::Model::validateMinLength("parentFilePath", parentFilePath, 40);
    Darabonba::Model::validatePattern("parentFilePath", parentFilePath, "[a-z0-9]{1,50}");
    Darabonba::Model::validatePattern("shareId", shareId, "[0-9]+");
    if (size && *size > 53687091200) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("size is required.")));
    }
    if (size && *size < 0) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("size is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (contentHash) {
      res["content_hash"] = boost::any(*contentHash);
    }
    if (contentHashName) {
      res["content_hash_name"] = boost::any(*contentHashName);
    }
    if (contentType) {
      res["content_type"] = boost::any(*contentType);
    }
    if (crc64Hash) {
      res["crc64_hash"] = boost::any(*crc64Hash);
    }
    if (createdAt) {
      res["created_at"] = boost::any(*createdAt);
    }
    if (description) {
      res["description"] = boost::any(*description);
    }
    if (domainId) {
      res["domain_id"] = boost::any(*domainId);
    }
    if (downloadUrl) {
      res["download_url"] = boost::any(*downloadUrl);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (fileExtension) {
      res["file_extension"] = boost::any(*fileExtension);
    }
    if (filePath) {
      res["file_path"] = boost::any(*filePath);
    }
    if (name) {
      res["name"] = boost::any(*name);
    }
    if (parentFilePath) {
      res["parent_file_path"] = boost::any(*parentFilePath);
    }
    if (shareId) {
      res["share_id"] = boost::any(*shareId);
    }
    if (size) {
      res["size"] = boost::any(*size);
    }
    if (status) {
      res["status"] = boost::any(*status);
    }
    if (thumbnail) {
      res["thumbnail"] = boost::any(*thumbnail);
    }
    if (trashedAt) {
      res["trashed_at"] = boost::any(*trashedAt);
    }
    if (type) {
      res["type"] = boost::any(*type);
    }
    if (updatedAt) {
      res["updated_at"] = boost::any(*updatedAt);
    }
    if (uploadId) {
      res["upload_id"] = boost::any(*uploadId);
    }
    if (url) {
      res["url"] = boost::any(*url);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("content_hash") != m.end() && !m["content_hash"].empty()) {
      contentHash = make_shared<string>(boost::any_cast<string>(m["content_hash"]));
    }
    if (m.find("content_hash_name") != m.end() && !m["content_hash_name"].empty()) {
      contentHashName = make_shared<string>(boost::any_cast<string>(m["content_hash_name"]));
    }
    if (m.find("content_type") != m.end() && !m["content_type"].empty()) {
      contentType = make_shared<string>(boost::any_cast<string>(m["content_type"]));
    }
    if (m.find("crc64_hash") != m.end() && !m["crc64_hash"].empty()) {
      crc64Hash = make_shared<string>(boost::any_cast<string>(m["crc64_hash"]));
    }
    if (m.find("created_at") != m.end() && !m["created_at"].empty()) {
      createdAt = make_shared<string>(boost::any_cast<string>(m["created_at"]));
    }
    if (m.find("description") != m.end() && !m["description"].empty()) {
      description = make_shared<string>(boost::any_cast<string>(m["description"]));
    }
    if (m.find("domain_id") != m.end() && !m["domain_id"].empty()) {
      domainId = make_shared<string>(boost::any_cast<string>(m["domain_id"]));
    }
    if (m.find("download_url") != m.end() && !m["download_url"].empty()) {
      downloadUrl = make_shared<string>(boost::any_cast<string>(m["download_url"]));
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("file_extension") != m.end() && !m["file_extension"].empty()) {
      fileExtension = make_shared<string>(boost::any_cast<string>(m["file_extension"]));
    }
    if (m.find("file_path") != m.end() && !m["file_path"].empty()) {
      filePath = make_shared<string>(boost::any_cast<string>(m["file_path"]));
    }
    if (m.find("name") != m.end() && !m["name"].empty()) {
      name = make_shared<string>(boost::any_cast<string>(m["name"]));
    }
    if (m.find("parent_file_path") != m.end() && !m["parent_file_path"].empty()) {
      parentFilePath = make_shared<string>(boost::any_cast<string>(m["parent_file_path"]));
    }
    if (m.find("share_id") != m.end() && !m["share_id"].empty()) {
      shareId = make_shared<string>(boost::any_cast<string>(m["share_id"]));
    }
    if (m.find("size") != m.end() && !m["size"].empty()) {
      size = make_shared<long>(boost::any_cast<long>(m["size"]));
    }
    if (m.find("status") != m.end() && !m["status"].empty()) {
      status = make_shared<string>(boost::any_cast<string>(m["status"]));
    }
    if (m.find("thumbnail") != m.end() && !m["thumbnail"].empty()) {
      thumbnail = make_shared<string>(boost::any_cast<string>(m["thumbnail"]));
    }
    if (m.find("trashed_at") != m.end() && !m["trashed_at"].empty()) {
      trashedAt = make_shared<string>(boost::any_cast<string>(m["trashed_at"]));
    }
    if (m.find("type") != m.end() && !m["type"].empty()) {
      type = make_shared<string>(boost::any_cast<string>(m["type"]));
    }
    if (m.find("updated_at") != m.end() && !m["updated_at"].empty()) {
      updatedAt = make_shared<string>(boost::any_cast<string>(m["updated_at"]));
    }
    if (m.find("upload_id") != m.end() && !m["upload_id"].empty()) {
      uploadId = make_shared<string>(boost::any_cast<string>(m["upload_id"]));
    }
    if (m.find("url") != m.end() && !m["url"].empty()) {
      url = make_shared<string>(boost::any_cast<string>(m["url"]));
    }
  }


  ~BaseOSSFileResponse() = default;
};
class BaseShareLinkResponse : public Darabonba::Model {
public:
  shared_ptr<string> createdAt{};
  shared_ptr<long> downloadCount{};
  shared_ptr<string> driveId{};
  shared_ptr<string> expiration{};
  shared_ptr<bool> expired{};
  shared_ptr<string> fileId{};
  shared_ptr<long> previewCount{};
  shared_ptr<long> saveCount{};
  shared_ptr<string> shareId{};
  shared_ptr<string> shareMsg{};
  shared_ptr<string> sharePolicy{};
  shared_ptr<string> sharePwd{};
  shared_ptr<string> shareUrl{};
  shared_ptr<string> updatedAt{};

  BaseShareLinkResponse() {}

  explicit BaseShareLinkResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (createdAt) {
      res["created_at"] = boost::any(*createdAt);
    }
    if (downloadCount) {
      res["download_count"] = boost::any(*downloadCount);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (expiration) {
      res["expiration"] = boost::any(*expiration);
    }
    if (expired) {
      res["expired"] = boost::any(*expired);
    }
    if (fileId) {
      res["file_id"] = boost::any(*fileId);
    }
    if (previewCount) {
      res["preview_count"] = boost::any(*previewCount);
    }
    if (saveCount) {
      res["save_count"] = boost::any(*saveCount);
    }
    if (shareId) {
      res["share_id"] = boost::any(*shareId);
    }
    if (shareMsg) {
      res["share_msg"] = boost::any(*shareMsg);
    }
    if (sharePolicy) {
      res["share_policy"] = boost::any(*sharePolicy);
    }
    if (sharePwd) {
      res["share_pwd"] = boost::any(*sharePwd);
    }
    if (shareUrl) {
      res["share_url"] = boost::any(*shareUrl);
    }
    if (updatedAt) {
      res["updated_at"] = boost::any(*updatedAt);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("created_at") != m.end() && !m["created_at"].empty()) {
      createdAt = make_shared<string>(boost::any_cast<string>(m["created_at"]));
    }
    if (m.find("download_count") != m.end() && !m["download_count"].empty()) {
      downloadCount = make_shared<long>(boost::any_cast<long>(m["download_count"]));
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("expiration") != m.end() && !m["expiration"].empty()) {
      expiration = make_shared<string>(boost::any_cast<string>(m["expiration"]));
    }
    if (m.find("expired") != m.end() && !m["expired"].empty()) {
      expired = make_shared<bool>(boost::any_cast<bool>(m["expired"]));
    }
    if (m.find("file_id") != m.end() && !m["file_id"].empty()) {
      fileId = make_shared<string>(boost::any_cast<string>(m["file_id"]));
    }
    if (m.find("preview_count") != m.end() && !m["preview_count"].empty()) {
      previewCount = make_shared<long>(boost::any_cast<long>(m["preview_count"]));
    }
    if (m.find("save_count") != m.end() && !m["save_count"].empty()) {
      saveCount = make_shared<long>(boost::any_cast<long>(m["save_count"]));
    }
    if (m.find("share_id") != m.end() && !m["share_id"].empty()) {
      shareId = make_shared<string>(boost::any_cast<string>(m["share_id"]));
    }
    if (m.find("share_msg") != m.end() && !m["share_msg"].empty()) {
      shareMsg = make_shared<string>(boost::any_cast<string>(m["share_msg"]));
    }
    if (m.find("share_policy") != m.end() && !m["share_policy"].empty()) {
      sharePolicy = make_shared<string>(boost::any_cast<string>(m["share_policy"]));
    }
    if (m.find("share_pwd") != m.end() && !m["share_pwd"].empty()) {
      sharePwd = make_shared<string>(boost::any_cast<string>(m["share_pwd"]));
    }
    if (m.find("share_url") != m.end() && !m["share_url"].empty()) {
      shareUrl = make_shared<string>(boost::any_cast<string>(m["share_url"]));
    }
    if (m.find("updated_at") != m.end() && !m["updated_at"].empty()) {
      updatedAt = make_shared<string>(boost::any_cast<string>(m["updated_at"]));
    }
  }


  ~BaseShareLinkResponse() = default;
};
class SharePermissionPolicy : public Darabonba::Model {
public:
  shared_ptr<string> filePath{};
  shared_ptr<bool> permissionInheritable{};
  shared_ptr<vector<string>> permissionList{};
  shared_ptr<string> permissionType{};

  SharePermissionPolicy() {}

  explicit SharePermissionPolicy(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (filePath) {
      res["file_path"] = boost::any(*filePath);
    }
    if (permissionInheritable) {
      res["permission_inheritable"] = boost::any(*permissionInheritable);
    }
    if (permissionList) {
      res["permission_list"] = boost::any(*permissionList);
    }
    if (permissionType) {
      res["permission_type"] = boost::any(*permissionType);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("file_path") != m.end() && !m["file_path"].empty()) {
      filePath = make_shared<string>(boost::any_cast<string>(m["file_path"]));
    }
    if (m.find("permission_inheritable") != m.end() && !m["permission_inheritable"].empty()) {
      permissionInheritable = make_shared<bool>(boost::any_cast<bool>(m["permission_inheritable"]));
    }
    if (m.find("permission_list") != m.end() && !m["permission_list"].empty()) {
      vector<string> toVec1;
      if (typeid(vector<boost::any>).name() == m["permission_list"].type().name()) {
        vector<boost::any> vec1 = boost::any_cast<vector<boost::any>>(m["permission_list"]);
        for (auto item:vec1) {
           toVec1.push_back(boost::any_cast<string>(item));
        }
      }
      permissionList = make_shared<vector<string>>(toVec1);
    }
    if (m.find("permission_type") != m.end() && !m["permission_type"].empty()) {
      permissionType = make_shared<string>(boost::any_cast<string>(m["permission_type"]));
    }
  }


  ~SharePermissionPolicy() = default;
};
class BaseShareResponse : public Darabonba::Model {
public:
  shared_ptr<string> createdAt{};
  shared_ptr<string> creator{};
  shared_ptr<string> description{};
  shared_ptr<string> domainId{};
  shared_ptr<string> driveId{};
  shared_ptr<string> expiration{};
  shared_ptr<bool> expired{};
  shared_ptr<string> owner{};
  shared_ptr<vector<string>> permissions{};
  shared_ptr<string> shareFilePath{};
  shared_ptr<string> shareId{};
  shared_ptr<string> shareName{};
  shared_ptr<vector<SharePermissionPolicy>> sharePolicy{};
  shared_ptr<string> status{};
  shared_ptr<string> updatedAt{};

  BaseShareResponse() {}

  explicit BaseShareResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (createdAt) {
      res["created_at"] = boost::any(*createdAt);
    }
    if (creator) {
      res["creator"] = boost::any(*creator);
    }
    if (description) {
      res["description"] = boost::any(*description);
    }
    if (domainId) {
      res["domain_id"] = boost::any(*domainId);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (expiration) {
      res["expiration"] = boost::any(*expiration);
    }
    if (expired) {
      res["expired"] = boost::any(*expired);
    }
    if (owner) {
      res["owner"] = boost::any(*owner);
    }
    if (permissions) {
      res["permissions"] = boost::any(*permissions);
    }
    if (shareFilePath) {
      res["share_file_path"] = boost::any(*shareFilePath);
    }
    if (shareId) {
      res["share_id"] = boost::any(*shareId);
    }
    if (shareName) {
      res["share_name"] = boost::any(*shareName);
    }
    if (sharePolicy) {
      vector<boost::any> temp1;
      for(auto item1:*sharePolicy){
        temp1.push_back(boost::any(item1.toMap()));
      }
      res["share_policy"] = boost::any(temp1);
    }
    if (status) {
      res["status"] = boost::any(*status);
    }
    if (updatedAt) {
      res["updated_at"] = boost::any(*updatedAt);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("created_at") != m.end() && !m["created_at"].empty()) {
      createdAt = make_shared<string>(boost::any_cast<string>(m["created_at"]));
    }
    if (m.find("creator") != m.end() && !m["creator"].empty()) {
      creator = make_shared<string>(boost::any_cast<string>(m["creator"]));
    }
    if (m.find("description") != m.end() && !m["description"].empty()) {
      description = make_shared<string>(boost::any_cast<string>(m["description"]));
    }
    if (m.find("domain_id") != m.end() && !m["domain_id"].empty()) {
      domainId = make_shared<string>(boost::any_cast<string>(m["domain_id"]));
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("expiration") != m.end() && !m["expiration"].empty()) {
      expiration = make_shared<string>(boost::any_cast<string>(m["expiration"]));
    }
    if (m.find("expired") != m.end() && !m["expired"].empty()) {
      expired = make_shared<bool>(boost::any_cast<bool>(m["expired"]));
    }
    if (m.find("owner") != m.end() && !m["owner"].empty()) {
      owner = make_shared<string>(boost::any_cast<string>(m["owner"]));
    }
    if (m.find("permissions") != m.end() && !m["permissions"].empty()) {
      vector<string> toVec1;
      if (typeid(vector<boost::any>).name() == m["permissions"].type().name()) {
        vector<boost::any> vec1 = boost::any_cast<vector<boost::any>>(m["permissions"]);
        for (auto item:vec1) {
           toVec1.push_back(boost::any_cast<string>(item));
        }
      }
      permissions = make_shared<vector<string>>(toVec1);
    }
    if (m.find("share_file_path") != m.end() && !m["share_file_path"].empty()) {
      shareFilePath = make_shared<string>(boost::any_cast<string>(m["share_file_path"]));
    }
    if (m.find("share_id") != m.end() && !m["share_id"].empty()) {
      shareId = make_shared<string>(boost::any_cast<string>(m["share_id"]));
    }
    if (m.find("share_name") != m.end() && !m["share_name"].empty()) {
      shareName = make_shared<string>(boost::any_cast<string>(m["share_name"]));
    }
    if (m.find("share_policy") != m.end() && !m["share_policy"].empty()) {
      if (typeid(vector<boost::any>).name() == m["share_policy"].type().name()) {
        vector<SharePermissionPolicy> expect1;
        for(auto item1:boost::any_cast<vector<boost::any>>(m["share_policy"])){
          if (typeid(map<string, boost::any>).name() == item1.type().name()) {
            SharePermissionPolicy model2;
            model2.fromMap(boost::any_cast<map<string, boost::any>>(item1));
            expect1.push_back(model2);
          }
        }
        sharePolicy = make_shared<vector<SharePermissionPolicy>>(expect1);
      }
    }
    if (m.find("status") != m.end() && !m["status"].empty()) {
      status = make_shared<string>(boost::any_cast<string>(m["status"]));
    }
    if (m.find("updated_at") != m.end() && !m["updated_at"].empty()) {
      updatedAt = make_shared<string>(boost::any_cast<string>(m["updated_at"]));
    }
  }


  ~BaseShareResponse() = default;
};
class BatchSubResponse : public Darabonba::Model {
public:
  shared_ptr<map<string, boost::any>> body{};
  shared_ptr<string> id{};
  shared_ptr<long> status{};

  BatchSubResponse() {}

  explicit BatchSubResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (body) {
      res["body"] = boost::any(*body);
    }
    if (id) {
      res["id"] = boost::any(*id);
    }
    if (status) {
      res["status"] = boost::any(*status);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("body") != m.end() && !m["body"].empty()) {
      map<string, boost::any> map1 = boost::any_cast<map<string, boost::any>>(m["body"]);
      map<string, boost::any> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      body = make_shared<map<string, boost::any>>(toMap1);
    }
    if (m.find("id") != m.end() && !m["id"].empty()) {
      id = make_shared<string>(boost::any_cast<string>(m["id"]));
    }
    if (m.find("status") != m.end() && !m["status"].empty()) {
      status = make_shared<long>(boost::any_cast<long>(m["status"]));
    }
  }


  ~BatchSubResponse() = default;
};
class BatchResponse : public Darabonba::Model {
public:
  shared_ptr<vector<BatchSubResponse>> responses{};

  BatchResponse() {}

  explicit BatchResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (responses) {
      vector<boost::any> temp1;
      for(auto item1:*responses){
        temp1.push_back(boost::any(item1.toMap()));
      }
      res["responses"] = boost::any(temp1);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("responses") != m.end() && !m["responses"].empty()) {
      if (typeid(vector<boost::any>).name() == m["responses"].type().name()) {
        vector<BatchSubResponse> expect1;
        for(auto item1:boost::any_cast<vector<boost::any>>(m["responses"])){
          if (typeid(map<string, boost::any>).name() == item1.type().name()) {
            BatchSubResponse model2;
            model2.fromMap(boost::any_cast<map<string, boost::any>>(item1));
            expect1.push_back(model2);
          }
        }
        responses = make_shared<vector<BatchSubResponse>>(expect1);
      }
    }
  }


  ~BatchResponse() = default;
};
class CancelLinkRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<string> temporaryToken{};

  CancelLinkRequest() {}

  explicit CancelLinkRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!temporaryToken) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("temporaryToken is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (temporaryToken) {
      res["temporary_token"] = boost::any(*temporaryToken);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("temporary_token") != m.end() && !m["temporary_token"].empty()) {
      temporaryToken = make_shared<string>(boost::any_cast<string>(m["temporary_token"]));
    }
  }


  ~CancelLinkRequest() = default;
};
class CompleteFileResponse : public Darabonba::Model {
public:
  shared_ptr<string> category{};
  shared_ptr<string> contentHash{};
  shared_ptr<string> contentHashName{};
  shared_ptr<string> contentType{};
  shared_ptr<string> crc64Hash{};
  shared_ptr<string> createdAt{};
  shared_ptr<string> description{};
  shared_ptr<string> domainId{};
  shared_ptr<string> downloadUrl{};
  shared_ptr<string> driveId{};
  shared_ptr<string> encryptMode{};
  shared_ptr<string> fileExtension{};
  shared_ptr<string> fileId{};
  shared_ptr<bool> hidden{};
  shared_ptr<ImageMediaResponse> imageMediaMetadata{};
  shared_ptr<vector<string>> labels{};
  shared_ptr<string> meta{};
  shared_ptr<string> name{};
  shared_ptr<string> parentFileId{};
  shared_ptr<int> punishFlag{};
  shared_ptr<long> size{};
  shared_ptr<bool> starred{};
  shared_ptr<string> status{};
  shared_ptr<map<string, boost::any>> streamsInfo{};
  shared_ptr<string> thumbnail{};
  shared_ptr<string> trashedAt{};
  shared_ptr<string> type{};
  shared_ptr<string> updatedAt{};
  shared_ptr<string> uploadId{};
  shared_ptr<string> url{};
  shared_ptr<string> userMeta{};
  shared_ptr<VideoMediaResponse> videoMediaMetadata{};
  shared_ptr<VideoPreviewResponse> videoPreviewMetadata{};

  CompleteFileResponse() {}

  explicit CompleteFileResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    Darabonba::Model::validatePattern("domainId", domainId, "[a-z0-9A-Z]+");
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    Darabonba::Model::validateMaxLength("fileId", fileId, 50);
    Darabonba::Model::validateMinLength("fileId", fileId, 40);
    Darabonba::Model::validatePattern("fileId", fileId, "[a-z0-9]{1,50}");
    if (!name) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("name is required.")));
    }
    Darabonba::Model::validatePattern("name", name, "[a-zA-Z0-9.-]{1,1000}");
    Darabonba::Model::validateMaxLength("parentFileId", parentFileId, 50);
    Darabonba::Model::validateMinLength("parentFileId", parentFileId, 40);
    Darabonba::Model::validatePattern("parentFileId", parentFileId, "[a-z0-9]{1,50}");
    if (size && *size > 53687091200) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("size is required.")));
    }
    if (size && *size < 0) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("size is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (category) {
      res["category"] = boost::any(*category);
    }
    if (contentHash) {
      res["content_hash"] = boost::any(*contentHash);
    }
    if (contentHashName) {
      res["content_hash_name"] = boost::any(*contentHashName);
    }
    if (contentType) {
      res["content_type"] = boost::any(*contentType);
    }
    if (crc64Hash) {
      res["crc64_hash"] = boost::any(*crc64Hash);
    }
    if (createdAt) {
      res["created_at"] = boost::any(*createdAt);
    }
    if (description) {
      res["description"] = boost::any(*description);
    }
    if (domainId) {
      res["domain_id"] = boost::any(*domainId);
    }
    if (downloadUrl) {
      res["download_url"] = boost::any(*downloadUrl);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (encryptMode) {
      res["encrypt_mode"] = boost::any(*encryptMode);
    }
    if (fileExtension) {
      res["file_extension"] = boost::any(*fileExtension);
    }
    if (fileId) {
      res["file_id"] = boost::any(*fileId);
    }
    if (hidden) {
      res["hidden"] = boost::any(*hidden);
    }
    if (imageMediaMetadata) {
      res["image_media_metadata"] = imageMediaMetadata ? boost::any(imageMediaMetadata->toMap()) : boost::any(map<string,boost::any>({}));
    }
    if (labels) {
      res["labels"] = boost::any(*labels);
    }
    if (meta) {
      res["meta"] = boost::any(*meta);
    }
    if (name) {
      res["name"] = boost::any(*name);
    }
    if (parentFileId) {
      res["parent_file_id"] = boost::any(*parentFileId);
    }
    if (punishFlag) {
      res["punish_flag"] = boost::any(*punishFlag);
    }
    if (size) {
      res["size"] = boost::any(*size);
    }
    if (starred) {
      res["starred"] = boost::any(*starred);
    }
    if (status) {
      res["status"] = boost::any(*status);
    }
    if (streamsInfo) {
      res["streams_info"] = boost::any(*streamsInfo);
    }
    if (thumbnail) {
      res["thumbnail"] = boost::any(*thumbnail);
    }
    if (trashedAt) {
      res["trashed_at"] = boost::any(*trashedAt);
    }
    if (type) {
      res["type"] = boost::any(*type);
    }
    if (updatedAt) {
      res["updated_at"] = boost::any(*updatedAt);
    }
    if (uploadId) {
      res["upload_id"] = boost::any(*uploadId);
    }
    if (url) {
      res["url"] = boost::any(*url);
    }
    if (userMeta) {
      res["user_meta"] = boost::any(*userMeta);
    }
    if (videoMediaMetadata) {
      res["video_media_metadata"] = videoMediaMetadata ? boost::any(videoMediaMetadata->toMap()) : boost::any(map<string,boost::any>({}));
    }
    if (videoPreviewMetadata) {
      res["video_preview_metadata"] = videoPreviewMetadata ? boost::any(videoPreviewMetadata->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("category") != m.end() && !m["category"].empty()) {
      category = make_shared<string>(boost::any_cast<string>(m["category"]));
    }
    if (m.find("content_hash") != m.end() && !m["content_hash"].empty()) {
      contentHash = make_shared<string>(boost::any_cast<string>(m["content_hash"]));
    }
    if (m.find("content_hash_name") != m.end() && !m["content_hash_name"].empty()) {
      contentHashName = make_shared<string>(boost::any_cast<string>(m["content_hash_name"]));
    }
    if (m.find("content_type") != m.end() && !m["content_type"].empty()) {
      contentType = make_shared<string>(boost::any_cast<string>(m["content_type"]));
    }
    if (m.find("crc64_hash") != m.end() && !m["crc64_hash"].empty()) {
      crc64Hash = make_shared<string>(boost::any_cast<string>(m["crc64_hash"]));
    }
    if (m.find("created_at") != m.end() && !m["created_at"].empty()) {
      createdAt = make_shared<string>(boost::any_cast<string>(m["created_at"]));
    }
    if (m.find("description") != m.end() && !m["description"].empty()) {
      description = make_shared<string>(boost::any_cast<string>(m["description"]));
    }
    if (m.find("domain_id") != m.end() && !m["domain_id"].empty()) {
      domainId = make_shared<string>(boost::any_cast<string>(m["domain_id"]));
    }
    if (m.find("download_url") != m.end() && !m["download_url"].empty()) {
      downloadUrl = make_shared<string>(boost::any_cast<string>(m["download_url"]));
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("encrypt_mode") != m.end() && !m["encrypt_mode"].empty()) {
      encryptMode = make_shared<string>(boost::any_cast<string>(m["encrypt_mode"]));
    }
    if (m.find("file_extension") != m.end() && !m["file_extension"].empty()) {
      fileExtension = make_shared<string>(boost::any_cast<string>(m["file_extension"]));
    }
    if (m.find("file_id") != m.end() && !m["file_id"].empty()) {
      fileId = make_shared<string>(boost::any_cast<string>(m["file_id"]));
    }
    if (m.find("hidden") != m.end() && !m["hidden"].empty()) {
      hidden = make_shared<bool>(boost::any_cast<bool>(m["hidden"]));
    }
    if (m.find("image_media_metadata") != m.end() && !m["image_media_metadata"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["image_media_metadata"].type().name()) {
        ImageMediaResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["image_media_metadata"]));
        imageMediaMetadata = make_shared<ImageMediaResponse>(model1);
      }
    }
    if (m.find("labels") != m.end() && !m["labels"].empty()) {
      vector<string> toVec1;
      if (typeid(vector<boost::any>).name() == m["labels"].type().name()) {
        vector<boost::any> vec1 = boost::any_cast<vector<boost::any>>(m["labels"]);
        for (auto item:vec1) {
           toVec1.push_back(boost::any_cast<string>(item));
        }
      }
      labels = make_shared<vector<string>>(toVec1);
    }
    if (m.find("meta") != m.end() && !m["meta"].empty()) {
      meta = make_shared<string>(boost::any_cast<string>(m["meta"]));
    }
    if (m.find("name") != m.end() && !m["name"].empty()) {
      name = make_shared<string>(boost::any_cast<string>(m["name"]));
    }
    if (m.find("parent_file_id") != m.end() && !m["parent_file_id"].empty()) {
      parentFileId = make_shared<string>(boost::any_cast<string>(m["parent_file_id"]));
    }
    if (m.find("punish_flag") != m.end() && !m["punish_flag"].empty()) {
      punishFlag = make_shared<int>(boost::any_cast<int>(m["punish_flag"]));
    }
    if (m.find("size") != m.end() && !m["size"].empty()) {
      size = make_shared<long>(boost::any_cast<long>(m["size"]));
    }
    if (m.find("starred") != m.end() && !m["starred"].empty()) {
      starred = make_shared<bool>(boost::any_cast<bool>(m["starred"]));
    }
    if (m.find("status") != m.end() && !m["status"].empty()) {
      status = make_shared<string>(boost::any_cast<string>(m["status"]));
    }
    if (m.find("streams_info") != m.end() && !m["streams_info"].empty()) {
      map<string, boost::any> map1 = boost::any_cast<map<string, boost::any>>(m["streams_info"]);
      map<string, boost::any> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      streamsInfo = make_shared<map<string, boost::any>>(toMap1);
    }
    if (m.find("thumbnail") != m.end() && !m["thumbnail"].empty()) {
      thumbnail = make_shared<string>(boost::any_cast<string>(m["thumbnail"]));
    }
    if (m.find("trashed_at") != m.end() && !m["trashed_at"].empty()) {
      trashedAt = make_shared<string>(boost::any_cast<string>(m["trashed_at"]));
    }
    if (m.find("type") != m.end() && !m["type"].empty()) {
      type = make_shared<string>(boost::any_cast<string>(m["type"]));
    }
    if (m.find("updated_at") != m.end() && !m["updated_at"].empty()) {
      updatedAt = make_shared<string>(boost::any_cast<string>(m["updated_at"]));
    }
    if (m.find("upload_id") != m.end() && !m["upload_id"].empty()) {
      uploadId = make_shared<string>(boost::any_cast<string>(m["upload_id"]));
    }
    if (m.find("url") != m.end() && !m["url"].empty()) {
      url = make_shared<string>(boost::any_cast<string>(m["url"]));
    }
    if (m.find("user_meta") != m.end() && !m["user_meta"].empty()) {
      userMeta = make_shared<string>(boost::any_cast<string>(m["user_meta"]));
    }
    if (m.find("video_media_metadata") != m.end() && !m["video_media_metadata"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["video_media_metadata"].type().name()) {
        VideoMediaResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["video_media_metadata"]));
        videoMediaMetadata = make_shared<VideoMediaResponse>(model1);
      }
    }
    if (m.find("video_preview_metadata") != m.end() && !m["video_preview_metadata"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["video_preview_metadata"].type().name()) {
        VideoPreviewResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["video_preview_metadata"]));
        videoPreviewMetadata = make_shared<VideoPreviewResponse>(model1);
      }
    }
  }


  ~CompleteFileResponse() = default;
};
class ConfirmLinkRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<string> temporaryToken{};

  ConfirmLinkRequest() {}

  explicit ConfirmLinkRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!temporaryToken) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("temporaryToken is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (temporaryToken) {
      res["temporary_token"] = boost::any(*temporaryToken);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("temporary_token") != m.end() && !m["temporary_token"].empty()) {
      temporaryToken = make_shared<string>(boost::any_cast<string>(m["temporary_token"]));
    }
  }


  ~ConfirmLinkRequest() = default;
};
class CopyFileResponse : public Darabonba::Model {
public:
  shared_ptr<string> asyncTaskId{};
  shared_ptr<string> domainId{};
  shared_ptr<string> driveId{};
  shared_ptr<string> fileId{};

  CopyFileResponse() {}

  explicit CopyFileResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    Darabonba::Model::validatePattern("domainId", domainId, "[a-z0-9A-Z]+");
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    Darabonba::Model::validateMaxLength("fileId", fileId, 50);
    Darabonba::Model::validateMinLength("fileId", fileId, 40);
    Darabonba::Model::validatePattern("fileId", fileId, "[a-z0-9]{1,50}");
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (asyncTaskId) {
      res["async_task_id"] = boost::any(*asyncTaskId);
    }
    if (domainId) {
      res["domain_id"] = boost::any(*domainId);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (fileId) {
      res["file_id"] = boost::any(*fileId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("async_task_id") != m.end() && !m["async_task_id"].empty()) {
      asyncTaskId = make_shared<string>(boost::any_cast<string>(m["async_task_id"]));
    }
    if (m.find("domain_id") != m.end() && !m["domain_id"].empty()) {
      domainId = make_shared<string>(boost::any_cast<string>(m["domain_id"]));
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("file_id") != m.end() && !m["file_id"].empty()) {
      fileId = make_shared<string>(boost::any_cast<string>(m["file_id"]));
    }
  }


  ~CopyFileResponse() = default;
};
class CorsRule : public Darabonba::Model {
public:
  shared_ptr<vector<string>> allowedHeader{};
  shared_ptr<vector<string>> allowedMethod{};
  shared_ptr<vector<string>> allowedOrigin{};
  shared_ptr<vector<string>> exposeHeader{};
  shared_ptr<long> maxAgeSeconds{};

  CorsRule() {}

  explicit CorsRule(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (allowedHeader) {
      res["allowed_header"] = boost::any(*allowedHeader);
    }
    if (allowedMethod) {
      res["allowed_method"] = boost::any(*allowedMethod);
    }
    if (allowedOrigin) {
      res["allowed_origin"] = boost::any(*allowedOrigin);
    }
    if (exposeHeader) {
      res["expose_header"] = boost::any(*exposeHeader);
    }
    if (maxAgeSeconds) {
      res["max_age_seconds"] = boost::any(*maxAgeSeconds);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("allowed_header") != m.end() && !m["allowed_header"].empty()) {
      vector<string> toVec1;
      if (typeid(vector<boost::any>).name() == m["allowed_header"].type().name()) {
        vector<boost::any> vec1 = boost::any_cast<vector<boost::any>>(m["allowed_header"]);
        for (auto item:vec1) {
           toVec1.push_back(boost::any_cast<string>(item));
        }
      }
      allowedHeader = make_shared<vector<string>>(toVec1);
    }
    if (m.find("allowed_method") != m.end() && !m["allowed_method"].empty()) {
      vector<string> toVec1;
      if (typeid(vector<boost::any>).name() == m["allowed_method"].type().name()) {
        vector<boost::any> vec1 = boost::any_cast<vector<boost::any>>(m["allowed_method"]);
        for (auto item:vec1) {
           toVec1.push_back(boost::any_cast<string>(item));
        }
      }
      allowedMethod = make_shared<vector<string>>(toVec1);
    }
    if (m.find("allowed_origin") != m.end() && !m["allowed_origin"].empty()) {
      vector<string> toVec1;
      if (typeid(vector<boost::any>).name() == m["allowed_origin"].type().name()) {
        vector<boost::any> vec1 = boost::any_cast<vector<boost::any>>(m["allowed_origin"]);
        for (auto item:vec1) {
           toVec1.push_back(boost::any_cast<string>(item));
        }
      }
      allowedOrigin = make_shared<vector<string>>(toVec1);
    }
    if (m.find("expose_header") != m.end() && !m["expose_header"].empty()) {
      vector<string> toVec1;
      if (typeid(vector<boost::any>).name() == m["expose_header"].type().name()) {
        vector<boost::any> vec1 = boost::any_cast<vector<boost::any>>(m["expose_header"]);
        for (auto item:vec1) {
           toVec1.push_back(boost::any_cast<string>(item));
        }
      }
      exposeHeader = make_shared<vector<string>>(toVec1);
    }
    if (m.find("max_age_seconds") != m.end() && !m["max_age_seconds"].empty()) {
      maxAgeSeconds = make_shared<long>(boost::any_cast<long>(m["max_age_seconds"]));
    }
  }


  ~CorsRule() = default;
};
class CreateDriveResponse : public Darabonba::Model {
public:
  shared_ptr<string> domainId{};
  shared_ptr<string> driveId{};

  CreateDriveResponse() {}

  explicit CreateDriveResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (domainId) {
      res["domain_id"] = boost::any(*domainId);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("domain_id") != m.end() && !m["domain_id"].empty()) {
      domainId = make_shared<string>(boost::any_cast<string>(m["domain_id"]));
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
  }


  ~CreateDriveResponse() = default;
};
class UploadPartInfo : public Darabonba::Model {
public:
  shared_ptr<string> etag{};
  shared_ptr<long> partNumber{};
  shared_ptr<long> partSize{};
  shared_ptr<string> uploadUrl{};

  UploadPartInfo() {}

  explicit UploadPartInfo(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (partNumber && *partNumber > 10000) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("partNumber is required.")));
    }
    if (partNumber && *partNumber < 1) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("partNumber is required.")));
    }
    if (partSize && *partSize > 5368709120) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("partSize is required.")));
    }
    if (partSize && *partSize < 102400) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("partSize is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (etag) {
      res["etag"] = boost::any(*etag);
    }
    if (partNumber) {
      res["part_number"] = boost::any(*partNumber);
    }
    if (partSize) {
      res["part_size"] = boost::any(*partSize);
    }
    if (uploadUrl) {
      res["upload_url"] = boost::any(*uploadUrl);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("etag") != m.end() && !m["etag"].empty()) {
      etag = make_shared<string>(boost::any_cast<string>(m["etag"]));
    }
    if (m.find("part_number") != m.end() && !m["part_number"].empty()) {
      partNumber = make_shared<long>(boost::any_cast<long>(m["part_number"]));
    }
    if (m.find("part_size") != m.end() && !m["part_size"].empty()) {
      partSize = make_shared<long>(boost::any_cast<long>(m["part_size"]));
    }
    if (m.find("upload_url") != m.end() && !m["upload_url"].empty()) {
      uploadUrl = make_shared<string>(boost::any_cast<string>(m["upload_url"]));
    }
  }


  ~UploadPartInfo() = default;
};
class CreateFileResponse : public Darabonba::Model {
public:
  shared_ptr<string> domainId{};
  shared_ptr<string> driveId{};
  shared_ptr<string> encryptMode{};
  shared_ptr<bool> exist{};
  shared_ptr<string> fileId{};
  shared_ptr<string> fileName{};
  shared_ptr<string> parentFileId{};
  shared_ptr<vector<UploadPartInfo>> partInfoList{};
  shared_ptr<bool> rapidUpload{};
  shared_ptr<string> status{};
  shared_ptr<map<string, boost::any>> streamsUploadInfo{};
  shared_ptr<string> type{};
  shared_ptr<string> uploadId{};

  CreateFileResponse() {}

  explicit CreateFileResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    Darabonba::Model::validateMaxLength("domainId", domainId, 50);
    Darabonba::Model::validateMinLength("domainId", domainId, 40);
    Darabonba::Model::validatePattern("domainId", domainId, "[a-z0-9]{1,50}");
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    Darabonba::Model::validateMaxLength("fileId", fileId, 50);
    Darabonba::Model::validateMinLength("fileId", fileId, 40);
    Darabonba::Model::validatePattern("fileId", fileId, "[a-z0-9]{1,50}");
    Darabonba::Model::validateMaxLength("fileName", fileName, 255);
    Darabonba::Model::validateMinLength("fileName", fileName, 1);
    Darabonba::Model::validateMaxLength("parentFileId", parentFileId, 50);
    Darabonba::Model::validateMinLength("parentFileId", parentFileId, 40);
    Darabonba::Model::validatePattern("parentFileId", parentFileId, "[a-z0-9]{1,50}");
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (domainId) {
      res["domain_id"] = boost::any(*domainId);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (encryptMode) {
      res["encrypt_mode"] = boost::any(*encryptMode);
    }
    if (exist) {
      res["exist"] = boost::any(*exist);
    }
    if (fileId) {
      res["file_id"] = boost::any(*fileId);
    }
    if (fileName) {
      res["file_name"] = boost::any(*fileName);
    }
    if (parentFileId) {
      res["parent_file_id"] = boost::any(*parentFileId);
    }
    if (partInfoList) {
      vector<boost::any> temp1;
      for(auto item1:*partInfoList){
        temp1.push_back(boost::any(item1.toMap()));
      }
      res["part_info_list"] = boost::any(temp1);
    }
    if (rapidUpload) {
      res["rapid_upload"] = boost::any(*rapidUpload);
    }
    if (status) {
      res["status"] = boost::any(*status);
    }
    if (streamsUploadInfo) {
      res["streams_upload_info"] = boost::any(*streamsUploadInfo);
    }
    if (type) {
      res["type"] = boost::any(*type);
    }
    if (uploadId) {
      res["upload_id"] = boost::any(*uploadId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("domain_id") != m.end() && !m["domain_id"].empty()) {
      domainId = make_shared<string>(boost::any_cast<string>(m["domain_id"]));
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("encrypt_mode") != m.end() && !m["encrypt_mode"].empty()) {
      encryptMode = make_shared<string>(boost::any_cast<string>(m["encrypt_mode"]));
    }
    if (m.find("exist") != m.end() && !m["exist"].empty()) {
      exist = make_shared<bool>(boost::any_cast<bool>(m["exist"]));
    }
    if (m.find("file_id") != m.end() && !m["file_id"].empty()) {
      fileId = make_shared<string>(boost::any_cast<string>(m["file_id"]));
    }
    if (m.find("file_name") != m.end() && !m["file_name"].empty()) {
      fileName = make_shared<string>(boost::any_cast<string>(m["file_name"]));
    }
    if (m.find("parent_file_id") != m.end() && !m["parent_file_id"].empty()) {
      parentFileId = make_shared<string>(boost::any_cast<string>(m["parent_file_id"]));
    }
    if (m.find("part_info_list") != m.end() && !m["part_info_list"].empty()) {
      if (typeid(vector<boost::any>).name() == m["part_info_list"].type().name()) {
        vector<UploadPartInfo> expect1;
        for(auto item1:boost::any_cast<vector<boost::any>>(m["part_info_list"])){
          if (typeid(map<string, boost::any>).name() == item1.type().name()) {
            UploadPartInfo model2;
            model2.fromMap(boost::any_cast<map<string, boost::any>>(item1));
            expect1.push_back(model2);
          }
        }
        partInfoList = make_shared<vector<UploadPartInfo>>(expect1);
      }
    }
    if (m.find("rapid_upload") != m.end() && !m["rapid_upload"].empty()) {
      rapidUpload = make_shared<bool>(boost::any_cast<bool>(m["rapid_upload"]));
    }
    if (m.find("status") != m.end() && !m["status"].empty()) {
      status = make_shared<string>(boost::any_cast<string>(m["status"]));
    }
    if (m.find("streams_upload_info") != m.end() && !m["streams_upload_info"].empty()) {
      map<string, boost::any> map1 = boost::any_cast<map<string, boost::any>>(m["streams_upload_info"]);
      map<string, boost::any> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      streamsUploadInfo = make_shared<map<string, boost::any>>(toMap1);
    }
    if (m.find("type") != m.end() && !m["type"].empty()) {
      type = make_shared<string>(boost::any_cast<string>(m["type"]));
    }
    if (m.find("upload_id") != m.end() && !m["upload_id"].empty()) {
      uploadId = make_shared<string>(boost::any_cast<string>(m["upload_id"]));
    }
  }


  ~CreateFileResponse() = default;
};
class CreateShareLinkResponse : public Darabonba::Model {
public:
  shared_ptr<string> shareId{};
  shared_ptr<string> shareMsg{};
  shared_ptr<string> sharePolicy{};
  shared_ptr<string> sharePwd{};
  shared_ptr<string> shareUrl{};

  CreateShareLinkResponse() {}

  explicit CreateShareLinkResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (shareId) {
      res["share_id"] = boost::any(*shareId);
    }
    if (shareMsg) {
      res["share_msg"] = boost::any(*shareMsg);
    }
    if (sharePolicy) {
      res["share_policy"] = boost::any(*sharePolicy);
    }
    if (sharePwd) {
      res["share_pwd"] = boost::any(*sharePwd);
    }
    if (shareUrl) {
      res["share_url"] = boost::any(*shareUrl);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("share_id") != m.end() && !m["share_id"].empty()) {
      shareId = make_shared<string>(boost::any_cast<string>(m["share_id"]));
    }
    if (m.find("share_msg") != m.end() && !m["share_msg"].empty()) {
      shareMsg = make_shared<string>(boost::any_cast<string>(m["share_msg"]));
    }
    if (m.find("share_policy") != m.end() && !m["share_policy"].empty()) {
      sharePolicy = make_shared<string>(boost::any_cast<string>(m["share_policy"]));
    }
    if (m.find("share_pwd") != m.end() && !m["share_pwd"].empty()) {
      sharePwd = make_shared<string>(boost::any_cast<string>(m["share_pwd"]));
    }
    if (m.find("share_url") != m.end() && !m["share_url"].empty()) {
      shareUrl = make_shared<string>(boost::any_cast<string>(m["share_url"]));
    }
  }


  ~CreateShareLinkResponse() = default;
};
class CreateShareResponse : public Darabonba::Model {
public:
  shared_ptr<string> domainId{};
  shared_ptr<string> shareId{};

  CreateShareResponse() {}

  explicit CreateShareResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (domainId) {
      res["domain_id"] = boost::any(*domainId);
    }
    if (shareId) {
      res["share_id"] = boost::any(*shareId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("domain_id") != m.end() && !m["domain_id"].empty()) {
      domainId = make_shared<string>(boost::any_cast<string>(m["domain_id"]));
    }
    if (m.find("share_id") != m.end() && !m["share_id"].empty()) {
      shareId = make_shared<string>(boost::any_cast<string>(m["share_id"]));
    }
  }


  ~CreateShareResponse() = default;
};
class DefaultChangePasswordRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<string> appId{};
  shared_ptr<string> encryptedKey{};
  shared_ptr<string> newPassword{};
  shared_ptr<string> phoneNumber{};
  shared_ptr<string> phoneRegion{};
  shared_ptr<string> state{};

  DefaultChangePasswordRequest() {}

  explicit DefaultChangePasswordRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!appId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("appId is required.")));
    }
    if (!encryptedKey) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("encryptedKey is required.")));
    }
    if (!newPassword) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("newPassword is required.")));
    }
    if (!phoneNumber) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("phoneNumber is required.")));
    }
    if (!state) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("state is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (appId) {
      res["app_id"] = boost::any(*appId);
    }
    if (encryptedKey) {
      res["encrypted_key"] = boost::any(*encryptedKey);
    }
    if (newPassword) {
      res["new_password"] = boost::any(*newPassword);
    }
    if (phoneNumber) {
      res["phone_number"] = boost::any(*phoneNumber);
    }
    if (phoneRegion) {
      res["phone_region"] = boost::any(*phoneRegion);
    }
    if (state) {
      res["state"] = boost::any(*state);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("app_id") != m.end() && !m["app_id"].empty()) {
      appId = make_shared<string>(boost::any_cast<string>(m["app_id"]));
    }
    if (m.find("encrypted_key") != m.end() && !m["encrypted_key"].empty()) {
      encryptedKey = make_shared<string>(boost::any_cast<string>(m["encrypted_key"]));
    }
    if (m.find("new_password") != m.end() && !m["new_password"].empty()) {
      newPassword = make_shared<string>(boost::any_cast<string>(m["new_password"]));
    }
    if (m.find("phone_number") != m.end() && !m["phone_number"].empty()) {
      phoneNumber = make_shared<string>(boost::any_cast<string>(m["phone_number"]));
    }
    if (m.find("phone_region") != m.end() && !m["phone_region"].empty()) {
      phoneRegion = make_shared<string>(boost::any_cast<string>(m["phone_region"]));
    }
    if (m.find("state") != m.end() && !m["state"].empty()) {
      state = make_shared<string>(boost::any_cast<string>(m["state"]));
    }
  }


  ~DefaultChangePasswordRequest() = default;
};
class DefaultSetPasswordRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<string> appId{};
  shared_ptr<string> encryptedKey{};
  shared_ptr<string> newPassword{};
  shared_ptr<string> state{};

  DefaultSetPasswordRequest() {}

  explicit DefaultSetPasswordRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!appId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("appId is required.")));
    }
    if (!encryptedKey) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("encryptedKey is required.")));
    }
    if (!newPassword) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("newPassword is required.")));
    }
    if (!state) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("state is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (appId) {
      res["app_id"] = boost::any(*appId);
    }
    if (encryptedKey) {
      res["encrypted_key"] = boost::any(*encryptedKey);
    }
    if (newPassword) {
      res["new_password"] = boost::any(*newPassword);
    }
    if (state) {
      res["state"] = boost::any(*state);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("app_id") != m.end() && !m["app_id"].empty()) {
      appId = make_shared<string>(boost::any_cast<string>(m["app_id"]));
    }
    if (m.find("encrypted_key") != m.end() && !m["encrypted_key"].empty()) {
      encryptedKey = make_shared<string>(boost::any_cast<string>(m["encrypted_key"]));
    }
    if (m.find("new_password") != m.end() && !m["new_password"].empty()) {
      newPassword = make_shared<string>(boost::any_cast<string>(m["new_password"]));
    }
    if (m.find("state") != m.end() && !m["state"].empty()) {
      state = make_shared<string>(boost::any_cast<string>(m["state"]));
    }
  }


  ~DefaultSetPasswordRequest() = default;
};
class DeleteDriveResponse : public Darabonba::Model {
public:

  DeleteDriveResponse() {}

  explicit DeleteDriveResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
  }


};
class DeleteFileResponse : public Darabonba::Model {
public:
  shared_ptr<string> asyncTaskId{};
  shared_ptr<string> domainId{};
  shared_ptr<string> driveId{};
  shared_ptr<string> fileId{};

  DeleteFileResponse() {}

  explicit DeleteFileResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    Darabonba::Model::validatePattern("domainId", domainId, "[a-z0-9A-Z]+");
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    Darabonba::Model::validateMaxLength("fileId", fileId, 50);
    Darabonba::Model::validateMinLength("fileId", fileId, 40);
    Darabonba::Model::validatePattern("fileId", fileId, "[a-z0-9]{1,50}");
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (asyncTaskId) {
      res["async_task_id"] = boost::any(*asyncTaskId);
    }
    if (domainId) {
      res["domain_id"] = boost::any(*domainId);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (fileId) {
      res["file_id"] = boost::any(*fileId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("async_task_id") != m.end() && !m["async_task_id"].empty()) {
      asyncTaskId = make_shared<string>(boost::any_cast<string>(m["async_task_id"]));
    }
    if (m.find("domain_id") != m.end() && !m["domain_id"].empty()) {
      domainId = make_shared<string>(boost::any_cast<string>(m["domain_id"]));
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("file_id") != m.end() && !m["file_id"].empty()) {
      fileId = make_shared<string>(boost::any_cast<string>(m["file_id"]));
    }
  }


  ~DeleteFileResponse() = default;
};
class DeleteFilesResponse : public Darabonba::Model {
public:
  shared_ptr<vector<string>> deletedFileIdList{};
  shared_ptr<string> domainId{};
  shared_ptr<string> driveId{};

  DeleteFilesResponse() {}

  explicit DeleteFilesResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    Darabonba::Model::validatePattern("domainId", domainId, "[a-z0-9A-Z]+");
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (deletedFileIdList) {
      res["deleted_file_id_list"] = boost::any(*deletedFileIdList);
    }
    if (domainId) {
      res["domain_id"] = boost::any(*domainId);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("deleted_file_id_list") != m.end() && !m["deleted_file_id_list"].empty()) {
      vector<string> toVec1;
      if (typeid(vector<boost::any>).name() == m["deleted_file_id_list"].type().name()) {
        vector<boost::any> vec1 = boost::any_cast<vector<boost::any>>(m["deleted_file_id_list"]);
        for (auto item:vec1) {
           toVec1.push_back(boost::any_cast<string>(item));
        }
      }
      deletedFileIdList = make_shared<vector<string>>(toVec1);
    }
    if (m.find("domain_id") != m.end() && !m["domain_id"].empty()) {
      domainId = make_shared<string>(boost::any_cast<string>(m["domain_id"]));
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
  }


  ~DeleteFilesResponse() = default;
};
class DeviceAuthorizeRequest : public Darabonba::Model {
public:
  shared_ptr<string> ClientID{};
  shared_ptr<string> DeviceInfo{};
  shared_ptr<string> DeviceName{};
  shared_ptr<string> LoginType{};
  shared_ptr<vector<string>> Scope{};

  DeviceAuthorizeRequest() {}

  explicit DeviceAuthorizeRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!ClientID) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("ClientID is required.")));
    }
    if (!DeviceName) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("DeviceName is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (ClientID) {
      res["ClientID"] = boost::any(*ClientID);
    }
    if (DeviceInfo) {
      res["DeviceInfo"] = boost::any(*DeviceInfo);
    }
    if (DeviceName) {
      res["DeviceName"] = boost::any(*DeviceName);
    }
    if (LoginType) {
      res["LoginType"] = boost::any(*LoginType);
    }
    if (Scope) {
      res["Scope"] = boost::any(*Scope);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("ClientID") != m.end() && !m["ClientID"].empty()) {
      ClientID = make_shared<string>(boost::any_cast<string>(m["ClientID"]));
    }
    if (m.find("DeviceInfo") != m.end() && !m["DeviceInfo"].empty()) {
      DeviceInfo = make_shared<string>(boost::any_cast<string>(m["DeviceInfo"]));
    }
    if (m.find("DeviceName") != m.end() && !m["DeviceName"].empty()) {
      DeviceName = make_shared<string>(boost::any_cast<string>(m["DeviceName"]));
    }
    if (m.find("LoginType") != m.end() && !m["LoginType"].empty()) {
      LoginType = make_shared<string>(boost::any_cast<string>(m["LoginType"]));
    }
    if (m.find("Scope") != m.end() && !m["Scope"].empty()) {
      vector<string> toVec1;
      if (typeid(vector<boost::any>).name() == m["Scope"].type().name()) {
        vector<boost::any> vec1 = boost::any_cast<vector<boost::any>>(m["Scope"]);
        for (auto item:vec1) {
           toVec1.push_back(boost::any_cast<string>(item));
        }
      }
      Scope = make_shared<vector<string>>(toVec1);
    }
  }


  ~DeviceAuthorizeRequest() = default;
};
class FileDeltaResponse : public Darabonba::Model {
public:
  shared_ptr<string> currentCategory{};
  shared_ptr<BaseFileResponse> file{};
  shared_ptr<string> fileId{};
  shared_ptr<string> op{};

  FileDeltaResponse() {}

  explicit FileDeltaResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (currentCategory) {
      res["current_category"] = boost::any(*currentCategory);
    }
    if (file) {
      res["file"] = file ? boost::any(file->toMap()) : boost::any(map<string,boost::any>({}));
    }
    if (fileId) {
      res["file_id"] = boost::any(*fileId);
    }
    if (op) {
      res["op"] = boost::any(*op);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("current_category") != m.end() && !m["current_category"].empty()) {
      currentCategory = make_shared<string>(boost::any_cast<string>(m["current_category"]));
    }
    if (m.find("file") != m.end() && !m["file"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["file"].type().name()) {
        BaseFileResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["file"]));
        file = make_shared<BaseFileResponse>(model1);
      }
    }
    if (m.find("file_id") != m.end() && !m["file_id"].empty()) {
      fileId = make_shared<string>(boost::any_cast<string>(m["file_id"]));
    }
    if (m.find("op") != m.end() && !m["op"].empty()) {
      op = make_shared<string>(boost::any_cast<string>(m["op"]));
    }
  }


  ~FileDeltaResponse() = default;
};
class GetAccessTokenByLinkInfoRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<string> extra{};
  shared_ptr<string> identity{};
  shared_ptr<string> type{};

  GetAccessTokenByLinkInfoRequest() {}

  explicit GetAccessTokenByLinkInfoRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!identity) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("identity is required.")));
    }
    if (!type) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("type is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (extra) {
      res["extra"] = boost::any(*extra);
    }
    if (identity) {
      res["identity"] = boost::any(*identity);
    }
    if (type) {
      res["type"] = boost::any(*type);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("extra") != m.end() && !m["extra"].empty()) {
      extra = make_shared<string>(boost::any_cast<string>(m["extra"]));
    }
    if (m.find("identity") != m.end() && !m["identity"].empty()) {
      identity = make_shared<string>(boost::any_cast<string>(m["identity"]));
    }
    if (m.find("type") != m.end() && !m["type"].empty()) {
      type = make_shared<string>(boost::any_cast<string>(m["type"]));
    }
  }


  ~GetAccessTokenByLinkInfoRequest() = default;
};
class GetAppPublicKeyRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<string> appId{};

  GetAppPublicKeyRequest() {}

  explicit GetAppPublicKeyRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (appId) {
      res["app_id"] = boost::any(*appId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("app_id") != m.end() && !m["app_id"].empty()) {
      appId = make_shared<string>(boost::any_cast<string>(m["app_id"]));
    }
  }


  ~GetAppPublicKeyRequest() = default;
};
class GetAsyncTaskResponse : public Darabonba::Model {
public:
  shared_ptr<string> asyncTaskId{};
  shared_ptr<string> message{};
  shared_ptr<string> state{};

  GetAsyncTaskResponse() {}

  explicit GetAsyncTaskResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (asyncTaskId) {
      res["async_task_id"] = boost::any(*asyncTaskId);
    }
    if (message) {
      res["message"] = boost::any(*message);
    }
    if (state) {
      res["state"] = boost::any(*state);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("async_task_id") != m.end() && !m["async_task_id"].empty()) {
      asyncTaskId = make_shared<string>(boost::any_cast<string>(m["async_task_id"]));
    }
    if (m.find("message") != m.end() && !m["message"].empty()) {
      message = make_shared<string>(boost::any_cast<string>(m["message"]));
    }
    if (m.find("state") != m.end() && !m["state"].empty()) {
      state = make_shared<string>(boost::any_cast<string>(m["state"]));
    }
  }


  ~GetAsyncTaskResponse() = default;
};
class GetByLinkInfoRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<string> extra{};
  shared_ptr<string> identity{};
  shared_ptr<string> type{};

  GetByLinkInfoRequest() {}

  explicit GetByLinkInfoRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!identity) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("identity is required.")));
    }
    if (!type) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("type is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (extra) {
      res["extra"] = boost::any(*extra);
    }
    if (identity) {
      res["identity"] = boost::any(*identity);
    }
    if (type) {
      res["type"] = boost::any(*type);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("extra") != m.end() && !m["extra"].empty()) {
      extra = make_shared<string>(boost::any_cast<string>(m["extra"]));
    }
    if (m.find("identity") != m.end() && !m["identity"].empty()) {
      identity = make_shared<string>(boost::any_cast<string>(m["identity"]));
    }
    if (m.find("type") != m.end() && !m["type"].empty()) {
      type = make_shared<string>(boost::any_cast<string>(m["type"]));
    }
  }


  ~GetByLinkInfoRequest() = default;
};
class GetCaptchaRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<string> appId{};

  GetCaptchaRequest() {}

  explicit GetCaptchaRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!appId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("appId is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (appId) {
      res["app_id"] = boost::any(*appId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("app_id") != m.end() && !m["app_id"].empty()) {
      appId = make_shared<string>(boost::any_cast<string>(m["app_id"]));
    }
  }


  ~GetCaptchaRequest() = default;
};
class RateLimit : public Darabonba::Model {
public:
  shared_ptr<long> partSize{};
  shared_ptr<long> partSpeed{};

  RateLimit() {}

  explicit RateLimit(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (partSize) {
      res["part_size"] = boost::any(*partSize);
    }
    if (partSpeed) {
      res["part_speed"] = boost::any(*partSpeed);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("part_size") != m.end() && !m["part_size"].empty()) {
      partSize = make_shared<long>(boost::any_cast<long>(m["part_size"]));
    }
    if (m.find("part_speed") != m.end() && !m["part_speed"].empty()) {
      partSpeed = make_shared<long>(boost::any_cast<long>(m["part_speed"]));
    }
  }


  ~RateLimit() = default;
};
class GetDownloadUrlResponse : public Darabonba::Model {
public:
  shared_ptr<string> expiration{};
  shared_ptr<string> method{};
  shared_ptr<RateLimit> ratelimit{};
  shared_ptr<long> size{};
  shared_ptr<map<string, boost::any>> streamsUrl{};
  shared_ptr<string> url{};

  GetDownloadUrlResponse() {}

  explicit GetDownloadUrlResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (expiration) {
      res["expiration"] = boost::any(*expiration);
    }
    if (method) {
      res["method"] = boost::any(*method);
    }
    if (ratelimit) {
      res["ratelimit"] = ratelimit ? boost::any(ratelimit->toMap()) : boost::any(map<string,boost::any>({}));
    }
    if (size) {
      res["size"] = boost::any(*size);
    }
    if (streamsUrl) {
      res["streams_url"] = boost::any(*streamsUrl);
    }
    if (url) {
      res["url"] = boost::any(*url);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("expiration") != m.end() && !m["expiration"].empty()) {
      expiration = make_shared<string>(boost::any_cast<string>(m["expiration"]));
    }
    if (m.find("method") != m.end() && !m["method"].empty()) {
      method = make_shared<string>(boost::any_cast<string>(m["method"]));
    }
    if (m.find("ratelimit") != m.end() && !m["ratelimit"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["ratelimit"].type().name()) {
        RateLimit model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["ratelimit"]));
        ratelimit = make_shared<RateLimit>(model1);
      }
    }
    if (m.find("size") != m.end() && !m["size"].empty()) {
      size = make_shared<long>(boost::any_cast<long>(m["size"]));
    }
    if (m.find("streams_url") != m.end() && !m["streams_url"].empty()) {
      map<string, boost::any> map1 = boost::any_cast<map<string, boost::any>>(m["streams_url"]);
      map<string, boost::any> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      streamsUrl = make_shared<map<string, boost::any>>(toMap1);
    }
    if (m.find("url") != m.end() && !m["url"].empty()) {
      url = make_shared<string>(boost::any_cast<string>(m["url"]));
    }
  }


  ~GetDownloadUrlResponse() = default;
};
class GetDriveResponse : public Darabonba::Model {
public:
  shared_ptr<string> creator{};
  shared_ptr<string> description{};
  shared_ptr<string> domainId{};
  shared_ptr<string> driveId{};
  shared_ptr<string> driveName{};
  shared_ptr<string> driveType{};
  shared_ptr<bool> encryptDataAccess{};
  shared_ptr<string> encryptMode{};
  shared_ptr<string> owner{};
  shared_ptr<string> relativePath{};
  shared_ptr<string> status{};
  shared_ptr<string> storeId{};
  shared_ptr<long> totalSize{};
  shared_ptr<long> usedSize{};

  GetDriveResponse() {}

  explicit GetDriveResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (creator) {
      res["creator"] = boost::any(*creator);
    }
    if (description) {
      res["description"] = boost::any(*description);
    }
    if (domainId) {
      res["domain_id"] = boost::any(*domainId);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (driveName) {
      res["drive_name"] = boost::any(*driveName);
    }
    if (driveType) {
      res["drive_type"] = boost::any(*driveType);
    }
    if (encryptDataAccess) {
      res["encrypt_data_access"] = boost::any(*encryptDataAccess);
    }
    if (encryptMode) {
      res["encrypt_mode"] = boost::any(*encryptMode);
    }
    if (owner) {
      res["owner"] = boost::any(*owner);
    }
    if (relativePath) {
      res["relative_path"] = boost::any(*relativePath);
    }
    if (status) {
      res["status"] = boost::any(*status);
    }
    if (storeId) {
      res["store_id"] = boost::any(*storeId);
    }
    if (totalSize) {
      res["total_size"] = boost::any(*totalSize);
    }
    if (usedSize) {
      res["used_size"] = boost::any(*usedSize);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("creator") != m.end() && !m["creator"].empty()) {
      creator = make_shared<string>(boost::any_cast<string>(m["creator"]));
    }
    if (m.find("description") != m.end() && !m["description"].empty()) {
      description = make_shared<string>(boost::any_cast<string>(m["description"]));
    }
    if (m.find("domain_id") != m.end() && !m["domain_id"].empty()) {
      domainId = make_shared<string>(boost::any_cast<string>(m["domain_id"]));
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("drive_name") != m.end() && !m["drive_name"].empty()) {
      driveName = make_shared<string>(boost::any_cast<string>(m["drive_name"]));
    }
    if (m.find("drive_type") != m.end() && !m["drive_type"].empty()) {
      driveType = make_shared<string>(boost::any_cast<string>(m["drive_type"]));
    }
    if (m.find("encrypt_data_access") != m.end() && !m["encrypt_data_access"].empty()) {
      encryptDataAccess = make_shared<bool>(boost::any_cast<bool>(m["encrypt_data_access"]));
    }
    if (m.find("encrypt_mode") != m.end() && !m["encrypt_mode"].empty()) {
      encryptMode = make_shared<string>(boost::any_cast<string>(m["encrypt_mode"]));
    }
    if (m.find("owner") != m.end() && !m["owner"].empty()) {
      owner = make_shared<string>(boost::any_cast<string>(m["owner"]));
    }
    if (m.find("relative_path") != m.end() && !m["relative_path"].empty()) {
      relativePath = make_shared<string>(boost::any_cast<string>(m["relative_path"]));
    }
    if (m.find("status") != m.end() && !m["status"].empty()) {
      status = make_shared<string>(boost::any_cast<string>(m["status"]));
    }
    if (m.find("store_id") != m.end() && !m["store_id"].empty()) {
      storeId = make_shared<string>(boost::any_cast<string>(m["store_id"]));
    }
    if (m.find("total_size") != m.end() && !m["total_size"].empty()) {
      totalSize = make_shared<long>(boost::any_cast<long>(m["total_size"]));
    }
    if (m.find("used_size") != m.end() && !m["used_size"].empty()) {
      usedSize = make_shared<long>(boost::any_cast<long>(m["used_size"]));
    }
  }


  ~GetDriveResponse() = default;
};
class GetFileByPathResponse : public Darabonba::Model {
public:
  shared_ptr<string> category{};
  shared_ptr<string> contentHash{};
  shared_ptr<string> contentHashName{};
  shared_ptr<string> contentType{};
  shared_ptr<string> crc64Hash{};
  shared_ptr<string> createdAt{};
  shared_ptr<string> description{};
  shared_ptr<string> domainId{};
  shared_ptr<string> downloadUrl{};
  shared_ptr<string> driveId{};
  shared_ptr<string> encryptMode{};
  shared_ptr<string> fileExtension{};
  shared_ptr<string> fileId{};
  shared_ptr<bool> hidden{};
  shared_ptr<ImageMediaResponse> imageMediaMetadata{};
  shared_ptr<vector<string>> labels{};
  shared_ptr<string> meta{};
  shared_ptr<string> name{};
  shared_ptr<string> parentFileId{};
  shared_ptr<int> punishFlag{};
  shared_ptr<long> size{};
  shared_ptr<bool> starred{};
  shared_ptr<string> status{};
  shared_ptr<map<string, boost::any>> streamsInfo{};
  shared_ptr<string> thumbnail{};
  shared_ptr<string> trashedAt{};
  shared_ptr<string> type{};
  shared_ptr<string> updatedAt{};
  shared_ptr<string> uploadId{};
  shared_ptr<string> url{};
  shared_ptr<string> userMeta{};
  shared_ptr<VideoMediaResponse> videoMediaMetadata{};
  shared_ptr<VideoPreviewResponse> videoPreviewMetadata{};

  GetFileByPathResponse() {}

  explicit GetFileByPathResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    Darabonba::Model::validatePattern("domainId", domainId, "[a-z0-9A-Z]+");
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    Darabonba::Model::validateMaxLength("fileId", fileId, 50);
    Darabonba::Model::validateMinLength("fileId", fileId, 40);
    Darabonba::Model::validatePattern("fileId", fileId, "[a-z0-9]{1,50}");
    if (!name) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("name is required.")));
    }
    Darabonba::Model::validatePattern("name", name, "[a-zA-Z0-9.-]{1,1000}");
    Darabonba::Model::validateMaxLength("parentFileId", parentFileId, 50);
    Darabonba::Model::validateMinLength("parentFileId", parentFileId, 40);
    Darabonba::Model::validatePattern("parentFileId", parentFileId, "[a-z0-9]{1,50}");
    if (size && *size > 53687091200) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("size is required.")));
    }
    if (size && *size < 0) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("size is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (category) {
      res["category"] = boost::any(*category);
    }
    if (contentHash) {
      res["content_hash"] = boost::any(*contentHash);
    }
    if (contentHashName) {
      res["content_hash_name"] = boost::any(*contentHashName);
    }
    if (contentType) {
      res["content_type"] = boost::any(*contentType);
    }
    if (crc64Hash) {
      res["crc64_hash"] = boost::any(*crc64Hash);
    }
    if (createdAt) {
      res["created_at"] = boost::any(*createdAt);
    }
    if (description) {
      res["description"] = boost::any(*description);
    }
    if (domainId) {
      res["domain_id"] = boost::any(*domainId);
    }
    if (downloadUrl) {
      res["download_url"] = boost::any(*downloadUrl);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (encryptMode) {
      res["encrypt_mode"] = boost::any(*encryptMode);
    }
    if (fileExtension) {
      res["file_extension"] = boost::any(*fileExtension);
    }
    if (fileId) {
      res["file_id"] = boost::any(*fileId);
    }
    if (hidden) {
      res["hidden"] = boost::any(*hidden);
    }
    if (imageMediaMetadata) {
      res["image_media_metadata"] = imageMediaMetadata ? boost::any(imageMediaMetadata->toMap()) : boost::any(map<string,boost::any>({}));
    }
    if (labels) {
      res["labels"] = boost::any(*labels);
    }
    if (meta) {
      res["meta"] = boost::any(*meta);
    }
    if (name) {
      res["name"] = boost::any(*name);
    }
    if (parentFileId) {
      res["parent_file_id"] = boost::any(*parentFileId);
    }
    if (punishFlag) {
      res["punish_flag"] = boost::any(*punishFlag);
    }
    if (size) {
      res["size"] = boost::any(*size);
    }
    if (starred) {
      res["starred"] = boost::any(*starred);
    }
    if (status) {
      res["status"] = boost::any(*status);
    }
    if (streamsInfo) {
      res["streams_info"] = boost::any(*streamsInfo);
    }
    if (thumbnail) {
      res["thumbnail"] = boost::any(*thumbnail);
    }
    if (trashedAt) {
      res["trashed_at"] = boost::any(*trashedAt);
    }
    if (type) {
      res["type"] = boost::any(*type);
    }
    if (updatedAt) {
      res["updated_at"] = boost::any(*updatedAt);
    }
    if (uploadId) {
      res["upload_id"] = boost::any(*uploadId);
    }
    if (url) {
      res["url"] = boost::any(*url);
    }
    if (userMeta) {
      res["user_meta"] = boost::any(*userMeta);
    }
    if (videoMediaMetadata) {
      res["video_media_metadata"] = videoMediaMetadata ? boost::any(videoMediaMetadata->toMap()) : boost::any(map<string,boost::any>({}));
    }
    if (videoPreviewMetadata) {
      res["video_preview_metadata"] = videoPreviewMetadata ? boost::any(videoPreviewMetadata->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("category") != m.end() && !m["category"].empty()) {
      category = make_shared<string>(boost::any_cast<string>(m["category"]));
    }
    if (m.find("content_hash") != m.end() && !m["content_hash"].empty()) {
      contentHash = make_shared<string>(boost::any_cast<string>(m["content_hash"]));
    }
    if (m.find("content_hash_name") != m.end() && !m["content_hash_name"].empty()) {
      contentHashName = make_shared<string>(boost::any_cast<string>(m["content_hash_name"]));
    }
    if (m.find("content_type") != m.end() && !m["content_type"].empty()) {
      contentType = make_shared<string>(boost::any_cast<string>(m["content_type"]));
    }
    if (m.find("crc64_hash") != m.end() && !m["crc64_hash"].empty()) {
      crc64Hash = make_shared<string>(boost::any_cast<string>(m["crc64_hash"]));
    }
    if (m.find("created_at") != m.end() && !m["created_at"].empty()) {
      createdAt = make_shared<string>(boost::any_cast<string>(m["created_at"]));
    }
    if (m.find("description") != m.end() && !m["description"].empty()) {
      description = make_shared<string>(boost::any_cast<string>(m["description"]));
    }
    if (m.find("domain_id") != m.end() && !m["domain_id"].empty()) {
      domainId = make_shared<string>(boost::any_cast<string>(m["domain_id"]));
    }
    if (m.find("download_url") != m.end() && !m["download_url"].empty()) {
      downloadUrl = make_shared<string>(boost::any_cast<string>(m["download_url"]));
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("encrypt_mode") != m.end() && !m["encrypt_mode"].empty()) {
      encryptMode = make_shared<string>(boost::any_cast<string>(m["encrypt_mode"]));
    }
    if (m.find("file_extension") != m.end() && !m["file_extension"].empty()) {
      fileExtension = make_shared<string>(boost::any_cast<string>(m["file_extension"]));
    }
    if (m.find("file_id") != m.end() && !m["file_id"].empty()) {
      fileId = make_shared<string>(boost::any_cast<string>(m["file_id"]));
    }
    if (m.find("hidden") != m.end() && !m["hidden"].empty()) {
      hidden = make_shared<bool>(boost::any_cast<bool>(m["hidden"]));
    }
    if (m.find("image_media_metadata") != m.end() && !m["image_media_metadata"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["image_media_metadata"].type().name()) {
        ImageMediaResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["image_media_metadata"]));
        imageMediaMetadata = make_shared<ImageMediaResponse>(model1);
      }
    }
    if (m.find("labels") != m.end() && !m["labels"].empty()) {
      vector<string> toVec1;
      if (typeid(vector<boost::any>).name() == m["labels"].type().name()) {
        vector<boost::any> vec1 = boost::any_cast<vector<boost::any>>(m["labels"]);
        for (auto item:vec1) {
           toVec1.push_back(boost::any_cast<string>(item));
        }
      }
      labels = make_shared<vector<string>>(toVec1);
    }
    if (m.find("meta") != m.end() && !m["meta"].empty()) {
      meta = make_shared<string>(boost::any_cast<string>(m["meta"]));
    }
    if (m.find("name") != m.end() && !m["name"].empty()) {
      name = make_shared<string>(boost::any_cast<string>(m["name"]));
    }
    if (m.find("parent_file_id") != m.end() && !m["parent_file_id"].empty()) {
      parentFileId = make_shared<string>(boost::any_cast<string>(m["parent_file_id"]));
    }
    if (m.find("punish_flag") != m.end() && !m["punish_flag"].empty()) {
      punishFlag = make_shared<int>(boost::any_cast<int>(m["punish_flag"]));
    }
    if (m.find("size") != m.end() && !m["size"].empty()) {
      size = make_shared<long>(boost::any_cast<long>(m["size"]));
    }
    if (m.find("starred") != m.end() && !m["starred"].empty()) {
      starred = make_shared<bool>(boost::any_cast<bool>(m["starred"]));
    }
    if (m.find("status") != m.end() && !m["status"].empty()) {
      status = make_shared<string>(boost::any_cast<string>(m["status"]));
    }
    if (m.find("streams_info") != m.end() && !m["streams_info"].empty()) {
      map<string, boost::any> map1 = boost::any_cast<map<string, boost::any>>(m["streams_info"]);
      map<string, boost::any> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      streamsInfo = make_shared<map<string, boost::any>>(toMap1);
    }
    if (m.find("thumbnail") != m.end() && !m["thumbnail"].empty()) {
      thumbnail = make_shared<string>(boost::any_cast<string>(m["thumbnail"]));
    }
    if (m.find("trashed_at") != m.end() && !m["trashed_at"].empty()) {
      trashedAt = make_shared<string>(boost::any_cast<string>(m["trashed_at"]));
    }
    if (m.find("type") != m.end() && !m["type"].empty()) {
      type = make_shared<string>(boost::any_cast<string>(m["type"]));
    }
    if (m.find("updated_at") != m.end() && !m["updated_at"].empty()) {
      updatedAt = make_shared<string>(boost::any_cast<string>(m["updated_at"]));
    }
    if (m.find("upload_id") != m.end() && !m["upload_id"].empty()) {
      uploadId = make_shared<string>(boost::any_cast<string>(m["upload_id"]));
    }
    if (m.find("url") != m.end() && !m["url"].empty()) {
      url = make_shared<string>(boost::any_cast<string>(m["url"]));
    }
    if (m.find("user_meta") != m.end() && !m["user_meta"].empty()) {
      userMeta = make_shared<string>(boost::any_cast<string>(m["user_meta"]));
    }
    if (m.find("video_media_metadata") != m.end() && !m["video_media_metadata"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["video_media_metadata"].type().name()) {
        VideoMediaResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["video_media_metadata"]));
        videoMediaMetadata = make_shared<VideoMediaResponse>(model1);
      }
    }
    if (m.find("video_preview_metadata") != m.end() && !m["video_preview_metadata"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["video_preview_metadata"].type().name()) {
        VideoPreviewResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["video_preview_metadata"]));
        videoPreviewMetadata = make_shared<VideoPreviewResponse>(model1);
      }
    }
  }


  ~GetFileByPathResponse() = default;
};
class GetFileResponse : public Darabonba::Model {
public:
  shared_ptr<string> category{};
  shared_ptr<string> contentHash{};
  shared_ptr<string> contentHashName{};
  shared_ptr<string> contentType{};
  shared_ptr<string> crc64Hash{};
  shared_ptr<string> createdAt{};
  shared_ptr<string> description{};
  shared_ptr<string> domainId{};
  shared_ptr<string> downloadUrl{};
  shared_ptr<string> driveId{};
  shared_ptr<string> encryptMode{};
  shared_ptr<string> fileExtension{};
  shared_ptr<string> fileId{};
  shared_ptr<bool> hidden{};
  shared_ptr<ImageMediaResponse> imageMediaMetadata{};
  shared_ptr<vector<string>> labels{};
  shared_ptr<string> meta{};
  shared_ptr<string> name{};
  shared_ptr<string> parentFileId{};
  shared_ptr<int> punishFlag{};
  shared_ptr<long> size{};
  shared_ptr<bool> starred{};
  shared_ptr<string> status{};
  shared_ptr<map<string, boost::any>> streamsInfo{};
  shared_ptr<string> thumbnail{};
  shared_ptr<string> trashedAt{};
  shared_ptr<string> type{};
  shared_ptr<string> updatedAt{};
  shared_ptr<string> uploadId{};
  shared_ptr<string> url{};
  shared_ptr<string> userMeta{};
  shared_ptr<VideoMediaResponse> videoMediaMetadata{};
  shared_ptr<VideoPreviewResponse> videoPreviewMetadata{};

  GetFileResponse() {}

  explicit GetFileResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    Darabonba::Model::validatePattern("domainId", domainId, "[a-z0-9A-Z]+");
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    Darabonba::Model::validateMaxLength("fileId", fileId, 50);
    Darabonba::Model::validateMinLength("fileId", fileId, 40);
    Darabonba::Model::validatePattern("fileId", fileId, "[a-z0-9]{1,50}");
    if (!name) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("name is required.")));
    }
    Darabonba::Model::validatePattern("name", name, "[a-zA-Z0-9.-]{1,1000}");
    Darabonba::Model::validateMaxLength("parentFileId", parentFileId, 50);
    Darabonba::Model::validateMinLength("parentFileId", parentFileId, 40);
    Darabonba::Model::validatePattern("parentFileId", parentFileId, "[a-z0-9]{1,50}");
    if (size && *size > 53687091200) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("size is required.")));
    }
    if (size && *size < 0) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("size is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (category) {
      res["category"] = boost::any(*category);
    }
    if (contentHash) {
      res["content_hash"] = boost::any(*contentHash);
    }
    if (contentHashName) {
      res["content_hash_name"] = boost::any(*contentHashName);
    }
    if (contentType) {
      res["content_type"] = boost::any(*contentType);
    }
    if (crc64Hash) {
      res["crc64_hash"] = boost::any(*crc64Hash);
    }
    if (createdAt) {
      res["created_at"] = boost::any(*createdAt);
    }
    if (description) {
      res["description"] = boost::any(*description);
    }
    if (domainId) {
      res["domain_id"] = boost::any(*domainId);
    }
    if (downloadUrl) {
      res["download_url"] = boost::any(*downloadUrl);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (encryptMode) {
      res["encrypt_mode"] = boost::any(*encryptMode);
    }
    if (fileExtension) {
      res["file_extension"] = boost::any(*fileExtension);
    }
    if (fileId) {
      res["file_id"] = boost::any(*fileId);
    }
    if (hidden) {
      res["hidden"] = boost::any(*hidden);
    }
    if (imageMediaMetadata) {
      res["image_media_metadata"] = imageMediaMetadata ? boost::any(imageMediaMetadata->toMap()) : boost::any(map<string,boost::any>({}));
    }
    if (labels) {
      res["labels"] = boost::any(*labels);
    }
    if (meta) {
      res["meta"] = boost::any(*meta);
    }
    if (name) {
      res["name"] = boost::any(*name);
    }
    if (parentFileId) {
      res["parent_file_id"] = boost::any(*parentFileId);
    }
    if (punishFlag) {
      res["punish_flag"] = boost::any(*punishFlag);
    }
    if (size) {
      res["size"] = boost::any(*size);
    }
    if (starred) {
      res["starred"] = boost::any(*starred);
    }
    if (status) {
      res["status"] = boost::any(*status);
    }
    if (streamsInfo) {
      res["streams_info"] = boost::any(*streamsInfo);
    }
    if (thumbnail) {
      res["thumbnail"] = boost::any(*thumbnail);
    }
    if (trashedAt) {
      res["trashed_at"] = boost::any(*trashedAt);
    }
    if (type) {
      res["type"] = boost::any(*type);
    }
    if (updatedAt) {
      res["updated_at"] = boost::any(*updatedAt);
    }
    if (uploadId) {
      res["upload_id"] = boost::any(*uploadId);
    }
    if (url) {
      res["url"] = boost::any(*url);
    }
    if (userMeta) {
      res["user_meta"] = boost::any(*userMeta);
    }
    if (videoMediaMetadata) {
      res["video_media_metadata"] = videoMediaMetadata ? boost::any(videoMediaMetadata->toMap()) : boost::any(map<string,boost::any>({}));
    }
    if (videoPreviewMetadata) {
      res["video_preview_metadata"] = videoPreviewMetadata ? boost::any(videoPreviewMetadata->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("category") != m.end() && !m["category"].empty()) {
      category = make_shared<string>(boost::any_cast<string>(m["category"]));
    }
    if (m.find("content_hash") != m.end() && !m["content_hash"].empty()) {
      contentHash = make_shared<string>(boost::any_cast<string>(m["content_hash"]));
    }
    if (m.find("content_hash_name") != m.end() && !m["content_hash_name"].empty()) {
      contentHashName = make_shared<string>(boost::any_cast<string>(m["content_hash_name"]));
    }
    if (m.find("content_type") != m.end() && !m["content_type"].empty()) {
      contentType = make_shared<string>(boost::any_cast<string>(m["content_type"]));
    }
    if (m.find("crc64_hash") != m.end() && !m["crc64_hash"].empty()) {
      crc64Hash = make_shared<string>(boost::any_cast<string>(m["crc64_hash"]));
    }
    if (m.find("created_at") != m.end() && !m["created_at"].empty()) {
      createdAt = make_shared<string>(boost::any_cast<string>(m["created_at"]));
    }
    if (m.find("description") != m.end() && !m["description"].empty()) {
      description = make_shared<string>(boost::any_cast<string>(m["description"]));
    }
    if (m.find("domain_id") != m.end() && !m["domain_id"].empty()) {
      domainId = make_shared<string>(boost::any_cast<string>(m["domain_id"]));
    }
    if (m.find("download_url") != m.end() && !m["download_url"].empty()) {
      downloadUrl = make_shared<string>(boost::any_cast<string>(m["download_url"]));
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("encrypt_mode") != m.end() && !m["encrypt_mode"].empty()) {
      encryptMode = make_shared<string>(boost::any_cast<string>(m["encrypt_mode"]));
    }
    if (m.find("file_extension") != m.end() && !m["file_extension"].empty()) {
      fileExtension = make_shared<string>(boost::any_cast<string>(m["file_extension"]));
    }
    if (m.find("file_id") != m.end() && !m["file_id"].empty()) {
      fileId = make_shared<string>(boost::any_cast<string>(m["file_id"]));
    }
    if (m.find("hidden") != m.end() && !m["hidden"].empty()) {
      hidden = make_shared<bool>(boost::any_cast<bool>(m["hidden"]));
    }
    if (m.find("image_media_metadata") != m.end() && !m["image_media_metadata"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["image_media_metadata"].type().name()) {
        ImageMediaResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["image_media_metadata"]));
        imageMediaMetadata = make_shared<ImageMediaResponse>(model1);
      }
    }
    if (m.find("labels") != m.end() && !m["labels"].empty()) {
      vector<string> toVec1;
      if (typeid(vector<boost::any>).name() == m["labels"].type().name()) {
        vector<boost::any> vec1 = boost::any_cast<vector<boost::any>>(m["labels"]);
        for (auto item:vec1) {
           toVec1.push_back(boost::any_cast<string>(item));
        }
      }
      labels = make_shared<vector<string>>(toVec1);
    }
    if (m.find("meta") != m.end() && !m["meta"].empty()) {
      meta = make_shared<string>(boost::any_cast<string>(m["meta"]));
    }
    if (m.find("name") != m.end() && !m["name"].empty()) {
      name = make_shared<string>(boost::any_cast<string>(m["name"]));
    }
    if (m.find("parent_file_id") != m.end() && !m["parent_file_id"].empty()) {
      parentFileId = make_shared<string>(boost::any_cast<string>(m["parent_file_id"]));
    }
    if (m.find("punish_flag") != m.end() && !m["punish_flag"].empty()) {
      punishFlag = make_shared<int>(boost::any_cast<int>(m["punish_flag"]));
    }
    if (m.find("size") != m.end() && !m["size"].empty()) {
      size = make_shared<long>(boost::any_cast<long>(m["size"]));
    }
    if (m.find("starred") != m.end() && !m["starred"].empty()) {
      starred = make_shared<bool>(boost::any_cast<bool>(m["starred"]));
    }
    if (m.find("status") != m.end() && !m["status"].empty()) {
      status = make_shared<string>(boost::any_cast<string>(m["status"]));
    }
    if (m.find("streams_info") != m.end() && !m["streams_info"].empty()) {
      map<string, boost::any> map1 = boost::any_cast<map<string, boost::any>>(m["streams_info"]);
      map<string, boost::any> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      streamsInfo = make_shared<map<string, boost::any>>(toMap1);
    }
    if (m.find("thumbnail") != m.end() && !m["thumbnail"].empty()) {
      thumbnail = make_shared<string>(boost::any_cast<string>(m["thumbnail"]));
    }
    if (m.find("trashed_at") != m.end() && !m["trashed_at"].empty()) {
      trashedAt = make_shared<string>(boost::any_cast<string>(m["trashed_at"]));
    }
    if (m.find("type") != m.end() && !m["type"].empty()) {
      type = make_shared<string>(boost::any_cast<string>(m["type"]));
    }
    if (m.find("updated_at") != m.end() && !m["updated_at"].empty()) {
      updatedAt = make_shared<string>(boost::any_cast<string>(m["updated_at"]));
    }
    if (m.find("upload_id") != m.end() && !m["upload_id"].empty()) {
      uploadId = make_shared<string>(boost::any_cast<string>(m["upload_id"]));
    }
    if (m.find("url") != m.end() && !m["url"].empty()) {
      url = make_shared<string>(boost::any_cast<string>(m["url"]));
    }
    if (m.find("user_meta") != m.end() && !m["user_meta"].empty()) {
      userMeta = make_shared<string>(boost::any_cast<string>(m["user_meta"]));
    }
    if (m.find("video_media_metadata") != m.end() && !m["video_media_metadata"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["video_media_metadata"].type().name()) {
        VideoMediaResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["video_media_metadata"]));
        videoMediaMetadata = make_shared<VideoMediaResponse>(model1);
      }
    }
    if (m.find("video_preview_metadata") != m.end() && !m["video_preview_metadata"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["video_preview_metadata"].type().name()) {
        VideoPreviewResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["video_preview_metadata"]));
        videoPreviewMetadata = make_shared<VideoPreviewResponse>(model1);
      }
    }
  }


  ~GetFileResponse() = default;
};
class GetLastCursorResponse : public Darabonba::Model {
public:
  shared_ptr<string> cursor{};

  GetLastCursorResponse() {}

  explicit GetLastCursorResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (cursor) {
      res["cursor"] = boost::any(*cursor);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("cursor") != m.end() && !m["cursor"].empty()) {
      cursor = make_shared<string>(boost::any_cast<string>(m["cursor"]));
    }
  }


  ~GetLastCursorResponse() = default;
};
class GetLinkInfoByUserIDRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<string> userId{};

  GetLinkInfoByUserIDRequest() {}

  explicit GetLinkInfoByUserIDRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!userId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("userId is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (userId) {
      res["user_id"] = boost::any(*userId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("user_id") != m.end() && !m["user_id"].empty()) {
      userId = make_shared<string>(boost::any_cast<string>(m["user_id"]));
    }
  }


  ~GetLinkInfoByUserIDRequest() = default;
};
class GetMediaPlayURLResponse : public Darabonba::Model {
public:
  shared_ptr<string> url{};

  GetMediaPlayURLResponse() {}

  explicit GetMediaPlayURLResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (url) {
      res["url"] = boost::any(*url);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("url") != m.end() && !m["url"].empty()) {
      url = make_shared<string>(boost::any_cast<string>(m["url"]));
    }
  }


  ~GetMediaPlayURLResponse() = default;
};
class GetOfficePreviewUrlResponse : public Darabonba::Model {
public:
  shared_ptr<string> accessToken{};
  shared_ptr<string> previewUrl{};

  GetOfficePreviewUrlResponse() {}

  explicit GetOfficePreviewUrlResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (accessToken) {
      res["access_token"] = boost::any(*accessToken);
    }
    if (previewUrl) {
      res["preview_url"] = boost::any(*previewUrl);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("access_token") != m.end() && !m["access_token"].empty()) {
      accessToken = make_shared<string>(boost::any_cast<string>(m["access_token"]));
    }
    if (m.find("preview_url") != m.end() && !m["preview_url"].empty()) {
      previewUrl = make_shared<string>(boost::any_cast<string>(m["preview_url"]));
    }
  }


  ~GetOfficePreviewUrlResponse() = default;
};
class GetPublicKeyResponse : public Darabonba::Model {
public:
  shared_ptr<string> appId{};
  shared_ptr<string> keyPairId{};
  shared_ptr<string> publicKey{};

  GetPublicKeyResponse() {}

  explicit GetPublicKeyResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!appId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("appId is required.")));
    }
    if (!publicKey) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("publicKey is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (appId) {
      res["app_id"] = boost::any(*appId);
    }
    if (keyPairId) {
      res["key_pair_id"] = boost::any(*keyPairId);
    }
    if (publicKey) {
      res["public_key"] = boost::any(*publicKey);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("app_id") != m.end() && !m["app_id"].empty()) {
      appId = make_shared<string>(boost::any_cast<string>(m["app_id"]));
    }
    if (m.find("key_pair_id") != m.end() && !m["key_pair_id"].empty()) {
      keyPairId = make_shared<string>(boost::any_cast<string>(m["key_pair_id"]));
    }
    if (m.find("public_key") != m.end() && !m["public_key"].empty()) {
      publicKey = make_shared<string>(boost::any_cast<string>(m["public_key"]));
    }
  }


  ~GetPublicKeyResponse() = default;
};
class GetShareLinkByAnonymousResponse : public Darabonba::Model {
public:
  shared_ptr<string> creatorId{};
  shared_ptr<string> creatorName{};
  shared_ptr<string> expiration{};
  shared_ptr<string> updatedAt{};

  GetShareLinkByAnonymousResponse() {}

  explicit GetShareLinkByAnonymousResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (creatorId) {
      res["creator_id"] = boost::any(*creatorId);
    }
    if (creatorName) {
      res["creator_name"] = boost::any(*creatorName);
    }
    if (expiration) {
      res["expiration"] = boost::any(*expiration);
    }
    if (updatedAt) {
      res["updated_at"] = boost::any(*updatedAt);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("creator_id") != m.end() && !m["creator_id"].empty()) {
      creatorId = make_shared<string>(boost::any_cast<string>(m["creator_id"]));
    }
    if (m.find("creator_name") != m.end() && !m["creator_name"].empty()) {
      creatorName = make_shared<string>(boost::any_cast<string>(m["creator_name"]));
    }
    if (m.find("expiration") != m.end() && !m["expiration"].empty()) {
      expiration = make_shared<string>(boost::any_cast<string>(m["expiration"]));
    }
    if (m.find("updated_at") != m.end() && !m["updated_at"].empty()) {
      updatedAt = make_shared<string>(boost::any_cast<string>(m["updated_at"]));
    }
  }


  ~GetShareLinkByAnonymousResponse() = default;
};
class GetShareLinkIDResponse : public Darabonba::Model {
public:
  shared_ptr<string> shareId{};
  shared_ptr<string> sharePwd{};

  GetShareLinkIDResponse() {}

  explicit GetShareLinkIDResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (shareId) {
      res["share_id"] = boost::any(*shareId);
    }
    if (sharePwd) {
      res["share_pwd"] = boost::any(*sharePwd);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("share_id") != m.end() && !m["share_id"].empty()) {
      shareId = make_shared<string>(boost::any_cast<string>(m["share_id"]));
    }
    if (m.find("share_pwd") != m.end() && !m["share_pwd"].empty()) {
      sharePwd = make_shared<string>(boost::any_cast<string>(m["share_pwd"]));
    }
  }


  ~GetShareLinkIDResponse() = default;
};
class GetShareLinkTokenResponse : public Darabonba::Model {
public:
  shared_ptr<string> expireTime{};
  shared_ptr<long> expiresIn{};
  shared_ptr<string> shareToken{};

  GetShareLinkTokenResponse() {}

  explicit GetShareLinkTokenResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!expireTime) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("expireTime is required.")));
    }
    if (!expiresIn) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("expiresIn is required.")));
    }
    if (!shareToken) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("shareToken is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (expireTime) {
      res["expire_time"] = boost::any(*expireTime);
    }
    if (expiresIn) {
      res["expires_in"] = boost::any(*expiresIn);
    }
    if (shareToken) {
      res["share_token"] = boost::any(*shareToken);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("expire_time") != m.end() && !m["expire_time"].empty()) {
      expireTime = make_shared<string>(boost::any_cast<string>(m["expire_time"]));
    }
    if (m.find("expires_in") != m.end() && !m["expires_in"].empty()) {
      expiresIn = make_shared<long>(boost::any_cast<long>(m["expires_in"]));
    }
    if (m.find("share_token") != m.end() && !m["share_token"].empty()) {
      shareToken = make_shared<string>(boost::any_cast<string>(m["share_token"]));
    }
  }


  ~GetShareLinkTokenResponse() = default;
};
class GetShareResponse : public Darabonba::Model {
public:
  shared_ptr<string> createdAt{};
  shared_ptr<string> creator{};
  shared_ptr<string> description{};
  shared_ptr<string> domainId{};
  shared_ptr<string> driveId{};
  shared_ptr<string> expiration{};
  shared_ptr<bool> expired{};
  shared_ptr<string> owner{};
  shared_ptr<vector<string>> permissions{};
  shared_ptr<string> shareFilePath{};
  shared_ptr<string> shareId{};
  shared_ptr<string> shareName{};
  shared_ptr<vector<SharePermissionPolicy>> sharePolicy{};
  shared_ptr<string> status{};
  shared_ptr<string> updatedAt{};

  GetShareResponse() {}

  explicit GetShareResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (createdAt) {
      res["created_at"] = boost::any(*createdAt);
    }
    if (creator) {
      res["creator"] = boost::any(*creator);
    }
    if (description) {
      res["description"] = boost::any(*description);
    }
    if (domainId) {
      res["domain_id"] = boost::any(*domainId);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (expiration) {
      res["expiration"] = boost::any(*expiration);
    }
    if (expired) {
      res["expired"] = boost::any(*expired);
    }
    if (owner) {
      res["owner"] = boost::any(*owner);
    }
    if (permissions) {
      res["permissions"] = boost::any(*permissions);
    }
    if (shareFilePath) {
      res["share_file_path"] = boost::any(*shareFilePath);
    }
    if (shareId) {
      res["share_id"] = boost::any(*shareId);
    }
    if (shareName) {
      res["share_name"] = boost::any(*shareName);
    }
    if (sharePolicy) {
      vector<boost::any> temp1;
      for(auto item1:*sharePolicy){
        temp1.push_back(boost::any(item1.toMap()));
      }
      res["share_policy"] = boost::any(temp1);
    }
    if (status) {
      res["status"] = boost::any(*status);
    }
    if (updatedAt) {
      res["updated_at"] = boost::any(*updatedAt);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("created_at") != m.end() && !m["created_at"].empty()) {
      createdAt = make_shared<string>(boost::any_cast<string>(m["created_at"]));
    }
    if (m.find("creator") != m.end() && !m["creator"].empty()) {
      creator = make_shared<string>(boost::any_cast<string>(m["creator"]));
    }
    if (m.find("description") != m.end() && !m["description"].empty()) {
      description = make_shared<string>(boost::any_cast<string>(m["description"]));
    }
    if (m.find("domain_id") != m.end() && !m["domain_id"].empty()) {
      domainId = make_shared<string>(boost::any_cast<string>(m["domain_id"]));
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("expiration") != m.end() && !m["expiration"].empty()) {
      expiration = make_shared<string>(boost::any_cast<string>(m["expiration"]));
    }
    if (m.find("expired") != m.end() && !m["expired"].empty()) {
      expired = make_shared<bool>(boost::any_cast<bool>(m["expired"]));
    }
    if (m.find("owner") != m.end() && !m["owner"].empty()) {
      owner = make_shared<string>(boost::any_cast<string>(m["owner"]));
    }
    if (m.find("permissions") != m.end() && !m["permissions"].empty()) {
      vector<string> toVec1;
      if (typeid(vector<boost::any>).name() == m["permissions"].type().name()) {
        vector<boost::any> vec1 = boost::any_cast<vector<boost::any>>(m["permissions"]);
        for (auto item:vec1) {
           toVec1.push_back(boost::any_cast<string>(item));
        }
      }
      permissions = make_shared<vector<string>>(toVec1);
    }
    if (m.find("share_file_path") != m.end() && !m["share_file_path"].empty()) {
      shareFilePath = make_shared<string>(boost::any_cast<string>(m["share_file_path"]));
    }
    if (m.find("share_id") != m.end() && !m["share_id"].empty()) {
      shareId = make_shared<string>(boost::any_cast<string>(m["share_id"]));
    }
    if (m.find("share_name") != m.end() && !m["share_name"].empty()) {
      shareName = make_shared<string>(boost::any_cast<string>(m["share_name"]));
    }
    if (m.find("share_policy") != m.end() && !m["share_policy"].empty()) {
      if (typeid(vector<boost::any>).name() == m["share_policy"].type().name()) {
        vector<SharePermissionPolicy> expect1;
        for(auto item1:boost::any_cast<vector<boost::any>>(m["share_policy"])){
          if (typeid(map<string, boost::any>).name() == item1.type().name()) {
            SharePermissionPolicy model2;
            model2.fromMap(boost::any_cast<map<string, boost::any>>(item1));
            expect1.push_back(model2);
          }
        }
        sharePolicy = make_shared<vector<SharePermissionPolicy>>(expect1);
      }
    }
    if (m.find("status") != m.end() && !m["status"].empty()) {
      status = make_shared<string>(boost::any_cast<string>(m["status"]));
    }
    if (m.find("updated_at") != m.end() && !m["updated_at"].empty()) {
      updatedAt = make_shared<string>(boost::any_cast<string>(m["updated_at"]));
    }
  }


  ~GetShareResponse() = default;
};
class GetUploadUrlResponse : public Darabonba::Model {
public:
  shared_ptr<string> createAt{};
  shared_ptr<string> domainId{};
  shared_ptr<string> driveId{};
  shared_ptr<string> fileId{};
  shared_ptr<vector<UploadPartInfo>> partInfoList{};
  shared_ptr<string> uploadId{};

  GetUploadUrlResponse() {}

  explicit GetUploadUrlResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    Darabonba::Model::validatePattern("domainId", domainId, "[a-z0-9A-Z]+");
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    Darabonba::Model::validateMaxLength("fileId", fileId, 50);
    Darabonba::Model::validateMinLength("fileId", fileId, 40);
    Darabonba::Model::validatePattern("fileId", fileId, "[a-z0-9]{1,50}");
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (createAt) {
      res["create_at"] = boost::any(*createAt);
    }
    if (domainId) {
      res["domain_id"] = boost::any(*domainId);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (fileId) {
      res["file_id"] = boost::any(*fileId);
    }
    if (partInfoList) {
      vector<boost::any> temp1;
      for(auto item1:*partInfoList){
        temp1.push_back(boost::any(item1.toMap()));
      }
      res["part_info_list"] = boost::any(temp1);
    }
    if (uploadId) {
      res["upload_id"] = boost::any(*uploadId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("create_at") != m.end() && !m["create_at"].empty()) {
      createAt = make_shared<string>(boost::any_cast<string>(m["create_at"]));
    }
    if (m.find("domain_id") != m.end() && !m["domain_id"].empty()) {
      domainId = make_shared<string>(boost::any_cast<string>(m["domain_id"]));
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("file_id") != m.end() && !m["file_id"].empty()) {
      fileId = make_shared<string>(boost::any_cast<string>(m["file_id"]));
    }
    if (m.find("part_info_list") != m.end() && !m["part_info_list"].empty()) {
      if (typeid(vector<boost::any>).name() == m["part_info_list"].type().name()) {
        vector<UploadPartInfo> expect1;
        for(auto item1:boost::any_cast<vector<boost::any>>(m["part_info_list"])){
          if (typeid(map<string, boost::any>).name() == item1.type().name()) {
            UploadPartInfo model2;
            model2.fromMap(boost::any_cast<map<string, boost::any>>(item1));
            expect1.push_back(model2);
          }
        }
        partInfoList = make_shared<vector<UploadPartInfo>>(expect1);
      }
    }
    if (m.find("upload_id") != m.end() && !m["upload_id"].empty()) {
      uploadId = make_shared<string>(boost::any_cast<string>(m["upload_id"]));
    }
  }


  ~GetUploadUrlResponse() = default;
};
class GetVideoPreviewSpriteURLResponse : public Darabonba::Model {
public:
  shared_ptr<long> col{};
  shared_ptr<long> count{};
  shared_ptr<long> frameCount{};
  shared_ptr<long> frameHeight{};
  shared_ptr<long> frameWidth{};
  shared_ptr<long> row{};
  shared_ptr<vector<string>> spriteUrlList{};

  GetVideoPreviewSpriteURLResponse() {}

  explicit GetVideoPreviewSpriteURLResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (col) {
      res["col"] = boost::any(*col);
    }
    if (count) {
      res["count"] = boost::any(*count);
    }
    if (frameCount) {
      res["frame_count"] = boost::any(*frameCount);
    }
    if (frameHeight) {
      res["frame_height"] = boost::any(*frameHeight);
    }
    if (frameWidth) {
      res["frame_width"] = boost::any(*frameWidth);
    }
    if (row) {
      res["row"] = boost::any(*row);
    }
    if (spriteUrlList) {
      res["sprite_url_list"] = boost::any(*spriteUrlList);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("col") != m.end() && !m["col"].empty()) {
      col = make_shared<long>(boost::any_cast<long>(m["col"]));
    }
    if (m.find("count") != m.end() && !m["count"].empty()) {
      count = make_shared<long>(boost::any_cast<long>(m["count"]));
    }
    if (m.find("frame_count") != m.end() && !m["frame_count"].empty()) {
      frameCount = make_shared<long>(boost::any_cast<long>(m["frame_count"]));
    }
    if (m.find("frame_height") != m.end() && !m["frame_height"].empty()) {
      frameHeight = make_shared<long>(boost::any_cast<long>(m["frame_height"]));
    }
    if (m.find("frame_width") != m.end() && !m["frame_width"].empty()) {
      frameWidth = make_shared<long>(boost::any_cast<long>(m["frame_width"]));
    }
    if (m.find("row") != m.end() && !m["row"].empty()) {
      row = make_shared<long>(boost::any_cast<long>(m["row"]));
    }
    if (m.find("sprite_url_list") != m.end() && !m["sprite_url_list"].empty()) {
      vector<string> toVec1;
      if (typeid(vector<boost::any>).name() == m["sprite_url_list"].type().name()) {
        vector<boost::any> vec1 = boost::any_cast<vector<boost::any>>(m["sprite_url_list"]);
        for (auto item:vec1) {
           toVec1.push_back(boost::any_cast<string>(item));
        }
      }
      spriteUrlList = make_shared<vector<string>>(toVec1);
    }
  }


  ~GetVideoPreviewSpriteURLResponse() = default;
};
class GetVideoPreviewURLResponse : public Darabonba::Model {
public:
  shared_ptr<string> previewUrl{};

  GetVideoPreviewURLResponse() {}

  explicit GetVideoPreviewURLResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (previewUrl) {
      res["preview_url"] = boost::any(*previewUrl);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("preview_url") != m.end() && !m["preview_url"].empty()) {
      previewUrl = make_shared<string>(boost::any_cast<string>(m["preview_url"]));
    }
  }


  ~GetVideoPreviewURLResponse() = default;
};
class ListByAnonymousResponse : public Darabonba::Model {
public:
  shared_ptr<vector<BaseFileAnonymousResponse>> items{};
  shared_ptr<string> nextMarker{};

  ListByAnonymousResponse() {}

  explicit ListByAnonymousResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (items) {
      vector<boost::any> temp1;
      for(auto item1:*items){
        temp1.push_back(boost::any(item1.toMap()));
      }
      res["items"] = boost::any(temp1);
    }
    if (nextMarker) {
      res["next_marker"] = boost::any(*nextMarker);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("items") != m.end() && !m["items"].empty()) {
      if (typeid(vector<boost::any>).name() == m["items"].type().name()) {
        vector<BaseFileAnonymousResponse> expect1;
        for(auto item1:boost::any_cast<vector<boost::any>>(m["items"])){
          if (typeid(map<string, boost::any>).name() == item1.type().name()) {
            BaseFileAnonymousResponse model2;
            model2.fromMap(boost::any_cast<map<string, boost::any>>(item1));
            expect1.push_back(model2);
          }
        }
        items = make_shared<vector<BaseFileAnonymousResponse>>(expect1);
      }
    }
    if (m.find("next_marker") != m.end() && !m["next_marker"].empty()) {
      nextMarker = make_shared<string>(boost::any_cast<string>(m["next_marker"]));
    }
  }


  ~ListByAnonymousResponse() = default;
};
class ListDriveResponse : public Darabonba::Model {
public:
  shared_ptr<vector<BaseDriveResponse>> items{};
  shared_ptr<string> nextMarker{};

  ListDriveResponse() {}

  explicit ListDriveResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (items) {
      vector<boost::any> temp1;
      for(auto item1:*items){
        temp1.push_back(boost::any(item1.toMap()));
      }
      res["items"] = boost::any(temp1);
    }
    if (nextMarker) {
      res["next_marker"] = boost::any(*nextMarker);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("items") != m.end() && !m["items"].empty()) {
      if (typeid(vector<boost::any>).name() == m["items"].type().name()) {
        vector<BaseDriveResponse> expect1;
        for(auto item1:boost::any_cast<vector<boost::any>>(m["items"])){
          if (typeid(map<string, boost::any>).name() == item1.type().name()) {
            BaseDriveResponse model2;
            model2.fromMap(boost::any_cast<map<string, boost::any>>(item1));
            expect1.push_back(model2);
          }
        }
        items = make_shared<vector<BaseDriveResponse>>(expect1);
      }
    }
    if (m.find("next_marker") != m.end() && !m["next_marker"].empty()) {
      nextMarker = make_shared<string>(boost::any_cast<string>(m["next_marker"]));
    }
  }


  ~ListDriveResponse() = default;
};
class ListFileDeltaResponse : public Darabonba::Model {
public:
  shared_ptr<string> cursor{};
  shared_ptr<bool> hasMore{};
  shared_ptr<vector<FileDeltaResponse>> items{};

  ListFileDeltaResponse() {}

  explicit ListFileDeltaResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (cursor) {
      res["cursor"] = boost::any(*cursor);
    }
    if (hasMore) {
      res["has_more"] = boost::any(*hasMore);
    }
    if (items) {
      vector<boost::any> temp1;
      for(auto item1:*items){
        temp1.push_back(boost::any(item1.toMap()));
      }
      res["items"] = boost::any(temp1);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("cursor") != m.end() && !m["cursor"].empty()) {
      cursor = make_shared<string>(boost::any_cast<string>(m["cursor"]));
    }
    if (m.find("has_more") != m.end() && !m["has_more"].empty()) {
      hasMore = make_shared<bool>(boost::any_cast<bool>(m["has_more"]));
    }
    if (m.find("items") != m.end() && !m["items"].empty()) {
      if (typeid(vector<boost::any>).name() == m["items"].type().name()) {
        vector<FileDeltaResponse> expect1;
        for(auto item1:boost::any_cast<vector<boost::any>>(m["items"])){
          if (typeid(map<string, boost::any>).name() == item1.type().name()) {
            FileDeltaResponse model2;
            model2.fromMap(boost::any_cast<map<string, boost::any>>(item1));
            expect1.push_back(model2);
          }
        }
        items = make_shared<vector<FileDeltaResponse>>(expect1);
      }
    }
  }


  ~ListFileDeltaResponse() = default;
};
class ListFileResponse : public Darabonba::Model {
public:
  shared_ptr<vector<BaseFileResponse>> items{};
  shared_ptr<string> nextMarker{};

  ListFileResponse() {}

  explicit ListFileResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (items) {
      vector<boost::any> temp1;
      for(auto item1:*items){
        temp1.push_back(boost::any(item1.toMap()));
      }
      res["items"] = boost::any(temp1);
    }
    if (nextMarker) {
      res["next_marker"] = boost::any(*nextMarker);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("items") != m.end() && !m["items"].empty()) {
      if (typeid(vector<boost::any>).name() == m["items"].type().name()) {
        vector<BaseFileResponse> expect1;
        for(auto item1:boost::any_cast<vector<boost::any>>(m["items"])){
          if (typeid(map<string, boost::any>).name() == item1.type().name()) {
            BaseFileResponse model2;
            model2.fromMap(boost::any_cast<map<string, boost::any>>(item1));
            expect1.push_back(model2);
          }
        }
        items = make_shared<vector<BaseFileResponse>>(expect1);
      }
    }
    if (m.find("next_marker") != m.end() && !m["next_marker"].empty()) {
      nextMarker = make_shared<string>(boost::any_cast<string>(m["next_marker"]));
    }
  }


  ~ListFileResponse() = default;
};
class ListShareLinkResponse : public Darabonba::Model {
public:
  shared_ptr<vector<BaseShareLinkResponse>> items{};
  shared_ptr<string> nextMarker{};

  ListShareLinkResponse() {}

  explicit ListShareLinkResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (items) {
      vector<boost::any> temp1;
      for(auto item1:*items){
        temp1.push_back(boost::any(item1.toMap()));
      }
      res["items"] = boost::any(temp1);
    }
    if (nextMarker) {
      res["next_marker"] = boost::any(*nextMarker);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("items") != m.end() && !m["items"].empty()) {
      if (typeid(vector<boost::any>).name() == m["items"].type().name()) {
        vector<BaseShareLinkResponse> expect1;
        for(auto item1:boost::any_cast<vector<boost::any>>(m["items"])){
          if (typeid(map<string, boost::any>).name() == item1.type().name()) {
            BaseShareLinkResponse model2;
            model2.fromMap(boost::any_cast<map<string, boost::any>>(item1));
            expect1.push_back(model2);
          }
        }
        items = make_shared<vector<BaseShareLinkResponse>>(expect1);
      }
    }
    if (m.find("next_marker") != m.end() && !m["next_marker"].empty()) {
      nextMarker = make_shared<string>(boost::any_cast<string>(m["next_marker"]));
    }
  }


  ~ListShareLinkResponse() = default;
};
class ListShareResponse : public Darabonba::Model {
public:
  shared_ptr<vector<BaseShareResponse>> items{};
  shared_ptr<string> nextMarker{};

  ListShareResponse() {}

  explicit ListShareResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (items) {
      vector<boost::any> temp1;
      for(auto item1:*items){
        temp1.push_back(boost::any(item1.toMap()));
      }
      res["items"] = boost::any(temp1);
    }
    if (nextMarker) {
      res["next_marker"] = boost::any(*nextMarker);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("items") != m.end() && !m["items"].empty()) {
      if (typeid(vector<boost::any>).name() == m["items"].type().name()) {
        vector<BaseShareResponse> expect1;
        for(auto item1:boost::any_cast<vector<boost::any>>(m["items"])){
          if (typeid(map<string, boost::any>).name() == item1.type().name()) {
            BaseShareResponse model2;
            model2.fromMap(boost::any_cast<map<string, boost::any>>(item1));
            expect1.push_back(model2);
          }
        }
        items = make_shared<vector<BaseShareResponse>>(expect1);
      }
    }
    if (m.find("next_marker") != m.end() && !m["next_marker"].empty()) {
      nextMarker = make_shared<string>(boost::any_cast<string>(m["next_marker"]));
    }
  }


  ~ListShareResponse() = default;
};
class StoreFile : public Darabonba::Model {
public:
  shared_ptr<string> domainId{};
  shared_ptr<string> name{};
  shared_ptr<string> parentFilePath{};
  shared_ptr<string> storeId{};
  shared_ptr<string> type{};

  StoreFile() {}

  explicit StoreFile(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (domainId) {
      res["domain_id"] = boost::any(*domainId);
    }
    if (name) {
      res["name"] = boost::any(*name);
    }
    if (parentFilePath) {
      res["parent_file_path"] = boost::any(*parentFilePath);
    }
    if (storeId) {
      res["store_id"] = boost::any(*storeId);
    }
    if (type) {
      res["type"] = boost::any(*type);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("domain_id") != m.end() && !m["domain_id"].empty()) {
      domainId = make_shared<string>(boost::any_cast<string>(m["domain_id"]));
    }
    if (m.find("name") != m.end() && !m["name"].empty()) {
      name = make_shared<string>(boost::any_cast<string>(m["name"]));
    }
    if (m.find("parent_file_path") != m.end() && !m["parent_file_path"].empty()) {
      parentFilePath = make_shared<string>(boost::any_cast<string>(m["parent_file_path"]));
    }
    if (m.find("store_id") != m.end() && !m["store_id"].empty()) {
      storeId = make_shared<string>(boost::any_cast<string>(m["store_id"]));
    }
    if (m.find("type") != m.end() && !m["type"].empty()) {
      type = make_shared<string>(boost::any_cast<string>(m["type"]));
    }
  }


  ~StoreFile() = default;
};
class ListStoreFileResponse : public Darabonba::Model {
public:
  shared_ptr<vector<StoreFile>> items{};
  shared_ptr<string> nextMarker{};

  ListStoreFileResponse() {}

  explicit ListStoreFileResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (items) {
      vector<boost::any> temp1;
      for(auto item1:*items){
        temp1.push_back(boost::any(item1.toMap()));
      }
      res["items"] = boost::any(temp1);
    }
    if (nextMarker) {
      res["next_marker"] = boost::any(*nextMarker);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("items") != m.end() && !m["items"].empty()) {
      if (typeid(vector<boost::any>).name() == m["items"].type().name()) {
        vector<StoreFile> expect1;
        for(auto item1:boost::any_cast<vector<boost::any>>(m["items"])){
          if (typeid(map<string, boost::any>).name() == item1.type().name()) {
            StoreFile model2;
            model2.fromMap(boost::any_cast<map<string, boost::any>>(item1));
            expect1.push_back(model2);
          }
        }
        items = make_shared<vector<StoreFile>>(expect1);
      }
    }
    if (m.find("next_marker") != m.end() && !m["next_marker"].empty()) {
      nextMarker = make_shared<string>(boost::any_cast<string>(m["next_marker"]));
    }
  }


  ~ListStoreFileResponse() = default;
};
class StoreItemResponse : public Darabonba::Model {
public:
  shared_ptr<string> accelerateEndpoint{};
  shared_ptr<string> basePath{};
  shared_ptr<string> bucket{};
  shared_ptr<string> cdnEndpoint{};
  shared_ptr<string> customizedAccelerateEndpoint{};
  shared_ptr<string> customizedCdnEndpoint{};
  shared_ptr<string> customizedEndpoint{};
  shared_ptr<string> customizedInternalEndpoint{};
  shared_ptr<string> domainId{};
  shared_ptr<string> endpoint{};
  shared_ptr<string> internalEndpoint{};
  shared_ptr<string> location{};
  shared_ptr<string> ownership{};
  shared_ptr<string> policy{};
  shared_ptr<string> roleArn{};
  shared_ptr<string> storeId{};
  shared_ptr<string> type{};

  StoreItemResponse() {}

  explicit StoreItemResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!bucket) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("bucket is required.")));
    }
    if (!endpoint) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("endpoint is required.")));
    }
    if (!ownership) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("ownership is required.")));
    }
    if (!policy) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("policy is required.")));
    }
    if (!storeId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("storeId is required.")));
    }
    if (!type) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("type is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (accelerateEndpoint) {
      res["accelerate_endpoint"] = boost::any(*accelerateEndpoint);
    }
    if (basePath) {
      res["base_path"] = boost::any(*basePath);
    }
    if (bucket) {
      res["bucket"] = boost::any(*bucket);
    }
    if (cdnEndpoint) {
      res["cdn_endpoint"] = boost::any(*cdnEndpoint);
    }
    if (customizedAccelerateEndpoint) {
      res["customized_accelerate_endpoint"] = boost::any(*customizedAccelerateEndpoint);
    }
    if (customizedCdnEndpoint) {
      res["customized_cdn_endpoint"] = boost::any(*customizedCdnEndpoint);
    }
    if (customizedEndpoint) {
      res["customized_endpoint"] = boost::any(*customizedEndpoint);
    }
    if (customizedInternalEndpoint) {
      res["customized_internal_endpoint"] = boost::any(*customizedInternalEndpoint);
    }
    if (domainId) {
      res["domain_id"] = boost::any(*domainId);
    }
    if (endpoint) {
      res["endpoint"] = boost::any(*endpoint);
    }
    if (internalEndpoint) {
      res["internal_endpoint"] = boost::any(*internalEndpoint);
    }
    if (location) {
      res["location"] = boost::any(*location);
    }
    if (ownership) {
      res["ownership"] = boost::any(*ownership);
    }
    if (policy) {
      res["policy"] = boost::any(*policy);
    }
    if (roleArn) {
      res["role_arn"] = boost::any(*roleArn);
    }
    if (storeId) {
      res["store_id"] = boost::any(*storeId);
    }
    if (type) {
      res["type"] = boost::any(*type);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("accelerate_endpoint") != m.end() && !m["accelerate_endpoint"].empty()) {
      accelerateEndpoint = make_shared<string>(boost::any_cast<string>(m["accelerate_endpoint"]));
    }
    if (m.find("base_path") != m.end() && !m["base_path"].empty()) {
      basePath = make_shared<string>(boost::any_cast<string>(m["base_path"]));
    }
    if (m.find("bucket") != m.end() && !m["bucket"].empty()) {
      bucket = make_shared<string>(boost::any_cast<string>(m["bucket"]));
    }
    if (m.find("cdn_endpoint") != m.end() && !m["cdn_endpoint"].empty()) {
      cdnEndpoint = make_shared<string>(boost::any_cast<string>(m["cdn_endpoint"]));
    }
    if (m.find("customized_accelerate_endpoint") != m.end() && !m["customized_accelerate_endpoint"].empty()) {
      customizedAccelerateEndpoint = make_shared<string>(boost::any_cast<string>(m["customized_accelerate_endpoint"]));
    }
    if (m.find("customized_cdn_endpoint") != m.end() && !m["customized_cdn_endpoint"].empty()) {
      customizedCdnEndpoint = make_shared<string>(boost::any_cast<string>(m["customized_cdn_endpoint"]));
    }
    if (m.find("customized_endpoint") != m.end() && !m["customized_endpoint"].empty()) {
      customizedEndpoint = make_shared<string>(boost::any_cast<string>(m["customized_endpoint"]));
    }
    if (m.find("customized_internal_endpoint") != m.end() && !m["customized_internal_endpoint"].empty()) {
      customizedInternalEndpoint = make_shared<string>(boost::any_cast<string>(m["customized_internal_endpoint"]));
    }
    if (m.find("domain_id") != m.end() && !m["domain_id"].empty()) {
      domainId = make_shared<string>(boost::any_cast<string>(m["domain_id"]));
    }
    if (m.find("endpoint") != m.end() && !m["endpoint"].empty()) {
      endpoint = make_shared<string>(boost::any_cast<string>(m["endpoint"]));
    }
    if (m.find("internal_endpoint") != m.end() && !m["internal_endpoint"].empty()) {
      internalEndpoint = make_shared<string>(boost::any_cast<string>(m["internal_endpoint"]));
    }
    if (m.find("location") != m.end() && !m["location"].empty()) {
      location = make_shared<string>(boost::any_cast<string>(m["location"]));
    }
    if (m.find("ownership") != m.end() && !m["ownership"].empty()) {
      ownership = make_shared<string>(boost::any_cast<string>(m["ownership"]));
    }
    if (m.find("policy") != m.end() && !m["policy"].empty()) {
      policy = make_shared<string>(boost::any_cast<string>(m["policy"]));
    }
    if (m.find("role_arn") != m.end() && !m["role_arn"].empty()) {
      roleArn = make_shared<string>(boost::any_cast<string>(m["role_arn"]));
    }
    if (m.find("store_id") != m.end() && !m["store_id"].empty()) {
      storeId = make_shared<string>(boost::any_cast<string>(m["store_id"]));
    }
    if (m.find("type") != m.end() && !m["type"].empty()) {
      type = make_shared<string>(boost::any_cast<string>(m["type"]));
    }
  }


  ~StoreItemResponse() = default;
};
class ListStoreResponse : public Darabonba::Model {
public:
  shared_ptr<vector<StoreItemResponse>> items{};

  ListStoreResponse() {}

  explicit ListStoreResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (items) {
      vector<boost::any> temp1;
      for(auto item1:*items){
        temp1.push_back(boost::any(item1.toMap()));
      }
      res["items"] = boost::any(temp1);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("items") != m.end() && !m["items"].empty()) {
      if (typeid(vector<boost::any>).name() == m["items"].type().name()) {
        vector<StoreItemResponse> expect1;
        for(auto item1:boost::any_cast<vector<boost::any>>(m["items"])){
          if (typeid(map<string, boost::any>).name() == item1.type().name()) {
            StoreItemResponse model2;
            model2.fromMap(boost::any_cast<map<string, boost::any>>(item1));
            expect1.push_back(model2);
          }
        }
        items = make_shared<vector<StoreItemResponse>>(expect1);
      }
    }
  }


  ~ListStoreResponse() = default;
};
class ListUploadedPartResponse : public Darabonba::Model {
public:
  shared_ptr<string> fileId{};
  shared_ptr<string> nextPartNumberMarker{};
  shared_ptr<string> uploadId{};
  shared_ptr<vector<UploadPartInfo>> uploadedParts{};

  ListUploadedPartResponse() {}

  explicit ListUploadedPartResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    Darabonba::Model::validateMaxLength("fileId", fileId, 50);
    Darabonba::Model::validateMinLength("fileId", fileId, 40);
    Darabonba::Model::validatePattern("fileId", fileId, "[a-z0-9]{1,50}");
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (fileId) {
      res["file_id"] = boost::any(*fileId);
    }
    if (nextPartNumberMarker) {
      res["next_part_number_marker"] = boost::any(*nextPartNumberMarker);
    }
    if (uploadId) {
      res["upload_id"] = boost::any(*uploadId);
    }
    if (uploadedParts) {
      vector<boost::any> temp1;
      for(auto item1:*uploadedParts){
        temp1.push_back(boost::any(item1.toMap()));
      }
      res["uploaded_parts"] = boost::any(temp1);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("file_id") != m.end() && !m["file_id"].empty()) {
      fileId = make_shared<string>(boost::any_cast<string>(m["file_id"]));
    }
    if (m.find("next_part_number_marker") != m.end() && !m["next_part_number_marker"].empty()) {
      nextPartNumberMarker = make_shared<string>(boost::any_cast<string>(m["next_part_number_marker"]));
    }
    if (m.find("upload_id") != m.end() && !m["upload_id"].empty()) {
      uploadId = make_shared<string>(boost::any_cast<string>(m["upload_id"]));
    }
    if (m.find("uploaded_parts") != m.end() && !m["uploaded_parts"].empty()) {
      if (typeid(vector<boost::any>).name() == m["uploaded_parts"].type().name()) {
        vector<UploadPartInfo> expect1;
        for(auto item1:boost::any_cast<vector<boost::any>>(m["uploaded_parts"])){
          if (typeid(map<string, boost::any>).name() == item1.type().name()) {
            UploadPartInfo model2;
            model2.fromMap(boost::any_cast<map<string, boost::any>>(item1));
            expect1.push_back(model2);
          }
        }
        uploadedParts = make_shared<vector<UploadPartInfo>>(expect1);
      }
    }
  }


  ~ListUploadedPartResponse() = default;
};
class LoginByCodeRequest : public Darabonba::Model {
public:
  shared_ptr<string> accessToken{};
  shared_ptr<string> appId{};
  shared_ptr<string> authCode{};
  shared_ptr<string> type{};

  LoginByCodeRequest() {}

  explicit LoginByCodeRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!appId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("appId is required.")));
    }
    if (!type) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("type is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (accessToken) {
      res["access_token"] = boost::any(*accessToken);
    }
    if (appId) {
      res["app_id"] = boost::any(*appId);
    }
    if (authCode) {
      res["auth_code"] = boost::any(*authCode);
    }
    if (type) {
      res["type"] = boost::any(*type);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("access_token") != m.end() && !m["access_token"].empty()) {
      accessToken = make_shared<string>(boost::any_cast<string>(m["access_token"]));
    }
    if (m.find("app_id") != m.end() && !m["app_id"].empty()) {
      appId = make_shared<string>(boost::any_cast<string>(m["app_id"]));
    }
    if (m.find("auth_code") != m.end() && !m["auth_code"].empty()) {
      authCode = make_shared<string>(boost::any_cast<string>(m["auth_code"]));
    }
    if (m.find("type") != m.end() && !m["type"].empty()) {
      type = make_shared<string>(boost::any_cast<string>(m["type"]));
    }
  }


  ~LoginByCodeRequest() = default;
};
class MobileCheckExistRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<string> appId{};
  shared_ptr<string> phoneNumber{};
  shared_ptr<string> phoneRegion{};

  MobileCheckExistRequest() {}

  explicit MobileCheckExistRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!appId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("appId is required.")));
    }
    if (!phoneNumber) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("phoneNumber is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (appId) {
      res["app_id"] = boost::any(*appId);
    }
    if (phoneNumber) {
      res["phone_number"] = boost::any(*phoneNumber);
    }
    if (phoneRegion) {
      res["phone_region"] = boost::any(*phoneRegion);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("app_id") != m.end() && !m["app_id"].empty()) {
      appId = make_shared<string>(boost::any_cast<string>(m["app_id"]));
    }
    if (m.find("phone_number") != m.end() && !m["phone_number"].empty()) {
      phoneNumber = make_shared<string>(boost::any_cast<string>(m["phone_number"]));
    }
    if (m.find("phone_region") != m.end() && !m["phone_region"].empty()) {
      phoneRegion = make_shared<string>(boost::any_cast<string>(m["phone_region"]));
    }
  }


  ~MobileCheckExistRequest() = default;
};
class MobileLoginRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<string> appId{};
  shared_ptr<bool> autoRegister{};
  shared_ptr<string> captchaId{};
  shared_ptr<string> captchaText{};
  shared_ptr<string> encryptedKey{};
  shared_ptr<string> password{};
  shared_ptr<string> phoneNumber{};
  shared_ptr<string> phoneRegion{};
  shared_ptr<string> smsCode{};
  shared_ptr<string> smsCodeId{};

  MobileLoginRequest() {}

  explicit MobileLoginRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!appId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("appId is required.")));
    }
    if (!phoneNumber) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("phoneNumber is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (appId) {
      res["app_id"] = boost::any(*appId);
    }
    if (autoRegister) {
      res["auto_register"] = boost::any(*autoRegister);
    }
    if (captchaId) {
      res["captcha_id"] = boost::any(*captchaId);
    }
    if (captchaText) {
      res["captcha_text"] = boost::any(*captchaText);
    }
    if (encryptedKey) {
      res["encrypted_key"] = boost::any(*encryptedKey);
    }
    if (password) {
      res["password"] = boost::any(*password);
    }
    if (phoneNumber) {
      res["phone_number"] = boost::any(*phoneNumber);
    }
    if (phoneRegion) {
      res["phone_region"] = boost::any(*phoneRegion);
    }
    if (smsCode) {
      res["sms_code"] = boost::any(*smsCode);
    }
    if (smsCodeId) {
      res["sms_code_id"] = boost::any(*smsCodeId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("app_id") != m.end() && !m["app_id"].empty()) {
      appId = make_shared<string>(boost::any_cast<string>(m["app_id"]));
    }
    if (m.find("auto_register") != m.end() && !m["auto_register"].empty()) {
      autoRegister = make_shared<bool>(boost::any_cast<bool>(m["auto_register"]));
    }
    if (m.find("captcha_id") != m.end() && !m["captcha_id"].empty()) {
      captchaId = make_shared<string>(boost::any_cast<string>(m["captcha_id"]));
    }
    if (m.find("captcha_text") != m.end() && !m["captcha_text"].empty()) {
      captchaText = make_shared<string>(boost::any_cast<string>(m["captcha_text"]));
    }
    if (m.find("encrypted_key") != m.end() && !m["encrypted_key"].empty()) {
      encryptedKey = make_shared<string>(boost::any_cast<string>(m["encrypted_key"]));
    }
    if (m.find("password") != m.end() && !m["password"].empty()) {
      password = make_shared<string>(boost::any_cast<string>(m["password"]));
    }
    if (m.find("phone_number") != m.end() && !m["phone_number"].empty()) {
      phoneNumber = make_shared<string>(boost::any_cast<string>(m["phone_number"]));
    }
    if (m.find("phone_region") != m.end() && !m["phone_region"].empty()) {
      phoneRegion = make_shared<string>(boost::any_cast<string>(m["phone_region"]));
    }
    if (m.find("sms_code") != m.end() && !m["sms_code"].empty()) {
      smsCode = make_shared<string>(boost::any_cast<string>(m["sms_code"]));
    }
    if (m.find("sms_code_id") != m.end() && !m["sms_code_id"].empty()) {
      smsCodeId = make_shared<string>(boost::any_cast<string>(m["sms_code_id"]));
    }
  }


  ~MobileLoginRequest() = default;
};
class MobileRegisterRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<string> appId{};
  shared_ptr<string> phoneNumber{};
  shared_ptr<string> phoneRegion{};
  shared_ptr<string> smsCode{};
  shared_ptr<string> smsCodeId{};

  MobileRegisterRequest() {}

  explicit MobileRegisterRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!appId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("appId is required.")));
    }
    if (!phoneNumber) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("phoneNumber is required.")));
    }
    if (!smsCode) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("smsCode is required.")));
    }
    if (!smsCodeId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("smsCodeId is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (appId) {
      res["app_id"] = boost::any(*appId);
    }
    if (phoneNumber) {
      res["phone_number"] = boost::any(*phoneNumber);
    }
    if (phoneRegion) {
      res["phone_region"] = boost::any(*phoneRegion);
    }
    if (smsCode) {
      res["sms_code"] = boost::any(*smsCode);
    }
    if (smsCodeId) {
      res["sms_code_id"] = boost::any(*smsCodeId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("app_id") != m.end() && !m["app_id"].empty()) {
      appId = make_shared<string>(boost::any_cast<string>(m["app_id"]));
    }
    if (m.find("phone_number") != m.end() && !m["phone_number"].empty()) {
      phoneNumber = make_shared<string>(boost::any_cast<string>(m["phone_number"]));
    }
    if (m.find("phone_region") != m.end() && !m["phone_region"].empty()) {
      phoneRegion = make_shared<string>(boost::any_cast<string>(m["phone_region"]));
    }
    if (m.find("sms_code") != m.end() && !m["sms_code"].empty()) {
      smsCode = make_shared<string>(boost::any_cast<string>(m["sms_code"]));
    }
    if (m.find("sms_code_id") != m.end() && !m["sms_code_id"].empty()) {
      smsCodeId = make_shared<string>(boost::any_cast<string>(m["sms_code_id"]));
    }
  }


  ~MobileRegisterRequest() = default;
};
class MobileSendSmsCodeRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<string> appId{};
  shared_ptr<string> captchaId{};
  shared_ptr<string> captchaText{};
  shared_ptr<string> phoneNumber{};
  shared_ptr<string> phoneRegion{};
  shared_ptr<string> type{};

  MobileSendSmsCodeRequest() {}

  explicit MobileSendSmsCodeRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!appId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("appId is required.")));
    }
    if (!phoneNumber) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("phoneNumber is required.")));
    }
    if (!type) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("type is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (appId) {
      res["app_id"] = boost::any(*appId);
    }
    if (captchaId) {
      res["captcha_id"] = boost::any(*captchaId);
    }
    if (captchaText) {
      res["captcha_text"] = boost::any(*captchaText);
    }
    if (phoneNumber) {
      res["phone_number"] = boost::any(*phoneNumber);
    }
    if (phoneRegion) {
      res["phone_region"] = boost::any(*phoneRegion);
    }
    if (type) {
      res["type"] = boost::any(*type);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("app_id") != m.end() && !m["app_id"].empty()) {
      appId = make_shared<string>(boost::any_cast<string>(m["app_id"]));
    }
    if (m.find("captcha_id") != m.end() && !m["captcha_id"].empty()) {
      captchaId = make_shared<string>(boost::any_cast<string>(m["captcha_id"]));
    }
    if (m.find("captcha_text") != m.end() && !m["captcha_text"].empty()) {
      captchaText = make_shared<string>(boost::any_cast<string>(m["captcha_text"]));
    }
    if (m.find("phone_number") != m.end() && !m["phone_number"].empty()) {
      phoneNumber = make_shared<string>(boost::any_cast<string>(m["phone_number"]));
    }
    if (m.find("phone_region") != m.end() && !m["phone_region"].empty()) {
      phoneRegion = make_shared<string>(boost::any_cast<string>(m["phone_region"]));
    }
    if (m.find("type") != m.end() && !m["type"].empty()) {
      type = make_shared<string>(boost::any_cast<string>(m["type"]));
    }
  }


  ~MobileSendSmsCodeRequest() = default;
};
class MoveFileResponse : public Darabonba::Model {
public:
  shared_ptr<string> asyncTaskId{};
  shared_ptr<string> domainId{};
  shared_ptr<string> driveId{};
  shared_ptr<string> fileId{};

  MoveFileResponse() {}

  explicit MoveFileResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    Darabonba::Model::validatePattern("domainId", domainId, "[a-z0-9A-Z]+");
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    Darabonba::Model::validateMaxLength("fileId", fileId, 50);
    Darabonba::Model::validateMinLength("fileId", fileId, 40);
    Darabonba::Model::validatePattern("fileId", fileId, "[a-z0-9]{1,50}");
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (asyncTaskId) {
      res["async_task_id"] = boost::any(*asyncTaskId);
    }
    if (domainId) {
      res["domain_id"] = boost::any(*domainId);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (fileId) {
      res["file_id"] = boost::any(*fileId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("async_task_id") != m.end() && !m["async_task_id"].empty()) {
      asyncTaskId = make_shared<string>(boost::any_cast<string>(m["async_task_id"]));
    }
    if (m.find("domain_id") != m.end() && !m["domain_id"].empty()) {
      domainId = make_shared<string>(boost::any_cast<string>(m["domain_id"]));
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("file_id") != m.end() && !m["file_id"].empty()) {
      fileId = make_shared<string>(boost::any_cast<string>(m["file_id"]));
    }
  }


  ~MoveFileResponse() = default;
};
class OSSCompleteFileResponse : public Darabonba::Model {
public:
  shared_ptr<string> contentHash{};
  shared_ptr<string> contentHashName{};
  shared_ptr<string> contentType{};
  shared_ptr<string> crc{};
  shared_ptr<string> crc64Hash{};
  shared_ptr<string> createdAt{};
  shared_ptr<string> description{};
  shared_ptr<string> domainId{};
  shared_ptr<string> downloadUrl{};
  shared_ptr<string> driveId{};
  shared_ptr<string> fileExtension{};
  shared_ptr<string> filePath{};
  shared_ptr<string> name{};
  shared_ptr<string> parentFilePath{};
  shared_ptr<string> shareId{};
  shared_ptr<long> size{};
  shared_ptr<string> status{};
  shared_ptr<string> thumbnail{};
  shared_ptr<string> trashedAt{};
  shared_ptr<string> type{};
  shared_ptr<string> updatedAt{};
  shared_ptr<string> uploadId{};
  shared_ptr<string> url{};

  OSSCompleteFileResponse() {}

  explicit OSSCompleteFileResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    Darabonba::Model::validatePattern("domainId", domainId, "[a-z0-9A-Z]+");
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    if (!name) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("name is required.")));
    }
    Darabonba::Model::validatePattern("name", name, "[a-zA-Z0-9.-]{1,1000}");
    Darabonba::Model::validateMaxLength("parentFilePath", parentFilePath, 50);
    Darabonba::Model::validateMinLength("parentFilePath", parentFilePath, 40);
    Darabonba::Model::validatePattern("parentFilePath", parentFilePath, "[a-z0-9]{1,50}");
    Darabonba::Model::validatePattern("shareId", shareId, "[0-9]+");
    if (size && *size > 53687091200) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("size is required.")));
    }
    if (size && *size < 0) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("size is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (contentHash) {
      res["content_hash"] = boost::any(*contentHash);
    }
    if (contentHashName) {
      res["content_hash_name"] = boost::any(*contentHashName);
    }
    if (contentType) {
      res["content_type"] = boost::any(*contentType);
    }
    if (crc) {
      res["crc"] = boost::any(*crc);
    }
    if (crc64Hash) {
      res["crc64_hash"] = boost::any(*crc64Hash);
    }
    if (createdAt) {
      res["created_at"] = boost::any(*createdAt);
    }
    if (description) {
      res["description"] = boost::any(*description);
    }
    if (domainId) {
      res["domain_id"] = boost::any(*domainId);
    }
    if (downloadUrl) {
      res["download_url"] = boost::any(*downloadUrl);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (fileExtension) {
      res["file_extension"] = boost::any(*fileExtension);
    }
    if (filePath) {
      res["file_path"] = boost::any(*filePath);
    }
    if (name) {
      res["name"] = boost::any(*name);
    }
    if (parentFilePath) {
      res["parent_file_path"] = boost::any(*parentFilePath);
    }
    if (shareId) {
      res["share_id"] = boost::any(*shareId);
    }
    if (size) {
      res["size"] = boost::any(*size);
    }
    if (status) {
      res["status"] = boost::any(*status);
    }
    if (thumbnail) {
      res["thumbnail"] = boost::any(*thumbnail);
    }
    if (trashedAt) {
      res["trashed_at"] = boost::any(*trashedAt);
    }
    if (type) {
      res["type"] = boost::any(*type);
    }
    if (updatedAt) {
      res["updated_at"] = boost::any(*updatedAt);
    }
    if (uploadId) {
      res["upload_id"] = boost::any(*uploadId);
    }
    if (url) {
      res["url"] = boost::any(*url);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("content_hash") != m.end() && !m["content_hash"].empty()) {
      contentHash = make_shared<string>(boost::any_cast<string>(m["content_hash"]));
    }
    if (m.find("content_hash_name") != m.end() && !m["content_hash_name"].empty()) {
      contentHashName = make_shared<string>(boost::any_cast<string>(m["content_hash_name"]));
    }
    if (m.find("content_type") != m.end() && !m["content_type"].empty()) {
      contentType = make_shared<string>(boost::any_cast<string>(m["content_type"]));
    }
    if (m.find("crc") != m.end() && !m["crc"].empty()) {
      crc = make_shared<string>(boost::any_cast<string>(m["crc"]));
    }
    if (m.find("crc64_hash") != m.end() && !m["crc64_hash"].empty()) {
      crc64Hash = make_shared<string>(boost::any_cast<string>(m["crc64_hash"]));
    }
    if (m.find("created_at") != m.end() && !m["created_at"].empty()) {
      createdAt = make_shared<string>(boost::any_cast<string>(m["created_at"]));
    }
    if (m.find("description") != m.end() && !m["description"].empty()) {
      description = make_shared<string>(boost::any_cast<string>(m["description"]));
    }
    if (m.find("domain_id") != m.end() && !m["domain_id"].empty()) {
      domainId = make_shared<string>(boost::any_cast<string>(m["domain_id"]));
    }
    if (m.find("download_url") != m.end() && !m["download_url"].empty()) {
      downloadUrl = make_shared<string>(boost::any_cast<string>(m["download_url"]));
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("file_extension") != m.end() && !m["file_extension"].empty()) {
      fileExtension = make_shared<string>(boost::any_cast<string>(m["file_extension"]));
    }
    if (m.find("file_path") != m.end() && !m["file_path"].empty()) {
      filePath = make_shared<string>(boost::any_cast<string>(m["file_path"]));
    }
    if (m.find("name") != m.end() && !m["name"].empty()) {
      name = make_shared<string>(boost::any_cast<string>(m["name"]));
    }
    if (m.find("parent_file_path") != m.end() && !m["parent_file_path"].empty()) {
      parentFilePath = make_shared<string>(boost::any_cast<string>(m["parent_file_path"]));
    }
    if (m.find("share_id") != m.end() && !m["share_id"].empty()) {
      shareId = make_shared<string>(boost::any_cast<string>(m["share_id"]));
    }
    if (m.find("size") != m.end() && !m["size"].empty()) {
      size = make_shared<long>(boost::any_cast<long>(m["size"]));
    }
    if (m.find("status") != m.end() && !m["status"].empty()) {
      status = make_shared<string>(boost::any_cast<string>(m["status"]));
    }
    if (m.find("thumbnail") != m.end() && !m["thumbnail"].empty()) {
      thumbnail = make_shared<string>(boost::any_cast<string>(m["thumbnail"]));
    }
    if (m.find("trashed_at") != m.end() && !m["trashed_at"].empty()) {
      trashedAt = make_shared<string>(boost::any_cast<string>(m["trashed_at"]));
    }
    if (m.find("type") != m.end() && !m["type"].empty()) {
      type = make_shared<string>(boost::any_cast<string>(m["type"]));
    }
    if (m.find("updated_at") != m.end() && !m["updated_at"].empty()) {
      updatedAt = make_shared<string>(boost::any_cast<string>(m["updated_at"]));
    }
    if (m.find("upload_id") != m.end() && !m["upload_id"].empty()) {
      uploadId = make_shared<string>(boost::any_cast<string>(m["upload_id"]));
    }
    if (m.find("url") != m.end() && !m["url"].empty()) {
      url = make_shared<string>(boost::any_cast<string>(m["url"]));
    }
  }


  ~OSSCompleteFileResponse() = default;
};
class OSSCopyFileResponse : public Darabonba::Model {
public:
  shared_ptr<string> asyncTaskId{};
  shared_ptr<string> domainId{};
  shared_ptr<string> driveId{};
  shared_ptr<string> filePath{};
  shared_ptr<string> shareId{};

  OSSCopyFileResponse() {}

  explicit OSSCopyFileResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    Darabonba::Model::validatePattern("domainId", domainId, "[a-z0-9A-Z-]+");
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    Darabonba::Model::validatePattern("shareId", shareId, "[a-z0-9A-Z]+");
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (asyncTaskId) {
      res["async_task_id"] = boost::any(*asyncTaskId);
    }
    if (domainId) {
      res["domain_id"] = boost::any(*domainId);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (filePath) {
      res["file_path"] = boost::any(*filePath);
    }
    if (shareId) {
      res["share_id"] = boost::any(*shareId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("async_task_id") != m.end() && !m["async_task_id"].empty()) {
      asyncTaskId = make_shared<string>(boost::any_cast<string>(m["async_task_id"]));
    }
    if (m.find("domain_id") != m.end() && !m["domain_id"].empty()) {
      domainId = make_shared<string>(boost::any_cast<string>(m["domain_id"]));
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("file_path") != m.end() && !m["file_path"].empty()) {
      filePath = make_shared<string>(boost::any_cast<string>(m["file_path"]));
    }
    if (m.find("share_id") != m.end() && !m["share_id"].empty()) {
      shareId = make_shared<string>(boost::any_cast<string>(m["share_id"]));
    }
  }


  ~OSSCopyFileResponse() = default;
};
class OSSCreateFileResponse : public Darabonba::Model {
public:
  shared_ptr<string> domainId{};
  shared_ptr<string> driveId{};
  shared_ptr<string> filePath{};
  shared_ptr<vector<UploadPartInfo>> partInfoList{};
  shared_ptr<string> shareId{};
  shared_ptr<string> type{};
  shared_ptr<string> uploadId{};

  OSSCreateFileResponse() {}

  explicit OSSCreateFileResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    Darabonba::Model::validateMaxLength("domainId", domainId, 50);
    Darabonba::Model::validateMinLength("domainId", domainId, 40);
    Darabonba::Model::validatePattern("domainId", domainId, "[a-z0-9]{1,50}");
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    Darabonba::Model::validatePattern("shareId", shareId, "[0-9]+");
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (domainId) {
      res["domain_id"] = boost::any(*domainId);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (filePath) {
      res["file_path"] = boost::any(*filePath);
    }
    if (partInfoList) {
      vector<boost::any> temp1;
      for(auto item1:*partInfoList){
        temp1.push_back(boost::any(item1.toMap()));
      }
      res["part_info_list"] = boost::any(temp1);
    }
    if (shareId) {
      res["share_id"] = boost::any(*shareId);
    }
    if (type) {
      res["type"] = boost::any(*type);
    }
    if (uploadId) {
      res["upload_id"] = boost::any(*uploadId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("domain_id") != m.end() && !m["domain_id"].empty()) {
      domainId = make_shared<string>(boost::any_cast<string>(m["domain_id"]));
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("file_path") != m.end() && !m["file_path"].empty()) {
      filePath = make_shared<string>(boost::any_cast<string>(m["file_path"]));
    }
    if (m.find("part_info_list") != m.end() && !m["part_info_list"].empty()) {
      if (typeid(vector<boost::any>).name() == m["part_info_list"].type().name()) {
        vector<UploadPartInfo> expect1;
        for(auto item1:boost::any_cast<vector<boost::any>>(m["part_info_list"])){
          if (typeid(map<string, boost::any>).name() == item1.type().name()) {
            UploadPartInfo model2;
            model2.fromMap(boost::any_cast<map<string, boost::any>>(item1));
            expect1.push_back(model2);
          }
        }
        partInfoList = make_shared<vector<UploadPartInfo>>(expect1);
      }
    }
    if (m.find("share_id") != m.end() && !m["share_id"].empty()) {
      shareId = make_shared<string>(boost::any_cast<string>(m["share_id"]));
    }
    if (m.find("type") != m.end() && !m["type"].empty()) {
      type = make_shared<string>(boost::any_cast<string>(m["type"]));
    }
    if (m.find("upload_id") != m.end() && !m["upload_id"].empty()) {
      uploadId = make_shared<string>(boost::any_cast<string>(m["upload_id"]));
    }
  }


  ~OSSCreateFileResponse() = default;
};
class OSSDeleteFileResponse : public Darabonba::Model {
public:
  shared_ptr<string> asyncTaskId{};
  shared_ptr<string> domainId{};
  shared_ptr<string> driveId{};
  shared_ptr<string> filePath{};
  shared_ptr<string> shareId{};

  OSSDeleteFileResponse() {}

  explicit OSSDeleteFileResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    Darabonba::Model::validatePattern("domainId", domainId, "[a-z0-9A-Z]+");
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    Darabonba::Model::validatePattern("shareId", shareId, "[a-z0-9A-Z]+");
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (asyncTaskId) {
      res["async_task_id"] = boost::any(*asyncTaskId);
    }
    if (domainId) {
      res["domain_id"] = boost::any(*domainId);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (filePath) {
      res["file_path"] = boost::any(*filePath);
    }
    if (shareId) {
      res["share_id"] = boost::any(*shareId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("async_task_id") != m.end() && !m["async_task_id"].empty()) {
      asyncTaskId = make_shared<string>(boost::any_cast<string>(m["async_task_id"]));
    }
    if (m.find("domain_id") != m.end() && !m["domain_id"].empty()) {
      domainId = make_shared<string>(boost::any_cast<string>(m["domain_id"]));
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("file_path") != m.end() && !m["file_path"].empty()) {
      filePath = make_shared<string>(boost::any_cast<string>(m["file_path"]));
    }
    if (m.find("share_id") != m.end() && !m["share_id"].empty()) {
      shareId = make_shared<string>(boost::any_cast<string>(m["share_id"]));
    }
  }


  ~OSSDeleteFileResponse() = default;
};
class OSSDeleteFilesResponse : public Darabonba::Model {
public:
  shared_ptr<vector<string>> deletedFileIdList{};
  shared_ptr<string> domainId{};
  shared_ptr<string> driveId{};
  shared_ptr<string> shareId{};

  OSSDeleteFilesResponse() {}

  explicit OSSDeleteFilesResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    Darabonba::Model::validatePattern("domainId", domainId, "[a-z0-9A-Z]+");
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    Darabonba::Model::validatePattern("shareId", shareId, "[0-9]+");
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (deletedFileIdList) {
      res["deleted_file_id_list"] = boost::any(*deletedFileIdList);
    }
    if (domainId) {
      res["domain_id"] = boost::any(*domainId);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (shareId) {
      res["share_id"] = boost::any(*shareId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("deleted_file_id_list") != m.end() && !m["deleted_file_id_list"].empty()) {
      vector<string> toVec1;
      if (typeid(vector<boost::any>).name() == m["deleted_file_id_list"].type().name()) {
        vector<boost::any> vec1 = boost::any_cast<vector<boost::any>>(m["deleted_file_id_list"]);
        for (auto item:vec1) {
           toVec1.push_back(boost::any_cast<string>(item));
        }
      }
      deletedFileIdList = make_shared<vector<string>>(toVec1);
    }
    if (m.find("domain_id") != m.end() && !m["domain_id"].empty()) {
      domainId = make_shared<string>(boost::any_cast<string>(m["domain_id"]));
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("share_id") != m.end() && !m["share_id"].empty()) {
      shareId = make_shared<string>(boost::any_cast<string>(m["share_id"]));
    }
  }


  ~OSSDeleteFilesResponse() = default;
};
class OSSGetDownloadUrlResponse : public Darabonba::Model {
public:
  shared_ptr<string> expiration{};
  shared_ptr<string> method{};
  shared_ptr<string> url{};

  OSSGetDownloadUrlResponse() {}

  explicit OSSGetDownloadUrlResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (expiration) {
      res["expiration"] = boost::any(*expiration);
    }
    if (method) {
      res["method"] = boost::any(*method);
    }
    if (url) {
      res["url"] = boost::any(*url);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("expiration") != m.end() && !m["expiration"].empty()) {
      expiration = make_shared<string>(boost::any_cast<string>(m["expiration"]));
    }
    if (m.find("method") != m.end() && !m["method"].empty()) {
      method = make_shared<string>(boost::any_cast<string>(m["method"]));
    }
    if (m.find("url") != m.end() && !m["url"].empty()) {
      url = make_shared<string>(boost::any_cast<string>(m["url"]));
    }
  }


  ~OSSGetDownloadUrlResponse() = default;
};
class OSSGetFileResponse : public Darabonba::Model {
public:
  shared_ptr<string> contentHash{};
  shared_ptr<string> contentHashName{};
  shared_ptr<string> contentType{};
  shared_ptr<string> crc64Hash{};
  shared_ptr<string> createdAt{};
  shared_ptr<string> description{};
  shared_ptr<string> domainId{};
  shared_ptr<string> downloadUrl{};
  shared_ptr<string> driveId{};
  shared_ptr<string> fileExtension{};
  shared_ptr<string> filePath{};
  shared_ptr<string> name{};
  shared_ptr<string> parentFilePath{};
  shared_ptr<string> shareId{};
  shared_ptr<long> size{};
  shared_ptr<string> status{};
  shared_ptr<string> thumbnail{};
  shared_ptr<string> trashedAt{};
  shared_ptr<string> type{};
  shared_ptr<string> updatedAt{};
  shared_ptr<string> uploadId{};
  shared_ptr<string> url{};

  OSSGetFileResponse() {}

  explicit OSSGetFileResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    Darabonba::Model::validatePattern("domainId", domainId, "[a-z0-9A-Z]+");
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    if (!name) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("name is required.")));
    }
    Darabonba::Model::validatePattern("name", name, "[a-zA-Z0-9.-]{1,1000}");
    Darabonba::Model::validateMaxLength("parentFilePath", parentFilePath, 50);
    Darabonba::Model::validateMinLength("parentFilePath", parentFilePath, 40);
    Darabonba::Model::validatePattern("parentFilePath", parentFilePath, "[a-z0-9]{1,50}");
    Darabonba::Model::validatePattern("shareId", shareId, "[0-9]+");
    if (size && *size > 53687091200) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("size is required.")));
    }
    if (size && *size < 0) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("size is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (contentHash) {
      res["content_hash"] = boost::any(*contentHash);
    }
    if (contentHashName) {
      res["content_hash_name"] = boost::any(*contentHashName);
    }
    if (contentType) {
      res["content_type"] = boost::any(*contentType);
    }
    if (crc64Hash) {
      res["crc64_hash"] = boost::any(*crc64Hash);
    }
    if (createdAt) {
      res["created_at"] = boost::any(*createdAt);
    }
    if (description) {
      res["description"] = boost::any(*description);
    }
    if (domainId) {
      res["domain_id"] = boost::any(*domainId);
    }
    if (downloadUrl) {
      res["download_url"] = boost::any(*downloadUrl);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (fileExtension) {
      res["file_extension"] = boost::any(*fileExtension);
    }
    if (filePath) {
      res["file_path"] = boost::any(*filePath);
    }
    if (name) {
      res["name"] = boost::any(*name);
    }
    if (parentFilePath) {
      res["parent_file_path"] = boost::any(*parentFilePath);
    }
    if (shareId) {
      res["share_id"] = boost::any(*shareId);
    }
    if (size) {
      res["size"] = boost::any(*size);
    }
    if (status) {
      res["status"] = boost::any(*status);
    }
    if (thumbnail) {
      res["thumbnail"] = boost::any(*thumbnail);
    }
    if (trashedAt) {
      res["trashed_at"] = boost::any(*trashedAt);
    }
    if (type) {
      res["type"] = boost::any(*type);
    }
    if (updatedAt) {
      res["updated_at"] = boost::any(*updatedAt);
    }
    if (uploadId) {
      res["upload_id"] = boost::any(*uploadId);
    }
    if (url) {
      res["url"] = boost::any(*url);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("content_hash") != m.end() && !m["content_hash"].empty()) {
      contentHash = make_shared<string>(boost::any_cast<string>(m["content_hash"]));
    }
    if (m.find("content_hash_name") != m.end() && !m["content_hash_name"].empty()) {
      contentHashName = make_shared<string>(boost::any_cast<string>(m["content_hash_name"]));
    }
    if (m.find("content_type") != m.end() && !m["content_type"].empty()) {
      contentType = make_shared<string>(boost::any_cast<string>(m["content_type"]));
    }
    if (m.find("crc64_hash") != m.end() && !m["crc64_hash"].empty()) {
      crc64Hash = make_shared<string>(boost::any_cast<string>(m["crc64_hash"]));
    }
    if (m.find("created_at") != m.end() && !m["created_at"].empty()) {
      createdAt = make_shared<string>(boost::any_cast<string>(m["created_at"]));
    }
    if (m.find("description") != m.end() && !m["description"].empty()) {
      description = make_shared<string>(boost::any_cast<string>(m["description"]));
    }
    if (m.find("domain_id") != m.end() && !m["domain_id"].empty()) {
      domainId = make_shared<string>(boost::any_cast<string>(m["domain_id"]));
    }
    if (m.find("download_url") != m.end() && !m["download_url"].empty()) {
      downloadUrl = make_shared<string>(boost::any_cast<string>(m["download_url"]));
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("file_extension") != m.end() && !m["file_extension"].empty()) {
      fileExtension = make_shared<string>(boost::any_cast<string>(m["file_extension"]));
    }
    if (m.find("file_path") != m.end() && !m["file_path"].empty()) {
      filePath = make_shared<string>(boost::any_cast<string>(m["file_path"]));
    }
    if (m.find("name") != m.end() && !m["name"].empty()) {
      name = make_shared<string>(boost::any_cast<string>(m["name"]));
    }
    if (m.find("parent_file_path") != m.end() && !m["parent_file_path"].empty()) {
      parentFilePath = make_shared<string>(boost::any_cast<string>(m["parent_file_path"]));
    }
    if (m.find("share_id") != m.end() && !m["share_id"].empty()) {
      shareId = make_shared<string>(boost::any_cast<string>(m["share_id"]));
    }
    if (m.find("size") != m.end() && !m["size"].empty()) {
      size = make_shared<long>(boost::any_cast<long>(m["size"]));
    }
    if (m.find("status") != m.end() && !m["status"].empty()) {
      status = make_shared<string>(boost::any_cast<string>(m["status"]));
    }
    if (m.find("thumbnail") != m.end() && !m["thumbnail"].empty()) {
      thumbnail = make_shared<string>(boost::any_cast<string>(m["thumbnail"]));
    }
    if (m.find("trashed_at") != m.end() && !m["trashed_at"].empty()) {
      trashedAt = make_shared<string>(boost::any_cast<string>(m["trashed_at"]));
    }
    if (m.find("type") != m.end() && !m["type"].empty()) {
      type = make_shared<string>(boost::any_cast<string>(m["type"]));
    }
    if (m.find("updated_at") != m.end() && !m["updated_at"].empty()) {
      updatedAt = make_shared<string>(boost::any_cast<string>(m["updated_at"]));
    }
    if (m.find("upload_id") != m.end() && !m["upload_id"].empty()) {
      uploadId = make_shared<string>(boost::any_cast<string>(m["upload_id"]));
    }
    if (m.find("url") != m.end() && !m["url"].empty()) {
      url = make_shared<string>(boost::any_cast<string>(m["url"]));
    }
  }


  ~OSSGetFileResponse() = default;
};
class OSSGetSecureUrlResponse : public Darabonba::Model {
public:
  shared_ptr<string> expiration{};
  shared_ptr<string> url{};

  OSSGetSecureUrlResponse() {}

  explicit OSSGetSecureUrlResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (expiration) {
      res["expiration"] = boost::any(*expiration);
    }
    if (url) {
      res["url"] = boost::any(*url);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("expiration") != m.end() && !m["expiration"].empty()) {
      expiration = make_shared<string>(boost::any_cast<string>(m["expiration"]));
    }
    if (m.find("url") != m.end() && !m["url"].empty()) {
      url = make_shared<string>(boost::any_cast<string>(m["url"]));
    }
  }


  ~OSSGetSecureUrlResponse() = default;
};
class OSSGetUploadUrlResponse : public Darabonba::Model {
public:
  shared_ptr<string> createAt{};
  shared_ptr<string> domainId{};
  shared_ptr<string> driveId{};
  shared_ptr<string> filePath{};
  shared_ptr<vector<UploadPartInfo>> partInfoList{};
  shared_ptr<string> uploadId{};

  OSSGetUploadUrlResponse() {}

  explicit OSSGetUploadUrlResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    Darabonba::Model::validatePattern("domainId", domainId, "[a-z0-9A-Z]+");
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (createAt) {
      res["create_at"] = boost::any(*createAt);
    }
    if (domainId) {
      res["domain_id"] = boost::any(*domainId);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (filePath) {
      res["file_path"] = boost::any(*filePath);
    }
    if (partInfoList) {
      vector<boost::any> temp1;
      for(auto item1:*partInfoList){
        temp1.push_back(boost::any(item1.toMap()));
      }
      res["part_info_list"] = boost::any(temp1);
    }
    if (uploadId) {
      res["upload_id"] = boost::any(*uploadId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("create_at") != m.end() && !m["create_at"].empty()) {
      createAt = make_shared<string>(boost::any_cast<string>(m["create_at"]));
    }
    if (m.find("domain_id") != m.end() && !m["domain_id"].empty()) {
      domainId = make_shared<string>(boost::any_cast<string>(m["domain_id"]));
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("file_path") != m.end() && !m["file_path"].empty()) {
      filePath = make_shared<string>(boost::any_cast<string>(m["file_path"]));
    }
    if (m.find("part_info_list") != m.end() && !m["part_info_list"].empty()) {
      if (typeid(vector<boost::any>).name() == m["part_info_list"].type().name()) {
        vector<UploadPartInfo> expect1;
        for(auto item1:boost::any_cast<vector<boost::any>>(m["part_info_list"])){
          if (typeid(map<string, boost::any>).name() == item1.type().name()) {
            UploadPartInfo model2;
            model2.fromMap(boost::any_cast<map<string, boost::any>>(item1));
            expect1.push_back(model2);
          }
        }
        partInfoList = make_shared<vector<UploadPartInfo>>(expect1);
      }
    }
    if (m.find("upload_id") != m.end() && !m["upload_id"].empty()) {
      uploadId = make_shared<string>(boost::any_cast<string>(m["upload_id"]));
    }
  }


  ~OSSGetUploadUrlResponse() = default;
};
class OSSListFileResponse : public Darabonba::Model {
public:
  shared_ptr<vector<BaseOSSFileResponse>> items{};
  shared_ptr<string> nextMarker{};

  OSSListFileResponse() {}

  explicit OSSListFileResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (items) {
      vector<boost::any> temp1;
      for(auto item1:*items){
        temp1.push_back(boost::any(item1.toMap()));
      }
      res["items"] = boost::any(temp1);
    }
    if (nextMarker) {
      res["next_marker"] = boost::any(*nextMarker);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("items") != m.end() && !m["items"].empty()) {
      if (typeid(vector<boost::any>).name() == m["items"].type().name()) {
        vector<BaseOSSFileResponse> expect1;
        for(auto item1:boost::any_cast<vector<boost::any>>(m["items"])){
          if (typeid(map<string, boost::any>).name() == item1.type().name()) {
            BaseOSSFileResponse model2;
            model2.fromMap(boost::any_cast<map<string, boost::any>>(item1));
            expect1.push_back(model2);
          }
        }
        items = make_shared<vector<BaseOSSFileResponse>>(expect1);
      }
    }
    if (m.find("next_marker") != m.end() && !m["next_marker"].empty()) {
      nextMarker = make_shared<string>(boost::any_cast<string>(m["next_marker"]));
    }
  }


  ~OSSListFileResponse() = default;
};
class OSSListUploadedPartResponse : public Darabonba::Model {
public:
  shared_ptr<string> filePath{};
  shared_ptr<string> nextPartNumberMarker{};
  shared_ptr<string> uploadId{};
  shared_ptr<vector<UploadPartInfo>> uploadedParts{};

  OSSListUploadedPartResponse() {}

  explicit OSSListUploadedPartResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (filePath) {
      res["file_path"] = boost::any(*filePath);
    }
    if (nextPartNumberMarker) {
      res["next_part_number_marker"] = boost::any(*nextPartNumberMarker);
    }
    if (uploadId) {
      res["upload_id"] = boost::any(*uploadId);
    }
    if (uploadedParts) {
      vector<boost::any> temp1;
      for(auto item1:*uploadedParts){
        temp1.push_back(boost::any(item1.toMap()));
      }
      res["uploaded_parts"] = boost::any(temp1);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("file_path") != m.end() && !m["file_path"].empty()) {
      filePath = make_shared<string>(boost::any_cast<string>(m["file_path"]));
    }
    if (m.find("next_part_number_marker") != m.end() && !m["next_part_number_marker"].empty()) {
      nextPartNumberMarker = make_shared<string>(boost::any_cast<string>(m["next_part_number_marker"]));
    }
    if (m.find("upload_id") != m.end() && !m["upload_id"].empty()) {
      uploadId = make_shared<string>(boost::any_cast<string>(m["upload_id"]));
    }
    if (m.find("uploaded_parts") != m.end() && !m["uploaded_parts"].empty()) {
      if (typeid(vector<boost::any>).name() == m["uploaded_parts"].type().name()) {
        vector<UploadPartInfo> expect1;
        for(auto item1:boost::any_cast<vector<boost::any>>(m["uploaded_parts"])){
          if (typeid(map<string, boost::any>).name() == item1.type().name()) {
            UploadPartInfo model2;
            model2.fromMap(boost::any_cast<map<string, boost::any>>(item1));
            expect1.push_back(model2);
          }
        }
        uploadedParts = make_shared<vector<UploadPartInfo>>(expect1);
      }
    }
  }


  ~OSSListUploadedPartResponse() = default;
};
class OSSMoveFileResponse : public Darabonba::Model {
public:
  shared_ptr<string> asyncTaskId{};
  shared_ptr<string> domainId{};
  shared_ptr<string> driveId{};
  shared_ptr<string> filePath{};
  shared_ptr<string> shareId{};

  OSSMoveFileResponse() {}

  explicit OSSMoveFileResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    Darabonba::Model::validatePattern("domainId", domainId, "[a-z0-9A-Z-]+");
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    Darabonba::Model::validatePattern("shareId", shareId, "[a-z0-9A-Z]+");
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (asyncTaskId) {
      res["async_task_id"] = boost::any(*asyncTaskId);
    }
    if (domainId) {
      res["domain_id"] = boost::any(*domainId);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (filePath) {
      res["file_path"] = boost::any(*filePath);
    }
    if (shareId) {
      res["share_id"] = boost::any(*shareId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("async_task_id") != m.end() && !m["async_task_id"].empty()) {
      asyncTaskId = make_shared<string>(boost::any_cast<string>(m["async_task_id"]));
    }
    if (m.find("domain_id") != m.end() && !m["domain_id"].empty()) {
      domainId = make_shared<string>(boost::any_cast<string>(m["domain_id"]));
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("file_path") != m.end() && !m["file_path"].empty()) {
      filePath = make_shared<string>(boost::any_cast<string>(m["file_path"]));
    }
    if (m.find("share_id") != m.end() && !m["share_id"].empty()) {
      shareId = make_shared<string>(boost::any_cast<string>(m["share_id"]));
    }
  }


  ~OSSMoveFileResponse() = default;
};
class OSSSearchFileResponse : public Darabonba::Model {
public:
  shared_ptr<vector<BaseOSSFileResponse>> items{};
  shared_ptr<string> nextMarker{};

  OSSSearchFileResponse() {}

  explicit OSSSearchFileResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (items) {
      vector<boost::any> temp1;
      for(auto item1:*items){
        temp1.push_back(boost::any(item1.toMap()));
      }
      res["items"] = boost::any(temp1);
    }
    if (nextMarker) {
      res["next_marker"] = boost::any(*nextMarker);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("items") != m.end() && !m["items"].empty()) {
      if (typeid(vector<boost::any>).name() == m["items"].type().name()) {
        vector<BaseOSSFileResponse> expect1;
        for(auto item1:boost::any_cast<vector<boost::any>>(m["items"])){
          if (typeid(map<string, boost::any>).name() == item1.type().name()) {
            BaseOSSFileResponse model2;
            model2.fromMap(boost::any_cast<map<string, boost::any>>(item1));
            expect1.push_back(model2);
          }
        }
        items = make_shared<vector<BaseOSSFileResponse>>(expect1);
      }
    }
    if (m.find("next_marker") != m.end() && !m["next_marker"].empty()) {
      nextMarker = make_shared<string>(boost::any_cast<string>(m["next_marker"]));
    }
  }


  ~OSSSearchFileResponse() = default;
};
class OSSUpdateFileMetaResponse : public Darabonba::Model {
public:
  shared_ptr<string> contentHash{};
  shared_ptr<string> contentHashName{};
  shared_ptr<string> contentType{};
  shared_ptr<string> crc64Hash{};
  shared_ptr<string> createdAt{};
  shared_ptr<string> description{};
  shared_ptr<string> domainId{};
  shared_ptr<string> downloadUrl{};
  shared_ptr<string> driveId{};
  shared_ptr<string> fileExtension{};
  shared_ptr<string> filePath{};
  shared_ptr<string> name{};
  shared_ptr<string> parentFilePath{};
  shared_ptr<string> shareId{};
  shared_ptr<long> size{};
  shared_ptr<string> status{};
  shared_ptr<string> thumbnail{};
  shared_ptr<string> trashedAt{};
  shared_ptr<string> type{};
  shared_ptr<string> updatedAt{};
  shared_ptr<string> uploadId{};
  shared_ptr<string> url{};

  OSSUpdateFileMetaResponse() {}

  explicit OSSUpdateFileMetaResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    Darabonba::Model::validatePattern("domainId", domainId, "[a-z0-9A-Z]+");
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    if (!name) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("name is required.")));
    }
    Darabonba::Model::validatePattern("name", name, "[a-zA-Z0-9.-]{1,1000}");
    Darabonba::Model::validateMaxLength("parentFilePath", parentFilePath, 50);
    Darabonba::Model::validateMinLength("parentFilePath", parentFilePath, 40);
    Darabonba::Model::validatePattern("parentFilePath", parentFilePath, "[a-z0-9]{1,50}");
    Darabonba::Model::validatePattern("shareId", shareId, "[0-9]+");
    if (size && *size > 53687091200) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("size is required.")));
    }
    if (size && *size < 0) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("size is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (contentHash) {
      res["content_hash"] = boost::any(*contentHash);
    }
    if (contentHashName) {
      res["content_hash_name"] = boost::any(*contentHashName);
    }
    if (contentType) {
      res["content_type"] = boost::any(*contentType);
    }
    if (crc64Hash) {
      res["crc64_hash"] = boost::any(*crc64Hash);
    }
    if (createdAt) {
      res["created_at"] = boost::any(*createdAt);
    }
    if (description) {
      res["description"] = boost::any(*description);
    }
    if (domainId) {
      res["domain_id"] = boost::any(*domainId);
    }
    if (downloadUrl) {
      res["download_url"] = boost::any(*downloadUrl);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (fileExtension) {
      res["file_extension"] = boost::any(*fileExtension);
    }
    if (filePath) {
      res["file_path"] = boost::any(*filePath);
    }
    if (name) {
      res["name"] = boost::any(*name);
    }
    if (parentFilePath) {
      res["parent_file_path"] = boost::any(*parentFilePath);
    }
    if (shareId) {
      res["share_id"] = boost::any(*shareId);
    }
    if (size) {
      res["size"] = boost::any(*size);
    }
    if (status) {
      res["status"] = boost::any(*status);
    }
    if (thumbnail) {
      res["thumbnail"] = boost::any(*thumbnail);
    }
    if (trashedAt) {
      res["trashed_at"] = boost::any(*trashedAt);
    }
    if (type) {
      res["type"] = boost::any(*type);
    }
    if (updatedAt) {
      res["updated_at"] = boost::any(*updatedAt);
    }
    if (uploadId) {
      res["upload_id"] = boost::any(*uploadId);
    }
    if (url) {
      res["url"] = boost::any(*url);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("content_hash") != m.end() && !m["content_hash"].empty()) {
      contentHash = make_shared<string>(boost::any_cast<string>(m["content_hash"]));
    }
    if (m.find("content_hash_name") != m.end() && !m["content_hash_name"].empty()) {
      contentHashName = make_shared<string>(boost::any_cast<string>(m["content_hash_name"]));
    }
    if (m.find("content_type") != m.end() && !m["content_type"].empty()) {
      contentType = make_shared<string>(boost::any_cast<string>(m["content_type"]));
    }
    if (m.find("crc64_hash") != m.end() && !m["crc64_hash"].empty()) {
      crc64Hash = make_shared<string>(boost::any_cast<string>(m["crc64_hash"]));
    }
    if (m.find("created_at") != m.end() && !m["created_at"].empty()) {
      createdAt = make_shared<string>(boost::any_cast<string>(m["created_at"]));
    }
    if (m.find("description") != m.end() && !m["description"].empty()) {
      description = make_shared<string>(boost::any_cast<string>(m["description"]));
    }
    if (m.find("domain_id") != m.end() && !m["domain_id"].empty()) {
      domainId = make_shared<string>(boost::any_cast<string>(m["domain_id"]));
    }
    if (m.find("download_url") != m.end() && !m["download_url"].empty()) {
      downloadUrl = make_shared<string>(boost::any_cast<string>(m["download_url"]));
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("file_extension") != m.end() && !m["file_extension"].empty()) {
      fileExtension = make_shared<string>(boost::any_cast<string>(m["file_extension"]));
    }
    if (m.find("file_path") != m.end() && !m["file_path"].empty()) {
      filePath = make_shared<string>(boost::any_cast<string>(m["file_path"]));
    }
    if (m.find("name") != m.end() && !m["name"].empty()) {
      name = make_shared<string>(boost::any_cast<string>(m["name"]));
    }
    if (m.find("parent_file_path") != m.end() && !m["parent_file_path"].empty()) {
      parentFilePath = make_shared<string>(boost::any_cast<string>(m["parent_file_path"]));
    }
    if (m.find("share_id") != m.end() && !m["share_id"].empty()) {
      shareId = make_shared<string>(boost::any_cast<string>(m["share_id"]));
    }
    if (m.find("size") != m.end() && !m["size"].empty()) {
      size = make_shared<long>(boost::any_cast<long>(m["size"]));
    }
    if (m.find("status") != m.end() && !m["status"].empty()) {
      status = make_shared<string>(boost::any_cast<string>(m["status"]));
    }
    if (m.find("thumbnail") != m.end() && !m["thumbnail"].empty()) {
      thumbnail = make_shared<string>(boost::any_cast<string>(m["thumbnail"]));
    }
    if (m.find("trashed_at") != m.end() && !m["trashed_at"].empty()) {
      trashedAt = make_shared<string>(boost::any_cast<string>(m["trashed_at"]));
    }
    if (m.find("type") != m.end() && !m["type"].empty()) {
      type = make_shared<string>(boost::any_cast<string>(m["type"]));
    }
    if (m.find("updated_at") != m.end() && !m["updated_at"].empty()) {
      updatedAt = make_shared<string>(boost::any_cast<string>(m["updated_at"]));
    }
    if (m.find("upload_id") != m.end() && !m["upload_id"].empty()) {
      uploadId = make_shared<string>(boost::any_cast<string>(m["upload_id"]));
    }
    if (m.find("url") != m.end() && !m["url"].empty()) {
      url = make_shared<string>(boost::any_cast<string>(m["url"]));
    }
  }


  ~OSSUpdateFileMetaResponse() = default;
};
class OSSVideoDRMLicenseResponse : public Darabonba::Model {
public:
  shared_ptr<string> data{};
  shared_ptr<long> states{};

  OSSVideoDRMLicenseResponse() {}

  explicit OSSVideoDRMLicenseResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!data) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("data is required.")));
    }
    if (!states) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("states is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (data) {
      res["data"] = boost::any(*data);
    }
    if (states) {
      res["states"] = boost::any(*states);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("data") != m.end() && !m["data"].empty()) {
      data = make_shared<string>(boost::any_cast<string>(m["data"]));
    }
    if (m.find("states") != m.end() && !m["states"].empty()) {
      states = make_shared<long>(boost::any_cast<long>(m["states"]));
    }
  }


  ~OSSVideoDRMLicenseResponse() = default;
};
class OSSVideoDefinitionResponse : public Darabonba::Model {
public:
  shared_ptr<vector<string>> definitionList{};
  shared_ptr<string> frameRate{};

  OSSVideoDefinitionResponse() {}

  explicit OSSVideoDefinitionResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (definitionList) {
      res["definition_list"] = boost::any(*definitionList);
    }
    if (frameRate) {
      res["frame_rate"] = boost::any(*frameRate);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("definition_list") != m.end() && !m["definition_list"].empty()) {
      vector<string> toVec1;
      if (typeid(vector<boost::any>).name() == m["definition_list"].type().name()) {
        vector<boost::any> vec1 = boost::any_cast<vector<boost::any>>(m["definition_list"]);
        for (auto item:vec1) {
           toVec1.push_back(boost::any_cast<string>(item));
        }
      }
      definitionList = make_shared<vector<string>>(toVec1);
    }
    if (m.find("frame_rate") != m.end() && !m["frame_rate"].empty()) {
      frameRate = make_shared<string>(boost::any_cast<string>(m["frame_rate"]));
    }
  }


  ~OSSVideoDefinitionResponse() = default;
};
class OSSVideoTranscodeResponse : public Darabonba::Model {
public:
  shared_ptr<vector<string>> definitionList{};
  shared_ptr<long> duration{};
  shared_ptr<long> hlsTime{};

  OSSVideoTranscodeResponse() {}

  explicit OSSVideoTranscodeResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (definitionList) {
      res["definition_list"] = boost::any(*definitionList);
    }
    if (duration) {
      res["duration"] = boost::any(*duration);
    }
    if (hlsTime) {
      res["hls_time"] = boost::any(*hlsTime);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("definition_list") != m.end() && !m["definition_list"].empty()) {
      vector<string> toVec1;
      if (typeid(vector<boost::any>).name() == m["definition_list"].type().name()) {
        vector<boost::any> vec1 = boost::any_cast<vector<boost::any>>(m["definition_list"]);
        for (auto item:vec1) {
           toVec1.push_back(boost::any_cast<string>(item));
        }
      }
      definitionList = make_shared<vector<string>>(toVec1);
    }
    if (m.find("duration") != m.end() && !m["duration"].empty()) {
      duration = make_shared<long>(boost::any_cast<long>(m["duration"]));
    }
    if (m.find("hls_time") != m.end() && !m["hls_time"].empty()) {
      hlsTime = make_shared<long>(boost::any_cast<long>(m["hls_time"]));
    }
  }


  ~OSSVideoTranscodeResponse() = default;
};
class PreHashCheckSuccessResponse : public Darabonba::Model {
public:
  shared_ptr<string> code{};
  shared_ptr<string> fileName{};
  shared_ptr<string> message{};
  shared_ptr<string> parentFileId{};
  shared_ptr<string> preHash{};

  PreHashCheckSuccessResponse() {}

  explicit PreHashCheckSuccessResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!parentFileId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("parentFileId is required.")));
    }
    Darabonba::Model::validateMaxLength("parentFileId", parentFileId, 50);
    Darabonba::Model::validateMinLength("parentFileId", parentFileId, 40);
    Darabonba::Model::validatePattern("parentFileId", parentFileId, "[a-z0-9]{1,50}");
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (code) {
      res["code"] = boost::any(*code);
    }
    if (fileName) {
      res["file_name"] = boost::any(*fileName);
    }
    if (message) {
      res["message"] = boost::any(*message);
    }
    if (parentFileId) {
      res["parent_file_id"] = boost::any(*parentFileId);
    }
    if (preHash) {
      res["pre_hash"] = boost::any(*preHash);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("code") != m.end() && !m["code"].empty()) {
      code = make_shared<string>(boost::any_cast<string>(m["code"]));
    }
    if (m.find("file_name") != m.end() && !m["file_name"].empty()) {
      fileName = make_shared<string>(boost::any_cast<string>(m["file_name"]));
    }
    if (m.find("message") != m.end() && !m["message"].empty()) {
      message = make_shared<string>(boost::any_cast<string>(m["message"]));
    }
    if (m.find("parent_file_id") != m.end() && !m["parent_file_id"].empty()) {
      parentFileId = make_shared<string>(boost::any_cast<string>(m["parent_file_id"]));
    }
    if (m.find("pre_hash") != m.end() && !m["pre_hash"].empty()) {
      preHash = make_shared<string>(boost::any_cast<string>(m["pre_hash"]));
    }
  }


  ~PreHashCheckSuccessResponse() = default;
};
class RevokeRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<string> appId{};
  shared_ptr<string> refreshToken{};

  RevokeRequest() {}

  explicit RevokeRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!appId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("appId is required.")));
    }
    if (!refreshToken) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("refreshToken is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (appId) {
      res["app_id"] = boost::any(*appId);
    }
    if (refreshToken) {
      res["refresh_token"] = boost::any(*refreshToken);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("app_id") != m.end() && !m["app_id"].empty()) {
      appId = make_shared<string>(boost::any_cast<string>(m["app_id"]));
    }
    if (m.find("refresh_token") != m.end() && !m["refresh_token"].empty()) {
      refreshToken = make_shared<string>(boost::any_cast<string>(m["refresh_token"]));
    }
  }


  ~RevokeRequest() = default;
};
class ScanFileMetaResponse : public Darabonba::Model {
public:
  shared_ptr<vector<BaseFileResponse>> items{};
  shared_ptr<string> nextMarker{};

  ScanFileMetaResponse() {}

  explicit ScanFileMetaResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (items) {
      vector<boost::any> temp1;
      for(auto item1:*items){
        temp1.push_back(boost::any(item1.toMap()));
      }
      res["items"] = boost::any(temp1);
    }
    if (nextMarker) {
      res["next_marker"] = boost::any(*nextMarker);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("items") != m.end() && !m["items"].empty()) {
      if (typeid(vector<boost::any>).name() == m["items"].type().name()) {
        vector<BaseFileResponse> expect1;
        for(auto item1:boost::any_cast<vector<boost::any>>(m["items"])){
          if (typeid(map<string, boost::any>).name() == item1.type().name()) {
            BaseFileResponse model2;
            model2.fromMap(boost::any_cast<map<string, boost::any>>(item1));
            expect1.push_back(model2);
          }
        }
        items = make_shared<vector<BaseFileResponse>>(expect1);
      }
    }
    if (m.find("next_marker") != m.end() && !m["next_marker"].empty()) {
      nextMarker = make_shared<string>(boost::any_cast<string>(m["next_marker"]));
    }
  }


  ~ScanFileMetaResponse() = default;
};
class SearchFileResponse : public Darabonba::Model {
public:
  shared_ptr<vector<BaseFileResponse>> items{};
  shared_ptr<string> nextMarker{};

  SearchFileResponse() {}

  explicit SearchFileResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (items) {
      vector<boost::any> temp1;
      for(auto item1:*items){
        temp1.push_back(boost::any(item1.toMap()));
      }
      res["items"] = boost::any(temp1);
    }
    if (nextMarker) {
      res["next_marker"] = boost::any(*nextMarker);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("items") != m.end() && !m["items"].empty()) {
      if (typeid(vector<boost::any>).name() == m["items"].type().name()) {
        vector<BaseFileResponse> expect1;
        for(auto item1:boost::any_cast<vector<boost::any>>(m["items"])){
          if (typeid(map<string, boost::any>).name() == item1.type().name()) {
            BaseFileResponse model2;
            model2.fromMap(boost::any_cast<map<string, boost::any>>(item1));
            expect1.push_back(model2);
          }
        }
        items = make_shared<vector<BaseFileResponse>>(expect1);
      }
    }
    if (m.find("next_marker") != m.end() && !m["next_marker"].empty()) {
      nextMarker = make_shared<string>(boost::any_cast<string>(m["next_marker"]));
    }
  }


  ~SearchFileResponse() = default;
};
class StreamInfo : public Darabonba::Model {
public:
  shared_ptr<string> crc64Hash{};
  shared_ptr<string> downloadUrl{};
  shared_ptr<string> thumbnail{};
  shared_ptr<string> url{};

  StreamInfo() {}

  explicit StreamInfo(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (crc64Hash) {
      res["crc64_hash"] = boost::any(*crc64Hash);
    }
    if (downloadUrl) {
      res["download_url"] = boost::any(*downloadUrl);
    }
    if (thumbnail) {
      res["thumbnail"] = boost::any(*thumbnail);
    }
    if (url) {
      res["url"] = boost::any(*url);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("crc64_hash") != m.end() && !m["crc64_hash"].empty()) {
      crc64Hash = make_shared<string>(boost::any_cast<string>(m["crc64_hash"]));
    }
    if (m.find("download_url") != m.end() && !m["download_url"].empty()) {
      downloadUrl = make_shared<string>(boost::any_cast<string>(m["download_url"]));
    }
    if (m.find("thumbnail") != m.end() && !m["thumbnail"].empty()) {
      thumbnail = make_shared<string>(boost::any_cast<string>(m["thumbnail"]));
    }
    if (m.find("url") != m.end() && !m["url"].empty()) {
      url = make_shared<string>(boost::any_cast<string>(m["url"]));
    }
  }


  ~StreamInfo() = default;
};
class StreamUploadInfo : public Darabonba::Model {
public:
  shared_ptr<vector<UploadPartInfo>> partInfoList{};
  shared_ptr<bool> preRapidUpload{};
  shared_ptr<bool> rapidUpload{};
  shared_ptr<string> uploadId{};

  StreamUploadInfo() {}

  explicit StreamUploadInfo(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (partInfoList) {
      vector<boost::any> temp1;
      for(auto item1:*partInfoList){
        temp1.push_back(boost::any(item1.toMap()));
      }
      res["part_info_list"] = boost::any(temp1);
    }
    if (preRapidUpload) {
      res["pre_rapid_upload"] = boost::any(*preRapidUpload);
    }
    if (rapidUpload) {
      res["rapid_upload"] = boost::any(*rapidUpload);
    }
    if (uploadId) {
      res["upload_id"] = boost::any(*uploadId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("part_info_list") != m.end() && !m["part_info_list"].empty()) {
      if (typeid(vector<boost::any>).name() == m["part_info_list"].type().name()) {
        vector<UploadPartInfo> expect1;
        for(auto item1:boost::any_cast<vector<boost::any>>(m["part_info_list"])){
          if (typeid(map<string, boost::any>).name() == item1.type().name()) {
            UploadPartInfo model2;
            model2.fromMap(boost::any_cast<map<string, boost::any>>(item1));
            expect1.push_back(model2);
          }
        }
        partInfoList = make_shared<vector<UploadPartInfo>>(expect1);
      }
    }
    if (m.find("pre_rapid_upload") != m.end() && !m["pre_rapid_upload"].empty()) {
      preRapidUpload = make_shared<bool>(boost::any_cast<bool>(m["pre_rapid_upload"]));
    }
    if (m.find("rapid_upload") != m.end() && !m["rapid_upload"].empty()) {
      rapidUpload = make_shared<bool>(boost::any_cast<bool>(m["rapid_upload"]));
    }
    if (m.find("upload_id") != m.end() && !m["upload_id"].empty()) {
      uploadId = make_shared<string>(boost::any_cast<string>(m["upload_id"]));
    }
  }


  ~StreamUploadInfo() = default;
};
class TokenRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<map<string, boost::any>> additionData{};
  shared_ptr<string> appId{};
  shared_ptr<string> grantType{};
  shared_ptr<string> refreshToken{};

  TokenRequest() {}

  explicit TokenRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!appId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("appId is required.")));
    }
    if (!grantType) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("grantType is required.")));
    }
    if (!refreshToken) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("refreshToken is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (additionData) {
      res["addition_data"] = boost::any(*additionData);
    }
    if (appId) {
      res["app_id"] = boost::any(*appId);
    }
    if (grantType) {
      res["grant_type"] = boost::any(*grantType);
    }
    if (refreshToken) {
      res["refresh_token"] = boost::any(*refreshToken);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("addition_data") != m.end() && !m["addition_data"].empty()) {
      map<string, boost::any> map1 = boost::any_cast<map<string, boost::any>>(m["addition_data"]);
      map<string, boost::any> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      additionData = make_shared<map<string, boost::any>>(toMap1);
    }
    if (m.find("app_id") != m.end() && !m["app_id"].empty()) {
      appId = make_shared<string>(boost::any_cast<string>(m["app_id"]));
    }
    if (m.find("grant_type") != m.end() && !m["grant_type"].empty()) {
      grantType = make_shared<string>(boost::any_cast<string>(m["grant_type"]));
    }
    if (m.find("refresh_token") != m.end() && !m["refresh_token"].empty()) {
      refreshToken = make_shared<string>(boost::any_cast<string>(m["refresh_token"]));
    }
  }


  ~TokenRequest() = default;
};
class UpdateDriveResponse : public Darabonba::Model {
public:
  shared_ptr<string> creator{};
  shared_ptr<string> description{};
  shared_ptr<string> domainId{};
  shared_ptr<string> driveId{};
  shared_ptr<string> driveName{};
  shared_ptr<string> driveType{};
  shared_ptr<bool> encryptDataAccess{};
  shared_ptr<string> encryptMode{};
  shared_ptr<string> owner{};
  shared_ptr<string> relativePath{};
  shared_ptr<string> status{};
  shared_ptr<string> storeId{};
  shared_ptr<long> totalSize{};
  shared_ptr<long> usedSize{};

  UpdateDriveResponse() {}

  explicit UpdateDriveResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (creator) {
      res["creator"] = boost::any(*creator);
    }
    if (description) {
      res["description"] = boost::any(*description);
    }
    if (domainId) {
      res["domain_id"] = boost::any(*domainId);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (driveName) {
      res["drive_name"] = boost::any(*driveName);
    }
    if (driveType) {
      res["drive_type"] = boost::any(*driveType);
    }
    if (encryptDataAccess) {
      res["encrypt_data_access"] = boost::any(*encryptDataAccess);
    }
    if (encryptMode) {
      res["encrypt_mode"] = boost::any(*encryptMode);
    }
    if (owner) {
      res["owner"] = boost::any(*owner);
    }
    if (relativePath) {
      res["relative_path"] = boost::any(*relativePath);
    }
    if (status) {
      res["status"] = boost::any(*status);
    }
    if (storeId) {
      res["store_id"] = boost::any(*storeId);
    }
    if (totalSize) {
      res["total_size"] = boost::any(*totalSize);
    }
    if (usedSize) {
      res["used_size"] = boost::any(*usedSize);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("creator") != m.end() && !m["creator"].empty()) {
      creator = make_shared<string>(boost::any_cast<string>(m["creator"]));
    }
    if (m.find("description") != m.end() && !m["description"].empty()) {
      description = make_shared<string>(boost::any_cast<string>(m["description"]));
    }
    if (m.find("domain_id") != m.end() && !m["domain_id"].empty()) {
      domainId = make_shared<string>(boost::any_cast<string>(m["domain_id"]));
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("drive_name") != m.end() && !m["drive_name"].empty()) {
      driveName = make_shared<string>(boost::any_cast<string>(m["drive_name"]));
    }
    if (m.find("drive_type") != m.end() && !m["drive_type"].empty()) {
      driveType = make_shared<string>(boost::any_cast<string>(m["drive_type"]));
    }
    if (m.find("encrypt_data_access") != m.end() && !m["encrypt_data_access"].empty()) {
      encryptDataAccess = make_shared<bool>(boost::any_cast<bool>(m["encrypt_data_access"]));
    }
    if (m.find("encrypt_mode") != m.end() && !m["encrypt_mode"].empty()) {
      encryptMode = make_shared<string>(boost::any_cast<string>(m["encrypt_mode"]));
    }
    if (m.find("owner") != m.end() && !m["owner"].empty()) {
      owner = make_shared<string>(boost::any_cast<string>(m["owner"]));
    }
    if (m.find("relative_path") != m.end() && !m["relative_path"].empty()) {
      relativePath = make_shared<string>(boost::any_cast<string>(m["relative_path"]));
    }
    if (m.find("status") != m.end() && !m["status"].empty()) {
      status = make_shared<string>(boost::any_cast<string>(m["status"]));
    }
    if (m.find("store_id") != m.end() && !m["store_id"].empty()) {
      storeId = make_shared<string>(boost::any_cast<string>(m["store_id"]));
    }
    if (m.find("total_size") != m.end() && !m["total_size"].empty()) {
      totalSize = make_shared<long>(boost::any_cast<long>(m["total_size"]));
    }
    if (m.find("used_size") != m.end() && !m["used_size"].empty()) {
      usedSize = make_shared<long>(boost::any_cast<long>(m["used_size"]));
    }
  }


  ~UpdateDriveResponse() = default;
};
class UpdateFileMetaResponse : public Darabonba::Model {
public:
  shared_ptr<string> category{};
  shared_ptr<string> contentHash{};
  shared_ptr<string> contentHashName{};
  shared_ptr<string> contentType{};
  shared_ptr<string> crc64Hash{};
  shared_ptr<string> createdAt{};
  shared_ptr<string> description{};
  shared_ptr<string> domainId{};
  shared_ptr<string> downloadUrl{};
  shared_ptr<string> driveId{};
  shared_ptr<string> encryptMode{};
  shared_ptr<string> fileExtension{};
  shared_ptr<string> fileId{};
  shared_ptr<bool> hidden{};
  shared_ptr<ImageMediaResponse> imageMediaMetadata{};
  shared_ptr<vector<string>> labels{};
  shared_ptr<string> meta{};
  shared_ptr<string> name{};
  shared_ptr<string> parentFileId{};
  shared_ptr<int> punishFlag{};
  shared_ptr<long> size{};
  shared_ptr<bool> starred{};
  shared_ptr<string> status{};
  shared_ptr<map<string, boost::any>> streamsInfo{};
  shared_ptr<string> thumbnail{};
  shared_ptr<string> trashedAt{};
  shared_ptr<string> type{};
  shared_ptr<string> updatedAt{};
  shared_ptr<string> uploadId{};
  shared_ptr<string> url{};
  shared_ptr<string> userMeta{};
  shared_ptr<VideoMediaResponse> videoMediaMetadata{};
  shared_ptr<VideoPreviewResponse> videoPreviewMetadata{};

  UpdateFileMetaResponse() {}

  explicit UpdateFileMetaResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    Darabonba::Model::validatePattern("domainId", domainId, "[a-z0-9A-Z]+");
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    Darabonba::Model::validateMaxLength("fileId", fileId, 50);
    Darabonba::Model::validateMinLength("fileId", fileId, 40);
    Darabonba::Model::validatePattern("fileId", fileId, "[a-z0-9]{1,50}");
    if (!name) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("name is required.")));
    }
    Darabonba::Model::validatePattern("name", name, "[a-zA-Z0-9.-]{1,1000}");
    Darabonba::Model::validateMaxLength("parentFileId", parentFileId, 50);
    Darabonba::Model::validateMinLength("parentFileId", parentFileId, 40);
    Darabonba::Model::validatePattern("parentFileId", parentFileId, "[a-z0-9]{1,50}");
    if (size && *size > 53687091200) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("size is required.")));
    }
    if (size && *size < 0) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("size is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (category) {
      res["category"] = boost::any(*category);
    }
    if (contentHash) {
      res["content_hash"] = boost::any(*contentHash);
    }
    if (contentHashName) {
      res["content_hash_name"] = boost::any(*contentHashName);
    }
    if (contentType) {
      res["content_type"] = boost::any(*contentType);
    }
    if (crc64Hash) {
      res["crc64_hash"] = boost::any(*crc64Hash);
    }
    if (createdAt) {
      res["created_at"] = boost::any(*createdAt);
    }
    if (description) {
      res["description"] = boost::any(*description);
    }
    if (domainId) {
      res["domain_id"] = boost::any(*domainId);
    }
    if (downloadUrl) {
      res["download_url"] = boost::any(*downloadUrl);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (encryptMode) {
      res["encrypt_mode"] = boost::any(*encryptMode);
    }
    if (fileExtension) {
      res["file_extension"] = boost::any(*fileExtension);
    }
    if (fileId) {
      res["file_id"] = boost::any(*fileId);
    }
    if (hidden) {
      res["hidden"] = boost::any(*hidden);
    }
    if (imageMediaMetadata) {
      res["image_media_metadata"] = imageMediaMetadata ? boost::any(imageMediaMetadata->toMap()) : boost::any(map<string,boost::any>({}));
    }
    if (labels) {
      res["labels"] = boost::any(*labels);
    }
    if (meta) {
      res["meta"] = boost::any(*meta);
    }
    if (name) {
      res["name"] = boost::any(*name);
    }
    if (parentFileId) {
      res["parent_file_id"] = boost::any(*parentFileId);
    }
    if (punishFlag) {
      res["punish_flag"] = boost::any(*punishFlag);
    }
    if (size) {
      res["size"] = boost::any(*size);
    }
    if (starred) {
      res["starred"] = boost::any(*starred);
    }
    if (status) {
      res["status"] = boost::any(*status);
    }
    if (streamsInfo) {
      res["streams_info"] = boost::any(*streamsInfo);
    }
    if (thumbnail) {
      res["thumbnail"] = boost::any(*thumbnail);
    }
    if (trashedAt) {
      res["trashed_at"] = boost::any(*trashedAt);
    }
    if (type) {
      res["type"] = boost::any(*type);
    }
    if (updatedAt) {
      res["updated_at"] = boost::any(*updatedAt);
    }
    if (uploadId) {
      res["upload_id"] = boost::any(*uploadId);
    }
    if (url) {
      res["url"] = boost::any(*url);
    }
    if (userMeta) {
      res["user_meta"] = boost::any(*userMeta);
    }
    if (videoMediaMetadata) {
      res["video_media_metadata"] = videoMediaMetadata ? boost::any(videoMediaMetadata->toMap()) : boost::any(map<string,boost::any>({}));
    }
    if (videoPreviewMetadata) {
      res["video_preview_metadata"] = videoPreviewMetadata ? boost::any(videoPreviewMetadata->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("category") != m.end() && !m["category"].empty()) {
      category = make_shared<string>(boost::any_cast<string>(m["category"]));
    }
    if (m.find("content_hash") != m.end() && !m["content_hash"].empty()) {
      contentHash = make_shared<string>(boost::any_cast<string>(m["content_hash"]));
    }
    if (m.find("content_hash_name") != m.end() && !m["content_hash_name"].empty()) {
      contentHashName = make_shared<string>(boost::any_cast<string>(m["content_hash_name"]));
    }
    if (m.find("content_type") != m.end() && !m["content_type"].empty()) {
      contentType = make_shared<string>(boost::any_cast<string>(m["content_type"]));
    }
    if (m.find("crc64_hash") != m.end() && !m["crc64_hash"].empty()) {
      crc64Hash = make_shared<string>(boost::any_cast<string>(m["crc64_hash"]));
    }
    if (m.find("created_at") != m.end() && !m["created_at"].empty()) {
      createdAt = make_shared<string>(boost::any_cast<string>(m["created_at"]));
    }
    if (m.find("description") != m.end() && !m["description"].empty()) {
      description = make_shared<string>(boost::any_cast<string>(m["description"]));
    }
    if (m.find("domain_id") != m.end() && !m["domain_id"].empty()) {
      domainId = make_shared<string>(boost::any_cast<string>(m["domain_id"]));
    }
    if (m.find("download_url") != m.end() && !m["download_url"].empty()) {
      downloadUrl = make_shared<string>(boost::any_cast<string>(m["download_url"]));
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("encrypt_mode") != m.end() && !m["encrypt_mode"].empty()) {
      encryptMode = make_shared<string>(boost::any_cast<string>(m["encrypt_mode"]));
    }
    if (m.find("file_extension") != m.end() && !m["file_extension"].empty()) {
      fileExtension = make_shared<string>(boost::any_cast<string>(m["file_extension"]));
    }
    if (m.find("file_id") != m.end() && !m["file_id"].empty()) {
      fileId = make_shared<string>(boost::any_cast<string>(m["file_id"]));
    }
    if (m.find("hidden") != m.end() && !m["hidden"].empty()) {
      hidden = make_shared<bool>(boost::any_cast<bool>(m["hidden"]));
    }
    if (m.find("image_media_metadata") != m.end() && !m["image_media_metadata"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["image_media_metadata"].type().name()) {
        ImageMediaResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["image_media_metadata"]));
        imageMediaMetadata = make_shared<ImageMediaResponse>(model1);
      }
    }
    if (m.find("labels") != m.end() && !m["labels"].empty()) {
      vector<string> toVec1;
      if (typeid(vector<boost::any>).name() == m["labels"].type().name()) {
        vector<boost::any> vec1 = boost::any_cast<vector<boost::any>>(m["labels"]);
        for (auto item:vec1) {
           toVec1.push_back(boost::any_cast<string>(item));
        }
      }
      labels = make_shared<vector<string>>(toVec1);
    }
    if (m.find("meta") != m.end() && !m["meta"].empty()) {
      meta = make_shared<string>(boost::any_cast<string>(m["meta"]));
    }
    if (m.find("name") != m.end() && !m["name"].empty()) {
      name = make_shared<string>(boost::any_cast<string>(m["name"]));
    }
    if (m.find("parent_file_id") != m.end() && !m["parent_file_id"].empty()) {
      parentFileId = make_shared<string>(boost::any_cast<string>(m["parent_file_id"]));
    }
    if (m.find("punish_flag") != m.end() && !m["punish_flag"].empty()) {
      punishFlag = make_shared<int>(boost::any_cast<int>(m["punish_flag"]));
    }
    if (m.find("size") != m.end() && !m["size"].empty()) {
      size = make_shared<long>(boost::any_cast<long>(m["size"]));
    }
    if (m.find("starred") != m.end() && !m["starred"].empty()) {
      starred = make_shared<bool>(boost::any_cast<bool>(m["starred"]));
    }
    if (m.find("status") != m.end() && !m["status"].empty()) {
      status = make_shared<string>(boost::any_cast<string>(m["status"]));
    }
    if (m.find("streams_info") != m.end() && !m["streams_info"].empty()) {
      map<string, boost::any> map1 = boost::any_cast<map<string, boost::any>>(m["streams_info"]);
      map<string, boost::any> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      streamsInfo = make_shared<map<string, boost::any>>(toMap1);
    }
    if (m.find("thumbnail") != m.end() && !m["thumbnail"].empty()) {
      thumbnail = make_shared<string>(boost::any_cast<string>(m["thumbnail"]));
    }
    if (m.find("trashed_at") != m.end() && !m["trashed_at"].empty()) {
      trashedAt = make_shared<string>(boost::any_cast<string>(m["trashed_at"]));
    }
    if (m.find("type") != m.end() && !m["type"].empty()) {
      type = make_shared<string>(boost::any_cast<string>(m["type"]));
    }
    if (m.find("updated_at") != m.end() && !m["updated_at"].empty()) {
      updatedAt = make_shared<string>(boost::any_cast<string>(m["updated_at"]));
    }
    if (m.find("upload_id") != m.end() && !m["upload_id"].empty()) {
      uploadId = make_shared<string>(boost::any_cast<string>(m["upload_id"]));
    }
    if (m.find("url") != m.end() && !m["url"].empty()) {
      url = make_shared<string>(boost::any_cast<string>(m["url"]));
    }
    if (m.find("user_meta") != m.end() && !m["user_meta"].empty()) {
      userMeta = make_shared<string>(boost::any_cast<string>(m["user_meta"]));
    }
    if (m.find("video_media_metadata") != m.end() && !m["video_media_metadata"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["video_media_metadata"].type().name()) {
        VideoMediaResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["video_media_metadata"]));
        videoMediaMetadata = make_shared<VideoMediaResponse>(model1);
      }
    }
    if (m.find("video_preview_metadata") != m.end() && !m["video_preview_metadata"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["video_preview_metadata"].type().name()) {
        VideoPreviewResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["video_preview_metadata"]));
        videoPreviewMetadata = make_shared<VideoPreviewResponse>(model1);
      }
    }
  }


  ~UpdateFileMetaResponse() = default;
};
class UpdateShareResponse : public Darabonba::Model {
public:
  shared_ptr<string> createdAt{};
  shared_ptr<string> creator{};
  shared_ptr<string> description{};
  shared_ptr<string> domainId{};
  shared_ptr<string> driveId{};
  shared_ptr<string> expiration{};
  shared_ptr<bool> expired{};
  shared_ptr<string> owner{};
  shared_ptr<vector<string>> permissions{};
  shared_ptr<string> shareFilePath{};
  shared_ptr<string> shareId{};
  shared_ptr<string> shareName{};
  shared_ptr<vector<SharePermissionPolicy>> sharePolicy{};
  shared_ptr<string> status{};
  shared_ptr<string> updatedAt{};

  UpdateShareResponse() {}

  explicit UpdateShareResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (createdAt) {
      res["created_at"] = boost::any(*createdAt);
    }
    if (creator) {
      res["creator"] = boost::any(*creator);
    }
    if (description) {
      res["description"] = boost::any(*description);
    }
    if (domainId) {
      res["domain_id"] = boost::any(*domainId);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (expiration) {
      res["expiration"] = boost::any(*expiration);
    }
    if (expired) {
      res["expired"] = boost::any(*expired);
    }
    if (owner) {
      res["owner"] = boost::any(*owner);
    }
    if (permissions) {
      res["permissions"] = boost::any(*permissions);
    }
    if (shareFilePath) {
      res["share_file_path"] = boost::any(*shareFilePath);
    }
    if (shareId) {
      res["share_id"] = boost::any(*shareId);
    }
    if (shareName) {
      res["share_name"] = boost::any(*shareName);
    }
    if (sharePolicy) {
      vector<boost::any> temp1;
      for(auto item1:*sharePolicy){
        temp1.push_back(boost::any(item1.toMap()));
      }
      res["share_policy"] = boost::any(temp1);
    }
    if (status) {
      res["status"] = boost::any(*status);
    }
    if (updatedAt) {
      res["updated_at"] = boost::any(*updatedAt);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("created_at") != m.end() && !m["created_at"].empty()) {
      createdAt = make_shared<string>(boost::any_cast<string>(m["created_at"]));
    }
    if (m.find("creator") != m.end() && !m["creator"].empty()) {
      creator = make_shared<string>(boost::any_cast<string>(m["creator"]));
    }
    if (m.find("description") != m.end() && !m["description"].empty()) {
      description = make_shared<string>(boost::any_cast<string>(m["description"]));
    }
    if (m.find("domain_id") != m.end() && !m["domain_id"].empty()) {
      domainId = make_shared<string>(boost::any_cast<string>(m["domain_id"]));
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("expiration") != m.end() && !m["expiration"].empty()) {
      expiration = make_shared<string>(boost::any_cast<string>(m["expiration"]));
    }
    if (m.find("expired") != m.end() && !m["expired"].empty()) {
      expired = make_shared<bool>(boost::any_cast<bool>(m["expired"]));
    }
    if (m.find("owner") != m.end() && !m["owner"].empty()) {
      owner = make_shared<string>(boost::any_cast<string>(m["owner"]));
    }
    if (m.find("permissions") != m.end() && !m["permissions"].empty()) {
      vector<string> toVec1;
      if (typeid(vector<boost::any>).name() == m["permissions"].type().name()) {
        vector<boost::any> vec1 = boost::any_cast<vector<boost::any>>(m["permissions"]);
        for (auto item:vec1) {
           toVec1.push_back(boost::any_cast<string>(item));
        }
      }
      permissions = make_shared<vector<string>>(toVec1);
    }
    if (m.find("share_file_path") != m.end() && !m["share_file_path"].empty()) {
      shareFilePath = make_shared<string>(boost::any_cast<string>(m["share_file_path"]));
    }
    if (m.find("share_id") != m.end() && !m["share_id"].empty()) {
      shareId = make_shared<string>(boost::any_cast<string>(m["share_id"]));
    }
    if (m.find("share_name") != m.end() && !m["share_name"].empty()) {
      shareName = make_shared<string>(boost::any_cast<string>(m["share_name"]));
    }
    if (m.find("share_policy") != m.end() && !m["share_policy"].empty()) {
      if (typeid(vector<boost::any>).name() == m["share_policy"].type().name()) {
        vector<SharePermissionPolicy> expect1;
        for(auto item1:boost::any_cast<vector<boost::any>>(m["share_policy"])){
          if (typeid(map<string, boost::any>).name() == item1.type().name()) {
            SharePermissionPolicy model2;
            model2.fromMap(boost::any_cast<map<string, boost::any>>(item1));
            expect1.push_back(model2);
          }
        }
        sharePolicy = make_shared<vector<SharePermissionPolicy>>(expect1);
      }
    }
    if (m.find("status") != m.end() && !m["status"].empty()) {
      status = make_shared<string>(boost::any_cast<string>(m["status"]));
    }
    if (m.find("updated_at") != m.end() && !m["updated_at"].empty()) {
      updatedAt = make_shared<string>(boost::any_cast<string>(m["updated_at"]));
    }
  }


  ~UpdateShareResponse() = default;
};
class UrlInfo : public Darabonba::Model {
public:
  shared_ptr<string> downloadUrl{};
  shared_ptr<string> thumbnail{};
  shared_ptr<string> url{};

  UrlInfo() {}

  explicit UrlInfo(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (downloadUrl) {
      res["download_url"] = boost::any(*downloadUrl);
    }
    if (thumbnail) {
      res["thumbnail"] = boost::any(*thumbnail);
    }
    if (url) {
      res["url"] = boost::any(*url);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("download_url") != m.end() && !m["download_url"].empty()) {
      downloadUrl = make_shared<string>(boost::any_cast<string>(m["download_url"]));
    }
    if (m.find("thumbnail") != m.end() && !m["thumbnail"].empty()) {
      thumbnail = make_shared<string>(boost::any_cast<string>(m["thumbnail"]));
    }
    if (m.find("url") != m.end() && !m["url"].empty()) {
      url = make_shared<string>(boost::any_cast<string>(m["url"]));
    }
  }


  ~UrlInfo() = default;
};
class UserAuthentication : public Darabonba::Model {
public:
  shared_ptr<string> AuthenticationType{};
  shared_ptr<long> CreatedAt{};
  shared_ptr<string> Detail{};
  shared_ptr<string> DomainID{};
  shared_ptr<string> Identity{};
  shared_ptr<long> LastLoginTime{};
  shared_ptr<string> Status{};
  shared_ptr<string> UserID{};
  shared_ptr<string> extra{};

  UserAuthentication() {}

  explicit UserAuthentication(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!AuthenticationType) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("AuthenticationType is required.")));
    }
    if (!CreatedAt) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("CreatedAt is required.")));
    }
    if (!Detail) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("Detail is required.")));
    }
    if (!DomainID) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("DomainID is required.")));
    }
    if (!Identity) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("Identity is required.")));
    }
    if (!LastLoginTime) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("LastLoginTime is required.")));
    }
    if (!Status) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("Status is required.")));
    }
    if (!UserID) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("UserID is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (AuthenticationType) {
      res["AuthenticationType"] = boost::any(*AuthenticationType);
    }
    if (CreatedAt) {
      res["CreatedAt"] = boost::any(*CreatedAt);
    }
    if (Detail) {
      res["Detail"] = boost::any(*Detail);
    }
    if (DomainID) {
      res["DomainID"] = boost::any(*DomainID);
    }
    if (Identity) {
      res["Identity"] = boost::any(*Identity);
    }
    if (LastLoginTime) {
      res["LastLoginTime"] = boost::any(*LastLoginTime);
    }
    if (Status) {
      res["Status"] = boost::any(*Status);
    }
    if (UserID) {
      res["UserID"] = boost::any(*UserID);
    }
    if (extra) {
      res["extra"] = boost::any(*extra);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("AuthenticationType") != m.end() && !m["AuthenticationType"].empty()) {
      AuthenticationType = make_shared<string>(boost::any_cast<string>(m["AuthenticationType"]));
    }
    if (m.find("CreatedAt") != m.end() && !m["CreatedAt"].empty()) {
      CreatedAt = make_shared<long>(boost::any_cast<long>(m["CreatedAt"]));
    }
    if (m.find("Detail") != m.end() && !m["Detail"].empty()) {
      Detail = make_shared<string>(boost::any_cast<string>(m["Detail"]));
    }
    if (m.find("DomainID") != m.end() && !m["DomainID"].empty()) {
      DomainID = make_shared<string>(boost::any_cast<string>(m["DomainID"]));
    }
    if (m.find("Identity") != m.end() && !m["Identity"].empty()) {
      Identity = make_shared<string>(boost::any_cast<string>(m["Identity"]));
    }
    if (m.find("LastLoginTime") != m.end() && !m["LastLoginTime"].empty()) {
      LastLoginTime = make_shared<long>(boost::any_cast<long>(m["LastLoginTime"]));
    }
    if (m.find("Status") != m.end() && !m["Status"].empty()) {
      Status = make_shared<string>(boost::any_cast<string>(m["Status"]));
    }
    if (m.find("UserID") != m.end() && !m["UserID"].empty()) {
      UserID = make_shared<string>(boost::any_cast<string>(m["UserID"]));
    }
    if (m.find("extra") != m.end() && !m["extra"].empty()) {
      extra = make_shared<string>(boost::any_cast<string>(m["extra"]));
    }
  }


  ~UserAuthentication() = default;
};
class VerifyCodeRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<string> appId{};
  shared_ptr<string> phoneNumber{};
  shared_ptr<string> phoneRegion{};
  shared_ptr<string> smsCode{};
  shared_ptr<string> smsCodeId{};
  shared_ptr<string> verifyType{};

  VerifyCodeRequest() {}

  explicit VerifyCodeRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!appId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("appId is required.")));
    }
    if (!phoneNumber) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("phoneNumber is required.")));
    }
    if (!smsCode) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("smsCode is required.")));
    }
    if (!smsCodeId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("smsCodeId is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (appId) {
      res["app_id"] = boost::any(*appId);
    }
    if (phoneNumber) {
      res["phone_number"] = boost::any(*phoneNumber);
    }
    if (phoneRegion) {
      res["phone_region"] = boost::any(*phoneRegion);
    }
    if (smsCode) {
      res["sms_code"] = boost::any(*smsCode);
    }
    if (smsCodeId) {
      res["sms_code_id"] = boost::any(*smsCodeId);
    }
    if (verifyType) {
      res["verify_type"] = boost::any(*verifyType);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("app_id") != m.end() && !m["app_id"].empty()) {
      appId = make_shared<string>(boost::any_cast<string>(m["app_id"]));
    }
    if (m.find("phone_number") != m.end() && !m["phone_number"].empty()) {
      phoneNumber = make_shared<string>(boost::any_cast<string>(m["phone_number"]));
    }
    if (m.find("phone_region") != m.end() && !m["phone_region"].empty()) {
      phoneRegion = make_shared<string>(boost::any_cast<string>(m["phone_region"]));
    }
    if (m.find("sms_code") != m.end() && !m["sms_code"].empty()) {
      smsCode = make_shared<string>(boost::any_cast<string>(m["sms_code"]));
    }
    if (m.find("sms_code_id") != m.end() && !m["sms_code_id"].empty()) {
      smsCodeId = make_shared<string>(boost::any_cast<string>(m["sms_code_id"]));
    }
    if (m.find("verify_type") != m.end() && !m["verify_type"].empty()) {
      verifyType = make_shared<string>(boost::any_cast<string>(m["verify_type"]));
    }
  }


  ~VerifyCodeRequest() = default;
};
class Store : public Darabonba::Model {
public:
  shared_ptr<string> accelerateEndpoint{};
  shared_ptr<string> basePath{};
  shared_ptr<string> bucket{};
  shared_ptr<string> cdnEndpoint{};
  shared_ptr<string> customizedAccelerateEndpoint{};
  shared_ptr<string> customizedCdnEndpoint{};
  shared_ptr<string> customizedEndpoint{};
  shared_ptr<string> customizedInternalEndpoint{};
  shared_ptr<string> endpoint{};
  shared_ptr<string> internalEndpoint{};
  shared_ptr<string> location{};
  shared_ptr<string> ownership{};
  shared_ptr<string> policy{};
  shared_ptr<string> roleArn{};
  shared_ptr<string> storeId{};
  shared_ptr<string> type{};

  Store() {}

  explicit Store(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!bucket) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("bucket is required.")));
    }
    if (!endpoint) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("endpoint is required.")));
    }
    if (!ownership) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("ownership is required.")));
    }
    if (!policy) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("policy is required.")));
    }
    if (!storeId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("storeId is required.")));
    }
    if (!type) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("type is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (accelerateEndpoint) {
      res["accelerate_endpoint"] = boost::any(*accelerateEndpoint);
    }
    if (basePath) {
      res["base_path"] = boost::any(*basePath);
    }
    if (bucket) {
      res["bucket"] = boost::any(*bucket);
    }
    if (cdnEndpoint) {
      res["cdn_endpoint"] = boost::any(*cdnEndpoint);
    }
    if (customizedAccelerateEndpoint) {
      res["customized_accelerate_endpoint"] = boost::any(*customizedAccelerateEndpoint);
    }
    if (customizedCdnEndpoint) {
      res["customized_cdn_endpoint"] = boost::any(*customizedCdnEndpoint);
    }
    if (customizedEndpoint) {
      res["customized_endpoint"] = boost::any(*customizedEndpoint);
    }
    if (customizedInternalEndpoint) {
      res["customized_internal_endpoint"] = boost::any(*customizedInternalEndpoint);
    }
    if (endpoint) {
      res["endpoint"] = boost::any(*endpoint);
    }
    if (internalEndpoint) {
      res["internal_endpoint"] = boost::any(*internalEndpoint);
    }
    if (location) {
      res["location"] = boost::any(*location);
    }
    if (ownership) {
      res["ownership"] = boost::any(*ownership);
    }
    if (policy) {
      res["policy"] = boost::any(*policy);
    }
    if (roleArn) {
      res["role_arn"] = boost::any(*roleArn);
    }
    if (storeId) {
      res["store_id"] = boost::any(*storeId);
    }
    if (type) {
      res["type"] = boost::any(*type);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("accelerate_endpoint") != m.end() && !m["accelerate_endpoint"].empty()) {
      accelerateEndpoint = make_shared<string>(boost::any_cast<string>(m["accelerate_endpoint"]));
    }
    if (m.find("base_path") != m.end() && !m["base_path"].empty()) {
      basePath = make_shared<string>(boost::any_cast<string>(m["base_path"]));
    }
    if (m.find("bucket") != m.end() && !m["bucket"].empty()) {
      bucket = make_shared<string>(boost::any_cast<string>(m["bucket"]));
    }
    if (m.find("cdn_endpoint") != m.end() && !m["cdn_endpoint"].empty()) {
      cdnEndpoint = make_shared<string>(boost::any_cast<string>(m["cdn_endpoint"]));
    }
    if (m.find("customized_accelerate_endpoint") != m.end() && !m["customized_accelerate_endpoint"].empty()) {
      customizedAccelerateEndpoint = make_shared<string>(boost::any_cast<string>(m["customized_accelerate_endpoint"]));
    }
    if (m.find("customized_cdn_endpoint") != m.end() && !m["customized_cdn_endpoint"].empty()) {
      customizedCdnEndpoint = make_shared<string>(boost::any_cast<string>(m["customized_cdn_endpoint"]));
    }
    if (m.find("customized_endpoint") != m.end() && !m["customized_endpoint"].empty()) {
      customizedEndpoint = make_shared<string>(boost::any_cast<string>(m["customized_endpoint"]));
    }
    if (m.find("customized_internal_endpoint") != m.end() && !m["customized_internal_endpoint"].empty()) {
      customizedInternalEndpoint = make_shared<string>(boost::any_cast<string>(m["customized_internal_endpoint"]));
    }
    if (m.find("endpoint") != m.end() && !m["endpoint"].empty()) {
      endpoint = make_shared<string>(boost::any_cast<string>(m["endpoint"]));
    }
    if (m.find("internal_endpoint") != m.end() && !m["internal_endpoint"].empty()) {
      internalEndpoint = make_shared<string>(boost::any_cast<string>(m["internal_endpoint"]));
    }
    if (m.find("location") != m.end() && !m["location"].empty()) {
      location = make_shared<string>(boost::any_cast<string>(m["location"]));
    }
    if (m.find("ownership") != m.end() && !m["ownership"].empty()) {
      ownership = make_shared<string>(boost::any_cast<string>(m["ownership"]));
    }
    if (m.find("policy") != m.end() && !m["policy"].empty()) {
      policy = make_shared<string>(boost::any_cast<string>(m["policy"]));
    }
    if (m.find("role_arn") != m.end() && !m["role_arn"].empty()) {
      roleArn = make_shared<string>(boost::any_cast<string>(m["role_arn"]));
    }
    if (m.find("store_id") != m.end() && !m["store_id"].empty()) {
      storeId = make_shared<string>(boost::any_cast<string>(m["store_id"]));
    }
    if (m.find("type") != m.end() && !m["type"].empty()) {
      type = make_shared<string>(boost::any_cast<string>(m["type"]));
    }
  }


  ~Store() = default;
};
class ListStoresResponse : public Darabonba::Model {
public:
  shared_ptr<vector<Store>> items{};

  ListStoresResponse() {}

  explicit ListStoresResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!items) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("items is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (items) {
      vector<boost::any> temp1;
      for(auto item1:*items){
        temp1.push_back(boost::any(item1.toMap()));
      }
      res["items"] = boost::any(temp1);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("items") != m.end() && !m["items"].empty()) {
      if (typeid(vector<boost::any>).name() == m["items"].type().name()) {
        vector<Store> expect1;
        for(auto item1:boost::any_cast<vector<boost::any>>(m["items"])){
          if (typeid(map<string, boost::any>).name() == item1.type().name()) {
            Store model2;
            model2.fromMap(boost::any_cast<map<string, boost::any>>(item1));
            expect1.push_back(model2);
          }
        }
        items = make_shared<vector<Store>>(expect1);
      }
    }
  }


  ~ListStoresResponse() = default;
};
class AdminListStoresModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<ListStoresResponse> body{};

  AdminListStoresModel() {}

  explicit AdminListStoresModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        ListStoresResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<ListStoresResponse>(model1);
      }
    }
  }


  ~AdminListStoresModel() = default;
};
class GetUserAccessTokenModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<AccessTokenResponse> body{};

  GetUserAccessTokenModel() {}

  explicit GetUserAccessTokenModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        AccessTokenResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<AccessTokenResponse>(model1);
      }
    }
  }


  ~GetUserAccessTokenModel() = default;
};
class AddStoreResponse : public Darabonba::Model {
public:
  shared_ptr<string> accelerateEndpoint{};
  shared_ptr<string> basePath{};
  shared_ptr<string> bucket{};
  shared_ptr<string> cdnEndpoint{};
  shared_ptr<string> customizedAccelerateEndpoint{};
  shared_ptr<string> customizedCdnEndpoint{};
  shared_ptr<string> customizedEndpoint{};
  shared_ptr<string> customizedInternalEndpoint{};
  shared_ptr<string> domainId{};
  shared_ptr<string> endpoint{};
  shared_ptr<string> internalEndpoint{};
  shared_ptr<string> location{};
  shared_ptr<string> ownership{};
  shared_ptr<string> policy{};
  shared_ptr<string> roleArn{};
  shared_ptr<string> storeId{};
  shared_ptr<string> type{};

  AddStoreResponse() {}

  explicit AddStoreResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!bucket) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("bucket is required.")));
    }
    if (!domainId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("domainId is required.")));
    }
    if (!endpoint) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("endpoint is required.")));
    }
    if (!ownership) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("ownership is required.")));
    }
    if (!policy) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("policy is required.")));
    }
    if (!storeId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("storeId is required.")));
    }
    if (!type) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("type is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (accelerateEndpoint) {
      res["accelerate_endpoint"] = boost::any(*accelerateEndpoint);
    }
    if (basePath) {
      res["base_path"] = boost::any(*basePath);
    }
    if (bucket) {
      res["bucket"] = boost::any(*bucket);
    }
    if (cdnEndpoint) {
      res["cdn_endpoint"] = boost::any(*cdnEndpoint);
    }
    if (customizedAccelerateEndpoint) {
      res["customized_accelerate_endpoint"] = boost::any(*customizedAccelerateEndpoint);
    }
    if (customizedCdnEndpoint) {
      res["customized_cdn_endpoint"] = boost::any(*customizedCdnEndpoint);
    }
    if (customizedEndpoint) {
      res["customized_endpoint"] = boost::any(*customizedEndpoint);
    }
    if (customizedInternalEndpoint) {
      res["customized_internal_endpoint"] = boost::any(*customizedInternalEndpoint);
    }
    if (domainId) {
      res["domain_id"] = boost::any(*domainId);
    }
    if (endpoint) {
      res["endpoint"] = boost::any(*endpoint);
    }
    if (internalEndpoint) {
      res["internal_endpoint"] = boost::any(*internalEndpoint);
    }
    if (location) {
      res["location"] = boost::any(*location);
    }
    if (ownership) {
      res["ownership"] = boost::any(*ownership);
    }
    if (policy) {
      res["policy"] = boost::any(*policy);
    }
    if (roleArn) {
      res["role_arn"] = boost::any(*roleArn);
    }
    if (storeId) {
      res["store_id"] = boost::any(*storeId);
    }
    if (type) {
      res["type"] = boost::any(*type);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("accelerate_endpoint") != m.end() && !m["accelerate_endpoint"].empty()) {
      accelerateEndpoint = make_shared<string>(boost::any_cast<string>(m["accelerate_endpoint"]));
    }
    if (m.find("base_path") != m.end() && !m["base_path"].empty()) {
      basePath = make_shared<string>(boost::any_cast<string>(m["base_path"]));
    }
    if (m.find("bucket") != m.end() && !m["bucket"].empty()) {
      bucket = make_shared<string>(boost::any_cast<string>(m["bucket"]));
    }
    if (m.find("cdn_endpoint") != m.end() && !m["cdn_endpoint"].empty()) {
      cdnEndpoint = make_shared<string>(boost::any_cast<string>(m["cdn_endpoint"]));
    }
    if (m.find("customized_accelerate_endpoint") != m.end() && !m["customized_accelerate_endpoint"].empty()) {
      customizedAccelerateEndpoint = make_shared<string>(boost::any_cast<string>(m["customized_accelerate_endpoint"]));
    }
    if (m.find("customized_cdn_endpoint") != m.end() && !m["customized_cdn_endpoint"].empty()) {
      customizedCdnEndpoint = make_shared<string>(boost::any_cast<string>(m["customized_cdn_endpoint"]));
    }
    if (m.find("customized_endpoint") != m.end() && !m["customized_endpoint"].empty()) {
      customizedEndpoint = make_shared<string>(boost::any_cast<string>(m["customized_endpoint"]));
    }
    if (m.find("customized_internal_endpoint") != m.end() && !m["customized_internal_endpoint"].empty()) {
      customizedInternalEndpoint = make_shared<string>(boost::any_cast<string>(m["customized_internal_endpoint"]));
    }
    if (m.find("domain_id") != m.end() && !m["domain_id"].empty()) {
      domainId = make_shared<string>(boost::any_cast<string>(m["domain_id"]));
    }
    if (m.find("endpoint") != m.end() && !m["endpoint"].empty()) {
      endpoint = make_shared<string>(boost::any_cast<string>(m["endpoint"]));
    }
    if (m.find("internal_endpoint") != m.end() && !m["internal_endpoint"].empty()) {
      internalEndpoint = make_shared<string>(boost::any_cast<string>(m["internal_endpoint"]));
    }
    if (m.find("location") != m.end() && !m["location"].empty()) {
      location = make_shared<string>(boost::any_cast<string>(m["location"]));
    }
    if (m.find("ownership") != m.end() && !m["ownership"].empty()) {
      ownership = make_shared<string>(boost::any_cast<string>(m["ownership"]));
    }
    if (m.find("policy") != m.end() && !m["policy"].empty()) {
      policy = make_shared<string>(boost::any_cast<string>(m["policy"]));
    }
    if (m.find("role_arn") != m.end() && !m["role_arn"].empty()) {
      roleArn = make_shared<string>(boost::any_cast<string>(m["role_arn"]));
    }
    if (m.find("store_id") != m.end() && !m["store_id"].empty()) {
      storeId = make_shared<string>(boost::any_cast<string>(m["store_id"]));
    }
    if (m.find("type") != m.end() && !m["type"].empty()) {
      type = make_shared<string>(boost::any_cast<string>(m["type"]));
    }
  }


  ~AddStoreResponse() = default;
};
class AdminListStoresRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};

  AdminListStoresRequest() {}

  explicit AdminListStoresRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
  }


  ~AdminListStoresRequest() = default;
};
class AppAccessStrategy : public Darabonba::Model {
public:
  shared_ptr<string> effect{};
  shared_ptr<vector<string>> exceptAppIdList{};

  AppAccessStrategy() {}

  explicit AppAccessStrategy(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (effect) {
      res["effect"] = boost::any(*effect);
    }
    if (exceptAppIdList) {
      res["except_app_id_list"] = boost::any(*exceptAppIdList);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("effect") != m.end() && !m["effect"].empty()) {
      effect = make_shared<string>(boost::any_cast<string>(m["effect"]));
    }
    if (m.find("except_app_id_list") != m.end() && !m["except_app_id_list"].empty()) {
      vector<string> toVec1;
      if (typeid(vector<boost::any>).name() == m["except_app_id_list"].type().name()) {
        vector<boost::any> vec1 = boost::any_cast<vector<boost::any>>(m["except_app_id_list"]);
        for (auto item:vec1) {
           toVec1.push_back(boost::any_cast<string>(item));
        }
      }
      exceptAppIdList = make_shared<vector<string>>(toVec1);
    }
  }


  ~AppAccessStrategy() = default;
};
class AuthConfig : public Darabonba::Model {
public:
  shared_ptr<string> appId{};
  shared_ptr<string> appSecret{};
  shared_ptr<bool> callbackSecurity{};
  shared_ptr<bool> enable{};
  shared_ptr<string> endpoint{};
  shared_ptr<string> enterpriseId{};
  shared_ptr<map<string, boost::any>> loginPageHeaders{};
  shared_ptr<string> loginPageTemplate{};
  shared_ptr<map<string, boost::any>> loginPageVars{};

  AuthConfig() {}

  explicit AuthConfig(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (appId) {
      res["app_id"] = boost::any(*appId);
    }
    if (appSecret) {
      res["app_secret"] = boost::any(*appSecret);
    }
    if (callbackSecurity) {
      res["callback_security"] = boost::any(*callbackSecurity);
    }
    if (enable) {
      res["enable"] = boost::any(*enable);
    }
    if (endpoint) {
      res["endpoint"] = boost::any(*endpoint);
    }
    if (enterpriseId) {
      res["enterprise_id"] = boost::any(*enterpriseId);
    }
    if (loginPageHeaders) {
      res["login_page_headers"] = boost::any(*loginPageHeaders);
    }
    if (loginPageTemplate) {
      res["login_page_template"] = boost::any(*loginPageTemplate);
    }
    if (loginPageVars) {
      res["login_page_vars"] = boost::any(*loginPageVars);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("app_id") != m.end() && !m["app_id"].empty()) {
      appId = make_shared<string>(boost::any_cast<string>(m["app_id"]));
    }
    if (m.find("app_secret") != m.end() && !m["app_secret"].empty()) {
      appSecret = make_shared<string>(boost::any_cast<string>(m["app_secret"]));
    }
    if (m.find("callback_security") != m.end() && !m["callback_security"].empty()) {
      callbackSecurity = make_shared<bool>(boost::any_cast<bool>(m["callback_security"]));
    }
    if (m.find("enable") != m.end() && !m["enable"].empty()) {
      enable = make_shared<bool>(boost::any_cast<bool>(m["enable"]));
    }
    if (m.find("endpoint") != m.end() && !m["endpoint"].empty()) {
      endpoint = make_shared<string>(boost::any_cast<string>(m["endpoint"]));
    }
    if (m.find("enterprise_id") != m.end() && !m["enterprise_id"].empty()) {
      enterpriseId = make_shared<string>(boost::any_cast<string>(m["enterprise_id"]));
    }
    if (m.find("login_page_headers") != m.end() && !m["login_page_headers"].empty()) {
      map<string, boost::any> map1 = boost::any_cast<map<string, boost::any>>(m["login_page_headers"]);
      map<string, boost::any> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      loginPageHeaders = make_shared<map<string, boost::any>>(toMap1);
    }
    if (m.find("login_page_template") != m.end() && !m["login_page_template"].empty()) {
      loginPageTemplate = make_shared<string>(boost::any_cast<string>(m["login_page_template"]));
    }
    if (m.find("login_page_vars") != m.end() && !m["login_page_vars"].empty()) {
      map<string, boost::any> map1 = boost::any_cast<map<string, boost::any>>(m["login_page_vars"]);
      map<string, boost::any> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      loginPageVars = make_shared<map<string, boost::any>>(toMap1);
    }
  }


  ~AuthConfig() = default;
};
class BaseDomainResponse : public Darabonba::Model {
public:
  shared_ptr<string> apiCname{};
  shared_ptr<string> authAlipayAppId{};
  shared_ptr<bool> authAlipayEnable{};
  shared_ptr<string> authAlipayPrivateKey{};
  shared_ptr<map<string, boost::any>> authConfig{};
  shared_ptr<string> authDingdingAppId{};
  shared_ptr<string> authDingdingAppSecret{};
  shared_ptr<bool> authDingdingEnable{};
  shared_ptr<bool> authEndpointEnable{};
  shared_ptr<string> authRamAppId{};
  shared_ptr<string> authRamAppSecret{};
  shared_ptr<bool> authRamEnable{};
  shared_ptr<string> createdAt{};
  shared_ptr<string> dataHashName{};
  shared_ptr<string> description{};
  shared_ptr<string> domainId{};
  shared_ptr<string> domainName{};
  shared_ptr<string> eventFilenameMatches{};
  shared_ptr<string> eventMnsEndpoint{};
  shared_ptr<string> eventMnsTopic{};
  shared_ptr<vector<string>> eventNames{};
  shared_ptr<string> eventRoleArn{};
  shared_ptr<bool> initDriveEnable{};
  shared_ptr<long> initDriveSize{};
  shared_ptr<string> initDriveStoreId{};
  shared_ptr<string> mode{};
  shared_ptr<string> pathType{};
  shared_ptr<AppAccessStrategy> publishedAppAccessStrategy{};
  shared_ptr<bool> sharable{};
  shared_ptr<string> storeLevel{};
  shared_ptr<vector<string>> storeRegionList{};
  shared_ptr<string> updatedAt{};

  BaseDomainResponse() {}

  explicit BaseDomainResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (apiCname) {
      res["api_cname"] = boost::any(*apiCname);
    }
    if (authAlipayAppId) {
      res["auth_alipay_app_id"] = boost::any(*authAlipayAppId);
    }
    if (authAlipayEnable) {
      res["auth_alipay_enable"] = boost::any(*authAlipayEnable);
    }
    if (authAlipayPrivateKey) {
      res["auth_alipay_private_key"] = boost::any(*authAlipayPrivateKey);
    }
    if (authConfig) {
      res["auth_config"] = boost::any(*authConfig);
    }
    if (authDingdingAppId) {
      res["auth_dingding_app_id"] = boost::any(*authDingdingAppId);
    }
    if (authDingdingAppSecret) {
      res["auth_dingding_app_secret"] = boost::any(*authDingdingAppSecret);
    }
    if (authDingdingEnable) {
      res["auth_dingding_enable"] = boost::any(*authDingdingEnable);
    }
    if (authEndpointEnable) {
      res["auth_endpoint_enable"] = boost::any(*authEndpointEnable);
    }
    if (authRamAppId) {
      res["auth_ram_app_id"] = boost::any(*authRamAppId);
    }
    if (authRamAppSecret) {
      res["auth_ram_app_secret"] = boost::any(*authRamAppSecret);
    }
    if (authRamEnable) {
      res["auth_ram_enable"] = boost::any(*authRamEnable);
    }
    if (createdAt) {
      res["created_at"] = boost::any(*createdAt);
    }
    if (dataHashName) {
      res["data_hash_name"] = boost::any(*dataHashName);
    }
    if (description) {
      res["description"] = boost::any(*description);
    }
    if (domainId) {
      res["domain_id"] = boost::any(*domainId);
    }
    if (domainName) {
      res["domain_name"] = boost::any(*domainName);
    }
    if (eventFilenameMatches) {
      res["event_filename_matches"] = boost::any(*eventFilenameMatches);
    }
    if (eventMnsEndpoint) {
      res["event_mns_endpoint"] = boost::any(*eventMnsEndpoint);
    }
    if (eventMnsTopic) {
      res["event_mns_topic"] = boost::any(*eventMnsTopic);
    }
    if (eventNames) {
      res["event_names"] = boost::any(*eventNames);
    }
    if (eventRoleArn) {
      res["event_role_arn"] = boost::any(*eventRoleArn);
    }
    if (initDriveEnable) {
      res["init_drive_enable"] = boost::any(*initDriveEnable);
    }
    if (initDriveSize) {
      res["init_drive_size"] = boost::any(*initDriveSize);
    }
    if (initDriveStoreId) {
      res["init_drive_store_id"] = boost::any(*initDriveStoreId);
    }
    if (mode) {
      res["mode"] = boost::any(*mode);
    }
    if (pathType) {
      res["path_type"] = boost::any(*pathType);
    }
    if (publishedAppAccessStrategy) {
      res["published_app_access_strategy"] = publishedAppAccessStrategy ? boost::any(publishedAppAccessStrategy->toMap()) : boost::any(map<string,boost::any>({}));
    }
    if (sharable) {
      res["sharable"] = boost::any(*sharable);
    }
    if (storeLevel) {
      res["store_level"] = boost::any(*storeLevel);
    }
    if (storeRegionList) {
      res["store_region_list"] = boost::any(*storeRegionList);
    }
    if (updatedAt) {
      res["updated_at"] = boost::any(*updatedAt);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("api_cname") != m.end() && !m["api_cname"].empty()) {
      apiCname = make_shared<string>(boost::any_cast<string>(m["api_cname"]));
    }
    if (m.find("auth_alipay_app_id") != m.end() && !m["auth_alipay_app_id"].empty()) {
      authAlipayAppId = make_shared<string>(boost::any_cast<string>(m["auth_alipay_app_id"]));
    }
    if (m.find("auth_alipay_enable") != m.end() && !m["auth_alipay_enable"].empty()) {
      authAlipayEnable = make_shared<bool>(boost::any_cast<bool>(m["auth_alipay_enable"]));
    }
    if (m.find("auth_alipay_private_key") != m.end() && !m["auth_alipay_private_key"].empty()) {
      authAlipayPrivateKey = make_shared<string>(boost::any_cast<string>(m["auth_alipay_private_key"]));
    }
    if (m.find("auth_config") != m.end() && !m["auth_config"].empty()) {
      map<string, boost::any> map1 = boost::any_cast<map<string, boost::any>>(m["auth_config"]);
      map<string, boost::any> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      authConfig = make_shared<map<string, boost::any>>(toMap1);
    }
    if (m.find("auth_dingding_app_id") != m.end() && !m["auth_dingding_app_id"].empty()) {
      authDingdingAppId = make_shared<string>(boost::any_cast<string>(m["auth_dingding_app_id"]));
    }
    if (m.find("auth_dingding_app_secret") != m.end() && !m["auth_dingding_app_secret"].empty()) {
      authDingdingAppSecret = make_shared<string>(boost::any_cast<string>(m["auth_dingding_app_secret"]));
    }
    if (m.find("auth_dingding_enable") != m.end() && !m["auth_dingding_enable"].empty()) {
      authDingdingEnable = make_shared<bool>(boost::any_cast<bool>(m["auth_dingding_enable"]));
    }
    if (m.find("auth_endpoint_enable") != m.end() && !m["auth_endpoint_enable"].empty()) {
      authEndpointEnable = make_shared<bool>(boost::any_cast<bool>(m["auth_endpoint_enable"]));
    }
    if (m.find("auth_ram_app_id") != m.end() && !m["auth_ram_app_id"].empty()) {
      authRamAppId = make_shared<string>(boost::any_cast<string>(m["auth_ram_app_id"]));
    }
    if (m.find("auth_ram_app_secret") != m.end() && !m["auth_ram_app_secret"].empty()) {
      authRamAppSecret = make_shared<string>(boost::any_cast<string>(m["auth_ram_app_secret"]));
    }
    if (m.find("auth_ram_enable") != m.end() && !m["auth_ram_enable"].empty()) {
      authRamEnable = make_shared<bool>(boost::any_cast<bool>(m["auth_ram_enable"]));
    }
    if (m.find("created_at") != m.end() && !m["created_at"].empty()) {
      createdAt = make_shared<string>(boost::any_cast<string>(m["created_at"]));
    }
    if (m.find("data_hash_name") != m.end() && !m["data_hash_name"].empty()) {
      dataHashName = make_shared<string>(boost::any_cast<string>(m["data_hash_name"]));
    }
    if (m.find("description") != m.end() && !m["description"].empty()) {
      description = make_shared<string>(boost::any_cast<string>(m["description"]));
    }
    if (m.find("domain_id") != m.end() && !m["domain_id"].empty()) {
      domainId = make_shared<string>(boost::any_cast<string>(m["domain_id"]));
    }
    if (m.find("domain_name") != m.end() && !m["domain_name"].empty()) {
      domainName = make_shared<string>(boost::any_cast<string>(m["domain_name"]));
    }
    if (m.find("event_filename_matches") != m.end() && !m["event_filename_matches"].empty()) {
      eventFilenameMatches = make_shared<string>(boost::any_cast<string>(m["event_filename_matches"]));
    }
    if (m.find("event_mns_endpoint") != m.end() && !m["event_mns_endpoint"].empty()) {
      eventMnsEndpoint = make_shared<string>(boost::any_cast<string>(m["event_mns_endpoint"]));
    }
    if (m.find("event_mns_topic") != m.end() && !m["event_mns_topic"].empty()) {
      eventMnsTopic = make_shared<string>(boost::any_cast<string>(m["event_mns_topic"]));
    }
    if (m.find("event_names") != m.end() && !m["event_names"].empty()) {
      vector<string> toVec1;
      if (typeid(vector<boost::any>).name() == m["event_names"].type().name()) {
        vector<boost::any> vec1 = boost::any_cast<vector<boost::any>>(m["event_names"]);
        for (auto item:vec1) {
           toVec1.push_back(boost::any_cast<string>(item));
        }
      }
      eventNames = make_shared<vector<string>>(toVec1);
    }
    if (m.find("event_role_arn") != m.end() && !m["event_role_arn"].empty()) {
      eventRoleArn = make_shared<string>(boost::any_cast<string>(m["event_role_arn"]));
    }
    if (m.find("init_drive_enable") != m.end() && !m["init_drive_enable"].empty()) {
      initDriveEnable = make_shared<bool>(boost::any_cast<bool>(m["init_drive_enable"]));
    }
    if (m.find("init_drive_size") != m.end() && !m["init_drive_size"].empty()) {
      initDriveSize = make_shared<long>(boost::any_cast<long>(m["init_drive_size"]));
    }
    if (m.find("init_drive_store_id") != m.end() && !m["init_drive_store_id"].empty()) {
      initDriveStoreId = make_shared<string>(boost::any_cast<string>(m["init_drive_store_id"]));
    }
    if (m.find("mode") != m.end() && !m["mode"].empty()) {
      mode = make_shared<string>(boost::any_cast<string>(m["mode"]));
    }
    if (m.find("path_type") != m.end() && !m["path_type"].empty()) {
      pathType = make_shared<string>(boost::any_cast<string>(m["path_type"]));
    }
    if (m.find("published_app_access_strategy") != m.end() && !m["published_app_access_strategy"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["published_app_access_strategy"].type().name()) {
        AppAccessStrategy model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["published_app_access_strategy"]));
        publishedAppAccessStrategy = make_shared<AppAccessStrategy>(model1);
      }
    }
    if (m.find("sharable") != m.end() && !m["sharable"].empty()) {
      sharable = make_shared<bool>(boost::any_cast<bool>(m["sharable"]));
    }
    if (m.find("store_level") != m.end() && !m["store_level"].empty()) {
      storeLevel = make_shared<string>(boost::any_cast<string>(m["store_level"]));
    }
    if (m.find("store_region_list") != m.end() && !m["store_region_list"].empty()) {
      vector<string> toVec1;
      if (typeid(vector<boost::any>).name() == m["store_region_list"].type().name()) {
        vector<boost::any> vec1 = boost::any_cast<vector<boost::any>>(m["store_region_list"]);
        for (auto item:vec1) {
           toVec1.push_back(boost::any_cast<string>(item));
        }
      }
      storeRegionList = make_shared<vector<string>>(toVec1);
    }
    if (m.find("updated_at") != m.end() && !m["updated_at"].empty()) {
      updatedAt = make_shared<string>(boost::any_cast<string>(m["updated_at"]));
    }
  }


  ~BaseDomainResponse() = default;
};
class CNameStatus : public Darabonba::Model {
public:
  shared_ptr<string> bingdingState{};
  shared_ptr<string> legalState{};
  shared_ptr<string> remark{};

  CNameStatus() {}

  explicit CNameStatus(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!bingdingState) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("bingdingState is required.")));
    }
    if (!legalState) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("legalState is required.")));
    }
    if (!remark) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("remark is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (bingdingState) {
      res["bingding_state"] = boost::any(*bingdingState);
    }
    if (legalState) {
      res["legal_state"] = boost::any(*legalState);
    }
    if (remark) {
      res["remark"] = boost::any(*remark);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("bingding_state") != m.end() && !m["bingding_state"].empty()) {
      bingdingState = make_shared<string>(boost::any_cast<string>(m["bingding_state"]));
    }
    if (m.find("legal_state") != m.end() && !m["legal_state"].empty()) {
      legalState = make_shared<string>(boost::any_cast<string>(m["legal_state"]));
    }
    if (m.find("remark") != m.end() && !m["remark"].empty()) {
      remark = make_shared<string>(boost::any_cast<string>(m["remark"]));
    }
  }


  ~CNameStatus() = default;
};
class CreateDomainResponse : public Darabonba::Model {
public:
  shared_ptr<string> apiCname{};
  shared_ptr<string> authAlipayAppId{};
  shared_ptr<bool> authAlipayEnable{};
  shared_ptr<string> authAlipayPrivateKey{};
  shared_ptr<map<string, boost::any>> authConfig{};
  shared_ptr<string> authDingdingAppId{};
  shared_ptr<string> authDingdingAppSecret{};
  shared_ptr<bool> authDingdingEnable{};
  shared_ptr<bool> authEndpointEnable{};
  shared_ptr<string> authRamAppId{};
  shared_ptr<string> authRamAppSecret{};
  shared_ptr<bool> authRamEnable{};
  shared_ptr<string> createdAt{};
  shared_ptr<string> dataHashName{};
  shared_ptr<string> description{};
  shared_ptr<string> domainId{};
  shared_ptr<string> domainName{};
  shared_ptr<string> eventFilenameMatches{};
  shared_ptr<string> eventMnsEndpoint{};
  shared_ptr<string> eventMnsTopic{};
  shared_ptr<vector<string>> eventNames{};
  shared_ptr<string> eventRoleArn{};
  shared_ptr<bool> initDriveEnable{};
  shared_ptr<long> initDriveSize{};
  shared_ptr<string> initDriveStoreId{};
  shared_ptr<string> mode{};
  shared_ptr<string> pathType{};
  shared_ptr<AppAccessStrategy> publishedAppAccessStrategy{};
  shared_ptr<bool> sharable{};
  shared_ptr<string> storeLevel{};
  shared_ptr<vector<string>> storeRegionList{};
  shared_ptr<string> updatedAt{};

  CreateDomainResponse() {}

  explicit CreateDomainResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (apiCname) {
      res["api_cname"] = boost::any(*apiCname);
    }
    if (authAlipayAppId) {
      res["auth_alipay_app_id"] = boost::any(*authAlipayAppId);
    }
    if (authAlipayEnable) {
      res["auth_alipay_enable"] = boost::any(*authAlipayEnable);
    }
    if (authAlipayPrivateKey) {
      res["auth_alipay_private_key"] = boost::any(*authAlipayPrivateKey);
    }
    if (authConfig) {
      res["auth_config"] = boost::any(*authConfig);
    }
    if (authDingdingAppId) {
      res["auth_dingding_app_id"] = boost::any(*authDingdingAppId);
    }
    if (authDingdingAppSecret) {
      res["auth_dingding_app_secret"] = boost::any(*authDingdingAppSecret);
    }
    if (authDingdingEnable) {
      res["auth_dingding_enable"] = boost::any(*authDingdingEnable);
    }
    if (authEndpointEnable) {
      res["auth_endpoint_enable"] = boost::any(*authEndpointEnable);
    }
    if (authRamAppId) {
      res["auth_ram_app_id"] = boost::any(*authRamAppId);
    }
    if (authRamAppSecret) {
      res["auth_ram_app_secret"] = boost::any(*authRamAppSecret);
    }
    if (authRamEnable) {
      res["auth_ram_enable"] = boost::any(*authRamEnable);
    }
    if (createdAt) {
      res["created_at"] = boost::any(*createdAt);
    }
    if (dataHashName) {
      res["data_hash_name"] = boost::any(*dataHashName);
    }
    if (description) {
      res["description"] = boost::any(*description);
    }
    if (domainId) {
      res["domain_id"] = boost::any(*domainId);
    }
    if (domainName) {
      res["domain_name"] = boost::any(*domainName);
    }
    if (eventFilenameMatches) {
      res["event_filename_matches"] = boost::any(*eventFilenameMatches);
    }
    if (eventMnsEndpoint) {
      res["event_mns_endpoint"] = boost::any(*eventMnsEndpoint);
    }
    if (eventMnsTopic) {
      res["event_mns_topic"] = boost::any(*eventMnsTopic);
    }
    if (eventNames) {
      res["event_names"] = boost::any(*eventNames);
    }
    if (eventRoleArn) {
      res["event_role_arn"] = boost::any(*eventRoleArn);
    }
    if (initDriveEnable) {
      res["init_drive_enable"] = boost::any(*initDriveEnable);
    }
    if (initDriveSize) {
      res["init_drive_size"] = boost::any(*initDriveSize);
    }
    if (initDriveStoreId) {
      res["init_drive_store_id"] = boost::any(*initDriveStoreId);
    }
    if (mode) {
      res["mode"] = boost::any(*mode);
    }
    if (pathType) {
      res["path_type"] = boost::any(*pathType);
    }
    if (publishedAppAccessStrategy) {
      res["published_app_access_strategy"] = publishedAppAccessStrategy ? boost::any(publishedAppAccessStrategy->toMap()) : boost::any(map<string,boost::any>({}));
    }
    if (sharable) {
      res["sharable"] = boost::any(*sharable);
    }
    if (storeLevel) {
      res["store_level"] = boost::any(*storeLevel);
    }
    if (storeRegionList) {
      res["store_region_list"] = boost::any(*storeRegionList);
    }
    if (updatedAt) {
      res["updated_at"] = boost::any(*updatedAt);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("api_cname") != m.end() && !m["api_cname"].empty()) {
      apiCname = make_shared<string>(boost::any_cast<string>(m["api_cname"]));
    }
    if (m.find("auth_alipay_app_id") != m.end() && !m["auth_alipay_app_id"].empty()) {
      authAlipayAppId = make_shared<string>(boost::any_cast<string>(m["auth_alipay_app_id"]));
    }
    if (m.find("auth_alipay_enable") != m.end() && !m["auth_alipay_enable"].empty()) {
      authAlipayEnable = make_shared<bool>(boost::any_cast<bool>(m["auth_alipay_enable"]));
    }
    if (m.find("auth_alipay_private_key") != m.end() && !m["auth_alipay_private_key"].empty()) {
      authAlipayPrivateKey = make_shared<string>(boost::any_cast<string>(m["auth_alipay_private_key"]));
    }
    if (m.find("auth_config") != m.end() && !m["auth_config"].empty()) {
      map<string, boost::any> map1 = boost::any_cast<map<string, boost::any>>(m["auth_config"]);
      map<string, boost::any> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      authConfig = make_shared<map<string, boost::any>>(toMap1);
    }
    if (m.find("auth_dingding_app_id") != m.end() && !m["auth_dingding_app_id"].empty()) {
      authDingdingAppId = make_shared<string>(boost::any_cast<string>(m["auth_dingding_app_id"]));
    }
    if (m.find("auth_dingding_app_secret") != m.end() && !m["auth_dingding_app_secret"].empty()) {
      authDingdingAppSecret = make_shared<string>(boost::any_cast<string>(m["auth_dingding_app_secret"]));
    }
    if (m.find("auth_dingding_enable") != m.end() && !m["auth_dingding_enable"].empty()) {
      authDingdingEnable = make_shared<bool>(boost::any_cast<bool>(m["auth_dingding_enable"]));
    }
    if (m.find("auth_endpoint_enable") != m.end() && !m["auth_endpoint_enable"].empty()) {
      authEndpointEnable = make_shared<bool>(boost::any_cast<bool>(m["auth_endpoint_enable"]));
    }
    if (m.find("auth_ram_app_id") != m.end() && !m["auth_ram_app_id"].empty()) {
      authRamAppId = make_shared<string>(boost::any_cast<string>(m["auth_ram_app_id"]));
    }
    if (m.find("auth_ram_app_secret") != m.end() && !m["auth_ram_app_secret"].empty()) {
      authRamAppSecret = make_shared<string>(boost::any_cast<string>(m["auth_ram_app_secret"]));
    }
    if (m.find("auth_ram_enable") != m.end() && !m["auth_ram_enable"].empty()) {
      authRamEnable = make_shared<bool>(boost::any_cast<bool>(m["auth_ram_enable"]));
    }
    if (m.find("created_at") != m.end() && !m["created_at"].empty()) {
      createdAt = make_shared<string>(boost::any_cast<string>(m["created_at"]));
    }
    if (m.find("data_hash_name") != m.end() && !m["data_hash_name"].empty()) {
      dataHashName = make_shared<string>(boost::any_cast<string>(m["data_hash_name"]));
    }
    if (m.find("description") != m.end() && !m["description"].empty()) {
      description = make_shared<string>(boost::any_cast<string>(m["description"]));
    }
    if (m.find("domain_id") != m.end() && !m["domain_id"].empty()) {
      domainId = make_shared<string>(boost::any_cast<string>(m["domain_id"]));
    }
    if (m.find("domain_name") != m.end() && !m["domain_name"].empty()) {
      domainName = make_shared<string>(boost::any_cast<string>(m["domain_name"]));
    }
    if (m.find("event_filename_matches") != m.end() && !m["event_filename_matches"].empty()) {
      eventFilenameMatches = make_shared<string>(boost::any_cast<string>(m["event_filename_matches"]));
    }
    if (m.find("event_mns_endpoint") != m.end() && !m["event_mns_endpoint"].empty()) {
      eventMnsEndpoint = make_shared<string>(boost::any_cast<string>(m["event_mns_endpoint"]));
    }
    if (m.find("event_mns_topic") != m.end() && !m["event_mns_topic"].empty()) {
      eventMnsTopic = make_shared<string>(boost::any_cast<string>(m["event_mns_topic"]));
    }
    if (m.find("event_names") != m.end() && !m["event_names"].empty()) {
      vector<string> toVec1;
      if (typeid(vector<boost::any>).name() == m["event_names"].type().name()) {
        vector<boost::any> vec1 = boost::any_cast<vector<boost::any>>(m["event_names"]);
        for (auto item:vec1) {
           toVec1.push_back(boost::any_cast<string>(item));
        }
      }
      eventNames = make_shared<vector<string>>(toVec1);
    }
    if (m.find("event_role_arn") != m.end() && !m["event_role_arn"].empty()) {
      eventRoleArn = make_shared<string>(boost::any_cast<string>(m["event_role_arn"]));
    }
    if (m.find("init_drive_enable") != m.end() && !m["init_drive_enable"].empty()) {
      initDriveEnable = make_shared<bool>(boost::any_cast<bool>(m["init_drive_enable"]));
    }
    if (m.find("init_drive_size") != m.end() && !m["init_drive_size"].empty()) {
      initDriveSize = make_shared<long>(boost::any_cast<long>(m["init_drive_size"]));
    }
    if (m.find("init_drive_store_id") != m.end() && !m["init_drive_store_id"].empty()) {
      initDriveStoreId = make_shared<string>(boost::any_cast<string>(m["init_drive_store_id"]));
    }
    if (m.find("mode") != m.end() && !m["mode"].empty()) {
      mode = make_shared<string>(boost::any_cast<string>(m["mode"]));
    }
    if (m.find("path_type") != m.end() && !m["path_type"].empty()) {
      pathType = make_shared<string>(boost::any_cast<string>(m["path_type"]));
    }
    if (m.find("published_app_access_strategy") != m.end() && !m["published_app_access_strategy"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["published_app_access_strategy"].type().name()) {
        AppAccessStrategy model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["published_app_access_strategy"]));
        publishedAppAccessStrategy = make_shared<AppAccessStrategy>(model1);
      }
    }
    if (m.find("sharable") != m.end() && !m["sharable"].empty()) {
      sharable = make_shared<bool>(boost::any_cast<bool>(m["sharable"]));
    }
    if (m.find("store_level") != m.end() && !m["store_level"].empty()) {
      storeLevel = make_shared<string>(boost::any_cast<string>(m["store_level"]));
    }
    if (m.find("store_region_list") != m.end() && !m["store_region_list"].empty()) {
      vector<string> toVec1;
      if (typeid(vector<boost::any>).name() == m["store_region_list"].type().name()) {
        vector<boost::any> vec1 = boost::any_cast<vector<boost::any>>(m["store_region_list"]);
        for (auto item:vec1) {
           toVec1.push_back(boost::any_cast<string>(item));
        }
      }
      storeRegionList = make_shared<vector<string>>(toVec1);
    }
    if (m.find("updated_at") != m.end() && !m["updated_at"].empty()) {
      updatedAt = make_shared<string>(boost::any_cast<string>(m["updated_at"]));
    }
  }


  ~CreateDomainResponse() = default;
};
class DataCName : public Darabonba::Model {
public:
  shared_ptr<string> dataCname{};
  shared_ptr<string> location{};

  DataCName() {}

  explicit DataCName(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!dataCname) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("dataCname is required.")));
    }
    if (!location) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("location is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (dataCname) {
      res["data_cname"] = boost::any(*dataCname);
    }
    if (location) {
      res["location"] = boost::any(*location);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("data_cname") != m.end() && !m["data_cname"].empty()) {
      dataCname = make_shared<string>(boost::any_cast<string>(m["data_cname"]));
    }
    if (m.find("location") != m.end() && !m["location"].empty()) {
      location = make_shared<string>(boost::any_cast<string>(m["location"]));
    }
  }


  ~DataCName() = default;
};
class DomainCNameResponse : public Darabonba::Model {
public:
  shared_ptr<vector<DataCName>> dataCnameList{};
  shared_ptr<string> domainId{};

  DomainCNameResponse() {}

  explicit DomainCNameResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!dataCnameList) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("dataCnameList is required.")));
    }
    if (!domainId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("domainId is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (dataCnameList) {
      vector<boost::any> temp1;
      for(auto item1:*dataCnameList){
        temp1.push_back(boost::any(item1.toMap()));
      }
      res["data_cname_list"] = boost::any(temp1);
    }
    if (domainId) {
      res["domain_id"] = boost::any(*domainId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("data_cname_list") != m.end() && !m["data_cname_list"].empty()) {
      if (typeid(vector<boost::any>).name() == m["data_cname_list"].type().name()) {
        vector<DataCName> expect1;
        for(auto item1:boost::any_cast<vector<boost::any>>(m["data_cname_list"])){
          if (typeid(map<string, boost::any>).name() == item1.type().name()) {
            DataCName model2;
            model2.fromMap(boost::any_cast<map<string, boost::any>>(item1));
            expect1.push_back(model2);
          }
        }
        dataCnameList = make_shared<vector<DataCName>>(expect1);
      }
    }
    if (m.find("domain_id") != m.end() && !m["domain_id"].empty()) {
      domainId = make_shared<string>(boost::any_cast<string>(m["domain_id"]));
    }
  }


  ~DomainCNameResponse() = default;
};
class GetAppResponse : public Darabonba::Model {
public:
  shared_ptr<string> aliOwnerId{};
  shared_ptr<string> appId{};
  shared_ptr<string> appName{};
  shared_ptr<string> appSecret{};
  shared_ptr<string> createdAt{};
  shared_ptr<string> description{};
  shared_ptr<string> logo{};
  shared_ptr<string> provider{};
  shared_ptr<string> redirectUri{};
  shared_ptr<vector<string>> scope{};
  shared_ptr<vector<string>> screenshots{};
  shared_ptr<string> stage{};
  shared_ptr<string> type{};
  shared_ptr<string> updatedAt{};

  GetAppResponse() {}

  explicit GetAppResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!aliOwnerId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("aliOwnerId is required.")));
    }
    if (!appId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("appId is required.")));
    }
    if (!appName) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("appName is required.")));
    }
    Darabonba::Model::validateMaxLength("appName", appName, 128);
    Darabonba::Model::validateMinLength("appName", appName, 1);
    Darabonba::Model::validatePattern("appName", appName, "[0-9a-zA-Z]+");
    if (!appSecret) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("appSecret is required.")));
    }
    if (!createdAt) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("createdAt is required.")));
    }
    if (!description) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("description is required.")));
    }
    Darabonba::Model::validateMaxLength("description", description, 128);
    Darabonba::Model::validateMinLength("description", description, 0);
    if (!logo) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("logo is required.")));
    }
    if (!provider) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("provider is required.")));
    }
    if (!redirectUri) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("redirectUri is required.")));
    }
    if (!scope) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("scope is required.")));
    }
    if (!screenshots) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("screenshots is required.")));
    }
    if (!stage) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("stage is required.")));
    }
    if (!type) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("type is required.")));
    }
    if (!updatedAt) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("updatedAt is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (aliOwnerId) {
      res["ali_owner_id"] = boost::any(*aliOwnerId);
    }
    if (appId) {
      res["app_id"] = boost::any(*appId);
    }
    if (appName) {
      res["app_name"] = boost::any(*appName);
    }
    if (appSecret) {
      res["app_secret"] = boost::any(*appSecret);
    }
    if (createdAt) {
      res["created_at"] = boost::any(*createdAt);
    }
    if (description) {
      res["description"] = boost::any(*description);
    }
    if (logo) {
      res["logo"] = boost::any(*logo);
    }
    if (provider) {
      res["provider"] = boost::any(*provider);
    }
    if (redirectUri) {
      res["redirect_uri"] = boost::any(*redirectUri);
    }
    if (scope) {
      res["scope"] = boost::any(*scope);
    }
    if (screenshots) {
      res["screenshots"] = boost::any(*screenshots);
    }
    if (stage) {
      res["stage"] = boost::any(*stage);
    }
    if (type) {
      res["type"] = boost::any(*type);
    }
    if (updatedAt) {
      res["updated_at"] = boost::any(*updatedAt);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("ali_owner_id") != m.end() && !m["ali_owner_id"].empty()) {
      aliOwnerId = make_shared<string>(boost::any_cast<string>(m["ali_owner_id"]));
    }
    if (m.find("app_id") != m.end() && !m["app_id"].empty()) {
      appId = make_shared<string>(boost::any_cast<string>(m["app_id"]));
    }
    if (m.find("app_name") != m.end() && !m["app_name"].empty()) {
      appName = make_shared<string>(boost::any_cast<string>(m["app_name"]));
    }
    if (m.find("app_secret") != m.end() && !m["app_secret"].empty()) {
      appSecret = make_shared<string>(boost::any_cast<string>(m["app_secret"]));
    }
    if (m.find("created_at") != m.end() && !m["created_at"].empty()) {
      createdAt = make_shared<string>(boost::any_cast<string>(m["created_at"]));
    }
    if (m.find("description") != m.end() && !m["description"].empty()) {
      description = make_shared<string>(boost::any_cast<string>(m["description"]));
    }
    if (m.find("logo") != m.end() && !m["logo"].empty()) {
      logo = make_shared<string>(boost::any_cast<string>(m["logo"]));
    }
    if (m.find("provider") != m.end() && !m["provider"].empty()) {
      provider = make_shared<string>(boost::any_cast<string>(m["provider"]));
    }
    if (m.find("redirect_uri") != m.end() && !m["redirect_uri"].empty()) {
      redirectUri = make_shared<string>(boost::any_cast<string>(m["redirect_uri"]));
    }
    if (m.find("scope") != m.end() && !m["scope"].empty()) {
      vector<string> toVec1;
      if (typeid(vector<boost::any>).name() == m["scope"].type().name()) {
        vector<boost::any> vec1 = boost::any_cast<vector<boost::any>>(m["scope"]);
        for (auto item:vec1) {
           toVec1.push_back(boost::any_cast<string>(item));
        }
      }
      scope = make_shared<vector<string>>(toVec1);
    }
    if (m.find("screenshots") != m.end() && !m["screenshots"].empty()) {
      vector<string> toVec1;
      if (typeid(vector<boost::any>).name() == m["screenshots"].type().name()) {
        vector<boost::any> vec1 = boost::any_cast<vector<boost::any>>(m["screenshots"]);
        for (auto item:vec1) {
           toVec1.push_back(boost::any_cast<string>(item));
        }
      }
      screenshots = make_shared<vector<string>>(toVec1);
    }
    if (m.find("stage") != m.end() && !m["stage"].empty()) {
      stage = make_shared<string>(boost::any_cast<string>(m["stage"]));
    }
    if (m.find("type") != m.end() && !m["type"].empty()) {
      type = make_shared<string>(boost::any_cast<string>(m["type"]));
    }
    if (m.find("updated_at") != m.end() && !m["updated_at"].empty()) {
      updatedAt = make_shared<string>(boost::any_cast<string>(m["updated_at"]));
    }
  }


  ~GetAppResponse() = default;
};
class GetBizCNameInfoResponse : public Darabonba::Model {
public:
  shared_ptr<string> bizCname{};
  shared_ptr<string> certId{};
  shared_ptr<string> certName{};
  shared_ptr<CNameStatus> cnameStatus{};
  shared_ptr<string> cnameType{};
  shared_ptr<string> domainId{};
  shared_ptr<bool> isVpc{};

  GetBizCNameInfoResponse() {}

  explicit GetBizCNameInfoResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!domainId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("domainId is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (bizCname) {
      res["biz_cname"] = boost::any(*bizCname);
    }
    if (certId) {
      res["cert_id"] = boost::any(*certId);
    }
    if (certName) {
      res["cert_name"] = boost::any(*certName);
    }
    if (cnameStatus) {
      res["cname_status"] = cnameStatus ? boost::any(cnameStatus->toMap()) : boost::any(map<string,boost::any>({}));
    }
    if (cnameType) {
      res["cname_type"] = boost::any(*cnameType);
    }
    if (domainId) {
      res["domain_id"] = boost::any(*domainId);
    }
    if (isVpc) {
      res["is_vpc"] = boost::any(*isVpc);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("biz_cname") != m.end() && !m["biz_cname"].empty()) {
      bizCname = make_shared<string>(boost::any_cast<string>(m["biz_cname"]));
    }
    if (m.find("cert_id") != m.end() && !m["cert_id"].empty()) {
      certId = make_shared<string>(boost::any_cast<string>(m["cert_id"]));
    }
    if (m.find("cert_name") != m.end() && !m["cert_name"].empty()) {
      certName = make_shared<string>(boost::any_cast<string>(m["cert_name"]));
    }
    if (m.find("cname_status") != m.end() && !m["cname_status"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["cname_status"].type().name()) {
        CNameStatus model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["cname_status"]));
        cnameStatus = make_shared<CNameStatus>(model1);
      }
    }
    if (m.find("cname_type") != m.end() && !m["cname_type"].empty()) {
      cnameType = make_shared<string>(boost::any_cast<string>(m["cname_type"]));
    }
    if (m.find("domain_id") != m.end() && !m["domain_id"].empty()) {
      domainId = make_shared<string>(boost::any_cast<string>(m["domain_id"]));
    }
    if (m.find("is_vpc") != m.end() && !m["is_vpc"].empty()) {
      isVpc = make_shared<bool>(boost::any_cast<bool>(m["is_vpc"]));
    }
  }


  ~GetBizCNameInfoResponse() = default;
};
class GetDomainResponse : public Darabonba::Model {
public:
  shared_ptr<string> apiCname{};
  shared_ptr<string> authAlipayAppId{};
  shared_ptr<bool> authAlipayEnable{};
  shared_ptr<string> authAlipayPrivateKey{};
  shared_ptr<map<string, boost::any>> authConfig{};
  shared_ptr<string> authDingdingAppId{};
  shared_ptr<string> authDingdingAppSecret{};
  shared_ptr<bool> authDingdingEnable{};
  shared_ptr<bool> authEndpointEnable{};
  shared_ptr<string> authRamAppId{};
  shared_ptr<string> authRamAppSecret{};
  shared_ptr<bool> authRamEnable{};
  shared_ptr<string> createdAt{};
  shared_ptr<string> dataHashName{};
  shared_ptr<string> description{};
  shared_ptr<string> domainId{};
  shared_ptr<string> domainName{};
  shared_ptr<string> eventFilenameMatches{};
  shared_ptr<string> eventMnsEndpoint{};
  shared_ptr<string> eventMnsTopic{};
  shared_ptr<vector<string>> eventNames{};
  shared_ptr<string> eventRoleArn{};
  shared_ptr<bool> initDriveEnable{};
  shared_ptr<long> initDriveSize{};
  shared_ptr<string> initDriveStoreId{};
  shared_ptr<string> mode{};
  shared_ptr<string> pathType{};
  shared_ptr<AppAccessStrategy> publishedAppAccessStrategy{};
  shared_ptr<bool> sharable{};
  shared_ptr<string> storeLevel{};
  shared_ptr<vector<string>> storeRegionList{};
  shared_ptr<string> updatedAt{};

  GetDomainResponse() {}

  explicit GetDomainResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (apiCname) {
      res["api_cname"] = boost::any(*apiCname);
    }
    if (authAlipayAppId) {
      res["auth_alipay_app_id"] = boost::any(*authAlipayAppId);
    }
    if (authAlipayEnable) {
      res["auth_alipay_enable"] = boost::any(*authAlipayEnable);
    }
    if (authAlipayPrivateKey) {
      res["auth_alipay_private_key"] = boost::any(*authAlipayPrivateKey);
    }
    if (authConfig) {
      res["auth_config"] = boost::any(*authConfig);
    }
    if (authDingdingAppId) {
      res["auth_dingding_app_id"] = boost::any(*authDingdingAppId);
    }
    if (authDingdingAppSecret) {
      res["auth_dingding_app_secret"] = boost::any(*authDingdingAppSecret);
    }
    if (authDingdingEnable) {
      res["auth_dingding_enable"] = boost::any(*authDingdingEnable);
    }
    if (authEndpointEnable) {
      res["auth_endpoint_enable"] = boost::any(*authEndpointEnable);
    }
    if (authRamAppId) {
      res["auth_ram_app_id"] = boost::any(*authRamAppId);
    }
    if (authRamAppSecret) {
      res["auth_ram_app_secret"] = boost::any(*authRamAppSecret);
    }
    if (authRamEnable) {
      res["auth_ram_enable"] = boost::any(*authRamEnable);
    }
    if (createdAt) {
      res["created_at"] = boost::any(*createdAt);
    }
    if (dataHashName) {
      res["data_hash_name"] = boost::any(*dataHashName);
    }
    if (description) {
      res["description"] = boost::any(*description);
    }
    if (domainId) {
      res["domain_id"] = boost::any(*domainId);
    }
    if (domainName) {
      res["domain_name"] = boost::any(*domainName);
    }
    if (eventFilenameMatches) {
      res["event_filename_matches"] = boost::any(*eventFilenameMatches);
    }
    if (eventMnsEndpoint) {
      res["event_mns_endpoint"] = boost::any(*eventMnsEndpoint);
    }
    if (eventMnsTopic) {
      res["event_mns_topic"] = boost::any(*eventMnsTopic);
    }
    if (eventNames) {
      res["event_names"] = boost::any(*eventNames);
    }
    if (eventRoleArn) {
      res["event_role_arn"] = boost::any(*eventRoleArn);
    }
    if (initDriveEnable) {
      res["init_drive_enable"] = boost::any(*initDriveEnable);
    }
    if (initDriveSize) {
      res["init_drive_size"] = boost::any(*initDriveSize);
    }
    if (initDriveStoreId) {
      res["init_drive_store_id"] = boost::any(*initDriveStoreId);
    }
    if (mode) {
      res["mode"] = boost::any(*mode);
    }
    if (pathType) {
      res["path_type"] = boost::any(*pathType);
    }
    if (publishedAppAccessStrategy) {
      res["published_app_access_strategy"] = publishedAppAccessStrategy ? boost::any(publishedAppAccessStrategy->toMap()) : boost::any(map<string,boost::any>({}));
    }
    if (sharable) {
      res["sharable"] = boost::any(*sharable);
    }
    if (storeLevel) {
      res["store_level"] = boost::any(*storeLevel);
    }
    if (storeRegionList) {
      res["store_region_list"] = boost::any(*storeRegionList);
    }
    if (updatedAt) {
      res["updated_at"] = boost::any(*updatedAt);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("api_cname") != m.end() && !m["api_cname"].empty()) {
      apiCname = make_shared<string>(boost::any_cast<string>(m["api_cname"]));
    }
    if (m.find("auth_alipay_app_id") != m.end() && !m["auth_alipay_app_id"].empty()) {
      authAlipayAppId = make_shared<string>(boost::any_cast<string>(m["auth_alipay_app_id"]));
    }
    if (m.find("auth_alipay_enable") != m.end() && !m["auth_alipay_enable"].empty()) {
      authAlipayEnable = make_shared<bool>(boost::any_cast<bool>(m["auth_alipay_enable"]));
    }
    if (m.find("auth_alipay_private_key") != m.end() && !m["auth_alipay_private_key"].empty()) {
      authAlipayPrivateKey = make_shared<string>(boost::any_cast<string>(m["auth_alipay_private_key"]));
    }
    if (m.find("auth_config") != m.end() && !m["auth_config"].empty()) {
      map<string, boost::any> map1 = boost::any_cast<map<string, boost::any>>(m["auth_config"]);
      map<string, boost::any> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      authConfig = make_shared<map<string, boost::any>>(toMap1);
    }
    if (m.find("auth_dingding_app_id") != m.end() && !m["auth_dingding_app_id"].empty()) {
      authDingdingAppId = make_shared<string>(boost::any_cast<string>(m["auth_dingding_app_id"]));
    }
    if (m.find("auth_dingding_app_secret") != m.end() && !m["auth_dingding_app_secret"].empty()) {
      authDingdingAppSecret = make_shared<string>(boost::any_cast<string>(m["auth_dingding_app_secret"]));
    }
    if (m.find("auth_dingding_enable") != m.end() && !m["auth_dingding_enable"].empty()) {
      authDingdingEnable = make_shared<bool>(boost::any_cast<bool>(m["auth_dingding_enable"]));
    }
    if (m.find("auth_endpoint_enable") != m.end() && !m["auth_endpoint_enable"].empty()) {
      authEndpointEnable = make_shared<bool>(boost::any_cast<bool>(m["auth_endpoint_enable"]));
    }
    if (m.find("auth_ram_app_id") != m.end() && !m["auth_ram_app_id"].empty()) {
      authRamAppId = make_shared<string>(boost::any_cast<string>(m["auth_ram_app_id"]));
    }
    if (m.find("auth_ram_app_secret") != m.end() && !m["auth_ram_app_secret"].empty()) {
      authRamAppSecret = make_shared<string>(boost::any_cast<string>(m["auth_ram_app_secret"]));
    }
    if (m.find("auth_ram_enable") != m.end() && !m["auth_ram_enable"].empty()) {
      authRamEnable = make_shared<bool>(boost::any_cast<bool>(m["auth_ram_enable"]));
    }
    if (m.find("created_at") != m.end() && !m["created_at"].empty()) {
      createdAt = make_shared<string>(boost::any_cast<string>(m["created_at"]));
    }
    if (m.find("data_hash_name") != m.end() && !m["data_hash_name"].empty()) {
      dataHashName = make_shared<string>(boost::any_cast<string>(m["data_hash_name"]));
    }
    if (m.find("description") != m.end() && !m["description"].empty()) {
      description = make_shared<string>(boost::any_cast<string>(m["description"]));
    }
    if (m.find("domain_id") != m.end() && !m["domain_id"].empty()) {
      domainId = make_shared<string>(boost::any_cast<string>(m["domain_id"]));
    }
    if (m.find("domain_name") != m.end() && !m["domain_name"].empty()) {
      domainName = make_shared<string>(boost::any_cast<string>(m["domain_name"]));
    }
    if (m.find("event_filename_matches") != m.end() && !m["event_filename_matches"].empty()) {
      eventFilenameMatches = make_shared<string>(boost::any_cast<string>(m["event_filename_matches"]));
    }
    if (m.find("event_mns_endpoint") != m.end() && !m["event_mns_endpoint"].empty()) {
      eventMnsEndpoint = make_shared<string>(boost::any_cast<string>(m["event_mns_endpoint"]));
    }
    if (m.find("event_mns_topic") != m.end() && !m["event_mns_topic"].empty()) {
      eventMnsTopic = make_shared<string>(boost::any_cast<string>(m["event_mns_topic"]));
    }
    if (m.find("event_names") != m.end() && !m["event_names"].empty()) {
      vector<string> toVec1;
      if (typeid(vector<boost::any>).name() == m["event_names"].type().name()) {
        vector<boost::any> vec1 = boost::any_cast<vector<boost::any>>(m["event_names"]);
        for (auto item:vec1) {
           toVec1.push_back(boost::any_cast<string>(item));
        }
      }
      eventNames = make_shared<vector<string>>(toVec1);
    }
    if (m.find("event_role_arn") != m.end() && !m["event_role_arn"].empty()) {
      eventRoleArn = make_shared<string>(boost::any_cast<string>(m["event_role_arn"]));
    }
    if (m.find("init_drive_enable") != m.end() && !m["init_drive_enable"].empty()) {
      initDriveEnable = make_shared<bool>(boost::any_cast<bool>(m["init_drive_enable"]));
    }
    if (m.find("init_drive_size") != m.end() && !m["init_drive_size"].empty()) {
      initDriveSize = make_shared<long>(boost::any_cast<long>(m["init_drive_size"]));
    }
    if (m.find("init_drive_store_id") != m.end() && !m["init_drive_store_id"].empty()) {
      initDriveStoreId = make_shared<string>(boost::any_cast<string>(m["init_drive_store_id"]));
    }
    if (m.find("mode") != m.end() && !m["mode"].empty()) {
      mode = make_shared<string>(boost::any_cast<string>(m["mode"]));
    }
    if (m.find("path_type") != m.end() && !m["path_type"].empty()) {
      pathType = make_shared<string>(boost::any_cast<string>(m["path_type"]));
    }
    if (m.find("published_app_access_strategy") != m.end() && !m["published_app_access_strategy"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["published_app_access_strategy"].type().name()) {
        AppAccessStrategy model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["published_app_access_strategy"]));
        publishedAppAccessStrategy = make_shared<AppAccessStrategy>(model1);
      }
    }
    if (m.find("sharable") != m.end() && !m["sharable"].empty()) {
      sharable = make_shared<bool>(boost::any_cast<bool>(m["sharable"]));
    }
    if (m.find("store_level") != m.end() && !m["store_level"].empty()) {
      storeLevel = make_shared<string>(boost::any_cast<string>(m["store_level"]));
    }
    if (m.find("store_region_list") != m.end() && !m["store_region_list"].empty()) {
      vector<string> toVec1;
      if (typeid(vector<boost::any>).name() == m["store_region_list"].type().name()) {
        vector<boost::any> vec1 = boost::any_cast<vector<boost::any>>(m["store_region_list"]);
        for (auto item:vec1) {
           toVec1.push_back(boost::any_cast<string>(item));
        }
      }
      storeRegionList = make_shared<vector<string>>(toVec1);
    }
    if (m.find("updated_at") != m.end() && !m["updated_at"].empty()) {
      updatedAt = make_shared<string>(boost::any_cast<string>(m["updated_at"]));
    }
  }


  ~GetDomainResponse() = default;
};
class GetUserAccessTokenRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<string> role{};
  shared_ptr<string> userId{};

  GetUserAccessTokenRequest() {}

  explicit GetUserAccessTokenRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!userId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("userId is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (role) {
      res["role"] = boost::any(*role);
    }
    if (userId) {
      res["user_id"] = boost::any(*userId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("role") != m.end() && !m["role"].empty()) {
      role = make_shared<string>(boost::any_cast<string>(m["role"]));
    }
    if (m.find("user_id") != m.end() && !m["user_id"].empty()) {
      userId = make_shared<string>(boost::any_cast<string>(m["user_id"]));
    }
  }


  ~GetUserAccessTokenRequest() = default;
};
class ListAppsResponse : public Darabonba::Model {
public:
  shared_ptr<vector<GetAppResponse>> items{};
  shared_ptr<string> nextMarker{};

  ListAppsResponse() {}

  explicit ListAppsResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!items) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("items is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (items) {
      vector<boost::any> temp1;
      for(auto item1:*items){
        temp1.push_back(boost::any(item1.toMap()));
      }
      res["items"] = boost::any(temp1);
    }
    if (nextMarker) {
      res["next_marker"] = boost::any(*nextMarker);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("items") != m.end() && !m["items"].empty()) {
      if (typeid(vector<boost::any>).name() == m["items"].type().name()) {
        vector<GetAppResponse> expect1;
        for(auto item1:boost::any_cast<vector<boost::any>>(m["items"])){
          if (typeid(map<string, boost::any>).name() == item1.type().name()) {
            GetAppResponse model2;
            model2.fromMap(boost::any_cast<map<string, boost::any>>(item1));
            expect1.push_back(model2);
          }
        }
        items = make_shared<vector<GetAppResponse>>(expect1);
      }
    }
    if (m.find("next_marker") != m.end() && !m["next_marker"].empty()) {
      nextMarker = make_shared<string>(boost::any_cast<string>(m["next_marker"]));
    }
  }


  ~ListAppsResponse() = default;
};
class ListDomainCORSRuleResponse : public Darabonba::Model {
public:
  shared_ptr<vector<CorsRule>> corsRuleList{};
  shared_ptr<string> domainId{};

  ListDomainCORSRuleResponse() {}

  explicit ListDomainCORSRuleResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (corsRuleList) {
      vector<boost::any> temp1;
      for(auto item1:*corsRuleList){
        temp1.push_back(boost::any(item1.toMap()));
      }
      res["cors_rule_list"] = boost::any(temp1);
    }
    if (domainId) {
      res["domain_id"] = boost::any(*domainId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("cors_rule_list") != m.end() && !m["cors_rule_list"].empty()) {
      if (typeid(vector<boost::any>).name() == m["cors_rule_list"].type().name()) {
        vector<CorsRule> expect1;
        for(auto item1:boost::any_cast<vector<boost::any>>(m["cors_rule_list"])){
          if (typeid(map<string, boost::any>).name() == item1.type().name()) {
            CorsRule model2;
            model2.fromMap(boost::any_cast<map<string, boost::any>>(item1));
            expect1.push_back(model2);
          }
        }
        corsRuleList = make_shared<vector<CorsRule>>(expect1);
      }
    }
    if (m.find("domain_id") != m.end() && !m["domain_id"].empty()) {
      domainId = make_shared<string>(boost::any_cast<string>(m["domain_id"]));
    }
  }


  ~ListDomainCORSRuleResponse() = default;
};
class ListDomainsResponse : public Darabonba::Model {
public:
  shared_ptr<vector<BaseDomainResponse>> items{};
  shared_ptr<string> nextMarker{};

  ListDomainsResponse() {}

  explicit ListDomainsResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (items) {
      vector<boost::any> temp1;
      for(auto item1:*items){
        temp1.push_back(boost::any(item1.toMap()));
      }
      res["items"] = boost::any(temp1);
    }
    if (nextMarker) {
      res["next_marker"] = boost::any(*nextMarker);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("items") != m.end() && !m["items"].empty()) {
      if (typeid(vector<boost::any>).name() == m["items"].type().name()) {
        vector<BaseDomainResponse> expect1;
        for(auto item1:boost::any_cast<vector<boost::any>>(m["items"])){
          if (typeid(map<string, boost::any>).name() == item1.type().name()) {
            BaseDomainResponse model2;
            model2.fromMap(boost::any_cast<map<string, boost::any>>(item1));
            expect1.push_back(model2);
          }
        }
        items = make_shared<vector<BaseDomainResponse>>(expect1);
      }
    }
    if (m.find("next_marker") != m.end() && !m["next_marker"].empty()) {
      nextMarker = make_shared<string>(boost::any_cast<string>(m["next_marker"]));
    }
  }


  ~ListDomainsResponse() = default;
};
class SetBizCNameCertResponse : public Darabonba::Model {
public:
  shared_ptr<string> bizCname{};
  shared_ptr<string> certName{};
  shared_ptr<string> cnameType{};
  shared_ptr<string> domainId{};
  shared_ptr<bool> isVpc{};

  SetBizCNameCertResponse() {}

  explicit SetBizCNameCertResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!domainId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("domainId is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (bizCname) {
      res["biz_cname"] = boost::any(*bizCname);
    }
    if (certName) {
      res["cert_name"] = boost::any(*certName);
    }
    if (cnameType) {
      res["cname_type"] = boost::any(*cnameType);
    }
    if (domainId) {
      res["domain_id"] = boost::any(*domainId);
    }
    if (isVpc) {
      res["is_vpc"] = boost::any(*isVpc);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("biz_cname") != m.end() && !m["biz_cname"].empty()) {
      bizCname = make_shared<string>(boost::any_cast<string>(m["biz_cname"]));
    }
    if (m.find("cert_name") != m.end() && !m["cert_name"].empty()) {
      certName = make_shared<string>(boost::any_cast<string>(m["cert_name"]));
    }
    if (m.find("cname_type") != m.end() && !m["cname_type"].empty()) {
      cnameType = make_shared<string>(boost::any_cast<string>(m["cname_type"]));
    }
    if (m.find("domain_id") != m.end() && !m["domain_id"].empty()) {
      domainId = make_shared<string>(boost::any_cast<string>(m["domain_id"]));
    }
    if (m.find("is_vpc") != m.end() && !m["is_vpc"].empty()) {
      isVpc = make_shared<bool>(boost::any_cast<bool>(m["is_vpc"]));
    }
  }


  ~SetBizCNameCertResponse() = default;
};
class SetBizCNameResponse : public Darabonba::Model {
public:
  shared_ptr<string> bizCname{};
  shared_ptr<CNameStatus> cnameStatus{};
  shared_ptr<string> cnameType{};
  shared_ptr<string> domainId{};
  shared_ptr<bool> isVpc{};

  SetBizCNameResponse() {}

  explicit SetBizCNameResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!domainId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("domainId is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (bizCname) {
      res["biz_cname"] = boost::any(*bizCname);
    }
    if (cnameStatus) {
      res["cname_status"] = cnameStatus ? boost::any(cnameStatus->toMap()) : boost::any(map<string,boost::any>({}));
    }
    if (cnameType) {
      res["cname_type"] = boost::any(*cnameType);
    }
    if (domainId) {
      res["domain_id"] = boost::any(*domainId);
    }
    if (isVpc) {
      res["is_vpc"] = boost::any(*isVpc);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("biz_cname") != m.end() && !m["biz_cname"].empty()) {
      bizCname = make_shared<string>(boost::any_cast<string>(m["biz_cname"]));
    }
    if (m.find("cname_status") != m.end() && !m["cname_status"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["cname_status"].type().name()) {
        CNameStatus model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["cname_status"]));
        cnameStatus = make_shared<CNameStatus>(model1);
      }
    }
    if (m.find("cname_type") != m.end() && !m["cname_type"].empty()) {
      cnameType = make_shared<string>(boost::any_cast<string>(m["cname_type"]));
    }
    if (m.find("domain_id") != m.end() && !m["domain_id"].empty()) {
      domainId = make_shared<string>(boost::any_cast<string>(m["domain_id"]));
    }
    if (m.find("is_vpc") != m.end() && !m["is_vpc"].empty()) {
      isVpc = make_shared<bool>(boost::any_cast<bool>(m["is_vpc"]));
    }
  }


  ~SetBizCNameResponse() = default;
};
class SetDataCNameResponse : public Darabonba::Model {
public:
  shared_ptr<string> dataCname{};
  shared_ptr<string> domainId{};
  shared_ptr<string> location{};

  SetDataCNameResponse() {}

  explicit SetDataCNameResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!dataCname) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("dataCname is required.")));
    }
    if (!domainId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("domainId is required.")));
    }
    if (!location) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("location is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (dataCname) {
      res["data_cname"] = boost::any(*dataCname);
    }
    if (domainId) {
      res["domain_id"] = boost::any(*domainId);
    }
    if (location) {
      res["location"] = boost::any(*location);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("data_cname") != m.end() && !m["data_cname"].empty()) {
      dataCname = make_shared<string>(boost::any_cast<string>(m["data_cname"]));
    }
    if (m.find("domain_id") != m.end() && !m["domain_id"].empty()) {
      domainId = make_shared<string>(boost::any_cast<string>(m["domain_id"]));
    }
    if (m.find("location") != m.end() && !m["location"].empty()) {
      location = make_shared<string>(boost::any_cast<string>(m["location"]));
    }
  }


  ~SetDataCNameResponse() = default;
};
class UpdateDomainResponse : public Darabonba::Model {
public:
  shared_ptr<string> apiCname{};
  shared_ptr<string> authAlipayAppId{};
  shared_ptr<bool> authAlipayEnable{};
  shared_ptr<string> authAlipayPrivateKey{};
  shared_ptr<map<string, boost::any>> authConfig{};
  shared_ptr<string> authDingdingAppId{};
  shared_ptr<string> authDingdingAppSecret{};
  shared_ptr<bool> authDingdingEnable{};
  shared_ptr<bool> authEndpointEnable{};
  shared_ptr<string> authRamAppId{};
  shared_ptr<string> authRamAppSecret{};
  shared_ptr<bool> authRamEnable{};
  shared_ptr<string> createdAt{};
  shared_ptr<string> dataHashName{};
  shared_ptr<string> description{};
  shared_ptr<string> domainId{};
  shared_ptr<string> domainName{};
  shared_ptr<string> eventFilenameMatches{};
  shared_ptr<string> eventMnsEndpoint{};
  shared_ptr<string> eventMnsTopic{};
  shared_ptr<vector<string>> eventNames{};
  shared_ptr<string> eventRoleArn{};
  shared_ptr<bool> initDriveEnable{};
  shared_ptr<long> initDriveSize{};
  shared_ptr<string> initDriveStoreId{};
  shared_ptr<string> mode{};
  shared_ptr<string> pathType{};
  shared_ptr<AppAccessStrategy> publishedAppAccessStrategy{};
  shared_ptr<bool> sharable{};
  shared_ptr<string> storeLevel{};
  shared_ptr<vector<string>> storeRegionList{};
  shared_ptr<string> updatedAt{};

  UpdateDomainResponse() {}

  explicit UpdateDomainResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (apiCname) {
      res["api_cname"] = boost::any(*apiCname);
    }
    if (authAlipayAppId) {
      res["auth_alipay_app_id"] = boost::any(*authAlipayAppId);
    }
    if (authAlipayEnable) {
      res["auth_alipay_enable"] = boost::any(*authAlipayEnable);
    }
    if (authAlipayPrivateKey) {
      res["auth_alipay_private_key"] = boost::any(*authAlipayPrivateKey);
    }
    if (authConfig) {
      res["auth_config"] = boost::any(*authConfig);
    }
    if (authDingdingAppId) {
      res["auth_dingding_app_id"] = boost::any(*authDingdingAppId);
    }
    if (authDingdingAppSecret) {
      res["auth_dingding_app_secret"] = boost::any(*authDingdingAppSecret);
    }
    if (authDingdingEnable) {
      res["auth_dingding_enable"] = boost::any(*authDingdingEnable);
    }
    if (authEndpointEnable) {
      res["auth_endpoint_enable"] = boost::any(*authEndpointEnable);
    }
    if (authRamAppId) {
      res["auth_ram_app_id"] = boost::any(*authRamAppId);
    }
    if (authRamAppSecret) {
      res["auth_ram_app_secret"] = boost::any(*authRamAppSecret);
    }
    if (authRamEnable) {
      res["auth_ram_enable"] = boost::any(*authRamEnable);
    }
    if (createdAt) {
      res["created_at"] = boost::any(*createdAt);
    }
    if (dataHashName) {
      res["data_hash_name"] = boost::any(*dataHashName);
    }
    if (description) {
      res["description"] = boost::any(*description);
    }
    if (domainId) {
      res["domain_id"] = boost::any(*domainId);
    }
    if (domainName) {
      res["domain_name"] = boost::any(*domainName);
    }
    if (eventFilenameMatches) {
      res["event_filename_matches"] = boost::any(*eventFilenameMatches);
    }
    if (eventMnsEndpoint) {
      res["event_mns_endpoint"] = boost::any(*eventMnsEndpoint);
    }
    if (eventMnsTopic) {
      res["event_mns_topic"] = boost::any(*eventMnsTopic);
    }
    if (eventNames) {
      res["event_names"] = boost::any(*eventNames);
    }
    if (eventRoleArn) {
      res["event_role_arn"] = boost::any(*eventRoleArn);
    }
    if (initDriveEnable) {
      res["init_drive_enable"] = boost::any(*initDriveEnable);
    }
    if (initDriveSize) {
      res["init_drive_size"] = boost::any(*initDriveSize);
    }
    if (initDriveStoreId) {
      res["init_drive_store_id"] = boost::any(*initDriveStoreId);
    }
    if (mode) {
      res["mode"] = boost::any(*mode);
    }
    if (pathType) {
      res["path_type"] = boost::any(*pathType);
    }
    if (publishedAppAccessStrategy) {
      res["published_app_access_strategy"] = publishedAppAccessStrategy ? boost::any(publishedAppAccessStrategy->toMap()) : boost::any(map<string,boost::any>({}));
    }
    if (sharable) {
      res["sharable"] = boost::any(*sharable);
    }
    if (storeLevel) {
      res["store_level"] = boost::any(*storeLevel);
    }
    if (storeRegionList) {
      res["store_region_list"] = boost::any(*storeRegionList);
    }
    if (updatedAt) {
      res["updated_at"] = boost::any(*updatedAt);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("api_cname") != m.end() && !m["api_cname"].empty()) {
      apiCname = make_shared<string>(boost::any_cast<string>(m["api_cname"]));
    }
    if (m.find("auth_alipay_app_id") != m.end() && !m["auth_alipay_app_id"].empty()) {
      authAlipayAppId = make_shared<string>(boost::any_cast<string>(m["auth_alipay_app_id"]));
    }
    if (m.find("auth_alipay_enable") != m.end() && !m["auth_alipay_enable"].empty()) {
      authAlipayEnable = make_shared<bool>(boost::any_cast<bool>(m["auth_alipay_enable"]));
    }
    if (m.find("auth_alipay_private_key") != m.end() && !m["auth_alipay_private_key"].empty()) {
      authAlipayPrivateKey = make_shared<string>(boost::any_cast<string>(m["auth_alipay_private_key"]));
    }
    if (m.find("auth_config") != m.end() && !m["auth_config"].empty()) {
      map<string, boost::any> map1 = boost::any_cast<map<string, boost::any>>(m["auth_config"]);
      map<string, boost::any> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      authConfig = make_shared<map<string, boost::any>>(toMap1);
    }
    if (m.find("auth_dingding_app_id") != m.end() && !m["auth_dingding_app_id"].empty()) {
      authDingdingAppId = make_shared<string>(boost::any_cast<string>(m["auth_dingding_app_id"]));
    }
    if (m.find("auth_dingding_app_secret") != m.end() && !m["auth_dingding_app_secret"].empty()) {
      authDingdingAppSecret = make_shared<string>(boost::any_cast<string>(m["auth_dingding_app_secret"]));
    }
    if (m.find("auth_dingding_enable") != m.end() && !m["auth_dingding_enable"].empty()) {
      authDingdingEnable = make_shared<bool>(boost::any_cast<bool>(m["auth_dingding_enable"]));
    }
    if (m.find("auth_endpoint_enable") != m.end() && !m["auth_endpoint_enable"].empty()) {
      authEndpointEnable = make_shared<bool>(boost::any_cast<bool>(m["auth_endpoint_enable"]));
    }
    if (m.find("auth_ram_app_id") != m.end() && !m["auth_ram_app_id"].empty()) {
      authRamAppId = make_shared<string>(boost::any_cast<string>(m["auth_ram_app_id"]));
    }
    if (m.find("auth_ram_app_secret") != m.end() && !m["auth_ram_app_secret"].empty()) {
      authRamAppSecret = make_shared<string>(boost::any_cast<string>(m["auth_ram_app_secret"]));
    }
    if (m.find("auth_ram_enable") != m.end() && !m["auth_ram_enable"].empty()) {
      authRamEnable = make_shared<bool>(boost::any_cast<bool>(m["auth_ram_enable"]));
    }
    if (m.find("created_at") != m.end() && !m["created_at"].empty()) {
      createdAt = make_shared<string>(boost::any_cast<string>(m["created_at"]));
    }
    if (m.find("data_hash_name") != m.end() && !m["data_hash_name"].empty()) {
      dataHashName = make_shared<string>(boost::any_cast<string>(m["data_hash_name"]));
    }
    if (m.find("description") != m.end() && !m["description"].empty()) {
      description = make_shared<string>(boost::any_cast<string>(m["description"]));
    }
    if (m.find("domain_id") != m.end() && !m["domain_id"].empty()) {
      domainId = make_shared<string>(boost::any_cast<string>(m["domain_id"]));
    }
    if (m.find("domain_name") != m.end() && !m["domain_name"].empty()) {
      domainName = make_shared<string>(boost::any_cast<string>(m["domain_name"]));
    }
    if (m.find("event_filename_matches") != m.end() && !m["event_filename_matches"].empty()) {
      eventFilenameMatches = make_shared<string>(boost::any_cast<string>(m["event_filename_matches"]));
    }
    if (m.find("event_mns_endpoint") != m.end() && !m["event_mns_endpoint"].empty()) {
      eventMnsEndpoint = make_shared<string>(boost::any_cast<string>(m["event_mns_endpoint"]));
    }
    if (m.find("event_mns_topic") != m.end() && !m["event_mns_topic"].empty()) {
      eventMnsTopic = make_shared<string>(boost::any_cast<string>(m["event_mns_topic"]));
    }
    if (m.find("event_names") != m.end() && !m["event_names"].empty()) {
      vector<string> toVec1;
      if (typeid(vector<boost::any>).name() == m["event_names"].type().name()) {
        vector<boost::any> vec1 = boost::any_cast<vector<boost::any>>(m["event_names"]);
        for (auto item:vec1) {
           toVec1.push_back(boost::any_cast<string>(item));
        }
      }
      eventNames = make_shared<vector<string>>(toVec1);
    }
    if (m.find("event_role_arn") != m.end() && !m["event_role_arn"].empty()) {
      eventRoleArn = make_shared<string>(boost::any_cast<string>(m["event_role_arn"]));
    }
    if (m.find("init_drive_enable") != m.end() && !m["init_drive_enable"].empty()) {
      initDriveEnable = make_shared<bool>(boost::any_cast<bool>(m["init_drive_enable"]));
    }
    if (m.find("init_drive_size") != m.end() && !m["init_drive_size"].empty()) {
      initDriveSize = make_shared<long>(boost::any_cast<long>(m["init_drive_size"]));
    }
    if (m.find("init_drive_store_id") != m.end() && !m["init_drive_store_id"].empty()) {
      initDriveStoreId = make_shared<string>(boost::any_cast<string>(m["init_drive_store_id"]));
    }
    if (m.find("mode") != m.end() && !m["mode"].empty()) {
      mode = make_shared<string>(boost::any_cast<string>(m["mode"]));
    }
    if (m.find("path_type") != m.end() && !m["path_type"].empty()) {
      pathType = make_shared<string>(boost::any_cast<string>(m["path_type"]));
    }
    if (m.find("published_app_access_strategy") != m.end() && !m["published_app_access_strategy"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["published_app_access_strategy"].type().name()) {
        AppAccessStrategy model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["published_app_access_strategy"]));
        publishedAppAccessStrategy = make_shared<AppAccessStrategy>(model1);
      }
    }
    if (m.find("sharable") != m.end() && !m["sharable"].empty()) {
      sharable = make_shared<bool>(boost::any_cast<bool>(m["sharable"]));
    }
    if (m.find("store_level") != m.end() && !m["store_level"].empty()) {
      storeLevel = make_shared<string>(boost::any_cast<string>(m["store_level"]));
    }
    if (m.find("store_region_list") != m.end() && !m["store_region_list"].empty()) {
      vector<string> toVec1;
      if (typeid(vector<boost::any>).name() == m["store_region_list"].type().name()) {
        vector<boost::any> vec1 = boost::any_cast<vector<boost::any>>(m["store_region_list"]);
        for (auto item:vec1) {
           toVec1.push_back(boost::any_cast<string>(item));
        }
      }
      storeRegionList = make_shared<vector<string>>(toVec1);
    }
    if (m.find("updated_at") != m.end() && !m["updated_at"].empty()) {
      updatedAt = make_shared<string>(boost::any_cast<string>(m["updated_at"]));
    }
  }


  ~UpdateDomainResponse() = default;
};
class GetAsyncTaskInfoModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<GetAsyncTaskResponse> body{};

  GetAsyncTaskInfoModel() {}

  explicit GetAsyncTaskInfoModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        GetAsyncTaskResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<GetAsyncTaskResponse>(model1);
      }
    }
  }


  ~GetAsyncTaskInfoModel() = default;
};
class BatchOperationModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<BatchResponse> body{};

  BatchOperationModel() {}

  explicit BatchOperationModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        BatchResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<BatchResponse>(model1);
      }
    }
  }


  ~BatchOperationModel() = default;
};
class CreateDriveModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<CreateDriveResponse> body{};

  CreateDriveModel() {}

  explicit CreateDriveModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        CreateDriveResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<CreateDriveResponse>(model1);
      }
    }
  }


  ~CreateDriveModel() = default;
};
class DeleteDriveModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};

  DeleteDriveModel() {}

  explicit DeleteDriveModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
  }


  ~DeleteDriveModel() = default;
};
class GetDriveModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<GetDriveResponse> body{};

  GetDriveModel() {}

  explicit GetDriveModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        GetDriveResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<GetDriveResponse>(model1);
      }
    }
  }


  ~GetDriveModel() = default;
};
class GetDefaultDriveModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<GetDriveResponse> body{};

  GetDefaultDriveModel() {}

  explicit GetDefaultDriveModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        GetDriveResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<GetDriveResponse>(model1);
      }
    }
  }


  ~GetDefaultDriveModel() = default;
};
class ListDrivesModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<ListDriveResponse> body{};

  ListDrivesModel() {}

  explicit ListDrivesModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        ListDriveResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<ListDriveResponse>(model1);
      }
    }
  }


  ~ListDrivesModel() = default;
};
class ListMyDrivesModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<ListDriveResponse> body{};

  ListMyDrivesModel() {}

  explicit ListMyDrivesModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        ListDriveResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<ListDriveResponse>(model1);
      }
    }
  }


  ~ListMyDrivesModel() = default;
};
class UpdateDriveModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<UpdateDriveResponse> body{};

  UpdateDriveModel() {}

  explicit UpdateDriveModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        UpdateDriveResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<UpdateDriveResponse>(model1);
      }
    }
  }


  ~UpdateDriveModel() = default;
};
class CompleteFileModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<CompleteFileResponse> body{};

  CompleteFileModel() {}

  explicit CompleteFileModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        CompleteFileResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<CompleteFileResponse>(model1);
      }
    }
  }


  ~CompleteFileModel() = default;
};
class CopyFileModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<CopyFileResponse> body{};

  CopyFileModel() {}

  explicit CopyFileModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        CopyFileResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<CopyFileResponse>(model1);
      }
    }
  }


  ~CopyFileModel() = default;
};
class CreateFileModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<CreateFileResponse> body{};

  CreateFileModel() {}

  explicit CreateFileModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        CreateFileResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<CreateFileResponse>(model1);
      }
    }
  }


  ~CreateFileModel() = default;
};
class DeleteFileModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<DeleteFileResponse> body{};

  DeleteFileModel() {}

  explicit DeleteFileModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        DeleteFileResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<DeleteFileResponse>(model1);
      }
    }
  }


  ~DeleteFileModel() = default;
};
class GetFileModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<GetFileResponse> body{};

  GetFileModel() {}

  explicit GetFileModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        GetFileResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<GetFileResponse>(model1);
      }
    }
  }


  ~GetFileModel() = default;
};
class GetFileByPathModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<GetFileByPathResponse> body{};

  GetFileByPathModel() {}

  explicit GetFileByPathModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        GetFileByPathResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<GetFileByPathResponse>(model1);
      }
    }
  }


  ~GetFileByPathModel() = default;
};
class GetDownloadUrlModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<GetDownloadUrlResponse> body{};

  GetDownloadUrlModel() {}

  explicit GetDownloadUrlModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        GetDownloadUrlResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<GetDownloadUrlResponse>(model1);
      }
    }
  }


  ~GetDownloadUrlModel() = default;
};
class GetLastCursorModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<GetLastCursorResponse> body{};

  GetLastCursorModel() {}

  explicit GetLastCursorModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        GetLastCursorResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<GetLastCursorResponse>(model1);
      }
    }
  }


  ~GetLastCursorModel() = default;
};
class GetMediaPlayUrlModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<GetMediaPlayURLResponse> body{};

  GetMediaPlayUrlModel() {}

  explicit GetMediaPlayUrlModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        GetMediaPlayURLResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<GetMediaPlayURLResponse>(model1);
      }
    }
  }


  ~GetMediaPlayUrlModel() = default;
};
class GetOfficePreviewUrlModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<GetOfficePreviewUrlResponse> body{};

  GetOfficePreviewUrlModel() {}

  explicit GetOfficePreviewUrlModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        GetOfficePreviewUrlResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<GetOfficePreviewUrlResponse>(model1);
      }
    }
  }


  ~GetOfficePreviewUrlModel() = default;
};
class GetUploadUrlModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<GetUploadUrlResponse> body{};

  GetUploadUrlModel() {}

  explicit GetUploadUrlModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        GetUploadUrlResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<GetUploadUrlResponse>(model1);
      }
    }
  }


  ~GetUploadUrlModel() = default;
};
class GetVideoPreviewSpriteUrlModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<GetVideoPreviewSpriteURLResponse> body{};

  GetVideoPreviewSpriteUrlModel() {}

  explicit GetVideoPreviewSpriteUrlModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        GetVideoPreviewSpriteURLResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<GetVideoPreviewSpriteURLResponse>(model1);
      }
    }
  }


  ~GetVideoPreviewSpriteUrlModel() = default;
};
class GetVideoPreviewUrlModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<GetVideoPreviewURLResponse> body{};

  GetVideoPreviewUrlModel() {}

  explicit GetVideoPreviewUrlModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        GetVideoPreviewURLResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<GetVideoPreviewURLResponse>(model1);
      }
    }
  }


  ~GetVideoPreviewUrlModel() = default;
};
class ListFileModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<ListFileResponse> body{};

  ListFileModel() {}

  explicit ListFileModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        ListFileResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<ListFileResponse>(model1);
      }
    }
  }


  ~ListFileModel() = default;
};
class ListFileByAnonymousModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<ListByAnonymousResponse> body{};

  ListFileByAnonymousModel() {}

  explicit ListFileByAnonymousModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        ListByAnonymousResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<ListByAnonymousResponse>(model1);
      }
    }
  }


  ~ListFileByAnonymousModel() = default;
};
class ListFileByCustomIndexKeyModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<ListFileResponse> body{};

  ListFileByCustomIndexKeyModel() {}

  explicit ListFileByCustomIndexKeyModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        ListFileResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<ListFileResponse>(model1);
      }
    }
  }


  ~ListFileByCustomIndexKeyModel() = default;
};
class ListFileDeltaModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<ListFileDeltaResponse> body{};

  ListFileDeltaModel() {}

  explicit ListFileDeltaModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        ListFileDeltaResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<ListFileDeltaResponse>(model1);
      }
    }
  }


  ~ListFileDeltaModel() = default;
};
class ListUploadedPartsModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<ListUploadedPartResponse> body{};

  ListUploadedPartsModel() {}

  explicit ListUploadedPartsModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        ListUploadedPartResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<ListUploadedPartResponse>(model1);
      }
    }
  }


  ~ListUploadedPartsModel() = default;
};
class MoveFileModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<MoveFileResponse> body{};

  MoveFileModel() {}

  explicit MoveFileModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        MoveFileResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<MoveFileResponse>(model1);
      }
    }
  }


  ~MoveFileModel() = default;
};
class ScanFileMetaModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<ScanFileMetaResponse> body{};

  ScanFileMetaModel() {}

  explicit ScanFileMetaModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        ScanFileMetaResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<ScanFileMetaResponse>(model1);
      }
    }
  }


  ~ScanFileMetaModel() = default;
};
class SearchFileModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<SearchFileResponse> body{};

  SearchFileModel() {}

  explicit SearchFileModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        SearchFileResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<SearchFileResponse>(model1);
      }
    }
  }


  ~SearchFileModel() = default;
};
class UpdateFileModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<UpdateFileMetaResponse> body{};

  UpdateFileModel() {}

  explicit UpdateFileModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        UpdateFileMetaResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<UpdateFileMetaResponse>(model1);
      }
    }
  }


  ~UpdateFileModel() = default;
};
class CancelShareLinkModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};

  CancelShareLinkModel() {}

  explicit CancelShareLinkModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
  }


  ~CancelShareLinkModel() = default;
};
class CreateShareLinkModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<CreateShareLinkResponse> body{};

  CreateShareLinkModel() {}

  explicit CreateShareLinkModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        CreateShareLinkResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<CreateShareLinkResponse>(model1);
      }
    }
  }


  ~CreateShareLinkModel() = default;
};
class GetShareIdModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<GetShareLinkIDResponse> body{};

  GetShareIdModel() {}

  explicit GetShareIdModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        GetShareLinkIDResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<GetShareLinkIDResponse>(model1);
      }
    }
  }


  ~GetShareIdModel() = default;
};
class GetShareTokenModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<GetShareLinkTokenResponse> body{};

  GetShareTokenModel() {}

  explicit GetShareTokenModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        GetShareLinkTokenResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<GetShareLinkTokenResponse>(model1);
      }
    }
  }


  ~GetShareTokenModel() = default;
};
class ListShareLinkModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<ListShareLinkResponse> body{};

  ListShareLinkModel() {}

  explicit ListShareLinkModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        ListShareLinkResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<ListShareLinkResponse>(model1);
      }
    }
  }


  ~ListShareLinkModel() = default;
};
class BaseCompleteFileRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, boost::any>> additionData{};
  shared_ptr<string> driveId{};
  shared_ptr<vector<UploadPartInfo>> partInfoList{};
  shared_ptr<string> uploadId{};

  BaseCompleteFileRequest() {}

  explicit BaseCompleteFileRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (additionData) {
      res["addition_data"] = boost::any(*additionData);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (partInfoList) {
      vector<boost::any> temp1;
      for(auto item1:*partInfoList){
        temp1.push_back(boost::any(item1.toMap()));
      }
      res["part_info_list"] = boost::any(temp1);
    }
    if (uploadId) {
      res["upload_id"] = boost::any(*uploadId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("addition_data") != m.end() && !m["addition_data"].empty()) {
      map<string, boost::any> map1 = boost::any_cast<map<string, boost::any>>(m["addition_data"]);
      map<string, boost::any> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      additionData = make_shared<map<string, boost::any>>(toMap1);
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("part_info_list") != m.end() && !m["part_info_list"].empty()) {
      if (typeid(vector<boost::any>).name() == m["part_info_list"].type().name()) {
        vector<UploadPartInfo> expect1;
        for(auto item1:boost::any_cast<vector<boost::any>>(m["part_info_list"])){
          if (typeid(map<string, boost::any>).name() == item1.type().name()) {
            UploadPartInfo model2;
            model2.fromMap(boost::any_cast<map<string, boost::any>>(item1));
            expect1.push_back(model2);
          }
        }
        partInfoList = make_shared<vector<UploadPartInfo>>(expect1);
      }
    }
    if (m.find("upload_id") != m.end() && !m["upload_id"].empty()) {
      uploadId = make_shared<string>(boost::any_cast<string>(m["upload_id"]));
    }
  }


  ~BaseCompleteFileRequest() = default;
};
class BaseCreateFileRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, boost::any>> additionData{};
  shared_ptr<string> contentMd5{};
  shared_ptr<string> contentType{};
  shared_ptr<string> name{};
  shared_ptr<vector<UploadPartInfo>> partInfoList{};
  shared_ptr<long> size{};
  shared_ptr<string> type{};

  BaseCreateFileRequest() {}

  explicit BaseCreateFileRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!name) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("name is required.")));
    }
    Darabonba::Model::validateMaxLength("name", name, 1024);
    Darabonba::Model::validateMinLength("name", name, 1);
    if (size && *size > 53687091200) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("size is required.")));
    }
    if (size && *size < 0) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("size is required.")));
    }
    if (!type) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("type is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (additionData) {
      res["addition_data"] = boost::any(*additionData);
    }
    if (contentMd5) {
      res["content_md5"] = boost::any(*contentMd5);
    }
    if (contentType) {
      res["content_type"] = boost::any(*contentType);
    }
    if (name) {
      res["name"] = boost::any(*name);
    }
    if (partInfoList) {
      vector<boost::any> temp1;
      for(auto item1:*partInfoList){
        temp1.push_back(boost::any(item1.toMap()));
      }
      res["part_info_list"] = boost::any(temp1);
    }
    if (size) {
      res["size"] = boost::any(*size);
    }
    if (type) {
      res["type"] = boost::any(*type);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("addition_data") != m.end() && !m["addition_data"].empty()) {
      map<string, boost::any> map1 = boost::any_cast<map<string, boost::any>>(m["addition_data"]);
      map<string, boost::any> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      additionData = make_shared<map<string, boost::any>>(toMap1);
    }
    if (m.find("content_md5") != m.end() && !m["content_md5"].empty()) {
      contentMd5 = make_shared<string>(boost::any_cast<string>(m["content_md5"]));
    }
    if (m.find("content_type") != m.end() && !m["content_type"].empty()) {
      contentType = make_shared<string>(boost::any_cast<string>(m["content_type"]));
    }
    if (m.find("name") != m.end() && !m["name"].empty()) {
      name = make_shared<string>(boost::any_cast<string>(m["name"]));
    }
    if (m.find("part_info_list") != m.end() && !m["part_info_list"].empty()) {
      if (typeid(vector<boost::any>).name() == m["part_info_list"].type().name()) {
        vector<UploadPartInfo> expect1;
        for(auto item1:boost::any_cast<vector<boost::any>>(m["part_info_list"])){
          if (typeid(map<string, boost::any>).name() == item1.type().name()) {
            UploadPartInfo model2;
            model2.fromMap(boost::any_cast<map<string, boost::any>>(item1));
            expect1.push_back(model2);
          }
        }
        partInfoList = make_shared<vector<UploadPartInfo>>(expect1);
      }
    }
    if (m.find("size") != m.end() && !m["size"].empty()) {
      size = make_shared<long>(boost::any_cast<long>(m["size"]));
    }
    if (m.find("type") != m.end() && !m["type"].empty()) {
      type = make_shared<string>(boost::any_cast<string>(m["type"]));
    }
  }


  ~BaseCreateFileRequest() = default;
};
class BaseFileRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, boost::any>> additionData{};

  BaseFileRequest() {}

  explicit BaseFileRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (additionData) {
      res["addition_data"] = boost::any(*additionData);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("addition_data") != m.end() && !m["addition_data"].empty()) {
      map<string, boost::any> map1 = boost::any_cast<map<string, boost::any>>(m["addition_data"]);
      map<string, boost::any> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      additionData = make_shared<map<string, boost::any>>(toMap1);
    }
  }


  ~BaseFileRequest() = default;
};
class BaseGetUploadUrlRequest : public Darabonba::Model {
public:
  shared_ptr<string> contentMd5{};
  shared_ptr<string> driveId{};
  shared_ptr<vector<UploadPartInfo>> partInfoList{};
  shared_ptr<string> uploadId{};

  BaseGetUploadUrlRequest() {}

  explicit BaseGetUploadUrlRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    Darabonba::Model::validateMaxLength("contentMd5", contentMd5, 32);
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    if (!uploadId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("uploadId is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (contentMd5) {
      res["content_md5"] = boost::any(*contentMd5);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (partInfoList) {
      vector<boost::any> temp1;
      for(auto item1:*partInfoList){
        temp1.push_back(boost::any(item1.toMap()));
      }
      res["part_info_list"] = boost::any(temp1);
    }
    if (uploadId) {
      res["upload_id"] = boost::any(*uploadId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("content_md5") != m.end() && !m["content_md5"].empty()) {
      contentMd5 = make_shared<string>(boost::any_cast<string>(m["content_md5"]));
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("part_info_list") != m.end() && !m["part_info_list"].empty()) {
      if (typeid(vector<boost::any>).name() == m["part_info_list"].type().name()) {
        vector<UploadPartInfo> expect1;
        for(auto item1:boost::any_cast<vector<boost::any>>(m["part_info_list"])){
          if (typeid(map<string, boost::any>).name() == item1.type().name()) {
            UploadPartInfo model2;
            model2.fromMap(boost::any_cast<map<string, boost::any>>(item1));
            expect1.push_back(model2);
          }
        }
        partInfoList = make_shared<vector<UploadPartInfo>>(expect1);
      }
    }
    if (m.find("upload_id") != m.end() && !m["upload_id"].empty()) {
      uploadId = make_shared<string>(boost::any_cast<string>(m["upload_id"]));
    }
  }


  ~BaseGetUploadUrlRequest() = default;
};
class BaseListFileRequest : public Darabonba::Model {
public:
  shared_ptr<string> driveId{};
  shared_ptr<string> imageThumbnailProcess{};
  shared_ptr<string> imageUrlProcess{};
  shared_ptr<long> limit{};
  shared_ptr<string> marker{};
  shared_ptr<string> videoThumbnailProcess{};

  BaseListFileRequest() {}

  explicit BaseListFileRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    if (limit && *limit > 100) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("limit is required.")));
    }
    if (limit && *limit < 0) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("limit is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (imageThumbnailProcess) {
      res["image_thumbnail_process"] = boost::any(*imageThumbnailProcess);
    }
    if (imageUrlProcess) {
      res["image_url_process"] = boost::any(*imageUrlProcess);
    }
    if (limit) {
      res["limit"] = boost::any(*limit);
    }
    if (marker) {
      res["marker"] = boost::any(*marker);
    }
    if (videoThumbnailProcess) {
      res["video_thumbnail_process"] = boost::any(*videoThumbnailProcess);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("image_thumbnail_process") != m.end() && !m["image_thumbnail_process"].empty()) {
      imageThumbnailProcess = make_shared<string>(boost::any_cast<string>(m["image_thumbnail_process"]));
    }
    if (m.find("image_url_process") != m.end() && !m["image_url_process"].empty()) {
      imageUrlProcess = make_shared<string>(boost::any_cast<string>(m["image_url_process"]));
    }
    if (m.find("limit") != m.end() && !m["limit"].empty()) {
      limit = make_shared<long>(boost::any_cast<long>(m["limit"]));
    }
    if (m.find("marker") != m.end() && !m["marker"].empty()) {
      marker = make_shared<string>(boost::any_cast<string>(m["marker"]));
    }
    if (m.find("video_thumbnail_process") != m.end() && !m["video_thumbnail_process"].empty()) {
      videoThumbnailProcess = make_shared<string>(boost::any_cast<string>(m["video_thumbnail_process"]));
    }
  }


  ~BaseListFileRequest() = default;
};
class BaseMoveFileRequest : public Darabonba::Model {
public:
  shared_ptr<string> driveId{};
  shared_ptr<string> newName{};
  shared_ptr<bool> overwrite{};

  BaseMoveFileRequest() {}

  explicit BaseMoveFileRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!driveId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("driveId is required.")));
    }
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    Darabonba::Model::validateMaxLength("newName", newName, 1024);
    Darabonba::Model::validateMinLength("newName", newName, 1);
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (newName) {
      res["new_name"] = boost::any(*newName);
    }
    if (overwrite) {
      res["overwrite"] = boost::any(*overwrite);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("new_name") != m.end() && !m["new_name"].empty()) {
      newName = make_shared<string>(boost::any_cast<string>(m["new_name"]));
    }
    if (m.find("overwrite") != m.end() && !m["overwrite"].empty()) {
      overwrite = make_shared<bool>(boost::any_cast<bool>(m["overwrite"]));
    }
  }


  ~BaseMoveFileRequest() = default;
};
class BatchSubRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, boost::any>> body{};
  shared_ptr<map<string, boost::any>> headers{};
  shared_ptr<string> id{};
  shared_ptr<string> method{};
  shared_ptr<string> url{};

  BatchSubRequest() {}

  explicit BatchSubRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!id) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("id is required.")));
    }
    if (!method) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("method is required.")));
    }
    if (!url) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("url is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (body) {
      res["body"] = boost::any(*body);
    }
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (id) {
      res["id"] = boost::any(*id);
    }
    if (method) {
      res["method"] = boost::any(*method);
    }
    if (url) {
      res["url"] = boost::any(*url);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("body") != m.end() && !m["body"].empty()) {
      map<string, boost::any> map1 = boost::any_cast<map<string, boost::any>>(m["body"]);
      map<string, boost::any> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      body = make_shared<map<string, boost::any>>(toMap1);
    }
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, boost::any> map1 = boost::any_cast<map<string, boost::any>>(m["headers"]);
      map<string, boost::any> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, boost::any>>(toMap1);
    }
    if (m.find("id") != m.end() && !m["id"].empty()) {
      id = make_shared<string>(boost::any_cast<string>(m["id"]));
    }
    if (m.find("method") != m.end() && !m["method"].empty()) {
      method = make_shared<string>(boost::any_cast<string>(m["method"]));
    }
    if (m.find("url") != m.end() && !m["url"].empty()) {
      url = make_shared<string>(boost::any_cast<string>(m["url"]));
    }
  }


  ~BatchSubRequest() = default;
};
class BatchRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<vector<BatchSubRequest>> requests{};
  shared_ptr<string> resource{};

  BatchRequest() {}

  explicit BatchRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!requests) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("requests is required.")));
    }
    if (!resource) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("resource is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (requests) {
      vector<boost::any> temp1;
      for(auto item1:*requests){
        temp1.push_back(boost::any(item1.toMap()));
      }
      res["requests"] = boost::any(temp1);
    }
    if (resource) {
      res["resource"] = boost::any(*resource);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("requests") != m.end() && !m["requests"].empty()) {
      if (typeid(vector<boost::any>).name() == m["requests"].type().name()) {
        vector<BatchSubRequest> expect1;
        for(auto item1:boost::any_cast<vector<boost::any>>(m["requests"])){
          if (typeid(map<string, boost::any>).name() == item1.type().name()) {
            BatchSubRequest model2;
            model2.fromMap(boost::any_cast<map<string, boost::any>>(item1));
            expect1.push_back(model2);
          }
        }
        requests = make_shared<vector<BatchSubRequest>>(expect1);
      }
    }
    if (m.find("resource") != m.end() && !m["resource"].empty()) {
      resource = make_shared<string>(boost::any_cast<string>(m["resource"]));
    }
  }


  ~BatchRequest() = default;
};
class CancelShareLinkRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<string> shareId{};

  CancelShareLinkRequest() {}

  explicit CancelShareLinkRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (shareId) {
      res["share_id"] = boost::any(*shareId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("share_id") != m.end() && !m["share_id"].empty()) {
      shareId = make_shared<string>(boost::any_cast<string>(m["share_id"]));
    }
  }


  ~CancelShareLinkRequest() = default;
};
class CompleteFileRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<map<string, boost::any>> additionData{};
  shared_ptr<string> driveId{};
  shared_ptr<string> fileId{};
  shared_ptr<vector<UploadPartInfo>> partInfoList{};
  shared_ptr<string> uploadId{};

  CompleteFileRequest() {}

  explicit CompleteFileRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    if (!fileId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("fileId is required.")));
    }
    Darabonba::Model::validateMaxLength("fileId", fileId, 50);
    Darabonba::Model::validateMinLength("fileId", fileId, 40);
    Darabonba::Model::validatePattern("fileId", fileId, "[a-z0-9]{1,50}");
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (additionData) {
      res["addition_data"] = boost::any(*additionData);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (fileId) {
      res["file_id"] = boost::any(*fileId);
    }
    if (partInfoList) {
      vector<boost::any> temp1;
      for(auto item1:*partInfoList){
        temp1.push_back(boost::any(item1.toMap()));
      }
      res["part_info_list"] = boost::any(temp1);
    }
    if (uploadId) {
      res["upload_id"] = boost::any(*uploadId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("addition_data") != m.end() && !m["addition_data"].empty()) {
      map<string, boost::any> map1 = boost::any_cast<map<string, boost::any>>(m["addition_data"]);
      map<string, boost::any> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      additionData = make_shared<map<string, boost::any>>(toMap1);
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("file_id") != m.end() && !m["file_id"].empty()) {
      fileId = make_shared<string>(boost::any_cast<string>(m["file_id"]));
    }
    if (m.find("part_info_list") != m.end() && !m["part_info_list"].empty()) {
      if (typeid(vector<boost::any>).name() == m["part_info_list"].type().name()) {
        vector<UploadPartInfo> expect1;
        for(auto item1:boost::any_cast<vector<boost::any>>(m["part_info_list"])){
          if (typeid(map<string, boost::any>).name() == item1.type().name()) {
            UploadPartInfo model2;
            model2.fromMap(boost::any_cast<map<string, boost::any>>(item1));
            expect1.push_back(model2);
          }
        }
        partInfoList = make_shared<vector<UploadPartInfo>>(expect1);
      }
    }
    if (m.find("upload_id") != m.end() && !m["upload_id"].empty()) {
      uploadId = make_shared<string>(boost::any_cast<string>(m["upload_id"]));
    }
  }


  ~CompleteFileRequest() = default;
};
class CopyFileRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<bool> autoRename{};
  shared_ptr<string> driveId{};
  shared_ptr<string> fileId{};
  shared_ptr<string> newName{};
  shared_ptr<string> shareId{};
  shared_ptr<string> toDriveId{};
  shared_ptr<string> toParentFileId{};

  CopyFileRequest() {}

  explicit CopyFileRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    if (!fileId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("fileId is required.")));
    }
    Darabonba::Model::validateMaxLength("fileId", fileId, 50);
    Darabonba::Model::validateMinLength("fileId", fileId, 40);
    Darabonba::Model::validatePattern("fileId", fileId, "[a-z0-9.-_]{1,50}");
    Darabonba::Model::validateMaxLength("newName", newName, 1024);
    Darabonba::Model::validateMinLength("newName", newName, 1);
    Darabonba::Model::validatePattern("toDriveId", toDriveId, "[0-9]+");
    if (!toParentFileId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("toParentFileId is required.")));
    }
    Darabonba::Model::validateMaxLength("toParentFileId", toParentFileId, 50);
    Darabonba::Model::validateMinLength("toParentFileId", toParentFileId, 4);
    Darabonba::Model::validatePattern("toParentFileId", toParentFileId, "[a-z0-9.-_]{1,50}");
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (autoRename) {
      res["auto_rename"] = boost::any(*autoRename);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (fileId) {
      res["file_id"] = boost::any(*fileId);
    }
    if (newName) {
      res["new_name"] = boost::any(*newName);
    }
    if (shareId) {
      res["share_id"] = boost::any(*shareId);
    }
    if (toDriveId) {
      res["to_drive_id"] = boost::any(*toDriveId);
    }
    if (toParentFileId) {
      res["to_parent_file_id"] = boost::any(*toParentFileId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("auto_rename") != m.end() && !m["auto_rename"].empty()) {
      autoRename = make_shared<bool>(boost::any_cast<bool>(m["auto_rename"]));
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("file_id") != m.end() && !m["file_id"].empty()) {
      fileId = make_shared<string>(boost::any_cast<string>(m["file_id"]));
    }
    if (m.find("new_name") != m.end() && !m["new_name"].empty()) {
      newName = make_shared<string>(boost::any_cast<string>(m["new_name"]));
    }
    if (m.find("share_id") != m.end() && !m["share_id"].empty()) {
      shareId = make_shared<string>(boost::any_cast<string>(m["share_id"]));
    }
    if (m.find("to_drive_id") != m.end() && !m["to_drive_id"].empty()) {
      toDriveId = make_shared<string>(boost::any_cast<string>(m["to_drive_id"]));
    }
    if (m.find("to_parent_file_id") != m.end() && !m["to_parent_file_id"].empty()) {
      toParentFileId = make_shared<string>(boost::any_cast<string>(m["to_parent_file_id"]));
    }
  }


  ~CopyFileRequest() = default;
};
class CreateDriveRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<bool> default_{};
  shared_ptr<string> description{};
  shared_ptr<string> driveName{};
  shared_ptr<string> driveType{};
  shared_ptr<string> encryptMode{};
  shared_ptr<string> owner{};
  shared_ptr<string> relativePath{};
  shared_ptr<string> status{};
  shared_ptr<string> storeId{};
  shared_ptr<long> totalSize{};

  CreateDriveRequest() {}

  explicit CreateDriveRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    Darabonba::Model::validateMaxLength("description", description, 1024);
    if (!driveName) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("driveName is required.")));
    }
    Darabonba::Model::validateMaxLength("driveName", driveName, 1024);
    if (!owner) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("owner is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (default_) {
      res["default"] = boost::any(*default_);
    }
    if (description) {
      res["description"] = boost::any(*description);
    }
    if (driveName) {
      res["drive_name"] = boost::any(*driveName);
    }
    if (driveType) {
      res["drive_type"] = boost::any(*driveType);
    }
    if (encryptMode) {
      res["encrypt_mode"] = boost::any(*encryptMode);
    }
    if (owner) {
      res["owner"] = boost::any(*owner);
    }
    if (relativePath) {
      res["relative_path"] = boost::any(*relativePath);
    }
    if (status) {
      res["status"] = boost::any(*status);
    }
    if (storeId) {
      res["store_id"] = boost::any(*storeId);
    }
    if (totalSize) {
      res["total_size"] = boost::any(*totalSize);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("default") != m.end() && !m["default"].empty()) {
      default_ = make_shared<bool>(boost::any_cast<bool>(m["default"]));
    }
    if (m.find("description") != m.end() && !m["description"].empty()) {
      description = make_shared<string>(boost::any_cast<string>(m["description"]));
    }
    if (m.find("drive_name") != m.end() && !m["drive_name"].empty()) {
      driveName = make_shared<string>(boost::any_cast<string>(m["drive_name"]));
    }
    if (m.find("drive_type") != m.end() && !m["drive_type"].empty()) {
      driveType = make_shared<string>(boost::any_cast<string>(m["drive_type"]));
    }
    if (m.find("encrypt_mode") != m.end() && !m["encrypt_mode"].empty()) {
      encryptMode = make_shared<string>(boost::any_cast<string>(m["encrypt_mode"]));
    }
    if (m.find("owner") != m.end() && !m["owner"].empty()) {
      owner = make_shared<string>(boost::any_cast<string>(m["owner"]));
    }
    if (m.find("relative_path") != m.end() && !m["relative_path"].empty()) {
      relativePath = make_shared<string>(boost::any_cast<string>(m["relative_path"]));
    }
    if (m.find("status") != m.end() && !m["status"].empty()) {
      status = make_shared<string>(boost::any_cast<string>(m["status"]));
    }
    if (m.find("store_id") != m.end() && !m["store_id"].empty()) {
      storeId = make_shared<string>(boost::any_cast<string>(m["store_id"]));
    }
    if (m.find("total_size") != m.end() && !m["total_size"].empty()) {
      totalSize = make_shared<long>(boost::any_cast<long>(m["total_size"]));
    }
  }


  ~CreateDriveRequest() = default;
};
class ImageMediaMetadata : public Darabonba::Model {
public:
  shared_ptr<long> height{};
  shared_ptr<long> width{};

  ImageMediaMetadata() {}

  explicit ImageMediaMetadata(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (height) {
      res["height"] = boost::any(*height);
    }
    if (width) {
      res["width"] = boost::any(*width);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("height") != m.end() && !m["height"].empty()) {
      height = make_shared<long>(boost::any_cast<long>(m["height"]));
    }
    if (m.find("width") != m.end() && !m["width"].empty()) {
      width = make_shared<long>(boost::any_cast<long>(m["width"]));
    }
  }


  ~ImageMediaMetadata() = default;
};
class VideoMediaMetadata : public Darabonba::Model {
public:
  shared_ptr<string> duration{};

  VideoMediaMetadata() {}

  explicit VideoMediaMetadata(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (duration) {
      res["duration"] = boost::any(*duration);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("duration") != m.end() && !m["duration"].empty()) {
      duration = make_shared<string>(boost::any_cast<string>(m["duration"]));
    }
  }


  ~VideoMediaMetadata() = default;
};
class CreateFileRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<map<string, boost::any>> additionData{};
  shared_ptr<bool> autoRename{};
  shared_ptr<string> checkNameMode{};
  shared_ptr<string> contentHash{};
  shared_ptr<string> contentHashName{};
  shared_ptr<string> contentMd5{};
  shared_ptr<string> contentType{};
  shared_ptr<string> description{};
  shared_ptr<string> driveId{};
  shared_ptr<string> encryptMode{};
  shared_ptr<string> fileId{};
  shared_ptr<bool> hidden{};
  shared_ptr<ImageMediaMetadata> imageMediaMetadata{};
  shared_ptr<vector<string>> labels{};
  shared_ptr<string> lastUpdatedAt{};
  shared_ptr<string> meta{};
  shared_ptr<string> name{};
  shared_ptr<string> parentFileId{};
  shared_ptr<vector<UploadPartInfo>> partInfoList{};
  shared_ptr<string> preHash{};
  shared_ptr<long> size{};
  shared_ptr<map<string, boost::any>> streamsInfo{};
  shared_ptr<string> type{};
  shared_ptr<string> userMeta{};
  shared_ptr<VideoMediaMetadata> videoMediaMetadata{};

  CreateFileRequest() {}

  explicit CreateFileRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    Darabonba::Model::validateMaxLength("description", description, 1024);
    Darabonba::Model::validateMinLength("description", description, 0);
    if (!driveId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("driveId is required.")));
    }
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    if (!name) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("name is required.")));
    }
    Darabonba::Model::validateMaxLength("name", name, 1024);
    Darabonba::Model::validateMinLength("name", name, 1);
    if (!parentFileId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("parentFileId is required.")));
    }
    Darabonba::Model::validateMaxLength("parentFileId", parentFileId, 50);
    Darabonba::Model::validateMinLength("parentFileId", parentFileId, 4);
    Darabonba::Model::validatePattern("parentFileId", parentFileId, "[a-z0-9]{1,50}");
    if (size && *size > 53687091200) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("size is required.")));
    }
    if (size && *size < 0) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("size is required.")));
    }
    if (!type) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("type is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (additionData) {
      res["addition_data"] = boost::any(*additionData);
    }
    if (autoRename) {
      res["auto_rename"] = boost::any(*autoRename);
    }
    if (checkNameMode) {
      res["check_name_mode"] = boost::any(*checkNameMode);
    }
    if (contentHash) {
      res["content_hash"] = boost::any(*contentHash);
    }
    if (contentHashName) {
      res["content_hash_name"] = boost::any(*contentHashName);
    }
    if (contentMd5) {
      res["content_md5"] = boost::any(*contentMd5);
    }
    if (contentType) {
      res["content_type"] = boost::any(*contentType);
    }
    if (description) {
      res["description"] = boost::any(*description);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (encryptMode) {
      res["encrypt_mode"] = boost::any(*encryptMode);
    }
    if (fileId) {
      res["file_id"] = boost::any(*fileId);
    }
    if (hidden) {
      res["hidden"] = boost::any(*hidden);
    }
    if (imageMediaMetadata) {
      res["image_media_metadata"] = imageMediaMetadata ? boost::any(imageMediaMetadata->toMap()) : boost::any(map<string,boost::any>({}));
    }
    if (labels) {
      res["labels"] = boost::any(*labels);
    }
    if (lastUpdatedAt) {
      res["last_updated_at"] = boost::any(*lastUpdatedAt);
    }
    if (meta) {
      res["meta"] = boost::any(*meta);
    }
    if (name) {
      res["name"] = boost::any(*name);
    }
    if (parentFileId) {
      res["parent_file_id"] = boost::any(*parentFileId);
    }
    if (partInfoList) {
      vector<boost::any> temp1;
      for(auto item1:*partInfoList){
        temp1.push_back(boost::any(item1.toMap()));
      }
      res["part_info_list"] = boost::any(temp1);
    }
    if (preHash) {
      res["pre_hash"] = boost::any(*preHash);
    }
    if (size) {
      res["size"] = boost::any(*size);
    }
    if (streamsInfo) {
      res["streams_info"] = boost::any(*streamsInfo);
    }
    if (type) {
      res["type"] = boost::any(*type);
    }
    if (userMeta) {
      res["user_meta"] = boost::any(*userMeta);
    }
    if (videoMediaMetadata) {
      res["video_media_metadata"] = videoMediaMetadata ? boost::any(videoMediaMetadata->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("addition_data") != m.end() && !m["addition_data"].empty()) {
      map<string, boost::any> map1 = boost::any_cast<map<string, boost::any>>(m["addition_data"]);
      map<string, boost::any> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      additionData = make_shared<map<string, boost::any>>(toMap1);
    }
    if (m.find("auto_rename") != m.end() && !m["auto_rename"].empty()) {
      autoRename = make_shared<bool>(boost::any_cast<bool>(m["auto_rename"]));
    }
    if (m.find("check_name_mode") != m.end() && !m["check_name_mode"].empty()) {
      checkNameMode = make_shared<string>(boost::any_cast<string>(m["check_name_mode"]));
    }
    if (m.find("content_hash") != m.end() && !m["content_hash"].empty()) {
      contentHash = make_shared<string>(boost::any_cast<string>(m["content_hash"]));
    }
    if (m.find("content_hash_name") != m.end() && !m["content_hash_name"].empty()) {
      contentHashName = make_shared<string>(boost::any_cast<string>(m["content_hash_name"]));
    }
    if (m.find("content_md5") != m.end() && !m["content_md5"].empty()) {
      contentMd5 = make_shared<string>(boost::any_cast<string>(m["content_md5"]));
    }
    if (m.find("content_type") != m.end() && !m["content_type"].empty()) {
      contentType = make_shared<string>(boost::any_cast<string>(m["content_type"]));
    }
    if (m.find("description") != m.end() && !m["description"].empty()) {
      description = make_shared<string>(boost::any_cast<string>(m["description"]));
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("encrypt_mode") != m.end() && !m["encrypt_mode"].empty()) {
      encryptMode = make_shared<string>(boost::any_cast<string>(m["encrypt_mode"]));
    }
    if (m.find("file_id") != m.end() && !m["file_id"].empty()) {
      fileId = make_shared<string>(boost::any_cast<string>(m["file_id"]));
    }
    if (m.find("hidden") != m.end() && !m["hidden"].empty()) {
      hidden = make_shared<bool>(boost::any_cast<bool>(m["hidden"]));
    }
    if (m.find("image_media_metadata") != m.end() && !m["image_media_metadata"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["image_media_metadata"].type().name()) {
        ImageMediaMetadata model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["image_media_metadata"]));
        imageMediaMetadata = make_shared<ImageMediaMetadata>(model1);
      }
    }
    if (m.find("labels") != m.end() && !m["labels"].empty()) {
      vector<string> toVec1;
      if (typeid(vector<boost::any>).name() == m["labels"].type().name()) {
        vector<boost::any> vec1 = boost::any_cast<vector<boost::any>>(m["labels"]);
        for (auto item:vec1) {
           toVec1.push_back(boost::any_cast<string>(item));
        }
      }
      labels = make_shared<vector<string>>(toVec1);
    }
    if (m.find("last_updated_at") != m.end() && !m["last_updated_at"].empty()) {
      lastUpdatedAt = make_shared<string>(boost::any_cast<string>(m["last_updated_at"]));
    }
    if (m.find("meta") != m.end() && !m["meta"].empty()) {
      meta = make_shared<string>(boost::any_cast<string>(m["meta"]));
    }
    if (m.find("name") != m.end() && !m["name"].empty()) {
      name = make_shared<string>(boost::any_cast<string>(m["name"]));
    }
    if (m.find("parent_file_id") != m.end() && !m["parent_file_id"].empty()) {
      parentFileId = make_shared<string>(boost::any_cast<string>(m["parent_file_id"]));
    }
    if (m.find("part_info_list") != m.end() && !m["part_info_list"].empty()) {
      if (typeid(vector<boost::any>).name() == m["part_info_list"].type().name()) {
        vector<UploadPartInfo> expect1;
        for(auto item1:boost::any_cast<vector<boost::any>>(m["part_info_list"])){
          if (typeid(map<string, boost::any>).name() == item1.type().name()) {
            UploadPartInfo model2;
            model2.fromMap(boost::any_cast<map<string, boost::any>>(item1));
            expect1.push_back(model2);
          }
        }
        partInfoList = make_shared<vector<UploadPartInfo>>(expect1);
      }
    }
    if (m.find("pre_hash") != m.end() && !m["pre_hash"].empty()) {
      preHash = make_shared<string>(boost::any_cast<string>(m["pre_hash"]));
    }
    if (m.find("size") != m.end() && !m["size"].empty()) {
      size = make_shared<long>(boost::any_cast<long>(m["size"]));
    }
    if (m.find("streams_info") != m.end() && !m["streams_info"].empty()) {
      map<string, boost::any> map1 = boost::any_cast<map<string, boost::any>>(m["streams_info"]);
      map<string, boost::any> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      streamsInfo = make_shared<map<string, boost::any>>(toMap1);
    }
    if (m.find("type") != m.end() && !m["type"].empty()) {
      type = make_shared<string>(boost::any_cast<string>(m["type"]));
    }
    if (m.find("user_meta") != m.end() && !m["user_meta"].empty()) {
      userMeta = make_shared<string>(boost::any_cast<string>(m["user_meta"]));
    }
    if (m.find("video_media_metadata") != m.end() && !m["video_media_metadata"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["video_media_metadata"].type().name()) {
        VideoMediaMetadata model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["video_media_metadata"]));
        videoMediaMetadata = make_shared<VideoMediaMetadata>(model1);
      }
    }
  }


  ~CreateFileRequest() = default;
};
class CreateShareLinkRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<string> driveId{};
  shared_ptr<string> expiration{};
  shared_ptr<string> fileId{};
  shared_ptr<string> sharePwd{};

  CreateShareLinkRequest() {}

  explicit CreateShareLinkRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!driveId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("driveId is required.")));
    }
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    if (!expiration) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("expiration is required.")));
    }
    if (!fileId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("fileId is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (expiration) {
      res["expiration"] = boost::any(*expiration);
    }
    if (fileId) {
      res["file_id"] = boost::any(*fileId);
    }
    if (sharePwd) {
      res["share_pwd"] = boost::any(*sharePwd);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("expiration") != m.end() && !m["expiration"].empty()) {
      expiration = make_shared<string>(boost::any_cast<string>(m["expiration"]));
    }
    if (m.find("file_id") != m.end() && !m["file_id"].empty()) {
      fileId = make_shared<string>(boost::any_cast<string>(m["file_id"]));
    }
    if (m.find("share_pwd") != m.end() && !m["share_pwd"].empty()) {
      sharePwd = make_shared<string>(boost::any_cast<string>(m["share_pwd"]));
    }
  }


  ~CreateShareLinkRequest() = default;
};
class CreateShareRequest : public Darabonba::Model {
public:
  shared_ptr<string> description{};
  shared_ptr<string> driveId{};
  shared_ptr<string> expiration{};
  shared_ptr<string> owner{};
  shared_ptr<vector<string>> permissions{};
  shared_ptr<string> shareFilePath{};
  shared_ptr<string> shareName{};
  shared_ptr<vector<SharePermissionPolicy>> sharePolicy{};
  shared_ptr<string> status{};

  CreateShareRequest() {}

  explicit CreateShareRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!driveId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("driveId is required.")));
    }
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    if (!owner) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("owner is required.")));
    }
    if (!shareFilePath) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("shareFilePath is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (description) {
      res["description"] = boost::any(*description);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (expiration) {
      res["expiration"] = boost::any(*expiration);
    }
    if (owner) {
      res["owner"] = boost::any(*owner);
    }
    if (permissions) {
      res["permissions"] = boost::any(*permissions);
    }
    if (shareFilePath) {
      res["share_file_path"] = boost::any(*shareFilePath);
    }
    if (shareName) {
      res["share_name"] = boost::any(*shareName);
    }
    if (sharePolicy) {
      vector<boost::any> temp1;
      for(auto item1:*sharePolicy){
        temp1.push_back(boost::any(item1.toMap()));
      }
      res["share_policy"] = boost::any(temp1);
    }
    if (status) {
      res["status"] = boost::any(*status);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("description") != m.end() && !m["description"].empty()) {
      description = make_shared<string>(boost::any_cast<string>(m["description"]));
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("expiration") != m.end() && !m["expiration"].empty()) {
      expiration = make_shared<string>(boost::any_cast<string>(m["expiration"]));
    }
    if (m.find("owner") != m.end() && !m["owner"].empty()) {
      owner = make_shared<string>(boost::any_cast<string>(m["owner"]));
    }
    if (m.find("permissions") != m.end() && !m["permissions"].empty()) {
      vector<string> toVec1;
      if (typeid(vector<boost::any>).name() == m["permissions"].type().name()) {
        vector<boost::any> vec1 = boost::any_cast<vector<boost::any>>(m["permissions"]);
        for (auto item:vec1) {
           toVec1.push_back(boost::any_cast<string>(item));
        }
      }
      permissions = make_shared<vector<string>>(toVec1);
    }
    if (m.find("share_file_path") != m.end() && !m["share_file_path"].empty()) {
      shareFilePath = make_shared<string>(boost::any_cast<string>(m["share_file_path"]));
    }
    if (m.find("share_name") != m.end() && !m["share_name"].empty()) {
      shareName = make_shared<string>(boost::any_cast<string>(m["share_name"]));
    }
    if (m.find("share_policy") != m.end() && !m["share_policy"].empty()) {
      if (typeid(vector<boost::any>).name() == m["share_policy"].type().name()) {
        vector<SharePermissionPolicy> expect1;
        for(auto item1:boost::any_cast<vector<boost::any>>(m["share_policy"])){
          if (typeid(map<string, boost::any>).name() == item1.type().name()) {
            SharePermissionPolicy model2;
            model2.fromMap(boost::any_cast<map<string, boost::any>>(item1));
            expect1.push_back(model2);
          }
        }
        sharePolicy = make_shared<vector<SharePermissionPolicy>>(expect1);
      }
    }
    if (m.find("status") != m.end() && !m["status"].empty()) {
      status = make_shared<string>(boost::any_cast<string>(m["status"]));
    }
  }


  ~CreateShareRequest() = default;
};
class DeleteDriveRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<string> driveId{};

  DeleteDriveRequest() {}

  explicit DeleteDriveRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!driveId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("driveId is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
  }


  ~DeleteDriveRequest() = default;
};
class DeleteFileRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<string> driveId{};
  shared_ptr<string> fileId{};
  shared_ptr<bool> permanently{};

  DeleteFileRequest() {}

  explicit DeleteFileRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!driveId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("driveId is required.")));
    }
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    if (!fileId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("fileId is required.")));
    }
    Darabonba::Model::validateMaxLength("fileId", fileId, 50);
    Darabonba::Model::validateMinLength("fileId", fileId, 40);
    Darabonba::Model::validatePattern("fileId", fileId, "[a-z0-9.-_]{1,50}");
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (fileId) {
      res["file_id"] = boost::any(*fileId);
    }
    if (permanently) {
      res["permanently"] = boost::any(*permanently);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("file_id") != m.end() && !m["file_id"].empty()) {
      fileId = make_shared<string>(boost::any_cast<string>(m["file_id"]));
    }
    if (m.find("permanently") != m.end() && !m["permanently"].empty()) {
      permanently = make_shared<bool>(boost::any_cast<bool>(m["permanently"]));
    }
  }


  ~DeleteFileRequest() = default;
};
class DeleteFilesRequest : public Darabonba::Model {
public:
  shared_ptr<string> driveId{};
  shared_ptr<vector<string>> fileIdList{};

  DeleteFilesRequest() {}

  explicit DeleteFilesRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!driveId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("driveId is required.")));
    }
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    if (!fileIdList) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("fileIdList is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (fileIdList) {
      res["file_id_list"] = boost::any(*fileIdList);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("file_id_list") != m.end() && !m["file_id_list"].empty()) {
      vector<string> toVec1;
      if (typeid(vector<boost::any>).name() == m["file_id_list"].type().name()) {
        vector<boost::any> vec1 = boost::any_cast<vector<boost::any>>(m["file_id_list"]);
        for (auto item:vec1) {
           toVec1.push_back(boost::any_cast<string>(item));
        }
      }
      fileIdList = make_shared<vector<string>>(toVec1);
    }
  }


  ~DeleteFilesRequest() = default;
};
class DeleteShareRequest : public Darabonba::Model {
public:
  shared_ptr<string> shareId{};

  DeleteShareRequest() {}

  explicit DeleteShareRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!shareId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("shareId is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (shareId) {
      res["share_id"] = boost::any(*shareId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("share_id") != m.end() && !m["share_id"].empty()) {
      shareId = make_shared<string>(boost::any_cast<string>(m["share_id"]));
    }
  }


  ~DeleteShareRequest() = default;
};
class DownloadRequest : public Darabonba::Model {
public:
  shared_ptr<string> DriveID{};
  shared_ptr<string> FileID{};
  shared_ptr<string> ImageThumbnailProcess{};
  shared_ptr<string> ShareID{};
  shared_ptr<string> VideoThumbnailProcess{};

  DownloadRequest() {}

  explicit DownloadRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!FileID) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("FileID is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (DriveID) {
      res["DriveID"] = boost::any(*DriveID);
    }
    if (FileID) {
      res["FileID"] = boost::any(*FileID);
    }
    if (ImageThumbnailProcess) {
      res["ImageThumbnailProcess"] = boost::any(*ImageThumbnailProcess);
    }
    if (ShareID) {
      res["ShareID"] = boost::any(*ShareID);
    }
    if (VideoThumbnailProcess) {
      res["VideoThumbnailProcess"] = boost::any(*VideoThumbnailProcess);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("DriveID") != m.end() && !m["DriveID"].empty()) {
      DriveID = make_shared<string>(boost::any_cast<string>(m["DriveID"]));
    }
    if (m.find("FileID") != m.end() && !m["FileID"].empty()) {
      FileID = make_shared<string>(boost::any_cast<string>(m["FileID"]));
    }
    if (m.find("ImageThumbnailProcess") != m.end() && !m["ImageThumbnailProcess"].empty()) {
      ImageThumbnailProcess = make_shared<string>(boost::any_cast<string>(m["ImageThumbnailProcess"]));
    }
    if (m.find("ShareID") != m.end() && !m["ShareID"].empty()) {
      ShareID = make_shared<string>(boost::any_cast<string>(m["ShareID"]));
    }
    if (m.find("VideoThumbnailProcess") != m.end() && !m["VideoThumbnailProcess"].empty()) {
      VideoThumbnailProcess = make_shared<string>(boost::any_cast<string>(m["VideoThumbnailProcess"]));
    }
  }


  ~DownloadRequest() = default;
};
class GetAsyncTaskRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<string> asyncTaskId{};

  GetAsyncTaskRequest() {}

  explicit GetAsyncTaskRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (asyncTaskId) {
      res["async_task_id"] = boost::any(*asyncTaskId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("async_task_id") != m.end() && !m["async_task_id"].empty()) {
      asyncTaskId = make_shared<string>(boost::any_cast<string>(m["async_task_id"]));
    }
  }


  ~GetAsyncTaskRequest() = default;
};
class GetDefaultDriveRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<string> userId{};

  GetDefaultDriveRequest() {}

  explicit GetDefaultDriveRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (userId) {
      res["user_id"] = boost::any(*userId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("user_id") != m.end() && !m["user_id"].empty()) {
      userId = make_shared<string>(boost::any_cast<string>(m["user_id"]));
    }
  }


  ~GetDefaultDriveRequest() = default;
};
class GetDownloadUrlRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<map<string, boost::any>> additionData{};
  shared_ptr<string> driveId{};
  shared_ptr<long> expireSec{};
  shared_ptr<string> fileId{};
  shared_ptr<string> fileName{};

  GetDownloadUrlRequest() {}

  explicit GetDownloadUrlRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!driveId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("driveId is required.")));
    }
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    if (expireSec && *expireSec > 14400) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("expireSec is required.")));
    }
    if (expireSec && *expireSec < 0) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("expireSec is required.")));
    }
    if (!fileId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("fileId is required.")));
    }
    Darabonba::Model::validateMaxLength("fileId", fileId, 50);
    Darabonba::Model::validateMinLength("fileId", fileId, 40);
    Darabonba::Model::validatePattern("fileId", fileId, "[a-z0-9.-_]{1,50}");
    Darabonba::Model::validateMaxLength("fileName", fileName, 1024);
    Darabonba::Model::validateMinLength("fileName", fileName, 1);
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (additionData) {
      res["addition_data"] = boost::any(*additionData);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (expireSec) {
      res["expire_sec"] = boost::any(*expireSec);
    }
    if (fileId) {
      res["file_id"] = boost::any(*fileId);
    }
    if (fileName) {
      res["file_name"] = boost::any(*fileName);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("addition_data") != m.end() && !m["addition_data"].empty()) {
      map<string, boost::any> map1 = boost::any_cast<map<string, boost::any>>(m["addition_data"]);
      map<string, boost::any> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      additionData = make_shared<map<string, boost::any>>(toMap1);
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("expire_sec") != m.end() && !m["expire_sec"].empty()) {
      expireSec = make_shared<long>(boost::any_cast<long>(m["expire_sec"]));
    }
    if (m.find("file_id") != m.end() && !m["file_id"].empty()) {
      fileId = make_shared<string>(boost::any_cast<string>(m["file_id"]));
    }
    if (m.find("file_name") != m.end() && !m["file_name"].empty()) {
      fileName = make_shared<string>(boost::any_cast<string>(m["file_name"]));
    }
  }


  ~GetDownloadUrlRequest() = default;
};
class GetDriveRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<string> driveId{};

  GetDriveRequest() {}

  explicit GetDriveRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!driveId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("driveId is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
  }


  ~GetDriveRequest() = default;
};
class GetFileByPathRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<string> driveId{};
  shared_ptr<string> fields{};
  shared_ptr<string> fileId{};
  shared_ptr<string> filePath{};
  shared_ptr<string> imageThumbnailProcess{};
  shared_ptr<string> imageUrlProcess{};
  shared_ptr<long> urlExpireSec{};
  shared_ptr<string> videoThumbnailProcess{};

  GetFileByPathRequest() {}

  explicit GetFileByPathRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!driveId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("driveId is required.")));
    }
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    if (!fileId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("fileId is required.")));
    }
    Darabonba::Model::validateMaxLength("fileId", fileId, 50);
    Darabonba::Model::validateMinLength("fileId", fileId, 40);
    Darabonba::Model::validatePattern("fileId", fileId, "[a-z0-9.-_]{1,50}");
    if (urlExpireSec && *urlExpireSec > 14400) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("urlExpireSec is required.")));
    }
    if (urlExpireSec && *urlExpireSec < 10) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("urlExpireSec is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (fields) {
      res["fields"] = boost::any(*fields);
    }
    if (fileId) {
      res["file_id"] = boost::any(*fileId);
    }
    if (filePath) {
      res["file_path"] = boost::any(*filePath);
    }
    if (imageThumbnailProcess) {
      res["image_thumbnail_process"] = boost::any(*imageThumbnailProcess);
    }
    if (imageUrlProcess) {
      res["image_url_process"] = boost::any(*imageUrlProcess);
    }
    if (urlExpireSec) {
      res["url_expire_sec"] = boost::any(*urlExpireSec);
    }
    if (videoThumbnailProcess) {
      res["video_thumbnail_process"] = boost::any(*videoThumbnailProcess);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("fields") != m.end() && !m["fields"].empty()) {
      fields = make_shared<string>(boost::any_cast<string>(m["fields"]));
    }
    if (m.find("file_id") != m.end() && !m["file_id"].empty()) {
      fileId = make_shared<string>(boost::any_cast<string>(m["file_id"]));
    }
    if (m.find("file_path") != m.end() && !m["file_path"].empty()) {
      filePath = make_shared<string>(boost::any_cast<string>(m["file_path"]));
    }
    if (m.find("image_thumbnail_process") != m.end() && !m["image_thumbnail_process"].empty()) {
      imageThumbnailProcess = make_shared<string>(boost::any_cast<string>(m["image_thumbnail_process"]));
    }
    if (m.find("image_url_process") != m.end() && !m["image_url_process"].empty()) {
      imageUrlProcess = make_shared<string>(boost::any_cast<string>(m["image_url_process"]));
    }
    if (m.find("url_expire_sec") != m.end() && !m["url_expire_sec"].empty()) {
      urlExpireSec = make_shared<long>(boost::any_cast<long>(m["url_expire_sec"]));
    }
    if (m.find("video_thumbnail_process") != m.end() && !m["video_thumbnail_process"].empty()) {
      videoThumbnailProcess = make_shared<string>(boost::any_cast<string>(m["video_thumbnail_process"]));
    }
  }


  ~GetFileByPathRequest() = default;
};
class GetFileRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<string> driveId{};
  shared_ptr<string> fields{};
  shared_ptr<string> fileId{};
  shared_ptr<string> imageThumbnailProcess{};
  shared_ptr<string> imageUrlProcess{};
  shared_ptr<long> urlExpireSec{};
  shared_ptr<string> videoThumbnailProcess{};

  GetFileRequest() {}

  explicit GetFileRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!driveId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("driveId is required.")));
    }
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    if (!fileId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("fileId is required.")));
    }
    Darabonba::Model::validateMaxLength("fileId", fileId, 50);
    Darabonba::Model::validateMinLength("fileId", fileId, 40);
    Darabonba::Model::validatePattern("fileId", fileId, "[a-z0-9.-_]{1,50}");
    if (urlExpireSec && *urlExpireSec > 14400) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("urlExpireSec is required.")));
    }
    if (urlExpireSec && *urlExpireSec < 10) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("urlExpireSec is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (fields) {
      res["fields"] = boost::any(*fields);
    }
    if (fileId) {
      res["file_id"] = boost::any(*fileId);
    }
    if (imageThumbnailProcess) {
      res["image_thumbnail_process"] = boost::any(*imageThumbnailProcess);
    }
    if (imageUrlProcess) {
      res["image_url_process"] = boost::any(*imageUrlProcess);
    }
    if (urlExpireSec) {
      res["url_expire_sec"] = boost::any(*urlExpireSec);
    }
    if (videoThumbnailProcess) {
      res["video_thumbnail_process"] = boost::any(*videoThumbnailProcess);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("fields") != m.end() && !m["fields"].empty()) {
      fields = make_shared<string>(boost::any_cast<string>(m["fields"]));
    }
    if (m.find("file_id") != m.end() && !m["file_id"].empty()) {
      fileId = make_shared<string>(boost::any_cast<string>(m["file_id"]));
    }
    if (m.find("image_thumbnail_process") != m.end() && !m["image_thumbnail_process"].empty()) {
      imageThumbnailProcess = make_shared<string>(boost::any_cast<string>(m["image_thumbnail_process"]));
    }
    if (m.find("image_url_process") != m.end() && !m["image_url_process"].empty()) {
      imageUrlProcess = make_shared<string>(boost::any_cast<string>(m["image_url_process"]));
    }
    if (m.find("url_expire_sec") != m.end() && !m["url_expire_sec"].empty()) {
      urlExpireSec = make_shared<long>(boost::any_cast<long>(m["url_expire_sec"]));
    }
    if (m.find("video_thumbnail_process") != m.end() && !m["video_thumbnail_process"].empty()) {
      videoThumbnailProcess = make_shared<string>(boost::any_cast<string>(m["video_thumbnail_process"]));
    }
  }


  ~GetFileRequest() = default;
};
class GetLastCursorRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<string> driveId{};

  GetLastCursorRequest() {}

  explicit GetLastCursorRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!driveId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("driveId is required.")));
    }
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
  }


  ~GetLastCursorRequest() = default;
};
class GetMediaPlayURLRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<string> driveId{};
  shared_ptr<string> fileId{};

  GetMediaPlayURLRequest() {}

  explicit GetMediaPlayURLRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!driveId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("driveId is required.")));
    }
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    if (!fileId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("fileId is required.")));
    }
    Darabonba::Model::validateMaxLength("fileId", fileId, 50);
    Darabonba::Model::validateMinLength("fileId", fileId, 40);
    Darabonba::Model::validatePattern("fileId", fileId, "[a-z0-9.-_]{1,50}");
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (fileId) {
      res["file_id"] = boost::any(*fileId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("file_id") != m.end() && !m["file_id"].empty()) {
      fileId = make_shared<string>(boost::any_cast<string>(m["file_id"]));
    }
  }


  ~GetMediaPlayURLRequest() = default;
};
class GetOfficePreviewUrlRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<map<string, boost::any>> additionData{};
  shared_ptr<string> driveId{};
  shared_ptr<string> fileId{};

  GetOfficePreviewUrlRequest() {}

  explicit GetOfficePreviewUrlRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!driveId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("driveId is required.")));
    }
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    if (!fileId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("fileId is required.")));
    }
    Darabonba::Model::validateMaxLength("fileId", fileId, 50);
    Darabonba::Model::validateMinLength("fileId", fileId, 40);
    Darabonba::Model::validatePattern("fileId", fileId, "[a-z0-9.-_]{1,50}");
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (additionData) {
      res["addition_data"] = boost::any(*additionData);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (fileId) {
      res["file_id"] = boost::any(*fileId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("addition_data") != m.end() && !m["addition_data"].empty()) {
      map<string, boost::any> map1 = boost::any_cast<map<string, boost::any>>(m["addition_data"]);
      map<string, boost::any> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      additionData = make_shared<map<string, boost::any>>(toMap1);
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("file_id") != m.end() && !m["file_id"].empty()) {
      fileId = make_shared<string>(boost::any_cast<string>(m["file_id"]));
    }
  }


  ~GetOfficePreviewUrlRequest() = default;
};
class GetShareLinkByAnonymousRequest : public Darabonba::Model {
public:
  shared_ptr<string> shareId{};

  GetShareLinkByAnonymousRequest() {}

  explicit GetShareLinkByAnonymousRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (shareId) {
      res["share_id"] = boost::any(*shareId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("share_id") != m.end() && !m["share_id"].empty()) {
      shareId = make_shared<string>(boost::any_cast<string>(m["share_id"]));
    }
  }


  ~GetShareLinkByAnonymousRequest() = default;
};
class GetShareLinkIDRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<string> shareMsg{};

  GetShareLinkIDRequest() {}

  explicit GetShareLinkIDRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (shareMsg) {
      res["share_msg"] = boost::any(*shareMsg);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("share_msg") != m.end() && !m["share_msg"].empty()) {
      shareMsg = make_shared<string>(boost::any_cast<string>(m["share_msg"]));
    }
  }


  ~GetShareLinkIDRequest() = default;
};
class GetShareLinkTokenRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<string> shareId{};
  shared_ptr<string> sharePwd{};

  GetShareLinkTokenRequest() {}

  explicit GetShareLinkTokenRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (shareId) {
      res["share_id"] = boost::any(*shareId);
    }
    if (sharePwd) {
      res["share_pwd"] = boost::any(*sharePwd);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("share_id") != m.end() && !m["share_id"].empty()) {
      shareId = make_shared<string>(boost::any_cast<string>(m["share_id"]));
    }
    if (m.find("share_pwd") != m.end() && !m["share_pwd"].empty()) {
      sharePwd = make_shared<string>(boost::any_cast<string>(m["share_pwd"]));
    }
  }


  ~GetShareLinkTokenRequest() = default;
};
class GetShareRequest : public Darabonba::Model {
public:
  shared_ptr<string> shareId{};

  GetShareRequest() {}

  explicit GetShareRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (shareId) {
      res["share_id"] = boost::any(*shareId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("share_id") != m.end() && !m["share_id"].empty()) {
      shareId = make_shared<string>(boost::any_cast<string>(m["share_id"]));
    }
  }


  ~GetShareRequest() = default;
};
class GetUploadUrlRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<string> contentMd5{};
  shared_ptr<string> driveId{};
  shared_ptr<string> fileId{};
  shared_ptr<vector<UploadPartInfo>> partInfoList{};
  shared_ptr<string> uploadId{};

  GetUploadUrlRequest() {}

  explicit GetUploadUrlRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    Darabonba::Model::validateMaxLength("contentMd5", contentMd5, 32);
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    if (!fileId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("fileId is required.")));
    }
    Darabonba::Model::validateMaxLength("fileId", fileId, 50);
    Darabonba::Model::validateMinLength("fileId", fileId, 40);
    Darabonba::Model::validatePattern("fileId", fileId, "[a-z0-9]{1,50}");
    if (!uploadId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("uploadId is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (contentMd5) {
      res["content_md5"] = boost::any(*contentMd5);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (fileId) {
      res["file_id"] = boost::any(*fileId);
    }
    if (partInfoList) {
      vector<boost::any> temp1;
      for(auto item1:*partInfoList){
        temp1.push_back(boost::any(item1.toMap()));
      }
      res["part_info_list"] = boost::any(temp1);
    }
    if (uploadId) {
      res["upload_id"] = boost::any(*uploadId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("content_md5") != m.end() && !m["content_md5"].empty()) {
      contentMd5 = make_shared<string>(boost::any_cast<string>(m["content_md5"]));
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("file_id") != m.end() && !m["file_id"].empty()) {
      fileId = make_shared<string>(boost::any_cast<string>(m["file_id"]));
    }
    if (m.find("part_info_list") != m.end() && !m["part_info_list"].empty()) {
      if (typeid(vector<boost::any>).name() == m["part_info_list"].type().name()) {
        vector<UploadPartInfo> expect1;
        for(auto item1:boost::any_cast<vector<boost::any>>(m["part_info_list"])){
          if (typeid(map<string, boost::any>).name() == item1.type().name()) {
            UploadPartInfo model2;
            model2.fromMap(boost::any_cast<map<string, boost::any>>(item1));
            expect1.push_back(model2);
          }
        }
        partInfoList = make_shared<vector<UploadPartInfo>>(expect1);
      }
    }
    if (m.find("upload_id") != m.end() && !m["upload_id"].empty()) {
      uploadId = make_shared<string>(boost::any_cast<string>(m["upload_id"]));
    }
  }


  ~GetUploadUrlRequest() = default;
};
class GetVideoPreviewSpriteURLRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<string> driveId{};
  shared_ptr<long> expireSec{};
  shared_ptr<string> fileId{};

  GetVideoPreviewSpriteURLRequest() {}

  explicit GetVideoPreviewSpriteURLRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!driveId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("driveId is required.")));
    }
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    if (expireSec && *expireSec > 14400) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("expireSec is required.")));
    }
    if (expireSec && *expireSec < 0) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("expireSec is required.")));
    }
    if (!fileId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("fileId is required.")));
    }
    Darabonba::Model::validateMaxLength("fileId", fileId, 50);
    Darabonba::Model::validateMinLength("fileId", fileId, 40);
    Darabonba::Model::validatePattern("fileId", fileId, "[a-z0-9.-_]{1,50}");
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (expireSec) {
      res["expire_sec"] = boost::any(*expireSec);
    }
    if (fileId) {
      res["file_id"] = boost::any(*fileId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("expire_sec") != m.end() && !m["expire_sec"].empty()) {
      expireSec = make_shared<long>(boost::any_cast<long>(m["expire_sec"]));
    }
    if (m.find("file_id") != m.end() && !m["file_id"].empty()) {
      fileId = make_shared<string>(boost::any_cast<string>(m["file_id"]));
    }
  }


  ~GetVideoPreviewSpriteURLRequest() = default;
};
class GetVideoPreviewURLRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<map<string, boost::any>> additionData{};
  shared_ptr<string> driveId{};
  shared_ptr<long> expireSec{};
  shared_ptr<string> fileId{};
  shared_ptr<string> templateId{};

  GetVideoPreviewURLRequest() {}

  explicit GetVideoPreviewURLRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!driveId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("driveId is required.")));
    }
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    if (expireSec && *expireSec > 14400) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("expireSec is required.")));
    }
    if (expireSec && *expireSec < 0) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("expireSec is required.")));
    }
    if (!fileId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("fileId is required.")));
    }
    Darabonba::Model::validateMaxLength("fileId", fileId, 50);
    Darabonba::Model::validateMinLength("fileId", fileId, 40);
    Darabonba::Model::validatePattern("fileId", fileId, "[a-z0-9.-_]{1,50}");
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (additionData) {
      res["addition_data"] = boost::any(*additionData);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (expireSec) {
      res["expire_sec"] = boost::any(*expireSec);
    }
    if (fileId) {
      res["file_id"] = boost::any(*fileId);
    }
    if (templateId) {
      res["template_id"] = boost::any(*templateId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("addition_data") != m.end() && !m["addition_data"].empty()) {
      map<string, boost::any> map1 = boost::any_cast<map<string, boost::any>>(m["addition_data"]);
      map<string, boost::any> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      additionData = make_shared<map<string, boost::any>>(toMap1);
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("expire_sec") != m.end() && !m["expire_sec"].empty()) {
      expireSec = make_shared<long>(boost::any_cast<long>(m["expire_sec"]));
    }
    if (m.find("file_id") != m.end() && !m["file_id"].empty()) {
      fileId = make_shared<string>(boost::any_cast<string>(m["file_id"]));
    }
    if (m.find("template_id") != m.end() && !m["template_id"].empty()) {
      templateId = make_shared<string>(boost::any_cast<string>(m["template_id"]));
    }
  }


  ~GetVideoPreviewURLRequest() = default;
};
class ListByAnonymousRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<long> limit{};
  shared_ptr<string> marker{};
  shared_ptr<string> parentFileId{};
  shared_ptr<string> shareId{};

  ListByAnonymousRequest() {}

  explicit ListByAnonymousRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (limit && *limit > 100) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("limit is required.")));
    }
    if (limit && *limit < 1) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("limit is required.")));
    }
    if (!parentFileId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("parentFileId is required.")));
    }
    Darabonba::Model::validateMaxLength("parentFileId", parentFileId, 50);
    Darabonba::Model::validateMinLength("parentFileId", parentFileId, 4);
    Darabonba::Model::validatePattern("parentFileId", parentFileId, "[a-z0-9]{1,50}");
    if (!shareId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("shareId is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (limit) {
      res["limit"] = boost::any(*limit);
    }
    if (marker) {
      res["marker"] = boost::any(*marker);
    }
    if (parentFileId) {
      res["parent_file_id"] = boost::any(*parentFileId);
    }
    if (shareId) {
      res["share_id"] = boost::any(*shareId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("limit") != m.end() && !m["limit"].empty()) {
      limit = make_shared<long>(boost::any_cast<long>(m["limit"]));
    }
    if (m.find("marker") != m.end() && !m["marker"].empty()) {
      marker = make_shared<string>(boost::any_cast<string>(m["marker"]));
    }
    if (m.find("parent_file_id") != m.end() && !m["parent_file_id"].empty()) {
      parentFileId = make_shared<string>(boost::any_cast<string>(m["parent_file_id"]));
    }
    if (m.find("share_id") != m.end() && !m["share_id"].empty()) {
      shareId = make_shared<string>(boost::any_cast<string>(m["share_id"]));
    }
  }


  ~ListByAnonymousRequest() = default;
};
class ListDriveRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<long> limit{};
  shared_ptr<string> marker{};
  shared_ptr<string> owner{};

  ListDriveRequest() {}

  explicit ListDriveRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (limit && *limit > 100) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("limit is required.")));
    }
    if (limit && *limit < 1) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("limit is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (limit) {
      res["limit"] = boost::any(*limit);
    }
    if (marker) {
      res["marker"] = boost::any(*marker);
    }
    if (owner) {
      res["owner"] = boost::any(*owner);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("limit") != m.end() && !m["limit"].empty()) {
      limit = make_shared<long>(boost::any_cast<long>(m["limit"]));
    }
    if (m.find("marker") != m.end() && !m["marker"].empty()) {
      marker = make_shared<string>(boost::any_cast<string>(m["marker"]));
    }
    if (m.find("owner") != m.end() && !m["owner"].empty()) {
      owner = make_shared<string>(boost::any_cast<string>(m["owner"]));
    }
  }


  ~ListDriveRequest() = default;
};
class ListFileByCustomIndexKeyRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<bool> Starred{};
  shared_ptr<string> category{};
  shared_ptr<string> customIndexKey{};
  shared_ptr<string> driveId{};
  shared_ptr<string> encryptMode{};
  shared_ptr<string> fields{};
  shared_ptr<string> imageThumbnailProcess{};
  shared_ptr<string> imageUrlProcess{};
  shared_ptr<long> limit{};
  shared_ptr<string> marker{};
  shared_ptr<string> orderDirection{};
  shared_ptr<string> status{};
  shared_ptr<string> type{};
  shared_ptr<long> urlExpireSec{};
  shared_ptr<string> videoThumbnailProcess{};

  ListFileByCustomIndexKeyRequest() {}

  explicit ListFileByCustomIndexKeyRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!customIndexKey) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("customIndexKey is required.")));
    }
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    if (limit && *limit > 100) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("limit is required.")));
    }
    if (limit && *limit < 0) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("limit is required.")));
    }
    if (urlExpireSec && *urlExpireSec > 14400) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("urlExpireSec is required.")));
    }
    if (urlExpireSec && *urlExpireSec < 10) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("urlExpireSec is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (Starred) {
      res["Starred"] = boost::any(*Starred);
    }
    if (category) {
      res["category"] = boost::any(*category);
    }
    if (customIndexKey) {
      res["custom_index_key"] = boost::any(*customIndexKey);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (encryptMode) {
      res["encrypt_mode"] = boost::any(*encryptMode);
    }
    if (fields) {
      res["fields"] = boost::any(*fields);
    }
    if (imageThumbnailProcess) {
      res["image_thumbnail_process"] = boost::any(*imageThumbnailProcess);
    }
    if (imageUrlProcess) {
      res["image_url_process"] = boost::any(*imageUrlProcess);
    }
    if (limit) {
      res["limit"] = boost::any(*limit);
    }
    if (marker) {
      res["marker"] = boost::any(*marker);
    }
    if (orderDirection) {
      res["order_direction"] = boost::any(*orderDirection);
    }
    if (status) {
      res["status"] = boost::any(*status);
    }
    if (type) {
      res["type"] = boost::any(*type);
    }
    if (urlExpireSec) {
      res["url_expire_sec"] = boost::any(*urlExpireSec);
    }
    if (videoThumbnailProcess) {
      res["video_thumbnail_process"] = boost::any(*videoThumbnailProcess);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("Starred") != m.end() && !m["Starred"].empty()) {
      Starred = make_shared<bool>(boost::any_cast<bool>(m["Starred"]));
    }
    if (m.find("category") != m.end() && !m["category"].empty()) {
      category = make_shared<string>(boost::any_cast<string>(m["category"]));
    }
    if (m.find("custom_index_key") != m.end() && !m["custom_index_key"].empty()) {
      customIndexKey = make_shared<string>(boost::any_cast<string>(m["custom_index_key"]));
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("encrypt_mode") != m.end() && !m["encrypt_mode"].empty()) {
      encryptMode = make_shared<string>(boost::any_cast<string>(m["encrypt_mode"]));
    }
    if (m.find("fields") != m.end() && !m["fields"].empty()) {
      fields = make_shared<string>(boost::any_cast<string>(m["fields"]));
    }
    if (m.find("image_thumbnail_process") != m.end() && !m["image_thumbnail_process"].empty()) {
      imageThumbnailProcess = make_shared<string>(boost::any_cast<string>(m["image_thumbnail_process"]));
    }
    if (m.find("image_url_process") != m.end() && !m["image_url_process"].empty()) {
      imageUrlProcess = make_shared<string>(boost::any_cast<string>(m["image_url_process"]));
    }
    if (m.find("limit") != m.end() && !m["limit"].empty()) {
      limit = make_shared<long>(boost::any_cast<long>(m["limit"]));
    }
    if (m.find("marker") != m.end() && !m["marker"].empty()) {
      marker = make_shared<string>(boost::any_cast<string>(m["marker"]));
    }
    if (m.find("order_direction") != m.end() && !m["order_direction"].empty()) {
      orderDirection = make_shared<string>(boost::any_cast<string>(m["order_direction"]));
    }
    if (m.find("status") != m.end() && !m["status"].empty()) {
      status = make_shared<string>(boost::any_cast<string>(m["status"]));
    }
    if (m.find("type") != m.end() && !m["type"].empty()) {
      type = make_shared<string>(boost::any_cast<string>(m["type"]));
    }
    if (m.find("url_expire_sec") != m.end() && !m["url_expire_sec"].empty()) {
      urlExpireSec = make_shared<long>(boost::any_cast<long>(m["url_expire_sec"]));
    }
    if (m.find("video_thumbnail_process") != m.end() && !m["video_thumbnail_process"].empty()) {
      videoThumbnailProcess = make_shared<string>(boost::any_cast<string>(m["video_thumbnail_process"]));
    }
  }


  ~ListFileByCustomIndexKeyRequest() = default;
};
class ListFileDeltaRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<string> cursor{};
  shared_ptr<string> driveId{};
  shared_ptr<long> limit{};

  ListFileDeltaRequest() {}

  explicit ListFileDeltaRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!driveId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("driveId is required.")));
    }
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (cursor) {
      res["cursor"] = boost::any(*cursor);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (limit) {
      res["limit"] = boost::any(*limit);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("cursor") != m.end() && !m["cursor"].empty()) {
      cursor = make_shared<string>(boost::any_cast<string>(m["cursor"]));
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("limit") != m.end() && !m["limit"].empty()) {
      limit = make_shared<long>(boost::any_cast<long>(m["limit"]));
    }
  }


  ~ListFileDeltaRequest() = default;
};
class ListFileRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<bool> Starred{};
  shared_ptr<bool> all{};
  shared_ptr<string> category{};
  shared_ptr<string> driveId{};
  shared_ptr<string> fields{};
  shared_ptr<string> imageThumbnailProcess{};
  shared_ptr<string> imageUrlProcess{};
  shared_ptr<long> limit{};
  shared_ptr<string> marker{};
  shared_ptr<string> orderBy{};
  shared_ptr<string> orderDirection{};
  shared_ptr<string> parentFileId{};
  shared_ptr<string> status{};
  shared_ptr<string> type{};
  shared_ptr<long> urlExpireSec{};
  shared_ptr<string> videoThumbnailProcess{};

  ListFileRequest() {}

  explicit ListFileRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    if (limit && *limit > 100) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("limit is required.")));
    }
    if (limit && *limit < 0) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("limit is required.")));
    }
    if (!parentFileId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("parentFileId is required.")));
    }
    Darabonba::Model::validateMaxLength("parentFileId", parentFileId, 50);
    Darabonba::Model::validateMinLength("parentFileId", parentFileId, 4);
    Darabonba::Model::validatePattern("parentFileId", parentFileId, "[a-z0-9.-_]{1,50}");
    if (urlExpireSec && *urlExpireSec > 14400) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("urlExpireSec is required.")));
    }
    if (urlExpireSec && *urlExpireSec < 10) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("urlExpireSec is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (Starred) {
      res["Starred"] = boost::any(*Starred);
    }
    if (all) {
      res["all"] = boost::any(*all);
    }
    if (category) {
      res["category"] = boost::any(*category);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (fields) {
      res["fields"] = boost::any(*fields);
    }
    if (imageThumbnailProcess) {
      res["image_thumbnail_process"] = boost::any(*imageThumbnailProcess);
    }
    if (imageUrlProcess) {
      res["image_url_process"] = boost::any(*imageUrlProcess);
    }
    if (limit) {
      res["limit"] = boost::any(*limit);
    }
    if (marker) {
      res["marker"] = boost::any(*marker);
    }
    if (orderBy) {
      res["order_by"] = boost::any(*orderBy);
    }
    if (orderDirection) {
      res["order_direction"] = boost::any(*orderDirection);
    }
    if (parentFileId) {
      res["parent_file_id"] = boost::any(*parentFileId);
    }
    if (status) {
      res["status"] = boost::any(*status);
    }
    if (type) {
      res["type"] = boost::any(*type);
    }
    if (urlExpireSec) {
      res["url_expire_sec"] = boost::any(*urlExpireSec);
    }
    if (videoThumbnailProcess) {
      res["video_thumbnail_process"] = boost::any(*videoThumbnailProcess);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("Starred") != m.end() && !m["Starred"].empty()) {
      Starred = make_shared<bool>(boost::any_cast<bool>(m["Starred"]));
    }
    if (m.find("all") != m.end() && !m["all"].empty()) {
      all = make_shared<bool>(boost::any_cast<bool>(m["all"]));
    }
    if (m.find("category") != m.end() && !m["category"].empty()) {
      category = make_shared<string>(boost::any_cast<string>(m["category"]));
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("fields") != m.end() && !m["fields"].empty()) {
      fields = make_shared<string>(boost::any_cast<string>(m["fields"]));
    }
    if (m.find("image_thumbnail_process") != m.end() && !m["image_thumbnail_process"].empty()) {
      imageThumbnailProcess = make_shared<string>(boost::any_cast<string>(m["image_thumbnail_process"]));
    }
    if (m.find("image_url_process") != m.end() && !m["image_url_process"].empty()) {
      imageUrlProcess = make_shared<string>(boost::any_cast<string>(m["image_url_process"]));
    }
    if (m.find("limit") != m.end() && !m["limit"].empty()) {
      limit = make_shared<long>(boost::any_cast<long>(m["limit"]));
    }
    if (m.find("marker") != m.end() && !m["marker"].empty()) {
      marker = make_shared<string>(boost::any_cast<string>(m["marker"]));
    }
    if (m.find("order_by") != m.end() && !m["order_by"].empty()) {
      orderBy = make_shared<string>(boost::any_cast<string>(m["order_by"]));
    }
    if (m.find("order_direction") != m.end() && !m["order_direction"].empty()) {
      orderDirection = make_shared<string>(boost::any_cast<string>(m["order_direction"]));
    }
    if (m.find("parent_file_id") != m.end() && !m["parent_file_id"].empty()) {
      parentFileId = make_shared<string>(boost::any_cast<string>(m["parent_file_id"]));
    }
    if (m.find("status") != m.end() && !m["status"].empty()) {
      status = make_shared<string>(boost::any_cast<string>(m["status"]));
    }
    if (m.find("type") != m.end() && !m["type"].empty()) {
      type = make_shared<string>(boost::any_cast<string>(m["type"]));
    }
    if (m.find("url_expire_sec") != m.end() && !m["url_expire_sec"].empty()) {
      urlExpireSec = make_shared<long>(boost::any_cast<long>(m["url_expire_sec"]));
    }
    if (m.find("video_thumbnail_process") != m.end() && !m["video_thumbnail_process"].empty()) {
      videoThumbnailProcess = make_shared<string>(boost::any_cast<string>(m["video_thumbnail_process"]));
    }
  }


  ~ListFileRequest() = default;
};
class ListMyDriveRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<long> limit{};
  shared_ptr<string> marker{};

  ListMyDriveRequest() {}

  explicit ListMyDriveRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (limit && *limit > 100) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("limit is required.")));
    }
    if (limit && *limit < 1) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("limit is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (limit) {
      res["limit"] = boost::any(*limit);
    }
    if (marker) {
      res["marker"] = boost::any(*marker);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("limit") != m.end() && !m["limit"].empty()) {
      limit = make_shared<long>(boost::any_cast<long>(m["limit"]));
    }
    if (m.find("marker") != m.end() && !m["marker"].empty()) {
      marker = make_shared<string>(boost::any_cast<string>(m["marker"]));
    }
  }


  ~ListMyDriveRequest() = default;
};
class ListShareLinkRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<string> creator{};
  shared_ptr<long> limit{};
  shared_ptr<string> marker{};

  ListShareLinkRequest() {}

  explicit ListShareLinkRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (limit && *limit > 100) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("limit is required.")));
    }
    if (limit && *limit < 1) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("limit is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (creator) {
      res["creator"] = boost::any(*creator);
    }
    if (limit) {
      res["limit"] = boost::any(*limit);
    }
    if (marker) {
      res["marker"] = boost::any(*marker);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("creator") != m.end() && !m["creator"].empty()) {
      creator = make_shared<string>(boost::any_cast<string>(m["creator"]));
    }
    if (m.find("limit") != m.end() && !m["limit"].empty()) {
      limit = make_shared<long>(boost::any_cast<long>(m["limit"]));
    }
    if (m.find("marker") != m.end() && !m["marker"].empty()) {
      marker = make_shared<string>(boost::any_cast<string>(m["marker"]));
    }
  }


  ~ListShareLinkRequest() = default;
};
class ListShareRequest : public Darabonba::Model {
public:
  shared_ptr<string> creator{};
  shared_ptr<string> driveId{};
  shared_ptr<long> limit{};
  shared_ptr<string> marker{};
  shared_ptr<string> owner{};
  shared_ptr<string> shareFilePath{};

  ListShareRequest() {}

  explicit ListShareRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    if (limit && *limit > 100) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("limit is required.")));
    }
    if (limit && *limit < 1) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("limit is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (creator) {
      res["creator"] = boost::any(*creator);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (limit) {
      res["limit"] = boost::any(*limit);
    }
    if (marker) {
      res["marker"] = boost::any(*marker);
    }
    if (owner) {
      res["owner"] = boost::any(*owner);
    }
    if (shareFilePath) {
      res["share_file_path"] = boost::any(*shareFilePath);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("creator") != m.end() && !m["creator"].empty()) {
      creator = make_shared<string>(boost::any_cast<string>(m["creator"]));
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("limit") != m.end() && !m["limit"].empty()) {
      limit = make_shared<long>(boost::any_cast<long>(m["limit"]));
    }
    if (m.find("marker") != m.end() && !m["marker"].empty()) {
      marker = make_shared<string>(boost::any_cast<string>(m["marker"]));
    }
    if (m.find("owner") != m.end() && !m["owner"].empty()) {
      owner = make_shared<string>(boost::any_cast<string>(m["owner"]));
    }
    if (m.find("share_file_path") != m.end() && !m["share_file_path"].empty()) {
      shareFilePath = make_shared<string>(boost::any_cast<string>(m["share_file_path"]));
    }
  }


  ~ListShareRequest() = default;
};
class ListStoreFileRequest : public Darabonba::Model {
public:
  shared_ptr<long> limit{};
  shared_ptr<string> marker{};
  shared_ptr<string> parentFilePath{};
  shared_ptr<string> storeId{};
  shared_ptr<string> type{};

  ListStoreFileRequest() {}

  explicit ListStoreFileRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (limit && *limit > 1000) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("limit is required.")));
    }
    if (limit && *limit < 1) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("limit is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (limit) {
      res["limit"] = boost::any(*limit);
    }
    if (marker) {
      res["marker"] = boost::any(*marker);
    }
    if (parentFilePath) {
      res["parent_file_path"] = boost::any(*parentFilePath);
    }
    if (storeId) {
      res["store_id"] = boost::any(*storeId);
    }
    if (type) {
      res["type"] = boost::any(*type);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("limit") != m.end() && !m["limit"].empty()) {
      limit = make_shared<long>(boost::any_cast<long>(m["limit"]));
    }
    if (m.find("marker") != m.end() && !m["marker"].empty()) {
      marker = make_shared<string>(boost::any_cast<string>(m["marker"]));
    }
    if (m.find("parent_file_path") != m.end() && !m["parent_file_path"].empty()) {
      parentFilePath = make_shared<string>(boost::any_cast<string>(m["parent_file_path"]));
    }
    if (m.find("store_id") != m.end() && !m["store_id"].empty()) {
      storeId = make_shared<string>(boost::any_cast<string>(m["store_id"]));
    }
    if (m.find("type") != m.end() && !m["type"].empty()) {
      type = make_shared<string>(boost::any_cast<string>(m["type"]));
    }
  }


  ~ListStoreFileRequest() = default;
};
class ListStoreRequest : public Darabonba::Model {
public:
  shared_ptr<string> domainId{};

  ListStoreRequest() {}

  explicit ListStoreRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (domainId) {
      res["domain_id"] = boost::any(*domainId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("domain_id") != m.end() && !m["domain_id"].empty()) {
      domainId = make_shared<string>(boost::any_cast<string>(m["domain_id"]));
    }
  }


  ~ListStoreRequest() = default;
};
class ListUploadedPartRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<string> driveId{};
  shared_ptr<string> fileId{};
  shared_ptr<long> limit{};
  shared_ptr<long> partNumberMarker{};
  shared_ptr<string> uploadId{};

  ListUploadedPartRequest() {}

  explicit ListUploadedPartRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!driveId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("driveId is required.")));
    }
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    if (!fileId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("fileId is required.")));
    }
    Darabonba::Model::validateMaxLength("fileId", fileId, 50);
    Darabonba::Model::validateMinLength("fileId", fileId, 40);
    Darabonba::Model::validatePattern("fileId", fileId, "[a-z0-9.-_]{1,50}");
    if (limit && *limit > 1000) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("limit is required.")));
    }
    if (limit && *limit < 1) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("limit is required.")));
    }
    if (partNumberMarker && *partNumberMarker < 1) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("partNumberMarker is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (fileId) {
      res["file_id"] = boost::any(*fileId);
    }
    if (limit) {
      res["limit"] = boost::any(*limit);
    }
    if (partNumberMarker) {
      res["part_number_marker"] = boost::any(*partNumberMarker);
    }
    if (uploadId) {
      res["upload_id"] = boost::any(*uploadId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("file_id") != m.end() && !m["file_id"].empty()) {
      fileId = make_shared<string>(boost::any_cast<string>(m["file_id"]));
    }
    if (m.find("limit") != m.end() && !m["limit"].empty()) {
      limit = make_shared<long>(boost::any_cast<long>(m["limit"]));
    }
    if (m.find("part_number_marker") != m.end() && !m["part_number_marker"].empty()) {
      partNumberMarker = make_shared<long>(boost::any_cast<long>(m["part_number_marker"]));
    }
    if (m.find("upload_id") != m.end() && !m["upload_id"].empty()) {
      uploadId = make_shared<string>(boost::any_cast<string>(m["upload_id"]));
    }
  }


  ~ListUploadedPartRequest() = default;
};
class MoveFileRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<string> driveId{};
  shared_ptr<string> fileId{};
  shared_ptr<string> newName{};
  shared_ptr<bool> overwrite{};
  shared_ptr<string> toParentFileId{};

  MoveFileRequest() {}

  explicit MoveFileRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!driveId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("driveId is required.")));
    }
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    if (!fileId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("fileId is required.")));
    }
    Darabonba::Model::validateMaxLength("fileId", fileId, 50);
    Darabonba::Model::validateMinLength("fileId", fileId, 40);
    Darabonba::Model::validatePattern("fileId", fileId, "[a-z0-9.-_]{1,50}");
    Darabonba::Model::validateMaxLength("newName", newName, 1024);
    Darabonba::Model::validateMinLength("newName", newName, 1);
    if (!toParentFileId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("toParentFileId is required.")));
    }
    Darabonba::Model::validateMaxLength("toParentFileId", toParentFileId, 50);
    Darabonba::Model::validateMinLength("toParentFileId", toParentFileId, 4);
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (fileId) {
      res["file_id"] = boost::any(*fileId);
    }
    if (newName) {
      res["new_name"] = boost::any(*newName);
    }
    if (overwrite) {
      res["overwrite"] = boost::any(*overwrite);
    }
    if (toParentFileId) {
      res["to_parent_file_id"] = boost::any(*toParentFileId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("file_id") != m.end() && !m["file_id"].empty()) {
      fileId = make_shared<string>(boost::any_cast<string>(m["file_id"]));
    }
    if (m.find("new_name") != m.end() && !m["new_name"].empty()) {
      newName = make_shared<string>(boost::any_cast<string>(m["new_name"]));
    }
    if (m.find("overwrite") != m.end() && !m["overwrite"].empty()) {
      overwrite = make_shared<bool>(boost::any_cast<bool>(m["overwrite"]));
    }
    if (m.find("to_parent_file_id") != m.end() && !m["to_parent_file_id"].empty()) {
      toParentFileId = make_shared<string>(boost::any_cast<string>(m["to_parent_file_id"]));
    }
  }


  ~MoveFileRequest() = default;
};
class OSSCompleteFileRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, boost::any>> additionData{};
  shared_ptr<string> driveId{};
  shared_ptr<string> filePath{};
  shared_ptr<bool> forbidOverwrite{};
  shared_ptr<vector<UploadPartInfo>> partInfoList{};
  shared_ptr<string> shareId{};
  shared_ptr<string> uploadId{};

  OSSCompleteFileRequest() {}

  explicit OSSCompleteFileRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (additionData) {
      res["addition_data"] = boost::any(*additionData);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (filePath) {
      res["file_path"] = boost::any(*filePath);
    }
    if (forbidOverwrite) {
      res["forbid_overwrite"] = boost::any(*forbidOverwrite);
    }
    if (partInfoList) {
      vector<boost::any> temp1;
      for(auto item1:*partInfoList){
        temp1.push_back(boost::any(item1.toMap()));
      }
      res["part_info_list"] = boost::any(temp1);
    }
    if (shareId) {
      res["share_id"] = boost::any(*shareId);
    }
    if (uploadId) {
      res["upload_id"] = boost::any(*uploadId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("addition_data") != m.end() && !m["addition_data"].empty()) {
      map<string, boost::any> map1 = boost::any_cast<map<string, boost::any>>(m["addition_data"]);
      map<string, boost::any> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      additionData = make_shared<map<string, boost::any>>(toMap1);
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("file_path") != m.end() && !m["file_path"].empty()) {
      filePath = make_shared<string>(boost::any_cast<string>(m["file_path"]));
    }
    if (m.find("forbid_overwrite") != m.end() && !m["forbid_overwrite"].empty()) {
      forbidOverwrite = make_shared<bool>(boost::any_cast<bool>(m["forbid_overwrite"]));
    }
    if (m.find("part_info_list") != m.end() && !m["part_info_list"].empty()) {
      if (typeid(vector<boost::any>).name() == m["part_info_list"].type().name()) {
        vector<UploadPartInfo> expect1;
        for(auto item1:boost::any_cast<vector<boost::any>>(m["part_info_list"])){
          if (typeid(map<string, boost::any>).name() == item1.type().name()) {
            UploadPartInfo model2;
            model2.fromMap(boost::any_cast<map<string, boost::any>>(item1));
            expect1.push_back(model2);
          }
        }
        partInfoList = make_shared<vector<UploadPartInfo>>(expect1);
      }
    }
    if (m.find("share_id") != m.end() && !m["share_id"].empty()) {
      shareId = make_shared<string>(boost::any_cast<string>(m["share_id"]));
    }
    if (m.find("upload_id") != m.end() && !m["upload_id"].empty()) {
      uploadId = make_shared<string>(boost::any_cast<string>(m["upload_id"]));
    }
  }


  ~OSSCompleteFileRequest() = default;
};
class OSSCopyFileRequest : public Darabonba::Model {
public:
  shared_ptr<string> driveId{};
  shared_ptr<string> filePath{};
  shared_ptr<string> newName{};
  shared_ptr<bool> overwrite{};
  shared_ptr<string> shareId{};
  shared_ptr<string> toDriveId{};
  shared_ptr<string> toParentFilePath{};
  shared_ptr<string> toShareId{};

  OSSCopyFileRequest() {}

  explicit OSSCopyFileRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    if (!filePath) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("filePath is required.")));
    }
    Darabonba::Model::validatePattern("newName", newName, "[a-zA-Z0-9.-]{1,1000}");
    Darabonba::Model::validatePattern("shareId", shareId, "[0-9a-zA-Z-]+");
    Darabonba::Model::validatePattern("toDriveId", toDriveId, "[0-9]+");
    if (!toParentFilePath) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("toParentFilePath is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (filePath) {
      res["file_path"] = boost::any(*filePath);
    }
    if (newName) {
      res["new_name"] = boost::any(*newName);
    }
    if (overwrite) {
      res["overwrite"] = boost::any(*overwrite);
    }
    if (shareId) {
      res["share_id"] = boost::any(*shareId);
    }
    if (toDriveId) {
      res["to_drive_id"] = boost::any(*toDriveId);
    }
    if (toParentFilePath) {
      res["to_parent_file_path"] = boost::any(*toParentFilePath);
    }
    if (toShareId) {
      res["to_share_id"] = boost::any(*toShareId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("file_path") != m.end() && !m["file_path"].empty()) {
      filePath = make_shared<string>(boost::any_cast<string>(m["file_path"]));
    }
    if (m.find("new_name") != m.end() && !m["new_name"].empty()) {
      newName = make_shared<string>(boost::any_cast<string>(m["new_name"]));
    }
    if (m.find("overwrite") != m.end() && !m["overwrite"].empty()) {
      overwrite = make_shared<bool>(boost::any_cast<bool>(m["overwrite"]));
    }
    if (m.find("share_id") != m.end() && !m["share_id"].empty()) {
      shareId = make_shared<string>(boost::any_cast<string>(m["share_id"]));
    }
    if (m.find("to_drive_id") != m.end() && !m["to_drive_id"].empty()) {
      toDriveId = make_shared<string>(boost::any_cast<string>(m["to_drive_id"]));
    }
    if (m.find("to_parent_file_path") != m.end() && !m["to_parent_file_path"].empty()) {
      toParentFilePath = make_shared<string>(boost::any_cast<string>(m["to_parent_file_path"]));
    }
    if (m.find("to_share_id") != m.end() && !m["to_share_id"].empty()) {
      toShareId = make_shared<string>(boost::any_cast<string>(m["to_share_id"]));
    }
  }


  ~OSSCopyFileRequest() = default;
};
class OSSCreateFileRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, boost::any>> additionData{};
  shared_ptr<string> contentMd5{};
  shared_ptr<string> contentType{};
  shared_ptr<string> driveId{};
  shared_ptr<bool> forbidOverwrite{};
  shared_ptr<string> name{};
  shared_ptr<string> parentFilePath{};
  shared_ptr<vector<UploadPartInfo>> partInfoList{};
  shared_ptr<string> shareId{};
  shared_ptr<long> size{};
  shared_ptr<string> type{};

  OSSCreateFileRequest() {}

  explicit OSSCreateFileRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    if (!name) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("name is required.")));
    }
    Darabonba::Model::validateMaxLength("name", name, 1024);
    Darabonba::Model::validateMinLength("name", name, 1);
    if (!parentFilePath) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("parentFilePath is required.")));
    }
    Darabonba::Model::validatePattern("shareId", shareId, "[0-9a-zA-Z-]+");
    if (size && *size > 53687091200) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("size is required.")));
    }
    if (size && *size < 0) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("size is required.")));
    }
    if (!type) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("type is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (additionData) {
      res["addition_data"] = boost::any(*additionData);
    }
    if (contentMd5) {
      res["content_md5"] = boost::any(*contentMd5);
    }
    if (contentType) {
      res["content_type"] = boost::any(*contentType);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (forbidOverwrite) {
      res["forbid_overwrite"] = boost::any(*forbidOverwrite);
    }
    if (name) {
      res["name"] = boost::any(*name);
    }
    if (parentFilePath) {
      res["parent_file_path"] = boost::any(*parentFilePath);
    }
    if (partInfoList) {
      vector<boost::any> temp1;
      for(auto item1:*partInfoList){
        temp1.push_back(boost::any(item1.toMap()));
      }
      res["part_info_list"] = boost::any(temp1);
    }
    if (shareId) {
      res["share_id"] = boost::any(*shareId);
    }
    if (size) {
      res["size"] = boost::any(*size);
    }
    if (type) {
      res["type"] = boost::any(*type);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("addition_data") != m.end() && !m["addition_data"].empty()) {
      map<string, boost::any> map1 = boost::any_cast<map<string, boost::any>>(m["addition_data"]);
      map<string, boost::any> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      additionData = make_shared<map<string, boost::any>>(toMap1);
    }
    if (m.find("content_md5") != m.end() && !m["content_md5"].empty()) {
      contentMd5 = make_shared<string>(boost::any_cast<string>(m["content_md5"]));
    }
    if (m.find("content_type") != m.end() && !m["content_type"].empty()) {
      contentType = make_shared<string>(boost::any_cast<string>(m["content_type"]));
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("forbid_overwrite") != m.end() && !m["forbid_overwrite"].empty()) {
      forbidOverwrite = make_shared<bool>(boost::any_cast<bool>(m["forbid_overwrite"]));
    }
    if (m.find("name") != m.end() && !m["name"].empty()) {
      name = make_shared<string>(boost::any_cast<string>(m["name"]));
    }
    if (m.find("parent_file_path") != m.end() && !m["parent_file_path"].empty()) {
      parentFilePath = make_shared<string>(boost::any_cast<string>(m["parent_file_path"]));
    }
    if (m.find("part_info_list") != m.end() && !m["part_info_list"].empty()) {
      if (typeid(vector<boost::any>).name() == m["part_info_list"].type().name()) {
        vector<UploadPartInfo> expect1;
        for(auto item1:boost::any_cast<vector<boost::any>>(m["part_info_list"])){
          if (typeid(map<string, boost::any>).name() == item1.type().name()) {
            UploadPartInfo model2;
            model2.fromMap(boost::any_cast<map<string, boost::any>>(item1));
            expect1.push_back(model2);
          }
        }
        partInfoList = make_shared<vector<UploadPartInfo>>(expect1);
      }
    }
    if (m.find("share_id") != m.end() && !m["share_id"].empty()) {
      shareId = make_shared<string>(boost::any_cast<string>(m["share_id"]));
    }
    if (m.find("size") != m.end() && !m["size"].empty()) {
      size = make_shared<long>(boost::any_cast<long>(m["size"]));
    }
    if (m.find("type") != m.end() && !m["type"].empty()) {
      type = make_shared<string>(boost::any_cast<string>(m["type"]));
    }
  }


  ~OSSCreateFileRequest() = default;
};
class OSSDeleteFileRequest : public Darabonba::Model {
public:
  shared_ptr<string> driveId{};
  shared_ptr<string> filePath{};
  shared_ptr<bool> permanently{};
  shared_ptr<string> shareId{};

  OSSDeleteFileRequest() {}

  explicit OSSDeleteFileRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    if (!filePath) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("filePath is required.")));
    }
    Darabonba::Model::validateMaxLength("filePath", filePath, 1000);
    Darabonba::Model::validateMinLength("filePath", filePath, 1);
    Darabonba::Model::validatePattern("shareId", shareId, "[0-9a-zA-Z-]+");
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (filePath) {
      res["file_path"] = boost::any(*filePath);
    }
    if (permanently) {
      res["permanently"] = boost::any(*permanently);
    }
    if (shareId) {
      res["share_id"] = boost::any(*shareId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("file_path") != m.end() && !m["file_path"].empty()) {
      filePath = make_shared<string>(boost::any_cast<string>(m["file_path"]));
    }
    if (m.find("permanently") != m.end() && !m["permanently"].empty()) {
      permanently = make_shared<bool>(boost::any_cast<bool>(m["permanently"]));
    }
    if (m.find("share_id") != m.end() && !m["share_id"].empty()) {
      shareId = make_shared<string>(boost::any_cast<string>(m["share_id"]));
    }
  }


  ~OSSDeleteFileRequest() = default;
};
class OSSGetDownloadUrlRequest : public Darabonba::Model {
public:
  shared_ptr<string> driveId{};
  shared_ptr<long> expireSec{};
  shared_ptr<string> fileName{};
  shared_ptr<string> filePath{};
  shared_ptr<string> shareId{};

  OSSGetDownloadUrlRequest() {}

  explicit OSSGetDownloadUrlRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    if (expireSec && *expireSec > 14400) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("expireSec is required.")));
    }
    if (expireSec && *expireSec < 10) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("expireSec is required.")));
    }
    if (!filePath) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("filePath is required.")));
    }
    Darabonba::Model::validateMaxLength("filePath", filePath, 1000);
    Darabonba::Model::validateMinLength("filePath", filePath, 1);
    Darabonba::Model::validatePattern("shareId", shareId, "[0-9a-zA-Z-]+");
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (expireSec) {
      res["expire_sec"] = boost::any(*expireSec);
    }
    if (fileName) {
      res["file_name"] = boost::any(*fileName);
    }
    if (filePath) {
      res["file_path"] = boost::any(*filePath);
    }
    if (shareId) {
      res["share_id"] = boost::any(*shareId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("expire_sec") != m.end() && !m["expire_sec"].empty()) {
      expireSec = make_shared<long>(boost::any_cast<long>(m["expire_sec"]));
    }
    if (m.find("file_name") != m.end() && !m["file_name"].empty()) {
      fileName = make_shared<string>(boost::any_cast<string>(m["file_name"]));
    }
    if (m.find("file_path") != m.end() && !m["file_path"].empty()) {
      filePath = make_shared<string>(boost::any_cast<string>(m["file_path"]));
    }
    if (m.find("share_id") != m.end() && !m["share_id"].empty()) {
      shareId = make_shared<string>(boost::any_cast<string>(m["share_id"]));
    }
  }


  ~OSSGetDownloadUrlRequest() = default;
};
class OSSGetFileRequest : public Darabonba::Model {
public:
  shared_ptr<string> driveId{};
  shared_ptr<string> filePath{};
  shared_ptr<string> imageThumbnailProcess{};
  shared_ptr<string> imageUrlProcess{};
  shared_ptr<string> shareId{};
  shared_ptr<long> urlExpireSec{};

  OSSGetFileRequest() {}

  explicit OSSGetFileRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    if (!filePath) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("filePath is required.")));
    }
    Darabonba::Model::validateMaxLength("filePath", filePath, 1000);
    Darabonba::Model::validateMinLength("filePath", filePath, 1);
    Darabonba::Model::validatePattern("shareId", shareId, "[0-9a-zA-Z-]+");
    if (urlExpireSec && *urlExpireSec > 14400) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("urlExpireSec is required.")));
    }
    if (urlExpireSec && *urlExpireSec < 10) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("urlExpireSec is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (filePath) {
      res["file_path"] = boost::any(*filePath);
    }
    if (imageThumbnailProcess) {
      res["image_thumbnail_process"] = boost::any(*imageThumbnailProcess);
    }
    if (imageUrlProcess) {
      res["image_url_process"] = boost::any(*imageUrlProcess);
    }
    if (shareId) {
      res["share_id"] = boost::any(*shareId);
    }
    if (urlExpireSec) {
      res["url_expire_sec"] = boost::any(*urlExpireSec);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("file_path") != m.end() && !m["file_path"].empty()) {
      filePath = make_shared<string>(boost::any_cast<string>(m["file_path"]));
    }
    if (m.find("image_thumbnail_process") != m.end() && !m["image_thumbnail_process"].empty()) {
      imageThumbnailProcess = make_shared<string>(boost::any_cast<string>(m["image_thumbnail_process"]));
    }
    if (m.find("image_url_process") != m.end() && !m["image_url_process"].empty()) {
      imageUrlProcess = make_shared<string>(boost::any_cast<string>(m["image_url_process"]));
    }
    if (m.find("share_id") != m.end() && !m["share_id"].empty()) {
      shareId = make_shared<string>(boost::any_cast<string>(m["share_id"]));
    }
    if (m.find("url_expire_sec") != m.end() && !m["url_expire_sec"].empty()) {
      urlExpireSec = make_shared<long>(boost::any_cast<long>(m["url_expire_sec"]));
    }
  }


  ~OSSGetFileRequest() = default;
};
class OSSGetSecureUrlRequest : public Darabonba::Model {
public:
  shared_ptr<string> driveId{};
  shared_ptr<long> expireSec{};
  shared_ptr<string> filePath{};
  shared_ptr<string> secureIp{};
  shared_ptr<string> shareId{};

  OSSGetSecureUrlRequest() {}

  explicit OSSGetSecureUrlRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    if (!filePath) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("filePath is required.")));
    }
    Darabonba::Model::validateMaxLength("filePath", filePath, 1000);
    Darabonba::Model::validateMinLength("filePath", filePath, 1);
    Darabonba::Model::validatePattern("shareId", shareId, "[0-9a-zA-Z-]+");
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (expireSec) {
      res["expire_sec"] = boost::any(*expireSec);
    }
    if (filePath) {
      res["file_path"] = boost::any(*filePath);
    }
    if (secureIp) {
      res["secure_ip"] = boost::any(*secureIp);
    }
    if (shareId) {
      res["share_id"] = boost::any(*shareId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("expire_sec") != m.end() && !m["expire_sec"].empty()) {
      expireSec = make_shared<long>(boost::any_cast<long>(m["expire_sec"]));
    }
    if (m.find("file_path") != m.end() && !m["file_path"].empty()) {
      filePath = make_shared<string>(boost::any_cast<string>(m["file_path"]));
    }
    if (m.find("secure_ip") != m.end() && !m["secure_ip"].empty()) {
      secureIp = make_shared<string>(boost::any_cast<string>(m["secure_ip"]));
    }
    if (m.find("share_id") != m.end() && !m["share_id"].empty()) {
      shareId = make_shared<string>(boost::any_cast<string>(m["share_id"]));
    }
  }


  ~OSSGetSecureUrlRequest() = default;
};
class OSSGetUploadUrlRequest : public Darabonba::Model {
public:
  shared_ptr<string> contentMd5{};
  shared_ptr<string> driveId{};
  shared_ptr<string> filePath{};
  shared_ptr<vector<UploadPartInfo>> partInfoList{};
  shared_ptr<string> shareId{};
  shared_ptr<string> uploadId{};

  OSSGetUploadUrlRequest() {}

  explicit OSSGetUploadUrlRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    Darabonba::Model::validateMaxLength("contentMd5", contentMd5, 32);
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    if (!filePath) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("filePath is required.")));
    }
    Darabonba::Model::validatePattern("shareId", shareId, "[0-9a-zA-Z-]+");
    if (!uploadId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("uploadId is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (contentMd5) {
      res["content_md5"] = boost::any(*contentMd5);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (filePath) {
      res["file_path"] = boost::any(*filePath);
    }
    if (partInfoList) {
      vector<boost::any> temp1;
      for(auto item1:*partInfoList){
        temp1.push_back(boost::any(item1.toMap()));
      }
      res["part_info_list"] = boost::any(temp1);
    }
    if (shareId) {
      res["share_id"] = boost::any(*shareId);
    }
    if (uploadId) {
      res["upload_id"] = boost::any(*uploadId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("content_md5") != m.end() && !m["content_md5"].empty()) {
      contentMd5 = make_shared<string>(boost::any_cast<string>(m["content_md5"]));
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("file_path") != m.end() && !m["file_path"].empty()) {
      filePath = make_shared<string>(boost::any_cast<string>(m["file_path"]));
    }
    if (m.find("part_info_list") != m.end() && !m["part_info_list"].empty()) {
      if (typeid(vector<boost::any>).name() == m["part_info_list"].type().name()) {
        vector<UploadPartInfo> expect1;
        for(auto item1:boost::any_cast<vector<boost::any>>(m["part_info_list"])){
          if (typeid(map<string, boost::any>).name() == item1.type().name()) {
            UploadPartInfo model2;
            model2.fromMap(boost::any_cast<map<string, boost::any>>(item1));
            expect1.push_back(model2);
          }
        }
        partInfoList = make_shared<vector<UploadPartInfo>>(expect1);
      }
    }
    if (m.find("share_id") != m.end() && !m["share_id"].empty()) {
      shareId = make_shared<string>(boost::any_cast<string>(m["share_id"]));
    }
    if (m.find("upload_id") != m.end() && !m["upload_id"].empty()) {
      uploadId = make_shared<string>(boost::any_cast<string>(m["upload_id"]));
    }
  }


  ~OSSGetUploadUrlRequest() = default;
};
class OSSListFileRequest : public Darabonba::Model {
public:
  shared_ptr<string> driveId{};
  shared_ptr<string> imageThumbnailProcess{};
  shared_ptr<string> imageUrlProcess{};
  shared_ptr<long> limit{};
  shared_ptr<string> marker{};
  shared_ptr<string> parentFilePath{};
  shared_ptr<string> shareId{};
  shared_ptr<long> urlExpireSec{};
  shared_ptr<string> videoThumbnailProcess{};

  OSSListFileRequest() {}

  explicit OSSListFileRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    if (limit && *limit > 100) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("limit is required.")));
    }
    if (limit && *limit < 0) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("limit is required.")));
    }
    if (!parentFilePath) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("parentFilePath is required.")));
    }
    Darabonba::Model::validatePattern("shareId", shareId, "[0-9a-zA-Z-]+");
    if (urlExpireSec && *urlExpireSec > 14400) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("urlExpireSec is required.")));
    }
    if (urlExpireSec && *urlExpireSec < 10) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("urlExpireSec is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (imageThumbnailProcess) {
      res["image_thumbnail_process"] = boost::any(*imageThumbnailProcess);
    }
    if (imageUrlProcess) {
      res["image_url_process"] = boost::any(*imageUrlProcess);
    }
    if (limit) {
      res["limit"] = boost::any(*limit);
    }
    if (marker) {
      res["marker"] = boost::any(*marker);
    }
    if (parentFilePath) {
      res["parent_file_path"] = boost::any(*parentFilePath);
    }
    if (shareId) {
      res["share_id"] = boost::any(*shareId);
    }
    if (urlExpireSec) {
      res["url_expire_sec"] = boost::any(*urlExpireSec);
    }
    if (videoThumbnailProcess) {
      res["video_thumbnail_process"] = boost::any(*videoThumbnailProcess);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("image_thumbnail_process") != m.end() && !m["image_thumbnail_process"].empty()) {
      imageThumbnailProcess = make_shared<string>(boost::any_cast<string>(m["image_thumbnail_process"]));
    }
    if (m.find("image_url_process") != m.end() && !m["image_url_process"].empty()) {
      imageUrlProcess = make_shared<string>(boost::any_cast<string>(m["image_url_process"]));
    }
    if (m.find("limit") != m.end() && !m["limit"].empty()) {
      limit = make_shared<long>(boost::any_cast<long>(m["limit"]));
    }
    if (m.find("marker") != m.end() && !m["marker"].empty()) {
      marker = make_shared<string>(boost::any_cast<string>(m["marker"]));
    }
    if (m.find("parent_file_path") != m.end() && !m["parent_file_path"].empty()) {
      parentFilePath = make_shared<string>(boost::any_cast<string>(m["parent_file_path"]));
    }
    if (m.find("share_id") != m.end() && !m["share_id"].empty()) {
      shareId = make_shared<string>(boost::any_cast<string>(m["share_id"]));
    }
    if (m.find("url_expire_sec") != m.end() && !m["url_expire_sec"].empty()) {
      urlExpireSec = make_shared<long>(boost::any_cast<long>(m["url_expire_sec"]));
    }
    if (m.find("video_thumbnail_process") != m.end() && !m["video_thumbnail_process"].empty()) {
      videoThumbnailProcess = make_shared<string>(boost::any_cast<string>(m["video_thumbnail_process"]));
    }
  }


  ~OSSListFileRequest() = default;
};
class OSSListUploadedPartRequest : public Darabonba::Model {
public:
  shared_ptr<string> driveId{};
  shared_ptr<string> filePath{};
  shared_ptr<long> limit{};
  shared_ptr<long> partNumberMarker{};
  shared_ptr<string> shareId{};
  shared_ptr<string> uploadId{};

  OSSListUploadedPartRequest() {}

  explicit OSSListUploadedPartRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    if (!filePath) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("filePath is required.")));
    }
    if (limit && *limit > 1000) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("limit is required.")));
    }
    if (limit && *limit < 1) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("limit is required.")));
    }
    if (partNumberMarker && *partNumberMarker < 1) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("partNumberMarker is required.")));
    }
    Darabonba::Model::validatePattern("shareId", shareId, "[0-9a-zA-Z-]+");
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (filePath) {
      res["file_path"] = boost::any(*filePath);
    }
    if (limit) {
      res["limit"] = boost::any(*limit);
    }
    if (partNumberMarker) {
      res["part_number_marker"] = boost::any(*partNumberMarker);
    }
    if (shareId) {
      res["share_id"] = boost::any(*shareId);
    }
    if (uploadId) {
      res["upload_id"] = boost::any(*uploadId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("file_path") != m.end() && !m["file_path"].empty()) {
      filePath = make_shared<string>(boost::any_cast<string>(m["file_path"]));
    }
    if (m.find("limit") != m.end() && !m["limit"].empty()) {
      limit = make_shared<long>(boost::any_cast<long>(m["limit"]));
    }
    if (m.find("part_number_marker") != m.end() && !m["part_number_marker"].empty()) {
      partNumberMarker = make_shared<long>(boost::any_cast<long>(m["part_number_marker"]));
    }
    if (m.find("share_id") != m.end() && !m["share_id"].empty()) {
      shareId = make_shared<string>(boost::any_cast<string>(m["share_id"]));
    }
    if (m.find("upload_id") != m.end() && !m["upload_id"].empty()) {
      uploadId = make_shared<string>(boost::any_cast<string>(m["upload_id"]));
    }
  }


  ~OSSListUploadedPartRequest() = default;
};
class OSSMoveFileRequest : public Darabonba::Model {
public:
  shared_ptr<string> driveId{};
  shared_ptr<string> filePath{};
  shared_ptr<string> newName{};
  shared_ptr<bool> overwrite{};
  shared_ptr<string> shareId{};
  shared_ptr<string> toParentFilePath{};

  OSSMoveFileRequest() {}

  explicit OSSMoveFileRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    Darabonba::Model::validatePattern("shareId", shareId, "[0-9a-zA-Z-]+");
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (filePath) {
      res["file_path"] = boost::any(*filePath);
    }
    if (newName) {
      res["new_name"] = boost::any(*newName);
    }
    if (overwrite) {
      res["overwrite"] = boost::any(*overwrite);
    }
    if (shareId) {
      res["share_id"] = boost::any(*shareId);
    }
    if (toParentFilePath) {
      res["to_parent_file_path"] = boost::any(*toParentFilePath);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("file_path") != m.end() && !m["file_path"].empty()) {
      filePath = make_shared<string>(boost::any_cast<string>(m["file_path"]));
    }
    if (m.find("new_name") != m.end() && !m["new_name"].empty()) {
      newName = make_shared<string>(boost::any_cast<string>(m["new_name"]));
    }
    if (m.find("overwrite") != m.end() && !m["overwrite"].empty()) {
      overwrite = make_shared<bool>(boost::any_cast<bool>(m["overwrite"]));
    }
    if (m.find("share_id") != m.end() && !m["share_id"].empty()) {
      shareId = make_shared<string>(boost::any_cast<string>(m["share_id"]));
    }
    if (m.find("to_parent_file_path") != m.end() && !m["to_parent_file_path"].empty()) {
      toParentFilePath = make_shared<string>(boost::any_cast<string>(m["to_parent_file_path"]));
    }
  }


  ~OSSMoveFileRequest() = default;
};
class OSSVideoDRMLicenseRequest : public Darabonba::Model {
public:
  shared_ptr<string> drmType{};
  shared_ptr<string> licenseRequest{};

  OSSVideoDRMLicenseRequest() {}

  explicit OSSVideoDRMLicenseRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!drmType) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("drmType is required.")));
    }
    if (!licenseRequest) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("licenseRequest is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (drmType) {
      res["drmType"] = boost::any(*drmType);
    }
    if (licenseRequest) {
      res["licenseRequest"] = boost::any(*licenseRequest);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("drmType") != m.end() && !m["drmType"].empty()) {
      drmType = make_shared<string>(boost::any_cast<string>(m["drmType"]));
    }
    if (m.find("licenseRequest") != m.end() && !m["licenseRequest"].empty()) {
      licenseRequest = make_shared<string>(boost::any_cast<string>(m["licenseRequest"]));
    }
  }


  ~OSSVideoDRMLicenseRequest() = default;
};
class OSSVideoDefinitionRequest : public Darabonba::Model {
public:
  shared_ptr<string> driveId{};
  shared_ptr<string> filePath{};
  shared_ptr<string> protectionScheme{};
  shared_ptr<string> shareId{};

  OSSVideoDefinitionRequest() {}

  explicit OSSVideoDefinitionRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    if (!filePath) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("filePath is required.")));
    }
    Darabonba::Model::validateMaxLength("filePath", filePath, 1000);
    Darabonba::Model::validateMinLength("filePath", filePath, 1);
    Darabonba::Model::validatePattern("shareId", shareId, "[0-9a-zA-Z-]+");
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (filePath) {
      res["file_path"] = boost::any(*filePath);
    }
    if (protectionScheme) {
      res["protection_scheme"] = boost::any(*protectionScheme);
    }
    if (shareId) {
      res["share_id"] = boost::any(*shareId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("file_path") != m.end() && !m["file_path"].empty()) {
      filePath = make_shared<string>(boost::any_cast<string>(m["file_path"]));
    }
    if (m.find("protection_scheme") != m.end() && !m["protection_scheme"].empty()) {
      protectionScheme = make_shared<string>(boost::any_cast<string>(m["protection_scheme"]));
    }
    if (m.find("share_id") != m.end() && !m["share_id"].empty()) {
      shareId = make_shared<string>(boost::any_cast<string>(m["share_id"]));
    }
  }


  ~OSSVideoDefinitionRequest() = default;
};
class OSSVideoM3U8Request : public Darabonba::Model {
public:
  shared_ptr<string> definition{};
  shared_ptr<string> driveId{};
  shared_ptr<long> expireSec{};
  shared_ptr<string> filePath{};
  shared_ptr<string> protectionScheme{};
  shared_ptr<string> shareId{};
  shared_ptr<string> signToken{};

  OSSVideoM3U8Request() {}

  explicit OSSVideoM3U8Request(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    if (expireSec && *expireSec > 86400) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("expireSec is required.")));
    }
    if (expireSec && *expireSec < 60) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("expireSec is required.")));
    }
    if (!filePath) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("filePath is required.")));
    }
    Darabonba::Model::validateMaxLength("filePath", filePath, 1000);
    Darabonba::Model::validateMinLength("filePath", filePath, 1);
    Darabonba::Model::validatePattern("shareId", shareId, "[0-9a-zA-Z-]+");
    if (!signToken) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("signToken is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (definition) {
      res["definition"] = boost::any(*definition);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (expireSec) {
      res["expire_sec"] = boost::any(*expireSec);
    }
    if (filePath) {
      res["file_path"] = boost::any(*filePath);
    }
    if (protectionScheme) {
      res["protection_scheme"] = boost::any(*protectionScheme);
    }
    if (shareId) {
      res["share_id"] = boost::any(*shareId);
    }
    if (signToken) {
      res["sign_token"] = boost::any(*signToken);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("definition") != m.end() && !m["definition"].empty()) {
      definition = make_shared<string>(boost::any_cast<string>(m["definition"]));
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("expire_sec") != m.end() && !m["expire_sec"].empty()) {
      expireSec = make_shared<long>(boost::any_cast<long>(m["expire_sec"]));
    }
    if (m.find("file_path") != m.end() && !m["file_path"].empty()) {
      filePath = make_shared<string>(boost::any_cast<string>(m["file_path"]));
    }
    if (m.find("protection_scheme") != m.end() && !m["protection_scheme"].empty()) {
      protectionScheme = make_shared<string>(boost::any_cast<string>(m["protection_scheme"]));
    }
    if (m.find("share_id") != m.end() && !m["share_id"].empty()) {
      shareId = make_shared<string>(boost::any_cast<string>(m["share_id"]));
    }
    if (m.find("sign_token") != m.end() && !m["sign_token"].empty()) {
      signToken = make_shared<string>(boost::any_cast<string>(m["sign_token"]));
    }
  }


  ~OSSVideoM3U8Request() = default;
};
class OSSVideoTranscodeRequest : public Darabonba::Model {
public:
  shared_ptr<string> driveId{};
  shared_ptr<string> filePath{};
  shared_ptr<long> hlsTime{};
  shared_ptr<string> protectionScheme{};
  shared_ptr<string> remarks{};
  shared_ptr<string> shareId{};
  shared_ptr<bool> transcode{};

  OSSVideoTranscodeRequest() {}

  explicit OSSVideoTranscodeRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    if (!filePath) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("filePath is required.")));
    }
    Darabonba::Model::validateMaxLength("filePath", filePath, 1000);
    Darabonba::Model::validateMinLength("filePath", filePath, 1);
    Darabonba::Model::validatePattern("shareId", shareId, "[0-9a-zA-Z-]+");
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (filePath) {
      res["file_path"] = boost::any(*filePath);
    }
    if (hlsTime) {
      res["hls_time"] = boost::any(*hlsTime);
    }
    if (protectionScheme) {
      res["protection_scheme"] = boost::any(*protectionScheme);
    }
    if (remarks) {
      res["remarks"] = boost::any(*remarks);
    }
    if (shareId) {
      res["share_id"] = boost::any(*shareId);
    }
    if (transcode) {
      res["transcode"] = boost::any(*transcode);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("file_path") != m.end() && !m["file_path"].empty()) {
      filePath = make_shared<string>(boost::any_cast<string>(m["file_path"]));
    }
    if (m.find("hls_time") != m.end() && !m["hls_time"].empty()) {
      hlsTime = make_shared<long>(boost::any_cast<long>(m["hls_time"]));
    }
    if (m.find("protection_scheme") != m.end() && !m["protection_scheme"].empty()) {
      protectionScheme = make_shared<string>(boost::any_cast<string>(m["protection_scheme"]));
    }
    if (m.find("remarks") != m.end() && !m["remarks"].empty()) {
      remarks = make_shared<string>(boost::any_cast<string>(m["remarks"]));
    }
    if (m.find("share_id") != m.end() && !m["share_id"].empty()) {
      shareId = make_shared<string>(boost::any_cast<string>(m["share_id"]));
    }
    if (m.find("transcode") != m.end() && !m["transcode"].empty()) {
      transcode = make_shared<bool>(boost::any_cast<bool>(m["transcode"]));
    }
  }


  ~OSSVideoTranscodeRequest() = default;
};
class PlayMediaRequest : public Darabonba::Model {
public:
  shared_ptr<string> AuthKey{};
  shared_ptr<string> DriveID{};
  shared_ptr<string> FileID{};

  PlayMediaRequest() {}

  explicit PlayMediaRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!AuthKey) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("AuthKey is required.")));
    }
    Darabonba::Model::validatePattern("AuthKey", AuthKey, "[a-z0-9]+");
    if (!DriveID) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("DriveID is required.")));
    }
    Darabonba::Model::validatePattern("DriveID", DriveID, "[0-9]+");
    if (!FileID) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("FileID is required.")));
    }
    Darabonba::Model::validateMaxLength("FileID", FileID, 50);
    Darabonba::Model::validateMinLength("FileID", FileID, 40);
    Darabonba::Model::validatePattern("FileID", FileID, "[a-z0-9.-_]{1,50}");
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (AuthKey) {
      res["AuthKey"] = boost::any(*AuthKey);
    }
    if (DriveID) {
      res["DriveID"] = boost::any(*DriveID);
    }
    if (FileID) {
      res["FileID"] = boost::any(*FileID);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("AuthKey") != m.end() && !m["AuthKey"].empty()) {
      AuthKey = make_shared<string>(boost::any_cast<string>(m["AuthKey"]));
    }
    if (m.find("DriveID") != m.end() && !m["DriveID"].empty()) {
      DriveID = make_shared<string>(boost::any_cast<string>(m["DriveID"]));
    }
    if (m.find("FileID") != m.end() && !m["FileID"].empty()) {
      FileID = make_shared<string>(boost::any_cast<string>(m["FileID"]));
    }
  }


  ~PlayMediaRequest() = default;
};
class ScanFileMetaRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<string> category{};
  shared_ptr<string> driveId{};
  shared_ptr<long> limit{};
  shared_ptr<string> marker{};

  ScanFileMetaRequest() {}

  explicit ScanFileMetaRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!driveId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("driveId is required.")));
    }
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    if (limit && *limit > 5000) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("limit is required.")));
    }
    if (limit && *limit < 1) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("limit is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (category) {
      res["category"] = boost::any(*category);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (limit) {
      res["limit"] = boost::any(*limit);
    }
    if (marker) {
      res["marker"] = boost::any(*marker);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("category") != m.end() && !m["category"].empty()) {
      category = make_shared<string>(boost::any_cast<string>(m["category"]));
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("limit") != m.end() && !m["limit"].empty()) {
      limit = make_shared<long>(boost::any_cast<long>(m["limit"]));
    }
    if (m.find("marker") != m.end() && !m["marker"].empty()) {
      marker = make_shared<string>(boost::any_cast<string>(m["marker"]));
    }
  }


  ~ScanFileMetaRequest() = default;
};
class SearchFileRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<string> driveId{};
  shared_ptr<string> imageThumbnailProcess{};
  shared_ptr<string> imageUrlProcess{};
  shared_ptr<long> limit{};
  shared_ptr<string> marker{};
  shared_ptr<string> orderBy{};
  shared_ptr<string> query{};
  shared_ptr<long> urlExpireSec{};
  shared_ptr<string> videoThumbnailProcess{};

  SearchFileRequest() {}

  explicit SearchFileRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!driveId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("driveId is required.")));
    }
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    if (limit && *limit > 100) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("limit is required.")));
    }
    if (limit && *limit < 1) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("limit is required.")));
    }
    Darabonba::Model::validateMaxLength("query", query, 4096);
    if (urlExpireSec && *urlExpireSec > 14400) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("urlExpireSec is required.")));
    }
    if (urlExpireSec && *urlExpireSec < 10) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("urlExpireSec is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (imageThumbnailProcess) {
      res["image_thumbnail_process"] = boost::any(*imageThumbnailProcess);
    }
    if (imageUrlProcess) {
      res["image_url_process"] = boost::any(*imageUrlProcess);
    }
    if (limit) {
      res["limit"] = boost::any(*limit);
    }
    if (marker) {
      res["marker"] = boost::any(*marker);
    }
    if (orderBy) {
      res["order_by"] = boost::any(*orderBy);
    }
    if (query) {
      res["query"] = boost::any(*query);
    }
    if (urlExpireSec) {
      res["url_expire_sec"] = boost::any(*urlExpireSec);
    }
    if (videoThumbnailProcess) {
      res["video_thumbnail_process"] = boost::any(*videoThumbnailProcess);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("image_thumbnail_process") != m.end() && !m["image_thumbnail_process"].empty()) {
      imageThumbnailProcess = make_shared<string>(boost::any_cast<string>(m["image_thumbnail_process"]));
    }
    if (m.find("image_url_process") != m.end() && !m["image_url_process"].empty()) {
      imageUrlProcess = make_shared<string>(boost::any_cast<string>(m["image_url_process"]));
    }
    if (m.find("limit") != m.end() && !m["limit"].empty()) {
      limit = make_shared<long>(boost::any_cast<long>(m["limit"]));
    }
    if (m.find("marker") != m.end() && !m["marker"].empty()) {
      marker = make_shared<string>(boost::any_cast<string>(m["marker"]));
    }
    if (m.find("order_by") != m.end() && !m["order_by"].empty()) {
      orderBy = make_shared<string>(boost::any_cast<string>(m["order_by"]));
    }
    if (m.find("query") != m.end() && !m["query"].empty()) {
      query = make_shared<string>(boost::any_cast<string>(m["query"]));
    }
    if (m.find("url_expire_sec") != m.end() && !m["url_expire_sec"].empty()) {
      urlExpireSec = make_shared<long>(boost::any_cast<long>(m["url_expire_sec"]));
    }
    if (m.find("video_thumbnail_process") != m.end() && !m["video_thumbnail_process"].empty()) {
      videoThumbnailProcess = make_shared<string>(boost::any_cast<string>(m["video_thumbnail_process"]));
    }
  }


  ~SearchFileRequest() = default;
};
class UCGetObjectInfoByObjectKeyRequest : public Darabonba::Model {
public:
  shared_ptr<string> objectKey{};

  UCGetObjectInfoByObjectKeyRequest() {}

  explicit UCGetObjectInfoByObjectKeyRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (objectKey) {
      res["object_key"] = boost::any(*objectKey);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("object_key") != m.end() && !m["object_key"].empty()) {
      objectKey = make_shared<string>(boost::any_cast<string>(m["object_key"]));
    }
  }


  ~UCGetObjectInfoByObjectKeyRequest() = default;
};
class UCGetObjectInfoBySha1Request : public Darabonba::Model {
public:
  shared_ptr<string> sha1{};

  UCGetObjectInfoBySha1Request() {}

  explicit UCGetObjectInfoBySha1Request(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (sha1) {
      res["sha1"] = boost::any(*sha1);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("sha1") != m.end() && !m["sha1"].empty()) {
      sha1 = make_shared<string>(boost::any_cast<string>(m["sha1"]));
    }
  }


  ~UCGetObjectInfoBySha1Request() = default;
};
class UpdateDriveRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<string> description{};
  shared_ptr<string> driveId{};
  shared_ptr<string> driveName{};
  shared_ptr<bool> encryptDataAccess{};
  shared_ptr<string> encryptMode{};
  shared_ptr<string> status{};
  shared_ptr<long> totalSize{};

  UpdateDriveRequest() {}

  explicit UpdateDriveRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    Darabonba::Model::validateMaxLength("description", description, 1024);
    if (!driveId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("driveId is required.")));
    }
    Darabonba::Model::validateMaxLength("driveName", driveName, 1024);
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (description) {
      res["description"] = boost::any(*description);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (driveName) {
      res["drive_name"] = boost::any(*driveName);
    }
    if (encryptDataAccess) {
      res["encrypt_data_access"] = boost::any(*encryptDataAccess);
    }
    if (encryptMode) {
      res["encrypt_mode"] = boost::any(*encryptMode);
    }
    if (status) {
      res["status"] = boost::any(*status);
    }
    if (totalSize) {
      res["total_size"] = boost::any(*totalSize);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("description") != m.end() && !m["description"].empty()) {
      description = make_shared<string>(boost::any_cast<string>(m["description"]));
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("drive_name") != m.end() && !m["drive_name"].empty()) {
      driveName = make_shared<string>(boost::any_cast<string>(m["drive_name"]));
    }
    if (m.find("encrypt_data_access") != m.end() && !m["encrypt_data_access"].empty()) {
      encryptDataAccess = make_shared<bool>(boost::any_cast<bool>(m["encrypt_data_access"]));
    }
    if (m.find("encrypt_mode") != m.end() && !m["encrypt_mode"].empty()) {
      encryptMode = make_shared<string>(boost::any_cast<string>(m["encrypt_mode"]));
    }
    if (m.find("status") != m.end() && !m["status"].empty()) {
      status = make_shared<string>(boost::any_cast<string>(m["status"]));
    }
    if (m.find("total_size") != m.end() && !m["total_size"].empty()) {
      totalSize = make_shared<long>(boost::any_cast<long>(m["total_size"]));
    }
  }


  ~UpdateDriveRequest() = default;
};
class UpdateFileMetaRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<string> checkNameMode{};
  shared_ptr<string> customIndexKey{};
  shared_ptr<string> description{};
  shared_ptr<string> driveId{};
  shared_ptr<string> encryptMode{};
  shared_ptr<string> fileId{};
  shared_ptr<bool> hidden{};
  shared_ptr<vector<string>> labels{};
  shared_ptr<string> meta{};
  shared_ptr<string> name{};
  shared_ptr<bool> starred{};
  shared_ptr<string> userMeta{};

  UpdateFileMetaRequest() {}

  explicit UpdateFileMetaRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    Darabonba::Model::validateMaxLength("description", description, 1024);
    if (!driveId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("driveId is required.")));
    }
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    if (!fileId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("fileId is required.")));
    }
    Darabonba::Model::validateMaxLength("fileId", fileId, 50);
    Darabonba::Model::validateMinLength("fileId", fileId, 40);
    Darabonba::Model::validatePattern("fileId", fileId, "[a-z0-9.-_]{1,50}");
    Darabonba::Model::validateMaxLength("name", name, 1024);
    Darabonba::Model::validateMinLength("name", name, 1);
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (checkNameMode) {
      res["check_name_mode"] = boost::any(*checkNameMode);
    }
    if (customIndexKey) {
      res["custom_index_key"] = boost::any(*customIndexKey);
    }
    if (description) {
      res["description"] = boost::any(*description);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (encryptMode) {
      res["encrypt_mode"] = boost::any(*encryptMode);
    }
    if (fileId) {
      res["file_id"] = boost::any(*fileId);
    }
    if (hidden) {
      res["hidden"] = boost::any(*hidden);
    }
    if (labels) {
      res["labels"] = boost::any(*labels);
    }
    if (meta) {
      res["meta"] = boost::any(*meta);
    }
    if (name) {
      res["name"] = boost::any(*name);
    }
    if (starred) {
      res["starred"] = boost::any(*starred);
    }
    if (userMeta) {
      res["user_meta"] = boost::any(*userMeta);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("check_name_mode") != m.end() && !m["check_name_mode"].empty()) {
      checkNameMode = make_shared<string>(boost::any_cast<string>(m["check_name_mode"]));
    }
    if (m.find("custom_index_key") != m.end() && !m["custom_index_key"].empty()) {
      customIndexKey = make_shared<string>(boost::any_cast<string>(m["custom_index_key"]));
    }
    if (m.find("description") != m.end() && !m["description"].empty()) {
      description = make_shared<string>(boost::any_cast<string>(m["description"]));
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("encrypt_mode") != m.end() && !m["encrypt_mode"].empty()) {
      encryptMode = make_shared<string>(boost::any_cast<string>(m["encrypt_mode"]));
    }
    if (m.find("file_id") != m.end() && !m["file_id"].empty()) {
      fileId = make_shared<string>(boost::any_cast<string>(m["file_id"]));
    }
    if (m.find("hidden") != m.end() && !m["hidden"].empty()) {
      hidden = make_shared<bool>(boost::any_cast<bool>(m["hidden"]));
    }
    if (m.find("labels") != m.end() && !m["labels"].empty()) {
      vector<string> toVec1;
      if (typeid(vector<boost::any>).name() == m["labels"].type().name()) {
        vector<boost::any> vec1 = boost::any_cast<vector<boost::any>>(m["labels"]);
        for (auto item:vec1) {
           toVec1.push_back(boost::any_cast<string>(item));
        }
      }
      labels = make_shared<vector<string>>(toVec1);
    }
    if (m.find("meta") != m.end() && !m["meta"].empty()) {
      meta = make_shared<string>(boost::any_cast<string>(m["meta"]));
    }
    if (m.find("name") != m.end() && !m["name"].empty()) {
      name = make_shared<string>(boost::any_cast<string>(m["name"]));
    }
    if (m.find("starred") != m.end() && !m["starred"].empty()) {
      starred = make_shared<bool>(boost::any_cast<bool>(m["starred"]));
    }
    if (m.find("user_meta") != m.end() && !m["user_meta"].empty()) {
      userMeta = make_shared<string>(boost::any_cast<string>(m["user_meta"]));
    }
  }


  ~UpdateFileMetaRequest() = default;
};
class UpdateShareRequest : public Darabonba::Model {
public:
  shared_ptr<string> description{};
  shared_ptr<string> expiration{};
  shared_ptr<vector<string>> permissions{};
  shared_ptr<string> shareId{};
  shared_ptr<string> shareName{};
  shared_ptr<vector<SharePermissionPolicy>> sharePolicy{};
  shared_ptr<string> status{};

  UpdateShareRequest() {}

  explicit UpdateShareRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    Darabonba::Model::validateMaxLength("description", description, 1024);
    if (!shareId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("shareId is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (description) {
      res["description"] = boost::any(*description);
    }
    if (expiration) {
      res["expiration"] = boost::any(*expiration);
    }
    if (permissions) {
      res["permissions"] = boost::any(*permissions);
    }
    if (shareId) {
      res["share_id"] = boost::any(*shareId);
    }
    if (shareName) {
      res["share_name"] = boost::any(*shareName);
    }
    if (sharePolicy) {
      vector<boost::any> temp1;
      for(auto item1:*sharePolicy){
        temp1.push_back(boost::any(item1.toMap()));
      }
      res["share_policy"] = boost::any(temp1);
    }
    if (status) {
      res["status"] = boost::any(*status);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("description") != m.end() && !m["description"].empty()) {
      description = make_shared<string>(boost::any_cast<string>(m["description"]));
    }
    if (m.find("expiration") != m.end() && !m["expiration"].empty()) {
      expiration = make_shared<string>(boost::any_cast<string>(m["expiration"]));
    }
    if (m.find("permissions") != m.end() && !m["permissions"].empty()) {
      vector<string> toVec1;
      if (typeid(vector<boost::any>).name() == m["permissions"].type().name()) {
        vector<boost::any> vec1 = boost::any_cast<vector<boost::any>>(m["permissions"]);
        for (auto item:vec1) {
           toVec1.push_back(boost::any_cast<string>(item));
        }
      }
      permissions = make_shared<vector<string>>(toVec1);
    }
    if (m.find("share_id") != m.end() && !m["share_id"].empty()) {
      shareId = make_shared<string>(boost::any_cast<string>(m["share_id"]));
    }
    if (m.find("share_name") != m.end() && !m["share_name"].empty()) {
      shareName = make_shared<string>(boost::any_cast<string>(m["share_name"]));
    }
    if (m.find("share_policy") != m.end() && !m["share_policy"].empty()) {
      if (typeid(vector<boost::any>).name() == m["share_policy"].type().name()) {
        vector<SharePermissionPolicy> expect1;
        for(auto item1:boost::any_cast<vector<boost::any>>(m["share_policy"])){
          if (typeid(map<string, boost::any>).name() == item1.type().name()) {
            SharePermissionPolicy model2;
            model2.fromMap(boost::any_cast<map<string, boost::any>>(item1));
            expect1.push_back(model2);
          }
        }
        sharePolicy = make_shared<vector<SharePermissionPolicy>>(expect1);
      }
    }
    if (m.find("status") != m.end() && !m["status"].empty()) {
      status = make_shared<string>(boost::any_cast<string>(m["status"]));
    }
  }


  ~UpdateShareRequest() = default;
};
class CreateUserResponse : public Darabonba::Model {
public:
  shared_ptr<string> avatar{};
  shared_ptr<long> createdAt{};
  shared_ptr<string> defaultDriveId{};
  shared_ptr<string> description{};
  shared_ptr<string> domainId{};
  shared_ptr<string> email{};
  shared_ptr<string> nickName{};
  shared_ptr<string> phone{};
  shared_ptr<string> role{};
  shared_ptr<string> status{};
  shared_ptr<long> updatedAt{};
  shared_ptr<map<string, boost::any>> userData{};
  shared_ptr<string> userId{};
  shared_ptr<string> userName{};

  CreateUserResponse() {}

  explicit CreateUserResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (avatar) {
      res["avatar"] = boost::any(*avatar);
    }
    if (createdAt) {
      res["created_at"] = boost::any(*createdAt);
    }
    if (defaultDriveId) {
      res["default_drive_id"] = boost::any(*defaultDriveId);
    }
    if (description) {
      res["description"] = boost::any(*description);
    }
    if (domainId) {
      res["domain_id"] = boost::any(*domainId);
    }
    if (email) {
      res["email"] = boost::any(*email);
    }
    if (nickName) {
      res["nick_name"] = boost::any(*nickName);
    }
    if (phone) {
      res["phone"] = boost::any(*phone);
    }
    if (role) {
      res["role"] = boost::any(*role);
    }
    if (status) {
      res["status"] = boost::any(*status);
    }
    if (updatedAt) {
      res["updated_at"] = boost::any(*updatedAt);
    }
    if (userData) {
      res["user_data"] = boost::any(*userData);
    }
    if (userId) {
      res["user_id"] = boost::any(*userId);
    }
    if (userName) {
      res["user_name"] = boost::any(*userName);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("avatar") != m.end() && !m["avatar"].empty()) {
      avatar = make_shared<string>(boost::any_cast<string>(m["avatar"]));
    }
    if (m.find("created_at") != m.end() && !m["created_at"].empty()) {
      createdAt = make_shared<long>(boost::any_cast<long>(m["created_at"]));
    }
    if (m.find("default_drive_id") != m.end() && !m["default_drive_id"].empty()) {
      defaultDriveId = make_shared<string>(boost::any_cast<string>(m["default_drive_id"]));
    }
    if (m.find("description") != m.end() && !m["description"].empty()) {
      description = make_shared<string>(boost::any_cast<string>(m["description"]));
    }
    if (m.find("domain_id") != m.end() && !m["domain_id"].empty()) {
      domainId = make_shared<string>(boost::any_cast<string>(m["domain_id"]));
    }
    if (m.find("email") != m.end() && !m["email"].empty()) {
      email = make_shared<string>(boost::any_cast<string>(m["email"]));
    }
    if (m.find("nick_name") != m.end() && !m["nick_name"].empty()) {
      nickName = make_shared<string>(boost::any_cast<string>(m["nick_name"]));
    }
    if (m.find("phone") != m.end() && !m["phone"].empty()) {
      phone = make_shared<string>(boost::any_cast<string>(m["phone"]));
    }
    if (m.find("role") != m.end() && !m["role"].empty()) {
      role = make_shared<string>(boost::any_cast<string>(m["role"]));
    }
    if (m.find("status") != m.end() && !m["status"].empty()) {
      status = make_shared<string>(boost::any_cast<string>(m["status"]));
    }
    if (m.find("updated_at") != m.end() && !m["updated_at"].empty()) {
      updatedAt = make_shared<long>(boost::any_cast<long>(m["updated_at"]));
    }
    if (m.find("user_data") != m.end() && !m["user_data"].empty()) {
      map<string, boost::any> map1 = boost::any_cast<map<string, boost::any>>(m["user_data"]);
      map<string, boost::any> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      userData = make_shared<map<string, boost::any>>(toMap1);
    }
    if (m.find("user_id") != m.end() && !m["user_id"].empty()) {
      userId = make_shared<string>(boost::any_cast<string>(m["user_id"]));
    }
    if (m.find("user_name") != m.end() && !m["user_name"].empty()) {
      userName = make_shared<string>(boost::any_cast<string>(m["user_name"]));
    }
  }


  ~CreateUserResponse() = default;
};
class CreateUserModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<CreateUserResponse> body{};

  CreateUserModel() {}

  explicit CreateUserModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        CreateUserResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<CreateUserResponse>(model1);
      }
    }
  }


  ~CreateUserModel() = default;
};
class DeleteUserModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};

  DeleteUserModel() {}

  explicit DeleteUserModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
  }


  ~DeleteUserModel() = default;
};
class GetUserResponse : public Darabonba::Model {
public:
  shared_ptr<string> avatar{};
  shared_ptr<long> createdAt{};
  shared_ptr<string> defaultDriveId{};
  shared_ptr<string> description{};
  shared_ptr<string> domainId{};
  shared_ptr<string> email{};
  shared_ptr<string> nickName{};
  shared_ptr<string> phone{};
  shared_ptr<string> role{};
  shared_ptr<string> status{};
  shared_ptr<long> updatedAt{};
  shared_ptr<map<string, boost::any>> userData{};
  shared_ptr<string> userId{};
  shared_ptr<string> userName{};

  GetUserResponse() {}

  explicit GetUserResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (avatar) {
      res["avatar"] = boost::any(*avatar);
    }
    if (createdAt) {
      res["created_at"] = boost::any(*createdAt);
    }
    if (defaultDriveId) {
      res["default_drive_id"] = boost::any(*defaultDriveId);
    }
    if (description) {
      res["description"] = boost::any(*description);
    }
    if (domainId) {
      res["domain_id"] = boost::any(*domainId);
    }
    if (email) {
      res["email"] = boost::any(*email);
    }
    if (nickName) {
      res["nick_name"] = boost::any(*nickName);
    }
    if (phone) {
      res["phone"] = boost::any(*phone);
    }
    if (role) {
      res["role"] = boost::any(*role);
    }
    if (status) {
      res["status"] = boost::any(*status);
    }
    if (updatedAt) {
      res["updated_at"] = boost::any(*updatedAt);
    }
    if (userData) {
      res["user_data"] = boost::any(*userData);
    }
    if (userId) {
      res["user_id"] = boost::any(*userId);
    }
    if (userName) {
      res["user_name"] = boost::any(*userName);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("avatar") != m.end() && !m["avatar"].empty()) {
      avatar = make_shared<string>(boost::any_cast<string>(m["avatar"]));
    }
    if (m.find("created_at") != m.end() && !m["created_at"].empty()) {
      createdAt = make_shared<long>(boost::any_cast<long>(m["created_at"]));
    }
    if (m.find("default_drive_id") != m.end() && !m["default_drive_id"].empty()) {
      defaultDriveId = make_shared<string>(boost::any_cast<string>(m["default_drive_id"]));
    }
    if (m.find("description") != m.end() && !m["description"].empty()) {
      description = make_shared<string>(boost::any_cast<string>(m["description"]));
    }
    if (m.find("domain_id") != m.end() && !m["domain_id"].empty()) {
      domainId = make_shared<string>(boost::any_cast<string>(m["domain_id"]));
    }
    if (m.find("email") != m.end() && !m["email"].empty()) {
      email = make_shared<string>(boost::any_cast<string>(m["email"]));
    }
    if (m.find("nick_name") != m.end() && !m["nick_name"].empty()) {
      nickName = make_shared<string>(boost::any_cast<string>(m["nick_name"]));
    }
    if (m.find("phone") != m.end() && !m["phone"].empty()) {
      phone = make_shared<string>(boost::any_cast<string>(m["phone"]));
    }
    if (m.find("role") != m.end() && !m["role"].empty()) {
      role = make_shared<string>(boost::any_cast<string>(m["role"]));
    }
    if (m.find("status") != m.end() && !m["status"].empty()) {
      status = make_shared<string>(boost::any_cast<string>(m["status"]));
    }
    if (m.find("updated_at") != m.end() && !m["updated_at"].empty()) {
      updatedAt = make_shared<long>(boost::any_cast<long>(m["updated_at"]));
    }
    if (m.find("user_data") != m.end() && !m["user_data"].empty()) {
      map<string, boost::any> map1 = boost::any_cast<map<string, boost::any>>(m["user_data"]);
      map<string, boost::any> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      userData = make_shared<map<string, boost::any>>(toMap1);
    }
    if (m.find("user_id") != m.end() && !m["user_id"].empty()) {
      userId = make_shared<string>(boost::any_cast<string>(m["user_id"]));
    }
    if (m.find("user_name") != m.end() && !m["user_name"].empty()) {
      userName = make_shared<string>(boost::any_cast<string>(m["user_name"]));
    }
  }


  ~GetUserResponse() = default;
};
class GetUserModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<GetUserResponse> body{};

  GetUserModel() {}

  explicit GetUserModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        GetUserResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<GetUserResponse>(model1);
      }
    }
  }


  ~GetUserModel() = default;
};
class BaseUserResponse : public Darabonba::Model {
public:
  shared_ptr<string> avatar{};
  shared_ptr<long> createdAt{};
  shared_ptr<string> defaultDriveId{};
  shared_ptr<string> description{};
  shared_ptr<string> domainId{};
  shared_ptr<string> email{};
  shared_ptr<string> nickName{};
  shared_ptr<string> phone{};
  shared_ptr<string> role{};
  shared_ptr<string> status{};
  shared_ptr<long> updatedAt{};
  shared_ptr<map<string, boost::any>> userData{};
  shared_ptr<string> userId{};
  shared_ptr<string> userName{};

  BaseUserResponse() {}

  explicit BaseUserResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (avatar) {
      res["avatar"] = boost::any(*avatar);
    }
    if (createdAt) {
      res["created_at"] = boost::any(*createdAt);
    }
    if (defaultDriveId) {
      res["default_drive_id"] = boost::any(*defaultDriveId);
    }
    if (description) {
      res["description"] = boost::any(*description);
    }
    if (domainId) {
      res["domain_id"] = boost::any(*domainId);
    }
    if (email) {
      res["email"] = boost::any(*email);
    }
    if (nickName) {
      res["nick_name"] = boost::any(*nickName);
    }
    if (phone) {
      res["phone"] = boost::any(*phone);
    }
    if (role) {
      res["role"] = boost::any(*role);
    }
    if (status) {
      res["status"] = boost::any(*status);
    }
    if (updatedAt) {
      res["updated_at"] = boost::any(*updatedAt);
    }
    if (userData) {
      res["user_data"] = boost::any(*userData);
    }
    if (userId) {
      res["user_id"] = boost::any(*userId);
    }
    if (userName) {
      res["user_name"] = boost::any(*userName);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("avatar") != m.end() && !m["avatar"].empty()) {
      avatar = make_shared<string>(boost::any_cast<string>(m["avatar"]));
    }
    if (m.find("created_at") != m.end() && !m["created_at"].empty()) {
      createdAt = make_shared<long>(boost::any_cast<long>(m["created_at"]));
    }
    if (m.find("default_drive_id") != m.end() && !m["default_drive_id"].empty()) {
      defaultDriveId = make_shared<string>(boost::any_cast<string>(m["default_drive_id"]));
    }
    if (m.find("description") != m.end() && !m["description"].empty()) {
      description = make_shared<string>(boost::any_cast<string>(m["description"]));
    }
    if (m.find("domain_id") != m.end() && !m["domain_id"].empty()) {
      domainId = make_shared<string>(boost::any_cast<string>(m["domain_id"]));
    }
    if (m.find("email") != m.end() && !m["email"].empty()) {
      email = make_shared<string>(boost::any_cast<string>(m["email"]));
    }
    if (m.find("nick_name") != m.end() && !m["nick_name"].empty()) {
      nickName = make_shared<string>(boost::any_cast<string>(m["nick_name"]));
    }
    if (m.find("phone") != m.end() && !m["phone"].empty()) {
      phone = make_shared<string>(boost::any_cast<string>(m["phone"]));
    }
    if (m.find("role") != m.end() && !m["role"].empty()) {
      role = make_shared<string>(boost::any_cast<string>(m["role"]));
    }
    if (m.find("status") != m.end() && !m["status"].empty()) {
      status = make_shared<string>(boost::any_cast<string>(m["status"]));
    }
    if (m.find("updated_at") != m.end() && !m["updated_at"].empty()) {
      updatedAt = make_shared<long>(boost::any_cast<long>(m["updated_at"]));
    }
    if (m.find("user_data") != m.end() && !m["user_data"].empty()) {
      map<string, boost::any> map1 = boost::any_cast<map<string, boost::any>>(m["user_data"]);
      map<string, boost::any> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      userData = make_shared<map<string, boost::any>>(toMap1);
    }
    if (m.find("user_id") != m.end() && !m["user_id"].empty()) {
      userId = make_shared<string>(boost::any_cast<string>(m["user_id"]));
    }
    if (m.find("user_name") != m.end() && !m["user_name"].empty()) {
      userName = make_shared<string>(boost::any_cast<string>(m["user_name"]));
    }
  }


  ~BaseUserResponse() = default;
};
class ListUserResponse : public Darabonba::Model {
public:
  shared_ptr<vector<BaseUserResponse>> items{};
  shared_ptr<string> nextMarker{};

  ListUserResponse() {}

  explicit ListUserResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (items) {
      vector<boost::any> temp1;
      for(auto item1:*items){
        temp1.push_back(boost::any(item1.toMap()));
      }
      res["items"] = boost::any(temp1);
    }
    if (nextMarker) {
      res["next_marker"] = boost::any(*nextMarker);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("items") != m.end() && !m["items"].empty()) {
      if (typeid(vector<boost::any>).name() == m["items"].type().name()) {
        vector<BaseUserResponse> expect1;
        for(auto item1:boost::any_cast<vector<boost::any>>(m["items"])){
          if (typeid(map<string, boost::any>).name() == item1.type().name()) {
            BaseUserResponse model2;
            model2.fromMap(boost::any_cast<map<string, boost::any>>(item1));
            expect1.push_back(model2);
          }
        }
        items = make_shared<vector<BaseUserResponse>>(expect1);
      }
    }
    if (m.find("next_marker") != m.end() && !m["next_marker"].empty()) {
      nextMarker = make_shared<string>(boost::any_cast<string>(m["next_marker"]));
    }
  }


  ~ListUserResponse() = default;
};
class ListUsersModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<ListUserResponse> body{};

  ListUsersModel() {}

  explicit ListUsersModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        ListUserResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<ListUserResponse>(model1);
      }
    }
  }


  ~ListUsersModel() = default;
};
class SearchUserModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<ListUserResponse> body{};

  SearchUserModel() {}

  explicit SearchUserModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        ListUserResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<ListUserResponse>(model1);
      }
    }
  }


  ~SearchUserModel() = default;
};
class UpdateUserResponse : public Darabonba::Model {
public:
  shared_ptr<string> avatar{};
  shared_ptr<long> createdAt{};
  shared_ptr<string> defaultDriveId{};
  shared_ptr<string> description{};
  shared_ptr<string> domainId{};
  shared_ptr<string> email{};
  shared_ptr<string> nickName{};
  shared_ptr<string> phone{};
  shared_ptr<string> role{};
  shared_ptr<string> status{};
  shared_ptr<long> updatedAt{};
  shared_ptr<map<string, boost::any>> userData{};
  shared_ptr<string> userId{};
  shared_ptr<string> userName{};

  UpdateUserResponse() {}

  explicit UpdateUserResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (avatar) {
      res["avatar"] = boost::any(*avatar);
    }
    if (createdAt) {
      res["created_at"] = boost::any(*createdAt);
    }
    if (defaultDriveId) {
      res["default_drive_id"] = boost::any(*defaultDriveId);
    }
    if (description) {
      res["description"] = boost::any(*description);
    }
    if (domainId) {
      res["domain_id"] = boost::any(*domainId);
    }
    if (email) {
      res["email"] = boost::any(*email);
    }
    if (nickName) {
      res["nick_name"] = boost::any(*nickName);
    }
    if (phone) {
      res["phone"] = boost::any(*phone);
    }
    if (role) {
      res["role"] = boost::any(*role);
    }
    if (status) {
      res["status"] = boost::any(*status);
    }
    if (updatedAt) {
      res["updated_at"] = boost::any(*updatedAt);
    }
    if (userData) {
      res["user_data"] = boost::any(*userData);
    }
    if (userId) {
      res["user_id"] = boost::any(*userId);
    }
    if (userName) {
      res["user_name"] = boost::any(*userName);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("avatar") != m.end() && !m["avatar"].empty()) {
      avatar = make_shared<string>(boost::any_cast<string>(m["avatar"]));
    }
    if (m.find("created_at") != m.end() && !m["created_at"].empty()) {
      createdAt = make_shared<long>(boost::any_cast<long>(m["created_at"]));
    }
    if (m.find("default_drive_id") != m.end() && !m["default_drive_id"].empty()) {
      defaultDriveId = make_shared<string>(boost::any_cast<string>(m["default_drive_id"]));
    }
    if (m.find("description") != m.end() && !m["description"].empty()) {
      description = make_shared<string>(boost::any_cast<string>(m["description"]));
    }
    if (m.find("domain_id") != m.end() && !m["domain_id"].empty()) {
      domainId = make_shared<string>(boost::any_cast<string>(m["domain_id"]));
    }
    if (m.find("email") != m.end() && !m["email"].empty()) {
      email = make_shared<string>(boost::any_cast<string>(m["email"]));
    }
    if (m.find("nick_name") != m.end() && !m["nick_name"].empty()) {
      nickName = make_shared<string>(boost::any_cast<string>(m["nick_name"]));
    }
    if (m.find("phone") != m.end() && !m["phone"].empty()) {
      phone = make_shared<string>(boost::any_cast<string>(m["phone"]));
    }
    if (m.find("role") != m.end() && !m["role"].empty()) {
      role = make_shared<string>(boost::any_cast<string>(m["role"]));
    }
    if (m.find("status") != m.end() && !m["status"].empty()) {
      status = make_shared<string>(boost::any_cast<string>(m["status"]));
    }
    if (m.find("updated_at") != m.end() && !m["updated_at"].empty()) {
      updatedAt = make_shared<long>(boost::any_cast<long>(m["updated_at"]));
    }
    if (m.find("user_data") != m.end() && !m["user_data"].empty()) {
      map<string, boost::any> map1 = boost::any_cast<map<string, boost::any>>(m["user_data"]);
      map<string, boost::any> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      userData = make_shared<map<string, boost::any>>(toMap1);
    }
    if (m.find("user_id") != m.end() && !m["user_id"].empty()) {
      userId = make_shared<string>(boost::any_cast<string>(m["user_id"]));
    }
    if (m.find("user_name") != m.end() && !m["user_name"].empty()) {
      userName = make_shared<string>(boost::any_cast<string>(m["user_name"]));
    }
  }


  ~UpdateUserResponse() = default;
};
class UpdateUserModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<UpdateUserResponse> body{};

  UpdateUserModel() {}

  explicit UpdateUserModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        UpdateUserResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<UpdateUserResponse>(model1);
      }
    }
  }


  ~UpdateUserModel() = default;
};
class CreateUserRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<string> avatar{};
  shared_ptr<string> description{};
  shared_ptr<string> email{};
  shared_ptr<string> nickName{};
  shared_ptr<string> phone{};
  shared_ptr<string> role{};
  shared_ptr<string> status{};
  shared_ptr<map<string, boost::any>> userData{};
  shared_ptr<string> userId{};
  shared_ptr<string> userName{};

  CreateUserRequest() {}

  explicit CreateUserRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    Darabonba::Model::validateMaxLength("description", description, 1024);
    if (!userId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("userId is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (avatar) {
      res["avatar"] = boost::any(*avatar);
    }
    if (description) {
      res["description"] = boost::any(*description);
    }
    if (email) {
      res["email"] = boost::any(*email);
    }
    if (nickName) {
      res["nick_name"] = boost::any(*nickName);
    }
    if (phone) {
      res["phone"] = boost::any(*phone);
    }
    if (role) {
      res["role"] = boost::any(*role);
    }
    if (status) {
      res["status"] = boost::any(*status);
    }
    if (userData) {
      res["user_data"] = boost::any(*userData);
    }
    if (userId) {
      res["user_id"] = boost::any(*userId);
    }
    if (userName) {
      res["user_name"] = boost::any(*userName);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("avatar") != m.end() && !m["avatar"].empty()) {
      avatar = make_shared<string>(boost::any_cast<string>(m["avatar"]));
    }
    if (m.find("description") != m.end() && !m["description"].empty()) {
      description = make_shared<string>(boost::any_cast<string>(m["description"]));
    }
    if (m.find("email") != m.end() && !m["email"].empty()) {
      email = make_shared<string>(boost::any_cast<string>(m["email"]));
    }
    if (m.find("nick_name") != m.end() && !m["nick_name"].empty()) {
      nickName = make_shared<string>(boost::any_cast<string>(m["nick_name"]));
    }
    if (m.find("phone") != m.end() && !m["phone"].empty()) {
      phone = make_shared<string>(boost::any_cast<string>(m["phone"]));
    }
    if (m.find("role") != m.end() && !m["role"].empty()) {
      role = make_shared<string>(boost::any_cast<string>(m["role"]));
    }
    if (m.find("status") != m.end() && !m["status"].empty()) {
      status = make_shared<string>(boost::any_cast<string>(m["status"]));
    }
    if (m.find("user_data") != m.end() && !m["user_data"].empty()) {
      map<string, boost::any> map1 = boost::any_cast<map<string, boost::any>>(m["user_data"]);
      map<string, boost::any> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      userData = make_shared<map<string, boost::any>>(toMap1);
    }
    if (m.find("user_id") != m.end() && !m["user_id"].empty()) {
      userId = make_shared<string>(boost::any_cast<string>(m["user_id"]));
    }
    if (m.find("user_name") != m.end() && !m["user_name"].empty()) {
      userName = make_shared<string>(boost::any_cast<string>(m["user_name"]));
    }
  }


  ~CreateUserRequest() = default;
};
class DeleteUserRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<string> userId{};

  DeleteUserRequest() {}

  explicit DeleteUserRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!userId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("userId is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (userId) {
      res["user_id"] = boost::any(*userId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("user_id") != m.end() && !m["user_id"].empty()) {
      userId = make_shared<string>(boost::any_cast<string>(m["user_id"]));
    }
  }


  ~DeleteUserRequest() = default;
};
class DeleteUserResponse : public Darabonba::Model {
public:

  DeleteUserResponse() {}

  explicit DeleteUserResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
  }


};
class GetUserRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<string> userId{};

  GetUserRequest() {}

  explicit GetUserRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (userId) {
      res["user_id"] = boost::any(*userId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("user_id") != m.end() && !m["user_id"].empty()) {
      userId = make_shared<string>(boost::any_cast<string>(m["user_id"]));
    }
  }


  ~GetUserRequest() = default;
};
class ListUserRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<long> limit{};
  shared_ptr<string> marker{};

  ListUserRequest() {}

  explicit ListUserRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (limit && *limit > 100) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("limit is required.")));
    }
    if (limit && *limit < 1) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("limit is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (limit) {
      res["limit"] = boost::any(*limit);
    }
    if (marker) {
      res["marker"] = boost::any(*marker);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("limit") != m.end() && !m["limit"].empty()) {
      limit = make_shared<long>(boost::any_cast<long>(m["limit"]));
    }
    if (m.find("marker") != m.end() && !m["marker"].empty()) {
      marker = make_shared<string>(boost::any_cast<string>(m["marker"]));
    }
  }


  ~ListUserRequest() = default;
};
class SearchUserRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<string> email{};
  shared_ptr<long> limit{};
  shared_ptr<string> marker{};
  shared_ptr<string> nickName{};
  shared_ptr<string> phone{};
  shared_ptr<string> role{};
  shared_ptr<string> status{};
  shared_ptr<string> userName{};

  SearchUserRequest() {}

  explicit SearchUserRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (limit && *limit > 100) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("limit is required.")));
    }
    if (limit && *limit < 1) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("limit is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (email) {
      res["email"] = boost::any(*email);
    }
    if (limit) {
      res["limit"] = boost::any(*limit);
    }
    if (marker) {
      res["marker"] = boost::any(*marker);
    }
    if (nickName) {
      res["nick_name"] = boost::any(*nickName);
    }
    if (phone) {
      res["phone"] = boost::any(*phone);
    }
    if (role) {
      res["role"] = boost::any(*role);
    }
    if (status) {
      res["status"] = boost::any(*status);
    }
    if (userName) {
      res["user_name"] = boost::any(*userName);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("email") != m.end() && !m["email"].empty()) {
      email = make_shared<string>(boost::any_cast<string>(m["email"]));
    }
    if (m.find("limit") != m.end() && !m["limit"].empty()) {
      limit = make_shared<long>(boost::any_cast<long>(m["limit"]));
    }
    if (m.find("marker") != m.end() && !m["marker"].empty()) {
      marker = make_shared<string>(boost::any_cast<string>(m["marker"]));
    }
    if (m.find("nick_name") != m.end() && !m["nick_name"].empty()) {
      nickName = make_shared<string>(boost::any_cast<string>(m["nick_name"]));
    }
    if (m.find("phone") != m.end() && !m["phone"].empty()) {
      phone = make_shared<string>(boost::any_cast<string>(m["phone"]));
    }
    if (m.find("role") != m.end() && !m["role"].empty()) {
      role = make_shared<string>(boost::any_cast<string>(m["role"]));
    }
    if (m.find("status") != m.end() && !m["status"].empty()) {
      status = make_shared<string>(boost::any_cast<string>(m["status"]));
    }
    if (m.find("user_name") != m.end() && !m["user_name"].empty()) {
      userName = make_shared<string>(boost::any_cast<string>(m["user_name"]));
    }
  }


  ~SearchUserRequest() = default;
};
class UpdateUserRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<string> avatar{};
  shared_ptr<string> description{};
  shared_ptr<string> email{};
  shared_ptr<string> nickName{};
  shared_ptr<string> phone{};
  shared_ptr<string> role{};
  shared_ptr<string> status{};
  shared_ptr<map<string, boost::any>> userData{};
  shared_ptr<string> userId{};

  UpdateUserRequest() {}

  explicit UpdateUserRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    Darabonba::Model::validateMaxLength("description", description, 1024);
    if (!userId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("userId is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (avatar) {
      res["avatar"] = boost::any(*avatar);
    }
    if (description) {
      res["description"] = boost::any(*description);
    }
    if (email) {
      res["email"] = boost::any(*email);
    }
    if (nickName) {
      res["nick_name"] = boost::any(*nickName);
    }
    if (phone) {
      res["phone"] = boost::any(*phone);
    }
    if (role) {
      res["role"] = boost::any(*role);
    }
    if (status) {
      res["status"] = boost::any(*status);
    }
    if (userData) {
      res["user_data"] = boost::any(*userData);
    }
    if (userId) {
      res["user_id"] = boost::any(*userId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("avatar") != m.end() && !m["avatar"].empty()) {
      avatar = make_shared<string>(boost::any_cast<string>(m["avatar"]));
    }
    if (m.find("description") != m.end() && !m["description"].empty()) {
      description = make_shared<string>(boost::any_cast<string>(m["description"]));
    }
    if (m.find("email") != m.end() && !m["email"].empty()) {
      email = make_shared<string>(boost::any_cast<string>(m["email"]));
    }
    if (m.find("nick_name") != m.end() && !m["nick_name"].empty()) {
      nickName = make_shared<string>(boost::any_cast<string>(m["nick_name"]));
    }
    if (m.find("phone") != m.end() && !m["phone"].empty()) {
      phone = make_shared<string>(boost::any_cast<string>(m["phone"]));
    }
    if (m.find("role") != m.end() && !m["role"].empty()) {
      role = make_shared<string>(boost::any_cast<string>(m["role"]));
    }
    if (m.find("status") != m.end() && !m["status"].empty()) {
      status = make_shared<string>(boost::any_cast<string>(m["status"]));
    }
    if (m.find("user_data") != m.end() && !m["user_data"].empty()) {
      map<string, boost::any> map1 = boost::any_cast<map<string, boost::any>>(m["user_data"]);
      map<string, boost::any> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      userData = make_shared<map<string, boost::any>>(toMap1);
    }
    if (m.find("user_id") != m.end() && !m["user_id"].empty()) {
      userId = make_shared<string>(boost::any_cast<string>(m["user_id"]));
    }
  }


  ~UpdateUserRequest() = default;
};
class CreateStoryResponse : public Darabonba::Model {
public:
  shared_ptr<string> driveId{};

  CreateStoryResponse() {}

  explicit CreateStoryResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
  }


  ~CreateStoryResponse() = default;
};
class CreateStoryModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<CreateStoryResponse> body{};

  CreateStoryModel() {}

  explicit CreateStoryModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        CreateStoryResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<CreateStoryResponse>(model1);
      }
    }
  }


  ~CreateStoryModel() = default;
};
class GetImageCountResponse : public Darabonba::Model {
public:
  shared_ptr<long> imageCount{};

  GetImageCountResponse() {}

  explicit GetImageCountResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (imageCount) {
      res["image_count"] = boost::any(*imageCount);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("image_count") != m.end() && !m["image_count"].empty()) {
      imageCount = make_shared<long>(boost::any_cast<long>(m["image_count"]));
    }
  }


  ~GetImageCountResponse() = default;
};
class GetPhotoCountModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<GetImageCountResponse> body{};

  GetPhotoCountModel() {}

  explicit GetPhotoCountModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        GetImageCountResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<GetImageCountResponse>(model1);
      }
    }
  }


  ~GetPhotoCountModel() = default;
};
class GetStoryDetailResponse : public Darabonba::Model {
public:
  shared_ptr<string> coverFileId{};
  shared_ptr<string> createdAt{};
  shared_ptr<vector<BaseFileResponse>> items{};
  shared_ptr<double> score{};
  shared_ptr<string> storyId{};
  shared_ptr<vector<int>> storyImagesDateRange{};
  shared_ptr<string> subTitle{};
  shared_ptr<string> title{};
  shared_ptr<string> updatedAt{};
  shared_ptr<string> videoStatus{};
  shared_ptr<string> videoUrl{};

  GetStoryDetailResponse() {}

  explicit GetStoryDetailResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (coverFileId) {
      res["cover_file_id"] = boost::any(*coverFileId);
    }
    if (createdAt) {
      res["created_at"] = boost::any(*createdAt);
    }
    if (items) {
      vector<boost::any> temp1;
      for(auto item1:*items){
        temp1.push_back(boost::any(item1.toMap()));
      }
      res["items"] = boost::any(temp1);
    }
    if (score) {
      res["score"] = boost::any(*score);
    }
    if (storyId) {
      res["story_id"] = boost::any(*storyId);
    }
    if (storyImagesDateRange) {
      res["story_images_date_range"] = boost::any(*storyImagesDateRange);
    }
    if (subTitle) {
      res["sub_title"] = boost::any(*subTitle);
    }
    if (title) {
      res["title"] = boost::any(*title);
    }
    if (updatedAt) {
      res["updated_at"] = boost::any(*updatedAt);
    }
    if (videoStatus) {
      res["video_status"] = boost::any(*videoStatus);
    }
    if (videoUrl) {
      res["video_url"] = boost::any(*videoUrl);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("cover_file_id") != m.end() && !m["cover_file_id"].empty()) {
      coverFileId = make_shared<string>(boost::any_cast<string>(m["cover_file_id"]));
    }
    if (m.find("created_at") != m.end() && !m["created_at"].empty()) {
      createdAt = make_shared<string>(boost::any_cast<string>(m["created_at"]));
    }
    if (m.find("items") != m.end() && !m["items"].empty()) {
      if (typeid(vector<boost::any>).name() == m["items"].type().name()) {
        vector<BaseFileResponse> expect1;
        for(auto item1:boost::any_cast<vector<boost::any>>(m["items"])){
          if (typeid(map<string, boost::any>).name() == item1.type().name()) {
            BaseFileResponse model2;
            model2.fromMap(boost::any_cast<map<string, boost::any>>(item1));
            expect1.push_back(model2);
          }
        }
        items = make_shared<vector<BaseFileResponse>>(expect1);
      }
    }
    if (m.find("score") != m.end() && !m["score"].empty()) {
      score = make_shared<double>(boost::any_cast<double>(m["score"]));
    }
    if (m.find("story_id") != m.end() && !m["story_id"].empty()) {
      storyId = make_shared<string>(boost::any_cast<string>(m["story_id"]));
    }
    if (m.find("story_images_date_range") != m.end() && !m["story_images_date_range"].empty()) {
      vector<int> toVec1;
      if (typeid(vector<boost::any>).name() == m["story_images_date_range"].type().name()) {
        vector<boost::any> vec1 = boost::any_cast<vector<boost::any>>(m["story_images_date_range"]);
        for (auto item:vec1) {
           toVec1.push_back(boost::any_cast<int>(item));
        }
      }
      storyImagesDateRange = make_shared<vector<int>>(toVec1);
    }
    if (m.find("sub_title") != m.end() && !m["sub_title"].empty()) {
      subTitle = make_shared<string>(boost::any_cast<string>(m["sub_title"]));
    }
    if (m.find("title") != m.end() && !m["title"].empty()) {
      title = make_shared<string>(boost::any_cast<string>(m["title"]));
    }
    if (m.find("updated_at") != m.end() && !m["updated_at"].empty()) {
      updatedAt = make_shared<string>(boost::any_cast<string>(m["updated_at"]));
    }
    if (m.find("video_status") != m.end() && !m["video_status"].empty()) {
      videoStatus = make_shared<string>(boost::any_cast<string>(m["video_status"]));
    }
    if (m.find("video_url") != m.end() && !m["video_url"].empty()) {
      videoUrl = make_shared<string>(boost::any_cast<string>(m["video_url"]));
    }
  }


  ~GetStoryDetailResponse() = default;
};
class GetStoryDetailModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<GetStoryDetailResponse> body{};

  GetStoryDetailModel() {}

  explicit GetStoryDetailModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        GetStoryDetailResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<GetStoryDetailResponse>(model1);
      }
    }
  }


  ~GetStoryDetailModel() = default;
};
class GetStoryTaskResponse : public Darabonba::Model {
public:
  shared_ptr<string> driveId{};
  shared_ptr<string> status{};

  GetStoryTaskResponse() {}

  explicit GetStoryTaskResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (status) {
      res["status"] = boost::any(*status);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("status") != m.end() && !m["status"].empty()) {
      status = make_shared<string>(boost::any_cast<string>(m["status"]));
    }
  }


  ~GetStoryTaskResponse() = default;
};
class GetStoryTaskModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<GetStoryTaskResponse> body{};

  GetStoryTaskModel() {}

  explicit GetStoryTaskModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        GetStoryTaskResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<GetStoryTaskResponse>(model1);
      }
    }
  }


  ~GetStoryTaskModel() = default;
};
class Address : public Darabonba::Model {
public:
  shared_ptr<string> city{};
  shared_ptr<string> country{};
  shared_ptr<string> district{};
  shared_ptr<string> province{};
  shared_ptr<string> township{};

  Address() {}

  explicit Address(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (city) {
      res["city"] = boost::any(*city);
    }
    if (country) {
      res["country"] = boost::any(*country);
    }
    if (district) {
      res["district"] = boost::any(*district);
    }
    if (province) {
      res["province"] = boost::any(*province);
    }
    if (township) {
      res["township"] = boost::any(*township);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("city") != m.end() && !m["city"].empty()) {
      city = make_shared<string>(boost::any_cast<string>(m["city"]));
    }
    if (m.find("country") != m.end() && !m["country"].empty()) {
      country = make_shared<string>(boost::any_cast<string>(m["country"]));
    }
    if (m.find("district") != m.end() && !m["district"].empty()) {
      district = make_shared<string>(boost::any_cast<string>(m["district"]));
    }
    if (m.find("province") != m.end() && !m["province"].empty()) {
      province = make_shared<string>(boost::any_cast<string>(m["province"]));
    }
    if (m.find("township") != m.end() && !m["township"].empty()) {
      township = make_shared<string>(boost::any_cast<string>(m["township"]));
    }
  }


  ~Address() = default;
};
class ImageAddressResponse : public Darabonba::Model {
public:
  shared_ptr<Address> addressDetail{};
  shared_ptr<long> count{};
  shared_ptr<string> coverFileId{};
  shared_ptr<string> coverUrl{};
  shared_ptr<string> location{};
  shared_ptr<string> name{};

  ImageAddressResponse() {}

  explicit ImageAddressResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (addressDetail) {
      res["address_detail"] = addressDetail ? boost::any(addressDetail->toMap()) : boost::any(map<string,boost::any>({}));
    }
    if (count) {
      res["count"] = boost::any(*count);
    }
    if (coverFileId) {
      res["cover_file_id"] = boost::any(*coverFileId);
    }
    if (coverUrl) {
      res["cover_url"] = boost::any(*coverUrl);
    }
    if (location) {
      res["location"] = boost::any(*location);
    }
    if (name) {
      res["name"] = boost::any(*name);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("address_detail") != m.end() && !m["address_detail"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["address_detail"].type().name()) {
        Address model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["address_detail"]));
        addressDetail = make_shared<Address>(model1);
      }
    }
    if (m.find("count") != m.end() && !m["count"].empty()) {
      count = make_shared<long>(boost::any_cast<long>(m["count"]));
    }
    if (m.find("cover_file_id") != m.end() && !m["cover_file_id"].empty()) {
      coverFileId = make_shared<string>(boost::any_cast<string>(m["cover_file_id"]));
    }
    if (m.find("cover_url") != m.end() && !m["cover_url"].empty()) {
      coverUrl = make_shared<string>(boost::any_cast<string>(m["cover_url"]));
    }
    if (m.find("location") != m.end() && !m["location"].empty()) {
      location = make_shared<string>(boost::any_cast<string>(m["location"]));
    }
    if (m.find("name") != m.end() && !m["name"].empty()) {
      name = make_shared<string>(boost::any_cast<string>(m["name"]));
    }
  }


  ~ImageAddressResponse() = default;
};
class ListImageAddressGroupsResponse : public Darabonba::Model {
public:
  shared_ptr<vector<ImageAddressResponse>> items{};
  shared_ptr<string> nextMarker{};

  ListImageAddressGroupsResponse() {}

  explicit ListImageAddressGroupsResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (items) {
      vector<boost::any> temp1;
      for(auto item1:*items){
        temp1.push_back(boost::any(item1.toMap()));
      }
      res["items"] = boost::any(temp1);
    }
    if (nextMarker) {
      res["next_marker"] = boost::any(*nextMarker);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("items") != m.end() && !m["items"].empty()) {
      if (typeid(vector<boost::any>).name() == m["items"].type().name()) {
        vector<ImageAddressResponse> expect1;
        for(auto item1:boost::any_cast<vector<boost::any>>(m["items"])){
          if (typeid(map<string, boost::any>).name() == item1.type().name()) {
            ImageAddressResponse model2;
            model2.fromMap(boost::any_cast<map<string, boost::any>>(item1));
            expect1.push_back(model2);
          }
        }
        items = make_shared<vector<ImageAddressResponse>>(expect1);
      }
    }
    if (m.find("next_marker") != m.end() && !m["next_marker"].empty()) {
      nextMarker = make_shared<string>(boost::any_cast<string>(m["next_marker"]));
    }
  }


  ~ListImageAddressGroupsResponse() = default;
};
class ListAddressGroupsModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<ListImageAddressGroupsResponse> body{};

  ListAddressGroupsModel() {}

  explicit ListAddressGroupsModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        ListImageAddressGroupsResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<ListImageAddressGroupsResponse>(model1);
      }
    }
  }


  ~ListAddressGroupsModel() = default;
};
class ImageFaceGroupResponse : public Darabonba::Model {
public:
  shared_ptr<string> coverFileId{};
  shared_ptr<string> createdAt{};
  shared_ptr<long> faceCount{};
  shared_ptr<string> groupCoverUrl{};
  shared_ptr<string> groupId{};
  shared_ptr<string> groupName{};
  shared_ptr<long> imageCount{};
  shared_ptr<string> updatedAt{};

  ImageFaceGroupResponse() {}

  explicit ImageFaceGroupResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (coverFileId) {
      res["cover_file_id"] = boost::any(*coverFileId);
    }
    if (createdAt) {
      res["created_at"] = boost::any(*createdAt);
    }
    if (faceCount) {
      res["face_count"] = boost::any(*faceCount);
    }
    if (groupCoverUrl) {
      res["group_cover_url"] = boost::any(*groupCoverUrl);
    }
    if (groupId) {
      res["group_id"] = boost::any(*groupId);
    }
    if (groupName) {
      res["group_name"] = boost::any(*groupName);
    }
    if (imageCount) {
      res["image_count"] = boost::any(*imageCount);
    }
    if (updatedAt) {
      res["updated_at"] = boost::any(*updatedAt);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("cover_file_id") != m.end() && !m["cover_file_id"].empty()) {
      coverFileId = make_shared<string>(boost::any_cast<string>(m["cover_file_id"]));
    }
    if (m.find("created_at") != m.end() && !m["created_at"].empty()) {
      createdAt = make_shared<string>(boost::any_cast<string>(m["created_at"]));
    }
    if (m.find("face_count") != m.end() && !m["face_count"].empty()) {
      faceCount = make_shared<long>(boost::any_cast<long>(m["face_count"]));
    }
    if (m.find("group_cover_url") != m.end() && !m["group_cover_url"].empty()) {
      groupCoverUrl = make_shared<string>(boost::any_cast<string>(m["group_cover_url"]));
    }
    if (m.find("group_id") != m.end() && !m["group_id"].empty()) {
      groupId = make_shared<string>(boost::any_cast<string>(m["group_id"]));
    }
    if (m.find("group_name") != m.end() && !m["group_name"].empty()) {
      groupName = make_shared<string>(boost::any_cast<string>(m["group_name"]));
    }
    if (m.find("image_count") != m.end() && !m["image_count"].empty()) {
      imageCount = make_shared<long>(boost::any_cast<long>(m["image_count"]));
    }
    if (m.find("updated_at") != m.end() && !m["updated_at"].empty()) {
      updatedAt = make_shared<string>(boost::any_cast<string>(m["updated_at"]));
    }
  }


  ~ImageFaceGroupResponse() = default;
};
class ListImageFaceGroupsResponse : public Darabonba::Model {
public:
  shared_ptr<vector<ImageFaceGroupResponse>> items{};
  shared_ptr<string> nextMarker{};

  ListImageFaceGroupsResponse() {}

  explicit ListImageFaceGroupsResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (items) {
      vector<boost::any> temp1;
      for(auto item1:*items){
        temp1.push_back(boost::any(item1.toMap()));
      }
      res["items"] = boost::any(temp1);
    }
    if (nextMarker) {
      res["next_marker"] = boost::any(*nextMarker);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("items") != m.end() && !m["items"].empty()) {
      if (typeid(vector<boost::any>).name() == m["items"].type().name()) {
        vector<ImageFaceGroupResponse> expect1;
        for(auto item1:boost::any_cast<vector<boost::any>>(m["items"])){
          if (typeid(map<string, boost::any>).name() == item1.type().name()) {
            ImageFaceGroupResponse model2;
            model2.fromMap(boost::any_cast<map<string, boost::any>>(item1));
            expect1.push_back(model2);
          }
        }
        items = make_shared<vector<ImageFaceGroupResponse>>(expect1);
      }
    }
    if (m.find("next_marker") != m.end() && !m["next_marker"].empty()) {
      nextMarker = make_shared<string>(boost::any_cast<string>(m["next_marker"]));
    }
  }


  ~ListImageFaceGroupsResponse() = default;
};
class ListFaceGroupsModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<ListImageFaceGroupsResponse> body{};

  ListFaceGroupsModel() {}

  explicit ListFaceGroupsModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        ListImageFaceGroupsResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<ListImageFaceGroupsResponse>(model1);
      }
    }
  }


  ~ListFaceGroupsModel() = default;
};
class StoryResponse : public Darabonba::Model {
public:
  shared_ptr<string> coverFileId{};
  shared_ptr<string> createdAt{};
  shared_ptr<double> score{};
  shared_ptr<string> storyId{};
  shared_ptr<vector<int>> storyImagesDateRange{};
  shared_ptr<string> subTitle{};
  shared_ptr<string> title{};
  shared_ptr<string> updatedAt{};
  shared_ptr<string> videoStatus{};
  shared_ptr<string> videoUrl{};

  StoryResponse() {}

  explicit StoryResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (coverFileId) {
      res["cover_file_id"] = boost::any(*coverFileId);
    }
    if (createdAt) {
      res["created_at"] = boost::any(*createdAt);
    }
    if (score) {
      res["score"] = boost::any(*score);
    }
    if (storyId) {
      res["story_id"] = boost::any(*storyId);
    }
    if (storyImagesDateRange) {
      res["story_images_date_range"] = boost::any(*storyImagesDateRange);
    }
    if (subTitle) {
      res["sub_title"] = boost::any(*subTitle);
    }
    if (title) {
      res["title"] = boost::any(*title);
    }
    if (updatedAt) {
      res["updated_at"] = boost::any(*updatedAt);
    }
    if (videoStatus) {
      res["video_status"] = boost::any(*videoStatus);
    }
    if (videoUrl) {
      res["video_url"] = boost::any(*videoUrl);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("cover_file_id") != m.end() && !m["cover_file_id"].empty()) {
      coverFileId = make_shared<string>(boost::any_cast<string>(m["cover_file_id"]));
    }
    if (m.find("created_at") != m.end() && !m["created_at"].empty()) {
      createdAt = make_shared<string>(boost::any_cast<string>(m["created_at"]));
    }
    if (m.find("score") != m.end() && !m["score"].empty()) {
      score = make_shared<double>(boost::any_cast<double>(m["score"]));
    }
    if (m.find("story_id") != m.end() && !m["story_id"].empty()) {
      storyId = make_shared<string>(boost::any_cast<string>(m["story_id"]));
    }
    if (m.find("story_images_date_range") != m.end() && !m["story_images_date_range"].empty()) {
      vector<int> toVec1;
      if (typeid(vector<boost::any>).name() == m["story_images_date_range"].type().name()) {
        vector<boost::any> vec1 = boost::any_cast<vector<boost::any>>(m["story_images_date_range"]);
        for (auto item:vec1) {
           toVec1.push_back(boost::any_cast<int>(item));
        }
      }
      storyImagesDateRange = make_shared<vector<int>>(toVec1);
    }
    if (m.find("sub_title") != m.end() && !m["sub_title"].empty()) {
      subTitle = make_shared<string>(boost::any_cast<string>(m["sub_title"]));
    }
    if (m.find("title") != m.end() && !m["title"].empty()) {
      title = make_shared<string>(boost::any_cast<string>(m["title"]));
    }
    if (m.find("updated_at") != m.end() && !m["updated_at"].empty()) {
      updatedAt = make_shared<string>(boost::any_cast<string>(m["updated_at"]));
    }
    if (m.find("video_status") != m.end() && !m["video_status"].empty()) {
      videoStatus = make_shared<string>(boost::any_cast<string>(m["video_status"]));
    }
    if (m.find("video_url") != m.end() && !m["video_url"].empty()) {
      videoUrl = make_shared<string>(boost::any_cast<string>(m["video_url"]));
    }
  }


  ~StoryResponse() = default;
};
class ListStoryResponse : public Darabonba::Model {
public:
  shared_ptr<vector<StoryResponse>> items{};
  shared_ptr<string> nextMarker{};

  ListStoryResponse() {}

  explicit ListStoryResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (items) {
      vector<boost::any> temp1;
      for(auto item1:*items){
        temp1.push_back(boost::any(item1.toMap()));
      }
      res["items"] = boost::any(temp1);
    }
    if (nextMarker) {
      res["next_marker"] = boost::any(*nextMarker);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("items") != m.end() && !m["items"].empty()) {
      if (typeid(vector<boost::any>).name() == m["items"].type().name()) {
        vector<StoryResponse> expect1;
        for(auto item1:boost::any_cast<vector<boost::any>>(m["items"])){
          if (typeid(map<string, boost::any>).name() == item1.type().name()) {
            StoryResponse model2;
            model2.fromMap(boost::any_cast<map<string, boost::any>>(item1));
            expect1.push_back(model2);
          }
        }
        items = make_shared<vector<StoryResponse>>(expect1);
      }
    }
    if (m.find("next_marker") != m.end() && !m["next_marker"].empty()) {
      nextMarker = make_shared<string>(boost::any_cast<string>(m["next_marker"]));
    }
  }


  ~ListStoryResponse() = default;
};
class ListStoryModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<ListStoryResponse> body{};

  ListStoryModel() {}

  explicit ListStoryModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        ListStoryResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<ListStoryResponse>(model1);
      }
    }
  }


  ~ListStoryModel() = default;
};
class ImageTagResponse : public Darabonba::Model {
public:
  shared_ptr<long> count{};
  shared_ptr<string> coverFileId{};
  shared_ptr<string> coverUrl{};
  shared_ptr<string> name{};

  ImageTagResponse() {}

  explicit ImageTagResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (count) {
      res["count"] = boost::any(*count);
    }
    if (coverFileId) {
      res["cover_file_id"] = boost::any(*coverFileId);
    }
    if (coverUrl) {
      res["cover_url"] = boost::any(*coverUrl);
    }
    if (name) {
      res["name"] = boost::any(*name);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("count") != m.end() && !m["count"].empty()) {
      count = make_shared<long>(boost::any_cast<long>(m["count"]));
    }
    if (m.find("cover_file_id") != m.end() && !m["cover_file_id"].empty()) {
      coverFileId = make_shared<string>(boost::any_cast<string>(m["cover_file_id"]));
    }
    if (m.find("cover_url") != m.end() && !m["cover_url"].empty()) {
      coverUrl = make_shared<string>(boost::any_cast<string>(m["cover_url"]));
    }
    if (m.find("name") != m.end() && !m["name"].empty()) {
      name = make_shared<string>(boost::any_cast<string>(m["name"]));
    }
  }


  ~ImageTagResponse() = default;
};
class ListImageTagsResponse : public Darabonba::Model {
public:
  shared_ptr<vector<ImageTagResponse>> tags{};

  ListImageTagsResponse() {}

  explicit ListImageTagsResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (tags) {
      vector<boost::any> temp1;
      for(auto item1:*tags){
        temp1.push_back(boost::any(item1.toMap()));
      }
      res["tags"] = boost::any(temp1);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("tags") != m.end() && !m["tags"].empty()) {
      if (typeid(vector<boost::any>).name() == m["tags"].type().name()) {
        vector<ImageTagResponse> expect1;
        for(auto item1:boost::any_cast<vector<boost::any>>(m["tags"])){
          if (typeid(map<string, boost::any>).name() == item1.type().name()) {
            ImageTagResponse model2;
            model2.fromMap(boost::any_cast<map<string, boost::any>>(item1));
            expect1.push_back(model2);
          }
        }
        tags = make_shared<vector<ImageTagResponse>>(expect1);
      }
    }
  }


  ~ListImageTagsResponse() = default;
};
class ListTagsModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<ListImageTagsResponse> body{};

  ListTagsModel() {}

  explicit ListTagsModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        ListImageTagsResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<ListImageTagsResponse>(model1);
      }
    }
  }


  ~ListTagsModel() = default;
};
class SearchImageAddressGroupsResponse : public Darabonba::Model {
public:
  shared_ptr<vector<ImageAddressResponse>> items{};

  SearchImageAddressGroupsResponse() {}

  explicit SearchImageAddressGroupsResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (items) {
      vector<boost::any> temp1;
      for(auto item1:*items){
        temp1.push_back(boost::any(item1.toMap()));
      }
      res["items"] = boost::any(temp1);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("items") != m.end() && !m["items"].empty()) {
      if (typeid(vector<boost::any>).name() == m["items"].type().name()) {
        vector<ImageAddressResponse> expect1;
        for(auto item1:boost::any_cast<vector<boost::any>>(m["items"])){
          if (typeid(map<string, boost::any>).name() == item1.type().name()) {
            ImageAddressResponse model2;
            model2.fromMap(boost::any_cast<map<string, boost::any>>(item1));
            expect1.push_back(model2);
          }
        }
        items = make_shared<vector<ImageAddressResponse>>(expect1);
      }
    }
  }


  ~SearchImageAddressGroupsResponse() = default;
};
class SearchAddressGroupsModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<SearchImageAddressGroupsResponse> body{};

  SearchAddressGroupsModel() {}

  explicit SearchAddressGroupsModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        SearchImageAddressGroupsResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<SearchImageAddressGroupsResponse>(model1);
      }
    }
  }


  ~SearchAddressGroupsModel() = default;
};
class UpdateFaceGroupInfoResponse : public Darabonba::Model {
public:
  shared_ptr<string> driveId{};
  shared_ptr<string> groupId{};

  UpdateFaceGroupInfoResponse() {}

  explicit UpdateFaceGroupInfoResponse(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (groupId) {
      res["group_id"] = boost::any(*groupId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("group_id") != m.end() && !m["group_id"].empty()) {
      groupId = make_shared<string>(boost::any_cast<string>(m["group_id"]));
    }
  }


  ~UpdateFaceGroupInfoResponse() = default;
};
class UpdateFacegroupInfoModel : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<UpdateFaceGroupInfoResponse> body{};

  UpdateFacegroupInfoModel() {}

  explicit UpdateFacegroupInfoModel(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!body) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("body is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (body) {
      res["body"] = body ? boost::any(body->toMap()) : boost::any(map<string,boost::any>({}));
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("body") != m.end() && !m["body"].empty()) {
      if (typeid(map<string, boost::any>).name() == m["body"].type().name()) {
        UpdateFaceGroupInfoResponse model1;
        model1.fromMap(boost::any_cast<map<string, boost::any>>(m["body"]));
        body = make_shared<UpdateFaceGroupInfoResponse>(model1);
      }
    }
  }


  ~UpdateFacegroupInfoModel() = default;
};
class CreateStoryRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<string> driveId{};

  CreateStoryRequest() {}

  explicit CreateStoryRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!driveId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("driveId is required.")));
    }
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
  }


  ~CreateStoryRequest() = default;
};
class GetImageCountRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<string> driveId{};

  GetImageCountRequest() {}

  explicit GetImageCountRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!driveId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("driveId is required.")));
    }
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
  }


  ~GetImageCountRequest() = default;
};
class GetStoryDetailRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<string> driveId{};
  shared_ptr<string> storyId{};
  shared_ptr<long> videoUrlExpireSec{};

  GetStoryDetailRequest() {}

  explicit GetStoryDetailRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!driveId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("driveId is required.")));
    }
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    if (!storyId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("storyId is required.")));
    }
    if (videoUrlExpireSec && *videoUrlExpireSec > 14400) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("videoUrlExpireSec is required.")));
    }
    if (videoUrlExpireSec && *videoUrlExpireSec < 10) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("videoUrlExpireSec is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (storyId) {
      res["story_id"] = boost::any(*storyId);
    }
    if (videoUrlExpireSec) {
      res["video_url_expire_sec"] = boost::any(*videoUrlExpireSec);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("story_id") != m.end() && !m["story_id"].empty()) {
      storyId = make_shared<string>(boost::any_cast<string>(m["story_id"]));
    }
    if (m.find("video_url_expire_sec") != m.end() && !m["video_url_expire_sec"].empty()) {
      videoUrlExpireSec = make_shared<long>(boost::any_cast<long>(m["video_url_expire_sec"]));
    }
  }


  ~GetStoryDetailRequest() = default;
};
class GetStoryTaskRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<string> driveId{};

  GetStoryTaskRequest() {}

  explicit GetStoryTaskRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!driveId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("driveId is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
  }


  ~GetStoryTaskRequest() = default;
};
class ListImageAddressGroupsRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<string> driveId{};
  shared_ptr<string> imageThumbnailProcess{};
  shared_ptr<long> limit{};
  shared_ptr<string> marker{};

  ListImageAddressGroupsRequest() {}

  explicit ListImageAddressGroupsRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!driveId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("driveId is required.")));
    }
    if (limit && *limit > 100) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("limit is required.")));
    }
    if (limit && *limit < 1) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("limit is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (imageThumbnailProcess) {
      res["image_thumbnail_process"] = boost::any(*imageThumbnailProcess);
    }
    if (limit) {
      res["limit"] = boost::any(*limit);
    }
    if (marker) {
      res["marker"] = boost::any(*marker);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("image_thumbnail_process") != m.end() && !m["image_thumbnail_process"].empty()) {
      imageThumbnailProcess = make_shared<string>(boost::any_cast<string>(m["image_thumbnail_process"]));
    }
    if (m.find("limit") != m.end() && !m["limit"].empty()) {
      limit = make_shared<long>(boost::any_cast<long>(m["limit"]));
    }
    if (m.find("marker") != m.end() && !m["marker"].empty()) {
      marker = make_shared<string>(boost::any_cast<string>(m["marker"]));
    }
  }


  ~ListImageAddressGroupsRequest() = default;
};
class ListImageFaceGroupsRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<string> driveId{};
  shared_ptr<long> limit{};
  shared_ptr<string> marker{};

  ListImageFaceGroupsRequest() {}

  explicit ListImageFaceGroupsRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!driveId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("driveId is required.")));
    }
    if (limit && *limit > 100) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("limit is required.")));
    }
    if (limit && *limit < 1) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("limit is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (limit) {
      res["limit"] = boost::any(*limit);
    }
    if (marker) {
      res["marker"] = boost::any(*marker);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("limit") != m.end() && !m["limit"].empty()) {
      limit = make_shared<long>(boost::any_cast<long>(m["limit"]));
    }
    if (m.find("marker") != m.end() && !m["marker"].empty()) {
      marker = make_shared<string>(boost::any_cast<string>(m["marker"]));
    }
  }


  ~ListImageFaceGroupsRequest() = default;
};
class ListImageTagsRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<string> driveId{};
  shared_ptr<string> imageThumbnailProcess{};

  ListImageTagsRequest() {}

  explicit ListImageTagsRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!driveId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("driveId is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (imageThumbnailProcess) {
      res["image_thumbnail_process"] = boost::any(*imageThumbnailProcess);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("image_thumbnail_process") != m.end() && !m["image_thumbnail_process"].empty()) {
      imageThumbnailProcess = make_shared<string>(boost::any_cast<string>(m["image_thumbnail_process"]));
    }
  }


  ~ListImageTagsRequest() = default;
};
class ListStoryRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<string> driveId{};
  shared_ptr<long> limit{};
  shared_ptr<string> marker{};

  ListStoryRequest() {}

  explicit ListStoryRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!driveId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("driveId is required.")));
    }
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    if (limit && *limit > 100) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("limit is required.")));
    }
    if (limit && *limit < 1) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("limit is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (limit) {
      res["limit"] = boost::any(*limit);
    }
    if (marker) {
      res["marker"] = boost::any(*marker);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("limit") != m.end() && !m["limit"].empty()) {
      limit = make_shared<long>(boost::any_cast<long>(m["limit"]));
    }
    if (m.find("marker") != m.end() && !m["marker"].empty()) {
      marker = make_shared<string>(boost::any_cast<string>(m["marker"]));
    }
  }


  ~ListStoryRequest() = default;
};
class RemoveStoryImagesRequest : public Darabonba::Model {
public:
  shared_ptr<string> driveId{};
  shared_ptr<vector<string>> fileIds{};
  shared_ptr<string> storyId{};

  RemoveStoryImagesRequest() {}

  explicit RemoveStoryImagesRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {}

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (fileIds) {
      res["file_ids"] = boost::any(*fileIds);
    }
    if (storyId) {
      res["story_id"] = boost::any(*storyId);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("file_ids") != m.end() && !m["file_ids"].empty()) {
      vector<string> toVec1;
      if (typeid(vector<boost::any>).name() == m["file_ids"].type().name()) {
        vector<boost::any> vec1 = boost::any_cast<vector<boost::any>>(m["file_ids"]);
        for (auto item:vec1) {
           toVec1.push_back(boost::any_cast<string>(item));
        }
      }
      fileIds = make_shared<vector<string>>(toVec1);
    }
    if (m.find("story_id") != m.end() && !m["story_id"].empty()) {
      storyId = make_shared<string>(boost::any_cast<string>(m["story_id"]));
    }
  }


  ~RemoveStoryImagesRequest() = default;
};
class SearchImageAddressGroupsRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<string> addressLevel{};
  shared_ptr<vector<string>> addressNames{};
  shared_ptr<string> brGeoPoint{};
  shared_ptr<string> driveId{};
  shared_ptr<string> imageThumbnailProcess{};
  shared_ptr<string> tlGeoPoint{};

  SearchImageAddressGroupsRequest() {}

  explicit SearchImageAddressGroupsRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!driveId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("driveId is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (addressLevel) {
      res["address_level"] = boost::any(*addressLevel);
    }
    if (addressNames) {
      res["address_names"] = boost::any(*addressNames);
    }
    if (brGeoPoint) {
      res["br_geo_point"] = boost::any(*brGeoPoint);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (imageThumbnailProcess) {
      res["image_thumbnail_process"] = boost::any(*imageThumbnailProcess);
    }
    if (tlGeoPoint) {
      res["tl_geo_point"] = boost::any(*tlGeoPoint);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("address_level") != m.end() && !m["address_level"].empty()) {
      addressLevel = make_shared<string>(boost::any_cast<string>(m["address_level"]));
    }
    if (m.find("address_names") != m.end() && !m["address_names"].empty()) {
      vector<string> toVec1;
      if (typeid(vector<boost::any>).name() == m["address_names"].type().name()) {
        vector<boost::any> vec1 = boost::any_cast<vector<boost::any>>(m["address_names"]);
        for (auto item:vec1) {
           toVec1.push_back(boost::any_cast<string>(item));
        }
      }
      addressNames = make_shared<vector<string>>(toVec1);
    }
    if (m.find("br_geo_point") != m.end() && !m["br_geo_point"].empty()) {
      brGeoPoint = make_shared<string>(boost::any_cast<string>(m["br_geo_point"]));
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("image_thumbnail_process") != m.end() && !m["image_thumbnail_process"].empty()) {
      imageThumbnailProcess = make_shared<string>(boost::any_cast<string>(m["image_thumbnail_process"]));
    }
    if (m.find("tl_geo_point") != m.end() && !m["tl_geo_point"].empty()) {
      tlGeoPoint = make_shared<string>(boost::any_cast<string>(m["tl_geo_point"]));
    }
  }


  ~SearchImageAddressGroupsRequest() = default;
};
class UpdateFaceGroupInfoRequest : public Darabonba::Model {
public:
  shared_ptr<map<string, string>> headers{};
  shared_ptr<string> driveId{};
  shared_ptr<string> groupId{};
  shared_ptr<string> groupName{};

  UpdateFaceGroupInfoRequest() {}

  explicit UpdateFaceGroupInfoRequest(const std::map<string, boost::any> &config) : Darabonba::Model(config) {
    fromMap(config);
  };

  void validate() override {
    if (!driveId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("driveId is required.")));
    }
    Darabonba::Model::validatePattern("driveId", driveId, "[0-9]+");
    if (!groupId) {
      BOOST_THROW_EXCEPTION(boost::enable_error_info(std::runtime_error("groupId is required.")));
    }
  }

  map<string, boost::any> toMap() override {
    map<string, boost::any> res;
    if (headers) {
      res["headers"] = boost::any(*headers);
    }
    if (driveId) {
      res["drive_id"] = boost::any(*driveId);
    }
    if (groupId) {
      res["group_id"] = boost::any(*groupId);
    }
    if (groupName) {
      res["group_name"] = boost::any(*groupName);
    }
    return res;
  }

  void fromMap(map<string, boost::any> m) override {
    if (m.find("headers") != m.end() && !m["headers"].empty()) {
      map<string, string> map1 = boost::any_cast<map<string, string>>(m["headers"]);
      map<string, string> toMap1;
      for (auto item:map1) {
         toMap1[item.first] = item.second;
      }
      headers = make_shared<map<string, string>>(toMap1);
    }
    if (m.find("drive_id") != m.end() && !m["drive_id"].empty()) {
      driveId = make_shared<string>(boost::any_cast<string>(m["drive_id"]));
    }
    if (m.find("group_id") != m.end() && !m["group_id"].empty()) {
      groupId = make_shared<string>(boost::any_cast<string>(m["group_id"]));
    }
    if (m.find("group_name") != m.end() && !m["group_name"].empty()) {
      groupName = make_shared<string>(boost::any_cast<string>(m["group_name"]));
    }
  }


  ~UpdateFaceGroupInfoRequest() = default;
};
class Client {
public:
  shared_ptr<string> _domainId{};
  shared_ptr<Alibabacloud_AccessTokenCredential::Client> _accessTokenCredential{};
  shared_ptr<string> _endpoint{};
  shared_ptr<string> _protocol{};
  shared_ptr<string> _nickname{};
  shared_ptr<string> _userAgent{};
  shared_ptr<Alibabacloud_Credential::Client> _credential{};
  explicit Client(const shared_ptr<Config>& config);
  CancelLinkModel cancelLinkEx(shared_ptr<CancelLinkRequest> request, shared_ptr<RuntimeOptions> runtime);
  ConfirmLinkModel confirmLinkEx(shared_ptr<ConfirmLinkRequest> request, shared_ptr<RuntimeOptions> runtime);
  ChangePasswordModel changePasswordEx(shared_ptr<DefaultChangePasswordRequest> request, shared_ptr<RuntimeOptions> runtime);
  SetPasswordModel setPasswordEx(shared_ptr<DefaultSetPasswordRequest> request, shared_ptr<RuntimeOptions> runtime);
  VerifyCodeModel verifyCodeEx(shared_ptr<VerifyCodeRequest> request, shared_ptr<RuntimeOptions> runtime);
  GetAccessTokenByLinkInfoModel getAccessTokenByLinkInfoEx(shared_ptr<GetAccessTokenByLinkInfoRequest> request, shared_ptr<RuntimeOptions> runtime);
  GetCaptchaModel getCaptchaEx(shared_ptr<GetCaptchaRequest> request, shared_ptr<RuntimeOptions> runtime);
  GetLinkInfoModel getLinkInfoEx(shared_ptr<GetByLinkInfoRequest> request, shared_ptr<RuntimeOptions> runtime);
  GetLinkInfoByUserIdModel getLinkInfoByUserIdEx(shared_ptr<GetLinkInfoByUserIDRequest> request, shared_ptr<RuntimeOptions> runtime);
  GetPublicKeyModel getPublicKeyEx(shared_ptr<GetAppPublicKeyRequest> request, shared_ptr<RuntimeOptions> runtime);
  LinkModel linkEx(shared_ptr<AccountLinkRequest> request, shared_ptr<RuntimeOptions> runtime);
  CheckExistModel checkExistEx(shared_ptr<MobileCheckExistRequest> request, shared_ptr<RuntimeOptions> runtime);
  LoginModel loginEx(shared_ptr<MobileLoginRequest> request, shared_ptr<RuntimeOptions> runtime);
  RegisterModel registerEx(shared_ptr<MobileRegisterRequest> request, shared_ptr<RuntimeOptions> runtime);
  MobileSendSmsCodeModel mobileSendSmsCodeEx(shared_ptr<MobileSendSmsCodeRequest> request, shared_ptr<RuntimeOptions> runtime);
  AccountRevokeModel accountRevokeEx(shared_ptr<RevokeRequest> request, shared_ptr<RuntimeOptions> runtime);
  AccountTokenModel accountTokenEx(shared_ptr<TokenRequest> request, shared_ptr<RuntimeOptions> runtime);
  AdminListStoresModel adminListStoresEx(shared_ptr<AdminListStoresRequest> request, shared_ptr<RuntimeOptions> runtime);
  GetUserAccessTokenModel getUserAccessTokenEx(shared_ptr<GetUserAccessTokenRequest> request, shared_ptr<RuntimeOptions> runtime);
  GetAsyncTaskInfoModel getAsyncTaskInfoEx(shared_ptr<GetAsyncTaskRequest> request, shared_ptr<RuntimeOptions> runtime);
  BatchOperationModel batchOperationEx(shared_ptr<BatchRequest> request, shared_ptr<RuntimeOptions> runtime);
  CreateDriveModel createDriveEx(shared_ptr<CreateDriveRequest> request, shared_ptr<RuntimeOptions> runtime);
  DeleteDriveModel deleteDriveEx(shared_ptr<DeleteDriveRequest> request, shared_ptr<RuntimeOptions> runtime);
  GetDriveModel getDriveEx(shared_ptr<GetDriveRequest> request, shared_ptr<RuntimeOptions> runtime);
  GetDefaultDriveModel getDefaultDriveEx(shared_ptr<GetDefaultDriveRequest> request, shared_ptr<RuntimeOptions> runtime);
  ListDrivesModel listDrivesEx(shared_ptr<ListDriveRequest> request, shared_ptr<RuntimeOptions> runtime);
  ListMyDrivesModel listMyDrivesEx(shared_ptr<ListMyDriveRequest> request, shared_ptr<RuntimeOptions> runtime);
  UpdateDriveModel updateDriveEx(shared_ptr<UpdateDriveRequest> request, shared_ptr<RuntimeOptions> runtime);
  CompleteFileModel completeFileEx(shared_ptr<CompleteFileRequest> request, shared_ptr<RuntimeOptions> runtime);
  CopyFileModel copyFileEx(shared_ptr<CopyFileRequest> request, shared_ptr<RuntimeOptions> runtime);
  CreateFileModel createFileEx(shared_ptr<CreateFileRequest> request, shared_ptr<RuntimeOptions> runtime);
  DeleteFileModel deleteFileEx(shared_ptr<DeleteFileRequest> request, shared_ptr<RuntimeOptions> runtime);
  GetFileModel getFileEx(shared_ptr<GetFileRequest> request, shared_ptr<RuntimeOptions> runtime);
  GetFileByPathModel getFileByPathEx(shared_ptr<GetFileByPathRequest> request, shared_ptr<RuntimeOptions> runtime);
  GetDownloadUrlModel getDownloadUrlEx(shared_ptr<GetDownloadUrlRequest> request, shared_ptr<RuntimeOptions> runtime);
  GetLastCursorModel getLastCursorEx(shared_ptr<GetLastCursorRequest> request, shared_ptr<RuntimeOptions> runtime);
  GetMediaPlayUrlModel getMediaPlayUrlEx(shared_ptr<GetMediaPlayURLRequest> request, shared_ptr<RuntimeOptions> runtime);
  GetOfficePreviewUrlModel getOfficePreviewUrlEx(shared_ptr<GetOfficePreviewUrlRequest> request, shared_ptr<RuntimeOptions> runtime);
  GetUploadUrlModel getUploadUrlEx(shared_ptr<GetUploadUrlRequest> request, shared_ptr<RuntimeOptions> runtime);
  GetVideoPreviewSpriteUrlModel getVideoPreviewSpriteUrlEx(shared_ptr<GetVideoPreviewSpriteURLRequest> request, shared_ptr<RuntimeOptions> runtime);
  GetVideoPreviewUrlModel getVideoPreviewUrlEx(shared_ptr<GetVideoPreviewURLRequest> request, shared_ptr<RuntimeOptions> runtime);
  ListFileModel listFileEx(shared_ptr<ListFileRequest> request, shared_ptr<RuntimeOptions> runtime);
  ListFileByAnonymousModel listFileByAnonymousEx(shared_ptr<ListByAnonymousRequest> request, shared_ptr<RuntimeOptions> runtime);
  ListFileByCustomIndexKeyModel listFileByCustomIndexKeyEx(shared_ptr<ListFileByCustomIndexKeyRequest> request, shared_ptr<RuntimeOptions> runtime);
  ListFileDeltaModel listFileDeltaEx(shared_ptr<ListFileDeltaRequest> request, shared_ptr<RuntimeOptions> runtime);
  ListUploadedPartsModel listUploadedPartsEx(shared_ptr<ListUploadedPartRequest> request, shared_ptr<RuntimeOptions> runtime);
  MoveFileModel moveFileEx(shared_ptr<MoveFileRequest> request, shared_ptr<RuntimeOptions> runtime);
  ScanFileMetaModel scanFileMetaEx(shared_ptr<ScanFileMetaRequest> request, shared_ptr<RuntimeOptions> runtime);
  SearchFileModel searchFileEx(shared_ptr<SearchFileRequest> request, shared_ptr<RuntimeOptions> runtime);
  UpdateFileModel updateFileEx(shared_ptr<UpdateFileMetaRequest> request, shared_ptr<RuntimeOptions> runtime);
  CancelShareLinkModel cancelShareLinkEx(shared_ptr<CancelShareLinkRequest> request, shared_ptr<RuntimeOptions> runtime);
  CreateShareLinkModel createShareLinkEx(shared_ptr<CreateShareLinkRequest> request, shared_ptr<RuntimeOptions> runtime);
  GetShareIdModel getShareIdEx(shared_ptr<GetShareLinkIDRequest> request, shared_ptr<RuntimeOptions> runtime);
  GetShareTokenModel getShareTokenEx(shared_ptr<GetShareLinkTokenRequest> request, shared_ptr<RuntimeOptions> runtime);
  ListShareLinkModel listShareLinkEx(shared_ptr<ListShareLinkRequest> request, shared_ptr<RuntimeOptions> runtime);
  CreateUserModel createUserEx(shared_ptr<CreateUserRequest> request, shared_ptr<RuntimeOptions> runtime);
  DeleteUserModel deleteUserEx(shared_ptr<DeleteUserRequest> request, shared_ptr<RuntimeOptions> runtime);
  GetUserModel getUserEx(shared_ptr<GetUserRequest> request, shared_ptr<RuntimeOptions> runtime);
  ListUsersModel listUsersEx(shared_ptr<ListUserRequest> request, shared_ptr<RuntimeOptions> runtime);
  SearchUserModel searchUserEx(shared_ptr<SearchUserRequest> request, shared_ptr<RuntimeOptions> runtime);
  UpdateUserModel updateUserEx(shared_ptr<UpdateUserRequest> request, shared_ptr<RuntimeOptions> runtime);
  CreateStoryModel createStoryEx(shared_ptr<CreateStoryRequest> request, shared_ptr<RuntimeOptions> runtime);
  GetPhotoCountModel getPhotoCountEx(shared_ptr<GetImageCountRequest> request, shared_ptr<RuntimeOptions> runtime);
  GetStoryDetailModel getStoryDetailEx(shared_ptr<GetStoryDetailRequest> request, shared_ptr<RuntimeOptions> runtime);
  GetStoryTaskModel getStoryTaskEx(shared_ptr<GetStoryTaskRequest> request, shared_ptr<RuntimeOptions> runtime);
  ListAddressGroupsModel listAddressGroupsEx(shared_ptr<ListImageAddressGroupsRequest> request, shared_ptr<RuntimeOptions> runtime);
  ListFaceGroupsModel listFaceGroupsEx(shared_ptr<ListImageFaceGroupsRequest> request, shared_ptr<RuntimeOptions> runtime);
  ListStoryModel listStoryEx(shared_ptr<ListStoryRequest> request, shared_ptr<RuntimeOptions> runtime);
  ListTagsModel listTagsEx(shared_ptr<ListImageTagsRequest> request, shared_ptr<RuntimeOptions> runtime);
  SearchAddressGroupsModel searchAddressGroupsEx(shared_ptr<SearchImageAddressGroupsRequest> request, shared_ptr<RuntimeOptions> runtime);
  UpdateFacegroupInfoModel updateFacegroupInfoEx(shared_ptr<UpdateFaceGroupInfoRequest> request, shared_ptr<RuntimeOptions> runtime);
  CancelLinkModel cancelLink(shared_ptr<CancelLinkRequest> request);
  ConfirmLinkModel confirmLink(shared_ptr<ConfirmLinkRequest> request);
  ChangePasswordModel changePassword(shared_ptr<DefaultChangePasswordRequest> request);
  SetPasswordModel setPassword(shared_ptr<DefaultSetPasswordRequest> request);
  VerifyCodeModel verifyCode(shared_ptr<VerifyCodeRequest> request);
  GetAccessTokenByLinkInfoModel getAccessTokenByLinkInfo(shared_ptr<GetAccessTokenByLinkInfoRequest> request);
  GetCaptchaModel getCaptcha(shared_ptr<GetCaptchaRequest> request);
  GetLinkInfoModel getLinkInfo(shared_ptr<GetByLinkInfoRequest> request);
  GetLinkInfoByUserIdModel getLinkInfoByUserId(shared_ptr<GetLinkInfoByUserIDRequest> request);
  GetPublicKeyModel getPublicKey(shared_ptr<GetAppPublicKeyRequest> request);
  LinkModel link(shared_ptr<AccountLinkRequest> request);
  CheckExistModel checkExist(shared_ptr<MobileCheckExistRequest> request);
  LoginModel login(shared_ptr<MobileLoginRequest> request);
  RegisterModel register_(shared_ptr<MobileRegisterRequest> request);
  MobileSendSmsCodeModel mobileSendSmsCode(shared_ptr<MobileSendSmsCodeRequest> request);
  AccountRevokeModel accountRevoke(shared_ptr<RevokeRequest> request);
  AccountTokenModel accountToken(shared_ptr<TokenRequest> request);
  AdminListStoresModel adminListStores(shared_ptr<AdminListStoresRequest> request);
  GetUserAccessTokenModel getUserAccessToken(shared_ptr<GetUserAccessTokenRequest> request);
  GetAsyncTaskInfoModel getAsyncTaskInfo(shared_ptr<GetAsyncTaskRequest> request);
  BatchOperationModel batchOperation(shared_ptr<BatchRequest> request);
  CreateDriveModel createDrive(shared_ptr<CreateDriveRequest> request);
  DeleteDriveModel deleteDrive(shared_ptr<DeleteDriveRequest> request);
  GetDriveModel getDrive(shared_ptr<GetDriveRequest> request);
  GetDefaultDriveModel getDefaultDrive(shared_ptr<GetDefaultDriveRequest> request);
  ListDrivesModel listDrives(shared_ptr<ListDriveRequest> request);
  ListMyDrivesModel listMyDrives(shared_ptr<ListMyDriveRequest> request);
  UpdateDriveModel updateDrive(shared_ptr<UpdateDriveRequest> request);
  CompleteFileModel completeFile(shared_ptr<CompleteFileRequest> request);
  CopyFileModel copyFile(shared_ptr<CopyFileRequest> request);
  CreateFileModel createFile(shared_ptr<CreateFileRequest> request);
  DeleteFileModel deleteFile(shared_ptr<DeleteFileRequest> request);
  GetFileModel getFile(shared_ptr<GetFileRequest> request);
  GetFileByPathModel getFileByPath(shared_ptr<GetFileByPathRequest> request);
  GetDownloadUrlModel getDownloadUrl(shared_ptr<GetDownloadUrlRequest> request);
  GetLastCursorModel getLastCursor(shared_ptr<GetLastCursorRequest> request);
  GetMediaPlayUrlModel getMediaPlayUrl(shared_ptr<GetMediaPlayURLRequest> request);
  GetOfficePreviewUrlModel getOfficePreviewUrl(shared_ptr<GetOfficePreviewUrlRequest> request);
  GetUploadUrlModel getUploadUrl(shared_ptr<GetUploadUrlRequest> request);
  GetVideoPreviewSpriteUrlModel getVideoPreviewSpriteUrl(shared_ptr<GetVideoPreviewSpriteURLRequest> request);
  GetVideoPreviewUrlModel getVideoPreviewUrl(shared_ptr<GetVideoPreviewURLRequest> request);
  ListFileModel listFile(shared_ptr<ListFileRequest> request);
  ListFileByAnonymousModel listFileByAnonymous(shared_ptr<ListByAnonymousRequest> request);
  ListFileByCustomIndexKeyModel listFileByCustomIndexKey(shared_ptr<ListFileByCustomIndexKeyRequest> request);
  ListFileDeltaModel listFileDelta(shared_ptr<ListFileDeltaRequest> request);
  ListUploadedPartsModel listUploadedParts(shared_ptr<ListUploadedPartRequest> request);
  MoveFileModel moveFile(shared_ptr<MoveFileRequest> request);
  ScanFileMetaModel scanFileMeta(shared_ptr<ScanFileMetaRequest> request);
  SearchFileModel searchFile(shared_ptr<SearchFileRequest> request);
  UpdateFileModel updateFile(shared_ptr<UpdateFileMetaRequest> request);
  CancelShareLinkModel cancelShareLink(shared_ptr<CancelShareLinkRequest> request);
  CreateShareLinkModel createShareLink(shared_ptr<CreateShareLinkRequest> request);
  GetShareIdModel getShareId(shared_ptr<GetShareLinkIDRequest> request);
  GetShareTokenModel getShareToken(shared_ptr<GetShareLinkTokenRequest> request);
  ListShareLinkModel listShareLink(shared_ptr<ListShareLinkRequest> request);
  CreateUserModel createUser(shared_ptr<CreateUserRequest> request);
  DeleteUserModel deleteUser(shared_ptr<DeleteUserRequest> request);
  GetUserModel getUser(shared_ptr<GetUserRequest> request);
  ListUsersModel listUsers(shared_ptr<ListUserRequest> request);
  SearchUserModel searchUser(shared_ptr<SearchUserRequest> request);
  UpdateUserModel updateUser(shared_ptr<UpdateUserRequest> request);
  CreateStoryModel createStory(shared_ptr<CreateStoryRequest> request);
  GetPhotoCountModel getPhotoCount(shared_ptr<GetImageCountRequest> request);
  GetStoryDetailModel getStoryDetail(shared_ptr<GetStoryDetailRequest> request);
  GetStoryTaskModel getStoryTask(shared_ptr<GetStoryTaskRequest> request);
  ListAddressGroupsModel listAddressGroups(shared_ptr<ListImageAddressGroupsRequest> request);
  ListFaceGroupsModel listFaceGroups(shared_ptr<ListImageFaceGroupsRequest> request);
  ListStoryModel listStory(shared_ptr<ListStoryRequest> request);
  ListTagsModel listTags(shared_ptr<ListImageTagsRequest> request);
  SearchAddressGroupsModel searchAddressGroups(shared_ptr<SearchImageAddressGroupsRequest> request);
  UpdateFacegroupInfoModel updateFacegroupInfo(shared_ptr<UpdateFaceGroupInfoRequest> request);
  string getPathname(shared_ptr<string> nickname, shared_ptr<string> path);
  void setExpireTime(shared_ptr<string> expireTime);
  string getExpireTime();
  void setRefreshToken(shared_ptr<string> token);
  string getRefreshToken();
  void setAccessToken(shared_ptr<string> token);
  string getAccessToken();
  void setUserAgent(shared_ptr<string> userAgent);
  void appendUserAgent(shared_ptr<string> userAgent);
  string getUserAgent();
  string getAccessKeyId();
  string getAccessKeySecret();
  string getSecurityToken();

  ~Client() = default;
};
} // namespace Alibabacloud_Pds

#endif
