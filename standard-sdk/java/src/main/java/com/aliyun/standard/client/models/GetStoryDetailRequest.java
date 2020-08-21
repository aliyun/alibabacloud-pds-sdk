// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.standard.client.models;

import com.aliyun.tea.*;

/**
 * Get story detail request
 */
public class GetStoryDetailRequest extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // drive_id
    @NameInMap("drive_id")
    @Validation(required = true, pattern = "[0-9]+")
    public String driveId;

    // story_id
    @NameInMap("story_id")
    @Validation(required = true)
    public String storyId;

    // url_expire_sec
    @NameInMap("video_url_expire_sec")
    public Long videoUrlExpireSec;

    public static GetStoryDetailRequest build(java.util.Map<String, ?> map) throws Exception {
        GetStoryDetailRequest self = new GetStoryDetailRequest();
        return TeaModel.build(map, self);
    }

    public GetStoryDetailRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetStoryDetailRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public GetStoryDetailRequest setStoryId(String storyId) {
        this.storyId = storyId;
        return this;
    }
    public String getStoryId() {
        return this.storyId;
    }

    public GetStoryDetailRequest setVideoUrlExpireSec(Long videoUrlExpireSec) {
        this.videoUrlExpireSec = videoUrlExpireSec;
        return this;
    }
    public Long getVideoUrlExpireSec() {
        return this.videoUrlExpireSec;
    }

}
