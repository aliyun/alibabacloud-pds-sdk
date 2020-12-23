// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * Remove story images response
 */
public class RemoveStoryImagesResponse extends TeaModel {
    // drive_id
    @NameInMap("drive_id")
    public String driveId;

    // file_ids
    @NameInMap("file_ids")
    public java.util.List<String> fileIds;

    @NameInMap("results")
    public java.util.List<RemoveStoryImagesResultItem> results;

    // story_id
    @NameInMap("story_id")
    public String storyId;

    // success_file_ids
    @NameInMap("success_file_ids")
    public java.util.List<String> successFileIds;

    public static RemoveStoryImagesResponse build(java.util.Map<String, ?> map) throws Exception {
        RemoveStoryImagesResponse self = new RemoveStoryImagesResponse();
        return TeaModel.build(map, self);
    }

    public RemoveStoryImagesResponse setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public RemoveStoryImagesResponse setFileIds(java.util.List<String> fileIds) {
        this.fileIds = fileIds;
        return this;
    }
    public java.util.List<String> getFileIds() {
        return this.fileIds;
    }

    public RemoveStoryImagesResponse setResults(java.util.List<RemoveStoryImagesResultItem> results) {
        this.results = results;
        return this;
    }
    public java.util.List<RemoveStoryImagesResultItem> getResults() {
        return this.results;
    }

    public RemoveStoryImagesResponse setStoryId(String storyId) {
        this.storyId = storyId;
        return this;
    }
    public String getStoryId() {
        return this.storyId;
    }

    public RemoveStoryImagesResponse setSuccessFileIds(java.util.List<String> successFileIds) {
        this.successFileIds = successFileIds;
        return this;
    }
    public java.util.List<String> getSuccessFileIds() {
        return this.successFileIds;
    }

}
