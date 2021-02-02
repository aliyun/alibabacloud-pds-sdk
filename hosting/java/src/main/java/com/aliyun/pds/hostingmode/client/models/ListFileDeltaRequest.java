// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.hostingmode.client.models;

import com.aliyun.tea.*;

/**
 * 获取增量文件操作记录
 */
public class ListFileDeltaRequest extends TeaModel {
    // cursor 游标
    @NameInMap("cursor")
    public String cursor;

    // drive_id
    @NameInMap("drive_id")
    @Validation(required = true, pattern = "[0-9]+")
    public String driveId;

    @NameInMap("image_cropping_aspect_ratios")
    public java.util.List<String> imageCroppingAspectRatios;

    // image_thumbnail_process
    @NameInMap("image_thumbnail_process")
    public String imageThumbnailProcess;

    // image_url_process
    @NameInMap("image_url_process")
    public String imageUrlProcess;

    // limit
    // default 100
    @NameInMap("limit")
    public Integer limit;

    // video_thumbnail_process
    // type:string
    @NameInMap("video_thumbnail_process")
    public String videoThumbnailProcess;

    public static ListFileDeltaRequest build(java.util.Map<String, ?> map) throws Exception {
        ListFileDeltaRequest self = new ListFileDeltaRequest();
        return TeaModel.build(map, self);
    }

    public ListFileDeltaRequest setCursor(String cursor) {
        this.cursor = cursor;
        return this;
    }
    public String getCursor() {
        return this.cursor;
    }

    public ListFileDeltaRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public ListFileDeltaRequest setImageCroppingAspectRatios(java.util.List<String> imageCroppingAspectRatios) {
        this.imageCroppingAspectRatios = imageCroppingAspectRatios;
        return this;
    }
    public java.util.List<String> getImageCroppingAspectRatios() {
        return this.imageCroppingAspectRatios;
    }

    public ListFileDeltaRequest setImageThumbnailProcess(String imageThumbnailProcess) {
        this.imageThumbnailProcess = imageThumbnailProcess;
        return this;
    }
    public String getImageThumbnailProcess() {
        return this.imageThumbnailProcess;
    }

    public ListFileDeltaRequest setImageUrlProcess(String imageUrlProcess) {
        this.imageUrlProcess = imageUrlProcess;
        return this;
    }
    public String getImageUrlProcess() {
        return this.imageUrlProcess;
    }

    public ListFileDeltaRequest setLimit(Integer limit) {
        this.limit = limit;
        return this;
    }
    public Integer getLimit() {
        return this.limit;
    }

    public ListFileDeltaRequest setVideoThumbnailProcess(String videoThumbnailProcess) {
        this.videoThumbnailProcess = videoThumbnailProcess;
        return this;
    }
    public String getVideoThumbnailProcess() {
        return this.videoThumbnailProcess;
    }

}
