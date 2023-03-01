// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 取消文件共享/授权请求
 */
public class FileRemovePermissionRequest extends TeaModel {
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

    /**
     * <p>被取消授权的用户或团队列表</p>
     */
    @NameInMap("member_list")
    @Validation(required = true)
    public java.util.List<FilePermissionMember> memberList;

    /**
     * <p>文件所属的subdomain_id</p>
     */
    @NameInMap("subdomain_id")
    public String subdomainId;

    public static FileRemovePermissionRequest build(java.util.Map<String, ?> map) throws Exception {
        FileRemovePermissionRequest self = new FileRemovePermissionRequest();
        return TeaModel.build(map, self);
    }

    public FileRemovePermissionRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public FileRemovePermissionRequest setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

    public FileRemovePermissionRequest setMemberList(java.util.List<FilePermissionMember> memberList) {
        this.memberList = memberList;
        return this;
    }
    public java.util.List<FilePermissionMember> getMemberList() {
        return this.memberList;
    }

    public FileRemovePermissionRequest setSubdomainId(String subdomainId) {
        this.subdomainId = subdomainId;
        return this;
    }
    public String getSubdomainId() {
        return this.subdomainId;
    }

}
