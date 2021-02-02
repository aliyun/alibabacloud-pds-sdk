// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.hostingmode.client.models;

import com.aliyun.tea.*;

/**
 * Create drive response
 */
public class CreateDriveResponse extends TeaModel {
    // Domain ID
    @NameInMap("domain_id")
    public String domainId;

    // Drive ID
    @NameInMap("drive_id")
    public String driveId;

    public static CreateDriveResponse build(java.util.Map<String, ?> map) throws Exception {
        CreateDriveResponse self = new CreateDriveResponse();
        return TeaModel.build(map, self);
    }

    public CreateDriveResponse setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public CreateDriveResponse setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

}
