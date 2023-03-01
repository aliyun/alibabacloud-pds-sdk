// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 查询 subdomain 概况
 */
public class GetSubdomainSummaryRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    /**
     * <p>subdomain</p>
     */
    @NameInMap("subdomain_id")
    public String subdomainId;

    public static GetSubdomainSummaryRequest build(java.util.Map<String, ?> map) throws Exception {
        GetSubdomainSummaryRequest self = new GetSubdomainSummaryRequest();
        return TeaModel.build(map, self);
    }

    public GetSubdomainSummaryRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public GetSubdomainSummaryRequest setSubdomainId(String subdomainId) {
        this.subdomainId = subdomainId;
        return this;
    }
    public String getSubdomainId() {
        return this.subdomainId;
    }

}
