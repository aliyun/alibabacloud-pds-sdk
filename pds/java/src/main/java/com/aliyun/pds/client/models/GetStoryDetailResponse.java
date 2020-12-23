// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 故事详情
 */
public class GetStoryDetailResponse extends TeaModel {
    // cover_file_id
    @NameInMap("cover_file_id")
    public String coverFileId;

    // created_at
    @NameInMap("created_at")
    public String createdAt;

    // items
    @NameInMap("items")
    public java.util.List<BaseCCPFileResponse> items;

    // score
    @NameInMap("score")
    public Double score;

    // story_id
    @NameInMap("story_id")
    public String storyId;

    // story_images_date_range
    @NameInMap("story_images_date_range")
    public java.util.List<Integer> storyImagesDateRange;

    // sub_title
    @NameInMap("sub_title")
    public String subTitle;

    // title
    @NameInMap("title")
    public String title;

    // updated_at
    @NameInMap("updated_at")
    public String updatedAt;

    // video_status
    @NameInMap("video_status")
    public String videoStatus;

    // video_url
    @NameInMap("video_url")
    public String videoUrl;

    public static GetStoryDetailResponse build(java.util.Map<String, ?> map) throws Exception {
        GetStoryDetailResponse self = new GetStoryDetailResponse();
        return TeaModel.build(map, self);
    }

    public GetStoryDetailResponse setCoverFileId(String coverFileId) {
        this.coverFileId = coverFileId;
        return this;
    }
    public String getCoverFileId() {
        return this.coverFileId;
    }

    public GetStoryDetailResponse setCreatedAt(String createdAt) {
        this.createdAt = createdAt;
        return this;
    }
    public String getCreatedAt() {
        return this.createdAt;
    }

    public GetStoryDetailResponse setItems(java.util.List<BaseCCPFileResponse> items) {
        this.items = items;
        return this;
    }
    public java.util.List<BaseCCPFileResponse> getItems() {
        return this.items;
    }

    public GetStoryDetailResponse setScore(Double score) {
        this.score = score;
        return this;
    }
    public Double getScore() {
        return this.score;
    }

    public GetStoryDetailResponse setStoryId(String storyId) {
        this.storyId = storyId;
        return this;
    }
    public String getStoryId() {
        return this.storyId;
    }

    public GetStoryDetailResponse setStoryImagesDateRange(java.util.List<Integer> storyImagesDateRange) {
        this.storyImagesDateRange = storyImagesDateRange;
        return this;
    }
    public java.util.List<Integer> getStoryImagesDateRange() {
        return this.storyImagesDateRange;
    }

    public GetStoryDetailResponse setSubTitle(String subTitle) {
        this.subTitle = subTitle;
        return this;
    }
    public String getSubTitle() {
        return this.subTitle;
    }

    public GetStoryDetailResponse setTitle(String title) {
        this.title = title;
        return this;
    }
    public String getTitle() {
        return this.title;
    }

    public GetStoryDetailResponse setUpdatedAt(String updatedAt) {
        this.updatedAt = updatedAt;
        return this;
    }
    public String getUpdatedAt() {
        return this.updatedAt;
    }

    public GetStoryDetailResponse setVideoStatus(String videoStatus) {
        this.videoStatus = videoStatus;
        return this;
    }
    public String getVideoStatus() {
        return this.videoStatus;
    }

    public GetStoryDetailResponse setVideoUrl(String videoUrl) {
        this.videoUrl = videoUrl;
        return this;
    }
    public String getVideoUrl() {
        return this.videoUrl;
    }

}
