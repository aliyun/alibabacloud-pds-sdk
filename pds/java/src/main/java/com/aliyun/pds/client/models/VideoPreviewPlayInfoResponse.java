// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 转码信息响应
 */
public class VideoPreviewPlayInfoResponse extends TeaModel {
    // category
    @NameInMap("category")
    public String category;

    @NameInMap("live_transcoding_subtitle_task_list")
    public java.util.List<LiveTranscodingSubtitleTaskResponse> liveTranscodingSubtitleTaskList;

    // 边转边播有效
    @NameInMap("live_transcoding_task_list")
    public java.util.List<LiveTranscodingTaskResponse> liveTranscodingTaskList;

    @NameInMap("meta")
    public VideoPreviewPlayInfoMetaResponse meta;

    // 离线转码有效
    @NameInMap("offline_video_transcoding_list")
    public java.util.List<VideoPreviewOfflineVideoTranscodingTaskResponse> offlineVideoTranscodingList;

    public static VideoPreviewPlayInfoResponse build(java.util.Map<String, ?> map) throws Exception {
        VideoPreviewPlayInfoResponse self = new VideoPreviewPlayInfoResponse();
        return TeaModel.build(map, self);
    }

    public VideoPreviewPlayInfoResponse setCategory(String category) {
        this.category = category;
        return this;
    }
    public String getCategory() {
        return this.category;
    }

    public VideoPreviewPlayInfoResponse setLiveTranscodingSubtitleTaskList(java.util.List<LiveTranscodingSubtitleTaskResponse> liveTranscodingSubtitleTaskList) {
        this.liveTranscodingSubtitleTaskList = liveTranscodingSubtitleTaskList;
        return this;
    }
    public java.util.List<LiveTranscodingSubtitleTaskResponse> getLiveTranscodingSubtitleTaskList() {
        return this.liveTranscodingSubtitleTaskList;
    }

    public VideoPreviewPlayInfoResponse setLiveTranscodingTaskList(java.util.List<LiveTranscodingTaskResponse> liveTranscodingTaskList) {
        this.liveTranscodingTaskList = liveTranscodingTaskList;
        return this;
    }
    public java.util.List<LiveTranscodingTaskResponse> getLiveTranscodingTaskList() {
        return this.liveTranscodingTaskList;
    }

    public VideoPreviewPlayInfoResponse setMeta(VideoPreviewPlayInfoMetaResponse meta) {
        this.meta = meta;
        return this;
    }
    public VideoPreviewPlayInfoMetaResponse getMeta() {
        return this.meta;
    }

    public VideoPreviewPlayInfoResponse setOfflineVideoTranscodingList(java.util.List<VideoPreviewOfflineVideoTranscodingTaskResponse> offlineVideoTranscodingList) {
        this.offlineVideoTranscodingList = offlineVideoTranscodingList;
        return this;
    }
    public java.util.List<VideoPreviewOfflineVideoTranscodingTaskResponse> getOfflineVideoTranscodingList() {
        return this.offlineVideoTranscodingList;
    }

}
