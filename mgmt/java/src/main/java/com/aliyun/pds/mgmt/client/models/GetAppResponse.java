// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class GetAppResponse extends TeaModel {
    /**
     * <p>App 拥有者</p>
     */
    @NameInMap("ali_owner_id")
    @Validation(required = true)
    public String aliOwnerId;

    /**
     * <p>App ID</p>
     */
    @NameInMap("app_id")
    @Validation(required = true)
    public String appId;

    /**
     * <p>App名称</p>
     */
    @NameInMap("app_name")
    @Validation(required = true, pattern = "[0-9a-zA-Z]+", maxLength = 128, minLength = 1)
    public String appName;

    /**
     * <p>App 秘钥</p>
     */
    @NameInMap("app_secret")
    @Validation(required = true)
    public String appSecret;

    /**
     * <p>App 创建时间</p>
     */
    @NameInMap("created_at")
    @Validation(required = true)
    public String createdAt;

    /**
     * <p>App描述</p>
     */
    @NameInMap("description")
    @Validation(required = true, maxLength = 128)
    public String description;

    /**
     * <p>App图标</p>
     */
    @NameInMap("logo")
    @Validation(required = true)
    public String logo;

    /**
     * <p>App 提供方</p>
     */
    @NameInMap("provider")
    @Validation(required = true)
    public String provider;

    /**
     * <p>App回调地址</p>
     */
    @NameInMap("redirect_uri")
    @Validation(required = true)
    public String redirectUri;

    /**
     * <p>App权限列表</p>
     */
    @NameInMap("scope")
    @Validation(required = true)
    public java.util.List<String> scope;

    /**
     * <p>App 屏幕截图</p>
     */
    @NameInMap("screenshots")
    @Validation(required = true)
    public java.util.List<String> screenshots;

    /**
     * <p>App 当前阶段</p>
     */
    @NameInMap("stage")
    @Validation(required = true)
    public String stage;

    /**
     * <p>App类型</p>
     */
    @NameInMap("type")
    @Validation(required = true)
    public String type;

    /**
     * <p>App 修改时间</p>
     */
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
