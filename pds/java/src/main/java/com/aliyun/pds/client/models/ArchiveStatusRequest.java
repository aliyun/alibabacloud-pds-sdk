// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 获取解压任务状态
 */
public class ArchiveStatusRequest extends TeaModel {
    /**
     * <p>格式类型，如果是uc，使用特殊格式</p>
     */
    @NameInMap("Format")
    public String Format;

    @NameInMap("RequestID")
    public String RequestID;

    @NameInMap("archive_type")
    public String archiveType;

    @NameInMap("domain_id")
    public String domainId;

    /**
     * <p>TODO 增加对ShareID的支持</p>
     */
    @NameInMap("drive_id")
    public String driveId;

    @NameInMap("file_id")
    public String fileId;

    @NameInMap("password")
    public String password;

    @NameInMap("task_id")
    public String taskId;

    public static ArchiveStatusRequest build(java.util.Map<String, ?> map) throws Exception {
        ArchiveStatusRequest self = new ArchiveStatusRequest();
        return TeaModel.build(map, self);
    }

    public ArchiveStatusRequest setFormat(String Format) {
        this.Format = Format;
        return this;
    }
    public String getFormat() {
        return this.Format;
    }

    public ArchiveStatusRequest setRequestID(String RequestID) {
        this.RequestID = RequestID;
        return this;
    }
    public String getRequestID() {
        return this.RequestID;
    }

    public ArchiveStatusRequest setArchiveType(String archiveType) {
        this.archiveType = archiveType;
        return this;
    }
    public String getArchiveType() {
        return this.archiveType;
    }

    public ArchiveStatusRequest setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public ArchiveStatusRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public ArchiveStatusRequest setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

    public ArchiveStatusRequest setPassword(String password) {
        this.password = password;
        return this;
    }
    public String getPassword() {
        return this.password;
    }

    public ArchiveStatusRequest setTaskId(String taskId) {
        this.taskId = taskId;
        return this;
    }
    public String getTaskId() {
        return this.taskId;
    }

}
