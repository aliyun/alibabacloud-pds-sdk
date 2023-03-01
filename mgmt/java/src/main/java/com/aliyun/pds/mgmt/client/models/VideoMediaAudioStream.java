// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class VideoMediaAudioStream extends TeaModel {
    /**
     * <p>bit_rate 音频比特率 单位：bps</p>
     */
    @NameInMap("bit_rate")
    public String bitRate;

    /**
     * <p>channel_layout 声道布局</p>
     */
    @NameInMap("channel_layout")
    public String channelLayout;

    /**
     * <p>channels 音频数/声道数</p>
     */
    @NameInMap("channels")
    public Long channels;

    /**
     * <p>code_name 音频编码模式</p>
     */
    @NameInMap("code_name")
    public String codeName;

    /**
     * <p>duration 单位 秒</p>
     */
    @NameInMap("duration")
    public String duration;

    /**
     * <p>sample_rate 音频采样率</p>
     */
    @NameInMap("sample_rate")
    public String sampleRate;

    public static VideoMediaAudioStream build(java.util.Map<String, ?> map) throws Exception {
        VideoMediaAudioStream self = new VideoMediaAudioStream();
        return TeaModel.build(map, self);
    }

    public VideoMediaAudioStream setBitRate(String bitRate) {
        this.bitRate = bitRate;
        return this;
    }
    public String getBitRate() {
        return this.bitRate;
    }

    public VideoMediaAudioStream setChannelLayout(String channelLayout) {
        this.channelLayout = channelLayout;
        return this;
    }
    public String getChannelLayout() {
        return this.channelLayout;
    }

    public VideoMediaAudioStream setChannels(Long channels) {
        this.channels = channels;
        return this;
    }
    public Long getChannels() {
        return this.channels;
    }

    public VideoMediaAudioStream setCodeName(String codeName) {
        this.codeName = codeName;
        return this;
    }
    public String getCodeName() {
        return this.codeName;
    }

    public VideoMediaAudioStream setDuration(String duration) {
        this.duration = duration;
        return this;
    }
    public String getDuration() {
        return this.duration;
    }

    public VideoMediaAudioStream setSampleRate(String sampleRate) {
        this.sampleRate = sampleRate;
        return this;
    }
    public String getSampleRate() {
        return this.sampleRate;
    }

}
