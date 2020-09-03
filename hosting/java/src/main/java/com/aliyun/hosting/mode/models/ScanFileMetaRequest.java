// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

/**
 * 全量获取file元信息的请求body
 */
public class ScanFileMetaRequest extends TeaModel {
    // category
    @NameInMap("category")
    public String category;

    // drive_id
    @NameInMap("drive_id")
    @Validation(required = true, pattern = "[0-9]+")
    public String driveId;

    // limit
    @NameInMap("limit")
    public Integer limit;

    // marker
    @NameInMap("marker")
    public String marker;

    public static ScanFileMetaRequest build(java.util.Map<String, ?> map) throws Exception {
        ScanFileMetaRequest self = new ScanFileMetaRequest();
        return TeaModel.build(map, self);
    }

    public ScanFileMetaRequest setCategory(String category) {
        this.category = category;
        return this;
    }
    public String getCategory() {
        return this.category;
    }

    public ScanFileMetaRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public ScanFileMetaRequest setLimit(Integer limit) {
        this.limit = limit;
        return this;
    }
    public Integer getLimit() {
        return this.limit;
    }

    public ScanFileMetaRequest setMarker(String marker) {
        this.marker = marker;
        return this;
    }
    public String getMarker() {
        return this.marker;
    }

}
