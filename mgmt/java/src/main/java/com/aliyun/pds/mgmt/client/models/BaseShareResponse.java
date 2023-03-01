// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * List share response
 */
public class BaseShareResponse extends TeaModel {
    /**
     * <p>created_at</p>
     */
    @NameInMap("created_at")
    public String createdAt;

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
     * <p>domain_id</p>
     */
    @NameInMap("domain_id")
    public String domainId;

    /**
     * <p>drive_id</p>
     */
    @NameInMap("drive_id")
    public String driveId;

    /**
     * <p>expiration</p>
     */
    @NameInMap("expiration")
    public String expiration;

    /**
     * <p>expired</p>
     */
    @NameInMap("expired")
    public Boolean expired;

    /**
     * <p>owner</p>
     */
    @NameInMap("owner")
    public String owner;

    /**
     * <p>owner</p>
     */
    @NameInMap("owner_type")
    public String ownerType;

    /**
     * <p>permissions</p>
     */
    @NameInMap("permissions")
    public java.util.List<String> permissions;

    /**
     * <p>share_file_id</p>
     */
    @NameInMap("share_file_id")
    public String shareFileId;

    /**
     * <p>share_path</p>
     */
    @NameInMap("share_file_path")
    public String shareFilePath;

    /**
     * <p>share_id</p>
     */
    @NameInMap("share_id")
    public String shareId;

    /**
     * <p>share_name</p>
     */
    @NameInMap("share_name")
    public String shareName;

    @NameInMap("share_policy")
    public java.util.List<SharePermissionPolicy> sharePolicy;

    /**
     * <p>status</p>
     */
    @NameInMap("status")
    public String status;

    /**
     * <p>updated_at</p>
     */
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
