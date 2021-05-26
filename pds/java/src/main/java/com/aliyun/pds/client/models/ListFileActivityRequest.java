// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class ListFileActivityRequest extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // addition_data
    @NameInMap("addition_data")
    public java.util.Map<String, ?> additionData;

    // DriveID
    @NameInMap("drive_id")
    public String driveId;

    // FileID
    @NameInMap("file_id")
    public String fileId;

    // Limit, default
    @NameInMap("limit")
    public Integer limit;

    // Marker
    @NameInMap("marker")
    public String marker;

    public static ListFileActivityRequest build(java.util.Map<String, ?> map) throws Exception {
        ListFileActivityRequest self = new ListFileActivityRequest();
        return TeaModel.build(map, self);
    }

    public ListFileActivityRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
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
