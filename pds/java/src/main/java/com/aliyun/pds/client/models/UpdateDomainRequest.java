// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * update domain request
 */
public class UpdateDomainRequest extends TeaModel {
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

    @NameInMap("custom_benefits")
    public java.util.Map<String, ?> customBenefits;

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
     * <p>Domain ID</p>
     */
    @NameInMap("domain_id")
    @Validation(required = true)
    public String domainId;

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

    @NameInMap("get_benefit")
    public Boolean getBenefit;

    /**
     * <p>单团队单drive</p>
     */
    @NameInMap("group_single_drive_enabled")
    public Boolean groupSingleDriveEnabled;

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
     * <p>自动初始化 Drive 使用 Store ID</p>
     */
    @NameInMap("init_drive_store_id")
    public String initDriveStoreId;

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
     * <p>状态</p>
     */
    @NameInMap("status")
    public Long status;

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

    public UpdateDomainRequest setCustomBenefits(java.util.Map<String, ?> customBenefits) {
        this.customBenefits = customBenefits;
        return this;
    }
    public java.util.Map<String, ?> getCustomBenefits() {
        return this.customBenefits;
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

    public UpdateDomainRequest setGetBenefit(Boolean getBenefit) {
        this.getBenefit = getBenefit;
        return this;
    }
    public Boolean getGetBenefit() {
        return this.getBenefit;
    }

    public UpdateDomainRequest setGroupSingleDriveEnabled(Boolean groupSingleDriveEnabled) {
        this.groupSingleDriveEnabled = groupSingleDriveEnabled;
        return this;
    }
    public Boolean getGroupSingleDriveEnabled() {
        return this.groupSingleDriveEnabled;
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

    public UpdateDomainRequest setSizeQuota(Long sizeQuota) {
        this.sizeQuota = sizeQuota;
        return this;
    }
    public Long getSizeQuota() {
        return this.sizeQuota;
    }

    public UpdateDomainRequest setStatus(Long status) {
        this.status = status;
        return this;
    }
    public Long getStatus() {
        return this.status;
    }

    public UpdateDomainRequest setUsedSizeRefreshInterval(Long usedSizeRefreshInterval) {
        this.usedSizeRefreshInterval = usedSizeRefreshInterval;
        return this;
    }
    public Long getUsedSizeRefreshInterval() {
        return this.usedSizeRefreshInterval;
    }

    public UpdateDomainRequest setUserCountQuota(Long userCountQuota) {
        this.userCountQuota = userCountQuota;
        return this;
    }
    public Long getUserCountQuota() {
        return this.userCountQuota;
    }

    public UpdateDomainRequest setUserSingleDriveEnabled(Boolean userSingleDriveEnabled) {
        this.userSingleDriveEnabled = userSingleDriveEnabled;
        return this;
    }
    public Boolean getUserSingleDriveEnabled() {
        return this.userSingleDriveEnabled;
    }

}
