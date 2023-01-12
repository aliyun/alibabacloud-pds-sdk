// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 转码配置
 */
public class VideoPreviewConfig extends TeaModel {
    @NameInMap("audio_config")
    public VideoPreviewAudioConfig audioConfig;

    @NameInMap("audio_template_list")
    public java.util.List<String> audioTemplateList;

    @NameInMap("audio_thumbnail")
    public VideoPreviewThumbnailConfig audioThumbnail;

    @NameInMap("auto_category_config")
    public VideoPreviewAutoCategoryConfig autoCategoryConfig;

    @NameInMap("backup_config")
    public VideoPreviewBackupConfig backupConfig;

    @NameInMap("drm_config")
    public VideoPreviewDrmConfig drmConfig;

    @NameInMap("enable_config")
    public VideoPreviewEnableConfig enableConfig;

    @NameInMap("enabled")
    public Boolean enabled;

    @NameInMap("live_transcoding_config")
    public VideoPreviewLiveTranscodingConfig liveTranscodingConfig;

    @NameInMap("quick_video_config")
    public VideoPreviewQuickVideoConfig quickVideoConfig;

    @NameInMap("rate_limit_config")
    public VideoPreviewRateLimitConfig rateLimitConfig;

    @NameInMap("sprite")
    public VideoPreviewSpriteConfig sprite;

    @NameInMap("store")
    public Store store;

    @NameInMap("store_id_map")
    public java.util.Map<String, ?> storeIdMap;

    @NameInMap("template_list")
    public java.util.List<String> templateList;

    @NameInMap("template_name_map")
    public java.util.Map<String, ?> templateNameMap;

    @NameInMap("template_policy_config")
    public VideoPreviewTemplatePolicyConfig templatePolicyConfig;

    @NameInMap("thumbnail")
    public VideoPreviewThumbnailConfig thumbnail;

    @NameInMap("video_config")
    public VideoPreviewVideoConfig videoConfig;

    @NameInMap("video_filter_config")
    public VideoPreviewVideoFilterConfig videoFilterConfig;

    public static VideoPreviewConfig build(java.util.Map<String, ?> map) throws Exception {
        VideoPreviewConfig self = new VideoPreviewConfig();
        return TeaModel.build(map, self);
    }

    public VideoPreviewConfig setAudioConfig(VideoPreviewAudioConfig audioConfig) {
        this.audioConfig = audioConfig;
        return this;
    }
    public VideoPreviewAudioConfig getAudioConfig() {
        return this.audioConfig;
    }

    public VideoPreviewConfig setAudioTemplateList(java.util.List<String> audioTemplateList) {
        this.audioTemplateList = audioTemplateList;
        return this;
    }
    public java.util.List<String> getAudioTemplateList() {
        return this.audioTemplateList;
    }

    public VideoPreviewConfig setAudioThumbnail(VideoPreviewThumbnailConfig audioThumbnail) {
        this.audioThumbnail = audioThumbnail;
        return this;
    }
    public VideoPreviewThumbnailConfig getAudioThumbnail() {
        return this.audioThumbnail;
    }

    public VideoPreviewConfig setAutoCategoryConfig(VideoPreviewAutoCategoryConfig autoCategoryConfig) {
        this.autoCategoryConfig = autoCategoryConfig;
        return this;
    }
    public VideoPreviewAutoCategoryConfig getAutoCategoryConfig() {
        return this.autoCategoryConfig;
    }

    public VideoPreviewConfig setBackupConfig(VideoPreviewBackupConfig backupConfig) {
        this.backupConfig = backupConfig;
        return this;
    }
    public VideoPreviewBackupConfig getBackupConfig() {
        return this.backupConfig;
    }

    public VideoPreviewConfig setDrmConfig(VideoPreviewDrmConfig drmConfig) {
        this.drmConfig = drmConfig;
        return this;
    }
    public VideoPreviewDrmConfig getDrmConfig() {
        return this.drmConfig;
    }

