// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * remove story files response
 */
public class RemoveStoryFilesResponse extends TeaModel {
    /**
     * <p>drive_id</p>
     */
    @NameInMap("drive_id")
    public String driveId;

    /**
     * <p>request_id</p>
     */
    @NameInMap("request_id")
    public String requestId;

    /**
     * <p>story_id</p>
     */
    @NameInMap("story_id")
    public String storyId;

    public static RemoveStoryFilesResponse build(java.util.Map<String, ?> map) throws Exception {
        RemoveStoryFilesResponse self = new RemoveStoryFilesResponse();
        return TeaModel.build(map, self);
    }

    public RemoveStoryFilesResponse setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public RemoveStoryFilesResponse setRequestId(String requestId) {
        this.requestId = requestId;
        return this;
    }
    public String getRequestId() {
        return this.requestId;
    }

    public RemoveStoryFilesResponse setStoryId(String storyId) {
        this.storyId = storyId;
        return this;
    }
    public String getStoryId() {
        return this.storyId;
    }

}
