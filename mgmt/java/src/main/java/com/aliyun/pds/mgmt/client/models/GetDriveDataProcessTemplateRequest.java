// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * get drive data process template request
 */
public class GetDriveDataProcessTemplateRequest extends TeaModel {
    /**
     * <p>drive_id</p>
     */
    @NameInMap("drive_id")
    @Validation(required = true, pattern = "[0-9]+")
    public String driveId;

    public static GetDriveDataProcessTemplateRequest build(java.util.Map<String, ?> map) throws Exception {
        GetDriveDataProcessTemplateRequest self = new GetDriveDataProcessTemplateRequest();
        return TeaModel.build(map, self);
    }

    public GetDriveDataProcessTemplateRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

}
