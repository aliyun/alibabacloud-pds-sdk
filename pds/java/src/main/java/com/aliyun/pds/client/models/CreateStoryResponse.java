// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 生成故事
 */
public class CreateStoryResponse extends TeaModel {
    // drive_id
    @NameInMap("drive_id")
    public String driveId;

    public static CreateStoryResponse build(java.util.Map<String, ?> map) throws Exception {
        CreateStoryResponse self = new CreateStoryResponse();
        return TeaModel.build(map, self);
    }

    public CreateStoryResponse setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

}
