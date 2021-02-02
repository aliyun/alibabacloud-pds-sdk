// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.hostingmode.client.models;

import com.aliyun.tea.*;

/**
 * 文件移动请求
 */
public class HostingMoveFileRequest extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // drive_id
    @NameInMap("drive_id")
    @Validation(pattern = "[0-9]+")
    public String driveId;

    // file_path
    @NameInMap("file_path")
    public String filePath;

    // new_name
    @NameInMap("new_name")
    public String newName;

    // overwrite
    // type: boolean
    @NameInMap("overwrite")
    public Boolean overwrite;

    // share_id
    @NameInMap("share_id")
    @Validation(pattern = "[0-9a-zA-Z-]+")
    public String shareId;

    // file_path
    @NameInMap("to_parent_file_path")
    public String toParentFilePath;

    public static HostingMoveFileRequest build(java.util.Map<String, ?> map) throws Exception {
        HostingMoveFileRequest self = new HostingMoveFileRequest();
        return TeaModel.build(map, self);
    }

    public HostingMoveFileRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public HostingMoveFileRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public HostingMoveFileRequest setFilePath(String filePath) {
        this.filePath = filePath;
        return this;
    }
    public String getFilePath() {
        return this.filePath;
    }

    public HostingMoveFileRequest setNewName(String newName) {
        this.newName = newName;
        return this;
    }
    public String getNewName() {
        return this.newName;
    }

    public HostingMoveFileRequest setOverwrite(Boolean overwrite) {
        this.overwrite = overwrite;
        return this;
    }
    public Boolean getOverwrite() {
        return this.overwrite;
    }

    public HostingMoveFileRequest setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

    public HostingMoveFileRequest setToParentFilePath(String toParentFilePath) {
        this.toParentFilePath = toParentFilePath;
        return this;
    }
    public String getToParentFilePath() {
        return this.toParentFilePath;
    }

}
