// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * update story response
 */
public class UpdateStoryResponse extends TeaModel {
    // drive_id
    @NameInMap("drive_id")
    public String driveId;

    // story_id
    @NameInMap("story_id")
    public String storyId;

    public static UpdateStoryResponse build(java.util.Map<String, ?> map) throws Exception {
        UpdateStoryResponse self = new UpdateStoryResponse();
        return TeaModel.build(map, self);
    }

    public UpdateStoryResponse setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public UpdateStoryResponse setStoryId(String storyId) {
        this.storyId = storyId;
        return this;
    }
    public String getStoryId() {
        return this.storyId;
    }

}
