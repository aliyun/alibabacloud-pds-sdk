// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 文件拷贝 response
 */
public class HostingCopyFileResponse extends TeaModel {
    // async_task_id
    @NameInMap("async_task_id")
    public String asyncTaskId;

    // domain_id
    @NameInMap("domain_id")
    @Validation(pattern = "[a-z0-9A-Z-]+")
    public String domainId;

    // drive_id
    @NameInMap("drive_id")
    @Validation(pattern = "[0-9]+")
    public String driveId;

    // file_path
    @NameInMap("file_path")
    public String filePath;

    // drive_id
    @NameInMap("share_id")
    @Validation(pattern = "[a-z0-9A-Z]+")
    public String shareId;

    public static HostingCopyFileResponse build(java.util.Map<String, ?> map) throws Exception {
        HostingCopyFileResponse self = new HostingCopyFileResponse();
        return TeaModel.build(map, self);
    }

    public HostingCopyFileResponse setAsyncTaskId(String asyncTaskId) {
        this.asyncTaskId = asyncTaskId;
        return this;
    }
    public String getAsyncTaskId() {
        return this.asyncTaskId;
    }

    public HostingCopyFileResponse setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public HostingCopyFileResponse setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public HostingCopyFileResponse setFilePath(String filePath) {
        this.filePath = filePath;
        return this;
    }
    public String getFilePath() {
        return this.filePath;
    }

    public HostingCopyFileResponse setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

}
