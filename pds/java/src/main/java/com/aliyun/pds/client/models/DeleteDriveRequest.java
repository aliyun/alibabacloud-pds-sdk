// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * Delete drive request
 */
public class DeleteDriveRequest extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // Drive ID
    @NameInMap("drive_id")
    @Validation(required = true)
    public String driveId;

    // Subdomain ID
    @NameInMap("subdomain_id")
    public String subdomainId;

    public static DeleteDriveRequest build(java.util.Map<String, ?> map) throws Exception {
        DeleteDriveRequest self = new DeleteDriveRequest();
        return TeaModel.build(map, self);
    }

    public DeleteDriveRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public DeleteDriveRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public DeleteDriveRequest setSubdomainId(String subdomainId) {
        this.subdomainId = subdomainId;
        return this;
    }
    public String getSubdomainId() {
        return this.subdomainId;
    }

}
