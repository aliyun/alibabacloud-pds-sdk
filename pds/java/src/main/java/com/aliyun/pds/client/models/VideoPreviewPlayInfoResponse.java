// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 转码信息响应
 */
public class VideoPreviewPlayInfoResponse extends TeaModel {
    /**
     * <p>deprecated, 使用外层Response中的同名字段替代</p>
     * <p>category，此字段为保持兼容而继续存在</p>
     */
    @NameInMap("category")
    public String category;

    @NameInMap("live_transcoding_subtitle_task_list")
    public java.util.List<LiveTranscodingSubtitleTaskResponse> liveTranscodingSubtitleTaskList;

    /**
     * <p>边转边播有效</p>
     */
    @NameInMap("live_transcoding_task_list")
    public java.util.List<LiveTranscodingTaskResponse> liveTranscodingTaskList;

    @NameInMap("meta")
    public VideoPreviewPlayInfoMetaResponse meta;

    /**
     * <p>离线转码有效</p>
     */
    @NameInMap("offline_video_transcoding_list")
    public java.util.List<VideoPreviewOfflineVideoTranscodingTaskResponse> offlineVideoTranscodingList;

    /**
     * <p>imm边转边播</p>
     */
    @NameInMap("quick_video_list")
    public java.util.List<QuickVideoTaskResponse> quickVideoList;

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

    public VideoPreviewPlayInfoResponse setQuickVideoList(java.util.List<QuickVideoTaskResponse> quickVideoList) {
        this.quickVideoList = quickVideoList;
        return this;
    }
    public java.util.List<QuickVideoTaskResponse> getQuickVideoList() {
        return this.quickVideoList;
    }

}
