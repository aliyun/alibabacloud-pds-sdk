// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 列举当前文件的共享/授权记录请求
 */
public class FileListPermissionRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    // 文件所属的drive_id
    @NameInMap("drive_id")
    @Validation(required = true)
    public String driveId;

    // 文件的file_id
    @NameInMap("file_id")
    @Validation(required = true)
    public String fileId;

    public static FileListPermissionRequest build(java.util.Map<String, ?> map) throws Exception {
        FileListPermissionRequest self = new FileListPermissionRequest();
        return TeaModel.build(map, self);
    }

    public FileListPermissionRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public FileListPermissionRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public FileListPermissionRequest setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

}
