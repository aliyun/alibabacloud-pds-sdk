// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class SecurityLogDetail extends TeaModel {
    @NameInMap("watermark_config")
    public WatermarkEnableConfig watermarkConfig;

    public static SecurityLogDetail build(java.util.Map<String, ?> map) throws Exception {
        SecurityLogDetail self = new SecurityLogDetail();
        return TeaModel.build(map, self);
    }

    public SecurityLogDetail setWatermarkConfig(WatermarkEnableConfig watermarkConfig) {
        this.watermarkConfig = watermarkConfig;
        return this;
    }
    public WatermarkEnableConfig getWatermarkConfig() {
        return this.watermarkConfig;
    }

}
