// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 还原文件response
 */
public class RestoreFileResponse extends TeaModel {
    // async_task_id
    @NameInMap("async_task_id")
    public String asyncTaskId;

    // domain_id
    @NameInMap("domain_id")
    public String domainId;

    // drive_id
    @NameInMap("drive_id")
    public String driveId;

    // file_id
    @NameInMap("file_id")
    public String fileId;

    public static RestoreFileResponse build(java.util.Map<String, ?> map) throws Exception {
        RestoreFileResponse self = new RestoreFileResponse();
        return TeaModel.build(map, self);
    }

    public RestoreFileResponse setAsyncTaskId(String asyncTaskId) {
        this.asyncTaskId = asyncTaskId;
        return this;
    }
    public String getAsyncTaskId() {
        return this.asyncTaskId;
    }

    public RestoreFileResponse setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public RestoreFileResponse setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public RestoreFileResponse setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

}
