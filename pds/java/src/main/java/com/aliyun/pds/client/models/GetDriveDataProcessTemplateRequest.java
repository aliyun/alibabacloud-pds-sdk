// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * get drive data process template request
 */
public class GetDriveDataProcessTemplateRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

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

    public GetDriveDataProcessTemplateRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public GetDriveDataProcessTemplateRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

}
