// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class GetSubdomainRequest extends TeaModel {
    /**
     * <p>用以唯一标识subdomain</p>
     */
    @NameInMap("subdomain_id")
    @Validation(required = true)
    public String subdomainId;

    public static GetSubdomainRequest build(java.util.Map<String, ?> map) throws Exception {
        GetSubdomainRequest self = new GetSubdomainRequest();
        return TeaModel.build(map, self);
    }

    public GetSubdomainRequest setSubdomainId(String subdomainId) {
        this.subdomainId = subdomainId;
        return this;
    }
    public String getSubdomainId() {
        return this.subdomainId;
    }

}
