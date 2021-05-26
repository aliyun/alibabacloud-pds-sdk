// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * Benefit package delivery info
 */
public class BenefitPkgDeliveryInfoResponse extends TeaModel {
    // 权益包下发的数量
    @NameInMap("amount")
    public Long amount;

    // 权益包下发的创建时间
    @NameInMap("created_at")
    public String createdAt;

    // 权益包下发的超期时间，is_permanent为false时，返回有效值
    @NameInMap("expire_time")
    public String expireTime;

    // 权益包是否永久有效
    @NameInMap("is_permanent")
    public Boolean isPermanent;

    public static BenefitPkgDeliveryInfoResponse build(java.util.Map<String, ?> map) throws Exception {
        BenefitPkgDeliveryInfoResponse self = new BenefitPkgDeliveryInfoResponse();
        return TeaModel.build(map, self);
    }

    public BenefitPkgDeliveryInfoResponse setAmount(Long amount) {
        this.amount = amount;
        return this;
    }
    public Long getAmount() {
        return this.amount;
    }

    public BenefitPkgDeliveryInfoResponse setCreatedAt(String createdAt) {
        this.createdAt = createdAt;
        return this;
    }
    public String getCreatedAt() {
        return this.createdAt;
    }

    public BenefitPkgDeliveryInfoResponse setExpireTime(String expireTime) {
        this.expireTime = expireTime;
        return this;
    }
    public String getExpireTime() {
        return this.expireTime;
    }

    public BenefitPkgDeliveryInfoResponse setIsPermanent(Boolean isPermanent) {
        this.isPermanent = isPermanent;
        return this;
    }
    public Boolean getIsPermanent() {
        return this.isPermanent;
    }

}
