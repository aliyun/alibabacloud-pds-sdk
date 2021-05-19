// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class CustomBenefitMetaRequest extends TeaModel {
    @NameInMap("enabled")
    public Boolean enabled;

    public static CustomBenefitMetaRequest build(java.util.Map<String, ?> map) throws Exception {
        CustomBenefitMetaRequest self = new CustomBenefitMetaRequest();
        return TeaModel.build(map, self);
    }

    public CustomBenefitMetaRequest setEnabled(Boolean enabled) {
        this.enabled = enabled;
        return this;
    }
    public Boolean getEnabled() {
        return this.enabled;
    }

}
