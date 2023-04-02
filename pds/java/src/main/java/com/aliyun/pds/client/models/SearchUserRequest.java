// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * # Search user request
 */
public class SearchUserRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    @NameInMap("drive_status")
    public String driveStatus;

    /**
     * <p>邮箱</p>
     */
    @NameInMap("email")
    public String email;

    @NameInMap("expired_at_range")
    public Int64Range expiredAtRange;

    /**
     * <p>每页大小限制</p>
     */
    @NameInMap("limit")
    @Validation(maximum = 100, minimum = 1)
    public Integer limit;

    /**
     * <p>翻页标记</p>
     */
    @NameInMap("marker")
    public String marker;

    /**
     * <p>昵称</p>
     */
    @NameInMap("nick_name")
    public String nickName;

    /**
     * <p>昵称-模糊搜索</p>
     */
    @NameInMap("nick_name_for_fuzzy")
    public String nickNameForFuzzy;

    @NameInMap("order_by")
    public String orderBy;

    @NameInMap("order_direction")
    public String orderDirection;

    /**
     * <p>电话号码</p>
     */
    @NameInMap("phone")
    public String phone;

    /**
     * <p>角色</p>
     */
    @NameInMap("role")
    public String role;

    /**
     * <p>状态</p>
     */
    @NameInMap("status")
    public String status;

    /**
     * <p>subdomain id</p>
     */
    @NameInMap("subdomain_id")
    public String subdomainId;

    /**
     * <p>用户名</p>
     */
    @NameInMap("user_name")
    public String userName;

    public static SearchUserRequest build(java.util.Map<String, ?> map) throws Exception {
        SearchUserRequest self = new SearchUserRequest();
        return TeaModel.build(map, self);
    }

    public SearchUserRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public SearchUserRequest setDriveStatus(String driveStatus) {
        this.driveStatus = driveStatus;
        return this;
    }
    public String getDriveStatus() {
        return this.driveStatus;
    }

    public SearchUserRequest setEmail(String email) {
        this.email = email;
        return this;
    }
    public String getEmail() {
        return this.email;
    }

    public SearchUserRequest setExpiredAtRange(Int64Range expiredAtRange) {
        this.expiredAtRange = expiredAtRange;
        return this;
    }
    public Int64Range getExpiredAtRange() {
        return this.expiredAtRange;
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

    public SearchUserRequest setNickNameForFuzzy(String nickNameForFuzzy) {
        this.nickNameForFuzzy = nickNameForFuzzy;
        return this;
    }
    public String getNickNameForFuzzy() {
        return this.nickNameForFuzzy;
    }

    public SearchUserRequest setOrderBy(String orderBy) {
        this.orderBy = orderBy;
        return this;
    }
    public String getOrderBy() {
        return this.orderBy;
    }

    public SearchUserRequest setOrderDirection(String orderDirection) {
        this.orderDirection = orderDirection;
        return this;
    }
    public String getOrderDirection() {
        return this.orderDirection;
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
