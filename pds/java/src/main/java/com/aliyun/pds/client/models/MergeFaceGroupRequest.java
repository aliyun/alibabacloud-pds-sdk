// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * Merge face group request
 */
public class MergeFaceGroupRequest extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // drive_id
    @NameInMap("drive_id")
    @Validation(required = true, pattern = "[0-9]+")
    public String driveId;

    // from_group_id
    @NameInMap("from_group_id")
    @Validation(required = true)
    public String fromGroupId;

    // to_group_id
    @NameInMap("to_group_id")
    @Validation(required = true)
    public String toGroupId;

    public static MergeFaceGroupRequest build(java.util.Map<String, ?> map) throws Exception {
        MergeFaceGroupRequest self = new MergeFaceGroupRequest();
        return TeaModel.build(map, self);
    }

    public MergeFaceGroupRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public MergeFaceGroupRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public MergeFaceGroupRequest setFromGroupId(String fromGroupId) {
        this.fromGroupId = fromGroupId;
        return this;
    }
    public String getFromGroupId() {
        return this.fromGroupId;
    }

    public MergeFaceGroupRequest setToGroupId(String toGroupId) {
        this.toGroupId = toGroupId;
        return this;
    }
    public String getToGroupId() {
        return this.toGroupId;
    }

}
