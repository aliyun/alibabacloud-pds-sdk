// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * get domain request
 */
public class GetDomainRequest extends TeaModel {
    /**
     * <p>Domain ID</p>
     */
    @NameInMap("domain_id")
    @Validation(required = true)
    public String domainId;

    /**
     * <p>fields,需要获取的属性字段,英文逗号分隔,*表示获取所有fields支持的枚举属性字段,为空不获取任何枚举属性字段</p>
     */
    @NameInMap("fields")
    public String fields;

    @NameInMap("get_benefit")
    public Boolean getBenefit;

    /**
     * <p>是否获取share/share_link详情</p>
     */
    @NameInMap("get_share_detail")
    public Boolean getShareDetail;

    /**
     * <p>是否 merge parent 配置</p>
     */
    @NameInMap("merge_parent")
    public Boolean mergeParent;

    public static GetDomainRequest build(java.util.Map<String, ?> map) throws Exception {
        GetDomainRequest self = new GetDomainRequest();
        return TeaModel.build(map, self);
    }

    public GetDomainRequest setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public GetDomainRequest setFields(String fields) {
        this.fields = fields;
        return this;
    }
    public String getFields() {
        return this.fields;
    }

    public GetDomainRequest setGetBenefit(Boolean getBenefit) {
        this.getBenefit = getBenefit;
        return this;
    }
    public Boolean getGetBenefit() {
        return this.getBenefit;
    }

    public GetDomainRequest setGetShareDetail(Boolean getShareDetail) {
        this.getShareDetail = getShareDetail;
        return this;
    }
    public Boolean getGetShareDetail() {
        return this.getShareDetail;
    }

    public GetDomainRequest setMergeParent(Boolean mergeParent) {
        this.mergeParent = mergeParent;
        return this;
    }
    public Boolean getMergeParent() {
        return this.mergeParent;
    }

}
