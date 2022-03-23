// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 获取分享中文件媒体播放地址的请求body
 */
public class CCPGetShareLinkVideoPreviewPlayInfoRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    // addition_data
    @NameInMap("addition_data")
    public java.util.Map<String, ?> additionData;

    // category
    @NameInMap("category")
    public String category;

    // drive_id
    @NameInMap("drive_id")
    @Validation(required = true, pattern = "[0-9]+")
    public String driveId;

    // file_id
    @NameInMap("file_id")
    @Validation(pattern = "[a-z0-9.-_]{1,50}", maxLength = 50, minLength = 40)
    public String fileId;

    @NameInMap("file_id_path")
    public String fileIdPath;

    // get_preview_url
    @NameInMap("get_preview_url")
    public Boolean getPreviewUrl;

    // get_subtitle_info
    @NameInMap("get_subtitle_info")
    public Boolean getSubtitleInfo;

    // get_without_url
    @NameInMap("get_without_url")
    public Boolean getWithoutUrl;

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

    // subtitle_language_list, 根据语言获取压制在视频中的字幕, 不传则取所有
    @NameInMap("subtitle_language_list")
    public java.util.List<String> subtitleLanguageList;

    // template_id
    @NameInMap("template_id")
    public String templateId;

    // url_expire_sec
    @NameInMap("url_expire_sec")
    @Validation(maximum = 600, minimum = 10)
    public Long urlExpireSec;

    // video_thumbnail_process
    // type:string
    @NameInMap("video_thumbnail_process")
    public String videoThumbnailProcess;

    public static CCPGetShareLinkVideoPreviewPlayInfoRequest build(java.util.Map<String, ?> map) throws Exception {
        CCPGetShareLinkVideoPreviewPlayInfoRequest self = new CCPGetShareLinkVideoPreviewPlayInfoRequest();
        return TeaModel.build(map, self);
    }

    public CCPGetShareLinkVideoPreviewPlayInfoRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public CCPGetShareLinkVideoPreviewPlayInfoRequest setAdditionData(java.util.Map<String, ?> additionData) {
        this.additionData = additionData;
        return this;
    }
    public java.util.Map<String, ?> getAdditionData() {
        return this.additionData;
    }

    public CCPGetShareLinkVideoPreviewPlayInfoRequest setCategory(String category) {
        this.category = category;
        return this;
    }
    public String getCategory() {
        return this.category;
    }

    public CCPGetShareLinkVideoPreviewPlayInfoRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public CCPGetShareLinkVideoPreviewPlayInfoRequest setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

    public CCPGetShareLinkVideoPreviewPlayInfoRequest setFileIdPath(String fileIdPath) {
        this.fileIdPath = fileIdPath;
        return this;
    }
    public String getFileIdPath() {
        return this.fileIdPath;
    }

    public CCPGetShareLinkVideoPreviewPlayInfoRequest setGetPreviewUrl(Boolean getPreviewUrl) {
        this.getPreviewUrl = getPreviewUrl;
        return this;
    }
    public Boolean getGetPreviewUrl() {
        return this.getPreviewUrl;
    }

    public CCPGetShareLinkVideoPreviewPlayInfoRequest setGetSubtitleInfo(Boolean getSubtitleInfo) {
        this.getSubtitleInfo = getSubtitleInfo;
        return this;
    }
    public Boolean getGetSubtitleInfo() {
        return this.getSubtitleInfo;
    }

    public CCPGetShareLinkVideoPreviewPlayInfoRequest setGetWithoutUrl(Boolean getWithoutUrl) {
        this.getWithoutUrl = getWithoutUrl;
        return this;
    }
    public Boolean getGetWithoutUrl() {
        return this.getWithoutUrl;
    }

    public CCPGetShareLinkVideoPreviewPlayInfoRequest setImageThumbnailProcess(String imageThumbnailProcess) {
        this.imageThumbnailProcess = imageThumbnailProcess;
        return this;
    }
    public String getImageThumbnailProcess() {
        return this.imageThumbnailProcess;
    }

    public CCPGetShareLinkVideoPreviewPlayInfoRequest setImageUrlProcess(String imageUrlProcess) {
        this.imageUrlProcess = imageUrlProcess;
        return this;
    }
    public String getImageUrlProcess() {
        return this.imageUrlProcess;
    }

    public CCPGetShareLinkVideoPreviewPlayInfoRequest setLocation(String location) {
        this.location = location;
        return this;
    }
    public String getLocation() {
        return this.location;
    }

    public CCPGetShareLinkVideoPreviewPlayInfoRequest setOfficeThumbnailProcess(String officeThumbnailProcess) {
        this.officeThumbnailProcess = officeThumbnailProcess;
        return this;
    }
    public String getOfficeThumbnailProcess() {
        return this.officeThumbnailProcess;
    }

    public CCPGetShareLinkVideoPreviewPlayInfoRequest setReferer(String referer) {
        this.referer = referer;
        return this;
    }
    public String getReferer() {
        return this.referer;
    }

    public CCPGetShareLinkVideoPreviewPlayInfoRequest setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

    public CCPGetShareLinkVideoPreviewPlayInfoRequest setSignToken(String signToken) {
        this.signToken = signToken;
        return this;
    }
    public String getSignToken() {
        return this.signToken;
    }

    public CCPGetShareLinkVideoPreviewPlayInfoRequest setSubtitleLanguageList(java.util.List<String> subtitleLanguageList) {
        this.subtitleLanguageList = subtitleLanguageList;
        return this;
    }
    public java.util.List<String> getSubtitleLanguageList() {
        return this.subtitleLanguageList;
    }

    public CCPGetShareLinkVideoPreviewPlayInfoRequest setTemplateId(String templateId) {
        this.templateId = templateId;
        return this;
    }
    public String getTemplateId() {
        return this.templateId;
    }

    public CCPGetShareLinkVideoPreviewPlayInfoRequest setUrlExpireSec(Long urlExpireSec) {
        this.urlExpireSec = urlExpireSec;
        return this;
    }
    public Long getUrlExpireSec() {
        return this.urlExpireSec;
    }

    public CCPGetShareLinkVideoPreviewPlayInfoRequest setVideoThumbnailProcess(String videoThumbnailProcess) {
        this.videoThumbnailProcess = videoThumbnailProcess;
        return this;
    }
    public String getVideoThumbnailProcess() {
        return this.videoThumbnailProcess;
    }

}
