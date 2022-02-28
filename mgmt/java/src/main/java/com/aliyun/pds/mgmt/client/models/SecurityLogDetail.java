// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class SecurityLogDetail extends TeaModel {
    @NameInMap("share_config")
    public ShareConfigLogDetail shareConfig;

    @NameInMap("share_link_config")
    public ShareLinkConfigLogDetail shareLinkConfig;

    @NameInMap("watermark_config")
    public WatermarkEnableConfig watermarkConfig;

    public static SecurityLogDetail build(java.util.Map<String, ?> map) throws Exception {
        SecurityLogDetail self = new SecurityLogDetail();
        return TeaModel.build(map, self);
    }

    public SecurityLogDetail setShareConfig(ShareConfigLogDetail shareConfig) {
        this.shareConfig = shareConfig;
        return this;
    }
    public ShareConfigLogDetail getShareConfig() {
        return this.shareConfig;
    }

    public SecurityLogDetail setShareLinkConfig(ShareLinkConfigLogDetail shareLinkConfig) {
        this.shareLinkConfig = shareLinkConfig;
        return this;
    }
    public ShareLinkConfigLogDetail getShareLinkConfig() {
        return this.shareLinkConfig;
    }

    public SecurityLogDetail setWatermarkConfig(WatermarkEnableConfig watermarkConfig) {
        this.watermarkConfig = watermarkConfig;
        return this;
    }
    public WatermarkEnableConfig getWatermarkConfig() {
        return this.watermarkConfig;
    }

}
