// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 *
 */
public class BaseIdentityBenefitPkgDeliveryInfoRequest extends TeaModel {
    // 权益包数量
    @NameInMap("amount")
    public Long amount;

    // 权益下发的唯一标识
    @NameInMap("delivery_id")
    public String deliveryId;

    // 权益包超期时间的时间戳，单位为毫秒
    @NameInMap("expire_time")
    public Long expireTime;

    public static BaseIdentityBenefitPkgDeliveryInfoRequest build(java.util.Map<String, ?> map) throws Exception {
        BaseIdentityBenefitPkgDeliveryInfoRequest self = new BaseIdentityBenefitPkgDeliveryInfoRequest();
        return TeaModel.build(map, self);
    }

    public BaseIdentityBenefitPkgDeliveryInfoRequest setAmount(Long amount) {
        this.amount = amount;
        return this;
    }
    public Long getAmount() {
        return this.amount;
    }

    public BaseIdentityBenefitPkgDeliveryInfoRequest setDeliveryId(String deliveryId) {
        this.deliveryId = deliveryId;
        return this;
    }
    public String getDeliveryId() {
        return this.deliveryId;
    }

    public BaseIdentityBenefitPkgDeliveryInfoRequest setExpireTime(Long expireTime) {
        this.expireTime = expireTime;
        return this;
    }
    public Long getExpireTime() {
        return this.expireTime;
    }

}
