// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class CreateSyncMappingRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    /**
     * <p>addition_data</p>
     */
    @NameInMap("addition_data")
    public String additionData;

    /**
     * <p>custom_meta</p>
     */
    @NameInMap("custom_meta")
    public String customMeta;

    /**
     * <p>device_name</p>
     */
    @NameInMap("device_name")
    public String deviceName;

    /**
     * <p>drive_id</p>
     */
    @NameInMap("drive_id")
    public String driveId;

    /**
     * <p>file_id</p>
     */
    @NameInMap("file_id")
    public String fileId;

    /**
     * <p>fs_id</p>
     */
    @NameInMap("fs_id")
    public String fsId;

    /**
     * <p>hidden</p>
     */
    @NameInMap("hidden")
    public Boolean hidden;

    /**
     * <p>local_path</p>
     */
    @NameInMap("local_path")
    public String localPath;

    /**
     * <p>name</p>
     */
    @NameInMap("name")
    public String name;

    /**
     * <p>sync_mode</p>
     */
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
