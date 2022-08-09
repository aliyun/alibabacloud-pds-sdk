// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 *
 */
public class AccountAccessTokenResponse extends TeaModel {
    // 用于调用业务接口的accessToken
    @NameInMap("access_token")
    @Validation(required = true)
    public String accessToken;

    // 当前用户头像
    @NameInMap("avatar")
    public String avatar;

    // Default Drive ID
    @NameInMap("default_drive_id")
    public String defaultDriveId;

    // Default Sbox Drive ID
    @NameInMap("default_sbox_drive_id")
    public String defaultSboxDriveId;

    // device_id 通过device flow 绑定的设备ID
    @NameInMap("device_id")
    public String deviceId;

    // device_name 通过device flow 绑定的设备名
    @NameInMap("device_name")
    public String deviceName;

    // domainID 用户登录的domainID
    @NameInMap("domain_id")
    public String domainId;

    // 当前用户已存在的登录方式
    @NameInMap("exist_link")
    public java.util.List<LinkInfo> existLink;

    // accessToken过期时间，ISO时间
    @NameInMap("expire_time")
    public String expireTime;

    // accessToken过期时间，单位秒
    @NameInMap("expires_in")
    public Long expiresIn;

    // 用户是否为第一次登录
    @NameInMap("is_first_login")
    public Boolean isFirstLogin;

    // 是否需要绑定
    @NameInMap("need_link")
    @Validation(required = true)
    public Boolean needLink;

    // 用户是否需要进行的实人认证
    @NameInMap("need_rp_verify")
    public Boolean needRpVerify;

    // 当前用户昵称
    @NameInMap("nick_name")
    public String nickName;

    // 用户的数据密码是否设置过
    @NameInMap("pin_setup")
    public Boolean pinSetup;

    // 用于刷新accessToken
    @NameInMap("refresh_token")
    public String refreshToken;

    // 当前用户角色
    @NameInMap("role")
    public String role;

    // 临时权限，用于登录成功后设置密码
    @NameInMap("state")
    public String state;

    // 当前用户状态
    @NameInMap("status")
    public String status;

    // subdomain_id 用户登录的subdomain_id
    @NameInMap("subdomain_id")
    public String subdomainId;

    // accessToken类型，Bearer
    @NameInMap("token_type")
    public String tokenType;

    // 用户自定义数据，格式为json，可用于配置项、少量临时数据等存储，不超过1K
    @NameInMap("user_data")
    public java.util.Map<String, ?> userData;

    // 当前用户ID
    @NameInMap("user_id")
    public String userId;

    // 当前用户名
    @NameInMap("user_name")
    public String userName;

    public static AccountAccessTokenResponse build(java.util.Map<String, ?> map) throws Exception {
        AccountAccessTokenResponse self = new AccountAccessTokenResponse();
        return TeaModel.build(map, self);
    }

    public AccountAccessTokenResponse setAccessToken(String accessToken) {
        this.accessToken = accessToken;
        return this;
    }
    public String getAccessToken() {
        return this.accessToken;
    }

    public AccountAccessTokenResponse setAvatar(String avatar) {
        this.avatar = avatar;
        return this;
    }
    public String getAvatar() {
        return this.avatar;
    }

    public AccountAccessTokenResponse setDefaultDriveId(String defaultDriveId) {
        this.defaultDriveId = defaultDriveId;
        return this;
    }
    public String getDefaultDriveId() {
        return this.defaultDriveId;
    }

    public AccountAccessTokenResponse setDefaultSboxDriveId(String defaultSboxDriveId) {
        this.defaultSboxDriveId = defaultSboxDriveId;
        return this;
    }
    public String getDefaultSboxDriveId() {
        return this.defaultSboxDriveId;
    }

    public AccountAccessTokenResponse setDeviceId(String deviceId) {
        this.deviceId = deviceId;
        return this;
    }
    public String getDeviceId() {
        return this.deviceId;
    }

    public AccountAccessTokenResponse setDeviceName(String deviceName) {
        this.deviceName = deviceName;
        return this;
    }
    public String getDeviceName() {
        return this.deviceName;
    }

    public AccountAccessTokenResponse setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public AccountAccessTokenResponse setExistLink(java.util.List<LinkInfo> existLink) {
        this.existLink = existLink;
        return this;
    }
    public java.util.List<LinkInfo> getExistLink() {
        return this.existLink;
    }

    public AccountAccessTokenResponse setExpireTime(String expireTime) {
        this.expireTime = expireTime;
        return this;
    }
    public String getExpireTime() {
        return this.expireTime;
    }

    public AccountAccessTokenResponse setExpiresIn(Long expiresIn) {
        this.expiresIn = expiresIn;
        return this;
    }
    public Long getExpiresIn() {
        return this.expiresIn;
    }

    public AccountAccessTokenResponse setIsFirstLogin(Boolean isFirstLogin) {
        this.isFirstLogin = isFirstLogin;
        return this;
    }
    public Boolean getIsFirstLogin() {
        return this.isFirstLogin;
    }

    public AccountAccessTokenResponse setNeedLink(Boolean needLink) {
        this.needLink = needLink;
        return this;
    }
    public Boolean getNeedLink() {
        return this.needLink;
    }

    public AccountAccessTokenResponse setNeedRpVerify(Boolean needRpVerify) {
        this.needRpVerify = needRpVerify;
        return this;
    }
    public Boolean getNeedRpVerify() {
        return this.needRpVerify;
    }

    public AccountAccessTokenResponse setNickName(String nickName) {
        this.nickName = nickName;
        return this;
    }
    public String getNickName() {
        return this.nickName;
    }

    public AccountAccessTokenResponse setPinSetup(Boolean pinSetup) {
        this.pinSetup = pinSetup;
        return this;
    }
    public Boolean getPinSetup() {
        return this.pinSetup;
    }

    public AccountAccessTokenResponse setRefreshToken(String refreshToken) {
        this.refreshToken = refreshToken;
        return this;
    }
    public String getRefreshToken() {
        return this.refreshToken;
    }

    public AccountAccessTokenResponse setRole(String role) {
        this.role = role;
        return this;
    }
    public String getRole() {
        return this.role;
    }

    public AccountAccessTokenResponse setState(String state) {
        this.state = state;
        return this;
    }
    public String getState() {
        return this.state;
    }

    public AccountAccessTokenResponse setStatus(String status) {
        this.status = status;
        return this;
    }
    public String getStatus() {
        return this.status;
    }

    public AccountAccessTokenResponse setSubdomainId(String subdomainId) {
        this.subdomainId = subdomainId;
        return this;
    }
    public String getSubdomainId() {
        return this.subdomainId;
    }

    public AccountAccessTokenResponse setTokenType(String tokenType) {
        this.tokenType = tokenType;
        return this;
    }
    public String getTokenType() {
        return this.tokenType;
    }

    public AccountAccessTokenResponse setUserData(java.util.Map<String, ?> userData) {
        this.userData = userData;
        return this;
    }
    public java.util.Map<String, ?> getUserData() {
        return this.userData;
    }

    public AccountAccessTokenResponse setUserId(String userId) {
        this.userId = userId;
        return this;
    }
    public String getUserId() {
        return this.userId;
    }

    public AccountAccessTokenResponse setUserName(String userName) {
        this.userName = userName;
        return this;
    }
    public String getUserName() {
        return this.userName;
    }

}
