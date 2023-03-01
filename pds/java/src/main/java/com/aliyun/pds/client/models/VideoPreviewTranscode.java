// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class VideoPreviewTranscode extends TeaModel {
    /**
     * <p>status</p>
     */
    @NameInMap("status")
    public String status;

    /**
     * <p>template_id</p>
     */
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
