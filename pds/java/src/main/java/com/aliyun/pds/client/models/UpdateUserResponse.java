// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * Update user response
 */
public class UpdateUserResponse extends TeaModel {
    /**
     * <p>头像</p>
     */
    @NameInMap("avatar")
    public String avatar;

    /**
     * <p>用户创建时间</p>
     */
    @NameInMap("created_at")
    public Long createdAt;

    /**
     * <p>creator</p>
     */
    @NameInMap("creator")
    public String creator;

    /**
     * <p>默认 Drive ID</p>
     */
    @NameInMap("default_drive_id")
    public String defaultDriveId;

    @NameInMap("default_location")
    public String defaultLocation;

    /**
     * <p>禁止用户自行修改密码</p>
     */
    @NameInMap("deny_change_password_by_self")
    public Boolean denyChangePasswordBySelf;

    /**
     * <p>用户备注信息</p>
     */
    @NameInMap("description")
    public String description;

    /**
     * <p>Domain ID</p>
     */
    @NameInMap("domain_id")
    public String domainId;

    /**
     * <p>邮箱</p>
     */
    @NameInMap("email")
    public String email;

    /**
     * <p>用户过期时间</p>
     */
    @NameInMap("expired_at")
    public Long expiredAt;

    @NameInMap("is_sync")
    public Boolean isSync;

    @NameInMap("last_login_time")
    public Long lastLoginTime;

    /**
     * <p>下次登录强制修改密码</p>
     */
    @NameInMap("need_change_password_next_login")
    public Boolean needChangePasswordNextLogin;

    /**
     * <p>昵称</p>
     */
    @NameInMap("nick_name")
    public String nickName;

    @NameInMap("permission")
    public java.util.Map<String, ?> permission;

    /**
     * <p>电话</p>
     */
    @NameInMap("phone")
    public String phone;

    /**
     * <p>国家编码</p>
     */
    @NameInMap("phone_region")
    public String phoneRegion;

    /**
     * <p>用户处罚标志</p>
     */
    @NameInMap("punish_flag")
    public Long punishFlag;

    @NameInMap("punishments")
    public java.util.List<PunishmentResponse> punishments;

    /**
     * <p>角色</p>
     */
    @NameInMap("role")
    public String role;

    /**
     * <p>用户状态</p>
     */
    @NameInMap("status")
    public String status;

    /**
     * <p>用户修改时间</p>
     */
    @NameInMap("updated_at")
    public Long updatedAt;

    /**
     * <p>用户自定义数据，格式为json，可用于配置项、少量临时数据等存储，不超过1K</p>
     */
    @NameInMap("user_data")
    public java.util.Map<String, ?> userData;

    /**
     * <p>用户 ID</p>
     */
    @NameInMap("user_id")
    public String userId;

    /**
     * <p>用户名称</p>
     */
    @NameInMap("user_name")
    public String userName;

    public static UpdateUserResponse build(java.util.Map<String, ?> map) throws Exception {
        UpdateUserResponse self = new UpdateUserResponse();
        return TeaModel.build(map, self);
    }

    public UpdateUserResponse setAvatar(String avatar) {
        this.avatar = avatar;
        return this;
    }
    public String getAvatar() {
        return this.avatar;
    }

    public UpdateUserResponse setCreatedAt(Long createdAt) {
        this.createdAt = createdAt;
        return this;
    }
    public Long getCreatedAt() {
        return this.createdAt;
    }

    public UpdateUserResponse setCreator(String creator) {
        this.creator = creator;
        return this;
    }
    public String getCreator() {
        return this.creator;
    }

    public UpdateUserResponse setDefaultDriveId(String defaultDriveId) {
        this.defaultDriveId = defaultDriveId;
        return this;
    }
    public String getDefaultDriveId() {
        return this.defaultDriveId;
    }

