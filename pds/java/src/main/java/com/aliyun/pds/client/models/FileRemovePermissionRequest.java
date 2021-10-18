// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 取消文件共享/授权请求
 */
public class FileRemovePermissionRequest extends TeaModel {
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

    // 被取消授权的用户或团队列表
    @NameInMap("member_list")
    @Validation(required = true)
    public java.util.List<FilePermissionMember> memberList;

    public static FileRemovePermissionRequest build(java.util.Map<String, ?> map) throws Exception {
        FileRemovePermissionRequest self = new FileRemovePermissionRequest();
        return TeaModel.build(map, self);
    }

    public FileRemovePermissionRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
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

}
