// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class CreateMembershipRequest extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // 描述
    @NameInMap("description")
    public String description;

    // group id
    @NameInMap("group_id")
    public String groupId;

    // 角色， member or admin
    @NameInMap("member_role")
    public String memberRole;

    @NameInMap("member_type")
    public String memberType;

    @NameInMap("sub_group_id")
    public String subGroupId;

    @NameInMap("subdomain_id")
    public String subdomainId;

    @NameInMap("user_id")
    public String userId;

    public static CreateMembershipRequest build(java.util.Map<String, ?> map) throws Exception {
        CreateMembershipRequest self = new CreateMembershipRequest();
        return TeaModel.build(map, self);
    }

    public CreateMembershipRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public CreateMembershipRequest setDescription(String description) {
        this.description = description;
        return this;
    }
    public String getDescription() {
        return this.description;
    }

    public CreateMembershipRequest setGroupId(String groupId) {
        this.groupId = groupId;
        return this;
    }
    public String getGroupId() {
        return this.groupId;
    }

    public CreateMembershipRequest setMemberRole(String memberRole) {
        this.memberRole = memberRole;
        return this;
    }
    public String getMemberRole() {
        return this.memberRole;
    }

    public CreateMembershipRequest setMemberType(String memberType) {
        this.memberType = memberType;
        return this;
    }
    public String getMemberType() {
        return this.memberType;
    }

    public CreateMembershipRequest setSubGroupId(String subGroupId) {
        this.subGroupId = subGroupId;
        return this;
    }
    public String getSubGroupId() {
        return this.subGroupId;
    }

    public CreateMembershipRequest setSubdomainId(String subdomainId) {
        this.subdomainId = subdomainId;
        return this;
    }
    public String getSubdomainId() {
        return this.subdomainId;
    }

    public CreateMembershipRequest setUserId(String userId) {
        this.userId = userId;
        return this;
    }
    public String getUserId() {
        return this.userId;
    }

}
