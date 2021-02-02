// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.hostingmode.client.models;

import com.aliyun.tea.*;

/**
 * Base user response
 */
public class BaseUserResponse extends TeaModel {
    // 头像
    @NameInMap("avatar")
    public String avatar;

    // 用户创建时间
    @NameInMap("created_at")
    public Long createdAt;

    // 默认 Drive ID
    @NameInMap("default_drive_id")
    public String defaultDriveId;

    // 用户备注信息
    @NameInMap("description")
    public String description;

    // Domain ID
    @NameInMap("domain_id")
    public String domainId;

    // 邮箱
    @NameInMap("email")
    public String email;

    // 昵称
    @NameInMap("nick_name")
    public String nickName;

    // 电话
    @NameInMap("phone")
    public String phone;

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

    public static BaseUserResponse build(java.util.Map<String, ?> map) throws Exception {
        BaseUserResponse self = new BaseUserResponse();
        return TeaModel.build(map, self);
    }

    public BaseUserResponse setAvatar(String avatar) {
        this.avatar = avatar;
        return this;
    }
    public String getAvatar() {
        return this.avatar;
    }

    public BaseUserResponse setCreatedAt(Long createdAt) {
        this.createdAt = createdAt;
        return this;
    }
    public Long getCreatedAt() {
        return this.createdAt;
    }

    public BaseUserResponse setDefaultDriveId(String defaultDriveId) {
        this.defaultDriveId = defaultDriveId;
        return this;
    }
    public String getDefaultDriveId() {
        return this.defaultDriveId;
    }

    public BaseUserResponse setDescription(String description) {
        this.description = description;
        return this;
    }
    public String getDescription() {
        return this.description;
    }

    public BaseUserResponse setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public BaseUserResponse setEmail(String email) {
        this.email = email;
        return this;
    }
    public String getEmail() {
        return this.email;
    }

    public BaseUserResponse setNickName(String nickName) {
        this.nickName = nickName;
        return this;
    }
    public String getNickName() {
        return this.nickName;
    }

    public BaseUserResponse setPhone(String phone) {
        this.phone = phone;
        return this;
    }
    public String getPhone() {
        return this.phone;
    }

    public BaseUserResponse setRole(String role) {
        this.role = role;
        return this;
    }
    public String getRole() {
        return this.role;
    }

    public BaseUserResponse setStatus(String status) {
        this.status = status;
        return this;
    }
    public String getStatus() {
        return this.status;
    }

    public BaseUserResponse setUpdatedAt(Long updatedAt) {
        this.updatedAt = updatedAt;
        return this;
    }
    public Long getUpdatedAt() {
        return this.updatedAt;
    }

    public BaseUserResponse setUserData(java.util.Map<String, ?> userData) {
        this.userData = userData;
        return this;
    }
    public java.util.Map<String, ?> getUserData() {
        return this.userData;
    }

    public BaseUserResponse setUserId(String userId) {
        this.userId = userId;
        return this;
    }
    public String getUserId() {
        return this.userId;
    }

    public BaseUserResponse setUserName(String userName) {
        this.userName = userName;
        return this;
    }
    public String getUserName() {
        return this.userName;
    }

}
