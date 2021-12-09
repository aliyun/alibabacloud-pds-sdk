// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 查询文件继承的共享/授权列表请求
 */
public class FileListInheritPermissionRequest extends TeaModel {
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

    @NameInMap("subdomain_id")
    public String subdomainId;

    public static FileListInheritPermissionRequest build(java.util.Map<String, ?> map) throws Exception {
        FileListInheritPermissionRequest self = new FileListInheritPermissionRequest();
        return TeaModel.build(map, self);
    }

    public FileListInheritPermissionRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public FileListInheritPermissionRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public FileListInheritPermissionRequest setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

    public FileListInheritPermissionRequest setSubdomainId(String subdomainId) {
        this.subdomainId = subdomainId;
        return this;
    }
    public String getSubdomainId() {
        return this.subdomainId;
    }

}
