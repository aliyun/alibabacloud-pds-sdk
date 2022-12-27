// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class CreateSyncMappingRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    // addition_data
    @NameInMap("addition_data")
    public String additionData;

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

    // hidden
    @NameInMap("hidden")
    public Boolean hidden;

    // local_path
    @NameInMap("local_path")
    public String localPath;

    // name
    @NameInMap("name")
    public String name;

    // sync_mode
    @NameInMap("sync_mode")
    public String syncMode;

    public static CreateSyncMappingRequest build(java.util.Map<String, ?> map) throws Exception {
        CreateSyncMappingRequest self = new CreateSyncMappingRequest();
        return TeaModel.build(map, self);
    }

    public CreateSyncMappingRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public CreateSyncMappingRequest setAdditionData(String additionData) {
        this.additionData = additionData;
        return this;
    }
    public String getAdditionData() {
        return this.additionData;
    }

    public CreateSyncMappingRequest setCustomMeta(String customMeta) {
        this.customMeta = customMeta;
        return this;
    }
    public String getCustomMeta() {
        return this.customMeta;
    }

    public CreateSyncMappingRequest setDeviceName(String deviceName) {
        this.deviceName = deviceName;
        return this;
    }
    public String getDeviceName() {
        return this.deviceName;
    }

    public CreateSyncMappingRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public CreateSyncMappingRequest setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

    public CreateSyncMappingRequest setFsId(String fsId) {
        this.fsId = fsId;
        return this;
    }
    public String getFsId() {
        return this.fsId;
    }

    public CreateSyncMappingRequest setHidden(Boolean hidden) {
        this.hidden = hidden;
        return this;
    }
    public Boolean getHidden() {
        return this.hidden;
    }

    public CreateSyncMappingRequest setLocalPath(String localPath) {
        this.localPath = localPath;
        return this;
    }
    public String getLocalPath() {
        return this.localPath;
    }

    public CreateSyncMappingRequest setName(String name) {
        this.name = name;
        return this;
    }
    public String getName() {
        return this.name;
    }

    public CreateSyncMappingRequest setSyncMode(String syncMode) {
        this.syncMode = syncMode;
        return this;
    }
    public String getSyncMode() {
        return this.syncMode;
    }

}
