// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

/**
 * 获取最新游标
 */
public class GetLastCursorRequest extends TeaModel {
    // drive_id
    @NameInMap("drive_id")
    @Validation(required = true, pattern = "[0-9]+")
    public String driveId;

    public static GetLastCursorRequest build(java.util.Map<String, ?> map) throws Exception {
        GetLastCursorRequest self = new GetLastCursorRequest();
        return TeaModel.build(map, self);
    }

    public GetLastCursorRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

}
