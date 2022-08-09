// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * remove story files request
 */
public class RemoveStoryFilesRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    // drive_id
    @NameInMap("drive_id")
    @Validation(required = true, pattern = "[0-9]+")
    public String driveId;

    @NameInMap("files")
    public java.util.List<StoryFile> files;

    // story_id
    @NameInMap("story_id")
    @Validation(required = true)
    public String storyId;

    public static RemoveStoryFilesRequest build(java.util.Map<String, ?> map) throws Exception {
        RemoveStoryFilesRequest self = new RemoveStoryFilesRequest();
        return TeaModel.build(map, self);
    }

    public RemoveStoryFilesRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public RemoveStoryFilesRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public RemoveStoryFilesRequest setFiles(java.util.List<StoryFile> files) {
        this.files = files;
        return this;
    }
    public java.util.List<StoryFile> getFiles() {
        return this.files;
    }

    public RemoveStoryFilesRequest setStoryId(String storyId) {
        this.storyId = storyId;
        return this;
    }
    public String getStoryId() {
        return this.storyId;
    }

}
