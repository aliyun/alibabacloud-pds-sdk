// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class UpdateSubdomainRequest extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // 描述
    @NameInMap("description")
    public String description;

    // 名称
    @NameInMap("name")
    public String name;

    // 用以唯一标识subdomain
    @NameInMap("subdomain_id")
    @Validation(required = true)
    public String subdomainId;

    // 逻辑空间quota，-1表示无限制，单位为字节
    @NameInMap("total_size")
    public Long totalSize;

    // 用户数quota，-1表示无限制
    @NameInMap("user_quota")
    public Long userQuota;

    public static UpdateSubdomainRequest build(java.util.Map<String, ?> map) throws Exception {
        UpdateSubdomainRequest self = new UpdateSubdomainRequest();
        return TeaModel.build(map, self);
    }

    public UpdateSubdomainRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
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

    public UpdateSubdomainRequest setUserQuota(Long userQuota) {
        this.userQuota = userQuota;
        return this;
    }
    public Long getUserQuota() {
        return this.userQuota;
    }

}
