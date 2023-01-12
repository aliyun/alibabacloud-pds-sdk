// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * update drive data process template request
 */
public class UpdateDriveDataProcessTemplateRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    /**
     * <p>drive_id</p>
     */
    @NameInMap("drive_id")
    @Validation(required = true, pattern = "[0-9]+")
    public String driveId;

    @NameInMap("template_id")
    public String templateId;

    public static UpdateDriveDataProcessTemplateRequest build(java.util.Map<String, ?> map) throws Exception {
        UpdateDriveDataProcessTemplateRequest self = new UpdateDriveDataProcessTemplateRequest();
        return TeaModel.build(map, self);
    }

    public UpdateDriveDataProcessTemplateRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public UpdateDriveDataProcessTemplateRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public UpdateDriveDataProcessTemplateRequest setTemplateId(String templateId) {
        this.templateId = templateId;
        return this;
    }
    public String getTemplateId() {
        return this.templateId;
    }

}
