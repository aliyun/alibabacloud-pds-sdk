// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 视频转码参数
 */
public class VideoPreviewVideo extends TeaModel {
    @NameInMap("height")
    public Long height;

    @NameInMap("keep_original")
    public Boolean keepOriginal;

    @NameInMap("video_bitrate")
    public Long videoBitrate;

    @NameInMap("video_codec")
    public String videoCodec;

    @NameInMap("video_frame_rate")
    public Long videoFrameRate;

    @NameInMap("width")
    public Long width;

    public static VideoPreviewVideo build(java.util.Map<String, ?> map) throws Exception {
        VideoPreviewVideo self = new VideoPreviewVideo();
        return TeaModel.build(map, self);
    }

    public VideoPreviewVideo setHeight(Long height) {
        this.height = height;
        return this;
    }
    public Long getHeight() {
        return this.height;
    }

    public VideoPreviewVideo setKeepOriginal(Boolean keepOriginal) {
        this.keepOriginal = keepOriginal;
        return this;
    }
    public Boolean getKeepOriginal() {
        return this.keepOriginal;
    }

    public VideoPreviewVideo setVideoBitrate(Long videoBitrate) {
        this.videoBitrate = videoBitrate;
        return this;
    }
    public Long getVideoBitrate() {
        return this.videoBitrate;
    }

    public VideoPreviewVideo setVideoCodec(String videoCodec) {
        this.videoCodec = videoCodec;
        return this;
    }
    public String getVideoCodec() {
        return this.videoCodec;
    }

    public VideoPreviewVideo setVideoFrameRate(Long videoFrameRate) {
        this.videoFrameRate = videoFrameRate;
        return this;
    }
    public Long getVideoFrameRate() {
        return this.videoFrameRate;
    }

    public VideoPreviewVideo setWidth(Long width) {
        this.width = width;
        return this;
    }
    public Long getWidth() {
        return this.width;
    }

}
