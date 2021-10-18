// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * list identity to benefit pkg mapping request
 */
public class ListIdentityToBenefitPkgMappingRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    // domain ID
    @NameInMap("domain_id")
    public String domainId;

    // 实体的唯一标识，如 userID
    @NameInMap("identity_id")
    @Validation(required = true)
    public String identityId;

    // 实体类型，当前支持user类型实体
    @NameInMap("identity_type")
    @Validation(required = true)
    public String identityType;

    // 是否返回已经超期的权益包，默认为false
    @NameInMap("include_expired")
    public Boolean includeExpired;

    public static ListIdentityToBenefitPkgMappingRequest build(java.util.Map<String, ?> map) throws Exception {
        ListIdentityToBenefitPkgMappingRequest self = new ListIdentityToBenefitPkgMappingRequest();
        return TeaModel.build(map, self);
    }

    public ListIdentityToBenefitPkgMappingRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public ListIdentityToBenefitPkgMappingRequest setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public ListIdentityToBenefitPkgMappingRequest setIdentityId(String identityId) {
        this.identityId = identityId;
        return this;
    }
    public String getIdentityId() {
        return this.identityId;
    }

    public ListIdentityToBenefitPkgMappingRequest setIdentityType(String identityType) {
        this.identityType = identityType;
        return this;
    }
    public String getIdentityType() {
        return this.identityType;
    }

    public ListIdentityToBenefitPkgMappingRequest setIncludeExpired(Boolean includeExpired) {
        this.includeExpired = includeExpired;
        return this;
    }
    public Boolean getIncludeExpired() {
        return this.includeExpired;
    }

}
