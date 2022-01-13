// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class CreateSyncMappingResponse extends TeaModel {
    // drive_id
    @NameInMap("drive_id")
    public String driveId;

    // file_id
    @NameInMap("file_id")
    public String fileId;

    public static CreateSyncMappingResponse build(java.util.Map<String, ?> map) throws Exception {
        CreateSyncMappingResponse self = new CreateSyncMappingResponse();
        return TeaModel.build(map, self);
    }

    public CreateSyncMappingResponse setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public CreateSyncMappingResponse setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

}
