// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.mgmt.mode.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class UpdateAppRequest extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // App ID
    @NameInMap("app_id")
    @Validation(required = true)
    public String appId;

    // App名称
    @NameInMap("app_name")
    @Validation(required = true, maxLength = 128, minLength = 1)
    public String appName;

    // App描述
    @NameInMap("description")
    @Validation(maxLength = 128)
    public String description;

    // App图标
    @NameInMap("logo")
    @Validation(required = true)
    public String logo;

    // App回调地址
    @NameInMap("redirect_uri")
    @Validation(required = true)
    public String redirectUri;

    // App权限列表
    @NameInMap("scope")
    @Validation(required = true)
    public java.util.List<String> scope;

    // App类型
    @NameInMap("type")
    @Validation(required = true)
    public String type;

    public static UpdateAppRequest build(java.util.Map<String, ?> map) throws Exception {
        UpdateAppRequest self = new UpdateAppRequest();
        return TeaModel.build(map, self);
    }

    public UpdateAppRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
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
