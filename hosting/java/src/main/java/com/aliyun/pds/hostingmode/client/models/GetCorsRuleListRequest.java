// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.hostingmode.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class GetCorsRuleListRequest extends TeaModel {
    // domain ID
    @NameInMap("domain_id")
    @Validation(required = true)
    public String domainId;

    public static GetCorsRuleListRequest build(java.util.Map<String, ?> map) throws Exception {
        GetCorsRuleListRequest self = new GetCorsRuleListRequest();
        return TeaModel.build(map, self);
    }

    public GetCorsRuleListRequest setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

}
