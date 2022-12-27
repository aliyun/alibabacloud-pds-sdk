// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class GetGroupResponse extends TeaModel {
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
     * <p>description</p>
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

    /**
     * <p>group name</p>
     */
    @NameInMap("group_name")
    public String groupName;

    @NameInMap("is_sync")
    public Boolean isSync;

    @NameInMap("permission")
    public java.util.Map<String, ?> permission;

    /**
     * <p>updated_at</p>
     */
    @NameInMap("updated_at")
    public Long updatedAt;

    public static GetGroupResponse build(java.util.Map<String, ?> map) throws Exception {
        GetGroupResponse self = new GetGroupResponse();
        return TeaModel.build(map, self);
    }

    public GetGroupResponse setCreatedAt(Long createdAt) {
        this.createdAt = createdAt;
        return this;
    }
    public Long getCreatedAt() {
        return this.createdAt;
    }

    public GetGroupResponse setCreator(String creator) {
        this.creator = creator;
        return this;
    }
    public String getCreator() {
        return this.creator;
    }

    public GetGroupResponse setDescription(String description) {
        this.description = description;
        return this;
    }
    public String getDescription() {
        return this.description;
    }

    public GetGroupResponse setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public GetGroupResponse setGroupId(String groupId) {
        this.groupId = groupId;
        return this;
    }
    public String getGroupId() {
        return this.groupId;
    }

    public GetGroupResponse setGroupName(String groupName) {
        this.groupName = groupName;
        return this;
    }
    public String getGroupName() {
        return this.groupName;
    }

    public GetGroupResponse setIsSync(Boolean isSync) {
        this.isSync = isSync;
        return this;
    }
    public Boolean getIsSync() {
        return this.isSync;
    }

    public GetGroupResponse setPermission(java.util.Map<String, ?> permission) {
        this.permission = permission;
        return this;
    }
    public java.util.Map<String, ?> getPermission() {
        return this.permission;
    }

    public GetGroupResponse setUpdatedAt(Long updatedAt) {
        this.updatedAt = updatedAt;
        return this;
    }
    public Long getUpdatedAt() {
        return this.updatedAt;
    }

}