    public VideoPreviewConfig setEnableConfig(VideoPreviewEnableConfig enableConfig) {
        this.enableConfig = enableConfig;
        return this;
    }
    public VideoPreviewEnableConfig getEnableConfig() {
        return this.enableConfig;
    }

    public VideoPreviewConfig setEnabled(Boolean enabled) {
        this.enabled = enabled;
        return this;
    }
    public Boolean getEnabled() {
        return this.enabled;
    }

    public VideoPreviewConfig setLiveTranscodingConfig(VideoPreviewLiveTranscodingConfig liveTranscodingConfig) {
        this.liveTranscodingConfig = liveTranscodingConfig;
        return this;
    }
    public VideoPreviewLiveTranscodingConfig getLiveTranscodingConfig() {
        return this.liveTranscodingConfig;
    }

    public VideoPreviewConfig setQuickVideoConfig(VideoPreviewQuickVideoConfig quickVideoConfig) {
        this.quickVideoConfig = quickVideoConfig;
        return this;
    }
    public VideoPreviewQuickVideoConfig getQuickVideoConfig() {
        return this.quickVideoConfig;
    }

    public VideoPreviewConfig setRateLimitConfig(VideoPreviewRateLimitConfig rateLimitConfig) {
        this.rateLimitConfig = rateLimitConfig;
        return this;
    }
    public VideoPreviewRateLimitConfig getRateLimitConfig() {
        return this.rateLimitConfig;
    }

    public VideoPreviewConfig setSprite(VideoPreviewSpriteConfig sprite) {
        this.sprite = sprite;
        return this;
    }
    public VideoPreviewSpriteConfig getSprite() {
        return this.sprite;
    }

    public VideoPreviewConfig setStore(Store store) {
        this.store = store;
        return this;
    }
    public Store getStore() {
        return this.store;
    }

    public VideoPreviewConfig setStoreIdMap(java.util.Map<String, ?> storeIdMap) {
        this.storeIdMap = storeIdMap;
        return this;
    }
    public java.util.Map<String, ?> getStoreIdMap() {
        return this.storeIdMap;
    }

    public VideoPreviewConfig setTemplateList(java.util.List<String> templateList) {
        this.templateList = templateList;
        return this;
    }
    public java.util.List<String> getTemplateList() {
        return this.templateList;
    }

    public VideoPreviewConfig setTemplateNameMap(java.util.Map<String, ?> templateNameMap) {
        this.templateNameMap = templateNameMap;
        return this;
    }
    public java.util.Map<String, ?> getTemplateNameMap() {
        return this.templateNameMap;
    }

    public VideoPreviewConfig setTemplatePolicyConfig(VideoPreviewTemplatePolicyConfig templatePolicyConfig) {
        this.templatePolicyConfig = templatePolicyConfig;
        return this;
    }
    public VideoPreviewTemplatePolicyConfig getTemplatePolicyConfig() {
        return this.templatePolicyConfig;
    }

    public VideoPreviewConfig setThumbnail(VideoPreviewThumbnailConfig thumbnail) {
        this.thumbnail = thumbnail;
        return this;
    }
    public VideoPreviewThumbnailConfig getThumbnail() {
        return this.thumbnail;
    }

    public VideoPreviewConfig setVideoConfig(VideoPreviewVideoConfig videoConfig) {
        this.videoConfig = videoConfig;
        return this;
    }
    public VideoPreviewVideoConfig getVideoConfig() {
        return this.videoConfig;
    }

    public VideoPreviewConfig setVideoFilterConfig(VideoPreviewVideoFilterConfig videoFilterConfig) {
        this.videoFilterConfig = videoFilterConfig;
        return this;
    }
    public VideoPreviewVideoFilterConfig getVideoFilterConfig() {
        return this.videoFilterConfig;
    }

}
