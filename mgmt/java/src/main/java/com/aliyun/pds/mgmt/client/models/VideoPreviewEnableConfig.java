// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 转码子开关配置
 */
public class VideoPreviewEnableConfig extends TeaModel {
    @NameInMap("disable_offline_audio_transcode")
    public Boolean disableOfflineAudioTranscode;

    @NameInMap("disable_offline_video_transcode")
    public Boolean disableOfflineVideoTranscode;

    @NameInMap("enable_transcode_when_play")
    public Boolean enableTranscodeWhenPlay;

    @NameInMap("enable_transcode_when_uploaded")
    public Boolean enableTranscodeWhenUploaded;

    public static VideoPreviewEnableConfig build(java.util.Map<String, ?> map) throws Exception {
        VideoPreviewEnableConfig self = new VideoPreviewEnableConfig();
        return TeaModel.build(map, self);
    }

    public VideoPreviewEnableConfig setDisableOfflineAudioTranscode(Boolean disableOfflineAudioTranscode) {
        this.disableOfflineAudioTranscode = disableOfflineAudioTranscode;
        return this;
    }
    public Boolean getDisableOfflineAudioTranscode() {
        return this.disableOfflineAudioTranscode;
    }

    public VideoPreviewEnableConfig setDisableOfflineVideoTranscode(Boolean disableOfflineVideoTranscode) {
        this.disableOfflineVideoTranscode = disableOfflineVideoTranscode;
        return this;
    }
    public Boolean getDisableOfflineVideoTranscode() {
        return this.disableOfflineVideoTranscode;
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
