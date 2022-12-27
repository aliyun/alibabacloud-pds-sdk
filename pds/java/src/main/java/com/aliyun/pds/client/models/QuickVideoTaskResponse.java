// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 快速转码task响应
 */
public class QuickVideoTaskResponse extends TeaModel {
    // status, 转码状态
    @NameInMap("status")
    public String status;

    // template_height
    @NameInMap("template_height")
    public Long templateHeight;

    // template_id, 转码模板id
    @NameInMap("template_id")
    public String templateId;

    // template_name, 模板文案id
    @NameInMap("template_name")
    public String templateName;

    // template_width
    @NameInMap("template_width")
    public Long templateWidth;

    // url, 视频播放地址
    @NameInMap("url")
    public String url;

    public static QuickVideoTaskResponse build(java.util.Map<String, ?> map) throws Exception {
        QuickVideoTaskResponse self = new QuickVideoTaskResponse();
        return TeaModel.build(map, self);
    }

    public QuickVideoTaskResponse setStatus(String status) {
        this.status = status;
        return this;
    }
    public String getStatus() {
        return this.status;
    }

    public QuickVideoTaskResponse setTemplateHeight(Long templateHeight) {
        this.templateHeight = templateHeight;
        return this;
    }
    public Long getTemplateHeight() {
        return this.templateHeight;
    }

    public QuickVideoTaskResponse setTemplateId(String templateId) {
        this.templateId = templateId;
        return this;
    }
    public String getTemplateId() {
        return this.templateId;
    }

    public QuickVideoTaskResponse setTemplateName(String templateName) {
        this.templateName = templateName;
        return this;
    }
    public String getTemplateName() {
        return this.templateName;
    }

    public QuickVideoTaskResponse setTemplateWidth(Long templateWidth) {
        this.templateWidth = templateWidth;
        return this;
    }
    public Long getTemplateWidth() {
        return this.templateWidth;
    }

    public QuickVideoTaskResponse setUrl(String url) {
        this.url = url;
        return this;
    }
    public String getUrl() {
        return this.url;
    }

}
