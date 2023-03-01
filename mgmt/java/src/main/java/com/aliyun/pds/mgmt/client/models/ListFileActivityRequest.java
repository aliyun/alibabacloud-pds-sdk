// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class ListFileActivityRequest extends TeaModel {
    /**
     * <p>addition_data</p>
     */
    @NameInMap("addition_data")
    public java.util.Map<String, ?> additionData;

    /**
     * <p>DriveID</p>
     */
    @NameInMap("drive_id")
    public String driveId;

    /**
     * <p>FileID</p>
     */
    @NameInMap("file_id")
    public String fileId;

    /**
     * <p>Limit, default</p>
     */
    @NameInMap("limit")
    public Integer limit;

    /**
     * <p>Marker</p>
     */
    @NameInMap("marker")
    public String marker;

    public static ListFileActivityRequest build(java.util.Map<String, ?> map) throws Exception {
        ListFileActivityRequest self = new ListFileActivityRequest();
        return TeaModel.build(map, self);
    }

    public ListFileActivityRequest setAdditionData(java.util.Map<String, ?> additionData) {
        this.additionData = additionData;
        return this;
    }
    public java.util.Map<String, ?> getAdditionData() {
        return this.additionData;
    }

    public ListFileActivityRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public ListFileActivityRequest setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

    public ListFileActivityRequest setLimit(Integer limit) {
        this.limit = limit;
        return this;
    }
    public Integer getLimit() {
        return this.limit;
    }

    public ListFileActivityRequest setMarker(String marker) {
        this.marker = marker;
        return this;
    }
    public String getMarker() {
        return this.marker;
    }

}
