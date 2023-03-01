// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * list cors rule request
 */
public class SetCorsRuleListRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    /**
     * <p>cors rule list</p>
     */
    @NameInMap("cors_rule_list")
    @Validation(required = true)
    public java.util.List<CorsRule> corsRuleList;

    /**
     * <p>domain ID</p>
     */
    @NameInMap("domain_id")
    @Validation(required = true)
    public String domainId;

    public static SetCorsRuleListRequest build(java.util.Map<String, ?> map) throws Exception {
        SetCorsRuleListRequest self = new SetCorsRuleListRequest();
        return TeaModel.build(map, self);
    }

    public SetCorsRuleListRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public SetCorsRuleListRequest setCorsRuleList(java.util.List<CorsRule> corsRuleList) {
        this.corsRuleList = corsRuleList;
        return this;
    }
    public java.util.List<CorsRule> getCorsRuleList() {
        return this.corsRuleList;
    }

    public SetCorsRuleListRequest setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

}
