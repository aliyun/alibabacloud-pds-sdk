// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * update drive data process template response
 */
public class UpdateDriveDataProcessTemplateResponse extends TeaModel {
    @NameInMap("drive_id")
    public String driveId;

    @NameInMap("template_id")
    public String templateId;

    public static UpdateDriveDataProcessTemplateResponse build(java.util.Map<String, ?> map) throws Exception {
        UpdateDriveDataProcessTemplateResponse self = new UpdateDriveDataProcessTemplateResponse();
        return TeaModel.build(map, self);
    }

    public UpdateDriveDataProcessTemplateResponse setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public UpdateDriveDataProcessTemplateResponse setTemplateId(String templateId) {
        this.templateId = templateId;
        return this;
    }
    public String getTemplateId() {
        return this.templateId;
    }

}
