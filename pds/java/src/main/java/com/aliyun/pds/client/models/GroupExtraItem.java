// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class GroupExtraItem extends TeaModel {
    // created_at
    @NameInMap("created_at")
    public Long createdAt;

    // creator
    @NameInMap("creator")
    public String creator;

    // description
    @NameInMap("description")
    public String description;

    // domain id
    @NameInMap("domain_id")
    public String domainId;

    @NameInMap("drive_list")
    public java.util.List<BaseDriveResponse> driveList;

    // group id
    @NameInMap("group_id")
    public String groupId;

    // group name
    @NameInMap("group_name")
    public String groupName;

    @NameInMap("is_sync")
    public Boolean isSync;

    @NameInMap("permission")
    public java.util.Map<String, ?> permission;

    // updated_at
    @NameInMap("updated_at")
    public Long updatedAt;

    public static GroupExtraItem build(java.util.Map<String, ?> map) throws Exception {
        GroupExtraItem self = new GroupExtraItem();
        return TeaModel.build(map, self);
    }

    public GroupExtraItem setCreatedAt(Long createdAt) {
        this.createdAt = createdAt;
        return this;
    }
    public Long getCreatedAt() {
        return this.createdAt;
    }

    public GroupExtraItem setCreator(String creator) {
        this.creator = creator;
        return this;
    }
    public String getCreator() {
        return this.creator;
    }

    public GroupExtraItem setDescription(String description) {
        this.description = description;
        return this;
    }
    public String getDescription() {
        return this.description;
    }

    public GroupExtraItem setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public GroupExtraItem setDriveList(java.util.List<BaseDriveResponse> driveList) {
        this.driveList = driveList;
        return this;
    }
    public java.util.List<BaseDriveResponse> getDriveList() {
        return this.driveList;
    }

    public GroupExtraItem setGroupId(String groupId) {
        this.groupId = groupId;
        return this;
    }
    public String getGroupId() {
        return this.groupId;
    }

    public GroupExtraItem setGroupName(String groupName) {
        this.groupName = groupName;
        return this;
    }
    public String getGroupName() {
        return this.groupName;
    }

    public GroupExtraItem setIsSync(Boolean isSync) {
        this.isSync = isSync;
        return this;
    }
    public Boolean getIsSync() {
        return this.isSync;
    }

    public GroupExtraItem setPermission(java.util.Map<String, ?> permission) {
        this.permission = permission;
        return this;
    }
    public java.util.Map<String, ?> getPermission() {
        return this.permission;
    }

    public GroupExtraItem setUpdatedAt(Long updatedAt) {
        this.updatedAt = updatedAt;
        return this;
    }
    public Long getUpdatedAt() {
        return this.updatedAt;
    }

}
