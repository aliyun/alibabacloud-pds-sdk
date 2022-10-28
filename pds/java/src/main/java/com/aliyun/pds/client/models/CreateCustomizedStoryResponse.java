// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 生成自定义故事
 */
public class CreateCustomizedStoryResponse extends TeaModel {
    // drive_id
    @NameInMap("drive_id")
    public String driveId;

    @NameInMap("story_id")
    public String storyId;

    public static CreateCustomizedStoryResponse build(java.util.Map<String, ?> map) throws Exception {
        CreateCustomizedStoryResponse self = new CreateCustomizedStoryResponse();
        return TeaModel.build(map, self);
    }

    public CreateCustomizedStoryResponse setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public CreateCustomizedStoryResponse setStoryId(String storyId) {
        this.storyId = storyId;
        return this;
    }
    public String getStoryId() {
        return this.storyId;
    }

}
