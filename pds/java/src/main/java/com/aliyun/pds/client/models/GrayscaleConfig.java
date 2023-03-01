// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class GrayscaleConfig extends TeaModel {
    @NameInMap("enabled")
    public Boolean enabled;

    @NameInMap("percentage")
    public Long percentage;

    public static GrayscaleConfig build(java.util.Map<String, ?> map) throws Exception {
        GrayscaleConfig self = new GrayscaleConfig();
        return TeaModel.build(map, self);
    }

    public GrayscaleConfig setEnabled(Boolean enabled) {
        this.enabled = enabled;
        return this;
    }
    public Boolean getEnabled() {
        return this.enabled;
    }

    public GrayscaleConfig setPercentage(Long percentage) {
        this.percentage = percentage;
        return this;
    }
    public Long getPercentage() {
        return this.percentage;
    }

}
