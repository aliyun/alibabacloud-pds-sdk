// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class GetSubdomainResponse extends TeaModel {
    // 创建时间
    @NameInMap("created_at")
    @Validation(required = true)
    public String createdAt;

    // 描述
    @NameInMap("description")
    @Validation(required = true)
    public String description;

    @NameInMap("group_singe_drive_enable")
    public Boolean groupSingeDriveEnable;

    // 名称
    @NameInMap("name")
    @Validation(required = true)
    public String name;

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

    // 当前状态
    @NameInMap("status")
    public Long status;

    // 用以唯一标识subdomain
    @NameInMap("subdomain_id")
    @Validation(required = true)
    public String subdomainId;

    // 逻辑空间quota，-1表示无限制，单位为字节
    @NameInMap("total_size")
    @Validation(required = true)
    public Long totalSize;

    // 更新时间
    @NameInMap("updated_at")
    @Validation(required = true)
    public String updatedAt;

    // 逻辑空间使用量，单位为字节
    @NameInMap("used_size")
    public Long usedSize;

    // 逻辑空间刷新周期，单位：秒
    @NameInMap("used_size_refresh_interval")
    public Long usedSizeRefreshInterval;

    // 用户数quota，-1表示无限制
    @NameInMap("user_quota")
    @Validation(required = true)
    public Long userQuota;

    @NameInMap("user_single_drive_enabled")
    public Boolean userSingleDriveEnabled;

    public static GetSubdomainResponse build(java.util.Map<String, ?> map) throws Exception {
        GetSubdomainResponse self = new GetSubdomainResponse();
        return TeaModel.build(map, self);
    }

    public GetSubdomainResponse setCreatedAt(String createdAt) {
        this.createdAt = createdAt;
        return this;
    }
    public String getCreatedAt() {
        return this.createdAt;
    }

    public GetSubdomainResponse setDescription(String description) {
        this.description = description;
        return this;
    }
    public String getDescription() {
        return this.description;
    }

    public GetSubdomainResponse setGroupSingeDriveEnable(Boolean groupSingeDriveEnable) {
        this.groupSingeDriveEnable = groupSingeDriveEnable;
        return this;
    }
    public Boolean getGroupSingeDriveEnable() {
        return this.groupSingeDriveEnable;
    }

    public GetSubdomainResponse setName(String name) {
        this.name = name;
        return this;
    }
    public String getName() {
        return this.name;
    }

    public GetSubdomainResponse setSharable(Boolean sharable) {
        this.sharable = sharable;
        return this;
    }
    public Boolean getSharable() {
        return this.sharable;
    }

    public GetSubdomainResponse setShareDetail(ShareDetailResponse shareDetail) {
        this.shareDetail = shareDetail;
        return this;
    }
    public ShareDetailResponse getShareDetail() {
        return this.shareDetail;
    }

    public GetSubdomainResponse setShareLinkDetail(ShareDetailResponse shareLinkDetail) {
        this.shareLinkDetail = shareLinkDetail;
        return this;
    }
    public ShareDetailResponse getShareLinkDetail() {
        return this.shareLinkDetail;
    }

    public GetSubdomainResponse setShareLinkEnabled(Boolean shareLinkEnabled) {
        this.shareLinkEnabled = shareLinkEnabled;
        return this;
    }
    public Boolean getShareLinkEnabled() {
        return this.shareLinkEnabled;
    }

    public GetSubdomainResponse setStatus(Long status) {
        this.status = status;
        return this;
    }
    public Long getStatus() {
        return this.status;
    }

    public GetSubdomainResponse setSubdomainId(String subdomainId) {
        this.subdomainId = subdomainId;
        return this;
    }
    public String getSubdomainId() {
        return this.subdomainId;
    }

    public GetSubdomainResponse setTotalSize(Long totalSize) {
        this.totalSize = totalSize;
        return this;
    }
    public Long getTotalSize() {
        return this.totalSize;
    }

    public GetSubdomainResponse setUpdatedAt(String updatedAt) {
        this.updatedAt = updatedAt;
        return this;
    }
    public String getUpdatedAt() {
        return this.updatedAt;
    }

    public GetSubdomainResponse setUsedSize(Long usedSize) {
        this.usedSize = usedSize;
        return this;
    }
    public Long getUsedSize() {
        return this.usedSize;
    }

    public GetSubdomainResponse setUsedSizeRefreshInterval(Long usedSizeRefreshInterval) {
        this.usedSizeRefreshInterval = usedSizeRefreshInterval;
        return this;
    }
    public Long getUsedSizeRefreshInterval() {
        return this.usedSizeRefreshInterval;
    }

    public GetSubdomainResponse setUserQuota(Long userQuota) {
        this.userQuota = userQuota;
        return this;
    }
    public Long getUserQuota() {
        return this.userQuota;
    }

    public GetSubdomainResponse setUserSingleDriveEnabled(Boolean userSingleDriveEnabled) {
        this.userSingleDriveEnabled = userSingleDriveEnabled;
        return this;
    }
    public Boolean getUserSingleDriveEnabled() {
        return this.userSingleDriveEnabled;
    }

}
