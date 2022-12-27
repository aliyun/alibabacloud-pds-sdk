// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 更新人脸分组信息结果
 */
public class UpdateFaceGroupInfoResponse extends TeaModel {
    /**
     * <p>drive_id</p>
     */
    @NameInMap("drive_id")
    public String driveId;

    /**
     * <p>group_id</p>
     */
    @NameInMap("group_id")
    public String groupId;

    public static UpdateFaceGroupInfoResponse build(java.util.Map<String, ?> map) throws Exception {
        UpdateFaceGroupInfoResponse self = new UpdateFaceGroupInfoResponse();
        return TeaModel.build(map, self);
    }

    public UpdateFaceGroupInfoResponse setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public UpdateFaceGroupInfoResponse setGroupId(String groupId) {
        this.groupId = groupId;
        return this;
    }
    public String getGroupId() {
        return this.groupId;
    }

}
