// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * Update story request
 */
public class UpdateStoryRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    @NameInMap("cover")
    public StoryFile cover;

    // custom_id
    @NameInMap("custom_id")
    public String customId;

    // custom_labels
    @NameInMap("custom_labels")
    public java.util.Map<String, ?> customLabels;

    // drive_id
    @NameInMap("drive_id")
    @Validation(required = true, pattern = "[0-9]+")
    public String driveId;

    // story_id
    @NameInMap("story_id")
    @Validation(required = true)
    public String storyId;

    // story_name
    @NameInMap("story_name")
    public String storyName;

    public static UpdateStoryRequest build(java.util.Map<String, ?> map) throws Exception {
        UpdateStoryRequest self = new UpdateStoryRequest();
        return TeaModel.build(map, self);
    }

    public UpdateStoryRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public UpdateStoryRequest setCover(StoryFile cover) {
        this.cover = cover;
        return this;
    }
    public StoryFile getCover() {
        return this.cover;
    }

    public UpdateStoryRequest setCustomId(String customId) {
        this.customId = customId;
        return this;
    }
    public String getCustomId() {
        return this.customId;
    }

    public UpdateStoryRequest setCustomLabels(java.util.Map<String, ?> customLabels) {
        this.customLabels = customLabels;
        return this;
    }
    public java.util.Map<String, ?> getCustomLabels() {
        return this.customLabels;
    }

    public UpdateStoryRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public UpdateStoryRequest setStoryId(String storyId) {
        this.storyId = storyId;
        return this;
    }
    public String getStoryId() {
        return this.storyId;
    }

    public UpdateStoryRequest setStoryName(String storyName) {
        this.storyName = storyName;
        return this;
    }
    public String getStoryName() {
        return this.storyName;
    }

}
