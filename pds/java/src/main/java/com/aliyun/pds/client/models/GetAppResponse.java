// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class GetAppResponse extends TeaModel {
    // App 拥有者
    @NameInMap("ali_owner_id")
    @Validation(required = true)
    public String aliOwnerId;

    // App ID
    @NameInMap("app_id")
    @Validation(required = true)
    public String appId;

    // App名称
    @NameInMap("app_name")
    @Validation(required = true, pattern = "[0-9a-zA-Z]+", maxLength = 128, minLength = 1)
    public String appName;

    // App 秘钥
    @NameInMap("app_secret")
    @Validation(required = true)
    public String appSecret;

    // App 创建时间
    @NameInMap("created_at")
    @Validation(required = true)
    public String createdAt;

    // App描述
    @NameInMap("description")
    @Validation(required = true, maxLength = 128)
    public String description;

    // App图标
    @NameInMap("logo")
    @Validation(required = true)
    public String logo;

    // App 提供方
    @NameInMap("provider")
    @Validation(required = true)
    public String provider;

    // App回调地址
    @NameInMap("redirect_uri")
    @Validation(required = true)
    public String redirectUri;

    // App权限列表
    @NameInMap("scope")
    @Validation(required = true)
    public java.util.List<String> scope;

    // App 屏幕截图
    @NameInMap("screenshots")
    @Validation(required = true)
    public java.util.List<String> screenshots;

    // App 当前阶段
    @NameInMap("stage")
    @Validation(required = true)
    public String stage;

    // App类型
    @NameInMap("type")
    @Validation(required = true)
    public String type;

    // App 修改时间
    @NameInMap("updated_at")
    @Validation(required = true)
    public String updatedAt;

    public static GetAppResponse build(java.util.Map<String, ?> map) throws Exception {
        GetAppResponse self = new GetAppResponse();
        return TeaModel.build(map, self);
    }

    public GetAppResponse setAliOwnerId(String aliOwnerId) {
        this.aliOwnerId = aliOwnerId;
        return this;
    }
    public String getAliOwnerId() {
        return this.aliOwnerId;
    }

    public GetAppResponse setAppId(String appId) {
        this.appId = appId;
        return this;
    }
    public String getAppId() {
        return this.appId;
    }

    public GetAppResponse setAppName(String appName) {
        this.appName = appName;
        return this;
    }
    public String getAppName() {
        return this.appName;
    }

    public GetAppResponse setAppSecret(String appSecret) {
        this.appSecret = appSecret;
        return this;
    }
    public String getAppSecret() {
        return this.appSecret;
    }

    public GetAppResponse setCreatedAt(String createdAt) {
        this.createdAt = createdAt;
        return this;
    }
    public String getCreatedAt() {
        return this.createdAt;
    }

    public GetAppResponse setDescription(String description) {
        this.description = description;
        return this;
    }
    public String getDescription() {
        return this.description;
    }

    public GetAppResponse setLogo(String logo) {
        this.logo = logo;
        return this;
    }
    public String getLogo() {
        return this.logo;
    }

    public GetAppResponse setProvider(String provider) {
        this.provider = provider;
        return this;
    }
    public String getProvider() {
        return this.provider;
    }

    public GetAppResponse setRedirectUri(String redirectUri) {
        this.redirectUri = redirectUri;
        return this;
    }
    public String getRedirectUri() {
        return this.redirectUri;
    }

    public GetAppResponse setScope(java.util.List<String> scope) {
        this.scope = scope;
        return this;
    }
    public java.util.List<String> getScope() {
        return this.scope;
    }

    public GetAppResponse setScreenshots(java.util.List<String> screenshots) {
        this.screenshots = screenshots;
        return this;
    }
    public java.util.List<String> getScreenshots() {
        return this.screenshots;
    }

    public GetAppResponse setStage(String stage) {
        this.stage = stage;
        return this;
    }
    public String getStage() {
        return this.stage;
    }

    public GetAppResponse setType(String type) {
        this.type = type;
        return this;
    }
    public String getType() {
        return this.type;
    }

    public GetAppResponse setUpdatedAt(String updatedAt) {
        this.updatedAt = updatedAt;
        return this;
    }
    public String getUpdatedAt() {
        return this.updatedAt;
    }

}
