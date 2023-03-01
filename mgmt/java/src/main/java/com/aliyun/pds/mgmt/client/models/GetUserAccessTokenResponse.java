// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class GetUserAccessTokenResponse extends TeaModel {
    /**
     * <p>用于调用业务接口的accessToken</p>
     */
    @NameInMap("access_token")
    @Validation(required = true)
    public String accessToken;

    /**
     * <p>Default Drive ID</p>
     */
    @NameInMap("default_drive_id")
    @Validation(required = true)
    public String defaultDriveId;

    /**
     * <p>accessToken过期时间，ISO时间</p>
     */
    @NameInMap("expire_time")
    @Validation(required = true)
    public String expireTime;

    /**
     * <p>accessToken过期时间，单位秒</p>
     */
    @NameInMap("expires_in")
    @Validation(required = true)
    public Long expiresIn;

    /**
     * <p>用于刷新accessToken</p>
     */
    @NameInMap("refresh_token")
    public String refreshToken;

    /**
     * <p>当前用户角色</p>
     */
    @NameInMap("role")
    @Validation(required = true)
    public String role;

    /**
     * <p>accessToken类型，Bearer</p>
     */
    @NameInMap("token_type")
    @Validation(required = true)
    public String tokenType;

    /**
     * <p>当前用户ID</p>
     */
    @NameInMap("user_id")
    @Validation(required = true)
    public String userId;

    public static GetUserAccessTokenResponse build(java.util.Map<String, ?> map) throws Exception {
        GetUserAccessTokenResponse self = new GetUserAccessTokenResponse();
        return TeaModel.build(map, self);
    }

    public GetUserAccessTokenResponse setAccessToken(String accessToken) {
        this.accessToken = accessToken;
        return this;
    }
    public String getAccessToken() {
        return this.accessToken;
    }

    public GetUserAccessTokenResponse setDefaultDriveId(String defaultDriveId) {
        this.defaultDriveId = defaultDriveId;
        return this;
    }
    public String getDefaultDriveId() {
        return this.defaultDriveId;
    }

    public GetUserAccessTokenResponse setExpireTime(String expireTime) {
        this.expireTime = expireTime;
        return this;
    }
    public String getExpireTime() {
        return this.expireTime;
    }

    public GetUserAccessTokenResponse setExpiresIn(Long expiresIn) {
        this.expiresIn = expiresIn;
        return this;
    }
    public Long getExpiresIn() {
        return this.expiresIn;
    }

    public GetUserAccessTokenResponse setRefreshToken(String refreshToken) {
        this.refreshToken = refreshToken;
        return this;
    }
    public String getRefreshToken() {
        return this.refreshToken;
    }

    public GetUserAccessTokenResponse setRole(String role) {
        this.role = role;
        return this;
    }
    public String getRole() {
        return this.role;
    }

    public GetUserAccessTokenResponse setTokenType(String tokenType) {
        this.tokenType = tokenType;
        return this;
    }
    public String getTokenType() {
        return this.tokenType;
    }

    public GetUserAccessTokenResponse setUserId(String userId) {
        this.userId = userId;
        return this;
    }
    public String getUserId() {
        return this.userId;
    }

}
