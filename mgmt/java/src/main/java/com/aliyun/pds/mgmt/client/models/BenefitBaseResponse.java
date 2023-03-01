// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * Benefit base info of benefit package
 */
public class BenefitBaseResponse extends TeaModel {
    /**
     * <p>权益的唯一标识</p>
     */
    @NameInMap("benefit_id")
    public String benefitId;

    @NameInMap("benefit_meta")
    public BenefitMetaResponse benefitMeta;

    /**
     * <p>权益包的唯一标识</p>
     */
    @NameInMap("benefit_pkg_id")
    public String benefitPkgId;

    /**
     * <p>权益的名称</p>
     */
    @NameInMap("name")
    public String name;

    public static BenefitBaseResponse build(java.util.Map<String, ?> map) throws Exception {
        BenefitBaseResponse self = new BenefitBaseResponse();
        return TeaModel.build(map, self);
    }

    public BenefitBaseResponse setBenefitId(String benefitId) {
        this.benefitId = benefitId;
        return this;
    }
    public String getBenefitId() {
        return this.benefitId;
    }

    public BenefitBaseResponse setBenefitMeta(BenefitMetaResponse benefitMeta) {
        this.benefitMeta = benefitMeta;
        return this;
    }
    public BenefitMetaResponse getBenefitMeta() {
        return this.benefitMeta;
    }

    public BenefitBaseResponse setBenefitPkgId(String benefitPkgId) {
        this.benefitPkgId = benefitPkgId;
        return this;
    }
    public String getBenefitPkgId() {
        return this.benefitPkgId;
    }

    public BenefitBaseResponse setName(String name) {
        this.name = name;
        return this;
    }
    public String getName() {
        return this.name;
    }

}
