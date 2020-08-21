// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * Remove story images request
 */
public class RemoveStoryImagesRequest extends TeaModel {
    @NameInMap("drive_id")
    public String driveId;

    @NameInMap("file_ids")
    public java.util.List<String> fileIds;

    @NameInMap("story_id")
    public String storyId;

    public static RemoveStoryImagesRequest build(java.util.Map<String, ?> map) throws Exception {
        RemoveStoryImagesRequest self = new RemoveStoryImagesRequest();
        return TeaModel.build(map, self);
    }

    public RemoveStoryImagesRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public RemoveStoryImagesRequest setFileIds(java.util.List<String> fileIds) {
        this.fileIds = fileIds;
        return this;
    }
    public java.util.List<String> getFileIds() {
        return this.fileIds;
    }

    public RemoveStoryImagesRequest setStoryId(String storyId) {
        this.storyId = storyId;
        return this;
    }
    public String getStoryId() {
        return this.storyId;
    }

}
