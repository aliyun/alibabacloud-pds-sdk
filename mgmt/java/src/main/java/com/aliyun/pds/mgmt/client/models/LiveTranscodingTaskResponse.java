// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 实时转码信息task响应
 */
public class LiveTranscodingTaskResponse extends TeaModel {
    // status
    @NameInMap("status")
    public String status;

    // template_id
    @NameInMap("template_id")
    public String templateId;

    // url
    @NameInMap("url")
    public String url;

    public static LiveTranscodingTaskResponse build(java.util.Map<String, ?> map) throws Exception {
        LiveTranscodingTaskResponse self = new LiveTranscodingTaskResponse();
        return TeaModel.build(map, self);
    }

    public LiveTranscodingTaskResponse setStatus(String status) {
        this.status = status;
        return this;
    }
    public String getStatus() {
        return this.status;
    }

    public LiveTranscodingTaskResponse setTemplateId(String templateId) {
        this.templateId = templateId;
        return this;
    }
    public String getTemplateId() {
        return this.templateId;
    }

    public LiveTranscodingTaskResponse setUrl(String url) {
        this.url = url;
        return this;
    }
    public String getUrl() {
        return this.url;
    }

}
