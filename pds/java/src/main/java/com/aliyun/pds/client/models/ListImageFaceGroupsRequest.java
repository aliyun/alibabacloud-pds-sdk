// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * # List image face groups request
 */
public class ListImageFaceGroupsRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    /**
     * <p>drive_id</p>
     */
    @NameInMap("drive_id")
    @Validation(required = true, pattern = "[0-9]+")
    public String driveId;

    /**
     * <p>每页大小限制</p>
     */
    @NameInMap("limit")
    @Validation(maximum = 100, minimum = 1)
    public Long limit;

    /**
     * <p>翻页标记</p>
     */
    @NameInMap("marker")
    public String marker;

    @NameInMap("remarks")
    public String remarks;

    /**
     * <p>ReturnTotalCount 是否返回人脸分组总数</p>
     */
    @NameInMap("return_total_count")
    public Boolean returnTotalCount;

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

    public ListImageFaceGroupsRequest setRemarks(String remarks) {
        this.remarks = remarks;
        return this;
    }
    public String getRemarks() {
        return this.remarks;
    }

    public ListImageFaceGroupsRequest setReturnTotalCount(Boolean returnTotalCount) {
        this.returnTotalCount = returnTotalCount;
        return this;
    }
    public Boolean getReturnTotalCount() {
        return this.returnTotalCount;
    }

}
