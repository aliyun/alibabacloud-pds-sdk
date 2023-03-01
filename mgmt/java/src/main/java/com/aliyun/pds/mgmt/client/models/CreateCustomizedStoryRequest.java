// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * Create custom story request
 */
public class CreateCustomizedStoryRequest extends TeaModel {
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

    @NameInMap("story_cover")
    public StoryFile storyCover;

    /**
     * <p>story_file_ids</p>
     */
    @NameInMap("story_files")
    public java.util.List<StoryFile> storyFiles;

    /**
     * <p>story_name</p>
     */
    @NameInMap("story_name")
    public String storyName;

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

    public static CreateCustomizedStoryRequest build(java.util.Map<String, ?> map) throws Exception {
        CreateCustomizedStoryRequest self = new CreateCustomizedStoryRequest();
        return TeaModel.build(map, self);
    }

    public CreateCustomizedStoryRequest setCustomLabels(java.util.Map<String, ?> customLabels) {
        this.customLabels = customLabels;
        return this;
    }
    public java.util.Map<String, ?> getCustomLabels() {
        return this.customLabels;
    }

    public CreateCustomizedStoryRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public CreateCustomizedStoryRequest setStoryCover(StoryFile storyCover) {
        this.storyCover = storyCover;
        return this;
    }
    public StoryFile getStoryCover() {
        return this.storyCover;
    }

    public CreateCustomizedStoryRequest setStoryFiles(java.util.List<StoryFile> storyFiles) {
        this.storyFiles = storyFiles;
        return this;
    }
    public java.util.List<StoryFile> getStoryFiles() {
        return this.storyFiles;
    }

    public CreateCustomizedStoryRequest setStoryName(String storyName) {
        this.storyName = storyName;
        return this;
    }
    public String getStoryName() {
        return this.storyName;
    }

    public CreateCustomizedStoryRequest setStorySubType(String storySubType) {
        this.storySubType = storySubType;
        return this;
    }
    public String getStorySubType() {
        return this.storySubType;
    }

    public CreateCustomizedStoryRequest setStoryType(String storyType) {
        this.storyType = storyType;
        return this;
    }
    public String getStoryType() {
        return this.storyType;
    }

}
