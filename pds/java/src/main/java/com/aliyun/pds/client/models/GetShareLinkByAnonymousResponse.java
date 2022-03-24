// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * get_share_link_by_anonymous response
 */
public class GetShareLinkByAnonymousResponse extends TeaModel {
    // access_count
    @NameInMap("access_count")
    public Long accessCount;

    // avatar
    @NameInMap("avatar")
    public String avatar;

    // comments
    @NameInMap("comments")
    public String comments;

    // creator_id
    @NameInMap("creator_id")
    public String creatorId;

    // creator_name
    @NameInMap("creator_name")
    public String creatorName;

    // creator_phone
    @NameInMap("creator_phone")
    public String creatorPhone;

    // 禁止下载分享中的文件
    @NameInMap("disable_download")
    public Boolean disableDownload;

    // 禁止预览分享中的文件
    @NameInMap("disable_preview")
    public Boolean disablePreview;

    // 禁止转存分享中的文件
    @NameInMap("disable_save")
    public Boolean disableSave;

    // 下载次数
    @NameInMap("download_count")
    public Long downloadCount;

    // 分享下载次数限制
    @NameInMap("download_limit")
    public Long downloadLimit;

    // expiration
    @NameInMap("expiration")
    public String expiration;

    // file_count
    @NameInMap("file_count")
    public Long fileCount;

    // preview_count
    @NameInMap("preview_count")
    public Long previewCount;

    // 分享预览次数限制
    @NameInMap("preview_limit")
    public Long previewLimit;

    // 举报次数
    @NameInMap("report_count")
    public Long reportCount;

    // 企业内(domain)登录后才允许使用分享
    @NameInMap("require_login")
    public Boolean requireLogin;

    // 转存次数
    @NameInMap("save_count")
    public Long saveCount;

    // 分享转存和下载的总次数限制
    @NameInMap("save_download_limit")
    public Long saveDownloadLimit;

    // 分享转存次数限制
    @NameInMap("save_limit")
    public Long saveLimit;

    // share_icon
    @NameInMap("share_icon")
    public String shareIcon;

    // share_name
    @NameInMap("share_name")
    public String shareName;

    // updated_at
    @NameInMap("updated_at")
    public String updatedAt;

    // 音视频播放次数
    @NameInMap("video_preview_count")
    public Long videoPreviewCount;

    public static GetShareLinkByAnonymousResponse build(java.util.Map<String, ?> map) throws Exception {
        GetShareLinkByAnonymousResponse self = new GetShareLinkByAnonymousResponse();
        return TeaModel.build(map, self);
    }

    public GetShareLinkByAnonymousResponse setAccessCount(Long accessCount) {
        this.accessCount = accessCount;
        return this;
    }
    public Long getAccessCount() {
        return this.accessCount;
    }

    public GetShareLinkByAnonymousResponse setAvatar(String avatar) {
        this.avatar = avatar;
        return this;
    }
    public String getAvatar() {
        return this.avatar;
    }

    public GetShareLinkByAnonymousResponse setComments(String comments) {
        this.comments = comments;
        return this;
    }
    public String getComments() {
        return this.comments;
    }

    public GetShareLinkByAnonymousResponse setCreatorId(String creatorId) {
        this.creatorId = creatorId;
        return this;
    }
    public String getCreatorId() {
        return this.creatorId;
    }

    public GetShareLinkByAnonymousResponse setCreatorName(String creatorName) {
        this.creatorName = creatorName;
        return this;
    }
    public String getCreatorName() {
        return this.creatorName;
    }

    public GetShareLinkByAnonymousResponse setCreatorPhone(String creatorPhone) {
        this.creatorPhone = creatorPhone;
        return this;
    }
    public String getCreatorPhone() {
        return this.creatorPhone;
    }

