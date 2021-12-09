// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class DeleteSubdomainResponse extends TeaModel {
    // 用以唯一标识subdomain
    @NameInMap("subdomain_id")
    @Validation(required = true)
    public String subdomainId;

    public static DeleteSubdomainResponse build(java.util.Map<String, ?> map) throws Exception {
        DeleteSubdomainResponse self = new DeleteSubdomainResponse();
        return TeaModel.build(map, self);
    }

    public DeleteSubdomainResponse setSubdomainId(String subdomainId) {
        this.subdomainId = subdomainId;
        return this;
    }
    public String getSubdomainId() {
        return this.subdomainId;
    }

}
