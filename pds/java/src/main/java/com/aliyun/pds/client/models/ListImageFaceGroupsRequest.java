// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * List image face groups request
 */
public class ListImageFaceGroupsRequest extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // Drive ID
    @NameInMap("drive_id")
    @Validation(required = true)
    public String driveId;

    // 每页大小限制
    @NameInMap("limit")
    @Validation(maximum = 100, minimum = 1)
    public Long limit;

    // 翻页标记
    @NameInMap("marker")
    public String marker;

    public static ListImageFaceGroupsRequest build(java.util.Map<String, ?> map) throws Exception {
        ListImageFaceGroupsRequest self = new ListImageFaceGroupsRequest();
        return TeaModel.build(map, self);
    }

    public ListImageFaceGroupsRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ListImageFaceGroupsRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public ListImageFaceGroupsRequest setLimit(Long limit) {
        this.limit = limit;
        return this;
    }
    public Long getLimit() {
        return this.limit;
    }

    public ListImageFaceGroupsRequest setMarker(String marker) {
        this.marker = marker;
        return this;
    }
    public String getMarker() {
        return this.marker;
    }

}
