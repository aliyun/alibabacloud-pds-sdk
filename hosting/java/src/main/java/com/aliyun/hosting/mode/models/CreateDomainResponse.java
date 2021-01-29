// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

/**
 * create domain response
 */
public class CreateDomainResponse extends TeaModel {
    // Domain APICName
    @NameInMap("api_cname")
    public String apiCname;

    // Domain AppCName
    @NameInMap("app_cname")
    public String appCname;

    // 支付宝 App Id
    @NameInMap("auth_alipay_app_id")
    public String authAlipayAppId;

    // 是否开启了支付宝认证
    @NameInMap("auth_alipay_enable")
    public Boolean authAlipayEnable;

    // 支付宝 App Secret
    @NameInMap("auth_alipay_private_key")
    public String authAlipayPrivateKey;

    // Domain AuthCName
    @NameInMap("auth_cname")
    public String authCname;

    // 登录相关信息
    @NameInMap("auth_config")
    public java.util.Map<String, ?> authConfig;

    // 钉钉 App Id
    @NameInMap("auth_dingding_app_id")
    public String authDingdingAppId;

    // 钉钉 App Secret
    @NameInMap("auth_dingding_app_secret")
    public String authDingdingAppSecret;

    // 是否开启了钉钉认证
    @NameInMap("auth_dingding_enable")
    public Boolean authDingdingEnable;

    @NameInMap("auth_endpoint_enable")
    public Boolean authEndpointEnable;

    // RAM App Id
    @NameInMap("auth_ram_app_id")
    public String authRamAppId;

    // RAM App Secret
    @NameInMap("auth_ram_app_secret")
    public String authRamAppSecret;

    // 是否开启了 RAM 认证
    @NameInMap("auth_ram_enable")
    public Boolean authRamEnable;

    // Domain 创建时间
    @NameInMap("created_at")
    public String createdAt;

    // 数据 Hash 算法
    @NameInMap("data_hash_name")
    public String dataHashName;

    // Domain 描述
    @NameInMap("description")
    public String description;

    // Domain ID
    @NameInMap("domain_id")
    public String domainId;

    // Domain 描述
    @NameInMap("domain_name")
    public String domainName;

    // 事件通知 MNS 匹配文件名
    @NameInMap("event_filename_matches")
    public String eventFilenameMatches;

    // 事件通知 MNS Endpoint
    @NameInMap("event_mns_endpoint")
    public String eventMnsEndpoint;

    // 事件通知 MNS Topic
    @NameInMap("event_mns_topic")
    public String eventMnsTopic;

    // 事件名列表
    @NameInMap("event_names")
    public java.util.List<String> eventNames;

    // 事件通知 Role Arn
    @NameInMap("event_role_arn")
    public String eventRoleArn;

    // 是否开启了自动初始化 Drive
    @NameInMap("init_drive_enable")
    public Boolean initDriveEnable;

    // 自动初始化 Drive 大小
    @NameInMap("init_drive_size")
    public Long initDriveSize;

    // 自动初始化 Drive 所用 Store ID
    @NameInMap("init_drive_store_id")
    public String initDriveStoreId;

    // Domain 类型
    @NameInMap("mode")
    public String mode;

    // Domain 类型
    @NameInMap("path_type")
    public String pathType;

    @NameInMap("published_app_access_strategy")
    public AppAccessStrategy publishedAppAccessStrategy;

    // 是否开启了分享
    @NameInMap("sharable")
    public Boolean sharable;

    // 存储级别
    @NameInMap("store_level")
    public String storeLevel;

    // 存储 Region 列表
    @NameInMap("store_region_list")
    public java.util.List<String> storeRegionList;

    // Domain 更新时间
    @NameInMap("updated_at")
    public String updatedAt;

    public static CreateDomainResponse build(java.util.Map<String, ?> map) throws Exception {
        CreateDomainResponse self = new CreateDomainResponse();
        return TeaModel.build(map, self);
    }

    public CreateDomainResponse setApiCname(String apiCname) {
        this.apiCname = apiCname;
        return this;
    }
    public String getApiCname() {
        return this.apiCname;
    }

    public CreateDomainResponse setAppCname(String appCname) {
        this.appCname = appCname;
        return this;
    }
    public String getAppCname() {
        return this.appCname;
    }

    public CreateDomainResponse setAuthAlipayAppId(String authAlipayAppId) {
        this.authAlipayAppId = authAlipayAppId;
        return this;
    }
    public String getAuthAlipayAppId() {
        return this.authAlipayAppId;
    }

    public CreateDomainResponse setAuthAlipayEnable(Boolean authAlipayEnable) {
        this.authAlipayEnable = authAlipayEnable;
        return this;
    }
    public Boolean getAuthAlipayEnable() {
        return this.authAlipayEnable;
    }

    public CreateDomainResponse setAuthAlipayPrivateKey(String authAlipayPrivateKey) {
        this.authAlipayPrivateKey = authAlipayPrivateKey;
        return this;
    }
    public String getAuthAlipayPrivateKey() {
        return this.authAlipayPrivateKey;
    }

    public CreateDomainResponse setAuthCname(String authCname) {
        this.authCname = authCname;
        return this;
    }
    public String getAuthCname() {
        return this.authCname;
    }

    public CreateDomainResponse setAuthConfig(java.util.Map<String, ?> authConfig) {
        this.authConfig = authConfig;
        return this;
    }
    public java.util.Map<String, ?> getAuthConfig() {
        return this.authConfig;
    }

    public CreateDomainResponse setAuthDingdingAppId(String authDingdingAppId) {
        this.authDingdingAppId = authDingdingAppId;
        return this;
    }
    public String getAuthDingdingAppId() {
        return this.authDingdingAppId;
    }

