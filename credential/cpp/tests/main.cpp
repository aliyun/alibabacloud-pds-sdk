#include "gtest/gtest.h"
#include <alibabacloud/access_token_credential.hpp>
#include <memory>

using namespace std;

int main(int argc, char **argv) {
  ::testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}

TEST(tests, test_basic) {
  Alibabacloud_AccessTokenCredential::Config config;
  config.refreshToken = make_shared<string>("refreshToken");
  config.accessToken = make_shared<string>("accessToken");
  config.expireTime = make_shared<string>("4000-01-01T12:12:12Z");

  Alibabacloud_AccessTokenCredential::Client client(make_shared<Alibabacloud_AccessTokenCredential::Config>(config));

  ASSERT_EQ(string("accessToken"), client.getAccessToken());
  ASSERT_EQ(string("refreshToken"), client.getRefreshToken());
  ASSERT_EQ(string("4000-01-01T12:12:12Z"), client.getExpireTime());
}

TEST(tests, test_get_set) {
  Alibabacloud_AccessTokenCredential::Config config;
  Alibabacloud_AccessTokenCredential::Client client(make_shared<Alibabacloud_AccessTokenCredential::Config>(config));

  client.setAccessToken(make_shared<string>("test"));
  ASSERT_EQ(string("test"), client.getAccessToken());

  client.setRefreshToken(make_shared<string>("token"));
  ASSERT_EQ(string("token"), client.getRefreshToken());

  client.setExpireTime(make_shared<string>("1"));
  ASSERT_EQ(string("1"), client.getExpireTime());
}

TEST(tests, test_ShouldRefresh) {
  shared_ptr<Alibabacloud_AccessTokenCredential::Config>
      config = make_shared<Alibabacloud_AccessTokenCredential::Config>();
  Alibabacloud_AccessTokenCredential::Client client(config);

  ASSERT_FALSE(client.shouldRefresh(1000));

  config->expireTime = make_shared<string>("2000-01-01T12:12:12Z");
  client = Alibabacloud_AccessTokenCredential::Client(config);
  ASSERT_FALSE(client.shouldRefresh(1000));

  config->refreshToken = make_shared<string>("test");
  client = Alibabacloud_AccessTokenCredential::Client(config);
  ASSERT_TRUE(client.shouldRefresh(1572509376182));
}
