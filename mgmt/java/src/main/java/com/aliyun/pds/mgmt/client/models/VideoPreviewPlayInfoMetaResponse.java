// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 获取转码信息meta响应
 */
public class VideoPreviewPlayInfoMetaResponse extends TeaModel {
    // duration, 视频长度
    @NameInMap("duration")
    public Double duration;

    // height, 视频高度
    @NameInMap("height")
    public Long height;

    @NameInMap("live_transcoding_meta")
    public LiveTranscodingMetaResponse liveTranscodingMeta;

    // width, 视频宽度
    @NameInMap("width")
    public Long width;

    public static VideoPreviewPlayInfoMetaResponse build(java.util.Map<String, ?> map) throws Exception {
        VideoPreviewPlayInfoMetaResponse self = new VideoPreviewPlayInfoMetaResponse();
        return TeaModel.build(map, self);
    }

    public VideoPreviewPlayInfoMetaResponse setDuration(Double duration) {
        this.duration = duration;
        return this;
    }
    public Double getDuration() {
        return this.duration;
    }

    public VideoPreviewPlayInfoMetaResponse setHeight(Long height) {
        this.height = height;
        return this;
    }
    public Long getHeight() {
        return this.height;
    }

    public VideoPreviewPlayInfoMetaResponse setLiveTranscodingMeta(LiveTranscodingMetaResponse liveTranscodingMeta) {
        this.liveTranscodingMeta = liveTranscodingMeta;
        return this;
    }
    public LiveTranscodingMetaResponse getLiveTranscodingMeta() {
        return this.liveTranscodingMeta;
    }

    public VideoPreviewPlayInfoMetaResponse setWidth(Long width) {
        this.width = width;
        return this;
    }
    public Long getWidth() {
        return this.width;
    }

}
