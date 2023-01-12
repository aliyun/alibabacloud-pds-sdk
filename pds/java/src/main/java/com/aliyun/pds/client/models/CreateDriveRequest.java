// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * create drive request
 */
public class CreateDriveRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    @NameInMap("category")
    public String category;

    /**
     * <p>是否默认drive, 只允许设置一个默认drive</p>
     */
    @NameInMap("default")
    public Boolean _default;

    /**
     * <p>描述信息</p>
     */
    @NameInMap("description")
    @Validation(maxLength = 1024)
    public String description;

    /**
     * <p>Drive 名称</p>
     */
    @NameInMap("drive_name")
    @Validation(required = true, maxLength = 1024)
    public String driveName;

    /**
     * <p>Drive类型</p>
     */
    @NameInMap("drive_type")
    public String driveType;

    @NameInMap("encrypt_mode")
    public String encryptMode;

    /**
     * <p>location</p>
     */
    @NameInMap("location")
    public String location;

    /**
     * <p>所属者</p>
     */
    @NameInMap("owner")
    @Validation(required = true)
    public String owner;

    /**
     * <p>所属者</p>
     */
    @NameInMap("owner_type")
    @Validation(required = true)
    public String ownerType;

    /**
     * <p>domain的PathType为OSSPath时必选。 Drive存储基于store的相对路径</p>
     */
    @NameInMap("relative_path")
    public String relativePath;

    /**
     * <p>状态</p>
     */
    @NameInMap("status")
    public String status;

    /**
     * <p>StoreID , domain的PathType为OSSPath时必选</p>
     */
    @NameInMap("store_id")
    public String storeId;

    /**
     * <p>Subdomain ID</p>
     */
    @NameInMap("subdomain_id")
    public String subdomainId;

    /**
     * <p>总大小,单位Byte [如果设置 -1 代表不限制]</p>
     */
    @NameInMap("total_size")
    public Long totalSize;

    public static CreateDriveRequest build(java.util.Map<String, ?> map) throws Exception {
        CreateDriveRequest self = new CreateDriveRequest();
        return TeaModel.build(map, self);
    }

    public CreateDriveRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public CreateDriveRequest setCategory(String category) {
        this.category = category;
        return this;
    }
    public String getCategory() {
        return this.category;
    }

    public CreateDriveRequest set_default(Boolean _default) {
        this._default = _default;
        return this;
    }
    public Boolean get_default() {
        return this._default;
    }

    public CreateDriveRequest setDescription(String description) {
        this.description = description;
        return this;
    }
    public String getDescription() {
        return this.description;
    }

    public CreateDriveRequest setDriveName(String driveName) {
        this.driveName = driveName;
        return this;
    }
    public String getDriveName() {
        return this.driveName;
    }

    public CreateDriveRequest setDriveType(String driveType) {
        this.driveType = driveType;
        return this;
    }
    public String getDriveType() {
        return this.driveType;
    }

    public CreateDriveRequest setEncryptMode(String encryptMode) {
        this.encryptMode = encryptMode;
        return this;
    }
    public String getEncryptMode() {
        return this.encryptMode;
    }

    public CreateDriveRequest setLocation(String location) {
        this.location = location;
        return this;
    }
    public String getLocation() {
        return this.location;
    }

    public CreateDriveRequest setOwner(String owner) {
        this.owner = owner;
        return this;
    }
    public String getOwner() {
        return this.owner;
    }

    public CreateDriveRequest setOwnerType(String ownerType) {
        this.ownerType = ownerType;
        return this;
    }
    public String getOwnerType() {
        return this.ownerType;
    }

    public CreateDriveRequest setRelativePath(String relativePath) {
        this.relativePath = relativePath;
        return this;
    }
    public String getRelativePath() {
        return this.relativePath;
    }

    public CreateDriveRequest setStatus(String status) {
        this.status = status;
        return this;
    }
    public String getStatus() {
        return this.status;
    }

    public CreateDriveRequest setStoreId(String storeId) {
        this.storeId = storeId;
        return this;
    }
    public String getStoreId() {
        return this.storeId;
    }

    public CreateDriveRequest setSubdomainId(String subdomainId) {
        this.subdomainId = subdomainId;
        return this;
    }
    public String getSubdomainId() {
        return this.subdomainId;
    }

    public CreateDriveRequest setTotalSize(Long totalSize) {
        this.totalSize = totalSize;
        return this;
    }
    public Long getTotalSize() {
        return this.totalSize;
    }

}
