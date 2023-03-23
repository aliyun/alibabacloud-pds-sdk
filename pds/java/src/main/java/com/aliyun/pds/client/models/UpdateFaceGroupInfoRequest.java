// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * # Update face group info request
 */
public class UpdateFaceGroupInfoRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    /**
     * <p>drive_id</p>
     */
    @NameInMap("drive_id")
    @Validation(required = true, pattern = "[0-9]+")
    public String driveId;

    /**
     * <p>group_cover_face_id</p>
     */
    @NameInMap("group_cover_face_id")
    public String groupCoverFaceId;

    /**
     * <p>group_id 列举人脸分组接口中获取</p>
     */
    @NameInMap("group_id")
    @Validation(required = true)
    public String groupId;

    /**
     * <p>group_name</p>
     */
    @NameInMap("group_name")
    public String groupName;

    /**
     * <p>remarks</p>
     */
    @NameInMap("remarks")
    public String remarks;

    public static UpdateFaceGroupInfoRequest build(java.util.Map<String, ?> map) throws Exception {
        UpdateFaceGroupInfoRequest self = new UpdateFaceGroupInfoRequest();
        return TeaModel.build(map, self);
    }

    public UpdateFaceGroupInfoRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public UpdateFaceGroupInfoRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public UpdateFaceGroupInfoRequest setGroupCoverFaceId(String groupCoverFaceId) {
        this.groupCoverFaceId = groupCoverFaceId;
        return this;
    }
    public String getGroupCoverFaceId() {
        return this.groupCoverFaceId;
    }

    public UpdateFaceGroupInfoRequest setGroupId(String groupId) {
        this.groupId = groupId;
        return this;
    }
    public String getGroupId() {
        return this.groupId;
    }

    public UpdateFaceGroupInfoRequest setGroupName(String groupName) {
        this.groupName = groupName;
        return this;
    }
    public String getGroupName() {
        return this.groupName;
    }

    public UpdateFaceGroupInfoRequest setRemarks(String remarks) {
        this.remarks = remarks;
        return this;
    }
    public String getRemarks() {
        return this.remarks;
    }

}
