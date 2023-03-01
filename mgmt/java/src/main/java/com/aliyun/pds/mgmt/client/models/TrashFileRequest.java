// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 删除文件请求，支持批量
 */
public class TrashFileRequest extends TeaModel {
    @NameInMap("check_folder_empty")
    public Boolean checkFolderEmpty;

    /**
     * <p>drive_id</p>
     */
    @NameInMap("drive_id")
    @Validation(pattern = "[0-9]+")
    public String driveId;

    /**
     * <p>file_id</p>
     */
    @NameInMap("file_id")
    @Validation(required = true, pattern = "[a-z0-9]{1,50}", maxLength = 50, minLength = 40)
    public String fileId;

    /**
     * <p>share_id, either share_id or drive_id is required</p>
     */
    @NameInMap("share_id")
    public String shareId;

    public static TrashFileRequest build(java.util.Map<String, ?> map) throws Exception {
        TrashFileRequest self = new TrashFileRequest();
        return TeaModel.build(map, self);
    }

    public TrashFileRequest setCheckFolderEmpty(Boolean checkFolderEmpty) {
        this.checkFolderEmpty = checkFolderEmpty;
        return this;
    }
    public Boolean getCheckFolderEmpty() {
        return this.checkFolderEmpty;
    }

    public TrashFileRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public TrashFileRequest setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

    public TrashFileRequest setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

}
