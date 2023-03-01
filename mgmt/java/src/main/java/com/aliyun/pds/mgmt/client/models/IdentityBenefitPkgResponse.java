// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * Identity benefit package response
 */
public class IdentityBenefitPkgResponse extends TeaModel {
    /**
     * <p>权益包中的权益列表</p>
     */
    @NameInMap("benefit_list")
    public java.util.List<BenefitBaseResponse> benefitList;

    /**
     * <p>权益包的唯一标识</p>
     */
    @NameInMap("benefit_pkg_id")
    public String benefitPkgId;

    /**
     * <p>权益包的下发信息</p>
     */
    @NameInMap("delivery_info_list")
    public java.util.List<BenefitPkgDeliveryInfoResponse> deliveryInfoList;

    /**
     * <p>权益包的名称</p>
     */
    @NameInMap("name")
    public String name;

    public static IdentityBenefitPkgResponse build(java.util.Map<String, ?> map) throws Exception {
        IdentityBenefitPkgResponse self = new IdentityBenefitPkgResponse();
        return TeaModel.build(map, self);
    }

    public IdentityBenefitPkgResponse setBenefitList(java.util.List<BenefitBaseResponse> benefitList) {
        this.benefitList = benefitList;
        return this;
    }
    public java.util.List<BenefitBaseResponse> getBenefitList() {
        return this.benefitList;
    }

    public IdentityBenefitPkgResponse setBenefitPkgId(String benefitPkgId) {
        this.benefitPkgId = benefitPkgId;
        return this;
    }
    public String getBenefitPkgId() {
        return this.benefitPkgId;
    }

    public IdentityBenefitPkgResponse setDeliveryInfoList(java.util.List<BenefitPkgDeliveryInfoResponse> deliveryInfoList) {
        this.deliveryInfoList = deliveryInfoList;
        return this;
    }
    public java.util.List<BenefitPkgDeliveryInfoResponse> getDeliveryInfoList() {
        return this.deliveryInfoList;
    }

    public IdentityBenefitPkgResponse setName(String name) {
        this.name = name;
        return this;
    }
    public String getName() {
        return this.name;
    }

}
