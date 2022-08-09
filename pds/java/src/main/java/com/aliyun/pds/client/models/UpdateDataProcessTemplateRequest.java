// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * update data process template request
 */
public class UpdateDataProcessTemplateRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    @NameInMap("resource_id")
    public String resourceId;

    @NameInMap("resource_type")
    public String resourceType;

    @NameInMap("template")
    public String template;

    @NameInMap("user_id")
    public String userId;

    public static UpdateDataProcessTemplateRequest build(java.util.Map<String, ?> map) throws Exception {
        UpdateDataProcessTemplateRequest self = new UpdateDataProcessTemplateRequest();
        return TeaModel.build(map, self);
    }

    public UpdateDataProcessTemplateRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public UpdateDataProcessTemplateRequest setResourceId(String resourceId) {
        this.resourceId = resourceId;
        return this;
    }
    public String getResourceId() {
        return this.resourceId;
    }

    public UpdateDataProcessTemplateRequest setResourceType(String resourceType) {
        this.resourceType = resourceType;
        return this;
    }
    public String getResourceType() {
        return this.resourceType;
    }

    public UpdateDataProcessTemplateRequest setTemplate(String template) {
        this.template = template;
        return this;
    }
    public String getTemplate() {
        return this.template;
    }

    public UpdateDataProcessTemplateRequest setUserId(String userId) {
        this.userId = userId;
        return this;
    }
    public String getUserId() {
        return this.userId;
    }

}
