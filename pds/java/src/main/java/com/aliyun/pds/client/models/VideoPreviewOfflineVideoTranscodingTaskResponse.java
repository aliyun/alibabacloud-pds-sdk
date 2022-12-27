// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 离线视频转码task响应
 */
public class VideoPreviewOfflineVideoTranscodingTaskResponse extends TeaModel {
    /**
     * <p>keep_original_resolution 转码后的视频分辨率是否保持原画(template分辨率大于当前视频)</p>
     */
    @NameInMap("keep_original_resolution")
    public Boolean keepOriginalResolution;

    /**
     * <p>protection_system DRM加密方式</p>
     */
    @NameInMap("protection_system")
    public String protectionSystem;

    /**
     * <p>status, 转码状态</p>
     */
    @NameInMap("status")
    public String status;

    /**
     * <p>template_id, 转码模板id</p>
     */
    @NameInMap("template_id")
    public String templateId;

    /**
     * <p>url, 视频播放地址</p>
     */
    @NameInMap("url")
    public String url;

    public static VideoPreviewOfflineVideoTranscodingTaskResponse build(java.util.Map<String, ?> map) throws Exception {
        VideoPreviewOfflineVideoTranscodingTaskResponse self = new VideoPreviewOfflineVideoTranscodingTaskResponse();
        return TeaModel.build(map, self);
    }

    public VideoPreviewOfflineVideoTranscodingTaskResponse setKeepOriginalResolution(Boolean keepOriginalResolution) {
        this.keepOriginalResolution = keepOriginalResolution;
        return this;
    }
    public Boolean getKeepOriginalResolution() {
        return this.keepOriginalResolution;
    }

    public VideoPreviewOfflineVideoTranscodingTaskResponse setProtectionSystem(String protectionSystem) {
        this.protectionSystem = protectionSystem;
        return this;
    }
    public String getProtectionSystem() {
        return this.protectionSystem;
    }

    public VideoPreviewOfflineVideoTranscodingTaskResponse setStatus(String status) {
        this.status = status;
        return this;
    }
    public String getStatus() {
        return this.status;
    }

    public VideoPreviewOfflineVideoTranscodingTaskResponse setTemplateId(String templateId) {
        this.templateId = templateId;
        return this;
    }
    public String getTemplateId() {
        return this.templateId;
    }

    public VideoPreviewOfflineVideoTranscodingTaskResponse setUrl(String url) {
        this.url = url;
        return this;
    }
    public String getUrl() {
        return this.url;
    }

}
