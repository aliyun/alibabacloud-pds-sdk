// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * get domain request
 */
public class GetDomainRequest extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // Domain ID
    @NameInMap("domain_id")
    @Validation(required = true)
    public String domainId;

    @NameInMap("get_benefit")
    public Boolean getBenefit;

    public static GetDomainRequest build(java.util.Map<String, ?> map) throws Exception {
        GetDomainRequest self = new GetDomainRequest();
        return TeaModel.build(map, self);
    }

    public GetDomainRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetDomainRequest setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public GetDomainRequest setGetBenefit(Boolean getBenefit) {
        this.getBenefit = getBenefit;
        return this;
    }
    public Boolean getGetBenefit() {
        return this.getBenefit;
    }

}
