// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * Search user request
 */
public class SearchUserRequest extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // 邮箱
    @NameInMap("email")
    public String email;

    // 每页大小限制
    @NameInMap("limit")
    public Integer limit;

    // 翻页标记
    @NameInMap("marker")
    public String marker;

    // 昵称
    @NameInMap("nick_name")
    public String nickName;

    // 电话号码
    @NameInMap("phone")
    public String phone;

    // 角色
    @NameInMap("role")
    public String role;

    // 状态
    @NameInMap("status")
    public String status;

    // subdomain id
    @NameInMap("subdomain_id")
    public String subdomainId;

    // 用户名
    @NameInMap("user_name")
    public String userName;

    public static SearchUserRequest build(java.util.Map<String, ?> map) throws Exception {
        SearchUserRequest self = new SearchUserRequest();
        return TeaModel.build(map, self);
    }

    public SearchUserRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public SearchUserRequest setEmail(String email) {
        this.email = email;
        return this;
    }
    public String getEmail() {
        return this.email;
    }

    public SearchUserRequest setLimit(Integer limit) {
        this.limit = limit;
        return this;
    }
    public Integer getLimit() {
        return this.limit;
    }

    public SearchUserRequest setMarker(String marker) {
        this.marker = marker;
        return this;
    }
    public String getMarker() {
        return this.marker;
    }

    public SearchUserRequest setNickName(String nickName) {
        this.nickName = nickName;
        return this;
    }
    public String getNickName() {
        return this.nickName;
    }

    public SearchUserRequest setPhone(String phone) {
        this.phone = phone;
        return this;
    }
    public String getPhone() {
        return this.phone;
    }

    public SearchUserRequest setRole(String role) {
        this.role = role;
        return this;
    }
    public String getRole() {
        return this.role;
    }

    public SearchUserRequest setStatus(String status) {
        this.status = status;
        return this;
    }
    public String getStatus() {
        return this.status;
    }

    public SearchUserRequest setSubdomainId(String subdomainId) {
        this.subdomainId = subdomainId;
        return this;
    }
    public String getSubdomainId() {
        return this.subdomainId;
    }

    public SearchUserRequest setUserName(String userName) {
        this.userName = userName;
        return this;
    }
    public String getUserName() {
        return this.userName;
    }

}
