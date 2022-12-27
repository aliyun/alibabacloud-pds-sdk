// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 获取转码信息响应
 */
public class CCPGetVideoPreviewPlayInfoResponse extends TeaModel {
    @NameInMap("audio_preview_play_info")
    public AudioPreviewPlayInfoResponse audioPreviewPlayInfo;

    // category
    @NameInMap("category")
    public String category;

    // domain_id
    @NameInMap("domain_id")
    @Validation(pattern = "[a-z0-9A-Z]+")
    public String domainId;

    // drive_id
    @NameInMap("drive_id")
    @Validation(pattern = "[0-9]+")
    public String driveId;

    // file_id
    @NameInMap("file_id")
    @Validation(pattern = "[a-z0-9]{1,50}", maxLength = 50, minLength = 40)
    public String fileId;

    // share_id
    @NameInMap("share_id")
    public String shareId;

    @NameInMap("video_preview_play_info")
    public VideoPreviewPlayInfoResponse videoPreviewPlayInfo;

    public static CCPGetVideoPreviewPlayInfoResponse build(java.util.Map<String, ?> map) throws Exception {
        CCPGetVideoPreviewPlayInfoResponse self = new CCPGetVideoPreviewPlayInfoResponse();
        return TeaModel.build(map, self);
    }

    public CCPGetVideoPreviewPlayInfoResponse setAudioPreviewPlayInfo(AudioPreviewPlayInfoResponse audioPreviewPlayInfo) {
        this.audioPreviewPlayInfo = audioPreviewPlayInfo;
        return this;
    }
    public AudioPreviewPlayInfoResponse getAudioPreviewPlayInfo() {
        return this.audioPreviewPlayInfo;
    }

    public CCPGetVideoPreviewPlayInfoResponse setCategory(String category) {
        this.category = category;
        return this;
    }
    public String getCategory() {
        return this.category;
    }

    public CCPGetVideoPreviewPlayInfoResponse setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public CCPGetVideoPreviewPlayInfoResponse setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public CCPGetVideoPreviewPlayInfoResponse setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

    public CCPGetVideoPreviewPlayInfoResponse setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

    public CCPGetVideoPreviewPlayInfoResponse setVideoPreviewPlayInfo(VideoPreviewPlayInfoResponse videoPreviewPlayInfo) {
        this.videoPreviewPlayInfo = videoPreviewPlayInfo;
        return this;
    }
    public VideoPreviewPlayInfoResponse getVideoPreviewPlayInfo() {
        return this.videoPreviewPlayInfo;
    }

}
