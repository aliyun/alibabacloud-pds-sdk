// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * ClearRecycleBinResponse
 */
public class ClearRecycleBinResponse extends TeaModel {
    // async_task_id
    @NameInMap("async_task_id")
    public String asyncTaskId;

    // domain_id
    @NameInMap("domain_id")
    public String domainId;

    // drive_id
    @NameInMap("drive_id")
    public String driveId;

    // task_id
    @NameInMap("task_id")
    public String taskId;

    public static ClearRecycleBinResponse build(java.util.Map<String, ?> map) throws Exception {
        ClearRecycleBinResponse self = new ClearRecycleBinResponse();
        return TeaModel.build(map, self);
    }

    public ClearRecycleBinResponse setAsyncTaskId(String asyncTaskId) {
        this.asyncTaskId = asyncTaskId;
        return this;
    }
    public String getAsyncTaskId() {
        return this.asyncTaskId;
    }

    public ClearRecycleBinResponse setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public ClearRecycleBinResponse setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public ClearRecycleBinResponse setTaskId(String taskId) {
        this.taskId = taskId;
        return this;
    }
    public String getTaskId() {
        return this.taskId;
    }

}
