// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * create domain request
 */
public class CreateDomainRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    /**
     * <p>登录相关信息</p>
     */
    @NameInMap("auth_config")
    public java.util.Map<String, ?> authConfig;

    /**
     * <p>钉钉 App Id</p>
     */
    @NameInMap("auth_dingding_app_id")
    public String authDingdingAppId;

    /**
     * <p>钉钉 App Secret</p>
     */
    @NameInMap("auth_dingding_app_secret")
    public String authDingdingAppSecret;

    /**
     * <p>启用钉钉认证</p>
     */
    @NameInMap("auth_dingding_enable")
    public Boolean authDingdingEnable;

    /**
     * <p>RAM App Id</p>
     */
    @NameInMap("auth_ram_app_id")
    public String authRamAppId;

    /**
     * <p>RAM App Secret</p>
     */
    @NameInMap("auth_ram_app_secret")
    public String authRamAppSecret;

    /**
     * <p>启用 RAM 认证</p>
     */
    @NameInMap("auth_ram_enable")
    public Boolean authRamEnable;

    /**
     * <p>数据 Hash 算法</p>
     */
    @NameInMap("data_hash_name")
    public String dataHashName;

    /**
     * <p>Domain 描述</p>
     */
    @NameInMap("description")
    public String description;

    /**
     * <p>Domain 名称</p>
     */
    @NameInMap("domain_name")
    public String domainName;

    /**
     * <p>事件通知 MNS 匹配文件名</p>
     */
    @NameInMap("event_filename_matches")
    public String eventFilenameMatches;

    /**
     * <p>事件通知 MNS Endpoint</p>
     */
    @NameInMap("event_mns_endpoint")
    public String eventMnsEndpoint;

    /**
     * <p>事件通知 MNS Topic</p>
     */
    @NameInMap("event_mns_topic")
    public String eventMnsTopic;

    /**
     * <p>事件名列表</p>
     */
    @NameInMap("event_names")
    public java.util.List<String> eventNames;

    /**
     * <p>事件通知 Role Arn</p>
     */
    @NameInMap("event_role_arn")
    public String eventRoleArn;

    /**
     * <p>单团队单drive</p>
     */
    @NameInMap("group_single_drive_enabled")
    public Boolean groupSingleDriveEnabled;

    @NameInMap("independent_store")
    public Boolean independentStore;

    /**
     * <p>开启自动初始化 Drive</p>
     */
    @NameInMap("init_drive_enable")
    public Boolean initDriveEnable;

    /**
     * <p>自动初始化 Drive 大小</p>
     */
    @NameInMap("init_drive_size")
    public Long initDriveSize;

    /**
     * <p>Domain 类型</p>
     */
    @NameInMap("mode")
    public String mode;

    /**
     * <p>父 Domain ID</p>
     */
    @NameInMap("parent_domain_id")
    public String parentDomainId;

    /**
     * <p>Domain 类型</p>
     */
    @NameInMap("path_type")
    public String pathType;

    @NameInMap("published_app_access_strategy")
    public AppAccessStrategy publishedAppAccessStrategy;

    /**
     * <p>开启分享</p>
     */
    @NameInMap("sharable")
    public Boolean sharable;

    /**
     * <p>逻辑空间quota，默认为-1，无限制，单位为字节</p>
     */
    @NameInMap("size_quota")
    public Long sizeQuota;

    /**
     * <p>存储级别</p>
     */
    @NameInMap("store_level")
    public String storeLevel;

    /**
     * <p>存储 Region 列表</p>
     */
    @NameInMap("store_region_list")
    public java.util.List<String> storeRegionList;

    /**
     * <p>逻辑空间刷新周期，单位：秒</p>
     */
    @NameInMap("used_size_refresh_interval")
    public Long usedSizeRefreshInterval;

    /**
     * <p>用户数quota，默认为-1，无限制</p>
     */
    @NameInMap("user_count_quota")
    public Long userCountQuota;

    /**
     * <p>单用户单drive</p>
     */
    @NameInMap("user_single_drive_enabled")
    public Boolean userSingleDriveEnabled;

    public static CreateDomainRequest build(java.util.Map<String, ?> map) throws Exception {
        CreateDomainRequest self = new CreateDomainRequest();
        return TeaModel.build(map, self);
    }

    public CreateDomainRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public CreateDomainRequest setAuthConfig(java.util.Map<String, ?> authConfig) {
        this.authConfig = authConfig;
        return this;
    }
    public java.util.Map<String, ?> getAuthConfig() {
        return this.authConfig;
    }

    public CreateDomainRequest setAuthDingdingAppId(String authDingdingAppId) {
        this.authDingdingAppId = authDingdingAppId;
        return this;
    }
    public String getAuthDingdingAppId() {
        return this.authDingdingAppId;
    }

    public CreateDomainRequest setAuthDingdingAppSecret(String authDingdingAppSecret) {
        this.authDingdingAppSecret = authDingdingAppSecret;
        return this;
    }
    public String getAuthDingdingAppSecret() {
        return this.authDingdingAppSecret;
    }

    public CreateDomainRequest setAuthDingdingEnable(Boolean authDingdingEnable) {
        this.authDingdingEnable = authDingdingEnable;
        return this;
    }
    public Boolean getAuthDingdingEnable() {
        return this.authDingdingEnable;
    }

    public CreateDomainRequest setAuthRamAppId(String authRamAppId) {
        this.authRamAppId = authRamAppId;
        return this;
    }
    public String getAuthRamAppId() {
        return this.authRamAppId;
    }

    public CreateDomainRequest setAuthRamAppSecret(String authRamAppSecret) {
        this.authRamAppSecret = authRamAppSecret;
        return this;
    }
    public String getAuthRamAppSecret() {
        return this.authRamAppSecret;
    }

    public CreateDomainRequest setAuthRamEnable(Boolean authRamEnable) {
        this.authRamEnable = authRamEnable;
        return this;
    }
    public Boolean getAuthRamEnable() {
        return this.authRamEnable;
    }

    public CreateDomainRequest setDataHashName(String dataHashName) {
        this.dataHashName = dataHashName;
        return this;
    }
    public String getDataHashName() {
        return this.dataHashName;
    }

    public CreateDomainRequest setDescription(String description) {
        this.description = description;
        return this;
    }
    public String getDescription() {
        return this.description;
    }

    public CreateDomainRequest setDomainName(String domainName) {
        this.domainName = domainName;
        return this;
    }
    public String getDomainName() {
        return this.domainName;
    }

    public CreateDomainRequest setEventFilenameMatches(String eventFilenameMatches) {
        this.eventFilenameMatches = eventFilenameMatches;
        return this;
    }
    public String getEventFilenameMatches() {
        return this.eventFilenameMatches;
    }

    public CreateDomainRequest setEventMnsEndpoint(String eventMnsEndpoint) {
        this.eventMnsEndpoint = eventMnsEndpoint;
        return this;
    }
    public String getEventMnsEndpoint() {
        return this.eventMnsEndpoint;
    }

    public CreateDomainRequest setEventMnsTopic(String eventMnsTopic) {
        this.eventMnsTopic = eventMnsTopic;
        return this;
    }
    public String getEventMnsTopic() {
        return this.eventMnsTopic;
    }

    public CreateDomainRequest setEventNames(java.util.List<String> eventNames) {
        this.eventNames = eventNames;
        return this;
    }
    public java.util.List<String> getEventNames() {
        return this.eventNames;
    }

    public CreateDomainRequest setEventRoleArn(String eventRoleArn) {
        this.eventRoleArn = eventRoleArn;
        return this;
    }
    public String getEventRoleArn() {
        return this.eventRoleArn;
    }

    public CreateDomainRequest setGroupSingleDriveEnabled(Boolean groupSingleDriveEnabled) {
        this.groupSingleDriveEnabled = groupSingleDriveEnabled;
        return this;
    }
    public Boolean getGroupSingleDriveEnabled() {
        return this.groupSingleDriveEnabled;
    }

    public CreateDomainRequest setIndependentStore(Boolean independentStore) {
        this.independentStore = independentStore;
        return this;
    }
    public Boolean getIndependentStore() {
        return this.independentStore;
    }

    public CreateDomainRequest setInitDriveEnable(Boolean initDriveEnable) {
        this.initDriveEnable = initDriveEnable;
        return this;
    }
    public Boolean getInitDriveEnable() {
        return this.initDriveEnable;
    }

    public CreateDomainRequest setInitDriveSize(Long initDriveSize) {
        this.initDriveSize = initDriveSize;
        return this;
    }
    public Long getInitDriveSize() {
        return this.initDriveSize;
    }

    public CreateDomainRequest setMode(String mode) {
        this.mode = mode;
        return this;
    }
    public String getMode() {
        return this.mode;
    }

    public CreateDomainRequest setParentDomainId(String parentDomainId) {
        this.parentDomainId = parentDomainId;
        return this;
    }
    public String getParentDomainId() {
        return this.parentDomainId;
    }

    public CreateDomainRequest setPathType(String pathType) {
        this.pathType = pathType;
        return this;
    }
    public String getPathType() {
        return this.pathType;
    }

    public CreateDomainRequest setPublishedAppAccessStrategy(AppAccessStrategy publishedAppAccessStrategy) {
        this.publishedAppAccessStrategy = publishedAppAccessStrategy;
        return this;
    }
    public AppAccessStrategy getPublishedAppAccessStrategy() {
        return this.publishedAppAccessStrategy;
    }

    public CreateDomainRequest setSharable(Boolean sharable) {
        this.sharable = sharable;
        return this;
    }
    public Boolean getSharable() {
        return this.sharable;
    }

    public CreateDomainRequest setSizeQuota(Long sizeQuota) {
        this.sizeQuota = sizeQuota;
        return this;
    }
    public Long getSizeQuota() {
        return this.sizeQuota;
    }

    public CreateDomainRequest setStoreLevel(String storeLevel) {
        this.storeLevel = storeLevel;
        return this;
    }
    public String getStoreLevel() {
        return this.storeLevel;
    }

    public CreateDomainRequest setStoreRegionList(java.util.List<String> storeRegionList) {
        this.storeRegionList = storeRegionList;
        return this;
    }
    public java.util.List<String> getStoreRegionList() {
        return this.storeRegionList;
    }

    public CreateDomainRequest setUsedSizeRefreshInterval(Long usedSizeRefreshInterval) {
        this.usedSizeRefreshInterval = usedSizeRefreshInterval;
        return this;
    }
    public Long getUsedSizeRefreshInterval() {
        return this.usedSizeRefreshInterval;
    }

    public CreateDomainRequest setUserCountQuota(Long userCountQuota) {
        this.userCountQuota = userCountQuota;
        return this;
    }
    public Long getUserCountQuota() {
        return this.userCountQuota;
    }

    public CreateDomainRequest setUserSingleDriveEnabled(Boolean userSingleDriveEnabled) {
        this.userSingleDriveEnabled = userSingleDriveEnabled;
        return this;
    }
    public Boolean getUserSingleDriveEnabled() {
        return this.userSingleDriveEnabled;
    }

}
