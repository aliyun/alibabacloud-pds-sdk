// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class VideoPreviewQuickVideoConfig extends TeaModel {
    @NameInMap("current_version")
    public Long currentVersion;

    @NameInMap("deprecated_version")
    public Long deprecatedVersion;

    @NameInMap("enable_config")
    public VideoPreviewLiveTranscodingEnableConfig enableConfig;

    @NameInMap("enabled")
    public Boolean enabled;

    @NameInMap("initial_ts_config")
    public VideoPreviewQuickVideoInitialTsConfig initialTsConfig;

    @NameInMap("leading_prefix")
    public String leadingPrefix;

    @NameInMap("m3u8_file_prefix")
    public String m3u8FilePrefix;

    @NameInMap("segment")
    public Long segment;

    @NameInMap("subtitle_config")
    public VideoPreviewLiveTranscodingSubtitleConfig subtitleConfig;

    @NameInMap("template_list")
    public java.util.List<String> templateList;

    @NameInMap("template_name_map")
    public java.util.Map<String, ?> templateNameMap;

    @NameInMap("ts_count_when_ts_404")
    public Long tsCountWhenTs404;

    public static VideoPreviewQuickVideoConfig build(java.util.Map<String, ?> map) throws Exception {
        VideoPreviewQuickVideoConfig self = new VideoPreviewQuickVideoConfig();
        return TeaModel.build(map, self);
    }

    public VideoPreviewQuickVideoConfig setCurrentVersion(Long currentVersion) {
        this.currentVersion = currentVersion;
        return this;
    }
    public Long getCurrentVersion() {
        return this.currentVersion;
    }

    public VideoPreviewQuickVideoConfig setDeprecatedVersion(Long deprecatedVersion) {
        this.deprecatedVersion = deprecatedVersion;
        return this;
    }
    public Long getDeprecatedVersion() {
        return this.deprecatedVersion;
    }

    public VideoPreviewQuickVideoConfig setEnableConfig(VideoPreviewLiveTranscodingEnableConfig enableConfig) {
        this.enableConfig = enableConfig;
        return this;
    }
    public VideoPreviewLiveTranscodingEnableConfig getEnableConfig() {
        return this.enableConfig;
    }

    public VideoPreviewQuickVideoConfig setEnabled(Boolean enabled) {
        this.enabled = enabled;
        return this;
    }
    public Boolean getEnabled() {
        return this.enabled;
    }

    public VideoPreviewQuickVideoConfig setInitialTsConfig(VideoPreviewQuickVideoInitialTsConfig initialTsConfig) {
        this.initialTsConfig = initialTsConfig;
        return this;
    }
    public VideoPreviewQuickVideoInitialTsConfig getInitialTsConfig() {
        return this.initialTsConfig;
    }

    public VideoPreviewQuickVideoConfig setLeadingPrefix(String leadingPrefix) {
        this.leadingPrefix = leadingPrefix;
        return this;
    }
    public String getLeadingPrefix() {
        return this.leadingPrefix;
    }

    public VideoPreviewQuickVideoConfig setM3u8FilePrefix(String m3u8FilePrefix) {
        this.m3u8FilePrefix = m3u8FilePrefix;
        return this;
    }
    public String getM3u8FilePrefix() {
        return this.m3u8FilePrefix;
    }

    public VideoPreviewQuickVideoConfig setSegment(Long segment) {
        this.segment = segment;
        return this;
    }
    public Long getSegment() {
        return this.segment;
    }

    public VideoPreviewQuickVideoConfig setSubtitleConfig(VideoPreviewLiveTranscodingSubtitleConfig subtitleConfig) {
        this.subtitleConfig = subtitleConfig;
        return this;
    }
    public VideoPreviewLiveTranscodingSubtitleConfig getSubtitleConfig() {
        return this.subtitleConfig;
    }

    public VideoPreviewQuickVideoConfig setTemplateList(java.util.List<String> templateList) {
        this.templateList = templateList;
        return this;
    }
    public java.util.List<String> getTemplateList() {
        return this.templateList;
    }

    public VideoPreviewQuickVideoConfig setTemplateNameMap(java.util.Map<String, ?> templateNameMap) {
        this.templateNameMap = templateNameMap;
        return this;
    }
    public java.util.Map<String, ?> getTemplateNameMap() {
        return this.templateNameMap;
    }

    public VideoPreviewQuickVideoConfig setTsCountWhenTs404(Long tsCountWhenTs404) {
        this.tsCountWhenTs404 = tsCountWhenTs404;
        return this;
    }
    public Long getTsCountWhenTs404() {
        return this.tsCountWhenTs404;
    }

}
