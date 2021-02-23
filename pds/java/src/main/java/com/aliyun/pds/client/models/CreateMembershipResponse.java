// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class CreateMembershipResponse extends TeaModel {
    // created_at
    @NameInMap("created_at")
    public Long createdAt;

    // 描述
    @NameInMap("description")
    public String description;

    // domain id
    @NameInMap("domain_id")
    public String domainId;

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

    // updated_at
    @NameInMap("updated_at")
    public Long updatedAt;

    @NameInMap("user_id")
    public String userId;

    public static CreateMembershipResponse build(java.util.Map<String, ?> map) throws Exception {
        CreateMembershipResponse self = new CreateMembershipResponse();
        return TeaModel.build(map, self);
    }

    public CreateMembershipResponse setCreatedAt(Long createdAt) {
        this.createdAt = createdAt;
        return this;
    }
    public Long getCreatedAt() {
        return this.createdAt;
    }

    public CreateMembershipResponse setDescription(String description) {
        this.description = description;
        return this;
    }
    public String getDescription() {
        return this.description;
    }

    public CreateMembershipResponse setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public CreateMembershipResponse setGroupId(String groupId) {
        this.groupId = groupId;
        return this;
    }
    public String getGroupId() {
        return this.groupId;
    }

    public CreateMembershipResponse setMemberRole(String memberRole) {
        this.memberRole = memberRole;
        return this;
    }
    public String getMemberRole() {
        return this.memberRole;
    }

    public CreateMembershipResponse setMemberType(String memberType) {
        this.memberType = memberType;
        return this;
    }
    public String getMemberType() {
        return this.memberType;
    }

    public CreateMembershipResponse setSubGroupId(String subGroupId) {
        this.subGroupId = subGroupId;
        return this;
    }
    public String getSubGroupId() {
        return this.subGroupId;
    }

    public CreateMembershipResponse setUpdatedAt(Long updatedAt) {
        this.updatedAt = updatedAt;
        return this;
    }
    public Long getUpdatedAt() {
        return this.updatedAt;
    }

    public CreateMembershipResponse setUserId(String userId) {
        this.userId = userId;
        return this;
    }
    public String getUserId() {
        return this.userId;
    }

}
