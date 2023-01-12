// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * add story files request
 */
public class AddStoryFilesRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    /**
     * <p>drive_id</p>
     */
    @NameInMap("drive_id")
    @Validation(required = true, pattern = "[0-9]+")
    public String driveId;

    @NameInMap("files")
    public java.util.List<StoryFile> files;

    /**
     * <p>story_id</p>
     */
    @NameInMap("story_id")
    @Validation(required = true)
    public String storyId;

    public static AddStoryFilesRequest build(java.util.Map<String, ?> map) throws Exception {
        AddStoryFilesRequest self = new AddStoryFilesRequest();
        return TeaModel.build(map, self);
    }

    public AddStoryFilesRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public AddStoryFilesRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public AddStoryFilesRequest setFiles(java.util.List<StoryFile> files) {
        this.files = files;
        return this;
    }
    public java.util.List<StoryFile> getFiles() {
        return this.files;
    }

    public AddStoryFilesRequest setStoryId(String storyId) {
        this.storyId = storyId;
        return this;
    }
    public String getStoryId() {
        return this.storyId;
    }

}
