// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class UpdateMembershipRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

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

    // subdomain id
    @NameInMap("subdomain_id")
    public String subdomainId;

    @NameInMap("user_id")
    public String userId;

    public static UpdateMembershipRequest build(java.util.Map<String, ?> map) throws Exception {
        UpdateMembershipRequest self = new UpdateMembershipRequest();
        return TeaModel.build(map, self);
    }

    public UpdateMembershipRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public UpdateMembershipRequest setDescription(String description) {
        this.description = description;
        return this;
    }
    public String getDescription() {
        return this.description;
    }

    public UpdateMembershipRequest setGroupId(String groupId) {
        this.groupId = groupId;
        return this;
    }
    public String getGroupId() {
        return this.groupId;
    }

    public UpdateMembershipRequest setMemberRole(String memberRole) {
        this.memberRole = memberRole;
        return this;
    }
    public String getMemberRole() {
        return this.memberRole;
    }

    public UpdateMembershipRequest setMemberType(String memberType) {
        this.memberType = memberType;
        return this;
    }
    public String getMemberType() {
        return this.memberType;
    }

    public UpdateMembershipRequest setSubGroupId(String subGroupId) {
        this.subGroupId = subGroupId;
        return this;
    }
    public String getSubGroupId() {
        return this.subGroupId;
    }

    public UpdateMembershipRequest setSubdomainId(String subdomainId) {
        this.subdomainId = subdomainId;
        return this;
    }
    public String getSubdomainId() {
        return this.subdomainId;
    }

    public UpdateMembershipRequest setUserId(String userId) {
        this.userId = userId;
        return this;
    }
    public String getUserId() {
        return this.userId;
    }

}
