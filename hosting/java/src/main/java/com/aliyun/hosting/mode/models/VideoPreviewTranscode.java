// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class VideoPreviewTranscode extends TeaModel {
    // status
    @NameInMap("status")
    public String status;

    // template_id
    @NameInMap("template_id")
    public String templateId;

    public static VideoPreviewTranscode build(java.util.Map<String, ?> map) throws Exception {
        VideoPreviewTranscode self = new VideoPreviewTranscode();
        return TeaModel.build(map, self);
    }

    public VideoPreviewTranscode setStatus(String status) {
        this.status = status;
        return this;
    }
    public String getStatus() {
        return this.status;
    }

    public VideoPreviewTranscode setTemplateId(String templateId) {
        this.templateId = templateId;
        return this;
    }
    public String getTemplateId() {
        return this.templateId;
    }

}
