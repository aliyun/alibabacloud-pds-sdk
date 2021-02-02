// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.hostingmode.client.models;

import com.aliyun.tea.*;

/**
 * update domain request
 */
public class UpdateDomainRequest extends TeaModel {
    @NameInMap("auth_config")
    public java.util.Map<String, ?> authConfig;

    // 钉钉 App Id
    @NameInMap("auth_dingding_app_id")
    public String authDingdingAppId;

    // 钉钉 App Secret
    @NameInMap("auth_dingding_app_secret")
    public String authDingdingAppSecret;

    // 启用钉钉认证
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

    // 启用 RAM 认证
    @NameInMap("auth_ram_enable")
    public Boolean authRamEnable;

    // 数据 Hash 算法
    @NameInMap("data_hash_name")
    public String dataHashName;

    // Domain 描述
    @NameInMap("description")
    public String description;

    // Domain ID
    @NameInMap("domain_id")
    @Validation(required = true)
    public String domainId;

    // Domain 名称
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

    // 开启自动初始化 Drive
    @NameInMap("init_drive_enable")
    public Boolean initDriveEnable;

    // 自动初始化 Drive 大小
    @NameInMap("init_drive_size")
    public Long initDriveSize;

    // 自动初始化 Drive 使用 Store ID
    @NameInMap("init_drive_store_id")
    public String initDriveStoreId;

    @NameInMap("published_app_access_strategy")
    public AppAccessStrategy publishedAppAccessStrategy;

    // 开启分享
    @NameInMap("sharable")
    public Boolean sharable;

    public static UpdateDomainRequest build(java.util.Map<String, ?> map) throws Exception {
        UpdateDomainRequest self = new UpdateDomainRequest();
        return TeaModel.build(map, self);
    }

    public UpdateDomainRequest setAuthConfig(java.util.Map<String, ?> authConfig) {
        this.authConfig = authConfig;
        return this;
    }
    public java.util.Map<String, ?> getAuthConfig() {
        return this.authConfig;
    }

    public UpdateDomainRequest setAuthDingdingAppId(String authDingdingAppId) {
        this.authDingdingAppId = authDingdingAppId;
        return this;
    }
    public String getAuthDingdingAppId() {
        return this.authDingdingAppId;
    }

    public UpdateDomainRequest setAuthDingdingAppSecret(String authDingdingAppSecret) {
        this.authDingdingAppSecret = authDingdingAppSecret;
        return this;
    }
    public String getAuthDingdingAppSecret() {
        return this.authDingdingAppSecret;
    }

    public UpdateDomainRequest setAuthDingdingEnable(Boolean authDingdingEnable) {
        this.authDingdingEnable = authDingdingEnable;
        return this;
    }
    public Boolean getAuthDingdingEnable() {
        return this.authDingdingEnable;
    }

    public UpdateDomainRequest setAuthEndpointEnable(Boolean authEndpointEnable) {
        this.authEndpointEnable = authEndpointEnable;
        return this;
    }
    public Boolean getAuthEndpointEnable() {
        return this.authEndpointEnable;
    }

    public UpdateDomainRequest setAuthRamAppId(String authRamAppId) {
        this.authRamAppId = authRamAppId;
        return this;
    }
    public String getAuthRamAppId() {
        return this.authRamAppId;
    }

    public UpdateDomainRequest setAuthRamAppSecret(String authRamAppSecret) {
        this.authRamAppSecret = authRamAppSecret;
        return this;
    }
    public String getAuthRamAppSecret() {
        return this.authRamAppSecret;
    }

    public UpdateDomainRequest setAuthRamEnable(Boolean authRamEnable) {
        this.authRamEnable = authRamEnable;
        return this;
    }
    public Boolean getAuthRamEnable() {
        return this.authRamEnable;
    }

    public UpdateDomainRequest setDataHashName(String dataHashName) {
        this.dataHashName = dataHashName;
        return this;
    }
    public String getDataHashName() {
        return this.dataHashName;
    }

    public UpdateDomainRequest setDescription(String description) {
        this.description = description;
        return this;
    }
    public String getDescription() {
        return this.description;
    }

    public UpdateDomainRequest setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public UpdateDomainRequest setDomainName(String domainName) {
        this.domainName = domainName;
        return this;
    }
    public String getDomainName() {
        return this.domainName;
    }

    public UpdateDomainRequest setEventFilenameMatches(String eventFilenameMatches) {
        this.eventFilenameMatches = eventFilenameMatches;
        return this;
    }
    public String getEventFilenameMatches() {
        return this.eventFilenameMatches;
    }

    public UpdateDomainRequest setEventMnsEndpoint(String eventMnsEndpoint) {
        this.eventMnsEndpoint = eventMnsEndpoint;
        return this;
    }
    public String getEventMnsEndpoint() {
        return this.eventMnsEndpoint;
    }

    public UpdateDomainRequest setEventMnsTopic(String eventMnsTopic) {
        this.eventMnsTopic = eventMnsTopic;
        return this;
    }
    public String getEventMnsTopic() {
        return this.eventMnsTopic;
    }

    public UpdateDomainRequest setEventNames(java.util.List<String> eventNames) {
        this.eventNames = eventNames;
        return this;
    }
    public java.util.List<String> getEventNames() {
        return this.eventNames;
    }

    public UpdateDomainRequest setEventRoleArn(String eventRoleArn) {
        this.eventRoleArn = eventRoleArn;
        return this;
    }
    public String getEventRoleArn() {
        return this.eventRoleArn;
    }

    public UpdateDomainRequest setInitDriveEnable(Boolean initDriveEnable) {
        this.initDriveEnable = initDriveEnable;
        return this;
    }
    public Boolean getInitDriveEnable() {
        return this.initDriveEnable;
    }

    public UpdateDomainRequest setInitDriveSize(Long initDriveSize) {
        this.initDriveSize = initDriveSize;
        return this;
    }
    public Long getInitDriveSize() {
        return this.initDriveSize;
    }

    public UpdateDomainRequest setInitDriveStoreId(String initDriveStoreId) {
        this.initDriveStoreId = initDriveStoreId;
        return this;
    }
    public String getInitDriveStoreId() {
        return this.initDriveStoreId;
    }

    public UpdateDomainRequest setPublishedAppAccessStrategy(AppAccessStrategy publishedAppAccessStrategy) {
        this.publishedAppAccessStrategy = publishedAppAccessStrategy;
        return this;
    }
    public AppAccessStrategy getPublishedAppAccessStrategy() {
        return this.publishedAppAccessStrategy;
    }

    public UpdateDomainRequest setSharable(Boolean sharable) {
        this.sharable = sharable;
        return this;
    }
    public Boolean getSharable() {
        return this.sharable;
    }

}
