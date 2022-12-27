// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class AccountTokenRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    /**
     * <p>addition_data</p>
     */
    @NameInMap("addition_data")
    public java.util.Map<String, ?> additionData;

    /**
     * <p>App ID, 当前访问的App</p>
     */
    @NameInMap("app_id")
    @Validation(required = true)
    public String appId;

    /**
     * <p>只能填refresh_token</p>
     */
    @NameInMap("grant_type")
    @Validation(required = true)
    public String grantType;

    /**
     * <p>refresh token, 登录时返回的</p>
     */
    @NameInMap("refresh_token")
    @Validation(required = true)
    public String refreshToken;

    public static AccountTokenRequest build(java.util.Map<String, ?> map) throws Exception {
        AccountTokenRequest self = new AccountTokenRequest();
        return TeaModel.build(map, self);
    }

    public AccountTokenRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public AccountTokenRequest setAdditionData(java.util.Map<String, ?> additionData) {
        this.additionData = additionData;
        return this;
    }
    public java.util.Map<String, ?> getAdditionData() {
        return this.additionData;
    }

    public AccountTokenRequest setAppId(String appId) {
        this.appId = appId;
        return this;
    }
    public String getAppId() {
        return this.appId;
    }

    public AccountTokenRequest setGrantType(String grantType) {
        this.grantType = grantType;
        return this;
    }
    public String getGrantType() {
        return this.grantType;
    }

    public AccountTokenRequest setRefreshToken(String refreshToken) {
        this.refreshToken = refreshToken;
        return this;
    }
    public String getRefreshToken() {
        return this.refreshToken;
    }

}
