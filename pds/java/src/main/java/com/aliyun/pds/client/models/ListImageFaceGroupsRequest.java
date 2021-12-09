// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * List image face groups request
 */
public class ListImageFaceGroupsRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    // drive_id
    @NameInMap("drive_id")
    @Validation(required = true, pattern = "[0-9]+")
    public String driveId;

    // 每页大小限制
    @NameInMap("limit")
    public Long limit;

    // 翻页标记
    @NameInMap("marker")
    public String marker;

    @NameInMap("remarks_array_query")
    public RemarksQueryRequest remarksArrayQuery;

    @NameInMap("remarks_query")
    public RemarksQueryRequest remarksQuery;

    public static ListImageFaceGroupsRequest build(java.util.Map<String, ?> map) throws Exception {
        ListImageFaceGroupsRequest self = new ListImageFaceGroupsRequest();
        return TeaModel.build(map, self);
    }

    public ListImageFaceGroupsRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
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

    public ListImageFaceGroupsRequest setRemarksArrayQuery(RemarksQueryRequest remarksArrayQuery) {
        this.remarksArrayQuery = remarksArrayQuery;
        return this;
    }
    public RemarksQueryRequest getRemarksArrayQuery() {
        return this.remarksArrayQuery;
    }

    public ListImageFaceGroupsRequest setRemarksQuery(RemarksQueryRequest remarksQuery) {
        this.remarksQuery = remarksQuery;
        return this;
    }
    public RemarksQueryRequest getRemarksQuery() {
        return this.remarksQuery;
    }

}
