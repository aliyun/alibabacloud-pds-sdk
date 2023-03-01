// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class VideoPreviewAudioMeta extends TeaModel {
    /**
     * <p>bitrate</p>
     */
    @NameInMap("bitrate")
    public Double bitrate;

    /**
     * <p>channels</p>
     */
    @NameInMap("channels")
    public Long channels;

    /**
     * <p>duration</p>
     */
    @NameInMap("duration")
    public Double duration;

    /**
     * <p>sample_rate</p>
     */
    @NameInMap("sample_rate")
    public Double sampleRate;

    public static VideoPreviewAudioMeta build(java.util.Map<String, ?> map) throws Exception {
        VideoPreviewAudioMeta self = new VideoPreviewAudioMeta();
        return TeaModel.build(map, self);
    }

    public VideoPreviewAudioMeta setBitrate(Double bitrate) {
        this.bitrate = bitrate;
        return this;
    }
    public Double getBitrate() {
        return this.bitrate;
    }

    public VideoPreviewAudioMeta setChannels(Long channels) {
        this.channels = channels;
        return this;
    }
    public Long getChannels() {
        return this.channels;
    }

    public VideoPreviewAudioMeta setDuration(Double duration) {
        this.duration = duration;
        return this;
    }
    public Double getDuration() {
        return this.duration;
    }

    public VideoPreviewAudioMeta setSampleRate(Double sampleRate) {
        this.sampleRate = sampleRate;
        return this;
    }
    public Double getSampleRate() {
        return this.sampleRate;
    }

}
