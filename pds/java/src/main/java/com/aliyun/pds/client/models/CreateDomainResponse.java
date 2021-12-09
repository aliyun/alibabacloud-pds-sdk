// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

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

    @NameInMap("app_config")
    public AppConfig appConfig;

    // 打包下载配置
    @NameInMap("archive_files_enable")
    public Boolean archiveFilesEnable;

    @NameInMap("audit_log_config")
    public AuditLogConfig auditLogConfig;

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

    @NameInMap("benefits")
    public java.util.Map<String, ?> benefits;

    // Domain 创建时间
    @NameInMap("created_at")
    public String createdAt;

    // 数据 Hash 算法
    @NameInMap("data_hash_name")
    public String dataHashName;

    @NameInMap("default_super_admin_config")
    public DomainSuperAdminConfig defaultSuperAdminConfig;

    // Domain 描述
    @NameInMap("description")
    public String description;

    // Domain ID
    @NameInMap("domain_id")
    public String domainId;

    // Domain 描述
    @NameInMap("domain_name")
    public String domainName;

    // 企业文件管理专属登录开关
    @NameInMap("enterprise_customized_login")
    public Boolean enterpriseCustomizedLogin;

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

    // 预付费domain过期时间
    @NameInMap("expire_time")
    public Long expireTime;

    @NameInMap("group_single_drive_enabled")
    public Boolean groupSingleDriveEnabled;

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

    @NameInMap("office_edit_config")
    public OfficeEditConfig officeEditConfig;

    @NameInMap("office_preview_config")
    public OfficePreviewConfig officePreviewConfig;

    @NameInMap("parallel_upload_enabled")
    public Boolean parallelUploadEnabled;

    // Domain 类型
    @NameInMap("path_type")
    public String pathType;

    // 预付费套餐
    @NameInMap("prepaid_package")
    public String prepaidPackage;

    @NameInMap("published_app_access_strategy")
    public AppAccessStrategy publishedAppAccessStrategy;

    @NameInMap("role_config")
    public RoleConfig roleConfig;

    // Domain ServiceCode
    @NameInMap("service_code")
    public String serviceCode;

    // 是否开启了共享
    @NameInMap("sharable")
    public Boolean sharable;

    @NameInMap("share_detail")
    public ShareDetailResponse shareDetail;

    @NameInMap("share_link_detail")
    public ShareDetailResponse shareLinkDetail;

    // 是否开启了分享
    @NameInMap("share_link_enabled")
    public Boolean shareLinkEnabled;

    // 容量配额
    @NameInMap("size_quota")
    public Long sizeQuota;

    // SPI 实例 id
    @NameInMap("spi_instance_id")
    public String spiInstanceId;

    // domain状态：创建中，正常，已过期
    @NameInMap("status")
    public Long status;

    // 存储级别
    @NameInMap("store_level")
    public String storeLevel;

    // 存储 Region 列表
    @NameInMap("store_region_list")
    public java.util.List<String> storeRegionList;

    // Domain 更新时间
    @NameInMap("updated_at")
    public String updatedAt;

    // 用户数配额
    @NameInMap("user_count_quota")
    public Long userCountQuota;

    // user和group只能有一个drive的开关
    @NameInMap("user_single_drive_enabled")
    public Boolean userSingleDriveEnabled;

    @NameInMap("video_preview_app_config")
    public VideoPreviewAppConfig videoPreviewAppConfig;

    @NameInMap("video_preview_config")
    public VideoPreviewConfig videoPreviewConfig;

    @NameInMap("watermark_config")
    public BaseWatermarkConfigResponse watermarkConfig;

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

    public CreateDomainResponse setAppConfig(AppConfig appConfig) {
        this.appConfig = appConfig;
        return this;
    }
    public AppConfig getAppConfig() {
        return this.appConfig;
    }

    public CreateDomainResponse setArchiveFilesEnable(Boolean archiveFilesEnable) {
        this.archiveFilesEnable = archiveFilesEnable;
        return this;
    }
    public Boolean getArchiveFilesEnable() {
        return this.archiveFilesEnable;
    }

    public CreateDomainResponse setAuditLogConfig(AuditLogConfig auditLogConfig) {
        this.auditLogConfig = auditLogConfig;
        return this;
    }
    public AuditLogConfig getAuditLogConfig() {
        return this.auditLogConfig;
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

    public CreateDomainResponse setBenefits(java.util.Map<String, ?> benefits) {
        this.benefits = benefits;
        return this;
    }
    public java.util.Map<String, ?> getBenefits() {
        return this.benefits;
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

    public CreateDomainResponse setDefaultSuperAdminConfig(DomainSuperAdminConfig defaultSuperAdminConfig) {
        this.defaultSuperAdminConfig = defaultSuperAdminConfig;
        return this;
    }
    public DomainSuperAdminConfig getDefaultSuperAdminConfig() {
        return this.defaultSuperAdminConfig;
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

    public CreateDomainResponse setEnterpriseCustomizedLogin(Boolean enterpriseCustomizedLogin) {
        this.enterpriseCustomizedLogin = enterpriseCustomizedLogin;
        return this;
    }
    public Boolean getEnterpriseCustomizedLogin() {
        return this.enterpriseCustomizedLogin;
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

    public CreateDomainResponse setExpireTime(Long expireTime) {
        this.expireTime = expireTime;
        return this;
    }
    public Long getExpireTime() {
        return this.expireTime;
    }

    public CreateDomainResponse setGroupSingleDriveEnabled(Boolean groupSingleDriveEnabled) {
        this.groupSingleDriveEnabled = groupSingleDriveEnabled;
        return this;
    }
    public Boolean getGroupSingleDriveEnabled() {
        return this.groupSingleDriveEnabled;
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

    public CreateDomainResponse setOfficeEditConfig(OfficeEditConfig officeEditConfig) {
        this.officeEditConfig = officeEditConfig;
        return this;
    }
    public OfficeEditConfig getOfficeEditConfig() {
        return this.officeEditConfig;
    }

    public CreateDomainResponse setOfficePreviewConfig(OfficePreviewConfig officePreviewConfig) {
        this.officePreviewConfig = officePreviewConfig;
        return this;
    }
    public OfficePreviewConfig getOfficePreviewConfig() {
        return this.officePreviewConfig;
    }

    public CreateDomainResponse setParallelUploadEnabled(Boolean parallelUploadEnabled) {
        this.parallelUploadEnabled = parallelUploadEnabled;
        return this;
    }
    public Boolean getParallelUploadEnabled() {
        return this.parallelUploadEnabled;
    }

    public CreateDomainResponse setPathType(String pathType) {
        this.pathType = pathType;
        return this;
    }
    public String getPathType() {
        return this.pathType;
    }

    public CreateDomainResponse setPrepaidPackage(String prepaidPackage) {
        this.prepaidPackage = prepaidPackage;
        return this;
    }
    public String getPrepaidPackage() {
        return this.prepaidPackage;
    }

    public CreateDomainResponse setPublishedAppAccessStrategy(AppAccessStrategy publishedAppAccessStrategy) {
        this.publishedAppAccessStrategy = publishedAppAccessStrategy;
        return this;
    }
    public AppAccessStrategy getPublishedAppAccessStrategy() {
        return this.publishedAppAccessStrategy;
    }

    public CreateDomainResponse setRoleConfig(RoleConfig roleConfig) {
        this.roleConfig = roleConfig;
        return this;
    }
    public RoleConfig getRoleConfig() {
        return this.roleConfig;
    }

    public CreateDomainResponse setServiceCode(String serviceCode) {
        this.serviceCode = serviceCode;
        return this;
    }
    public String getServiceCode() {
        return this.serviceCode;
    }

    public CreateDomainResponse setSharable(Boolean sharable) {
        this.sharable = sharable;
        return this;
    }
    public Boolean getSharable() {
        return this.sharable;
    }

    public CreateDomainResponse setShareDetail(ShareDetailResponse shareDetail) {
        this.shareDetail = shareDetail;
        return this;
    }
    public ShareDetailResponse getShareDetail() {
        return this.shareDetail;
    }

    public CreateDomainResponse setShareLinkDetail(ShareDetailResponse shareLinkDetail) {
        this.shareLinkDetail = shareLinkDetail;
        return this;
    }
    public ShareDetailResponse getShareLinkDetail() {
        return this.shareLinkDetail;
    }

    public CreateDomainResponse setShareLinkEnabled(Boolean shareLinkEnabled) {
        this.shareLinkEnabled = shareLinkEnabled;
        return this;
    }
    public Boolean getShareLinkEnabled() {
        return this.shareLinkEnabled;
    }

    public CreateDomainResponse setSizeQuota(Long sizeQuota) {
        this.sizeQuota = sizeQuota;
        return this;
    }
    public Long getSizeQuota() {
        return this.sizeQuota;
    }

    public CreateDomainResponse setSpiInstanceId(String spiInstanceId) {
        this.spiInstanceId = spiInstanceId;
        return this;
    }
    public String getSpiInstanceId() {
        return this.spiInstanceId;
    }

    public CreateDomainResponse setStatus(Long status) {
        this.status = status;
        return this;
    }
    public Long getStatus() {
        return this.status;
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

    public CreateDomainResponse setUserCountQuota(Long userCountQuota) {
        this.userCountQuota = userCountQuota;
        return this;
    }
    public Long getUserCountQuota() {
        return this.userCountQuota;
    }

    public CreateDomainResponse setUserSingleDriveEnabled(Boolean userSingleDriveEnabled) {
        this.userSingleDriveEnabled = userSingleDriveEnabled;
        return this;
    }
    public Boolean getUserSingleDriveEnabled() {
        return this.userSingleDriveEnabled;
    }

    public CreateDomainResponse setVideoPreviewAppConfig(VideoPreviewAppConfig videoPreviewAppConfig) {
        this.videoPreviewAppConfig = videoPreviewAppConfig;
        return this;
    }
    public VideoPreviewAppConfig getVideoPreviewAppConfig() {
        return this.videoPreviewAppConfig;
    }

    public CreateDomainResponse setVideoPreviewConfig(VideoPreviewConfig videoPreviewConfig) {
        this.videoPreviewConfig = videoPreviewConfig;
        return this;
    }
    public VideoPreviewConfig getVideoPreviewConfig() {
        return this.videoPreviewConfig;
    }

    public CreateDomainResponse setWatermarkConfig(BaseWatermarkConfigResponse watermarkConfig) {
        this.watermarkConfig = watermarkConfig;
        return this;
    }
    public BaseWatermarkConfigResponse getWatermarkConfig() {
        return this.watermarkConfig;
    }

}
