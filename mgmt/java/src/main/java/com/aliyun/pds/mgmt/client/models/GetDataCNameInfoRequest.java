// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class GetDataCNameInfoRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    // domain ID
    @NameInMap("domain_id")
    @Validation(required = true)
    public String domainId;

    public static GetDataCNameInfoRequest build(java.util.Map<String, ?> map) throws Exception {
        GetDataCNameInfoRequest self = new GetDataCNameInfoRequest();
        return TeaModel.build(map, self);
    }

    public GetDataCNameInfoRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public GetDataCNameInfoRequest setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

}
