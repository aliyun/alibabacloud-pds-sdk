// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 实时转码refTask配置
 */
public class VideoPreviewLiveTranscodingRefTaskConfig extends TeaModel {
    @NameInMap("duration")
    public Double duration;

    @NameInMap("enabled")
    public Boolean enabled;

    public static VideoPreviewLiveTranscodingRefTaskConfig build(java.util.Map<String, ?> map) throws Exception {
        VideoPreviewLiveTranscodingRefTaskConfig self = new VideoPreviewLiveTranscodingRefTaskConfig();
        return TeaModel.build(map, self);
    }

    public VideoPreviewLiveTranscodingRefTaskConfig setDuration(Double duration) {
        this.duration = duration;
        return this;
    }
    public Double getDuration() {
        return this.duration;
    }

    public VideoPreviewLiveTranscodingRefTaskConfig setEnabled(Boolean enabled) {
        this.enabled = enabled;
        return this;
    }
    public Boolean getEnabled() {
        return this.enabled;
    }

}
