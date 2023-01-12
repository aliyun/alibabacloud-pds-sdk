// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class AccountAccessTokenResponse extends TeaModel {
    /**
     * <p>用于调用业务接口的accessToken</p>
     */
    @NameInMap("access_token")
    @Validation(required = true)
    public String accessToken;

    /**
     * <p>当前用户头像</p>
     */
    @NameInMap("avatar")
    public String avatar;

    /**
     * <p>Default Drive ID</p>
     */
    @NameInMap("default_drive_id")
    public String defaultDriveId;

    /**
     * <p>Default Sbox Drive ID</p>
     */
    @NameInMap("default_sbox_drive_id")
    public String defaultSboxDriveId;

    /**
     * <p>device_id 通过device flow 绑定的设备ID</p>
     */
    @NameInMap("device_id")
    public String deviceId;

    /**
     * <p>device_name 通过device flow 绑定的设备名</p>
     */
    @NameInMap("device_name")
    public String deviceName;

    /**
     * <p>domainID 用户登录的domainID</p>
     */
    @NameInMap("domain_id")
    public String domainId;

    /**
     * <p>当前用户已存在的登录方式</p>
     */
    @NameInMap("exist_link")
    public java.util.List<LinkInfo> existLink;

    /**
     * <p>accessToken过期时间，ISO时间</p>
     */
    @NameInMap("expire_time")
    public String expireTime;

    /**
     * <p>accessToken过期时间，单位秒</p>
     */
    @NameInMap("expires_in")
    public Long expiresIn;

    /**
     * <p>用户是否为第一次登录</p>
     */
    @NameInMap("is_first_login")
    public Boolean isFirstLogin;

    /**
     * <p>是否需要绑定</p>
     */
    @NameInMap("need_link")
    @Validation(required = true)
    public Boolean needLink;

    /**
     * <p>用户是否需要进行的实人认证</p>
     */
    @NameInMap("need_rp_verify")
    public Boolean needRpVerify;

    /**
     * <p>当前用户昵称</p>
     */
    @NameInMap("nick_name")
    public String nickName;

    /**
     * <p>用户的数据密码是否设置过</p>
     */
    @NameInMap("pin_setup")
    public Boolean pinSetup;

    /**
     * <p>用于刷新accessToken</p>
     */
    @NameInMap("refresh_token")
    public String refreshToken;

    /**
     * <p>当前用户角色</p>
     */
    @NameInMap("role")
    public String role;

    /**
     * <p>临时权限，用于登录成功后设置密码</p>
     */
    @NameInMap("state")
    public String state;

    /**
     * <p>当前用户状态</p>
     */
    @NameInMap("status")
    public String status;

    /**
     * <p>subdomain_id 用户登录的subdomain_id</p>
     */
    @NameInMap("subdomain_id")
    public String subdomainId;

    /**
     * <p>accessToken类型，Bearer</p>
     */
    @NameInMap("token_type")
    public String tokenType;

    /**
     * <p>用户自定义数据，格式为json，可用于配置项、少量临时数据等存储，不超过1K</p>
     */
    @NameInMap("user_data")
    public java.util.Map<String, ?> userData;

    /**
     * <p>当前用户ID</p>
     */
    @NameInMap("user_id")
    public String userId;

    /**
     * <p>当前用户名</p>
     */
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