    public GetShareLinkByAnonymousResponse setDisableDownload(Boolean disableDownload) {
        this.disableDownload = disableDownload;
        return this;
    }
    public Boolean getDisableDownload() {
        return this.disableDownload;
    }

    public GetShareLinkByAnonymousResponse setDisablePreview(Boolean disablePreview) {
        this.disablePreview = disablePreview;
        return this;
    }
    public Boolean getDisablePreview() {
        return this.disablePreview;
    }

    public GetShareLinkByAnonymousResponse setDisableSave(Boolean disableSave) {
        this.disableSave = disableSave;
        return this;
    }
    public Boolean getDisableSave() {
        return this.disableSave;
    }

    public GetShareLinkByAnonymousResponse setDownloadCount(Long downloadCount) {
        this.downloadCount = downloadCount;
        return this;
    }
    public Long getDownloadCount() {
        return this.downloadCount;
    }

    public GetShareLinkByAnonymousResponse setDownloadLimit(Long downloadLimit) {
        this.downloadLimit = downloadLimit;
        return this;
    }
    public Long getDownloadLimit() {
        return this.downloadLimit;
    }

    public GetShareLinkByAnonymousResponse setExpiration(String expiration) {
        this.expiration = expiration;
        return this;
    }
    public String getExpiration() {
        return this.expiration;
    }

    public GetShareLinkByAnonymousResponse setFileCount(Long fileCount) {
        this.fileCount = fileCount;
        return this;
    }
    public Long getFileCount() {
        return this.fileCount;
    }

    public GetShareLinkByAnonymousResponse setPreviewCount(Long previewCount) {
        this.previewCount = previewCount;
        return this;
    }
    public Long getPreviewCount() {
        return this.previewCount;
    }

    public GetShareLinkByAnonymousResponse setPreviewLimit(Long previewLimit) {
        this.previewLimit = previewLimit;
        return this;
    }
    public Long getPreviewLimit() {
        return this.previewLimit;
    }

    public GetShareLinkByAnonymousResponse setReportCount(Long reportCount) {
        this.reportCount = reportCount;
        return this;
    }
    public Long getReportCount() {
        return this.reportCount;
    }

    public GetShareLinkByAnonymousResponse setRequireLogin(Boolean requireLogin) {
        this.requireLogin = requireLogin;
        return this;
    }
    public Boolean getRequireLogin() {
        return this.requireLogin;
    }

    public GetShareLinkByAnonymousResponse setSaveCount(Long saveCount) {
        this.saveCount = saveCount;
        return this;
    }
    public Long getSaveCount() {
        return this.saveCount;
    }

    public GetShareLinkByAnonymousResponse setSaveDownloadLimit(Long saveDownloadLimit) {
        this.saveDownloadLimit = saveDownloadLimit;
        return this;
    }
    public Long getSaveDownloadLimit() {
        return this.saveDownloadLimit;
    }

    public GetShareLinkByAnonymousResponse setSaveLimit(Long saveLimit) {
        this.saveLimit = saveLimit;
        return this;
    }
    public Long getSaveLimit() {
        return this.saveLimit;
    }

    public GetShareLinkByAnonymousResponse setShareIcon(String shareIcon) {
        this.shareIcon = shareIcon;
        return this;
    }
    public String getShareIcon() {
        return this.shareIcon;
    }

    public GetShareLinkByAnonymousResponse setShareName(String shareName) {
        this.shareName = shareName;
        return this;
    }
    public String getShareName() {
        return this.shareName;
    }

    public GetShareLinkByAnonymousResponse setUpdatedAt(String updatedAt) {
        this.updatedAt = updatedAt;
        return this;
    }
    public String getUpdatedAt() {
        return this.updatedAt;
    }

    public GetShareLinkByAnonymousResponse setVideoPreviewCount(Long videoPreviewCount) {
        this.videoPreviewCount = videoPreviewCount;
        return this;
    }
    public Long getVideoPreviewCount() {
        return this.videoPreviewCount;
    }

}
