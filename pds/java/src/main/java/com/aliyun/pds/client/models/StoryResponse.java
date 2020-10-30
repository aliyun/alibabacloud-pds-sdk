// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class StoryResponse extends TeaModel {
    // cover_file_id
    @NameInMap("cover_file_id")
    public String coverFileId;

    // created_at
    @NameInMap("created_at")
    public String createdAt;

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

    public static StoryResponse build(java.util.Map<String, ?> map) throws Exception {
        StoryResponse self = new StoryResponse();
        return TeaModel.build(map, self);
    }

    public StoryResponse setCoverFileId(String coverFileId) {
        this.coverFileId = coverFileId;
        return this;
    }
    public String getCoverFileId() {
        return this.coverFileId;
    }

    public StoryResponse setCreatedAt(String createdAt) {
        this.createdAt = createdAt;
        return this;
    }
    public String getCreatedAt() {
        return this.createdAt;
    }

    public StoryResponse setScore(Double score) {
        this.score = score;
        return this;
    }
    public Double getScore() {
        return this.score;
    }

    public StoryResponse setStoryId(String storyId) {
        this.storyId = storyId;
        return this;
    }
    public String getStoryId() {
        return this.storyId;
    }

    public StoryResponse setStoryImagesDateRange(java.util.List<Integer> storyImagesDateRange) {
        this.storyImagesDateRange = storyImagesDateRange;
        return this;
    }
    public java.util.List<Integer> getStoryImagesDateRange() {
        return this.storyImagesDateRange;
    }

    public StoryResponse setSubTitle(String subTitle) {
        this.subTitle = subTitle;
        return this;
    }
    public String getSubTitle() {
        return this.subTitle;
    }

    public StoryResponse setTitle(String title) {
        this.title = title;
        return this;
    }
    public String getTitle() {
        return this.title;
    }

    public StoryResponse setUpdatedAt(String updatedAt) {
        this.updatedAt = updatedAt;
        return this;
    }
    public String getUpdatedAt() {
        return this.updatedAt;
    }

    public StoryResponse setVideoStatus(String videoStatus) {
        this.videoStatus = videoStatus;
        return this;
    }
    public String getVideoStatus() {
        return this.videoStatus;
    }

    public StoryResponse setVideoUrl(String videoUrl) {
        this.videoUrl = videoUrl;
        return this;
    }
    public String getVideoUrl() {
        return this.videoUrl;
    }

}
