// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class GetSubdomainMgmtRequest extends TeaModel {
    /**
     * <p>用以唯一标识domain</p>
     */
    @NameInMap("domain_id")
    @Validation(required = true)
    public String domainId;

    /**
     * <p>是否获取share/share_link详情</p>
     */
    @NameInMap("get_share_detail")
    public Boolean getShareDetail;

    /**
     * <p>用以唯一标识subdomain</p>
     */
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
