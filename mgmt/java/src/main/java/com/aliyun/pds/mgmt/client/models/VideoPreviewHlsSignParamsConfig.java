// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class VideoPreviewHlsSignParamsConfig extends TeaModel {
    @NameInMap("disable_headers")
    public Boolean disableHeaders;

    @NameInMap("enabled")
    public Boolean enabled;

    @NameInMap("gray_config")
    public ApiConfig grayConfig;

    public static VideoPreviewHlsSignParamsConfig build(java.util.Map<String, ?> map) throws Exception {
        VideoPreviewHlsSignParamsConfig self = new VideoPreviewHlsSignParamsConfig();
        return TeaModel.build(map, self);
    }

    public VideoPreviewHlsSignParamsConfig setDisableHeaders(Boolean disableHeaders) {
        this.disableHeaders = disableHeaders;
        return this;
    }
    public Boolean getDisableHeaders() {
        return this.disableHeaders;
    }

    public VideoPreviewHlsSignParamsConfig setEnabled(Boolean enabled) {
        this.enabled = enabled;
        return this;
    }
    public Boolean getEnabled() {
        return this.enabled;
    }

    public VideoPreviewHlsSignParamsConfig setGrayConfig(ApiConfig grayConfig) {
        this.grayConfig = grayConfig;
        return this;
    }
    public ApiConfig getGrayConfig() {
        return this.grayConfig;
    }

}
