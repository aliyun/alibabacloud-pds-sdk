// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 音频转码信息meta响应
 */
public class AudioPreviewPlayInfoMetaResponse extends TeaModel {
    // bitrate, 码率
    @NameInMap("bitrate")
    public Long bitrate;

    // channels, 声道数
    @NameInMap("channels")
    public Long channels;

    // duration, 视频长度
    @NameInMap("duration")
    public Double duration;

    // sample_rate, 采样率
    @NameInMap("sample_rate")
    public Long sampleRate;

    public static AudioPreviewPlayInfoMetaResponse build(java.util.Map<String, ?> map) throws Exception {
        AudioPreviewPlayInfoMetaResponse self = new AudioPreviewPlayInfoMetaResponse();
        return TeaModel.build(map, self);
    }

    public AudioPreviewPlayInfoMetaResponse setBitrate(Long bitrate) {
        this.bitrate = bitrate;
        return this;
    }
    public Long getBitrate() {
        return this.bitrate;
    }

    public AudioPreviewPlayInfoMetaResponse setChannels(Long channels) {
        this.channels = channels;
        return this;
    }
    public Long getChannels() {
        return this.channels;
    }

    public AudioPreviewPlayInfoMetaResponse setDuration(Double duration) {
        this.duration = duration;
        return this;
    }
    public Double getDuration() {
        return this.duration;
    }

    public AudioPreviewPlayInfoMetaResponse setSampleRate(Long sampleRate) {
        this.sampleRate = sampleRate;
        return this;
    }
    public Long getSampleRate() {
        return this.sampleRate;
    }

}
