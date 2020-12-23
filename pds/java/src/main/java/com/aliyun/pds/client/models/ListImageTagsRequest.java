// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * List image tags request
 */
public class ListImageTagsRequest extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // Drive ID
    @NameInMap("drive_id")
    @Validation(required = true)
    public String driveId;

    // image_thumbnail_process
    @NameInMap("image_thumbnail_process")
    public String imageThumbnailProcess;

    // video_thumbnail_process
    // type:string
    @NameInMap("video_thumbnail_process")
    public String videoThumbnailProcess;

    public static ListImageTagsRequest build(java.util.Map<String, ?> map) throws Exception {
        ListImageTagsRequest self = new ListImageTagsRequest();
        return TeaModel.build(map, self);
    }

    public ListImageTagsRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ListImageTagsRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public ListImageTagsRequest setImageThumbnailProcess(String imageThumbnailProcess) {
        this.imageThumbnailProcess = imageThumbnailProcess;
        return this;
    }
    public String getImageThumbnailProcess() {
        return this.imageThumbnailProcess;
    }

    public ListImageTagsRequest setVideoThumbnailProcess(String videoThumbnailProcess) {
        this.videoThumbnailProcess = videoThumbnailProcess;
        return this;
    }
    public String getVideoThumbnailProcess() {
        return this.videoThumbnailProcess;
    }

}
