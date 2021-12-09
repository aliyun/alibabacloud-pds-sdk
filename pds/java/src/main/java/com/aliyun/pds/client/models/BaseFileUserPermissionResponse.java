// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 用户文件共享/授权列表返回信息
 */
public class BaseFileUserPermissionResponse extends TeaModel {
    // 当前用户是否能访问此授权
    @NameInMap("can_access")
    @Validation(required = true)
    public Boolean canAccess;

    // 创建时间
    @NameInMap("created_at")
    @Validation(required = true)
    public Long createdAt;

    // 创建者的UserID
    @NameInMap("creator")
    @Validation(required = true)
    public String creator;

    // 是否禁用子团队继承
    @NameInMap("disinherit_sub_group")
    @Validation(required = true)
    public Boolean disinheritSubGroup;

    // domain_id
    @NameInMap("domain_id")
    @Validation(required = true)
    public String domainId;

    // 被授权的driveID
    @NameInMap("drive_id")
    @Validation(required = true)
    public String driveId;

    // 过期时间
    @NameInMap("expire_time")
    @Validation(required = true)
    public Long expireTime;

    // 授权的文件ID
    @NameInMap("file_full_path")
    @Validation(required = true)
    public String fileFullPath;

    // 授权的文件ID
    @NameInMap("file_id")
    @Validation(required = true)
    public String fileId;

    @NameInMap("identity")
    @Validation(required = true)
    public Identity identity;

    // 授予的角色
    @NameInMap("role_id")
    @Validation(required = true)
    public String roleId;

    public static BaseFileUserPermissionResponse build(java.util.Map<String, ?> map) throws Exception {
        BaseFileUserPermissionResponse self = new BaseFileUserPermissionResponse();
        return TeaModel.build(map, self);
    }

    public BaseFileUserPermissionResponse setCanAccess(Boolean canAccess) {
        this.canAccess = canAccess;
        return this;
    }
    public Boolean getCanAccess() {
        return this.canAccess;
    }

    public BaseFileUserPermissionResponse setCreatedAt(Long createdAt) {
        this.createdAt = createdAt;
        return this;
    }
    public Long getCreatedAt() {
        return this.createdAt;
    }

    public BaseFileUserPermissionResponse setCreator(String creator) {
        this.creator = creator;
        return this;
    }
    public String getCreator() {
        return this.creator;
    }

    public BaseFileUserPermissionResponse setDisinheritSubGroup(Boolean disinheritSubGroup) {
        this.disinheritSubGroup = disinheritSubGroup;
        return this;
    }
    public Boolean getDisinheritSubGroup() {
        return this.disinheritSubGroup;
    }

    public BaseFileUserPermissionResponse setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public BaseFileUserPermissionResponse setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public BaseFileUserPermissionResponse setExpireTime(Long expireTime) {
        this.expireTime = expireTime;
        return this;
    }
    public Long getExpireTime() {
        return this.expireTime;
    }

    public BaseFileUserPermissionResponse setFileFullPath(String fileFullPath) {
        this.fileFullPath = fileFullPath;
        return this;
    }
    public String getFileFullPath() {
        return this.fileFullPath;
    }

    public BaseFileUserPermissionResponse setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

    public BaseFileUserPermissionResponse setIdentity(Identity identity) {
        this.identity = identity;
        return this;
    }
    public Identity getIdentity() {
        return this.identity;
    }

    public BaseFileUserPermissionResponse setRoleId(String roleId) {
        this.roleId = roleId;
        return this;
    }
    public String getRoleId() {
        return this.roleId;
    }

}
