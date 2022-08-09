// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 *
 */
public class BaseIdentityToBenefitPkgMappingRequest extends TeaModel {
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

    public static BaseIdentityToBenefitPkgMappingRequest build(java.util.Map<String, ?> map) throws Exception {
        BaseIdentityToBenefitPkgMappingRequest self = new BaseIdentityToBenefitPkgMappingRequest();
        return TeaModel.build(map, self);
    }

    public BaseIdentityToBenefitPkgMappingRequest setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public BaseIdentityToBenefitPkgMappingRequest setIdentityId(String identityId) {
        this.identityId = identityId;
        return this;
    }
    public String getIdentityId() {
        return this.identityId;
    }

    public BaseIdentityToBenefitPkgMappingRequest setIdentityType(String identityType) {
        this.identityType = identityType;
        return this;
    }
    public String getIdentityType() {
        return this.identityType;
    }

}
