// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class TokenRequest extends TeaModel {
    // JWT方式授权需要传此参数，传入JWT签名的声明，用于更换accessToken
    @NameInMap("Assertion")
    public String Assertion;

    // Client ID, 此处填写创建App时返回的AppID
    @NameInMap("ClientID")
    @Validation(required = true)
    public String ClientID;

    // Client ID, 此处填写创建App时返回的AppSecret
    @NameInMap("ClientSecret")
    @Validation(required = true)
    public String ClientSecret;

    // 认证后回调参数中的code
    @NameInMap("Code")
    public String Code;

    // OAuth2.0 device flow换取token参数
    @NameInMap("DeviceCode")
    public String DeviceCode;

    // 通过code获取accessToken或者通过refresh_token获取accessToken
    @NameInMap("GrantType")
    @Validation(required = true)
    public String GrantType;

    // 回调地址, 此处填写创建App时填写的回调地址，OAuth方式登录时需要传入
    @NameInMap("RedirectUri")
    public String RedirectUri;

    // 刷新accessToken使用的refreshToken
    @NameInMap("RefreshToken")
    public String RefreshToken;

    public static TokenRequest build(java.util.Map<String, ?> map) throws Exception {
        TokenRequest self = new TokenRequest();
        return TeaModel.build(map, self);
    }

    public TokenRequest setAssertion(String Assertion) {
        this.Assertion = Assertion;
        return this;
    }
    public String getAssertion() {
        return this.Assertion;
    }

    public TokenRequest setClientID(String ClientID) {
        this.ClientID = ClientID;
        return this;
    }
    public String getClientID() {
        return this.ClientID;
    }

    public TokenRequest setClientSecret(String ClientSecret) {
        this.ClientSecret = ClientSecret;
        return this;
    }
    public String getClientSecret() {
        return this.ClientSecret;
    }

    public TokenRequest setCode(String Code) {
        this.Code = Code;
        return this;
    }
    public String getCode() {
        return this.Code;
    }

    public TokenRequest setDeviceCode(String DeviceCode) {
        this.DeviceCode = DeviceCode;
        return this;
    }
    public String getDeviceCode() {
        return this.DeviceCode;
    }

    public TokenRequest setGrantType(String GrantType) {
        this.GrantType = GrantType;
        return this;
    }
    public String getGrantType() {
        return this.GrantType;
    }

    public TokenRequest setRedirectUri(String RedirectUri) {
        this.RedirectUri = RedirectUri;
        return this;
    }
    public String getRedirectUri() {
        return this.RedirectUri;
    }

    public TokenRequest setRefreshToken(String RefreshToken) {
        this.RefreshToken = RefreshToken;
        return this;
    }
    public String getRefreshToken() {
        return this.RefreshToken;
    }

}
