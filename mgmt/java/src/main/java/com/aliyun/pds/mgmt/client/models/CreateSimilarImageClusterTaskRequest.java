// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * create similar image cluster task request
 */
public class CreateSimilarImageClusterTaskRequest extends TeaModel {
    /**
     * <p>drive_id</p>
     */
    @NameInMap("drive_id")
    @Validation(required = true, pattern = "[0-9]+")
    public String driveId;

    public static CreateSimilarImageClusterTaskRequest build(java.util.Map<String, ?> map) throws Exception {
        CreateSimilarImageClusterTaskRequest self = new CreateSimilarImageClusterTaskRequest();
        return TeaModel.build(map, self);
    }

    public CreateSimilarImageClusterTaskRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

}
