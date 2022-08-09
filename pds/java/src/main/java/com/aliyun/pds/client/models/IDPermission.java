// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 *
 */
public class IDPermission extends TeaModel {
    @NameInMap("ActionList")
    public java.util.List<ActionItem> ActionList;

    @NameInMap("Collection")
    public String Collection;

    @NameInMap("Condition")
    public Condition Condition;

    @NameInMap("CreatedAt")
    public Long CreatedAt;

    @NameInMap("Deleted")
    public String Deleted;

    @NameInMap("DisinheritSubGroup")
    public Boolean DisinheritSubGroup;

    @NameInMap("DomainID")
    public String DomainID;

    @NameInMap("Effect")
    public String Effect;

    @NameInMap("ExpireTime")
    public Long ExpireTime;

    @NameInMap("IdentityID")
    public String IdentityID;

    @NameInMap("IdentityType")
    public String IdentityType;

    @NameInMap("Resource")
    public String Resource;

    @NameInMap("ResourceType")
    public String ResourceType;

    @NameInMap("Roles")
    public java.util.List<String> Roles;

    @NameInMap("SequenceNumber")
    public Long SequenceNumber;

    @NameInMap("UpdatedAt")
    public Long UpdatedAt;

    @NameInMap("UpdatedBy")
    public String UpdatedBy;

    @NameInMap("UserTags")
    public java.util.List<String> UserTags;

    public static IDPermission build(java.util.Map<String, ?> map) throws Exception {
        IDPermission self = new IDPermission();
        return TeaModel.build(map, self);
    }

    public IDPermission setActionList(java.util.List<ActionItem> ActionList) {
        this.ActionList = ActionList;
        return this;
    }
    public java.util.List<ActionItem> getActionList() {
        return this.ActionList;
    }

    public IDPermission setCollection(String Collection) {
        this.Collection = Collection;
        return this;
    }
    public String getCollection() {
        return this.Collection;
    }

    public IDPermission setCondition(Condition Condition) {
        this.Condition = Condition;
        return this;
    }
    public Condition getCondition() {
        return this.Condition;
    }

    public IDPermission setCreatedAt(Long CreatedAt) {
        this.CreatedAt = CreatedAt;
        return this;
    }
    public Long getCreatedAt() {
        return this.CreatedAt;
    }

    public IDPermission setDeleted(String Deleted) {
        this.Deleted = Deleted;
        return this;
    }
    public String getDeleted() {
        return this.Deleted;
    }

    public IDPermission setDisinheritSubGroup(Boolean DisinheritSubGroup) {
        this.DisinheritSubGroup = DisinheritSubGroup;
        return this;
    }
    public Boolean getDisinheritSubGroup() {
        return this.DisinheritSubGroup;
    }

    public IDPermission setDomainID(String DomainID) {
        this.DomainID = DomainID;
        return this;
    }
    public String getDomainID() {
        return this.DomainID;
    }

    public IDPermission setEffect(String Effect) {
        this.Effect = Effect;
        return this;
    }
    public String getEffect() {
        return this.Effect;
    }

    public IDPermission setExpireTime(Long ExpireTime) {
        this.ExpireTime = ExpireTime;
        return this;
    }
    public Long getExpireTime() {
        return this.ExpireTime;
    }

    public IDPermission setIdentityID(String IdentityID) {
        this.IdentityID = IdentityID;
        return this;
    }
    public String getIdentityID() {
        return this.IdentityID;
    }

    public IDPermission setIdentityType(String IdentityType) {
        this.IdentityType = IdentityType;
        return this;
    }
    public String getIdentityType() {
        return this.IdentityType;
    }

    public IDPermission setResource(String Resource) {
        this.Resource = Resource;
        return this;
    }
    public String getResource() {
        return this.Resource;
    }

    public IDPermission setResourceType(String ResourceType) {
        this.ResourceType = ResourceType;
        return this;
    }
    public String getResourceType() {
        return this.ResourceType;
    }

    public IDPermission setRoles(java.util.List<String> Roles) {
        this.Roles = Roles;
        return this;
    }
    public java.util.List<String> getRoles() {
        return this.Roles;
    }

    public IDPermission setSequenceNumber(Long SequenceNumber) {
        this.SequenceNumber = SequenceNumber;
        return this;
    }
    public Long getSequenceNumber() {
        return this.SequenceNumber;
    }

    public IDPermission setUpdatedAt(Long UpdatedAt) {
        this.UpdatedAt = UpdatedAt;
        return this;
    }
    public Long getUpdatedAt() {
        return this.UpdatedAt;
    }

    public IDPermission setUpdatedBy(String UpdatedBy) {
        this.UpdatedBy = UpdatedBy;
        return this;
    }
    public String getUpdatedBy() {
        return this.UpdatedBy;
    }

    public IDPermission setUserTags(java.util.List<String> UserTags) {
        this.UserTags = UserTags;
        return this;
    }
    public java.util.List<String> getUserTags() {
        return this.UserTags;
    }

}
