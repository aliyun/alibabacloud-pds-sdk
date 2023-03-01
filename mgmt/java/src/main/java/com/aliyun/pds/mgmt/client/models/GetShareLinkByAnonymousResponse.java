// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * get_share_link_by_anonymous response
 */
public class GetShareLinkByAnonymousResponse extends TeaModel {
    /**
     * <p>access_count</p>
     */
    @NameInMap("access_count")
    public Long accessCount;

    /**
     * <p>avatar</p>
     */
    @NameInMap("avatar")
    public String avatar;

    /**
     * <p>文件分享大类</p>
     */
    @NameInMap("category")
    public String category;

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
     * <p>允许上传的目录列表</p>
     */
    @NameInMap("creatable_file_id_list")
    public java.util.List<String> creatableFileIdList;

    /**
     * <p>creator_id</p>
     */
    @NameInMap("creator_id")
    public String creatorId;

    /**
     * <p>creator_name</p>
     */
    @NameInMap("creator_name")
    public String creatorName;

    /**
     * <p>creator_phone</p>
     */
    @NameInMap("creator_phone")
    public String creatorPhone;

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
     * <p>下载次数</p>
     */
    @NameInMap("download_count")
    public Long downloadCount;

    /**
     * <p>分享下载次数限制</p>
     */
    @NameInMap("download_limit")
    public Long downloadLimit;

    /**
     * <p>expiration</p>
     */
    @NameInMap("expiration")
    public String expiration;

    /**
     * <p>file_count</p>
     */
    @NameInMap("file_count")
    public Long fileCount;

    /**
     * <p>has_pwd</p>
     */
    @NameInMap("has_pwd")
    public Boolean hasPwd;

    /**
     * <p>need_check_pwd</p>
     */
    @NameInMap("need_check_pwd")
    public Boolean needCheckPwd;

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
     * <p>举报次数</p>
     */
    @NameInMap("report_count")
    public Long reportCount;

    /**
     * <p>企业内(domain)登录后才允许使用分享</p>
     */
    @NameInMap("require_login")
    public Boolean requireLogin;

    /**
     * <p>转存次数</p>
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
     * <p>share_name</p>
     */
    @NameInMap("share_name")
    public String shareName;

    /**
     * <p>updated_at</p>
     */
    @NameInMap("updated_at")
    public String updatedAt;

    /**
     * <p>音视频播放次数</p>
     */
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

    public GetShareLinkByAnonymousResponse setCategory(String category) {
        this.category = category;
        return this;
    }
    public String getCategory() {
        return this.category;
    }

    public GetShareLinkByAnonymousResponse setComments(String comments) {
        this.comments = comments;
        return this;
    }
    public String getComments() {
        return this.comments;
    }

    public GetShareLinkByAnonymousResponse setCreatable(Boolean creatable) {
        this.creatable = creatable;
        return this;
    }
    public Boolean getCreatable() {
        return this.creatable;
    }

    public GetShareLinkByAnonymousResponse setCreatableFileIdList(java.util.List<String> creatableFileIdList) {
        this.creatableFileIdList = creatableFileIdList;
        return this;
    }
    public java.util.List<String> getCreatableFileIdList() {
        return this.creatableFileIdList;
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

    public GetShareLinkByAnonymousResponse setDisableVisible(Boolean disableVisible) {
        this.disableVisible = disableVisible;
        return this;
    }
    public Boolean getDisableVisible() {
        return this.disableVisible;
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

    public GetShareLinkByAnonymousResponse setHasPwd(Boolean hasPwd) {
        this.hasPwd = hasPwd;
        return this;
    }
    public Boolean getHasPwd() {
        return this.hasPwd;
    }

    public GetShareLinkByAnonymousResponse setNeedCheckPwd(Boolean needCheckPwd) {
        this.needCheckPwd = needCheckPwd;
        return this;
    }
    public Boolean getNeedCheckPwd() {
        return this.needCheckPwd;
    }

    public GetShareLinkByAnonymousResponse setOfficeEditable(Boolean officeEditable) {
        this.officeEditable = officeEditable;
        return this;
    }
    public Boolean getOfficeEditable() {
        return this.officeEditable;
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
