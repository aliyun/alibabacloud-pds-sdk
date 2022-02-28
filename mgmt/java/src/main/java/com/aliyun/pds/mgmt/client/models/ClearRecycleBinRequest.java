// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 清空回收站
 */
public class ClearRecycleBinRequest extends TeaModel {
    // drive_id
    @NameInMap("drive_id")
    @Validation(pattern = "[0-9]+")
    public String driveId;

    public static ClearRecycleBinRequest build(java.util.Map<String, ?> map) throws Exception {
        ClearRecycleBinRequest self = new ClearRecycleBinRequest();
        return TeaModel.build(map, self);
    }

    public ClearRecycleBinRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

}
