// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class UpdateShareLinkPermissionRequest extends TeaModel {
    // 允许上传
    @NameInMap("creatable")
    public Boolean creatable;

    // 禁止下载分享中的文件
    @NameInMap("disable_download")
    public Boolean disableDownload;

    // 禁止预览分享中的文件
    @NameInMap("disable_preview")
    public Boolean disablePreview;

    // 禁止转存分享中的文件
    @NameInMap("disable_save")
    public Boolean disableSave;

    // 分享中的文件不可见
    @NameInMap("disable_visible")
    public Boolean disableVisible;

    // 分享下载次数限制
    @NameInMap("download_limit")
    public Long downloadLimit;

    // 允许在线编辑文档
    @NameInMap("office_editable")
    public Boolean officeEditable;

    // 分享预览次数限制
    @NameInMap("preview_limit")
    public Long previewLimit;

    // 企业内(domain)登录后才允许使用分享
    @NameInMap("require_login")
    public Boolean requireLogin;

    // 分享转存和下载的总次数限制
    @NameInMap("save_download_limit")
    public Long saveDownloadLimit;

    // 分享转存次数限制
    @NameInMap("save_limit")
    public Long saveLimit;

    public static UpdateShareLinkPermissionRequest build(java.util.Map<String, ?> map) throws Exception {
        UpdateShareLinkPermissionRequest self = new UpdateShareLinkPermissionRequest();
        return TeaModel.build(map, self);
    }

    public UpdateShareLinkPermissionRequest setCreatable(Boolean creatable) {
        this.creatable = creatable;
        return this;
    }
    public Boolean getCreatable() {
        return this.creatable;
    }

    public UpdateShareLinkPermissionRequest setDisableDownload(Boolean disableDownload) {
        this.disableDownload = disableDownload;
        return this;
    }
    public Boolean getDisableDownload() {
        return this.disableDownload;
    }

    public UpdateShareLinkPermissionRequest setDisablePreview(Boolean disablePreview) {
        this.disablePreview = disablePreview;
        return this;
    }
    public Boolean getDisablePreview() {
        return this.disablePreview;
    }

    public UpdateShareLinkPermissionRequest setDisableSave(Boolean disableSave) {
        this.disableSave = disableSave;
        return this;
    }
    public Boolean getDisableSave() {
        return this.disableSave;
    }

    public UpdateShareLinkPermissionRequest setDisableVisible(Boolean disableVisible) {
        this.disableVisible = disableVisible;
        return this;
    }
    public Boolean getDisableVisible() {
        return this.disableVisible;
    }

    public UpdateShareLinkPermissionRequest setDownloadLimit(Long downloadLimit) {
        this.downloadLimit = downloadLimit;
        return this;
    }
    public Long getDownloadLimit() {
        return this.downloadLimit;
    }

    public UpdateShareLinkPermissionRequest setOfficeEditable(Boolean officeEditable) {
        this.officeEditable = officeEditable;
        return this;
    }
    public Boolean getOfficeEditable() {
        return this.officeEditable;
    }

    public UpdateShareLinkPermissionRequest setPreviewLimit(Long previewLimit) {
        this.previewLimit = previewLimit;
        return this;
    }
    public Long getPreviewLimit() {
        return this.previewLimit;
    }

    public UpdateShareLinkPermissionRequest setRequireLogin(Boolean requireLogin) {
        this.requireLogin = requireLogin;
        return this;
    }
    public Boolean getRequireLogin() {
        return this.requireLogin;
    }

    public UpdateShareLinkPermissionRequest setSaveDownloadLimit(Long saveDownloadLimit) {
        this.saveDownloadLimit = saveDownloadLimit;
        return this;
    }
    public Long getSaveDownloadLimit() {
        return this.saveDownloadLimit;
    }

    public UpdateShareLinkPermissionRequest setSaveLimit(Long saveLimit) {
        this.saveLimit = saveLimit;
        return this;
    }
    public Long getSaveLimit() {
        return this.saveLimit;
    }

}
