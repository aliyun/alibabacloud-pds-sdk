// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * copy file request
 */
public class HostingCopyFileRequest extends TeaModel {
    /**
     * <p>addition_data</p>
     */
    @NameInMap("addition_data")
    public java.util.Map<String, ?> additionData;

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
    @Validation(required = true)
    public String filePath;

    /**
     * <p>new_name</p>
     */
    @NameInMap("new_name")
    @Validation(maxLength = 1024, minLength = 1)
    public String newName;

    /**
     * <p>overwrite</p>
     * <p>type: boolean</p>
     */
    @NameInMap("overwrite")
    public Boolean overwrite;

    @NameInMap("referer")
    public String referer;

    /**
     * <p>share_id</p>
     */
    @NameInMap("share_id")
    @Validation(pattern = "[0-9a-zA-Z-]+")
    public String shareId;

    /**
     * <p>to_drive_id</p>
     */
    @NameInMap("to_drive_id")
    @Validation(pattern = "[0-9]+")
    public String toDriveId;

    /**
     * <p>to_parent_file_path</p>
     */
    @NameInMap("to_parent_file_path")
    @Validation(required = true)
    public String toParentFilePath;

    /**
     * <p>share_id</p>
     */
    @NameInMap("to_share_id")
    public String toShareId;

    public static HostingCopyFileRequest build(java.util.Map<String, ?> map) throws Exception {
        HostingCopyFileRequest self = new HostingCopyFileRequest();
        return TeaModel.build(map, self);
    }

    public HostingCopyFileRequest setAdditionData(java.util.Map<String, ?> additionData) {
        this.additionData = additionData;
        return this;
    }
    public java.util.Map<String, ?> getAdditionData() {
        return this.additionData;
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

    public HostingCopyFileRequest setReferer(String referer) {
        this.referer = referer;
        return this;
    }
    public String getReferer() {
        return this.referer;
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