    public CreateDomainResponse setAuthDingdingAppSecret(String authDingdingAppSecret) {
        this.authDingdingAppSecret = authDingdingAppSecret;
        return this;
    }
    public String getAuthDingdingAppSecret() {
        return this.authDingdingAppSecret;
    }

    public CreateDomainResponse setAuthDingdingEnable(Boolean authDingdingEnable) {
        this.authDingdingEnable = authDingdingEnable;
        return this;
    }
    public Boolean getAuthDingdingEnable() {
        return this.authDingdingEnable;
    }

    public CreateDomainResponse setAuthEndpointEnable(Boolean authEndpointEnable) {
        this.authEndpointEnable = authEndpointEnable;
        return this;
    }
    public Boolean getAuthEndpointEnable() {
        return this.authEndpointEnable;
    }

    public CreateDomainResponse setAuthRamAppId(String authRamAppId) {
        this.authRamAppId = authRamAppId;
        return this;
    }
    public String getAuthRamAppId() {
        return this.authRamAppId;
    }

    public CreateDomainResponse setAuthRamAppSecret(String authRamAppSecret) {
        this.authRamAppSecret = authRamAppSecret;
        return this;
    }
    public String getAuthRamAppSecret() {
        return this.authRamAppSecret;
    }

    public CreateDomainResponse setAuthRamEnable(Boolean authRamEnable) {
        this.authRamEnable = authRamEnable;
        return this;
    }
    public Boolean getAuthRamEnable() {
        return this.authRamEnable;
    }

    public CreateDomainResponse setCreatedAt(String createdAt) {
        this.createdAt = createdAt;
        return this;
    }
    public String getCreatedAt() {
        return this.createdAt;
    }

    public CreateDomainResponse setDataHashName(String dataHashName) {
        this.dataHashName = dataHashName;
        return this;
    }
    public String getDataHashName() {
        return this.dataHashName;
    }

    public CreateDomainResponse setDescription(String description) {
        this.description = description;
        return this;
    }
    public String getDescription() {
        return this.description;
    }

    public CreateDomainResponse setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public CreateDomainResponse setDomainName(String domainName) {
        this.domainName = domainName;
        return this;
    }
    public String getDomainName() {
        return this.domainName;
    }

    public CreateDomainResponse setEventFilenameMatches(String eventFilenameMatches) {
        this.eventFilenameMatches = eventFilenameMatches;
        return this;
    }
    public String getEventFilenameMatches() {
        return this.eventFilenameMatches;
    }

    public CreateDomainResponse setEventMnsEndpoint(String eventMnsEndpoint) {
        this.eventMnsEndpoint = eventMnsEndpoint;
        return this;
    }
    public String getEventMnsEndpoint() {
        return this.eventMnsEndpoint;
    }

    public CreateDomainResponse setEventMnsTopic(String eventMnsTopic) {
        this.eventMnsTopic = eventMnsTopic;
        return this;
    }
    public String getEventMnsTopic() {
        return this.eventMnsTopic;
    }

    public CreateDomainResponse setEventNames(java.util.List<String> eventNames) {
        this.eventNames = eventNames;
        return this;
    }
    public java.util.List<String> getEventNames() {
        return this.eventNames;
    }

    public CreateDomainResponse setEventRoleArn(String eventRoleArn) {
        this.eventRoleArn = eventRoleArn;
        return this;
    }
    public String getEventRoleArn() {
        return this.eventRoleArn;
    }

    public CreateDomainResponse setInitDriveEnable(Boolean initDriveEnable) {
        this.initDriveEnable = initDriveEnable;
        return this;
    }
    public Boolean getInitDriveEnable() {
        return this.initDriveEnable;
    }

    public CreateDomainResponse setInitDriveSize(Long initDriveSize) {
        this.initDriveSize = initDriveSize;
        return this;
    }
    public Long getInitDriveSize() {
        return this.initDriveSize;
    }

    public CreateDomainResponse setInitDriveStoreId(String initDriveStoreId) {
        this.initDriveStoreId = initDriveStoreId;
        return this;
    }
    public String getInitDriveStoreId() {
        return this.initDriveStoreId;
    }

    public CreateDomainResponse setMode(String mode) {
        this.mode = mode;
        return this;
    }
    public String getMode() {
        return this.mode;
    }

    public CreateDomainResponse setPathType(String pathType) {
        this.pathType = pathType;
        return this;
    }
    public String getPathType() {
        return this.pathType;
    }

    public CreateDomainResponse setPublishedAppAccessStrategy(AppAccessStrategy publishedAppAccessStrategy) {
        this.publishedAppAccessStrategy = publishedAppAccessStrategy;
        return this;
    }
    public AppAccessStrategy getPublishedAppAccessStrategy() {
        return this.publishedAppAccessStrategy;
    }

    public CreateDomainResponse setSharable(Boolean sharable) {
        this.sharable = sharable;
        return this;
    }
    public Boolean getSharable() {
        return this.sharable;
    }

    public CreateDomainResponse setStoreLevel(String storeLevel) {
        this.storeLevel = storeLevel;
        return this;
    }
    public String getStoreLevel() {
        return this.storeLevel;
    }

    public CreateDomainResponse setStoreRegionList(java.util.List<String> storeRegionList) {
        this.storeRegionList = storeRegionList;
        return this;
    }
    public java.util.List<String> getStoreRegionList() {
        return this.storeRegionList;
    }

    public CreateDomainResponse setUpdatedAt(String updatedAt) {
        this.updatedAt = updatedAt;
        return this;
    }
    public String getUpdatedAt() {
        return this.updatedAt;
    }

}
