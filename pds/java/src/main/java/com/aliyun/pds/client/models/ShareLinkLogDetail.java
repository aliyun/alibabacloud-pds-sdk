// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class ShareLinkLogDetail extends TeaModel {
    // creatable
    @NameInMap("creatable")
    public Boolean creatable;

    // enable_preview
    @NameInMap("enable_preview")
    public Boolean enablePreview;

    // enable_save_download
    @NameInMap("enable_save_download")
    public Boolean enableSaveDownload;

    // enable_visible
    @NameInMap("enable_visible")
    public Boolean enableVisible;

    // expiration
    @NameInMap("expiration")
    public String expiration;

    // has_multi_object
    @NameInMap("has_multi_object")
    public Boolean hasMultiObject;

    // has_pwd
    @NameInMap("has_pwd")
    public Boolean hasPwd;

    // preview_limit
    @NameInMap("preview_limit")
    public Long previewLimit;

    // require_login
    @NameInMap("require_login")
    public Boolean requireLogin;

    // save_download_limit
    @NameInMap("save_download_limit")
    public Long saveDownloadLimit;

    // share_created_at
    @NameInMap("share_created_at")
    public String shareCreatedAt;

    // share_creator_id
    @NameInMap("share_creator_id")
    public String shareCreatorId;

    // share_creator_name
    @NameInMap("share_creator_name")
    public String shareCreatorName;

    // share_id (脱敏)
    @NameInMap("share_id")
    public String shareId;

    // to_parent_path
    @NameInMap("to_parent_path")
    public String toParentPath;

    // to_parent_path_type
    @NameInMap("to_parent_path_type")
    public String toParentPathType;

    // type
    @NameInMap("type")
    public String type;

    public static ShareLinkLogDetail build(java.util.Map<String, ?> map) throws Exception {
        ShareLinkLogDetail self = new ShareLinkLogDetail();
        return TeaModel.build(map, self);
    }

    public ShareLinkLogDetail setCreatable(Boolean creatable) {
        this.creatable = creatable;
        return this;
    }
    public Boolean getCreatable() {
        return this.creatable;
    }

    public ShareLinkLogDetail setEnablePreview(Boolean enablePreview) {
        this.enablePreview = enablePreview;
        return this;
    }
    public Boolean getEnablePreview() {
        return this.enablePreview;
    }

    public ShareLinkLogDetail setEnableSaveDownload(Boolean enableSaveDownload) {
        this.enableSaveDownload = enableSaveDownload;
        return this;
    }
    public Boolean getEnableSaveDownload() {
        return this.enableSaveDownload;
    }

    public ShareLinkLogDetail setEnableVisible(Boolean enableVisible) {
        this.enableVisible = enableVisible;
        return this;
    }
    public Boolean getEnableVisible() {
        return this.enableVisible;
    }

    public ShareLinkLogDetail setExpiration(String expiration) {
        this.expiration = expiration;
        return this;
    }
    public String getExpiration() {
        return this.expiration;
    }

    public ShareLinkLogDetail setHasMultiObject(Boolean hasMultiObject) {
        this.hasMultiObject = hasMultiObject;
        return this;
    }
    public Boolean getHasMultiObject() {
        return this.hasMultiObject;
    }

    public ShareLinkLogDetail setHasPwd(Boolean hasPwd) {
        this.hasPwd = hasPwd;
        return this;
    }
    public Boolean getHasPwd() {
        return this.hasPwd;
    }

    public ShareLinkLogDetail setPreviewLimit(Long previewLimit) {
        this.previewLimit = previewLimit;
        return this;
    }
    public Long getPreviewLimit() {
        return this.previewLimit;
    }

    public ShareLinkLogDetail setRequireLogin(Boolean requireLogin) {
        this.requireLogin = requireLogin;
        return this;
    }
    public Boolean getRequireLogin() {
        return this.requireLogin;
    }

    public ShareLinkLogDetail setSaveDownloadLimit(Long saveDownloadLimit) {
        this.saveDownloadLimit = saveDownloadLimit;
        return this;
    }
    public Long getSaveDownloadLimit() {
        return this.saveDownloadLimit;
    }

    public ShareLinkLogDetail setShareCreatedAt(String shareCreatedAt) {
        this.shareCreatedAt = shareCreatedAt;
        return this;
    }
    public String getShareCreatedAt() {
        return this.shareCreatedAt;
    }

    public ShareLinkLogDetail setShareCreatorId(String shareCreatorId) {
        this.shareCreatorId = shareCreatorId;
        return this;
    }
    public String getShareCreatorId() {
        return this.shareCreatorId;
    }

    public ShareLinkLogDetail setShareCreatorName(String shareCreatorName) {
        this.shareCreatorName = shareCreatorName;
        return this;
    }
    public String getShareCreatorName() {
        return this.shareCreatorName;
    }

    public ShareLinkLogDetail setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

    public ShareLinkLogDetail setToParentPath(String toParentPath) {
        this.toParentPath = toParentPath;
        return this;
    }
    public String getToParentPath() {
        return this.toParentPath;
    }

    public ShareLinkLogDetail setToParentPathType(String toParentPathType) {
        this.toParentPathType = toParentPathType;
        return this;
    }
    public String getToParentPathType() {
        return this.toParentPathType;
    }

    public ShareLinkLogDetail setType(String type) {
        this.type = type;
        return this;
    }
    public String getType() {
        return this.type;
    }

}
