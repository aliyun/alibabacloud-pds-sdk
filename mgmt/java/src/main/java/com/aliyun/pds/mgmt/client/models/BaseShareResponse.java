// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * List share response
 */
public class BaseShareResponse extends TeaModel {
    // created_at
    @NameInMap("created_at")
    public String createdAt;

    // creator
    @NameInMap("creator")
    public String creator;

    // description
    @NameInMap("description")
    public String description;

    // domain_id
    @NameInMap("domain_id")
    public String domainId;

    // drive_id
    @NameInMap("drive_id")
    public String driveId;

    // expiration
    @NameInMap("expiration")
    public String expiration;

    // expired
    @NameInMap("expired")
    public Boolean expired;

    // owner
    @NameInMap("owner")
    public String owner;

    // owner
    @NameInMap("owner_type")
    public String ownerType;

    // permissions
    @NameInMap("permissions")
    public java.util.List<String> permissions;

    // share_file_id
    @NameInMap("share_file_id")
    public String shareFileId;

    // share_path
    @NameInMap("share_file_path")
    public String shareFilePath;

    // share_id
    @NameInMap("share_id")
    public String shareId;

    // share_name
    @NameInMap("share_name")
    public String shareName;

    @NameInMap("share_policy")
    public java.util.List<SharePermissionPolicy> sharePolicy;

    // status
    @NameInMap("status")
    public String status;

    // updated_at
    @NameInMap("updated_at")
    public String updatedAt;

    public static BaseShareResponse build(java.util.Map<String, ?> map) throws Exception {
        BaseShareResponse self = new BaseShareResponse();
        return TeaModel.build(map, self);
    }

    public BaseShareResponse setCreatedAt(String createdAt) {
        this.createdAt = createdAt;
        return this;
    }
    public String getCreatedAt() {
        return this.createdAt;
    }

    public BaseShareResponse setCreator(String creator) {
        this.creator = creator;
        return this;
    }
    public String getCreator() {
        return this.creator;
    }

    public BaseShareResponse setDescription(String description) {
        this.description = description;
        return this;
    }
    public String getDescription() {
        return this.description;
    }

    public BaseShareResponse setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public BaseShareResponse setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public BaseShareResponse setExpiration(String expiration) {
        this.expiration = expiration;
        return this;
    }
    public String getExpiration() {
        return this.expiration;
    }

    public BaseShareResponse setExpired(Boolean expired) {
        this.expired = expired;
        return this;
    }
    public Boolean getExpired() {
        return this.expired;
    }

    public BaseShareResponse setOwner(String owner) {
        this.owner = owner;
        return this;
    }
    public String getOwner() {
        return this.owner;
    }

    public BaseShareResponse setOwnerType(String ownerType) {
        this.ownerType = ownerType;
        return this;
    }
    public String getOwnerType() {
        return this.ownerType;
    }

    public BaseShareResponse setPermissions(java.util.List<String> permissions) {
        this.permissions = permissions;
        return this;
    }
    public java.util.List<String> getPermissions() {
        return this.permissions;
    }

    public BaseShareResponse setShareFileId(String shareFileId) {
        this.shareFileId = shareFileId;
        return this;
    }
    public String getShareFileId() {
        return this.shareFileId;
    }

    public BaseShareResponse setShareFilePath(String shareFilePath) {
        this.shareFilePath = shareFilePath;
        return this;
    }
    public String getShareFilePath() {
        return this.shareFilePath;
    }

    public BaseShareResponse setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

    public BaseShareResponse setShareName(String shareName) {
        this.shareName = shareName;
        return this;
    }
    public String getShareName() {
        return this.shareName;
    }

    public BaseShareResponse setSharePolicy(java.util.List<SharePermissionPolicy> sharePolicy) {
        this.sharePolicy = sharePolicy;
        return this;
    }
    public java.util.List<SharePermissionPolicy> getSharePolicy() {
        return this.sharePolicy;
    }

    public BaseShareResponse setStatus(String status) {
        this.status = status;
        return this;
    }
    public String getStatus() {
        return this.status;
    }

    public BaseShareResponse setUpdatedAt(String updatedAt) {
        this.updatedAt = updatedAt;
        return this;
    }
    public String getUpdatedAt() {
        return this.updatedAt;
    }

}
