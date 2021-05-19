// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * Benefit meta response
 */
public class BenefitMetaResponse extends TeaModel {
    // 权益的配置
    @NameInMap("config")
    public String config;

    // 权益的开关
    @NameInMap("enabled")
    public Boolean enabled;

    // 权益的配额
    @NameInMap("quota")
    public Long quota;

    public static BenefitMetaResponse build(java.util.Map<String, ?> map) throws Exception {
        BenefitMetaResponse self = new BenefitMetaResponse();
        return TeaModel.build(map, self);
    }

    public BenefitMetaResponse setConfig(String config) {
        this.config = config;
        return this;
    }
    public String getConfig() {
        return this.config;
    }

    public BenefitMetaResponse setEnabled(Boolean enabled) {
        this.enabled = enabled;
        return this;
    }
    public Boolean getEnabled() {
        return this.enabled;
    }

    public BenefitMetaResponse setQuota(Long quota) {
        this.quota = quota;
        return this;
    }
    public Long getQuota() {
        return this.quota;
    }

}
