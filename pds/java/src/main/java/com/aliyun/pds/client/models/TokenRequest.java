// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class TokenRequest extends TeaModel {
    /**
     * <p>JWT方式授权需要传此参数，传入JWT签名的声明，用于更换accessToken</p>
     */
    @NameInMap("Assertion")
    public String Assertion;

    /**
     * <p>Client ID, 此处填写创建App时返回的AppID</p>
     */
    @NameInMap("ClientID")
    @Validation(required = true)
    public String ClientID;

    /**
     * <p>Client ID, 此处填写创建App时返回的AppSecret</p>
     */
    @NameInMap("ClientSecret")
    @Validation(required = true)
    public String ClientSecret;

    /**
     * <p>认证后回调参数中的code</p>
     */
    @NameInMap("Code")
    public String Code;

    /**
     * <p>OAuth2.0 device flow换取token参数</p>
     */
    @NameInMap("DeviceCode")
    public String DeviceCode;

    /**
     * <p>通过code获取accessToken或者通过refresh_token获取accessToken</p>
     */
    @NameInMap("GrantType")
    @Validation(required = true)
    public String GrantType;

    /**
     * <p>回调地址, 此处填写创建App时填写的回调地址，OAuth方式登录时需要传入</p>
     */
    @NameInMap("RedirectUri")
    public String RedirectUri;

    /**
     * <p>刷新accessToken使用的refreshToken</p>
     */
    @NameInMap("RefreshToken")
    public String RefreshToken;

    /**
     * <p>SubDomainID</p>
     */
    @NameInMap("SubDomainID")
    public String SubDomainID;

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

    public TokenRequest setSubDomainID(String SubDomainID) {
        this.SubDomainID = SubDomainID;
        return this;
    }
    public String getSubDomainID() {
        return this.SubDomainID;
    }

}
