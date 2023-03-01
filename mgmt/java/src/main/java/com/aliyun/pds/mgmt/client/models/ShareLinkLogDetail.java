// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class ShareLinkLogDetail extends TeaModel {
    /**
     * <p>creatable</p>
     */
    @NameInMap("creatable")
    public Boolean creatable;

    /**
     * <p>enable_preview</p>
     */
    @NameInMap("enable_preview")
    public Boolean enablePreview;

    /**
     * <p>enable_save_download</p>
     */
    @NameInMap("enable_save_download")
    public Boolean enableSaveDownload;

    /**
     * <p>enable_visible</p>
     */
    @NameInMap("enable_visible")
    public Boolean enableVisible;

    /**
     * <p>expiration</p>
     */
    @NameInMap("expiration")
    public String expiration;

    /**
     * <p>has_multi_object</p>
     */
    @NameInMap("has_multi_object")
    public Boolean hasMultiObject;

    /**
     * <p>has_pwd</p>
     */
    @NameInMap("has_pwd")
    public Boolean hasPwd;

    /**
     * <p>office_editable</p>
     */
    @NameInMap("office_editable")
    public Boolean officeEditable;

    /**
     * <p>preview_limit</p>
     */
    @NameInMap("preview_limit")
    public Long previewLimit;

    /**
     * <p>require_login</p>
     */
    @NameInMap("require_login")
    public Boolean requireLogin;

    /**
     * <p>save_download_limit</p>
     */
    @NameInMap("save_download_limit")
    public Long saveDownloadLimit;

    /**
     * <p>share_created_at</p>
     */
    @NameInMap("share_created_at")
    public String shareCreatedAt;

    /**
     * <p>share_creator_id</p>
     */
    @NameInMap("share_creator_id")
    public String shareCreatorId;

    /**
     * <p>share_creator_name</p>
     */
    @NameInMap("share_creator_name")
    public String shareCreatorName;

    /**
     * <p>share_id (脱敏)</p>
     */
    @NameInMap("share_id")
    public String shareId;

    /**
     * <p>to_parent_path</p>
     */
    @NameInMap("to_parent_path")
    public String toParentPath;

    /**
     * <p>to_parent_path_type</p>
     */
    @NameInMap("to_parent_path_type")
    public String toParentPathType;

    /**
     * <p>type</p>
     */
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

    public ShareLinkLogDetail setOfficeEditable(Boolean officeEditable) {
        this.officeEditable = officeEditable;
        return this;
    }
    public Boolean getOfficeEditable() {
        return this.officeEditable;
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
