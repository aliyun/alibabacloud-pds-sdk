// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class UpdateSubdomainRequest extends TeaModel {
    /**
     * <p>描述</p>
     */
    @NameInMap("description")
    public String description;

    /**
     * <p>名称</p>
     */
    @NameInMap("name")
    public String name;

    /**
     * <p>是否开启了共享</p>
     */
    @NameInMap("sharable")
    public Boolean sharable;

    /**
     * <p>是否开启了分享</p>
     */
    @NameInMap("share_link_enabled")
    public Boolean shareLinkEnabled;

    /**
     * <p>状态</p>
     */
    @NameInMap("status")
    public Long status;

    /**
     * <p>用以唯一标识subdomain</p>
     */
    @NameInMap("subdomain_id")
    @Validation(required = true)
    public String subdomainId;

    /**
     * <p>逻辑空间quota，-1表示无限制，单位为字节</p>
     */
    @NameInMap("total_size")
    public Long totalSize;

    /**
     * <p>逻辑空间刷新周期，单位：秒</p>
     */
    @NameInMap("used_size_refresh_interval")
    public Long usedSizeRefreshInterval;

    /**
     * <p>用户数quota，-1表示无限制</p>
     */
    @NameInMap("user_quota")
    public Long userQuota;

    public static UpdateSubdomainRequest build(java.util.Map<String, ?> map) throws Exception {
        UpdateSubdomainRequest self = new UpdateSubdomainRequest();
        return TeaModel.build(map, self);
    }

    public UpdateSubdomainRequest setDescription(String description) {
        this.description = description;
        return this;
    }
    public String getDescription() {
        return this.description;
    }

    public UpdateSubdomainRequest setName(String name) {
        this.name = name;
        return this;
    }
    public String getName() {
        return this.name;
    }

    public UpdateSubdomainRequest setSharable(Boolean sharable) {
        this.sharable = sharable;
        return this;
    }
    public Boolean getSharable() {
        return this.sharable;
    }

    public UpdateSubdomainRequest setShareLinkEnabled(Boolean shareLinkEnabled) {
        this.shareLinkEnabled = shareLinkEnabled;
        return this;
    }
    public Boolean getShareLinkEnabled() {
        return this.shareLinkEnabled;
    }

    public UpdateSubdomainRequest setStatus(Long status) {
        this.status = status;
        return this;
    }
    public Long getStatus() {
        return this.status;
    }

    public UpdateSubdomainRequest setSubdomainId(String subdomainId) {
        this.subdomainId = subdomainId;
        return this;
    }
    public String getSubdomainId() {
        return this.subdomainId;
    }

    public UpdateSubdomainRequest setTotalSize(Long totalSize) {
        this.totalSize = totalSize;
        return this;
    }
    public Long getTotalSize() {
        return this.totalSize;
    }

    public UpdateSubdomainRequest setUsedSizeRefreshInterval(Long usedSizeRefreshInterval) {
        this.usedSizeRefreshInterval = usedSizeRefreshInterval;
        return this;
    }
    public Long getUsedSizeRefreshInterval() {
        return this.usedSizeRefreshInterval;
    }

    public UpdateSubdomainRequest setUserQuota(Long userQuota) {
        this.userQuota = userQuota;
        return this;
    }
    public Long getUserQuota() {
        return this.userQuota;
    }

}
