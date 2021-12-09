// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 文件被共享/授权的成员列表
 */
public class FilePermissionMember extends TeaModel {
    // 子团队禁止继承此权限
    @NameInMap("disinherit_sub_group")
    public Boolean disinheritSubGroup;

    // 过期时间，传入时间戳，单位毫秒
    @NameInMap("expire_time")
    @Validation(required = true)
    public Long expireTime;

    @NameInMap("identity")
    @Validation(required = true)
    public Identity identity;

    // 授予的角色，目前支持：SystemFileOwner(文件协同)、SystemFileDownloader(下载者)、SystemFileEditor(编辑者)、SystemFileEditorWithoutDelete(无删除编辑者)、SystemFileEditorWithoutShareLink(无分享编辑者)、SystemFileMetaViewer(可见列表)、SystemFileUploader(上传者)、SystemFileUploaderAndDownloader(上传/下载者)、SystemFileDownloaderWithShareLink(下载/分享者)、SystemFileUploaderAndDownloaderWithShareLink(上传/下载/分享者)、SystemFileUploaderAndViewer(预览/上传者)、SystemFileUploaderWithShareLink(上传/分享者)、SystemFileViewer(预览者)
    @NameInMap("role_id")
    @Validation(required = true)
    public String roleId;

    public static FilePermissionMember build(java.util.Map<String, ?> map) throws Exception {
        FilePermissionMember self = new FilePermissionMember();
        return TeaModel.build(map, self);
    }

    public FilePermissionMember setDisinheritSubGroup(Boolean disinheritSubGroup) {
        this.disinheritSubGroup = disinheritSubGroup;
        return this;
    }
    public Boolean getDisinheritSubGroup() {
        return this.disinheritSubGroup;
    }

    public FilePermissionMember setExpireTime(Long expireTime) {
        this.expireTime = expireTime;
        return this;
    }
    public Long getExpireTime() {
        return this.expireTime;
    }

    public FilePermissionMember setIdentity(Identity identity) {
        this.identity = identity;
        return this;
    }
    public Identity getIdentity() {
        return this.identity;
    }

    public FilePermissionMember setRoleId(String roleId) {
        this.roleId = roleId;
        return this;
    }
    public String getRoleId() {
        return this.roleId;
    }

}
