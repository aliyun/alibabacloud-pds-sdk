// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class Permission extends TeaModel {
    @NameInMap("ActionList")
    public java.util.List<ActionItem> ActionList;

    @NameInMap("CreatedAt")
    public Long CreatedAt;

    @NameInMap("Deleted")
    public String Deleted;

    @NameInMap("DomainID")
    public String DomainID;

    @NameInMap("IdentityID")
    public String IdentityID;

    @NameInMap("IdentityType")
    public String IdentityType;

    @NameInMap("Resource")
    public String Resource;

    @NameInMap("ResourceType")
    public String ResourceType;

    @NameInMap("SequenceNumber")
    public Long SequenceNumber;

    @NameInMap("UpdatedAt")
    public Long UpdatedAt;

    @NameInMap("UpdatedBy")
    public String UpdatedBy;

    public static Permission build(java.util.Map<String, ?> map) throws Exception {
        Permission self = new Permission();
        return TeaModel.build(map, self);
    }

    public Permission setActionList(java.util.List<ActionItem> ActionList) {
        this.ActionList = ActionList;
        return this;
    }
    public java.util.List<ActionItem> getActionList() {
        return this.ActionList;
    }

    public Permission setCreatedAt(Long CreatedAt) {
        this.CreatedAt = CreatedAt;
        return this;
    }
    public Long getCreatedAt() {
        return this.CreatedAt;
    }

    public Permission setDeleted(String Deleted) {
        this.Deleted = Deleted;
        return this;
    }
    public String getDeleted() {
        return this.Deleted;
    }

    public Permission setDomainID(String DomainID) {
        this.DomainID = DomainID;
        return this;
    }
    public String getDomainID() {
        return this.DomainID;
    }

    public Permission setIdentityID(String IdentityID) {
        this.IdentityID = IdentityID;
        return this;
    }
    public String getIdentityID() {
        return this.IdentityID;
    }

    public Permission setIdentityType(String IdentityType) {
        this.IdentityType = IdentityType;
        return this;
    }
    public String getIdentityType() {
        return this.IdentityType;
    }

    public Permission setResource(String Resource) {
        this.Resource = Resource;
        return this;
    }
    public String getResource() {
        return this.Resource;
    }

    public Permission setResourceType(String ResourceType) {
        this.ResourceType = ResourceType;
        return this;
    }
    public String getResourceType() {
        return this.ResourceType;
    }

    public Permission setSequenceNumber(Long SequenceNumber) {
        this.SequenceNumber = SequenceNumber;
        return this;
    }
    public Long getSequenceNumber() {
        return this.SequenceNumber;
    }

    public Permission setUpdatedAt(Long UpdatedAt) {
        this.UpdatedAt = UpdatedAt;
        return this;
    }
    public Long getUpdatedAt() {
        return this.UpdatedAt;
    }

    public Permission setUpdatedBy(String UpdatedBy) {
        this.UpdatedBy = UpdatedBy;
        return this;
    }
    public String getUpdatedBy() {
        return this.UpdatedBy;
    }

}
