// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class BaseSubdomainResponse extends TeaModel {
    // 创建时间
    @NameInMap("created_at")
    @Validation(required = true)
    public String createdAt;

    // 描述
    @NameInMap("description")
    @Validation(required = true)
    public String description;

    // 名称
    @NameInMap("name")
    @Validation(required = true)
    public String name;

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

    // 用户数quota，-1表示无限制
    @NameInMap("user_quota")
    @Validation(required = true)
    public Long userQuota;

    public static BaseSubdomainResponse build(java.util.Map<String, ?> map) throws Exception {
        BaseSubdomainResponse self = new BaseSubdomainResponse();
        return TeaModel.build(map, self);
    }

    public BaseSubdomainResponse setCreatedAt(String createdAt) {
        this.createdAt = createdAt;
        return this;
    }
    public String getCreatedAt() {
        return this.createdAt;
    }

    public BaseSubdomainResponse setDescription(String description) {
        this.description = description;
        return this;
    }
    public String getDescription() {
        return this.description;
    }

    public BaseSubdomainResponse setName(String name) {
        this.name = name;
        return this;
    }
    public String getName() {
        return this.name;
    }

    public BaseSubdomainResponse setSubdomainId(String subdomainId) {
        this.subdomainId = subdomainId;
        return this;
    }
    public String getSubdomainId() {
        return this.subdomainId;
    }

    public BaseSubdomainResponse setTotalSize(Long totalSize) {
        this.totalSize = totalSize;
        return this;
    }
    public Long getTotalSize() {
        return this.totalSize;
    }

    public BaseSubdomainResponse setUpdatedAt(String updatedAt) {
        this.updatedAt = updatedAt;
        return this;
    }
    public String getUpdatedAt() {
        return this.updatedAt;
    }

    public BaseSubdomainResponse setUserQuota(Long userQuota) {
        this.userQuota = userQuota;
        return this;
    }
    public Long getUserQuota() {
        return this.userQuota;
    }

}
