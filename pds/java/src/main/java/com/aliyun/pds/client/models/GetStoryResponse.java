// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 生成故事
 */
public class GetStoryResponse extends TeaModel {
    /**
     * <p>cover_file_id</p>
     */
    @NameInMap("cover_file_id")
    public String coverFileId;

    /**
     * <p>cover_file_url</p>
     */
    @NameInMap("cover_file_thumbnail_url")
    public String coverFileThumbnailUrl;

    /**
     * <p>created_at</p>
     */
    @NameInMap("created_at")
    public String createdAt;

    /**
     * <p>custom_id</p>
     */
    @NameInMap("custom_id")
    public String customId;

    /**
     * <p>custom_labels</p>
     */
    @NameInMap("custom_labels")
    public java.util.Map<String, ?> customLabels;

    /**
     * <p>face_group_ids</p>
     */
    @NameInMap("face_group_ids")
    public java.util.List<String> faceGroupIds;

    /**
     * <p>story_end_time</p>
     */
    @NameInMap("story_end_time")
    public String storyEndTime;

    @NameInMap("story_file_list")
    public java.util.List<BaseCCPFileResponse> storyFileList;

    /**
     * <p>story_id</p>
     */
    @NameInMap("story_id")
    public String storyId;

    /**
     * <p>story_name</p>
     */
    @NameInMap("story_name")
    public String storyName;

    /**
     * <p>story_start_time</p>
     */
    @NameInMap("story_start_time")
    public String storyStartTime;

    /**
     * <p>story_sub_type</p>
     */
    @NameInMap("story_sub_type")
    public String storySubType;

    /**
     * <p>story_type</p>
     */
    @NameInMap("story_type")
    public String storyType;

    /**
     * <p>updated_at</p>
     */
    @NameInMap("updated_at")
    public String updatedAt;

    public static GetStoryResponse build(java.util.Map<String, ?> map) throws Exception {
        GetStoryResponse self = new GetStoryResponse();
        return TeaModel.build(map, self);
    }

    public GetStoryResponse setCoverFileId(String coverFileId) {
        this.coverFileId = coverFileId;
        return this;
    }
    public String getCoverFileId() {
        return this.coverFileId;
    }

    public GetStoryResponse setCoverFileThumbnailUrl(String coverFileThumbnailUrl) {
        this.coverFileThumbnailUrl = coverFileThumbnailUrl;
        return this;
    }
    public String getCoverFileThumbnailUrl() {
        return this.coverFileThumbnailUrl;
    }

    public GetStoryResponse setCreatedAt(String createdAt) {
        this.createdAt = createdAt;
        return this;
    }
    public String getCreatedAt() {
        return this.createdAt;
    }

    public GetStoryResponse setCustomId(String customId) {
        this.customId = customId;
        return this;
    }
    public String getCustomId() {
        return this.customId;
    }

    public GetStoryResponse setCustomLabels(java.util.Map<String, ?> customLabels) {
        this.customLabels = customLabels;
        return this;
    }
    public java.util.Map<String, ?> getCustomLabels() {
        return this.customLabels;
    }

    public GetStoryResponse setFaceGroupIds(java.util.List<String> faceGroupIds) {
        this.faceGroupIds = faceGroupIds;
        return this;
    }
    public java.util.List<String> getFaceGroupIds() {
        return this.faceGroupIds;
    }

    public GetStoryResponse setStoryEndTime(String storyEndTime) {
        this.storyEndTime = storyEndTime;
        return this;
    }
    public String getStoryEndTime() {
        return this.storyEndTime;
    }

    public GetStoryResponse setStoryFileList(java.util.List<BaseCCPFileResponse> storyFileList) {
        this.storyFileList = storyFileList;
        return this;
    }
    public java.util.List<BaseCCPFileResponse> getStoryFileList() {
        return this.storyFileList;
    }

    public GetStoryResponse setStoryId(String storyId) {
        this.storyId = storyId;
        return this;
    }
    public String getStoryId() {
        return this.storyId;
    }

    public GetStoryResponse setStoryName(String storyName) {
        this.storyName = storyName;
        return this;
    }
    public String getStoryName() {
        return this.storyName;
    }

    public GetStoryResponse setStoryStartTime(String storyStartTime) {
        this.storyStartTime = storyStartTime;
        return this;
    }
    public String getStoryStartTime() {
        return this.storyStartTime;
    }

    public GetStoryResponse setStorySubType(String storySubType) {
        this.storySubType = storySubType;
        return this;
    }
    public String getStorySubType() {
        return this.storySubType;
    }

    public GetStoryResponse setStoryType(String storyType) {
        this.storyType = storyType;
        return this;
    }
    public String getStoryType() {
        return this.storyType;
    }

    public GetStoryResponse setUpdatedAt(String updatedAt) {
        this.updatedAt = updatedAt;
        return this;
    }
    public String getUpdatedAt() {
        return this.updatedAt;
    }

}
