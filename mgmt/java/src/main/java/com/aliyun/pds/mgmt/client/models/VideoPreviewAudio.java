// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 音频转码参数
 */
public class VideoPreviewAudio extends TeaModel {
    @NameInMap("audio_bitrate")
    public Long audioBitrate;

    @NameInMap("audio_channel")
    public Long audioChannel;

    @NameInMap("audio_codec")
    public String audioCodec;

    @NameInMap("audio_sample_rate")
    public Long audioSampleRate;

    public static VideoPreviewAudio build(java.util.Map<String, ?> map) throws Exception {
        VideoPreviewAudio self = new VideoPreviewAudio();
        return TeaModel.build(map, self);
    }

    public VideoPreviewAudio setAudioBitrate(Long audioBitrate) {
        this.audioBitrate = audioBitrate;
        return this;
    }
    public Long getAudioBitrate() {
        return this.audioBitrate;
    }

    public VideoPreviewAudio setAudioChannel(Long audioChannel) {
        this.audioChannel = audioChannel;
        return this;
    }
    public Long getAudioChannel() {
        return this.audioChannel;
    }

    public VideoPreviewAudio setAudioCodec(String audioCodec) {
        this.audioCodec = audioCodec;
        return this;
    }
    public String getAudioCodec() {
        return this.audioCodec;
    }

    public VideoPreviewAudio setAudioSampleRate(Long audioSampleRate) {
        this.audioSampleRate = audioSampleRate;
        return this;
    }
    public Long getAudioSampleRate() {
        return this.audioSampleRate;
    }

}
