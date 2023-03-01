// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * Get face group info request
 */
public class GetFaceGroupInfoRequest extends TeaModel {
    /**
     * <p>drive_id</p>
     */
    @NameInMap("drive_id")
    @Validation(required = true, pattern = "[0-9]+")
    public String driveId;

    /**
     * <p>group_id 列举人脸分组接口中获取</p>
     */
    @NameInMap("group_id")
    @Validation(required = true)
    public String groupId;

    public static GetFaceGroupInfoRequest build(java.util.Map<String, ?> map) throws Exception {
        GetFaceGroupInfoRequest self = new GetFaceGroupInfoRequest();
        return TeaModel.build(map, self);
    }

    public GetFaceGroupInfoRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public GetFaceGroupInfoRequest setGroupId(String groupId) {
        this.groupId = groupId;
        return this;
    }
    public String getGroupId() {
        return this.groupId;
    }

}
