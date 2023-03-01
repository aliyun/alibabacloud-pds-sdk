// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 视频转码配置
 */
public class VideoPreviewVideoConfig extends TeaModel {
    @NameInMap("default_output_ext")
    public String defaultOutputExt;

    @NameInMap("fix_resolution")
    public Boolean fixResolution;

    @NameInMap("keep_original")
    public Boolean keepOriginal;

    @NameInMap("m3u8_config")
    public VideoPreviewM3U8Config m3u8Config;

    @NameInMap("protection_system")
    public String protectionSystem;

    @NameInMap("support_ext")
    public java.util.List<String> supportExt;

    @NameInMap("template")
    public java.util.List<VideoPreviewVideoTemplate> template;

    public static VideoPreviewVideoConfig build(java.util.Map<String, ?> map) throws Exception {
        VideoPreviewVideoConfig self = new VideoPreviewVideoConfig();
        return TeaModel.build(map, self);
    }

    public VideoPreviewVideoConfig setDefaultOutputExt(String defaultOutputExt) {
        this.defaultOutputExt = defaultOutputExt;
        return this;
    }
    public String getDefaultOutputExt() {
        return this.defaultOutputExt;
    }

    public VideoPreviewVideoConfig setFixResolution(Boolean fixResolution) {
        this.fixResolution = fixResolution;
        return this;
    }
    public Boolean getFixResolution() {
        return this.fixResolution;
    }

    public VideoPreviewVideoConfig setKeepOriginal(Boolean keepOriginal) {
        this.keepOriginal = keepOriginal;
        return this;
    }
    public Boolean getKeepOriginal() {
        return this.keepOriginal;
    }

    public VideoPreviewVideoConfig setM3u8Config(VideoPreviewM3U8Config m3u8Config) {
        this.m3u8Config = m3u8Config;
        return this;
    }
    public VideoPreviewM3U8Config getM3u8Config() {
        return this.m3u8Config;
    }

    public VideoPreviewVideoConfig setProtectionSystem(String protectionSystem) {
        this.protectionSystem = protectionSystem;
        return this;
    }
    public String getProtectionSystem() {
        return this.protectionSystem;
    }

    public VideoPreviewVideoConfig setSupportExt(java.util.List<String> supportExt) {
        this.supportExt = supportExt;
        return this;
    }
    public java.util.List<String> getSupportExt() {
        return this.supportExt;
    }

    public VideoPreviewVideoConfig setTemplate(java.util.List<VideoPreviewVideoTemplate> template) {
        this.template = template;
        return this;
    }
    public java.util.List<VideoPreviewVideoTemplate> getTemplate() {
        return this.template;
    }

}
