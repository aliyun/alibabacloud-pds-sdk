// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class VideoPreviewEnableConfig extends TeaModel {
    @NameInMap("enable_transcode_when_play")
    public Boolean enableTranscodeWhenPlay;

    @NameInMap("enable_transcode_when_uploaded")
    public Boolean enableTranscodeWhenUploaded;

    public static VideoPreviewEnableConfig build(java.util.Map<String, ?> map) throws Exception {
        VideoPreviewEnableConfig self = new VideoPreviewEnableConfig();
        return TeaModel.build(map, self);
    }

    public VideoPreviewEnableConfig setEnableTranscodeWhenPlay(Boolean enableTranscodeWhenPlay) {
        this.enableTranscodeWhenPlay = enableTranscodeWhenPlay;
        return this;
    }
    public Boolean getEnableTranscodeWhenPlay() {
        return this.enableTranscodeWhenPlay;
    }

    public VideoPreviewEnableConfig setEnableTranscodeWhenUploaded(Boolean enableTranscodeWhenUploaded) {
        this.enableTranscodeWhenUploaded = enableTranscodeWhenUploaded;
        return this;
    }
    public Boolean getEnableTranscodeWhenUploaded() {
        return this.enableTranscodeWhenUploaded;
    }

}
