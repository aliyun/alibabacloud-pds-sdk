// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * Create story request
 */
public class CreateStoryRequest extends TeaModel {
    @NameInMap("address")
    public Address address;

    /**
     * <p>custom_id</p>
     */
    @NameInMap("custom_id")
    public String customId;

    /**
     * <p>custom_labels</p>
     */
    @NameInMap("custom_labels")
    public java.util.Map<String, ?> customLabels;

    /**
     * <p>drive_id</p>
     */
    @NameInMap("drive_id")
    @Validation(required = true, pattern = "[0-9]+")
    public String driveId;

    /**
     * <p>max_image_count</p>
     */
    @NameInMap("max_image_count")
    public Long maxImageCount;

    /**
     * <p>min_image_count</p>
     */
    @NameInMap("min_image_count")
    public Long minImageCount;

    /**
     * <p>story_end_time</p>
     */
    @NameInMap("story_end_time")
    public String storyEndTime;

    /**
     * <p>story_id</p>
     */
    @NameInMap("story_id")
    public String storyId;

    /**
     * <p>story_name</p>
     */
    @NameInMap("story_name")
    public String storyName;

    /**
     * <p>story_start_time</p>
     */
    @NameInMap("story_start_time")
    public String storyStartTime;

    /**
     * <p>story_sub_type</p>
     */
    @NameInMap("story_sub_type")
    public String storySubType;

    /**
     * <p>story_type</p>
     */
    @NameInMap("story_type")
    @Validation(required = true)
    public String storyType;

    public static CreateStoryRequest build(java.util.Map<String, ?> map) throws Exception {
        CreateStoryRequest self = new CreateStoryRequest();
        return TeaModel.build(map, self);
    }

    public CreateStoryRequest setAddress(Address address) {
        this.address = address;
        return this;
    }
    public Address getAddress() {
        return this.address;
    }

    public CreateStoryRequest setCustomId(String customId) {
        this.customId = customId;
        return this;
    }
    public String getCustomId() {
        return this.customId;
    }

    public CreateStoryRequest setCustomLabels(java.util.Map<String, ?> customLabels) {
        this.customLabels = customLabels;
        return this;
    }
    public java.util.Map<String, ?> getCustomLabels() {
        return this.customLabels;
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

    public CreateStoryRequest setStorySubType(String storySubType) {
        this.storySubType = storySubType;
        return this;
    }
    public String getStorySubType() {
        return this.storySubType;
    }

    public CreateStoryRequest setStoryType(String storyType) {
        this.storyType = storyType;
        return this;
    }
    public String getStoryType() {
        return this.storyType;
    }

}
