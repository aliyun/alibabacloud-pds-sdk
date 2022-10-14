// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class CustomBenefitMeta extends TeaModel {
    @NameInMap("config")
    public String config;

    @NameInMap("cover_lower_level")
    public Boolean coverLowerLevel;

    @NameInMap("enabled")
    public Boolean enabled;

    @NameInMap("quota")
    public Long quota;

    public static CustomBenefitMeta build(java.util.Map<String, ?> map) throws Exception {
        CustomBenefitMeta self = new CustomBenefitMeta();
        return TeaModel.build(map, self);
    }

    public CustomBenefitMeta setConfig(String config) {
        this.config = config;
        return this;
    }
    public String getConfig() {
        return this.config;
    }

    public CustomBenefitMeta setCoverLowerLevel(Boolean coverLowerLevel) {
        this.coverLowerLevel = coverLowerLevel;
        return this;
    }
    public Boolean getCoverLowerLevel() {
        return this.coverLowerLevel;
    }

    public CustomBenefitMeta setEnabled(Boolean enabled) {
        this.enabled = enabled;
        return this;
    }
    public Boolean getEnabled() {
        return this.enabled;
    }

    public CustomBenefitMeta setQuota(Long quota) {
        this.quota = quota;
        return this;
    }
    public Long getQuota() {
        return this.quota;
    }

}
