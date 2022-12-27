// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class MediaPlayInfoTemplate extends TeaModel {
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

    /**
     * <p>url</p>
     */
    @NameInMap("url")
    public String url;

    public static MediaPlayInfoTemplate build(java.util.Map<String, ?> map) throws Exception {
        MediaPlayInfoTemplate self = new MediaPlayInfoTemplate();
        return TeaModel.build(map, self);
    }

    public MediaPlayInfoTemplate setStatus(String status) {
        this.status = status;
        return this;
    }
    public String getStatus() {
        return this.status;
    }

    public MediaPlayInfoTemplate setTemplateId(String templateId) {
        this.templateId = templateId;
        return this;
    }
    public String getTemplateId() {
        return this.templateId;
    }

    public MediaPlayInfoTemplate setUrl(String url) {
        this.url = url;
        return this;
    }
    public String getUrl() {
        return this.url;
    }

}
