// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * get identity to benefit pkg mapping request
 */
public class GetIdentityToBenefitPkgMappingRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    /**
     * <p>权益包的唯一标识</p>
     */
    @NameInMap("benefit_pkg_id")
    @Validation(required = true)
    public String benefitPkgId;

    /**
     * <p>domain ID</p>
     */
    @NameInMap("domain_id")
    public String domainId;

    /**
     * <p>实体的唯一标识，如 userID</p>
     */
    @NameInMap("identity_id")
    @Validation(required = true)
    public String identityId;

    /**
     * <p>实体类型，当前支持user类型实体</p>
     */
    @NameInMap("identity_type")
    @Validation(required = true)
    public String identityType;

    public static GetIdentityToBenefitPkgMappingRequest build(java.util.Map<String, ?> map) throws Exception {
        GetIdentityToBenefitPkgMappingRequest self = new GetIdentityToBenefitPkgMappingRequest();
        return TeaModel.build(map, self);
    }

    public GetIdentityToBenefitPkgMappingRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public GetIdentityToBenefitPkgMappingRequest setBenefitPkgId(String benefitPkgId) {
        this.benefitPkgId = benefitPkgId;
        return this;
    }
    public String getBenefitPkgId() {
        return this.benefitPkgId;
    }

    public GetIdentityToBenefitPkgMappingRequest setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public GetIdentityToBenefitPkgMappingRequest setIdentityId(String identityId) {
        this.identityId = identityId;
        return this;
    }
    public String getIdentityId() {
        return this.identityId;
    }

    public GetIdentityToBenefitPkgMappingRequest setIdentityType(String identityType) {
        this.identityType = identityType;
        return this;
    }
    public String getIdentityType() {
        return this.identityType;
    }

}
