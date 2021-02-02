// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.hostingmode.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class CreateAppRequest extends TeaModel {
    // App名称
    @NameInMap("app_name")
    @Validation(required = true, maxLength = 128, minLength = 1)
    public String appName;

    // App描述
    @NameInMap("description")
    @Validation(maxLength = 128)
    public String description;

    // 是否是domain私有App
    @NameInMap("is_third_party")
    public Boolean isThirdParty;

    // App图标
    @NameInMap("logo")
    @Validation(required = true)
    public String logo;

    // RSA加密算法的公钥, PEM格式
    @NameInMap("public_key")
    @Validation(required = true)
    public String publicKey;

    // App回调地址
    @NameInMap("redirect_uri")
    public String redirectUri;

    // App权限列表
    @NameInMap("scope")
    @Validation(required = true)
    public java.util.List<String> scope;

    // App类型
    @NameInMap("type")
    @Validation(required = true)
    public String type;

    public static CreateAppRequest build(java.util.Map<String, ?> map) throws Exception {
        CreateAppRequest self = new CreateAppRequest();
        return TeaModel.build(map, self);
    }

    public CreateAppRequest setAppName(String appName) {
        this.appName = appName;
        return this;
    }
    public String getAppName() {
        return this.appName;
    }

    public CreateAppRequest setDescription(String description) {
        this.description = description;
        return this;
    }
    public String getDescription() {
        return this.description;
    }

    public CreateAppRequest setIsThirdParty(Boolean isThirdParty) {
        this.isThirdParty = isThirdParty;
        return this;
    }
    public Boolean getIsThirdParty() {
        return this.isThirdParty;
    }

    public CreateAppRequest setLogo(String logo) {
        this.logo = logo;
        return this;
    }
    public String getLogo() {
        return this.logo;
    }

    public CreateAppRequest setPublicKey(String publicKey) {
        this.publicKey = publicKey;
        return this;
    }
    public String getPublicKey() {
        return this.publicKey;
    }

    public CreateAppRequest setRedirectUri(String redirectUri) {
        this.redirectUri = redirectUri;
        return this;
    }
    public String getRedirectUri() {
        return this.redirectUri;
    }

    public CreateAppRequest setScope(java.util.List<String> scope) {
        this.scope = scope;
        return this;
    }
    public java.util.List<String> getScope() {
        return this.scope;
    }

    public CreateAppRequest setType(String type) {
        this.type = type;
        return this;
    }
    public String getType() {
        return this.type;
    }

}
