// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 *
 */
public class SyncMappingItem extends TeaModel {
    // created_at
    @NameInMap("created_at")
    public String createdAt;

    // custom_meta
    @NameInMap("custom_meta")
    public String customMeta;

    // device_name
    @NameInMap("device_name")
    public String deviceName;

    // drive_id
    @NameInMap("drive_id")
    public String driveId;

    // file_id
    @NameInMap("file_id")
    public String fileId;

    // fs_id
    @NameInMap("fs_id")
    public String fsId;

    // local_path
    @NameInMap("local_path")
    public String localPath;

    // sync_mode
    @NameInMap("sync_mode")
    public String syncMode;

    // updated_at
    @NameInMap("updated_at")
    public String updatedAt;

    public static SyncMappingItem build(java.util.Map<String, ?> map) throws Exception {
        SyncMappingItem self = new SyncMappingItem();
        return TeaModel.build(map, self);
    }

    public SyncMappingItem setCreatedAt(String createdAt) {
        this.createdAt = createdAt;
        return this;
    }
    public String getCreatedAt() {
        return this.createdAt;
    }

    public SyncMappingItem setCustomMeta(String customMeta) {
        this.customMeta = customMeta;
        return this;
    }
    public String getCustomMeta() {
        return this.customMeta;
    }

    public SyncMappingItem setDeviceName(String deviceName) {
        this.deviceName = deviceName;
        return this;
    }
    public String getDeviceName() {
        return this.deviceName;
    }

    public SyncMappingItem setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public SyncMappingItem setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

    public SyncMappingItem setFsId(String fsId) {
        this.fsId = fsId;
        return this;
    }
    public String getFsId() {
        return this.fsId;
    }

    public SyncMappingItem setLocalPath(String localPath) {
        this.localPath = localPath;
        return this;
    }
    public String getLocalPath() {
        return this.localPath;
    }

    public SyncMappingItem setSyncMode(String syncMode) {
        this.syncMode = syncMode;
        return this;
    }
    public String getSyncMode() {
        return this.syncMode;
    }

    public SyncMappingItem setUpdatedAt(String updatedAt) {
        this.updatedAt = updatedAt;
        return this;
    }
    public String getUpdatedAt() {
        return this.updatedAt;
    }

}
