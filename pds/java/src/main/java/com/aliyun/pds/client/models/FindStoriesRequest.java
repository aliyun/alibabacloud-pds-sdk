// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * find story request
 */
public class FindStoriesRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    // cover_image_thumbnail_process
    @NameInMap("cover_image_thumbnail_process")
    public String coverImageThumbnailProcess;

    // cover_video_thumbnail_process
    @NameInMap("cover_video_thumbnail_process")
    public String coverVideoThumbnailProcess;

    @NameInMap("create_time_range")
    public FindStoryRequestTimeRange createTimeRange;

    // drive_id
    @NameInMap("drive_id")
    @Validation(required = true, pattern = "[0-9]+")
    public String driveId;

    // face_group_ids
    @NameInMap("face_group_ids")
    public java.util.List<String> faceGroupIds;

    // limit
    @NameInMap("limit")
    public Long limit;

    // marker
    @NameInMap("marker")
    public String marker;

    @NameInMap("story_end_time_range")
    public FindStoryRequestTimeRange storyEndTimeRange;

    // story_id
    @NameInMap("story_id")
    public String storyId;

    // story_name
    @NameInMap("story_name")
    public String storyName;

    @NameInMap("story_start_time_range")
    public FindStoryRequestTimeRange storyStartTimeRange;

    // story_type
    @NameInMap("story_type")
    public String storyType;

    // url_expire_sec
    @NameInMap("url_expire_sec")
    public Long urlExpireSec;

    public static FindStoriesRequest build(java.util.Map<String, ?> map) throws Exception {
        FindStoriesRequest self = new FindStoriesRequest();
        return TeaModel.build(map, self);
    }

    public FindStoriesRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public FindStoriesRequest setCoverImageThumbnailProcess(String coverImageThumbnailProcess) {
        this.coverImageThumbnailProcess = coverImageThumbnailProcess;
        return this;
    }
    public String getCoverImageThumbnailProcess() {
        return this.coverImageThumbnailProcess;
    }

    public FindStoriesRequest setCoverVideoThumbnailProcess(String coverVideoThumbnailProcess) {
        this.coverVideoThumbnailProcess = coverVideoThumbnailProcess;
        return this;
    }
    public String getCoverVideoThumbnailProcess() {
        return this.coverVideoThumbnailProcess;
    }

    public FindStoriesRequest setCreateTimeRange(FindStoryRequestTimeRange createTimeRange) {
        this.createTimeRange = createTimeRange;
        return this;
    }
    public FindStoryRequestTimeRange getCreateTimeRange() {
        return this.createTimeRange;
    }

    public FindStoriesRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public FindStoriesRequest setFaceGroupIds(java.util.List<String> faceGroupIds) {
        this.faceGroupIds = faceGroupIds;
        return this;
    }
    public java.util.List<String> getFaceGroupIds() {
        return this.faceGroupIds;
    }

    public FindStoriesRequest setLimit(Long limit) {
        this.limit = limit;
        return this;
    }
    public Long getLimit() {
        return this.limit;
    }

    public FindStoriesRequest setMarker(String marker) {
        this.marker = marker;
        return this;
    }
    public String getMarker() {
        return this.marker;
    }

    public FindStoriesRequest setStoryEndTimeRange(FindStoryRequestTimeRange storyEndTimeRange) {
        this.storyEndTimeRange = storyEndTimeRange;
        return this;
    }
    public FindStoryRequestTimeRange getStoryEndTimeRange() {
        return this.storyEndTimeRange;
    }

    public FindStoriesRequest setStoryId(String storyId) {
        this.storyId = storyId;
        return this;
    }
    public String getStoryId() {
        return this.storyId;
    }

    public FindStoriesRequest setStoryName(String storyName) {
        this.storyName = storyName;
        return this;
    }
    public String getStoryName() {
        return this.storyName;
    }

    public FindStoriesRequest setStoryStartTimeRange(FindStoryRequestTimeRange storyStartTimeRange) {
        this.storyStartTimeRange = storyStartTimeRange;
        return this;
    }
    public FindStoryRequestTimeRange getStoryStartTimeRange() {
        return this.storyStartTimeRange;
    }

    public FindStoriesRequest setStoryType(String storyType) {
        this.storyType = storyType;
        return this;
    }
    public String getStoryType() {
        return this.storyType;
    }

    public FindStoriesRequest setUrlExpireSec(Long urlExpireSec) {
        this.urlExpireSec = urlExpireSec;
        return this;
    }
    public Long getUrlExpireSec() {
        return this.urlExpireSec;
    }

}
