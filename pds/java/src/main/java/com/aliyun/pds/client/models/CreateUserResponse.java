// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * Create user response
 */
public class CreateUserResponse extends TeaModel {
    // 头像
    @NameInMap("avatar")
    public String avatar;

    // 用户创建时间
    @NameInMap("created_at")
    public Long createdAt;

    // creator
    @NameInMap("creator")
    public String creator;

    // 默认 Drive ID
    @NameInMap("default_drive_id")
    public String defaultDriveId;

    @NameInMap("default_location")
    public String defaultLocation;

    // 禁止用户自行修改密码
    @NameInMap("deny_change_password_by_self")
    public Boolean denyChangePasswordBySelf;

    // 用户备注信息
    @NameInMap("description")
    public String description;

    // Domain ID
    @NameInMap("domain_id")
    public String domainId;

    // 邮箱
    @NameInMap("email")
    public String email;

    // 用户过期时间
    @NameInMap("expired_at")
    public Long expiredAt;

    @NameInMap("is_sync")
    public Boolean isSync;

    @NameInMap("last_login_time")
    public Long lastLoginTime;

    // 下次登录强制修改密码
    @NameInMap("need_change_password_next_login")
    public Boolean needChangePasswordNextLogin;

    // 昵称
    @NameInMap("nick_name")
    public String nickName;

    @NameInMap("permission")
    public java.util.Map<String, ?> permission;

    // 电话
    @NameInMap("phone")
    public String phone;

    // 国家编码
    @NameInMap("phone_region")
    public String phoneRegion;

    // 用户处罚标志
    @NameInMap("punish_flag")
    public Long punishFlag;

    @NameInMap("punishments")
    public java.util.List<PunishmentResponse> punishments;

    // 角色
    @NameInMap("role")
    public String role;

    // 用户状态
    @NameInMap("status")
    public String status;

    // 用户修改时间
    @NameInMap("updated_at")
    public Long updatedAt;

    // 用户自定义数据，格式为json，可用于配置项、少量临时数据等存储，不超过1K
    @NameInMap("user_data")
    public java.util.Map<String, ?> userData;

    // 用户 ID
    @NameInMap("user_id")
    public String userId;

    // 用户名称
    @NameInMap("user_name")
    public String userName;

    public static CreateUserResponse build(java.util.Map<String, ?> map) throws Exception {
        CreateUserResponse self = new CreateUserResponse();
        return TeaModel.build(map, self);
    }

    public CreateUserResponse setAvatar(String avatar) {
        this.avatar = avatar;
        return this;
    }
    public String getAvatar() {
        return this.avatar;
    }

    public CreateUserResponse setCreatedAt(Long createdAt) {
        this.createdAt = createdAt;
        return this;
    }
    public Long getCreatedAt() {
        return this.createdAt;
    }

    public CreateUserResponse setCreator(String creator) {
        this.creator = creator;
        return this;
    }
    public String getCreator() {
        return this.creator;
    }

    public CreateUserResponse setDefaultDriveId(String defaultDriveId) {
        this.defaultDriveId = defaultDriveId;
        return this;
    }
    public String getDefaultDriveId() {
        return this.defaultDriveId;
    }

    public CreateUserResponse setDefaultLocation(String defaultLocation) {
        this.defaultLocation = defaultLocation;
        return this;
    }
    public String getDefaultLocation() {
        return this.defaultLocation;
    }

    public CreateUserResponse setDenyChangePasswordBySelf(Boolean denyChangePasswordBySelf) {
        this.denyChangePasswordBySelf = denyChangePasswordBySelf;
        return this;
    }
    public Boolean getDenyChangePasswordBySelf() {
        return this.denyChangePasswordBySelf;
    }

    public CreateUserResponse setDescription(String description) {
        this.description = description;
        return this;
    }
    public String getDescription() {
        return this.description;
    }

    public CreateUserResponse setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public CreateUserResponse setEmail(String email) {
        this.email = email;
        return this;
    }
    public String getEmail() {
        return this.email;
    }

    public CreateUserResponse setExpiredAt(Long expiredAt) {
        this.expiredAt = expiredAt;
        return this;
    }
    public Long getExpiredAt() {
        return this.expiredAt;
    }

    public CreateUserResponse setIsSync(Boolean isSync) {
        this.isSync = isSync;
        return this;
    }
    public Boolean getIsSync() {
        return this.isSync;
    }

    public CreateUserResponse setLastLoginTime(Long lastLoginTime) {
        this.lastLoginTime = lastLoginTime;
        return this;
    }
    public Long getLastLoginTime() {
        return this.lastLoginTime;
    }

    public CreateUserResponse setNeedChangePasswordNextLogin(Boolean needChangePasswordNextLogin) {
        this.needChangePasswordNextLogin = needChangePasswordNextLogin;
        return this;
    }
    public Boolean getNeedChangePasswordNextLogin() {
        return this.needChangePasswordNextLogin;
    }

    public CreateUserResponse setNickName(String nickName) {
        this.nickName = nickName;
        return this;
    }
    public String getNickName() {
        return this.nickName;
    }

    public CreateUserResponse setPermission(java.util.Map<String, ?> permission) {
        this.permission = permission;
        return this;
    }
    public java.util.Map<String, ?> getPermission() {
        return this.permission;
    }

    public CreateUserResponse setPhone(String phone) {
        this.phone = phone;
        return this;
    }
    public String getPhone() {
        return this.phone;
    }

    public CreateUserResponse setPhoneRegion(String phoneRegion) {
        this.phoneRegion = phoneRegion;
        return this;
    }
    public String getPhoneRegion() {
        return this.phoneRegion;
    }

    public CreateUserResponse setPunishFlag(Long punishFlag) {
        this.punishFlag = punishFlag;
        return this;
    }
    public Long getPunishFlag() {
        return this.punishFlag;
    }

    public CreateUserResponse setPunishments(java.util.List<PunishmentResponse> punishments) {
        this.punishments = punishments;
        return this;
    }
    public java.util.List<PunishmentResponse> getPunishments() {
        return this.punishments;
    }

    public CreateUserResponse setRole(String role) {
        this.role = role;
        return this;
    }
    public String getRole() {
        return this.role;
    }

    public CreateUserResponse setStatus(String status) {
        this.status = status;
        return this;
    }
    public String getStatus() {
        return this.status;
    }

    public CreateUserResponse setUpdatedAt(Long updatedAt) {
        this.updatedAt = updatedAt;
        return this;
    }
    public Long getUpdatedAt() {
        return this.updatedAt;
    }

    public CreateUserResponse setUserData(java.util.Map<String, ?> userData) {
        this.userData = userData;
        return this;
    }
    public java.util.Map<String, ?> getUserData() {
        return this.userData;
    }

    public CreateUserResponse setUserId(String userId) {
        this.userId = userId;
        return this;
    }
    public String getUserId() {
        return this.userId;
    }

    public CreateUserResponse setUserName(String userName) {
        this.userName = userName;
        return this;
    }
    public String getUserName() {
        return this.userName;
    }

}
