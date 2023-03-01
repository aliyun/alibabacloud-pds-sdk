// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class VideoPreviewResponse extends TeaModel {
    /**
     * <p>audio_channels</p>
     */
    @NameInMap("audio_channels")
    public Long audioChannels;

    /**
     * <p>audio_format</p>
     */
    @NameInMap("audio_format")
    public String audioFormat;

    @NameInMap("audio_meta")
    public VideoPreviewAudioMeta audioMeta;

    @NameInMap("audio_music_meta")
    public VideoPreviewAudioMusicMeta audioMusicMeta;

    /**
     * <p>audio_sample_rate</p>
     */
    @NameInMap("audio_sample_rate")
    public String audioSampleRate;

    /**
     * <p>audio_template_list</p>
     */
    @NameInMap("audio_template_list")
    public java.util.List<VideoPreviewTranscode> audioTemplateList;

    /**
     * <p>bitrate</p>
     */
    @NameInMap("bitrate")
    public String bitrate;

    /**
     * <p>duration</p>
     */
    @NameInMap("duration")
    public String duration;

    /**
     * <p>frame_rate</p>
     */
    @NameInMap("frame_rate")
    public String frameRate;

    /**
     * <p>height</p>
     */
    @NameInMap("height")
    public Long height;

    @NameInMap("sprite_info")
    public VideoPreviewSpriteResponse spriteInfo;

    /**
     * <p>template_list</p>
     */
    @NameInMap("template_list")
    public java.util.List<VideoPreviewTranscode> templateList;

    /**
     * <p>thumbnail</p>
     */
    @NameInMap("thumbnail")
    public String thumbnail;

    /**
     * <p>video_format</p>
     */
    @NameInMap("video_format")
    public String videoFormat;

    /**
     * <p>width</p>
     */
    @NameInMap("width")
    public Long width;

    public static VideoPreviewResponse build(java.util.Map<String, ?> map) throws Exception {
        VideoPreviewResponse self = new VideoPreviewResponse();
        return TeaModel.build(map, self);
    }

    public VideoPreviewResponse setAudioChannels(Long audioChannels) {
        this.audioChannels = audioChannels;
        return this;
    }
    public Long getAudioChannels() {
        return this.audioChannels;
    }

    public VideoPreviewResponse setAudioFormat(String audioFormat) {
        this.audioFormat = audioFormat;
        return this;
    }
    public String getAudioFormat() {
        return this.audioFormat;
    }

    public VideoPreviewResponse setAudioMeta(VideoPreviewAudioMeta audioMeta) {
        this.audioMeta = audioMeta;
        return this;
    }
    public VideoPreviewAudioMeta getAudioMeta() {
        return this.audioMeta;
    }

    public VideoPreviewResponse setAudioMusicMeta(VideoPreviewAudioMusicMeta audioMusicMeta) {
        this.audioMusicMeta = audioMusicMeta;
        return this;
    }
    public VideoPreviewAudioMusicMeta getAudioMusicMeta() {
        return this.audioMusicMeta;
    }

    public VideoPreviewResponse setAudioSampleRate(String audioSampleRate) {
        this.audioSampleRate = audioSampleRate;
        return this;
    }
    public String getAudioSampleRate() {
        return this.audioSampleRate;
    }

    public VideoPreviewResponse setAudioTemplateList(java.util.List<VideoPreviewTranscode> audioTemplateList) {
        this.audioTemplateList = audioTemplateList;
        return this;
    }
    public java.util.List<VideoPreviewTranscode> getAudioTemplateList() {
        return this.audioTemplateList;
    }

    public VideoPreviewResponse setBitrate(String bitrate) {
        this.bitrate = bitrate;
        return this;
    }
    public String getBitrate() {
        return this.bitrate;
    }

    public VideoPreviewResponse setDuration(String duration) {
        this.duration = duration;
        return this;
    }
    public String getDuration() {
        return this.duration;
    }

    public VideoPreviewResponse setFrameRate(String frameRate) {
        this.frameRate = frameRate;
        return this;
    }
    public String getFrameRate() {
        return this.frameRate;
    }

    public VideoPreviewResponse setHeight(Long height) {
        this.height = height;
        return this;
    }
    public Long getHeight() {
        return this.height;
    }

    public VideoPreviewResponse setSpriteInfo(VideoPreviewSpriteResponse spriteInfo) {
        this.spriteInfo = spriteInfo;
        return this;
    }
    public VideoPreviewSpriteResponse getSpriteInfo() {
        return this.spriteInfo;
    }

    public VideoPreviewResponse setTemplateList(java.util.List<VideoPreviewTranscode> templateList) {
        this.templateList = templateList;
        return this;
    }
    public java.util.List<VideoPreviewTranscode> getTemplateList() {
        return this.templateList;
    }

    public VideoPreviewResponse setThumbnail(String thumbnail) {
        this.thumbnail = thumbnail;
        return this;
    }
    public String getThumbnail() {
        return this.thumbnail;
    }

    public VideoPreviewResponse setVideoFormat(String videoFormat) {
        this.videoFormat = videoFormat;
        return this;
    }
    public String getVideoFormat() {
        return this.videoFormat;
    }

    public VideoPreviewResponse setWidth(Long width) {
        this.width = width;
        return this;
    }
    public Long getWidth() {
        return this.width;
    }

}
