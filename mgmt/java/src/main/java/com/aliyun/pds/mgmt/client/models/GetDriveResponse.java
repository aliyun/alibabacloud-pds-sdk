// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * Get drive response
 */
public class GetDriveResponse extends TeaModel {
    @NameInMap("action_list")
    public java.util.List<String> actionList;

    @NameInMap("created_at")
    public String createdAt;

    // Drive 创建者
    @NameInMap("creator")
    public String creator;

    // Drive 备注信息
    @NameInMap("description")
    public String description;

    // Domain ID
    @NameInMap("domain_id")
    public String domainId;

    // Drive ID
    @NameInMap("drive_id")
    public String driveId;

    // Drive 名称
    @NameInMap("drive_name")
    public String driveName;

    // Drive 类型
    @NameInMap("drive_type")
    public String driveType;

    @NameInMap("encrypt_data_access")
    public Boolean encryptDataAccess;

    @NameInMap("encrypt_mode")
    public String encryptMode;

    // Drive 所有者
    @NameInMap("owner")
    public String owner;

    // Drive 所有者类型
    @NameInMap("owner_type")
    public String ownerType;

    @NameInMap("permission")
    public java.util.Map<String, ?> permission;

    // Drive存储基于store的相对路径，domain的PathType为OSSPath时返回
    @NameInMap("relative_path")
    public String relativePath;

    // Drive 状态
    @NameInMap("status")
    public String status;

    // 存储 ID, domain的PathType为OSSPath时返回
    @NameInMap("store_id")
    public String storeId;

    // subdomain_id
    @NameInMap("subdomain_id")
    public String subdomainId;

    // Drive 空间总量
    @NameInMap("total_size")
    public Long totalSize;

    // Drive 空间已使用量
    @NameInMap("used_size")
    public Long usedSize;

    public static GetDriveResponse build(java.util.Map<String, ?> map) throws Exception {
        GetDriveResponse self = new GetDriveResponse();
        return TeaModel.build(map, self);
    }

    public GetDriveResponse setActionList(java.util.List<String> actionList) {
        this.actionList = actionList;
        return this;
    }
    public java.util.List<String> getActionList() {
        return this.actionList;
    }

    public GetDriveResponse setCreatedAt(String createdAt) {
        this.createdAt = createdAt;
        return this;
    }
    public String getCreatedAt() {
        return this.createdAt;
    }

    public GetDriveResponse setCreator(String creator) {
        this.creator = creator;
        return this;
    }
    public String getCreator() {
        return this.creator;
    }

    public GetDriveResponse setDescription(String description) {
        this.description = description;
        return this;
    }
    public String getDescription() {
        return this.description;
    }

    public GetDriveResponse setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public GetDriveResponse setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public GetDriveResponse setDriveName(String driveName) {
        this.driveName = driveName;
        return this;
    }
    public String getDriveName() {
        return this.driveName;
    }

    public GetDriveResponse setDriveType(String driveType) {
        this.driveType = driveType;
        return this;
    }
    public String getDriveType() {
        return this.driveType;
    }

    public GetDriveResponse setEncryptDataAccess(Boolean encryptDataAccess) {
        this.encryptDataAccess = encryptDataAccess;
        return this;
    }
    public Boolean getEncryptDataAccess() {
        return this.encryptDataAccess;
    }

    public GetDriveResponse setEncryptMode(String encryptMode) {
        this.encryptMode = encryptMode;
        return this;
    }
    public String getEncryptMode() {
        return this.encryptMode;
    }

    public GetDriveResponse setOwner(String owner) {
        this.owner = owner;
        return this;
    }
    public String getOwner() {
        return this.owner;
    }

    public GetDriveResponse setOwnerType(String ownerType) {
        this.ownerType = ownerType;
        return this;
    }
    public String getOwnerType() {
        return this.ownerType;
    }

    public GetDriveResponse setPermission(java.util.Map<String, ?> permission) {
        this.permission = permission;
        return this;
    }
    public java.util.Map<String, ?> getPermission() {
        return this.permission;
    }

    public GetDriveResponse setRelativePath(String relativePath) {
        this.relativePath = relativePath;
        return this;
    }
    public String getRelativePath() {
        return this.relativePath;
    }

    public GetDriveResponse setStatus(String status) {
        this.status = status;
        return this;
    }
    public String getStatus() {
        return this.status;
    }

    public GetDriveResponse setStoreId(String storeId) {
        this.storeId = storeId;
        return this;
    }
    public String getStoreId() {
        return this.storeId;
    }

    public GetDriveResponse setSubdomainId(String subdomainId) {
        this.subdomainId = subdomainId;
        return this;
    }
    public String getSubdomainId() {
        return this.subdomainId;
    }

    public GetDriveResponse setTotalSize(Long totalSize) {
        this.totalSize = totalSize;
        return this;
    }
    public Long getTotalSize() {
        return this.totalSize;
    }

    public GetDriveResponse setUsedSize(Long usedSize) {
        this.usedSize = usedSize;
        return this;
    }
    public Long getUsedSize() {
        return this.usedSize;
    }

}
