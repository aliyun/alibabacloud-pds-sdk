// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * Create user request
 */
public class CreateUserRequest extends TeaModel {
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

    @NameInMap("group_info_list")
    public java.util.List<GroupInfo> groupInfoList;

    // 用户地域
    @NameInMap("location")
    public String location;

    // 下次登录后是否强制修改密码
    @NameInMap("need_change_password_next_login")
    public Boolean needChangePasswordNextLogin;

    // 昵称
    @NameInMap("nick_name")
    public String nickName;

    // 电话号码
    @NameInMap("phone")
    public String phone;

    // 用户明文密码
    @NameInMap("plain_password")
    public String plainPassword;

    // 角色
    @NameInMap("role")
    public String role;

    // 状态
    @NameInMap("status")
    public String status;

    // subdomain id
    @NameInMap("subdomain_id")
    public String subdomainId;

    // 用户自定义数据，格式为json，可用于配置项、少量临时数据等存储，不超过1K
    @NameInMap("user_data")
    public java.util.Map<String, ?> userData;

    // 用户 ID
    @NameInMap("user_id")
    @Validation(required = true)
    public String userId;

    // 用户名称
    @NameInMap("user_name")
    public String userName;

    public static CreateUserRequest build(java.util.Map<String, ?> map) throws Exception {
        CreateUserRequest self = new CreateUserRequest();
        return TeaModel.build(map, self);
    }

    public CreateUserRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public CreateUserRequest setAvatar(String avatar) {
        this.avatar = avatar;
        return this;
    }
    public String getAvatar() {
        return this.avatar;
    }

    public CreateUserRequest setDenyChangePasswordBySelf(Boolean denyChangePasswordBySelf) {
        this.denyChangePasswordBySelf = denyChangePasswordBySelf;
        return this;
    }
    public Boolean getDenyChangePasswordBySelf() {
        return this.denyChangePasswordBySelf;
    }

    public CreateUserRequest setDescription(String description) {
        this.description = description;
        return this;
    }
    public String getDescription() {
        return this.description;
    }

    public CreateUserRequest setEmail(String email) {
        this.email = email;
        return this;
    }
    public String getEmail() {
        return this.email;
    }

    public CreateUserRequest setGroupInfoList(java.util.List<GroupInfo> groupInfoList) {
        this.groupInfoList = groupInfoList;
        return this;
    }
    public java.util.List<GroupInfo> getGroupInfoList() {
        return this.groupInfoList;
    }

    public CreateUserRequest setLocation(String location) {
        this.location = location;
        return this;
    }
    public String getLocation() {
        return this.location;
    }

    public CreateUserRequest setNeedChangePasswordNextLogin(Boolean needChangePasswordNextLogin) {
        this.needChangePasswordNextLogin = needChangePasswordNextLogin;
        return this;
    }
    public Boolean getNeedChangePasswordNextLogin() {
        return this.needChangePasswordNextLogin;
    }

    public CreateUserRequest setNickName(String nickName) {
        this.nickName = nickName;
        return this;
    }
    public String getNickName() {
        return this.nickName;
    }

    public CreateUserRequest setPhone(String phone) {
        this.phone = phone;
        return this;
    }
    public String getPhone() {
        return this.phone;
    }

    public CreateUserRequest setPlainPassword(String plainPassword) {
        this.plainPassword = plainPassword;
        return this;
    }
    public String getPlainPassword() {
        return this.plainPassword;
    }

    public CreateUserRequest setRole(String role) {
        this.role = role;
        return this;
    }
    public String getRole() {
        return this.role;
    }

    public CreateUserRequest setStatus(String status) {
        this.status = status;
        return this;
    }
    public String getStatus() {
        return this.status;
    }

    public CreateUserRequest setSubdomainId(String subdomainId) {
        this.subdomainId = subdomainId;
        return this;
    }
    public String getSubdomainId() {
        return this.subdomainId;
    }

    public CreateUserRequest setUserData(java.util.Map<String, ?> userData) {
        this.userData = userData;
        return this;
    }
    public java.util.Map<String, ?> getUserData() {
        return this.userData;
    }

    public CreateUserRequest setUserId(String userId) {
        this.userId = userId;
        return this;
    }
    public String getUserId() {
        return this.userId;
    }

    public CreateUserRequest setUserName(String userName) {
        this.userName = userName;
        return this;
    }
    public String getUserName() {
        return this.userName;
    }

}
