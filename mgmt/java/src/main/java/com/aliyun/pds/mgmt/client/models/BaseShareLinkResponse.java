// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * list_share_link response
 */
public class BaseShareLinkResponse extends TeaModel {
    /**
     * <p>access_count</p>
     */
    @NameInMap("access_count")
    public Long accessCount;

    /**
     * <p>Category</p>
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
     * <p>created_at</p>
     */
    @NameInMap("created_at")
    public String createdAt;

    /**
     * <p>creator</p>
     */
    @NameInMap("creator")
    public String creator;

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
     * <p>file_list</p>
     */
    @NameInMap("drive_file_list")
    public java.util.List<ShareFile> driveFileList;

    /**
     * <p>drive_id</p>
     */
    @NameInMap("drive_id")
    public String driveId;

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
     * <p>expired</p>
     */
    @NameInMap("expired")
    public Boolean expired;

    /**
     * <p>file_id</p>
     */
    @NameInMap("file_id")
    public String fileId;

    /**
     * <p>file_id_list</p>
     */
    @NameInMap("file_id_list")
    public java.util.List<String> fileIdList;

    /**
     * <p>file_id_list</p>
     */
    @NameInMap("file_path_list")
    public java.util.List<String> filePathList;

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
     * <p>是否分享整个drive中的文件，仅文件分享才有效，true时file_id_list字段无效</p>
     */
    @NameInMap("share_all_files")
    public Boolean shareAllFiles;

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
     * <p>share_msg</p>
     */
    @NameInMap("share_msg")
    public String shareMsg;

    /**
     * <p>share_name</p>
     */
    @NameInMap("share_name")
    public String shareName;

    /**
     * <p>share_policy</p>
     */
    @NameInMap("share_policy")
    public String sharePolicy;

    /**
     * <p>share_pwd</p>
     */
    @NameInMap("share_pwd")
    public String sharePwd;

    /**
     * <p>share_url</p>
     */
    @NameInMap("share_url")
    public String shareUrl;

    /**
     * <p>status</p>
     */
    @NameInMap("status")
    public String status;

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

    /**
     * <p>ViewID</p>
     */
    @NameInMap("view_id")
    public String viewId;

    public static BaseShareLinkResponse build(java.util.Map<String, ?> map) throws Exception {
        BaseShareLinkResponse self = new BaseShareLinkResponse();
        return TeaModel.build(map, self);
    }

    public BaseShareLinkResponse setAccessCount(Long accessCount) {
        this.accessCount = accessCount;
        return this;
    }
    public Long getAccessCount() {
        return this.accessCount;
    }

    public BaseShareLinkResponse setCategory(String category) {
        this.category = category;
        return this;
    }
    public String getCategory() {
        return this.category;
    }

    public BaseShareLinkResponse setComments(String comments) {
        this.comments = comments;
        return this;
    }
    public String getComments() {
        return this.comments;
    }

    public BaseShareLinkResponse setCreatable(Boolean creatable) {
        this.creatable = creatable;
        return this;
    }
    public Boolean getCreatable() {
        return this.creatable;
    }

    public BaseShareLinkResponse setCreatableFileIdList(java.util.List<String> creatableFileIdList) {
        this.creatableFileIdList = creatableFileIdList;
        return this;
    }
    public java.util.List<String> getCreatableFileIdList() {
        return this.creatableFileIdList;
    }

    public BaseShareLinkResponse setCreatedAt(String createdAt) {
        this.createdAt = createdAt;
        return this;
    }
    public String getCreatedAt() {
        return this.createdAt;
    }

    public BaseShareLinkResponse setCreator(String creator) {
        this.creator = creator;
        return this;
    }
    public String getCreator() {
        return this.creator;
    }

    public BaseShareLinkResponse setDescription(String description) {
        this.description = description;
        return this;
    }
    public String getDescription() {
        return this.description;
    }

    public BaseShareLinkResponse setDisableDownload(Boolean disableDownload) {
        this.disableDownload = disableDownload;
        return this;
    }
    public Boolean getDisableDownload() {
        return this.disableDownload;
    }

    public BaseShareLinkResponse setDisablePreview(Boolean disablePreview) {
        this.disablePreview = disablePreview;
        return this;
    }
    public Boolean getDisablePreview() {
        return this.disablePreview;
    }

    public BaseShareLinkResponse setDisableSave(Boolean disableSave) {
        this.disableSave = disableSave;
        return this;
    }
    public Boolean getDisableSave() {
        return this.disableSave;
    }

    public BaseShareLinkResponse setDisableVisible(Boolean disableVisible) {
        this.disableVisible = disableVisible;
        return this;
    }
    public Boolean getDisableVisible() {
        return this.disableVisible;
    }

    public BaseShareLinkResponse setDownloadCount(Long downloadCount) {
        this.downloadCount = downloadCount;
        return this;
    }
    public Long getDownloadCount() {
        return this.downloadCount;
    }

    public BaseShareLinkResponse setDownloadLimit(Long downloadLimit) {
        this.downloadLimit = downloadLimit;
        return this;
    }
    public Long getDownloadLimit() {
        return this.downloadLimit;
    }

    public BaseShareLinkResponse setDriveFileList(java.util.List<ShareFile> driveFileList) {
        this.driveFileList = driveFileList;
        return this;
    }
    public java.util.List<ShareFile> getDriveFileList() {
        return this.driveFileList;
    }

