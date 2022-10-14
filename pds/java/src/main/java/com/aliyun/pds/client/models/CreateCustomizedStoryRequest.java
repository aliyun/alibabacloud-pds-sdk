// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * Create custom story request
 */
public class CreateCustomizedStoryRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    // custom_labels
    @NameInMap("custom_labels")
    public java.util.Map<String, ?> customLabels;

    // drive_id
    @NameInMap("drive_id")
    @Validation(required = true, pattern = "[0-9]+")
    public String driveId;

    @NameInMap("story_cover")
    public StoryFile storyCover;

    // story_file_ids
    @NameInMap("story_files")
    public java.util.List<StoryFile> storyFiles;

    // story_name
    @NameInMap("story_name")
    public String storyName;

    // story_sub_type
    @NameInMap("story_sub_type")
    public String storySubType;

    // story_type
    @NameInMap("story_type")
    @Validation(required = true)
    public String storyType;

    public static CreateCustomizedStoryRequest build(java.util.Map<String, ?> map) throws Exception {
        CreateCustomizedStoryRequest self = new CreateCustomizedStoryRequest();
        return TeaModel.build(map, self);
    }

    public CreateCustomizedStoryRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
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
