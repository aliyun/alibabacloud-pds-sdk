// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * Get create story task request
 */
public class GetStoryTaskRequest extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // Drive ID
    @NameInMap("drive_id")
    @Validation(required = true)
    public String driveId;

    public static GetStoryTaskRequest build(java.util.Map<String, ?> map) throws Exception {
        GetStoryTaskRequest self = new GetStoryTaskRequest();
        return TeaModel.build(map, self);
    }

    public GetStoryTaskRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetStoryTaskRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

}
