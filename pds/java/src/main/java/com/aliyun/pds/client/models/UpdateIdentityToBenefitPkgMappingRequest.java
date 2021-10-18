// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * update identity to benefit pkg mapping request
 */
public class UpdateIdentityToBenefitPkgMappingRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    // 权益包数量
    @NameInMap("amount")
    public Long amount;

    // 权益包的唯一标识
    @NameInMap("benefit_pkg_id")
    @Validation(required = true)
    public String benefitPkgId;

    // 实体权益包关联的自定义Meta
    @NameInMap("custom_benefit_meta")
    public String customBenefitMeta;

    // 权益下发的唯一标识
    @NameInMap("delivery_id")
    public String deliveryId;

    // domain ID
    @NameInMap("domain_id")
    public String domainId;

    // 权益包超期时间的时间戳，单位为毫秒
    @NameInMap("expire_time")
    public Long expireTime;

    // 实体的唯一标识，如 userID
    @NameInMap("identity_id")
    @Validation(required = true)
    public String identityId;

    // 实体类型，当前支持user类型实体
    @NameInMap("identity_type")
    @Validation(required = true)
    public String identityType;

    // nonce ID
    @NameInMap("nonce_id")
    public String nonceId;

    public static UpdateIdentityToBenefitPkgMappingRequest build(java.util.Map<String, ?> map) throws Exception {
        UpdateIdentityToBenefitPkgMappingRequest self = new UpdateIdentityToBenefitPkgMappingRequest();
        return TeaModel.build(map, self);
    }

    public UpdateIdentityToBenefitPkgMappingRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public UpdateIdentityToBenefitPkgMappingRequest setAmount(Long amount) {
        this.amount = amount;
        return this;
    }
    public Long getAmount() {
        return this.amount;
    }

    public UpdateIdentityToBenefitPkgMappingRequest setBenefitPkgId(String benefitPkgId) {
        this.benefitPkgId = benefitPkgId;
        return this;
    }
    public String getBenefitPkgId() {
        return this.benefitPkgId;
    }

    public UpdateIdentityToBenefitPkgMappingRequest setCustomBenefitMeta(String customBenefitMeta) {
        this.customBenefitMeta = customBenefitMeta;
        return this;
    }
    public String getCustomBenefitMeta() {
        return this.customBenefitMeta;
    }

    public UpdateIdentityToBenefitPkgMappingRequest setDeliveryId(String deliveryId) {
        this.deliveryId = deliveryId;
        return this;
    }
    public String getDeliveryId() {
        return this.deliveryId;
    }

    public UpdateIdentityToBenefitPkgMappingRequest setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public UpdateIdentityToBenefitPkgMappingRequest setExpireTime(Long expireTime) {
        this.expireTime = expireTime;
        return this;
    }
    public Long getExpireTime() {
        return this.expireTime;
    }

    public UpdateIdentityToBenefitPkgMappingRequest setIdentityId(String identityId) {
        this.identityId = identityId;
        return this;
    }
    public String getIdentityId() {
        return this.identityId;
    }

    public UpdateIdentityToBenefitPkgMappingRequest setIdentityType(String identityType) {
        this.identityType = identityType;
        return this;
    }
    public String getIdentityType() {
        return this.identityType;
    }

    public UpdateIdentityToBenefitPkgMappingRequest setNonceId(String nonceId) {
        this.nonceId = nonceId;
        return this;
    }
    public String getNonceId() {
        return this.nonceId;
    }

}
