// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 获取转码信息请求
 */
public class CCPGetVideoPreviewPlayInfoRequest extends TeaModel {
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
    @Validation(pattern = "[0-9]+")
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

    // location
    @NameInMap("location")
    public String location;

    @NameInMap("referer")
    public String referer;

    // revision_id
    @NameInMap("revision_id")
    public String revisionId;

    // share_id, either share_id or drive_id is required
    @NameInMap("share_id")
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
    @Validation(maximum = 14400, minimum = 10)
    public Long urlExpireSec;

    public static CCPGetVideoPreviewPlayInfoRequest build(java.util.Map<String, ?> map) throws Exception {
        CCPGetVideoPreviewPlayInfoRequest self = new CCPGetVideoPreviewPlayInfoRequest();
        return TeaModel.build(map, self);
    }

    public CCPGetVideoPreviewPlayInfoRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public CCPGetVideoPreviewPlayInfoRequest setAdditionData(java.util.Map<String, ?> additionData) {
        this.additionData = additionData;
        return this;
    }
    public java.util.Map<String, ?> getAdditionData() {
        return this.additionData;
    }

    public CCPGetVideoPreviewPlayInfoRequest setCategory(String category) {
        this.category = category;
        return this;
    }
    public String getCategory() {
        return this.category;
    }

    public CCPGetVideoPreviewPlayInfoRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public CCPGetVideoPreviewPlayInfoRequest setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

    public CCPGetVideoPreviewPlayInfoRequest setFileIdPath(String fileIdPath) {
        this.fileIdPath = fileIdPath;
        return this;
    }
    public String getFileIdPath() {
        return this.fileIdPath;
    }

    public CCPGetVideoPreviewPlayInfoRequest setGetPreviewUrl(Boolean getPreviewUrl) {
        this.getPreviewUrl = getPreviewUrl;
        return this;
    }
    public Boolean getGetPreviewUrl() {
        return this.getPreviewUrl;
    }

    public CCPGetVideoPreviewPlayInfoRequest setGetSubtitleInfo(Boolean getSubtitleInfo) {
        this.getSubtitleInfo = getSubtitleInfo;
        return this;
    }
    public Boolean getGetSubtitleInfo() {
        return this.getSubtitleInfo;
    }

    public CCPGetVideoPreviewPlayInfoRequest setGetWithoutUrl(Boolean getWithoutUrl) {
        this.getWithoutUrl = getWithoutUrl;
        return this;
    }
    public Boolean getGetWithoutUrl() {
        return this.getWithoutUrl;
    }

    public CCPGetVideoPreviewPlayInfoRequest setLocation(String location) {
        this.location = location;
        return this;
    }
    public String getLocation() {
        return this.location;
    }

    public CCPGetVideoPreviewPlayInfoRequest setReferer(String referer) {
        this.referer = referer;
        return this;
    }
    public String getReferer() {
        return this.referer;
    }

    public CCPGetVideoPreviewPlayInfoRequest setRevisionId(String revisionId) {
        this.revisionId = revisionId;
        return this;
    }
    public String getRevisionId() {
        return this.revisionId;
    }

    public CCPGetVideoPreviewPlayInfoRequest setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

    public CCPGetVideoPreviewPlayInfoRequest setSignToken(String signToken) {
        this.signToken = signToken;
        return this;
    }
    public String getSignToken() {
        return this.signToken;
    }

    public CCPGetVideoPreviewPlayInfoRequest setSubtitleLanguageList(java.util.List<String> subtitleLanguageList) {
        this.subtitleLanguageList = subtitleLanguageList;
        return this;
    }
    public java.util.List<String> getSubtitleLanguageList() {
        return this.subtitleLanguageList;
    }

    public CCPGetVideoPreviewPlayInfoRequest setTemplateId(String templateId) {
        this.templateId = templateId;
        return this;
    }
    public String getTemplateId() {
        return this.templateId;
    }

    public CCPGetVideoPreviewPlayInfoRequest setUrlExpireSec(Long urlExpireSec) {
        this.urlExpireSec = urlExpireSec;
        return this;
    }
    public Long getUrlExpireSec() {
        return this.urlExpireSec;
    }

}
