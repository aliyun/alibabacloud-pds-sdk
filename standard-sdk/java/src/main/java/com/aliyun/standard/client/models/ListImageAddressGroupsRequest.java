// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.standard.client.models;

import com.aliyun.tea.*;

/**
 * List image address groups request
 */
public class ListImageAddressGroupsRequest extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // Drive ID
    @NameInMap("drive_id")
    @Validation(required = true)
    public String driveId;

    // image_thumbnail_process
type:string
    @NameInMap("image_thumbnail_process")
    public String imageThumbnailProcess;

    // 每页大小限制
    @NameInMap("limit")
    public Integer limit;

    // 翻页标记
    @NameInMap("marker")
    public String marker;

    public static ListImageAddressGroupsRequest build(java.util.Map<String, ?> map) throws Exception {
        ListImageAddressGroupsRequest self = new ListImageAddressGroupsRequest();
        return TeaModel.build(map, self);
    }

    public ListImageAddressGroupsRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ListImageAddressGroupsRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public ListImageAddressGroupsRequest setImageThumbnailProcess(String imageThumbnailProcess) {
        this.imageThumbnailProcess = imageThumbnailProcess;
        return this;
    }
    public String getImageThumbnailProcess() {
        return this.imageThumbnailProcess;
    }

    public ListImageAddressGroupsRequest setLimit(Integer limit) {
        this.limit = limit;
        return this;
    }
    public Integer getLimit() {
        return this.limit;
    }

    public ListImageAddressGroupsRequest setMarker(String marker) {
        this.marker = marker;
        return this;
    }
    public String getMarker() {
        return this.marker;
    }

}