    public BaseShareLinkResponse setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public BaseShareLinkResponse setEnableFileChangedNotify(Boolean enableFileChangedNotify) {
        this.enableFileChangedNotify = enableFileChangedNotify;
        return this;
    }
    public Boolean getEnableFileChangedNotify() {
        return this.enableFileChangedNotify;
    }

    public BaseShareLinkResponse setExpiration(String expiration) {
        this.expiration = expiration;
        return this;
    }
    public String getExpiration() {
        return this.expiration;
    }

    public BaseShareLinkResponse setExpired(Boolean expired) {
        this.expired = expired;
        return this;
    }
    public Boolean getExpired() {
        return this.expired;
    }

    public BaseShareLinkResponse setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

    public BaseShareLinkResponse setFileIdList(java.util.List<String> fileIdList) {
        this.fileIdList = fileIdList;
        return this;
    }
    public java.util.List<String> getFileIdList() {
        return this.fileIdList;
    }

    public BaseShareLinkResponse setFilePathList(java.util.List<String> filePathList) {
        this.filePathList = filePathList;
        return this;
    }
    public java.util.List<String> getFilePathList() {
        return this.filePathList;
    }

    public BaseShareLinkResponse setIsSubscribed(Boolean isSubscribed) {
        this.isSubscribed = isSubscribed;
        return this;
    }
    public Boolean getIsSubscribed() {
        return this.isSubscribed;
    }

    public BaseShareLinkResponse setNumOfSubscribers(Long numOfSubscribers) {
        this.numOfSubscribers = numOfSubscribers;
        return this;
    }
    public Long getNumOfSubscribers() {
        return this.numOfSubscribers;
    }

    public BaseShareLinkResponse setOfficeEditable(Boolean officeEditable) {
        this.officeEditable = officeEditable;
        return this;
    }
    public Boolean getOfficeEditable() {
        return this.officeEditable;
    }

    public BaseShareLinkResponse setPreviewCount(Long previewCount) {
        this.previewCount = previewCount;
        return this;
    }
    public Long getPreviewCount() {
        return this.previewCount;
    }

    public BaseShareLinkResponse setPreviewLimit(Long previewLimit) {
        this.previewLimit = previewLimit;
        return this;
    }
    public Long getPreviewLimit() {
        return this.previewLimit;
    }

    public BaseShareLinkResponse setReportCount(Long reportCount) {
        this.reportCount = reportCount;
        return this;
    }
    public Long getReportCount() {
        return this.reportCount;
    }

    public BaseShareLinkResponse setRequireLogin(Boolean requireLogin) {
        this.requireLogin = requireLogin;
        return this;
    }
    public Boolean getRequireLogin() {
        return this.requireLogin;
    }

    public BaseShareLinkResponse setSaveCount(Long saveCount) {
        this.saveCount = saveCount;
        return this;
    }
    public Long getSaveCount() {
        return this.saveCount;
    }

    public BaseShareLinkResponse setSaveDownloadLimit(Long saveDownloadLimit) {
        this.saveDownloadLimit = saveDownloadLimit;
        return this;
    }
    public Long getSaveDownloadLimit() {
        return this.saveDownloadLimit;
    }

    public BaseShareLinkResponse setSaveLimit(Long saveLimit) {
        this.saveLimit = saveLimit;
        return this;
    }
    public Long getSaveLimit() {
        return this.saveLimit;
    }

    public BaseShareLinkResponse setShareAllFiles(Boolean shareAllFiles) {
        this.shareAllFiles = shareAllFiles;
        return this;
    }
    public Boolean getShareAllFiles() {
        return this.shareAllFiles;
    }

    public BaseShareLinkResponse setShareIcon(String shareIcon) {
        this.shareIcon = shareIcon;
        return this;
    }
    public String getShareIcon() {
        return this.shareIcon;
    }

    public BaseShareLinkResponse setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

    public BaseShareLinkResponse setShareMsg(String shareMsg) {
        this.shareMsg = shareMsg;
        return this;
    }
    public String getShareMsg() {
        return this.shareMsg;
    }

    public BaseShareLinkResponse setShareName(String shareName) {
        this.shareName = shareName;
        return this;
    }
    public String getShareName() {
        return this.shareName;
    }

    public BaseShareLinkResponse setSharePolicy(String sharePolicy) {
        this.sharePolicy = sharePolicy;
        return this;
    }
    public String getSharePolicy() {
        return this.sharePolicy;
    }

    public BaseShareLinkResponse setSharePwd(String sharePwd) {
        this.sharePwd = sharePwd;
        return this;
    }
    public String getSharePwd() {
        return this.sharePwd;
    }

    public BaseShareLinkResponse setShareUrl(String shareUrl) {
        this.shareUrl = shareUrl;
        return this;
    }
    public String getShareUrl() {
        return this.shareUrl;
    }

    public BaseShareLinkResponse setStatus(String status) {
        this.status = status;
        return this;
    }
    public String getStatus() {
        return this.status;
    }

    public BaseShareLinkResponse setUpdatedAt(String updatedAt) {
        this.updatedAt = updatedAt;
        return this;
    }
    public String getUpdatedAt() {
        return this.updatedAt;
    }

    public BaseShareLinkResponse setVideoPreviewCount(Long videoPreviewCount) {
        this.videoPreviewCount = videoPreviewCount;
        return this;
    }
    public Long getVideoPreviewCount() {
        return this.videoPreviewCount;
    }

    public BaseShareLinkResponse setViewId(String viewId) {
        this.viewId = viewId;
        return this;
    }
    public String getViewId() {
        return this.viewId;
    }

}
