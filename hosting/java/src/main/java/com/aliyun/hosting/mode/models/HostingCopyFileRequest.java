// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

/**
 * copy file request
 */
public class HostingCopyFileRequest extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // drive_id
    @NameInMap("drive_id")
    @Validation(pattern = "[0-9]+")
    public String driveId;

    // file_path
    @NameInMap("file_path")
    @Validation(required = true)
    public String filePath;

    // new_name
    @NameInMap("new_name")
    @Validation(pattern = "[a-zA-Z0-9.-]{1,1000}")
    public String newName;

    // overwrite
    // type: boolean
    @NameInMap("overwrite")
    public Boolean overwrite;

    // share_id
    @NameInMap("share_id")
    @Validation(pattern = "[0-9a-zA-Z-]+")
    public String shareId;

    // to_drive_id
    @NameInMap("to_drive_id")
    @Validation(pattern = "[0-9]+")
    public String toDriveId;

    // to_parent_file_path
    @NameInMap("to_parent_file_path")
    @Validation(required = true)
    public String toParentFilePath;

    // share_id
    @NameInMap("to_share_id")
    public String toShareId;

    public static HostingCopyFileRequest build(java.util.Map<String, ?> map) throws Exception {
        HostingCopyFileRequest self = new HostingCopyFileRequest();
        return TeaModel.build(map, self);
    }

    public HostingCopyFileRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public HostingCopyFileRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public HostingCopyFileRequest setFilePath(String filePath) {
        this.filePath = filePath;
        return this;
    }
    public String getFilePath() {
        return this.filePath;
    }

    public HostingCopyFileRequest setNewName(String newName) {
        this.newName = newName;
        return this;
    }
    public String getNewName() {
        return this.newName;
    }

    public HostingCopyFileRequest setOverwrite(Boolean overwrite) {
        this.overwrite = overwrite;
        return this;
    }
    public Boolean getOverwrite() {
        return this.overwrite;
    }

    public HostingCopyFileRequest setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

    public HostingCopyFileRequest setToDriveId(String toDriveId) {
        this.toDriveId = toDriveId;
        return this;
    }
    public String getToDriveId() {
        return this.toDriveId;
    }

    public HostingCopyFileRequest setToParentFilePath(String toParentFilePath) {
        this.toParentFilePath = toParentFilePath;
        return this;
    }
    public String getToParentFilePath() {
        return this.toParentFilePath;
    }

    public HostingCopyFileRequest setToShareId(String toShareId) {
        this.toShareId = toShareId;
        return this;
    }
    public String getToShareId() {
        return this.toShareId;
    }

}
