// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class BaseGroupResponse extends TeaModel {
    // created_at
    @NameInMap("created_at")
    public Long createdAt;

    // description
    @NameInMap("description")
    public String description;

    // domain id
    @NameInMap("domain_id")
    public String domainId;

    // group id
    @NameInMap("group_id")
    public String groupId;

    // group name
    @NameInMap("group_name")
    public String groupName;

    @NameInMap("permission")
    public java.util.Map<String, ?> permission;

    // updated_at
    @NameInMap("updated_at")
    public Long updatedAt;

    public static BaseGroupResponse build(java.util.Map<String, ?> map) throws Exception {
        BaseGroupResponse self = new BaseGroupResponse();
        return TeaModel.build(map, self);
    }

    public BaseGroupResponse setCreatedAt(Long createdAt) {
        this.createdAt = createdAt;
        return this;
    }
    public Long getCreatedAt() {
        return this.createdAt;
    }

    public BaseGroupResponse setDescription(String description) {
        this.description = description;
        return this;
    }
    public String getDescription() {
        return this.description;
    }

    public BaseGroupResponse setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public BaseGroupResponse setGroupId(String groupId) {
        this.groupId = groupId;
        return this;
    }
    public String getGroupId() {
        return this.groupId;
    }

    public BaseGroupResponse setGroupName(String groupName) {
        this.groupName = groupName;
        return this;
    }
    public String getGroupName() {
        return this.groupName;
    }

    public BaseGroupResponse setPermission(java.util.Map<String, ?> permission) {
        this.permission = permission;
        return this;
    }
    public java.util.Map<String, ?> getPermission() {
        return this.permission;
    }

    public BaseGroupResponse setUpdatedAt(Long updatedAt) {
        this.updatedAt = updatedAt;
        return this;
    }
    public Long getUpdatedAt() {
        return this.updatedAt;
    }

}
