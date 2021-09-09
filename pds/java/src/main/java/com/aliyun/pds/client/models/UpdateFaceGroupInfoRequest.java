// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * Update face group info request
 */
public class UpdateFaceGroupInfoRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    // drive_id
    @NameInMap("drive_id")
    @Validation(required = true, pattern = "[0-9]+")
    public String driveId;

    // group_cover_face_id
    @NameInMap("group_cover_face_id")
    public String groupCoverFaceId;

    // group_id 列举人脸分组接口中获取
    @NameInMap("group_id")
    @Validation(required = true)
    public String groupId;

    // group_name
    @NameInMap("group_name")
    public String groupName;

    // remarks
    @NameInMap("remarks")
    public String remarks;

    // remarks_array
    @NameInMap("remarks_array")
    public java.util.List<String> remarksArray;

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

    public UpdateFaceGroupInfoRequest setRemarksArray(java.util.List<String> remarksArray) {
        this.remarksArray = remarksArray;
        return this;
    }
    public java.util.List<String> getRemarksArray() {
        return this.remarksArray;
    }

}
