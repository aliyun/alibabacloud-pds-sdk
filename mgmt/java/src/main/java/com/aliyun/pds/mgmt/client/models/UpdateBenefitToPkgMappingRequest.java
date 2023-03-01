// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * update benefit to benefit package mapping request
 */
public class UpdateBenefitToPkgMappingRequest extends TeaModel {
    @NameInMap("allow_config_by_tenant")
    public Boolean allowConfigByTenant;

    @NameInMap("allow_config_by_user")
    public Boolean allowConfigByUser;

    @NameInMap("allow_show_to_tenant")
    public Boolean allowShowToTenant;

    @NameInMap("allow_show_to_user")
    public Boolean allowShowToUser;

    @NameInMap("benefit_id")
    public String benefitId;

    @NameInMap("benefit_meta")
    public BenefitMeta benefitMeta;

    @NameInMap("benefit_pkg_id")
    public String benefitPkgId;

    @NameInMap("name")
    public String name;

    @NameInMap("user_meta")
    public String userMeta;

    public static UpdateBenefitToPkgMappingRequest build(java.util.Map<String, ?> map) throws Exception {
        UpdateBenefitToPkgMappingRequest self = new UpdateBenefitToPkgMappingRequest();
        return TeaModel.build(map, self);
    }

    public UpdateBenefitToPkgMappingRequest setAllowConfigByTenant(Boolean allowConfigByTenant) {
        this.allowConfigByTenant = allowConfigByTenant;
        return this;
    }
    public Boolean getAllowConfigByTenant() {
        return this.allowConfigByTenant;
    }

    public UpdateBenefitToPkgMappingRequest setAllowConfigByUser(Boolean allowConfigByUser) {
        this.allowConfigByUser = allowConfigByUser;
        return this;
    }
    public Boolean getAllowConfigByUser() {
        return this.allowConfigByUser;
    }

    public UpdateBenefitToPkgMappingRequest setAllowShowToTenant(Boolean allowShowToTenant) {
        this.allowShowToTenant = allowShowToTenant;
        return this;
    }
    public Boolean getAllowShowToTenant() {
        return this.allowShowToTenant;
    }

    public UpdateBenefitToPkgMappingRequest setAllowShowToUser(Boolean allowShowToUser) {
        this.allowShowToUser = allowShowToUser;
        return this;
    }
    public Boolean getAllowShowToUser() {
        return this.allowShowToUser;
    }

    public UpdateBenefitToPkgMappingRequest setBenefitId(String benefitId) {
        this.benefitId = benefitId;
        return this;
    }
    public String getBenefitId() {
        return this.benefitId;
    }

    public UpdateBenefitToPkgMappingRequest setBenefitMeta(BenefitMeta benefitMeta) {
        this.benefitMeta = benefitMeta;
        return this;
    }
    public BenefitMeta getBenefitMeta() {
        return this.benefitMeta;
    }

    public UpdateBenefitToPkgMappingRequest setBenefitPkgId(String benefitPkgId) {
        this.benefitPkgId = benefitPkgId;
        return this;
    }
    public String getBenefitPkgId() {
        return this.benefitPkgId;
    }

    public UpdateBenefitToPkgMappingRequest setName(String name) {
        this.name = name;
        return this;
    }
    public String getName() {
        return this.name;
    }

    public UpdateBenefitToPkgMappingRequest setUserMeta(String userMeta) {
        this.userMeta = userMeta;
        return this;
    }
    public String getUserMeta() {
        return this.userMeta;
    }

}
