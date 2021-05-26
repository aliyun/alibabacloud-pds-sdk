// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 获取分享中文件下载地址的请求body
 */
public class GetShareLinkDownloadURLRequest extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // addition_data
    @NameInMap("addition_data")
    public java.util.Map<String, ?> additionData;

    // expire_sec
    @NameInMap("expire_sec")
    @Validation(maximum = 600, minimum = 1)
    public Long expireSec;

    // file_id
    @NameInMap("file_id")
    @Validation(required = true, pattern = "[a-z0-9.-_]{1,50}", maxLength = 50, minLength = 40)
    public String fileId;

    @NameInMap("file_id_path")
    public String fileIdPath;

    // get_audio_play_info
    @NameInMap("get_audio_play_info")
    public Boolean getAudioPlayInfo;

    // get_video_play_info
    @NameInMap("get_video_play_info")
    public Boolean getVideoPlayInfo;

    // image_thumbnail_process
    @NameInMap("image_thumbnail_process")
    public String imageThumbnailProcess;

    // image_url_process
    @NameInMap("image_url_process")
    public String imageUrlProcess;

    // location
    @NameInMap("location")
    public String location;

    // office_thumbnail_process
    @NameInMap("office_thumbnail_process")
    public String officeThumbnailProcess;

    @NameInMap("referer")
    public String referer;

    // share_id is required
    @NameInMap("share_id")
    @Validation(required = true)
    public String shareId;

    @NameInMap("sign_token")
    public String signToken;

    // video_thumbnail_process
    // type:string
    @NameInMap("video_thumbnail_process")
    public String videoThumbnailProcess;

    public static GetShareLinkDownloadURLRequest build(java.util.Map<String, ?> map) throws Exception {
        GetShareLinkDownloadURLRequest self = new GetShareLinkDownloadURLRequest();
        return TeaModel.build(map, self);
    }

    public GetShareLinkDownloadURLRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetShareLinkDownloadURLRequest setAdditionData(java.util.Map<String, ?> additionData) {
        this.additionData = additionData;
        return this;
    }
    public java.util.Map<String, ?> getAdditionData() {
        return this.additionData;
    }

    public GetShareLinkDownloadURLRequest setExpireSec(Long expireSec) {
        this.expireSec = expireSec;
        return this;
    }
    public Long getExpireSec() {
        return this.expireSec;
    }

    public GetShareLinkDownloadURLRequest setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

    public GetShareLinkDownloadURLRequest setFileIdPath(String fileIdPath) {
        this.fileIdPath = fileIdPath;
        return this;
    }
    public String getFileIdPath() {
        return this.fileIdPath;
    }

    public GetShareLinkDownloadURLRequest setGetAudioPlayInfo(Boolean getAudioPlayInfo) {
        this.getAudioPlayInfo = getAudioPlayInfo;
        return this;
    }
    public Boolean getGetAudioPlayInfo() {
        return this.getAudioPlayInfo;
    }

    public GetShareLinkDownloadURLRequest setGetVideoPlayInfo(Boolean getVideoPlayInfo) {
        this.getVideoPlayInfo = getVideoPlayInfo;
        return this;
    }
    public Boolean getGetVideoPlayInfo() {
        return this.getVideoPlayInfo;
    }

    public GetShareLinkDownloadURLRequest setImageThumbnailProcess(String imageThumbnailProcess) {
        this.imageThumbnailProcess = imageThumbnailProcess;
        return this;
    }
    public String getImageThumbnailProcess() {
        return this.imageThumbnailProcess;
    }

    public GetShareLinkDownloadURLRequest setImageUrlProcess(String imageUrlProcess) {
        this.imageUrlProcess = imageUrlProcess;
        return this;
    }
    public String getImageUrlProcess() {
        return this.imageUrlProcess;
    }

    public GetShareLinkDownloadURLRequest setLocation(String location) {
        this.location = location;
        return this;
    }
    public String getLocation() {
        return this.location;
    }

    public GetShareLinkDownloadURLRequest setOfficeThumbnailProcess(String officeThumbnailProcess) {
        this.officeThumbnailProcess = officeThumbnailProcess;
        return this;
    }
    public String getOfficeThumbnailProcess() {
        return this.officeThumbnailProcess;
    }

    public GetShareLinkDownloadURLRequest setReferer(String referer) {
        this.referer = referer;
        return this;
    }
    public String getReferer() {
        return this.referer;
    }

    public GetShareLinkDownloadURLRequest setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

    public GetShareLinkDownloadURLRequest setSignToken(String signToken) {
        this.signToken = signToken;
        return this;
    }
    public String getSignToken() {
        return this.signToken;
    }

    public GetShareLinkDownloadURLRequest setVideoThumbnailProcess(String videoThumbnailProcess) {
        this.videoThumbnailProcess = videoThumbnailProcess;
        return this;
    }
    public String getVideoThumbnailProcess() {
        return this.videoThumbnailProcess;
    }

}
