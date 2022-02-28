// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class GetSubdomainMgmtRequest extends TeaModel {
    // 用以唯一标识domain
    @NameInMap("domain_id")
    @Validation(required = true)
    public String domainId;

    // 是否获取share/share_link详情
    @NameInMap("get_share_detail")
    public Boolean getShareDetail;

    // 用以唯一标识subdomain
    @NameInMap("subdomain_id")
    @Validation(required = true)
    public String subdomainId;

    public static GetSubdomainMgmtRequest build(java.util.Map<String, ?> map) throws Exception {
        GetSubdomainMgmtRequest self = new GetSubdomainMgmtRequest();
        return TeaModel.build(map, self);
    }

    public GetSubdomainMgmtRequest setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public GetSubdomainMgmtRequest setGetShareDetail(Boolean getShareDetail) {
        this.getShareDetail = getShareDetail;
        return this;
    }
    public Boolean getGetShareDetail() {
        return this.getShareDetail;
    }

    public GetSubdomainMgmtRequest setSubdomainId(String subdomainId) {
        this.subdomainId = subdomainId;
        return this;
    }
    public String getSubdomainId() {
        return this.subdomainId;
    }

}
