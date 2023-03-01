// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 列举当前文件的共享/授权记录请求
 */
public class FileListPermissionRequest extends TeaModel {
    /**
     * <p>文件所属的drive_id</p>
     */
    @NameInMap("drive_id")
    @Validation(required = true)
    public String driveId;

    /**
     * <p>文件的file_id</p>
     */
    @NameInMap("file_id")
    @Validation(required = true)
    public String fileId;

    @NameInMap("subdomain_id")
    public String subdomainId;

    public static FileListPermissionRequest build(java.util.Map<String, ?> map) throws Exception {
        FileListPermissionRequest self = new FileListPermissionRequest();
        return TeaModel.build(map, self);
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

    public FileListPermissionRequest setSubdomainId(String subdomainId) {
        this.subdomainId = subdomainId;
        return this;
    }
    public String getSubdomainId() {
        return this.subdomainId;
    }

}
