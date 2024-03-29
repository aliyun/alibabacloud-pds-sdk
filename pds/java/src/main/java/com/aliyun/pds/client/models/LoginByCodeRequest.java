// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class LoginByCodeRequest extends TeaModel {
    /**
     * <p>鉴权后返回的accessToken，淘宝登录需要此字段</p>
     */
    @NameInMap("access_token")
    public String accessToken;

    /**
     * <p>App ID, 当前访问的App</p>
     */
    @NameInMap("app_id")
    @Validation(required = true)
    public String appId;

    /**
     * <p>鉴权后返回的AuthCode，支付宝登录需要此字段</p>
     */
    @NameInMap("auth_code")
    public String authCode;

    /**
     * <p>鉴权类型，淘宝、支付宝</p>
     */
    @NameInMap("type")
    @Validation(required = true)
    public String type;

    public static LoginByCodeRequest build(java.util.Map<String, ?> map) throws Exception {
        LoginByCodeRequest self = new LoginByCodeRequest();
        return TeaModel.build(map, self);
    }

    public LoginByCodeRequest setAccessToken(String accessToken) {
        this.accessToken = accessToken;
        return this;
    }
    public String getAccessToken() {
        return this.accessToken;
    }

    public LoginByCodeRequest setAppId(String appId) {
        this.appId = appId;
        return this;
    }
    public String getAppId() {
        return this.appId;
    }

    public LoginByCodeRequest setAuthCode(String authCode) {
        this.authCode = authCode;
        return this;
    }
    public String getAuthCode() {
        return this.authCode;
    }

    public LoginByCodeRequest setType(String type) {
        this.type = type;
        return this;
    }
    public String getType() {
        return this.type;
    }

}
