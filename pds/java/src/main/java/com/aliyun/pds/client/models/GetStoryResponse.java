// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 生成故事
 */
public class GetStoryResponse extends TeaModel {
    // cover_file_id
    @NameInMap("cover_file_id")
    public String coverFileId;

    // cover_file_url
    @NameInMap("cover_file_thumbnail_url")
    public String coverFileThumbnailUrl;

    // created_at
    @NameInMap("created_at")
    public String createdAt;

    // event_type
    @NameInMap("event_type")
    public String eventType;

    // face_group_ids
    @NameInMap("face_group_ids")
    public java.util.List<String> faceGroupIds;

    // story_end_time
    @NameInMap("story_end_time")
    public String storyEndTime;

    @NameInMap("story_file_list")
    public java.util.List<BaseCCPFileResponse> storyFileList;

    // story_id
    @NameInMap("story_id")
    public String storyId;

    // story_name
    @NameInMap("story_name")
    public String storyName;

    // story_start_time
    @NameInMap("story_start_time")
    public String storyStartTime;

    // story_type
    @NameInMap("story_type")
    public String storyType;

    // updated_at
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

    public GetStoryResponse setEventType(String eventType) {
        this.eventType = eventType;
        return this;
    }
    public String getEventType() {
        return this.eventType;
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
