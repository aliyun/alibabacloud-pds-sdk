// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * template update response
 */
public class UpdateDataProcessTemplateResponse extends TeaModel {
    @NameInMap("resource_id")
    public String resourceId;

    @NameInMap("resource_type")
    public String resourceType;

    @NameInMap("template")
    public String template;

    public static UpdateDataProcessTemplateResponse build(java.util.Map<String, ?> map) throws Exception {
        UpdateDataProcessTemplateResponse self = new UpdateDataProcessTemplateResponse();
        return TeaModel.build(map, self);
    }

    public UpdateDataProcessTemplateResponse setResourceId(String resourceId) {
        this.resourceId = resourceId;
        return this;
    }
    public String getResourceId() {
        return this.resourceId;
    }

    public UpdateDataProcessTemplateResponse setResourceType(String resourceType) {
        this.resourceType = resourceType;
        return this;
    }
    public String getResourceType() {
        return this.resourceType;
    }

    public UpdateDataProcessTemplateResponse setTemplate(String template) {
        this.template = template;
        return this;
    }
    public String getTemplate() {
        return this.template;
    }

}
