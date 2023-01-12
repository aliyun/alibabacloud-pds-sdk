// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class ShareLinkPermissionResponse extends TeaModel {
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
     * <p>分享下载次数限制</p>
     */
    @NameInMap("download_limit")
    public Long downloadLimit;

    /**
     * <p>允许在线编辑文档</p>
     */
    @NameInMap("office_editable")
    public Boolean officeEditable;

    /**
     * <p>分享预览次数限制</p>
     */
    @NameInMap("preview_limit")
    public Long previewLimit;

    /**
     * <p>企业内(domain)登录后才允许使用分享</p>
     */
    @NameInMap("require_login")
    public Boolean requireLogin;

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

    public static ShareLinkPermissionResponse build(java.util.Map<String, ?> map) throws Exception {
        ShareLinkPermissionResponse self = new ShareLinkPermissionResponse();
        return TeaModel.build(map, self);
    }

    public ShareLinkPermissionResponse setCreatable(Boolean creatable) {
        this.creatable = creatable;
        return this;
    }
    public Boolean getCreatable() {
        return this.creatable;
    }

    public ShareLinkPermissionResponse setCreatableFileIdList(java.util.List<String> creatableFileIdList) {
        this.creatableFileIdList = creatableFileIdList;
        return this;
    }
    public java.util.List<String> getCreatableFileIdList() {
        return this.creatableFileIdList;
    }

    public ShareLinkPermissionResponse setDisableDownload(Boolean disableDownload) {
        this.disableDownload = disableDownload;
        return this;
    }
    public Boolean getDisableDownload() {
        return this.disableDownload;
    }

    public ShareLinkPermissionResponse setDisablePreview(Boolean disablePreview) {
        this.disablePreview = disablePreview;
        return this;
    }
    public Boolean getDisablePreview() {
        return this.disablePreview;
    }

    public ShareLinkPermissionResponse setDisableSave(Boolean disableSave) {
        this.disableSave = disableSave;
        return this;
    }
    public Boolean getDisableSave() {
        return this.disableSave;
    }

    public ShareLinkPermissionResponse setDisableVisible(Boolean disableVisible) {
        this.disableVisible = disableVisible;
        return this;
    }
    public Boolean getDisableVisible() {
        return this.disableVisible;
    }

    public ShareLinkPermissionResponse setDownloadLimit(Long downloadLimit) {
        this.downloadLimit = downloadLimit;
        return this;
    }
    public Long getDownloadLimit() {
        return this.downloadLimit;
    }

    public ShareLinkPermissionResponse setOfficeEditable(Boolean officeEditable) {
        this.officeEditable = officeEditable;
        return this;
    }
    public Boolean getOfficeEditable() {
        return this.officeEditable;
    }

    public ShareLinkPermissionResponse setPreviewLimit(Long previewLimit) {
        this.previewLimit = previewLimit;
        return this;
    }
    public Long getPreviewLimit() {
        return this.previewLimit;
    }

    public ShareLinkPermissionResponse setRequireLogin(Boolean requireLogin) {
        this.requireLogin = requireLogin;
        return this;
    }
    public Boolean getRequireLogin() {
        return this.requireLogin;
    }

    public ShareLinkPermissionResponse setSaveDownloadLimit(Long saveDownloadLimit) {
        this.saveDownloadLimit = saveDownloadLimit;
        return this;
    }
    public Long getSaveDownloadLimit() {
        return this.saveDownloadLimit;
    }

    public ShareLinkPermissionResponse setSaveLimit(Long saveLimit) {
        this.saveLimit = saveLimit;
        return this;
    }
    public Long getSaveLimit() {
        return this.saveLimit;
    }

}
