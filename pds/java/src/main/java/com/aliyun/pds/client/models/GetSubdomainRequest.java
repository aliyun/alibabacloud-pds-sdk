// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class GetSubdomainRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    // 用以唯一标识subdomain
    @NameInMap("subdomain_id")
    @Validation(required = true)
    public String subdomainId;

    public static GetSubdomainRequest build(java.util.Map<String, ?> map) throws Exception {
        GetSubdomainRequest self = new GetSubdomainRequest();
        return TeaModel.build(map, self);
    }

    public GetSubdomainRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public GetSubdomainRequest setSubdomainId(String subdomainId) {
        this.subdomainId = subdomainId;
        return this;
    }
    public String getSubdomainId() {
        return this.subdomainId;
    }

}
