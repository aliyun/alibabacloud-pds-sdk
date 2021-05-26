// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class VideoPreviewAudioTemplate extends TeaModel {
    @NameInMap("audio_bitrate")
    public Long audioBitrate;

    @NameInMap("audio_channel")
    public Long audioChannel;

    @NameInMap("audio_codec")
    public String audioCodec;

    @NameInMap("audio_output_ext")
    public String audioOutputExt;

    @NameInMap("audio_sample_rate")
    public Long audioSampleRate;

    @NameInMap("audio_template_id")
    public String audioTemplateId;

    public static VideoPreviewAudioTemplate build(java.util.Map<String, ?> map) throws Exception {
        VideoPreviewAudioTemplate self = new VideoPreviewAudioTemplate();
        return TeaModel.build(map, self);
    }

    public VideoPreviewAudioTemplate setAudioBitrate(Long audioBitrate) {
        this.audioBitrate = audioBitrate;
        return this;
    }
    public Long getAudioBitrate() {
        return this.audioBitrate;
    }

    public VideoPreviewAudioTemplate setAudioChannel(Long audioChannel) {
        this.audioChannel = audioChannel;
        return this;
    }
    public Long getAudioChannel() {
        return this.audioChannel;
    }

    public VideoPreviewAudioTemplate setAudioCodec(String audioCodec) {
        this.audioCodec = audioCodec;
        return this;
    }
    public String getAudioCodec() {
        return this.audioCodec;
    }

    public VideoPreviewAudioTemplate setAudioOutputExt(String audioOutputExt) {
        this.audioOutputExt = audioOutputExt;
        return this;
    }
    public String getAudioOutputExt() {
        return this.audioOutputExt;
    }

    public VideoPreviewAudioTemplate setAudioSampleRate(Long audioSampleRate) {
        this.audioSampleRate = audioSampleRate;
        return this;
    }
    public Long getAudioSampleRate() {
        return this.audioSampleRate;
    }

    public VideoPreviewAudioTemplate setAudioTemplateId(String audioTemplateId) {
        this.audioTemplateId = audioTemplateId;
        return this;
    }
    public String getAudioTemplateId() {
        return this.audioTemplateId;
    }

}
