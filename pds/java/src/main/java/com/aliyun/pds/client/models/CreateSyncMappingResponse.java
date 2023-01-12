// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class CreateSyncMappingResponse extends TeaModel {
    /**
     * <p>drive_id</p>
     */
    @NameInMap("drive_id")
    public String driveId;

    /**
     * <p>exist</p>
     */
    @NameInMap("exist")
    public Boolean exist;

    /**
     * <p>file_id</p>
     */
    @NameInMap("file_id")
    public String fileId;

    /**
     * <p>name string</p>
     */
    @NameInMap("name")
    public String name;

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

    public CreateSyncMappingResponse setExist(Boolean exist) {
        this.exist = exist;
        return this;
    }
    public Boolean getExist() {
        return this.exist;
    }

    public CreateSyncMappingResponse setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

    public CreateSyncMappingResponse setName(String name) {
        this.name = name;
        return this;
    }
    public String getName() {
        return this.name;
    }

}
