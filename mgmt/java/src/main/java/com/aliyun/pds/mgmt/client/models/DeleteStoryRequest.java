// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * delete story request
 */
public class DeleteStoryRequest extends TeaModel {
    /**
     * <p>drive_id</p>
     */
    @NameInMap("drive_id")
    @Validation(required = true, pattern = "[0-9]+")
    public String driveId;

    /**
     * <p>story_id</p>
     */
    @NameInMap("story_id")
    @Validation(required = true)
    public String storyId;

    public static DeleteStoryRequest build(java.util.Map<String, ?> map) throws Exception {
        DeleteStoryRequest self = new DeleteStoryRequest();
        return TeaModel.build(map, self);
    }

    public DeleteStoryRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public DeleteStoryRequest setStoryId(String storyId) {
        this.storyId = storyId;
        return this;
    }
    public String getStoryId() {
        return this.storyId;
    }

}
