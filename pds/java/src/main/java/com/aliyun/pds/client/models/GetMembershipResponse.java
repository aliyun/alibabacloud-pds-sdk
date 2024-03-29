// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class GetMembershipResponse extends TeaModel {
    /**
     * <p>created_at</p>
     */
    @NameInMap("created_at")
    public Long createdAt;

    /**
     * <p>creator</p>
     */
    @NameInMap("creator")
    public String creator;

    /**
     * <p>描述</p>
     */
    @NameInMap("description")
    public String description;

    /**
     * <p>domain id</p>
     */
    @NameInMap("domain_id")
    public String domainId;

    /**
     * <p>group id</p>
     */
    @NameInMap("group_id")
    public String groupId;

    @NameInMap("is_sync")
    public Boolean isSync;

    /**
     * <p>角色， member or admin</p>
     */
    @NameInMap("member_role")
    public String memberRole;

    @NameInMap("member_type")
    public String memberType;

    @NameInMap("sub_group_id")
    public String subGroupId;

    /**
     * <p>updated_at</p>
     */
    @NameInMap("updated_at")
    public Long updatedAt;

    @NameInMap("user_id")
    public String userId;

    public static GetMembershipResponse build(java.util.Map<String, ?> map) throws Exception {
        GetMembershipResponse self = new GetMembershipResponse();
        return TeaModel.build(map, self);
    }

    public GetMembershipResponse setCreatedAt(Long createdAt) {
        this.createdAt = createdAt;
        return this;
    }
    public Long getCreatedAt() {
        return this.createdAt;
    }

    public GetMembershipResponse setCreator(String creator) {
        this.creator = creator;
        return this;
    }
    public String getCreator() {
        return this.creator;
    }

    public GetMembershipResponse setDescription(String description) {
        this.description = description;
        return this;
    }
    public String getDescription() {
        return this.description;
    }

    public GetMembershipResponse setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public GetMembershipResponse setGroupId(String groupId) {
        this.groupId = groupId;
        return this;
    }
    public String getGroupId() {
        return this.groupId;
    }

    public GetMembershipResponse setIsSync(Boolean isSync) {
        this.isSync = isSync;
        return this;
    }
    public Boolean getIsSync() {
        return this.isSync;
    }

    public GetMembershipResponse setMemberRole(String memberRole) {
        this.memberRole = memberRole;
        return this;
    }
    public String getMemberRole() {
        return this.memberRole;
    }

    public GetMembershipResponse setMemberType(String memberType) {
        this.memberType = memberType;
        return this;
    }
    public String getMemberType() {
        return this.memberType;
    }

    public GetMembershipResponse setSubGroupId(String subGroupId) {
        this.subGroupId = subGroupId;
        return this;
    }
    public String getSubGroupId() {
        return this.subGroupId;
    }

    public GetMembershipResponse setUpdatedAt(Long updatedAt) {
        this.updatedAt = updatedAt;
        return this;
    }
    public Long getUpdatedAt() {
        return this.updatedAt;
    }

    public GetMembershipResponse setUserId(String userId) {
        this.userId = userId;
        return this;
    }
    public String getUserId() {
        return this.userId;
    }

}
