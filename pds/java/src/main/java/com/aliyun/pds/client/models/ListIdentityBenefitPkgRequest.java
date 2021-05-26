// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * List identity benefit package request
 */
public class ListIdentityBenefitPkgRequest extends TeaModel {
    // 查询特定的benefit ID，include_benefit为true时有效。 如果为空，不做任何过滤；如果不为空，只返回包含特定benefit ID的权益包；也只返回权益包中特定的权益信息。
    @NameInMap("benefit_id_list")
    public java.util.List<String> benefitIdList;

    // domain ID AK方式访问，参数identity_type为user时，该项必传
    @NameInMap("domain_id")
    public String domainId;

    // 实体类型，目前只支持查询user类型实体绑定的权益包
    @NameInMap("identity_type")
    @Validation(required = true)
    public String identityType;

    // 是否返回权益包中的权益，默认为false
    @NameInMap("include_benefit")
    public Boolean includeBenefit;

    // 是否返回已经超期的权益包，默认为false
    @NameInMap("include_expired")
    public Boolean includeExpired;

    // 用户 ID, AK方式访问，参数identity_type为user时，该项必传
    @NameInMap("user_id")
    public String userId;

    public static ListIdentityBenefitPkgRequest build(java.util.Map<String, ?> map) throws Exception {
        ListIdentityBenefitPkgRequest self = new ListIdentityBenefitPkgRequest();
        return TeaModel.build(map, self);
    }

    public ListIdentityBenefitPkgRequest setBenefitIdList(java.util.List<String> benefitIdList) {
        this.benefitIdList = benefitIdList;
        return this;
    }
    public java.util.List<String> getBenefitIdList() {
        return this.benefitIdList;
    }

    public ListIdentityBenefitPkgRequest setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public ListIdentityBenefitPkgRequest setIdentityType(String identityType) {
        this.identityType = identityType;
        return this;
    }
    public String getIdentityType() {
        return this.identityType;
    }

    public ListIdentityBenefitPkgRequest setIncludeBenefit(Boolean includeBenefit) {
        this.includeBenefit = includeBenefit;
        return this;
    }
    public Boolean getIncludeBenefit() {
        return this.includeBenefit;
    }

    public ListIdentityBenefitPkgRequest setIncludeExpired(Boolean includeExpired) {
        this.includeExpired = includeExpired;
        return this;
    }
    public Boolean getIncludeExpired() {
        return this.includeExpired;
    }

    public ListIdentityBenefitPkgRequest setUserId(String userId) {
        this.userId = userId;
        return this;
    }
    public String getUserId() {
        return this.userId;
    }

}
