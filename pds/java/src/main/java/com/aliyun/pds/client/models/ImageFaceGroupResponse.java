// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class ImageFaceGroupResponse extends TeaModel {
    // 人脸分组生成时间
    @NameInMap("created_at")
    public String createdAt;

    // 人脸个数
    @NameInMap("face_count")
    public Long faceCount;

    // 人脸分组封面头像地址
    @NameInMap("group_cover_url")
    public String groupCoverUrl;

    // 人脸分组 ID
    @NameInMap("group_id")
    public String groupId;

    // 人脸分组名称
    @NameInMap("group_name")
    public String groupName;

    // 照片个数
    @NameInMap("image_count")
    public Long imageCount;

    // 人脸分组修改时间
    @NameInMap("updated_at")
    public String updatedAt;

    public static ImageFaceGroupResponse build(java.util.Map<String, ?> map) throws Exception {
        ImageFaceGroupResponse self = new ImageFaceGroupResponse();
        return TeaModel.build(map, self);
    }

    public ImageFaceGroupResponse setCreatedAt(String createdAt) {
        this.createdAt = createdAt;
        return this;
    }
    public String getCreatedAt() {
        return this.createdAt;
    }

    public ImageFaceGroupResponse setFaceCount(Long faceCount) {
        this.faceCount = faceCount;
        return this;
    }
    public Long getFaceCount() {
        return this.faceCount;
    }

    public ImageFaceGroupResponse setGroupCoverUrl(String groupCoverUrl) {
        this.groupCoverUrl = groupCoverUrl;
        return this;
    }
    public String getGroupCoverUrl() {
        return this.groupCoverUrl;
    }

    public ImageFaceGroupResponse setGroupId(String groupId) {
        this.groupId = groupId;
        return this;
    }
    public String getGroupId() {
        return this.groupId;
    }

    public ImageFaceGroupResponse setGroupName(String groupName) {
        this.groupName = groupName;
        return this;
    }
    public String getGroupName() {
        return this.groupName;
    }

    public ImageFaceGroupResponse setImageCount(Long imageCount) {
        this.imageCount = imageCount;
        return this;
    }
    public Long getImageCount() {
        return this.imageCount;
    }

    public ImageFaceGroupResponse setUpdatedAt(String updatedAt) {
        this.updatedAt = updatedAt;
        return this;
    }
    public String getUpdatedAt() {
        return this.updatedAt;
    }

}
