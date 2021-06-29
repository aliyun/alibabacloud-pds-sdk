// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * Create story request
 */
public class CreateStoryRequest extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // drive_id
    @NameInMap("drive_id")
    @Validation(required = true, pattern = "[0-9]+")
    public String driveId;

    // max_image_count
    @NameInMap("max_image_count")
    public Long maxImageCount;

    // min_image_count
    @NameInMap("min_image_count")
    public Long minImageCount;

    // story_end_time
    @NameInMap("story_end_time")
    public String storyEndTime;

    // story_id
    @NameInMap("story_id")
    public String storyId;

    // story_name
    @NameInMap("story_name")
    public String storyName;

    // story_start_time
    @NameInMap("story_start_time")
    public String storyStartTime;

    // story_type
    @NameInMap("story_type")
    @Validation(required = true)
    public String storyType;

    public static CreateStoryRequest build(java.util.Map<String, ?> map) throws Exception {
        CreateStoryRequest self = new CreateStoryRequest();
        return TeaModel.build(map, self);
    }

    public CreateStoryRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public CreateStoryRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public CreateStoryRequest setMaxImageCount(Long maxImageCount) {
        this.maxImageCount = maxImageCount;
        return this;
    }
    public Long getMaxImageCount() {
        return this.maxImageCount;
    }

    public CreateStoryRequest setMinImageCount(Long minImageCount) {
        this.minImageCount = minImageCount;
        return this;
    }
    public Long getMinImageCount() {
        return this.minImageCount;
    }

    public CreateStoryRequest setStoryEndTime(String storyEndTime) {
        this.storyEndTime = storyEndTime;
        return this;
    }
    public String getStoryEndTime() {
        return this.storyEndTime;
    }

    public CreateStoryRequest setStoryId(String storyId) {
        this.storyId = storyId;
        return this;
    }
    public String getStoryId() {
        return this.storyId;
    }

    public CreateStoryRequest setStoryName(String storyName) {
        this.storyName = storyName;
        return this;
    }
    public String getStoryName() {
        return this.storyName;
    }

    public CreateStoryRequest setStoryStartTime(String storyStartTime) {
        this.storyStartTime = storyStartTime;
        return this;
    }
    public String getStoryStartTime() {
        return this.storyStartTime;
    }

    public CreateStoryRequest setStoryType(String storyType) {
        this.storyType = storyType;
        return this;
    }
    public String getStoryType() {
        return this.storyType;
    }

}
