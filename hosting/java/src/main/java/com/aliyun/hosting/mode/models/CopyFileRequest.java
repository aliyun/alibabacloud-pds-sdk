// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

/**
 * 文件拷贝
 */
public class CopyFileRequest extends TeaModel {
    // auto_rename
    // type: boolean
    @NameInMap("auto_rename")
    public Boolean autoRename;

    // drive_id
    @NameInMap("drive_id")
    @Validation(pattern = "[0-9]+")
    public String driveId;

    // file_id
    @NameInMap("file_id")
    @Validation(required = true, pattern = "[a-z0-9.-_]{1,50}", maxLength = 50, minLength = 40)
    public String fileId;

    // new_name
    @NameInMap("new_name")
    @Validation(maxLength = 1024, minLength = 1)
    public String newName;

    // share_id, either share_id or drive_id is required
    @NameInMap("share_id")
    public String shareId;

    // to_drive_id
    @NameInMap("to_drive_id")
    @Validation(pattern = "[0-9]+")
    public String toDriveId;

    // to_parent_file_id
    @NameInMap("to_parent_file_id")
    @Validation(required = true, pattern = "[a-z0-9.-_]{1,50}", maxLength = 50, minLength = 4)
    public String toParentFileId;

    public static CopyFileRequest build(java.util.Map<String, ?> map) throws Exception {
        CopyFileRequest self = new CopyFileRequest();
        return TeaModel.build(map, self);
    }

    public CopyFileRequest setAutoRename(Boolean autoRename) {
        this.autoRename = autoRename;
        return this;
    }
    public Boolean getAutoRename() {
        return this.autoRename;
    }

    public CopyFileRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public CopyFileRequest setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

    public CopyFileRequest setNewName(String newName) {
        this.newName = newName;
        return this;
    }
    public String getNewName() {
        return this.newName;
    }

    public CopyFileRequest setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

    public CopyFileRequest setToDriveId(String toDriveId) {
        this.toDriveId = toDriveId;
        return this;
    }
    public String getToDriveId() {
        return this.toDriveId;
    }

    public CopyFileRequest setToParentFileId(String toParentFileId) {
        this.toParentFileId = toParentFileId;
        return this;
    }
    public String getToParentFileId() {
        return this.toParentFileId;
    }

}
