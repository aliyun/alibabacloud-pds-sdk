// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 离线音频转码task响应
 */
public class VideoPreviewOfflineAudioTranscodingTaskResponse extends TeaModel {
    /**
     * <p>status, 转码状态</p>
     */
    @NameInMap("status")
    public String status;

    /**
     * <p>template_bitrate, 音频码率，单位Kbps</p>
     */
    @NameInMap("template_bitrate")
    public Long templateBitrate;

    /**
     * <p>template_id, 转码模板id</p>
     */
    @NameInMap("template_id")
    public String templateId;

    /**
     * <p>template_name, 模板文案id</p>
     */
    @NameInMap("template_name")
    public String templateName;

    /**
     * <p>url, 播放地址</p>
     */
    @NameInMap("url")
    public String url;

    public static VideoPreviewOfflineAudioTranscodingTaskResponse build(java.util.Map<String, ?> map) throws Exception {
        VideoPreviewOfflineAudioTranscodingTaskResponse self = new VideoPreviewOfflineAudioTranscodingTaskResponse();
        return TeaModel.build(map, self);
    }

    public VideoPreviewOfflineAudioTranscodingTaskResponse setStatus(String status) {
        this.status = status;
        return this;
    }
    public String getStatus() {
        return this.status;
    }

    public VideoPreviewOfflineAudioTranscodingTaskResponse setTemplateBitrate(Long templateBitrate) {
        this.templateBitrate = templateBitrate;
        return this;
    }
    public Long getTemplateBitrate() {
        return this.templateBitrate;
    }

    public VideoPreviewOfflineAudioTranscodingTaskResponse setTemplateId(String templateId) {
        this.templateId = templateId;
        return this;
    }
    public String getTemplateId() {
        return this.templateId;
    }

    public VideoPreviewOfflineAudioTranscodingTaskResponse setTemplateName(String templateName) {
        this.templateName = templateName;
        return this;
    }
    public String getTemplateName() {
        return this.templateName;
    }

    public VideoPreviewOfflineAudioTranscodingTaskResponse setUrl(String url) {
        this.url = url;
        return this;
    }
    public String getUrl() {
        return this.url;
    }

}
