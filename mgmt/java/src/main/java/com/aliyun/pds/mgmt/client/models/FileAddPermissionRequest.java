// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 文件共享/授权请求
 */
public class FileAddPermissionRequest extends TeaModel {
    // 文件所属的drive_id
    @NameInMap("drive_id")
    @Validation(required = true)
    public String driveId;

    // 文件的file_id
    @NameInMap("file_id")
    @Validation(required = true)
    public String fileId;

    // 被授权的用户或团队列表
    @NameInMap("member_list")
    @Validation(required = true)
    public java.util.List<FilePermissionMember> memberList;

    // 文件所属的subdomain_id
    @NameInMap("subdomain_id")
    public String subdomainId;

    public static FileAddPermissionRequest build(java.util.Map<String, ?> map) throws Exception {
        FileAddPermissionRequest self = new FileAddPermissionRequest();
        return TeaModel.build(map, self);
    }

    public FileAddPermissionRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public FileAddPermissionRequest setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

    public FileAddPermissionRequest setMemberList(java.util.List<FilePermissionMember> memberList) {
        this.memberList = memberList;
        return this;
    }
    public java.util.List<FilePermissionMember> getMemberList() {
        return this.memberList;
    }

    public FileAddPermissionRequest setSubdomainId(String subdomainId) {
        this.subdomainId = subdomainId;
        return this;
    }
    public String getSubdomainId() {
        return this.subdomainId;
    }

}
