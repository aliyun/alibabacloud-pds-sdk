// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * add story files response
 */
public class AddStoryFilesResponse extends TeaModel {
    // drive_id
    @NameInMap("drive_id")
    public String driveId;

    // files
    @NameInMap("files")
    public java.util.List<AddStoryFile> files;

    // request_id
    @NameInMap("request_id")
    public String requestId;

    // story_id
    @NameInMap("story_id")
    public String storyId;

    public static AddStoryFilesResponse build(java.util.Map<String, ?> map) throws Exception {
        AddStoryFilesResponse self = new AddStoryFilesResponse();
        return TeaModel.build(map, self);
    }

    public AddStoryFilesResponse setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public AddStoryFilesResponse setFiles(java.util.List<AddStoryFile> files) {
        this.files = files;
        return this;
    }
    public java.util.List<AddStoryFile> getFiles() {
        return this.files;
    }

    public AddStoryFilesResponse setRequestId(String requestId) {
        this.requestId = requestId;
        return this;
    }
    public String getRequestId() {
        return this.requestId;
    }

    public AddStoryFilesResponse setStoryId(String storyId) {
        this.storyId = storyId;
        return this;
    }
    public String getStoryId() {
        return this.storyId;
    }

}
