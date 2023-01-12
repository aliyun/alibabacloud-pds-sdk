// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * update_share_link request
 */
public class UpdateShareLinkRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    /**
     * <p>comments</p>
     */
    @NameInMap("comments")
    public String comments;

    /**
     * <p>允许上传</p>
     */
    @NameInMap("creatable")
    public Boolean creatable;

    /**
     * <p>description</p>
     */
    @NameInMap("description")
    public String description;

    /**
     * <p>禁止下载分享中的文件</p>
     */
    @NameInMap("disable_download")
    public Boolean disableDownload;

    /**
     * <p>禁止预览分享中的文件</p>
     */
    @NameInMap("disable_preview")
    public Boolean disablePreview;

    /**
     * <p>禁止转存分享中的文件</p>
     */
    @NameInMap("disable_save")
    public Boolean disableSave;

    /**
     * <p>分享中的文件不可见</p>
     */
    @NameInMap("disable_visible")
    public Boolean disableVisible;

    /**
     * <p>download_count</p>
     */
    @NameInMap("download_count")
    public Long downloadCount;

    /**
     * <p>分享下载次数限制</p>
     */
    @NameInMap("download_limit")
    public Long downloadLimit;

    /**
     * <p>enable_file_changed_notify</p>
     */
    @NameInMap("enable_file_changed_notify")
    public Boolean enableFileChangedNotify;

    /**
     * <p>expiration</p>
     */
    @NameInMap("expiration")
    public String expiration;

    /**
     * <p>is_subscribed</p>
     */
    @NameInMap("is_subscribed")
    public Boolean isSubscribed;

    /**
     * <p>num_of_subscribers</p>
     */
    @NameInMap("num_of_subscribers")
    public Long numOfSubscribers;

    /**
     * <p>允许在线编辑文档</p>
     */
    @NameInMap("office_editable")
    public Boolean officeEditable;

    /**
     * <p>preview_count</p>
     */
    @NameInMap("preview_count")
    public Long previewCount;

    /**
     * <p>分享预览次数限制</p>
     */
    @NameInMap("preview_limit")
    public Long previewLimit;

    /**
     * <p>report_count</p>
     */
    @NameInMap("report_count")
    public Long reportCount;

    /**
     * <p>企业内(domain)登录后才允许使用分享</p>
     */
    @NameInMap("require_login")
    public Boolean requireLogin;

    /**
     * <p>save_count</p>
     */
    @NameInMap("save_count")
    public Long saveCount;

    /**
     * <p>分享转存和下载的总次数限制</p>
     */
    @NameInMap("save_download_limit")
    public Long saveDownloadLimit;

    /**
     * <p>分享转存次数限制</p>
     */
    @NameInMap("save_limit")
    public Long saveLimit;

    /**
     * <p>share_icon</p>
     */
    @NameInMap("share_icon")
    public String shareIcon;

    /**
     * <p>share_id</p>
     */
    @NameInMap("share_id")
    public String shareId;

    /**
     * <p>share_name</p>
     */
    @NameInMap("share_name")
    public String shareName;

    /**
     * <p>share_pwd</p>
     */
    @NameInMap("share_pwd")
    public String sharePwd;

    /**
     * <p>status</p>
     */
    @NameInMap("status")
    public String status;

    /**
     * <p>video_preview_count</p>
     */
    @NameInMap("video_preview_count")
    public Long videoPreviewCount;

    public static UpdateShareLinkRequest build(java.util.Map<String, ?> map) throws Exception {
        UpdateShareLinkRequest self = new UpdateShareLinkRequest();
        return TeaModel.build(map, self);
    }

    public UpdateShareLinkRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public UpdateShareLinkRequest setComments(String comments) {
        this.comments = comments;
        return this;
    }
    public String getComments() {
        return this.comments;
    }

    public UpdateShareLinkRequest setCreatable(Boolean creatable) {
        this.creatable = creatable;
        return this;
    }
    public Boolean getCreatable() {
        return this.creatable;
    }

    public UpdateShareLinkRequest setDescription(String description) {
        this.description = description;
        return this;
    }
    public String getDescription() {
        return this.description;
    }

    public UpdateShareLinkRequest setDisableDownload(Boolean disableDownload) {
        this.disableDownload = disableDownload;
        return this;
    }
    public Boolean getDisableDownload() {
        return this.disableDownload;
    }

    public UpdateShareLinkRequest setDisablePreview(Boolean disablePreview) {
        this.disablePreview = disablePreview;
        return this;
    }
    public Boolean getDisablePreview() {
        return this.disablePreview;
    }

    public UpdateShareLinkRequest setDisableSave(Boolean disableSave) {
        this.disableSave = disableSave;
        return this;
    }
    public Boolean getDisableSave() {
        return this.disableSave;
    }

    public UpdateShareLinkRequest setDisableVisible(Boolean disableVisible) {
        this.disableVisible = disableVisible;
        return this;
    }
    public Boolean getDisableVisible() {
        return this.disableVisible;
    }

    public UpdateShareLinkRequest setDownloadCount(Long downloadCount) {
        this.downloadCount = downloadCount;
        return this;
    }
    public Long getDownloadCount() {
        return this.downloadCount;
    }

    public UpdateShareLinkRequest setDownloadLimit(Long downloadLimit) {
        this.downloadLimit = downloadLimit;
        return this;
    }
    public Long getDownloadLimit() {
        return this.downloadLimit;
    }

    public UpdateShareLinkRequest setEnableFileChangedNotify(Boolean enableFileChangedNotify) {
        this.enableFileChangedNotify = enableFileChangedNotify;
        return this;
    }
    public Boolean getEnableFileChangedNotify() {
        return this.enableFileChangedNotify;
    }

    public UpdateShareLinkRequest setExpiration(String expiration) {
        this.expiration = expiration;
        return this;
    }
    public String getExpiration() {
        return this.expiration;
    }

    public UpdateShareLinkRequest setIsSubscribed(Boolean isSubscribed) {
        this.isSubscribed = isSubscribed;
        return this;
    }
    public Boolean getIsSubscribed() {
        return this.isSubscribed;
    }

    public UpdateShareLinkRequest setNumOfSubscribers(Long numOfSubscribers) {
        this.numOfSubscribers = numOfSubscribers;
        return this;
    }
    public Long getNumOfSubscribers() {
        return this.numOfSubscribers;
    }

    public UpdateShareLinkRequest setOfficeEditable(Boolean officeEditable) {
        this.officeEditable = officeEditable;
        return this;
    }
    public Boolean getOfficeEditable() {
        return this.officeEditable;
    }

    public UpdateShareLinkRequest setPreviewCount(Long previewCount) {
        this.previewCount = previewCount;
        return this;
    }
    public Long getPreviewCount() {
        return this.previewCount;
    }

    public UpdateShareLinkRequest setPreviewLimit(Long previewLimit) {
        this.previewLimit = previewLimit;
        return this;
    }
    public Long getPreviewLimit() {
        return this.previewLimit;
    }

    public UpdateShareLinkRequest setReportCount(Long reportCount) {
        this.reportCount = reportCount;
        return this;
    }
    public Long getReportCount() {
        return this.reportCount;
    }

    public UpdateShareLinkRequest setRequireLogin(Boolean requireLogin) {
        this.requireLogin = requireLogin;
        return this;
    }
    public Boolean getRequireLogin() {
        return this.requireLogin;
    }

    public UpdateShareLinkRequest setSaveCount(Long saveCount) {
        this.saveCount = saveCount;
        return this;
    }
    public Long getSaveCount() {
        return this.saveCount;
    }

    public UpdateShareLinkRequest setSaveDownloadLimit(Long saveDownloadLimit) {
        this.saveDownloadLimit = saveDownloadLimit;
        return this;
    }
    public Long getSaveDownloadLimit() {
        return this.saveDownloadLimit;
    }

    public UpdateShareLinkRequest setSaveLimit(Long saveLimit) {
        this.saveLimit = saveLimit;
        return this;
    }
    public Long getSaveLimit() {
        return this.saveLimit;
    }

    public UpdateShareLinkRequest setShareIcon(String shareIcon) {
        this.shareIcon = shareIcon;
        return this;
    }
    public String getShareIcon() {
        return this.shareIcon;
    }

    public UpdateShareLinkRequest setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

    public UpdateShareLinkRequest setShareName(String shareName) {
        this.shareName = shareName;
        return this;
    }
    public String getShareName() {
        return this.shareName;
    }

    public UpdateShareLinkRequest setSharePwd(String sharePwd) {
        this.sharePwd = sharePwd;
        return this;
    }
    public String getSharePwd() {
        return this.sharePwd;
    }

    public UpdateShareLinkRequest setStatus(String status) {
        this.status = status;
        return this;
    }
    public String getStatus() {
        return this.status;
    }

    public UpdateShareLinkRequest setVideoPreviewCount(Long videoPreviewCount) {
        this.videoPreviewCount = videoPreviewCount;
        return this;
    }
    public Long getVideoPreviewCount() {
        return this.videoPreviewCount;
    }

}
