// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * List image address groups request
 */
public class ListImageAddressGroupsRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    // drive_id
    @NameInMap("drive_id")
    @Validation(required = true, pattern = "[0-9]+")
    public String driveId;

    // image_thumbnail_process
    @NameInMap("image_thumbnail_process")
    public String imageThumbnailProcess;

    // 每页大小限制
    @NameInMap("limit")
    @Validation(maximum = 100, minimum = 1)
    public Integer limit;

    // 翻页标记
    @NameInMap("marker")
    public String marker;

    // video_thumbnail_process
    @NameInMap("video_thumbnail_process")
    public String videoThumbnailProcess;

    public static ListImageAddressGroupsRequest build(java.util.Map<String, ?> map) throws Exception {
        ListImageAddressGroupsRequest self = new ListImageAddressGroupsRequest();
        return TeaModel.build(map, self);
    }

    public ListImageAddressGroupsRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
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

    public ListImageAddressGroupsRequest setVideoThumbnailProcess(String videoThumbnailProcess) {
        this.videoThumbnailProcess = videoThumbnailProcess;
        return this;
    }
    public String getVideoThumbnailProcess() {
        return this.videoThumbnailProcess;
    }

}
