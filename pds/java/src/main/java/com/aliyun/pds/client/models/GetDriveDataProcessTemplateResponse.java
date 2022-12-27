// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * get drive data process template response
 */
public class GetDriveDataProcessTemplateResponse extends TeaModel {
    @NameInMap("template_id")
    public String templateId;

    public static GetDriveDataProcessTemplateResponse build(java.util.Map<String, ?> map) throws Exception {
        GetDriveDataProcessTemplateResponse self = new GetDriveDataProcessTemplateResponse();
        return TeaModel.build(map, self);
    }

    public GetDriveDataProcessTemplateResponse setTemplateId(String templateId) {
        this.templateId = templateId;
        return this;
    }
    public String getTemplateId() {
        return this.templateId;
    }

}
