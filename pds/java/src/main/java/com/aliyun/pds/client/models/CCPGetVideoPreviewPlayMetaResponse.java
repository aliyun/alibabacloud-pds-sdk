// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 获取播放元信息响应
 */
public class CCPGetVideoPreviewPlayMetaResponse extends TeaModel {
    @NameInMap("audio_preview_play_meta")
    public AudioPreviewPlayInfoResponse audioPreviewPlayMeta;

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

    @NameInMap("video_preview_play_meta")
    public VideoPreviewPlayInfoResponse videoPreviewPlayMeta;

    public static CCPGetVideoPreviewPlayMetaResponse build(java.util.Map<String, ?> map) throws Exception {
        CCPGetVideoPreviewPlayMetaResponse self = new CCPGetVideoPreviewPlayMetaResponse();
        return TeaModel.build(map, self);
    }

    public CCPGetVideoPreviewPlayMetaResponse setAudioPreviewPlayMeta(AudioPreviewPlayInfoResponse audioPreviewPlayMeta) {
        this.audioPreviewPlayMeta = audioPreviewPlayMeta;
        return this;
    }
    public AudioPreviewPlayInfoResponse getAudioPreviewPlayMeta() {
        return this.audioPreviewPlayMeta;
    }

    public CCPGetVideoPreviewPlayMetaResponse setCategory(String category) {
        this.category = category;
        return this;
    }
    public String getCategory() {
        return this.category;
    }

    public CCPGetVideoPreviewPlayMetaResponse setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public CCPGetVideoPreviewPlayMetaResponse setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public CCPGetVideoPreviewPlayMetaResponse setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

    public CCPGetVideoPreviewPlayMetaResponse setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

    public CCPGetVideoPreviewPlayMetaResponse setVideoPreviewPlayMeta(VideoPreviewPlayInfoResponse videoPreviewPlayMeta) {
        this.videoPreviewPlayMeta = videoPreviewPlayMeta;
        return this;
    }
    public VideoPreviewPlayInfoResponse getVideoPreviewPlayMeta() {
        return this.videoPreviewPlayMeta;
    }

}
