// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 转码源过滤配置（TODO: 未完整测试）
同时满足以下所有null条件，则不触发转码。如果没有配置任何条件，那么不触发过滤
 */
public class VideoPreviewVideoFilterConfig extends TeaModel {
    @NameInMap("audio_bitrate")
    public Long audioBitrate;

    @NameInMap("audio_channel")
    public Long audioChannel;

    // 音频信息过滤
    @NameInMap("audio_codec_list")
    public java.util.List<String> audioCodecList;

    @NameInMap("audio_sample_rate")
    public Long audioSampleRate;

    @NameInMap("bitrate")
    public Long bitrate;

    // 综合信息过滤
    @NameInMap("duration")
    public Long duration;

    @NameInMap("height")
    public Long height;

    @NameInMap("pixel")
    public Long pixel;

    @NameInMap("size")
    public Long size;

    @NameInMap("video_bitrate")
    public Long videoBitrate;

    // 视频信息过滤
    @NameInMap("video_codec_list")
    public java.util.List<String> videoCodecList;

    @NameInMap("video_frame_rate")
    public Long videoFrameRate;

    @NameInMap("width")
    public Long width;

    public static VideoPreviewVideoFilterConfig build(java.util.Map<String, ?> map) throws Exception {
        VideoPreviewVideoFilterConfig self = new VideoPreviewVideoFilterConfig();
        return TeaModel.build(map, self);
    }

    public VideoPreviewVideoFilterConfig setAudioBitrate(Long audioBitrate) {
        this.audioBitrate = audioBitrate;
        return this;
    }
    public Long getAudioBitrate() {
        return this.audioBitrate;
    }

    public VideoPreviewVideoFilterConfig setAudioChannel(Long audioChannel) {
        this.audioChannel = audioChannel;
        return this;
    }
    public Long getAudioChannel() {
        return this.audioChannel;
    }

    public VideoPreviewVideoFilterConfig setAudioCodecList(java.util.List<String> audioCodecList) {
        this.audioCodecList = audioCodecList;
        return this;
    }
    public java.util.List<String> getAudioCodecList() {
        return this.audioCodecList;
    }

    public VideoPreviewVideoFilterConfig setAudioSampleRate(Long audioSampleRate) {
        this.audioSampleRate = audioSampleRate;
        return this;
    }
    public Long getAudioSampleRate() {
        return this.audioSampleRate;
    }

    public VideoPreviewVideoFilterConfig setBitrate(Long bitrate) {
        this.bitrate = bitrate;
        return this;
    }
    public Long getBitrate() {
        return this.bitrate;
    }

    public VideoPreviewVideoFilterConfig setDuration(Long duration) {
        this.duration = duration;
        return this;
    }
    public Long getDuration() {
        return this.duration;
    }

    public VideoPreviewVideoFilterConfig setHeight(Long height) {
        this.height = height;
        return this;
    }
    public Long getHeight() {
        return this.height;
    }

    public VideoPreviewVideoFilterConfig setPixel(Long pixel) {
        this.pixel = pixel;
        return this;
    }
    public Long getPixel() {
        return this.pixel;
    }

    public VideoPreviewVideoFilterConfig setSize(Long size) {
        this.size = size;
        return this;
    }
    public Long getSize() {
        return this.size;
    }

    public VideoPreviewVideoFilterConfig setVideoBitrate(Long videoBitrate) {
        this.videoBitrate = videoBitrate;
        return this;
    }
    public Long getVideoBitrate() {
        return this.videoBitrate;
    }

    public VideoPreviewVideoFilterConfig setVideoCodecList(java.util.List<String> videoCodecList) {
        this.videoCodecList = videoCodecList;
        return this;
    }
    public java.util.List<String> getVideoCodecList() {
        return this.videoCodecList;
    }

    public VideoPreviewVideoFilterConfig setVideoFrameRate(Long videoFrameRate) {
        this.videoFrameRate = videoFrameRate;
        return this;
    }
    public Long getVideoFrameRate() {
        return this.videoFrameRate;
    }

    public VideoPreviewVideoFilterConfig setWidth(Long width) {
        this.width = width;
        return this;
    }
    public Long getWidth() {
        return this.width;
    }

}
