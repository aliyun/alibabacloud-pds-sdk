// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 人脸分组信息
 */
public class ImageFaceGroupResponse extends TeaModel {
    /**
     * <p>人脸分组生成时间</p>
     */
    @NameInMap("created_at")
    public String createdAt;

    @NameInMap("group_cover_face_boundary")
    public FaceBoundary groupCoverFaceBoundary;

    /**
     * <p>group_cover_file_id</p>
     */
    @NameInMap("group_cover_file_id")
    public String groupCoverFileId;

    /**
     * <p>group_cover_height</p>
     */
    @NameInMap("group_cover_height")
    public Long groupCoverHeight;

    /**
     * <p>人脸分组封面头像地址</p>
     */
    @NameInMap("group_cover_url")
    public String groupCoverUrl;

    /**
     * <p>group_cover_width</p>
     */
    @NameInMap("group_cover_width")
    public Long groupCoverWidth;

    /**
     * <p>人脸分组 ID</p>
     */
    @NameInMap("group_id")
    public String groupId;

    /**
     * <p>人脸分组名称</p>
     */
    @NameInMap("group_name")
    public String groupName;

    /**
     * <p>照片个数</p>
     */
    @NameInMap("image_count")
    public Long imageCount;

    /**
     * <p>remarks</p>
     */
    @NameInMap("remarks")
    public String remarks;

    /**
     * <p>remarks_array</p>
     */
    @NameInMap("remarks_array")
    public java.util.List<String> remarksArray;

    /**
     * <p>人脸分组修改时间</p>
     */
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

    public ImageFaceGroupResponse setGroupCoverFaceBoundary(FaceBoundary groupCoverFaceBoundary) {
        this.groupCoverFaceBoundary = groupCoverFaceBoundary;
        return this;
    }
    public FaceBoundary getGroupCoverFaceBoundary() {
        return this.groupCoverFaceBoundary;
    }

    public ImageFaceGroupResponse setGroupCoverFileId(String groupCoverFileId) {
        this.groupCoverFileId = groupCoverFileId;
        return this;
    }
    public String getGroupCoverFileId() {
        return this.groupCoverFileId;
    }

    public ImageFaceGroupResponse setGroupCoverHeight(Long groupCoverHeight) {
        this.groupCoverHeight = groupCoverHeight;
        return this;
    }
    public Long getGroupCoverHeight() {
        return this.groupCoverHeight;
    }

    public ImageFaceGroupResponse setGroupCoverUrl(String groupCoverUrl) {
        this.groupCoverUrl = groupCoverUrl;
        return this;
    }
    public String getGroupCoverUrl() {
        return this.groupCoverUrl;
    }

    public ImageFaceGroupResponse setGroupCoverWidth(Long groupCoverWidth) {
        this.groupCoverWidth = groupCoverWidth;
        return this;
    }
    public Long getGroupCoverWidth() {
        return this.groupCoverWidth;
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

    public ImageFaceGroupResponse setRemarks(String remarks) {
        this.remarks = remarks;
        return this;
    }
    public String getRemarks() {
        return this.remarks;
    }

    public ImageFaceGroupResponse setRemarksArray(java.util.List<String> remarksArray) {
        this.remarksArray = remarksArray;
        return this;
    }
    public java.util.List<String> getRemarksArray() {
        return this.remarksArray;
    }

    public ImageFaceGroupResponse setUpdatedAt(String updatedAt) {
        this.updatedAt = updatedAt;
        return this;
    }
    public String getUpdatedAt() {
        return this.updatedAt;
    }

}
