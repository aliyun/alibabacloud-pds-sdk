// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 删除文件到回收站response
 */
public class TrashFileResponse extends TeaModel {
    /**
     * <p>async_task_id</p>
     */
    @NameInMap("async_task_id")
    public String asyncTaskId;

    /**
     * <p>domain_id</p>
     */
    @NameInMap("domain_id")
    public String domainId;

    /**
     * <p>drive_id</p>
     */
    @NameInMap("drive_id")
    public String driveId;

    /**
     * <p>file_id</p>
     */
    @NameInMap("file_id")
    public String fileId;

    public static TrashFileResponse build(java.util.Map<String, ?> map) throws Exception {
        TrashFileResponse self = new TrashFileResponse();
        return TeaModel.build(map, self);
    }

    public TrashFileResponse setAsyncTaskId(String asyncTaskId) {
        this.asyncTaskId = asyncTaskId;
        return this;
    }
    public String getAsyncTaskId() {
        return this.asyncTaskId;
    }

    public TrashFileResponse setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public TrashFileResponse setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public TrashFileResponse setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

}
