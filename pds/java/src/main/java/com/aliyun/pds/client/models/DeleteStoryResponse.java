// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 删除故事
 */
public class DeleteStoryResponse extends TeaModel {
    /**
     * <p>drive_id</p>
     */
    @NameInMap("drive_id")
    public String driveId;

    public static DeleteStoryResponse build(java.util.Map<String, ?> map) throws Exception {
        DeleteStoryResponse self = new DeleteStoryResponse();
        return TeaModel.build(map, self);
    }

    public DeleteStoryResponse setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

}
