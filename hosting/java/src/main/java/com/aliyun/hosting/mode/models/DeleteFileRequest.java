// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

/**
 * 删除文件请求
 */
public class DeleteFileRequest extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // drive_id
    @NameInMap("drive_id")
    @Validation(pattern = "[0-9]+")
    public String driveId;

    @NameInMap("file_id")
    public String fileId;

    @NameInMap("file_id_path")
    public String fileIdPath;

    // permanently
    // type: false
    @NameInMap("permanently")
    public Boolean permanently;

    @NameInMap("share_id")
    public String shareId;

    public static DeleteFileRequest build(java.util.Map<String, ?> map) throws Exception {
        DeleteFileRequest self = new DeleteFileRequest();
        return TeaModel.build(map, self);
    }

    public DeleteFileRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public DeleteFileRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public DeleteFileRequest setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

    public DeleteFileRequest setFileIdPath(String fileIdPath) {
        this.fileIdPath = fileIdPath;
        return this;
    }
    public String getFileIdPath() {
        return this.fileIdPath;
    }

    public DeleteFileRequest setPermanently(Boolean permanently) {
        this.permanently = permanently;
        return this;
    }
    public Boolean getPermanently() {
        return this.permanently;
    }

    public DeleteFileRequest setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

}
