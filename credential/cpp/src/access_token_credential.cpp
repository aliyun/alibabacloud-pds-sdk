// This file is auto-generated, don't edit it. Thanks.

#include <alibabacloud/access_token_credential.hpp>
#include <boost/throw_exception.hpp>
#include <darabonba/core.hpp>
#include <ctime>
#include <memory>
#include <boost/lexical_cast.hpp>
#include <boost/property_tree/json_parser.hpp>
#include <boost/property_tree/ptree.hpp>
#include <regex>
#include <sstream>
#include <string>
#include <utility>

using namespace std;

using namespace Alibabacloud_AccessTokenCredential;

Alibabacloud_AccessTokenCredential::Client::Client(const shared_ptr<Config> &config) {
  _endpoint = config->endpoint;
  _domainId = config->domainId;
  _clientId = config->clientId;
  _refreshToken = config->refreshToken;
  _clientSecret = config->clientSecret;
  _accessToken = config->accessToken;
  _expireTime = config->expireTime;
};

void Alibabacloud_AccessTokenCredential::Client::setExpireTime(shared_ptr<string> expireTime) {
  _expireTime = std::move(expireTime);
}

string Alibabacloud_AccessTokenCredential::Client::getExpireTime() {
  return *_expireTime;
}

string Alibabacloud_AccessTokenCredential::Client::getRefreshToken() {
  return *_refreshToken;
}

void Alibabacloud_AccessTokenCredential::Client::setRefreshToken(shared_ptr<string> refreshToken) {
  _refreshToken = std::move(refreshToken);
}

void Alibabacloud_AccessTokenCredential::Client::setAccessToken(shared_ptr<string> accessToken) {
  _accessToken = std::move(accessToken);
}

time_t utc_strtotime(const std::string &utc_datetime) {
  struct tm tm{};
  strptime(utc_datetime.c_str(), "%Y-%m-%dT%H:%M:%SZ", &tm);
  time_t t = timegm(&tm);
  return boost::lexical_cast<long long>(t);
}

bool Alibabacloud_AccessTokenCredential::Client::shouldRefresh(long now) const {
  if (!_expireTime || !_refreshToken) {
    return false;
  }
  long expire = utc_strtotime(*_expireTime);
  return expire - now <= 500;
}

string Alibabacloud_AccessTokenCredential::Client::getAccessToken() {
  if (!_accessToken) {
    BOOST_THROW_EXCEPTION(std::runtime_error("AccessToken is null"));
  }
  long now = static_cast<long int>(time(nullptr));
  if (shouldRefresh(now)) {
    refreshAccessToken();
  }
  return *_accessToken;
}

string ltrim(std::string s) {
  s.erase(s.begin(), std::find_if(s.begin(), s.end(), [](unsigned char ch) {
    return !std::isspace(ch);
  }));
  return s;
}

string rtrim(std::string s) {
  s.erase(std::find_if(s.rbegin(), s.rend(),
                       [](unsigned char ch) { return !std::isspace(ch); })
              .base(),
          s.end());
  return s;
}

string trim(std::string s) {
  s = ltrim(s);
  s = rtrim(s);
  return s;
}

string getHost(const shared_ptr<string> &endpoint, const shared_ptr<string> &domainId, const string &suffix) {
  if (!endpoint && domainId) {
    return *domainId + suffix;
  }
  string e = !endpoint ? "" : trim(*endpoint);
  return e;
}

string getDateUTCString() {
  char buf[80];
  time_t t = time(nullptr);
  std::strftime(buf, sizeof buf, "%Y-%m-%dT%H:%M:%SZ", gmtime(&t));
  return buf;
}

boost::any parse_json(boost::property_tree::ptree pt) {
  if (pt.empty()) {
    if (pt.data() == "true" || pt.data() == "false") {
      return boost::any(pt.get_value<bool>());
    } else if (regex_search(pt.data(), regex("^-?\\d+$"))) {
      long ln = atol(pt.data().c_str());
      if (ln > 2147483647 || ln < -2147483648) {
        return boost::any(ln);
      } else {
        return boost::any(atoi(pt.data().c_str()));
      }
    } else if (regex_search(pt.data(), regex(R"(^-?\d+\.{1}\d+$)"))) {
      return boost::any(atof(pt.data().c_str()));
    }
    return boost::any(pt.data());
  }
  vector<boost::any> vec;
  map<string, boost::any> m;
  for (const auto &it : pt) {
    if (!it.first.empty()) {
      m[it.first] = parse_json(it.second);
    } else {
      vec.push_back(parse_json(it.second));
    }
  }
  return vec.empty() ? boost::any(m) : boost::any(vec);
}

boost::any json_decode(const string &val) {
  stringstream ss(val);
  using namespace boost::property_tree;
  ptree pt;
  read_json(ss, pt);
  return parse_json(pt);
}

void Alibabacloud_AccessTokenCredential::Client::refreshAccessToken() {
  Darabonba::Request req;
  req.protocol = "http";
  req.method = "POST";
  req.pathname = "/v2/oauth/token";
  req.headers["host"] = getHost(_endpoint, _domainId, ".api.aliyunpds.com");
  req.headers["content-type"] = "application/x-www-form-urlencoded; charset=utf-8";
  req.headers["date"] = getDateUTCString();
  req.headers["accept"] = "application/json";
  req.headers["x-acs-signature-method"] = "HMAC-SHA1";
  req.headers["x-acs-signature-version"] = "1.0";

  string refreshToken = !_refreshToken ? "" : *_refreshToken;
  string clientId = !_clientId ? "" : *_clientId;
  string clientSecret = !_clientSecret ? "" : *_clientSecret;

  shared_ptr<stringstream> body = make_shared<stringstream>();
  *body << "grant_type=refresh_token&refresh_token=" << refreshToken
        << "&client_id=" << clientId
        << "&client_secret=" << clientSecret;
  req.body = make_shared<Darabonba::Stream>(body);

  Darabonba::Response response = doAction(req);
  string content = response.body->read();
  if (response.statusCode == 200) {
    boost::any res = json_decode(content);
    map<string, boost::any> result = boost::any_cast<map<string, boost::any>>(res);
    _expireTime = make_shared<string>(boost::any_cast<string>(result["expire_time"]));
    _accessToken = make_shared<string>(boost::any_cast<string>(result["access_token"]));
    _refreshToken = make_shared<string>(boost::any_cast<string>(result["refresh_token"]));
  } else {
    BOOST_THROW_EXCEPTION(std::runtime_error(content));
  }
}

