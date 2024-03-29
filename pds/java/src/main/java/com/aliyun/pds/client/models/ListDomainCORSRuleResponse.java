// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * list domain cors response
 */
public class ListDomainCORSRuleResponse extends TeaModel {
    /**
     * <p>cors rule 列表</p>
     */
    @NameInMap("cors_rule_list")
    public java.util.List<CorsRule> corsRuleList;

    /**
     * <p>Domain ID</p>
     */
    @NameInMap("domain_id")
    public String domainId;

    public static ListDomainCORSRuleResponse build(java.util.Map<String, ?> map) throws Exception {
        ListDomainCORSRuleResponse self = new ListDomainCORSRuleResponse();
        return TeaModel.build(map, self);
    }

    public ListDomainCORSRuleResponse setCorsRuleList(java.util.List<CorsRule> corsRuleList) {
        this.corsRuleList = corsRuleList;
        return this;
    }
    public java.util.List<CorsRule> getCorsRuleList() {
        return this.corsRuleList;
    }

    public ListDomainCORSRuleResponse setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

}
