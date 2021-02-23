// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class DeleteSubdomainRequest extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // 用以唯一标识subdomain
    @NameInMap("subdomain_id")
    @Validation(required = true)
    public String subdomainId;

    public static DeleteSubdomainRequest build(java.util.Map<String, ?> map) throws Exception {
        DeleteSubdomainRequest self = new DeleteSubdomainRequest();
        return TeaModel.build(map, self);
    }

    public DeleteSubdomainRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public DeleteSubdomainRequest setSubdomainId(String subdomainId) {
        this.subdomainId = subdomainId;
        return this;
    }
    public String getSubdomainId() {
        return this.subdomainId;
    }

}
