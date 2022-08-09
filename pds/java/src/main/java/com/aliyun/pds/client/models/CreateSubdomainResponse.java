// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 *
 */
public class CreateSubdomainResponse extends TeaModel {
    // 用以唯一标识subdomain
    @NameInMap("subdomain_id")
    @Validation(required = true)
    public String subdomainId;

    public static CreateSubdomainResponse build(java.util.Map<String, ?> map) throws Exception {
        CreateSubdomainResponse self = new CreateSubdomainResponse();
        return TeaModel.build(map, self);
    }

    public CreateSubdomainResponse setSubdomainId(String subdomainId) {
        this.subdomainId = subdomainId;
        return this;
    }
    public String getSubdomainId() {
        return this.subdomainId;
    }

}
