// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class VideoPreviewAutoScaleConfig extends TeaModel {
    @NameInMap("enabled")
    public Boolean enabled;

    @NameInMap("max_length")
    public Long maxLength;

    public static VideoPreviewAutoScaleConfig build(java.util.Map<String, ?> map) throws Exception {
        VideoPreviewAutoScaleConfig self = new VideoPreviewAutoScaleConfig();
        return TeaModel.build(map, self);
    }

    public VideoPreviewAutoScaleConfig setEnabled(Boolean enabled) {
        this.enabled = enabled;
        return this;
    }
    public Boolean getEnabled() {
        return this.enabled;
    }

    public VideoPreviewAutoScaleConfig setMaxLength(Long maxLength) {
        this.maxLength = maxLength;
        return this;
    }
    public Long getMaxLength() {
        return this.maxLength;
    }

}
