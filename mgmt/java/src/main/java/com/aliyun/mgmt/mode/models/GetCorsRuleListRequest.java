// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.mgmt.mode.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class GetCorsRuleListRequest extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // domain ID
    @NameInMap("domain_id")
    @Validation(required = true)
    public String domainId;

    public static GetCorsRuleListRequest build(java.util.Map<String, ?> map) throws Exception {
        GetCorsRuleListRequest self = new GetCorsRuleListRequest();
        return TeaModel.build(map, self);
    }

    public GetCorsRuleListRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetCorsRuleListRequest setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

}
