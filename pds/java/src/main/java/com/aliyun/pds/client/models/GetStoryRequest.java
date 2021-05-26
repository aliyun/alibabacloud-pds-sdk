// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * Get story request
 */
public class GetStoryRequest extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // cover_image_thumbnail_process
    @NameInMap("cover_image_thumbnail_process")
    public String coverImageThumbnailProcess;

    // cover_video_thumbnail_process
    @NameInMap("cover_video_thumbnail_process")
    public String coverVideoThumbnailProcess;

    // drive_id
    @NameInMap("drive_id")
    @Validation(required = true, pattern = "[0-9]+")
    public String driveId;

    // image_process
    @NameInMap("image_process")
    public String imageProcess;

    // image_thumbnail_process
    @NameInMap("image_thumbnail_process")
    public String imageThumbnailProcess;

    // story_id
    @NameInMap("story_id")
    @Validation(required = true)
    public String storyId;

    // url_expire_sec
    @NameInMap("url_expire_sec")
    public Long urlExpireSec;

    // video_thumbnail_process
    @NameInMap("video_thumbnail_process")
    public String videoThumbnailProcess;

    public static GetStoryRequest build(java.util.Map<String, ?> map) throws Exception {
        GetStoryRequest self = new GetStoryRequest();
        return TeaModel.build(map, self);
    }

    public GetStoryRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetStoryRequest setCoverImageThumbnailProcess(String coverImageThumbnailProcess) {
        this.coverImageThumbnailProcess = coverImageThumbnailProcess;
        return this;
    }
    public String getCoverImageThumbnailProcess() {
        return this.coverImageThumbnailProcess;
    }

    public GetStoryRequest setCoverVideoThumbnailProcess(String coverVideoThumbnailProcess) {
        this.coverVideoThumbnailProcess = coverVideoThumbnailProcess;
        return this;
    }
    public String getCoverVideoThumbnailProcess() {
        return this.coverVideoThumbnailProcess;
    }

    public GetStoryRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public GetStoryRequest setImageProcess(String imageProcess) {
        this.imageProcess = imageProcess;
        return this;
    }
    public String getImageProcess() {
        return this.imageProcess;
    }

    public GetStoryRequest setImageThumbnailProcess(String imageThumbnailProcess) {
        this.imageThumbnailProcess = imageThumbnailProcess;
        return this;
    }
    public String getImageThumbnailProcess() {
        return this.imageThumbnailProcess;
    }

    public GetStoryRequest setStoryId(String storyId) {
        this.storyId = storyId;
        return this;
    }
    public String getStoryId() {
        return this.storyId;
    }

    public GetStoryRequest setUrlExpireSec(Long urlExpireSec) {
        this.urlExpireSec = urlExpireSec;
        return this;
    }
    public Long getUrlExpireSec() {
        return this.urlExpireSec;
    }

    public GetStoryRequest setVideoThumbnailProcess(String videoThumbnailProcess) {
        this.videoThumbnailProcess = videoThumbnailProcess;
        return this;
    }
    public String getVideoThumbnailProcess() {
        return this.videoThumbnailProcess;
    }

}
