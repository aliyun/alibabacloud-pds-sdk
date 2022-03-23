// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 实时转码字幕配置
 */
public class VideoPreviewLiveTranscodingSubtitleConfig extends TeaModel {
    @NameInMap("enabled")
    public Boolean enabled;

    @NameInMap("extract_format")
    public String extractFormat;

    @NameInMap("subtitle_lang_list")
    public java.util.List<String> subtitleLangList;

    public static VideoPreviewLiveTranscodingSubtitleConfig build(java.util.Map<String, ?> map) throws Exception {
        VideoPreviewLiveTranscodingSubtitleConfig self = new VideoPreviewLiveTranscodingSubtitleConfig();
        return TeaModel.build(map, self);
    }

    public VideoPreviewLiveTranscodingSubtitleConfig setEnabled(Boolean enabled) {
        this.enabled = enabled;
        return this;
    }
    public Boolean getEnabled() {
        return this.enabled;
    }

    public VideoPreviewLiveTranscodingSubtitleConfig setExtractFormat(String extractFormat) {
        this.extractFormat = extractFormat;
        return this;
    }
    public String getExtractFormat() {
        return this.extractFormat;
    }

    public VideoPreviewLiveTranscodingSubtitleConfig setSubtitleLangList(java.util.List<String> subtitleLangList) {
        this.subtitleLangList = subtitleLangList;
        return this;
    }
    public java.util.List<String> getSubtitleLangList() {
        return this.subtitleLangList;
    }

}
