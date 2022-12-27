// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 获取分享中媒体播放地址response
 */
public class CCPGetShareLinkVideoPreviewPlayInfoResponse extends TeaModel {
    @NameInMap("audio_preview_play_info")
    public AudioPreviewPlayInfoResponse audioPreviewPlayInfo;

    // category
    @NameInMap("category")
    public String category;

    // file_id
    @NameInMap("file_id")
    @Validation(pattern = "[a-z0-9]{1,50}", maxLength = 50, minLength = 40)
    public String fileId;

    // share_id
    @NameInMap("share_id")
    public String shareId;

    @NameInMap("video_preview_play_info")
    public VideoPreviewPlayInfoResponse videoPreviewPlayInfo;

    public static CCPGetShareLinkVideoPreviewPlayInfoResponse build(java.util.Map<String, ?> map) throws Exception {
        CCPGetShareLinkVideoPreviewPlayInfoResponse self = new CCPGetShareLinkVideoPreviewPlayInfoResponse();
        return TeaModel.build(map, self);
    }

    public CCPGetShareLinkVideoPreviewPlayInfoResponse setAudioPreviewPlayInfo(AudioPreviewPlayInfoResponse audioPreviewPlayInfo) {
        this.audioPreviewPlayInfo = audioPreviewPlayInfo;
        return this;
    }
    public AudioPreviewPlayInfoResponse getAudioPreviewPlayInfo() {
        return this.audioPreviewPlayInfo;
    }

    public CCPGetShareLinkVideoPreviewPlayInfoResponse setCategory(String category) {
        this.category = category;
        return this;
    }
    public String getCategory() {
        return this.category;
    }

    public CCPGetShareLinkVideoPreviewPlayInfoResponse setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

    public CCPGetShareLinkVideoPreviewPlayInfoResponse setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

    public CCPGetShareLinkVideoPreviewPlayInfoResponse setVideoPreviewPlayInfo(VideoPreviewPlayInfoResponse videoPreviewPlayInfo) {
        this.videoPreviewPlayInfo = videoPreviewPlayInfo;
        return this;
    }
    public VideoPreviewPlayInfoResponse getVideoPreviewPlayInfo() {
        return this.videoPreviewPlayInfo;
    }

}