    public UpdateUserResponse setDefaultLocation(String defaultLocation) {
        this.defaultLocation = defaultLocation;
        return this;
    }
    public String getDefaultLocation() {
        return this.defaultLocation;
    }

    public UpdateUserResponse setDenyChangePasswordBySelf(Boolean denyChangePasswordBySelf) {
        this.denyChangePasswordBySelf = denyChangePasswordBySelf;
        return this;
    }
    public Boolean getDenyChangePasswordBySelf() {
        return this.denyChangePasswordBySelf;
    }

    public UpdateUserResponse setDescription(String description) {
        this.description = description;
        return this;
    }
    public String getDescription() {
        return this.description;
    }

    public UpdateUserResponse setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public UpdateUserResponse setEmail(String email) {
        this.email = email;
        return this;
    }
    public String getEmail() {
        return this.email;
    }

    public UpdateUserResponse setExpiredAt(Long expiredAt) {
        this.expiredAt = expiredAt;
        return this;
    }
    public Long getExpiredAt() {
        return this.expiredAt;
    }

    public UpdateUserResponse setIsSync(Boolean isSync) {
        this.isSync = isSync;
        return this;
    }
    public Boolean getIsSync() {
        return this.isSync;
    }

    public UpdateUserResponse setLastLoginTime(Long lastLoginTime) {
        this.lastLoginTime = lastLoginTime;
        return this;
    }
    public Long getLastLoginTime() {
        return this.lastLoginTime;
    }

    public UpdateUserResponse setNeedChangePasswordNextLogin(Boolean needChangePasswordNextLogin) {
        this.needChangePasswordNextLogin = needChangePasswordNextLogin;
        return this;
    }
    public Boolean getNeedChangePasswordNextLogin() {
        return this.needChangePasswordNextLogin;
    }

    public UpdateUserResponse setNickName(String nickName) {
        this.nickName = nickName;
        return this;
    }
    public String getNickName() {
        return this.nickName;
    }

    public UpdateUserResponse setPermission(java.util.Map<String, ?> permission) {
        this.permission = permission;
        return this;
    }
    public java.util.Map<String, ?> getPermission() {
        return this.permission;
    }

    public UpdateUserResponse setPhone(String phone) {
        this.phone = phone;
        return this;
    }
    public String getPhone() {
        return this.phone;
    }

    public UpdateUserResponse setPhoneRegion(String phoneRegion) {
        this.phoneRegion = phoneRegion;
        return this;
    }
    public String getPhoneRegion() {
        return this.phoneRegion;
    }

    public UpdateUserResponse setPunishFlag(Long punishFlag) {
        this.punishFlag = punishFlag;
        return this;
    }
    public Long getPunishFlag() {
        return this.punishFlag;
    }

    public UpdateUserResponse setPunishments(java.util.List<PunishmentResponse> punishments) {
        this.punishments = punishments;
        return this;
    }
    public java.util.List<PunishmentResponse> getPunishments() {
        return this.punishments;
    }

    public UpdateUserResponse setRole(String role) {
        this.role = role;
        return this;
    }
    public String getRole() {
        return this.role;
    }

    public UpdateUserResponse setStatus(String status) {
        this.status = status;
        return this;
    }
    public String getStatus() {
        return this.status;
    }

    public UpdateUserResponse setUpdatedAt(Long updatedAt) {
        this.updatedAt = updatedAt;
        return this;
    }
    public Long getUpdatedAt() {
        return this.updatedAt;
    }

    public UpdateUserResponse setUserData(java.util.Map<String, ?> userData) {
        this.userData = userData;
        return this;
    }
    public java.util.Map<String, ?> getUserData() {
        return this.userData;
    }

    public UpdateUserResponse setUserId(String userId) {
        this.userId = userId;
        return this;
    }
    public String getUserId() {
        return this.userId;
    }

    public UpdateUserResponse setUserName(String userName) {
        this.userName = userName;
        return this;
    }
    public String getUserName() {
        return this.userName;
    }

}
