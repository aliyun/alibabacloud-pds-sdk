// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 删除文件 response
 */
public class HostingDeleteFileResponse extends TeaModel {
    /**
     * <p>async_task_id</p>
     */
    @NameInMap("async_task_id")
    public String asyncTaskId;

    /**
     * <p>domain_id</p>
     */
    @NameInMap("domain_id")
    @Validation(pattern = "[a-z0-9A-Z]+")
    public String domainId;

    /**
     * <p>drive_id</p>
     */
    @NameInMap("drive_id")
    @Validation(pattern = "[0-9]+")
    public String driveId;

    /**
     * <p>file_path</p>
     */
    @NameInMap("file_path")
    public String filePath;

    /**
     * <p>share_id</p>
     */
    @NameInMap("share_id")
    @Validation(pattern = "[a-z0-9A-Z]+")
    public String shareId;

    public static HostingDeleteFileResponse build(java.util.Map<String, ?> map) throws Exception {
        HostingDeleteFileResponse self = new HostingDeleteFileResponse();
        return TeaModel.build(map, self);
    }

    public HostingDeleteFileResponse setAsyncTaskId(String asyncTaskId) {
        this.asyncTaskId = asyncTaskId;
        return this;
    }
    public String getAsyncTaskId() {
        return this.asyncTaskId;
    }

    public HostingDeleteFileResponse setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public HostingDeleteFileResponse setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public HostingDeleteFileResponse setFilePath(String filePath) {
        this.filePath = filePath;
        return this;
    }
    public String getFilePath() {
        return this.filePath;
    }

    public HostingDeleteFileResponse setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

}
