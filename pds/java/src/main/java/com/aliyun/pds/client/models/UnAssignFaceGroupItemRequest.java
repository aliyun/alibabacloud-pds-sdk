// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * Unassign facegroup item request
 */
public class UnAssignFaceGroupItemRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    // drive_id
    @NameInMap("drive_id")
    @Validation(required = true, pattern = "[0-9]+")
    public String driveId;

    // face_group_id
    @NameInMap("face_group_id")
    public String faceGroupId;

    // file_id
    @NameInMap("file_id")
    @Validation(required = true)
    public String fileId;

    // group_id 列举人脸分组接口中获取
    @NameInMap("group_id")
    public String groupId;

    public static UnAssignFaceGroupItemRequest build(java.util.Map<String, ?> map) throws Exception {
        UnAssignFaceGroupItemRequest self = new UnAssignFaceGroupItemRequest();
        return TeaModel.build(map, self);
    }

    public UnAssignFaceGroupItemRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public UnAssignFaceGroupItemRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public UnAssignFaceGroupItemRequest setFaceGroupId(String faceGroupId) {
        this.faceGroupId = faceGroupId;
        return this;
    }
    public String getFaceGroupId() {
        return this.faceGroupId;
    }

    public UnAssignFaceGroupItemRequest setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

    public UnAssignFaceGroupItemRequest setGroupId(String groupId) {
        this.groupId = groupId;
        return this;
    }
    public String getGroupId() {
        return this.groupId;
    }

}
