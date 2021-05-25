// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * list_share_link response
 */
public class BaseShareLinkResponse extends TeaModel {
    // created_at
    @NameInMap("created_at")
    public String createdAt;

    // creator
    @NameInMap("creator")
    public String creator;

    // description
    @NameInMap("description")
    public String description;

    // 下载次数
    @NameInMap("download_count")
    public Long downloadCount;

    // drive_id
    @NameInMap("drive_id")
    public String driveId;

    // expiration
    @NameInMap("expiration")
    public String expiration;

    // expired
    @NameInMap("expired")
    public Boolean expired;

    // file_id
    @NameInMap("file_id")
    public String fileId;

    // file_id_list
    @NameInMap("file_id_list")
    public java.util.List<String> fileIdList;

    // file_id_list
    @NameInMap("file_path_list")
    public java.util.List<String> filePathList;

    // preview_count
    @NameInMap("preview_count")
    public Long previewCount;

    // 转存次数
    @NameInMap("save_count")
    public Long saveCount;

    // share_id
    @NameInMap("share_id")
    public String shareId;

    // share_msg
    @NameInMap("share_msg")
    public String shareMsg;

    // share_name
    @NameInMap("share_name")
    public String shareName;

    // share_policy
    @NameInMap("share_policy")
    public String sharePolicy;

    // share_pwd
    @NameInMap("share_pwd")
    public String sharePwd;

    // share_url
    @NameInMap("share_url")
    public String shareUrl;

    // updated_at
    @NameInMap("updated_at")
    public String updatedAt;

    public static BaseShareLinkResponse build(java.util.Map<String, ?> map) throws Exception {
        BaseShareLinkResponse self = new BaseShareLinkResponse();
        return TeaModel.build(map, self);
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

    public BaseShareLinkResponse setDownloadCount(Long downloadCount) {
        this.downloadCount = downloadCount;
        return this;
    }
    public Long getDownloadCount() {
        return this.downloadCount;
    }

    public BaseShareLinkResponse setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
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

    public BaseShareLinkResponse setPreviewCount(Long previewCount) {
        this.previewCount = previewCount;
        return this;
    }
    public Long getPreviewCount() {
        return this.previewCount;
    }

    public BaseShareLinkResponse setSaveCount(Long saveCount) {
        this.saveCount = saveCount;
        return this;
    }
    public Long getSaveCount() {
        return this.saveCount;
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

    public BaseShareLinkResponse setUpdatedAt(String updatedAt) {
        this.updatedAt = updatedAt;
        return this;
    }
    public String getUpdatedAt() {
        return this.updatedAt;
    }

}
