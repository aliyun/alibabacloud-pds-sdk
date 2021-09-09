// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 获取解压任务状态
 */
public class ArchiveUncompressRequest extends TeaModel {
    // 格式类型，如果是uc，使用特殊格式
    @NameInMap("Format")
    public String Format;

    @NameInMap("RequestID")
    public String RequestID;

    @NameInMap("archive_type")
    public String archiveType;

    @NameInMap("domain_id")
    public String domainId;

    // TODO 增加对ShareID的支持
    @NameInMap("drive_id")
    public String driveId;

    @NameInMap("file_id")
    public String fileId;

    @NameInMap("password")
    public String password;

    @NameInMap("task_id")
    public String taskId;

    public static ArchiveUncompressRequest build(java.util.Map<String, ?> map) throws Exception {
        ArchiveUncompressRequest self = new ArchiveUncompressRequest();
        return TeaModel.build(map, self);
    }

    public ArchiveUncompressRequest setFormat(String Format) {
        this.Format = Format;
        return this;
    }
    public String getFormat() {
        return this.Format;
    }

    public ArchiveUncompressRequest setRequestID(String RequestID) {
        this.RequestID = RequestID;
        return this;
    }
    public String getRequestID() {
        return this.RequestID;
    }

    public ArchiveUncompressRequest setArchiveType(String archiveType) {
        this.archiveType = archiveType;
        return this;
    }
    public String getArchiveType() {
        return this.archiveType;
    }

    public ArchiveUncompressRequest setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public ArchiveUncompressRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public ArchiveUncompressRequest setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

    public ArchiveUncompressRequest setPassword(String password) {
        this.password = password;
        return this;
    }
    public String getPassword() {
        return this.password;
    }

    public ArchiveUncompressRequest setTaskId(String taskId) {
        this.taskId = taskId;
        return this;
    }
    public String getTaskId() {
        return this.taskId;
    }

}
