// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * Update drive request
 */
public class UpdateDriveRequest extends TeaModel {
    // 描述信息
    @NameInMap("description")
    @Validation(maxLength = 1024)
    public String description;

    // Drive ID
    @NameInMap("drive_id")
    @Validation(required = true)
    public String driveId;

    // Drive 名称
    @NameInMap("drive_name")
    @Validation(maxLength = 1024)
    public String driveName;

    // 授权访问加密数据
    @NameInMap("encrypt_data_access")
    public Boolean encryptDataAccess;

    // 加密模式
    @NameInMap("encrypt_mode")
    public String encryptMode;

    // 状态
    @NameInMap("status")
    public String status;

    // Subdomain ID
    @NameInMap("subdomain_id")
    public String subdomainId;

    // 总大小,单位Byte [如果设置 -1 代表不限制]
    @NameInMap("total_size")
    public Long totalSize;

    public static UpdateDriveRequest build(java.util.Map<String, ?> map) throws Exception {
        UpdateDriveRequest self = new UpdateDriveRequest();
        return TeaModel.build(map, self);
    }

    public UpdateDriveRequest setDescription(String description) {
        this.description = description;
        return this;
    }
    public String getDescription() {
        return this.description;
    }

    public UpdateDriveRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public UpdateDriveRequest setDriveName(String driveName) {
        this.driveName = driveName;
        return this;
    }
    public String getDriveName() {
        return this.driveName;
    }

    public UpdateDriveRequest setEncryptDataAccess(Boolean encryptDataAccess) {
        this.encryptDataAccess = encryptDataAccess;
        return this;
    }
    public Boolean getEncryptDataAccess() {
        return this.encryptDataAccess;
    }

    public UpdateDriveRequest setEncryptMode(String encryptMode) {
        this.encryptMode = encryptMode;
        return this;
    }
    public String getEncryptMode() {
        return this.encryptMode;
    }

    public UpdateDriveRequest setStatus(String status) {
        this.status = status;
        return this;
    }
    public String getStatus() {
        return this.status;
    }

    public UpdateDriveRequest setSubdomainId(String subdomainId) {
        this.subdomainId = subdomainId;
        return this;
    }
    public String getSubdomainId() {
        return this.subdomainId;
    }

    public UpdateDriveRequest setTotalSize(Long totalSize) {
        this.totalSize = totalSize;
        return this;
    }
    public Long getTotalSize() {
        return this.totalSize;
    }

}
