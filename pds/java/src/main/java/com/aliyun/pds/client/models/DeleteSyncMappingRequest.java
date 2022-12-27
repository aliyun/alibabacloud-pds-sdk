// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class DeleteSyncMappingRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    @NameInMap("Mode")
    public String Mode;

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
     * <p>fs_id</p>
     */
    @NameInMap("fs_id")
    public String fsId;

    /**
     * <p>local_path</p>
     */
    @NameInMap("local_path")
    public String localPath;

    public static DeleteSyncMappingRequest build(java.util.Map<String, ?> map) throws Exception {
        DeleteSyncMappingRequest self = new DeleteSyncMappingRequest();
        return TeaModel.build(map, self);
    }

    public DeleteSyncMappingRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public DeleteSyncMappingRequest setMode(String Mode) {
        this.Mode = Mode;
        return this;
    }
    public String getMode() {
        return this.Mode;
    }

    public DeleteSyncMappingRequest setDeviceName(String deviceName) {
        this.deviceName = deviceName;
        return this;
    }
    public String getDeviceName() {
        return this.deviceName;
    }

    public DeleteSyncMappingRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public DeleteSyncMappingRequest setFsId(String fsId) {
        this.fsId = fsId;
        return this;
    }
    public String getFsId() {
        return this.fsId;
    }

    public DeleteSyncMappingRequest setLocalPath(String localPath) {
        this.localPath = localPath;
        return this;
    }
    public String getLocalPath() {
        return this.localPath;
    }

}
