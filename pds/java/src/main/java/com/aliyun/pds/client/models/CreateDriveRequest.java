// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * create drive request
 */
public class CreateDriveRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    // 是否默认drive, 只允许设置一个默认drive
    @NameInMap("default")
    public Boolean _default;

    // 描述信息
    @NameInMap("description")
    @Validation(maxLength = 1024)
    public String description;

    // Drive 名称
    @NameInMap("drive_name")
    @Validation(required = true, maxLength = 1024)
    public String driveName;

    // Drive类型
    @NameInMap("drive_type")
    public String driveType;

    @NameInMap("encrypt_mode")
    public String encryptMode;

    // location
    @NameInMap("location")
    public String location;

    // 所属者
    @NameInMap("owner")
    @Validation(required = true)
    public String owner;

    // 所属者
    @NameInMap("owner_type")
    @Validation(required = true)
    public String ownerType;

    // domain的PathType为OSSPath时必选。 Drive存储基于store的相对路径
    @NameInMap("relative_path")
    public String relativePath;

    // 状态
    @NameInMap("status")
    public String status;

    // StoreID , domain的PathType为OSSPath时必选
    @NameInMap("store_id")
    public String storeId;

    // Subdomain ID
    @NameInMap("subdomain_id")
    public String subdomainId;

    // 总大小,单位Byte [如果设置 -1 代表不限制]
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
