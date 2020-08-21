// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 故事任务状态
 */
public class GetStoryTaskResponse extends TeaModel {
    @NameInMap("drive_id")
    public String driveId;

    @NameInMap("status")
    public String status;

    public static GetStoryTaskResponse build(java.util.Map<String, ?> map) throws Exception {
        GetStoryTaskResponse self = new GetStoryTaskResponse();
        return TeaModel.build(map, self);
    }

    public GetStoryTaskResponse setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public GetStoryTaskResponse setStatus(String status) {
        this.status = status;
        return this;
    }
    public String getStatus() {
        return this.status;
    }

}
