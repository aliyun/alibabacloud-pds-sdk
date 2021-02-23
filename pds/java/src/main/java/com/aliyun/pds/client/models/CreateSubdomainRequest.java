// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class CreateSubdomainRequest extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // 描述
    @NameInMap("description")
    public String description;

    // 名称，注意该字段会校验重名的subdomain
    @NameInMap("name")
    @Validation(required = true)
    public String name;

    // 逻辑空间quota，默认为-1，无限制，单位为字节
    @NameInMap("total_size")
    public Long totalSize;

    // 用户数quota，默认为-1，无限制
    @NameInMap("user_quota")
    public Long userQuota;

    public static CreateSubdomainRequest build(java.util.Map<String, ?> map) throws Exception {
        CreateSubdomainRequest self = new CreateSubdomainRequest();
        return TeaModel.build(map, self);
    }

    public CreateSubdomainRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public CreateSubdomainRequest setDescription(String description) {
        this.description = description;
        return this;
    }
    public String getDescription() {
        return this.description;
    }

    public CreateSubdomainRequest setName(String name) {
        this.name = name;
        return this;
    }
    public String getName() {
        return this.name;
    }

    public CreateSubdomainRequest setTotalSize(Long totalSize) {
        this.totalSize = totalSize;
        return this;
    }
    public Long getTotalSize() {
        return this.totalSize;
    }

    public CreateSubdomainRequest setUserQuota(Long userQuota) {
        this.userQuota = userQuota;
        return this;
    }
    public Long getUserQuota() {
        return this.userQuota;
    }

}
