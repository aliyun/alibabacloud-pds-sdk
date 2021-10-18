// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * Identity to benefit pkg mapping info
 */
public class BaseIdentityToBenefitPkgMappingResponse extends TeaModel {
    @NameInMap("benefit_pkg_computation_rule")
    public String benefitPkgComputationRule;

    @NameInMap("benefit_pkg_id")
    public String benefitPkgId;

    @NameInMap("benefit_pkg_name")
    public String benefitPkgName;

    @NameInMap("benefit_pkg_owner_id")
    public String benefitPkgOwnerId;

    @NameInMap("benefit_pkg_priority")
    public Long benefitPkgPriority;

    @NameInMap("benefit_pkg_type")
    public String benefitPkgType;

    @NameInMap("created_at")
    public String createdAt;

    @NameInMap("custom_benefit_meta")
    public java.util.Map<String, ?> customBenefitMeta;

    @NameInMap("delivery_info_list")
    public java.util.List<BenefitPkgDeliveryInfoResponse> deliveryInfoList;

    @NameInMap("identity_id")
    public String identityId;

    @NameInMap("identity_type")
    public String identityType;

    @NameInMap("updated_at")
    public String updatedAt;

    public static BaseIdentityToBenefitPkgMappingResponse build(java.util.Map<String, ?> map) throws Exception {
        BaseIdentityToBenefitPkgMappingResponse self = new BaseIdentityToBenefitPkgMappingResponse();
        return TeaModel.build(map, self);
    }

    public BaseIdentityToBenefitPkgMappingResponse setBenefitPkgComputationRule(String benefitPkgComputationRule) {
        this.benefitPkgComputationRule = benefitPkgComputationRule;
        return this;
    }
    public String getBenefitPkgComputationRule() {
        return this.benefitPkgComputationRule;
    }

    public BaseIdentityToBenefitPkgMappingResponse setBenefitPkgId(String benefitPkgId) {
        this.benefitPkgId = benefitPkgId;
        return this;
    }
    public String getBenefitPkgId() {
        return this.benefitPkgId;
    }

    public BaseIdentityToBenefitPkgMappingResponse setBenefitPkgName(String benefitPkgName) {
        this.benefitPkgName = benefitPkgName;
        return this;
    }
    public String getBenefitPkgName() {
        return this.benefitPkgName;
    }

    public BaseIdentityToBenefitPkgMappingResponse setBenefitPkgOwnerId(String benefitPkgOwnerId) {
        this.benefitPkgOwnerId = benefitPkgOwnerId;
        return this;
    }
    public String getBenefitPkgOwnerId() {
        return this.benefitPkgOwnerId;
    }

    public BaseIdentityToBenefitPkgMappingResponse setBenefitPkgPriority(Long benefitPkgPriority) {
        this.benefitPkgPriority = benefitPkgPriority;
        return this;
    }
    public Long getBenefitPkgPriority() {
        return this.benefitPkgPriority;
    }

    public BaseIdentityToBenefitPkgMappingResponse setBenefitPkgType(String benefitPkgType) {
        this.benefitPkgType = benefitPkgType;
        return this;
    }
    public String getBenefitPkgType() {
        return this.benefitPkgType;
    }

    public BaseIdentityToBenefitPkgMappingResponse setCreatedAt(String createdAt) {
        this.createdAt = createdAt;
        return this;
    }
    public String getCreatedAt() {
        return this.createdAt;
    }

    public BaseIdentityToBenefitPkgMappingResponse setCustomBenefitMeta(java.util.Map<String, ?> customBenefitMeta) {
        this.customBenefitMeta = customBenefitMeta;
        return this;
    }
    public java.util.Map<String, ?> getCustomBenefitMeta() {
        return this.customBenefitMeta;
    }

    public BaseIdentityToBenefitPkgMappingResponse setDeliveryInfoList(java.util.List<BenefitPkgDeliveryInfoResponse> deliveryInfoList) {
        this.deliveryInfoList = deliveryInfoList;
        return this;
    }
    public java.util.List<BenefitPkgDeliveryInfoResponse> getDeliveryInfoList() {
        return this.deliveryInfoList;
    }

    public BaseIdentityToBenefitPkgMappingResponse setIdentityId(String identityId) {
        this.identityId = identityId;
        return this;
    }
    public String getIdentityId() {
        return this.identityId;
    }

    public BaseIdentityToBenefitPkgMappingResponse setIdentityType(String identityType) {
        this.identityType = identityType;
        return this;
    }
    public String getIdentityType() {
        return this.identityType;
    }

    public BaseIdentityToBenefitPkgMappingResponse setUpdatedAt(String updatedAt) {
        this.updatedAt = updatedAt;
        return this;
    }
    public String getUpdatedAt() {
        return this.updatedAt;
    }

}
