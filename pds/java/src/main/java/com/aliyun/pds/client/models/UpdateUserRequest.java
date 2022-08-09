// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * Update user request
 */
public class UpdateUserRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    // 头像
    @NameInMap("avatar")
    public String avatar;

    // 是否能自己修改密码
    @NameInMap("deny_change_password_by_self")
    public Boolean denyChangePasswordBySelf;

    // 描述信息
    @NameInMap("description")
    @Validation(maxLength = 1024)
    public String description;

    // 邮箱
    @NameInMap("email")
    public String email;

    // 用户过期时间
    @NameInMap("expired_at")
    public Long expiredAt;

    @NameInMap("group_info_list")
    public java.util.List<GroupInfo> groupInfoList;

    // 下次登录后是否强制修改密码
    @NameInMap("need_change_password_next_login")
    public Boolean needChangePasswordNextLogin;

    // 昵称
    @NameInMap("nick_name")
    public String nickName;

    // 电话号码
    @NameInMap("phone")
    public String phone;

    // 国家编码
    @NameInMap("phone_region")
    public String phoneRegion;

    // 用户明文密码
    @NameInMap("plain_password")
    public String plainPassword;

    // 角色
    @NameInMap("role")
    public String role;

    // 状态
    @NameInMap("status")
    public String status;

    // 用户自定义数据，格式为json，可用于配置项、少量临时数据等存储，不超过1K
    @NameInMap("user_data")
    public java.util.Map<String, ?> userData;

    // 用户 ID
    @NameInMap("user_id")
    @Validation(required = true)
    public String userId;

    public static UpdateUserRequest build(java.util.Map<String, ?> map) throws Exception {
        UpdateUserRequest self = new UpdateUserRequest();
        return TeaModel.build(map, self);
    }

    public UpdateUserRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public UpdateUserRequest setAvatar(String avatar) {
        this.avatar = avatar;
        return this;
    }
    public String getAvatar() {
        return this.avatar;
    }

    public UpdateUserRequest setDenyChangePasswordBySelf(Boolean denyChangePasswordBySelf) {
        this.denyChangePasswordBySelf = denyChangePasswordBySelf;
        return this;
    }
    public Boolean getDenyChangePasswordBySelf() {
        return this.denyChangePasswordBySelf;
    }

    public UpdateUserRequest setDescription(String description) {
        this.description = description;
        return this;
    }
    public String getDescription() {
        return this.description;
    }

    public UpdateUserRequest setEmail(String email) {
        this.email = email;
        return this;
    }
    public String getEmail() {
        return this.email;
    }

    public UpdateUserRequest setExpiredAt(Long expiredAt) {
        this.expiredAt = expiredAt;
        return this;
    }
    public Long getExpiredAt() {
        return this.expiredAt;
    }

    public UpdateUserRequest setGroupInfoList(java.util.List<GroupInfo> groupInfoList) {
        this.groupInfoList = groupInfoList;
        return this;
    }
    public java.util.List<GroupInfo> getGroupInfoList() {
        return this.groupInfoList;
    }

    public UpdateUserRequest setNeedChangePasswordNextLogin(Boolean needChangePasswordNextLogin) {
        this.needChangePasswordNextLogin = needChangePasswordNextLogin;
        return this;
    }
    public Boolean getNeedChangePasswordNextLogin() {
        return this.needChangePasswordNextLogin;
    }

    public UpdateUserRequest setNickName(String nickName) {
        this.nickName = nickName;
        return this;
    }
    public String getNickName() {
        return this.nickName;
    }

    public UpdateUserRequest setPhone(String phone) {
        this.phone = phone;
        return this;
    }
    public String getPhone() {
        return this.phone;
    }

    public UpdateUserRequest setPhoneRegion(String phoneRegion) {
        this.phoneRegion = phoneRegion;
        return this;
    }
    public String getPhoneRegion() {
        return this.phoneRegion;
    }

    public UpdateUserRequest setPlainPassword(String plainPassword) {
        this.plainPassword = plainPassword;
        return this;
    }
    public String getPlainPassword() {
        return this.plainPassword;
    }

    public UpdateUserRequest setRole(String role) {
        this.role = role;
        return this;
    }
    public String getRole() {
        return this.role;
    }

    public UpdateUserRequest setStatus(String status) {
        this.status = status;
        return this;
    }
    public String getStatus() {
        return this.status;
    }

    public UpdateUserRequest setUserData(java.util.Map<String, ?> userData) {
        this.userData = userData;
        return this;
    }
    public java.util.Map<String, ?> getUserData() {
        return this.userData;
    }

    public UpdateUserRequest setUserId(String userId) {
        this.userId = userId;
        return this;
    }
    public String getUserId() {
        return this.userId;
    }

}
