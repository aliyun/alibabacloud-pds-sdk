// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class UpdateShareLinkPermissionRequest extends TeaModel {
    // 禁止下载分享中的文件
    @NameInMap("disable_download")
    public Boolean disableDownload;

    // 禁止预览分享中的文件
    @NameInMap("disable_preview")
    public Boolean disablePreview;

    // 禁止转存分享中的文件
    @NameInMap("disable_save")
    public Boolean disableSave;

    // 分享下载次数限制
    @NameInMap("download_limit")
    public Long downloadLimit;

    // 允许上传文件到分享
    @NameInMap("enable_upload")
    public Boolean enableUpload;

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

    public UpdateShareLinkPermissionRequest setDownloadLimit(Long downloadLimit) {
        this.downloadLimit = downloadLimit;
        return this;
    }
    public Long getDownloadLimit() {
        return this.downloadLimit;
    }

    public UpdateShareLinkPermissionRequest setEnableUpload(Boolean enableUpload) {
        this.enableUpload = enableUpload;
        return this;
    }
    public Boolean getEnableUpload() {
        return this.enableUpload;
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
