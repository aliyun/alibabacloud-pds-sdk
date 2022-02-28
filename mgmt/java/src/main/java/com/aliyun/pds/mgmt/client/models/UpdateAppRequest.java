// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class UpdateAppRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    // App ID
    @NameInMap("app_id")
    @Validation(required = true)
    public String appId;

    // App名称
    @NameInMap("app_name")
    @Validation(maxLength = 128, minLength = 1)
    public String appName;

    // App描述
    @NameInMap("description")
    @Validation(maxLength = 1024)
    public String description;

    // App图标
    @NameInMap("logo")
    public String logo;

    // App回调地址
    @NameInMap("redirect_uri")
    public String redirectUri;

    // App权限列表
    @NameInMap("scope")
    public java.util.List<String> scope;

    // App类型
    @NameInMap("type")
    public String type;

    public static UpdateAppRequest build(java.util.Map<String, ?> map) throws Exception {
        UpdateAppRequest self = new UpdateAppRequest();
        return TeaModel.build(map, self);
    }

    public UpdateAppRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public UpdateAppRequest setAppId(String appId) {
        this.appId = appId;
        return this;
    }
    public String getAppId() {
        return this.appId;
    }

    public UpdateAppRequest setAppName(String appName) {
        this.appName = appName;
        return this;
    }
    public String getAppName() {
        return this.appName;
    }

    public UpdateAppRequest setDescription(String description) {
        this.description = description;
        return this;
    }
    public String getDescription() {
        return this.description;
    }

    public UpdateAppRequest setLogo(String logo) {
        this.logo = logo;
        return this;
    }
    public String getLogo() {
        return this.logo;
    }

    public UpdateAppRequest setRedirectUri(String redirectUri) {
        this.redirectUri = redirectUri;
        return this;
    }
    public String getRedirectUri() {
        return this.redirectUri;
    }

    public UpdateAppRequest setScope(java.util.List<String> scope) {
        this.scope = scope;
        return this;
    }
    public java.util.List<String> getScope() {
        return this.scope;
    }

    public UpdateAppRequest setType(String type) {
        this.type = type;
        return this;
    }
    public String getType() {
        return this.type;
    }

}
