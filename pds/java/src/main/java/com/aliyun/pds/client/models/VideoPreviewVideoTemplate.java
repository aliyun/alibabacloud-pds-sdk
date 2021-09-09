// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 视频转码模板
 */
public class VideoPreviewVideoTemplate extends TeaModel {
    @NameInMap("audio_bitrate")
    public Long audioBitrate;

    @NameInMap("audio_channel")
    public Long audioChannel;

    @NameInMap("audio_codec")
    public String audioCodec;

    @NameInMap("audio_sample_rate")
    public Long audioSampleRate;

    @NameInMap("height")
    public Long height;

    @NameInMap("keep_original")
    public Boolean keepOriginal;

    @NameInMap("video_bitrate")
    public Long videoBitrate;

    @NameInMap("video_codec")
    public String videoCodec;

    @NameInMap("video_frame_rate")
    public Long videoFrameRate;

    @NameInMap("video_output_ext")
    public String videoOutputExt;

    @NameInMap("video_template_id")
    public String videoTemplateId;

    @NameInMap("width")
    public Long width;

    public static VideoPreviewVideoTemplate build(java.util.Map<String, ?> map) throws Exception {
        VideoPreviewVideoTemplate self = new VideoPreviewVideoTemplate();
        return TeaModel.build(map, self);
    }

    public VideoPreviewVideoTemplate setAudioBitrate(Long audioBitrate) {
        this.audioBitrate = audioBitrate;
        return this;
    }
    public Long getAudioBitrate() {
        return this.audioBitrate;
    }

    public VideoPreviewVideoTemplate setAudioChannel(Long audioChannel) {
        this.audioChannel = audioChannel;
        return this;
    }
    public Long getAudioChannel() {
        return this.audioChannel;
    }

    public VideoPreviewVideoTemplate setAudioCodec(String audioCodec) {
        this.audioCodec = audioCodec;
        return this;
    }
    public String getAudioCodec() {
        return this.audioCodec;
    }

    public VideoPreviewVideoTemplate setAudioSampleRate(Long audioSampleRate) {
        this.audioSampleRate = audioSampleRate;
        return this;
    }
    public Long getAudioSampleRate() {
        return this.audioSampleRate;
    }

    public VideoPreviewVideoTemplate setHeight(Long height) {
        this.height = height;
        return this;
    }
    public Long getHeight() {
        return this.height;
    }

    public VideoPreviewVideoTemplate setKeepOriginal(Boolean keepOriginal) {
        this.keepOriginal = keepOriginal;
        return this;
    }
    public Boolean getKeepOriginal() {
        return this.keepOriginal;
    }

    public VideoPreviewVideoTemplate setVideoBitrate(Long videoBitrate) {
        this.videoBitrate = videoBitrate;
        return this;
    }
    public Long getVideoBitrate() {
        return this.videoBitrate;
    }

    public VideoPreviewVideoTemplate setVideoCodec(String videoCodec) {
        this.videoCodec = videoCodec;
        return this;
    }
    public String getVideoCodec() {
        return this.videoCodec;
    }

    public VideoPreviewVideoTemplate setVideoFrameRate(Long videoFrameRate) {
        this.videoFrameRate = videoFrameRate;
        return this;
    }
    public Long getVideoFrameRate() {
        return this.videoFrameRate;
    }

    public VideoPreviewVideoTemplate setVideoOutputExt(String videoOutputExt) {
        this.videoOutputExt = videoOutputExt;
        return this;
    }
    public String getVideoOutputExt() {
        return this.videoOutputExt;
    }

    public VideoPreviewVideoTemplate setVideoTemplateId(String videoTemplateId) {
        this.videoTemplateId = videoTemplateId;
        return this;
    }
    public String getVideoTemplateId() {
        return this.videoTemplateId;
    }

    public VideoPreviewVideoTemplate setWidth(Long width) {
        this.width = width;
        return this;
    }
    public Long getWidth() {
        return this.width;
    }

}
