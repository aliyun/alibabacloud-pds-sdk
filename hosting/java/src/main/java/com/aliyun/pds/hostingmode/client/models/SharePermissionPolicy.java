// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.hostingmode.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class SharePermissionPolicy extends TeaModel {
    @NameInMap("file_id")
    public String fileId;

    @NameInMap("file_path")
    public String filePath;

    @NameInMap("permission_inheritable")
    public Boolean permissionInheritable;

    @NameInMap("permission_list")
    public java.util.List<String> permissionList;

    @NameInMap("permission_type")
    public String permissionType;

    public static SharePermissionPolicy build(java.util.Map<String, ?> map) throws Exception {
        SharePermissionPolicy self = new SharePermissionPolicy();
        return TeaModel.build(map, self);
    }

    public SharePermissionPolicy setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

    public SharePermissionPolicy setFilePath(String filePath) {
        this.filePath = filePath;
        return this;
    }
    public String getFilePath() {
        return this.filePath;
    }

    public SharePermissionPolicy setPermissionInheritable(Boolean permissionInheritable) {
        this.permissionInheritable = permissionInheritable;
        return this;
    }
    public Boolean getPermissionInheritable() {
        return this.permissionInheritable;
    }

    public SharePermissionPolicy setPermissionList(java.util.List<String> permissionList) {
        this.permissionList = permissionList;
        return this;
    }
    public java.util.List<String> getPermissionList() {
        return this.permissionList;
    }

    public SharePermissionPolicy setPermissionType(String permissionType) {
        this.permissionType = permissionType;
        return this;
    }
    public String getPermissionType() {
        return this.permissionType;
    }

}
