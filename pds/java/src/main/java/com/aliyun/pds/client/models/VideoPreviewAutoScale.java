// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class VideoPreviewAutoScale extends TeaModel {
    @NameInMap("enabled")
    public Boolean enabled;

    @NameInMap("max_length")
    public Long maxLength;

    public static VideoPreviewAutoScale build(java.util.Map<String, ?> map) throws Exception {
        VideoPreviewAutoScale self = new VideoPreviewAutoScale();
        return TeaModel.build(map, self);
    }

    public VideoPreviewAutoScale setEnabled(Boolean enabled) {
        this.enabled = enabled;
        return this;
    }
    public Boolean getEnabled() {
        return this.enabled;
    }

    public VideoPreviewAutoScale setMaxLength(Long maxLength) {
        this.maxLength = maxLength;
        return this;
    }
    public Long getMaxLength() {
        return this.maxLength;
    }

}
