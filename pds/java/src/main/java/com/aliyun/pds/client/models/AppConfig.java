// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class AppConfig extends TeaModel {
    @NameInMap("allow_upload_custom_file_ext_list")
    public java.util.List<String> allowUploadCustomFileExtList;

    @NameInMap("allow_upload_file_category_list")
    public java.util.List<String> allowUploadFileCategoryList;

    @NameInMap("audio_play_enable")
    public Boolean audioPlayEnable;

    @NameInMap("black_admin_menu_items")
    public String blackAdminMenuItems;

    @NameInMap("custom_account_identity_base_64")
    public Boolean customAccountIdentityBase64;

    @NameInMap("default_url_expire_sec")
    public Long defaultUrlExpireSec;

    @NameInMap("disable_client_builder")
    public Boolean disableClientBuilder;

    @NameInMap("disable_group")
    public Boolean disableGroup;

    @NameInMap("enable_edit_file_with_create_perm")
    public Boolean enableEditFileWithCreatePerm;

    @NameInMap("enable_hidden_file")
    public Boolean enableHiddenFile;

    @NameInMap("enable_share_link_count_limit")
    public Boolean enableShareLinkCountLimit;

    @NameInMap("enable_sse_oss")
    public Boolean enableSseOss;

    @NameInMap("enable_transfer_acceleration")
    public Boolean enableTransferAcceleration;

    @NameInMap("enable_update_share_link_by_admin")
    public Boolean enableUpdateShareLinkByAdmin;

    @NameInMap("hidden_switch_user_role_entry")
    public Boolean hiddenSwitchUserRoleEntry;

    @NameInMap("hide_admin_entry")
    public Boolean hideAdminEntry;

    @NameInMap("hide_client_download_entry")
    public Boolean hideClientDownloadEntry;

    @NameInMap("hide_drive_file_entry")
    public Boolean hideDriveFileEntry;

    @NameInMap("hide_logout_entry")
    public Boolean hideLogoutEntry;

    @NameInMap("hide_share_admin_entry")
    public Boolean hideShareAdminEntry;

    @NameInMap("hide_sharelink_login")
    public Boolean hideSharelinkLogin;

    @NameInMap("hide_user_entry")
    public Boolean hideUserEntry;

    @NameInMap("mount_app_enable")
    public Boolean mountAppEnable;

    @NameInMap("same_name_file_upload_mode")
    public String sameNameFileUploadMode;

    @NameInMap("share_hide_disabled_user")
    public Boolean shareHideDisabledUser;

    @NameInMap("share_link_disable_download")
    public Boolean shareLinkDisableDownload;

    @NameInMap("share_link_disable_upload")
    public Boolean shareLinkDisableUpload;

    @NameInMap("share_link_login_access_only")
    public Boolean shareLinkLoginAccessOnly;

    @NameInMap("show_customized_login_config")
    public Boolean showCustomizedLoginConfig;

    @NameInMap("single_file_upload_size_limit")
    public Long singleFileUploadSizeLimit;

    @NameInMap("sync_app_enable")
    public Boolean syncAppEnable;

    @NameInMap("user_can_access_group_recycle_bin")
    public Boolean userCanAccessGroupRecycleBin;

    @NameInMap("video_play_enable")
    public Boolean videoPlayEnable;

    @NameInMap("web_client_download_mode")
    public String webClientDownloadMode;

    @NameInMap("web_version")
    public String webVersion;

    @NameInMap("white_admin_menu_items")
    public String whiteAdminMenuItems;

    public static AppConfig build(java.util.Map<String, ?> map) throws Exception {
        AppConfig self = new AppConfig();
        return TeaModel.build(map, self);
    }

    public AppConfig setAllowUploadCustomFileExtList(java.util.List<String> allowUploadCustomFileExtList) {
        this.allowUploadCustomFileExtList = allowUploadCustomFileExtList;
        return this;
    }
    public java.util.List<String> getAllowUploadCustomFileExtList() {
        return this.allowUploadCustomFileExtList;
    }

    public AppConfig setAllowUploadFileCategoryList(java.util.List<String> allowUploadFileCategoryList) {
        this.allowUploadFileCategoryList = allowUploadFileCategoryList;
        return this;
    }
    public java.util.List<String> getAllowUploadFileCategoryList() {
        return this.allowUploadFileCategoryList;
    }

    public AppConfig setAudioPlayEnable(Boolean audioPlayEnable) {
        this.audioPlayEnable = audioPlayEnable;
        return this;
    }
    public Boolean getAudioPlayEnable() {
        return this.audioPlayEnable;
    }

    public AppConfig setBlackAdminMenuItems(String blackAdminMenuItems) {
        this.blackAdminMenuItems = blackAdminMenuItems;
        return this;
    }
    public String getBlackAdminMenuItems() {
        return this.blackAdminMenuItems;
    }

    public AppConfig setCustomAccountIdentityBase64(Boolean customAccountIdentityBase64) {
        this.customAccountIdentityBase64 = customAccountIdentityBase64;
        return this;
    }
    public Boolean getCustomAccountIdentityBase64() {
        return this.customAccountIdentityBase64;
    }

    public AppConfig setDefaultUrlExpireSec(Long defaultUrlExpireSec) {
        this.defaultUrlExpireSec = defaultUrlExpireSec;
        return this;
    }
    public Long getDefaultUrlExpireSec() {
        return this.defaultUrlExpireSec;
    }

    public AppConfig setDisableClientBuilder(Boolean disableClientBuilder) {
        this.disableClientBuilder = disableClientBuilder;
        return this;
    }
    public Boolean getDisableClientBuilder() {
        return this.disableClientBuilder;
    }

    public AppConfig setDisableGroup(Boolean disableGroup) {
        this.disableGroup = disableGroup;
        return this;
    }
    public Boolean getDisableGroup() {
        return this.disableGroup;
    }

    public AppConfig setEnableEditFileWithCreatePerm(Boolean enableEditFileWithCreatePerm) {
        this.enableEditFileWithCreatePerm = enableEditFileWithCreatePerm;
        return this;
    }
    public Boolean getEnableEditFileWithCreatePerm() {
        return this.enableEditFileWithCreatePerm;
    }

    public AppConfig setEnableHiddenFile(Boolean enableHiddenFile) {
        this.enableHiddenFile = enableHiddenFile;
        return this;
    }
    public Boolean getEnableHiddenFile() {
        return this.enableHiddenFile;
    }

    public AppConfig setEnableShareLinkCountLimit(Boolean enableShareLinkCountLimit) {
        this.enableShareLinkCountLimit = enableShareLinkCountLimit;
        return this;
    }
    public Boolean getEnableShareLinkCountLimit() {
        return this.enableShareLinkCountLimit;
    }

    public AppConfig setEnableSseOss(Boolean enableSseOss) {
        this.enableSseOss = enableSseOss;
        return this;
    }
    public Boolean getEnableSseOss() {
        return this.enableSseOss;
    }

    public AppConfig setEnableTransferAcceleration(Boolean enableTransferAcceleration) {
        this.enableTransferAcceleration = enableTransferAcceleration;
        return this;
    }
    public Boolean getEnableTransferAcceleration() {
        return this.enableTransferAcceleration;
    }

    public AppConfig setEnableUpdateShareLinkByAdmin(Boolean enableUpdateShareLinkByAdmin) {
        this.enableUpdateShareLinkByAdmin = enableUpdateShareLinkByAdmin;
        return this;
    }
    public Boolean getEnableUpdateShareLinkByAdmin() {
        return this.enableUpdateShareLinkByAdmin;
    }

    public AppConfig setHiddenSwitchUserRoleEntry(Boolean hiddenSwitchUserRoleEntry) {
        this.hiddenSwitchUserRoleEntry = hiddenSwitchUserRoleEntry;
        return this;
    }
    public Boolean getHiddenSwitchUserRoleEntry() {
        return this.hiddenSwitchUserRoleEntry;
    }

    public AppConfig setHideAdminEntry(Boolean hideAdminEntry) {
        this.hideAdminEntry = hideAdminEntry;
        return this;
    }
    public Boolean getHideAdminEntry() {
        return this.hideAdminEntry;
    }

    public AppConfig setHideClientDownloadEntry(Boolean hideClientDownloadEntry) {
        this.hideClientDownloadEntry = hideClientDownloadEntry;
        return this;
    }
    public Boolean getHideClientDownloadEntry() {
        return this.hideClientDownloadEntry;
    }

    public AppConfig setHideDriveFileEntry(Boolean hideDriveFileEntry) {
        this.hideDriveFileEntry = hideDriveFileEntry;
        return this;
    }
    public Boolean getHideDriveFileEntry() {
        return this.hideDriveFileEntry;
    }

    public AppConfig setHideLogoutEntry(Boolean hideLogoutEntry) {
        this.hideLogoutEntry = hideLogoutEntry;
        return this;
    }
    public Boolean getHideLogoutEntry() {
        return this.hideLogoutEntry;
    }

    public AppConfig setHideShareAdminEntry(Boolean hideShareAdminEntry) {
        this.hideShareAdminEntry = hideShareAdminEntry;
        return this;
    }
    public Boolean getHideShareAdminEntry() {
        return this.hideShareAdminEntry;
    }

    public AppConfig setHideSharelinkLogin(Boolean hideSharelinkLogin) {
        this.hideSharelinkLogin = hideSharelinkLogin;
        return this;
    }
    public Boolean getHideSharelinkLogin() {
        return this.hideSharelinkLogin;
    }

    public AppConfig setHideUserEntry(Boolean hideUserEntry) {
        this.hideUserEntry = hideUserEntry;
        return this;
    }
    public Boolean getHideUserEntry() {
        return this.hideUserEntry;
    }

    public AppConfig setMountAppEnable(Boolean mountAppEnable) {
        this.mountAppEnable = mountAppEnable;
        return this;
    }
    public Boolean getMountAppEnable() {
        return this.mountAppEnable;
    }

    public AppConfig setSameNameFileUploadMode(String sameNameFileUploadMode) {
        this.sameNameFileUploadMode = sameNameFileUploadMode;
        return this;
    }
    public String getSameNameFileUploadMode() {
        return this.sameNameFileUploadMode;
    }

    public AppConfig setShareHideDisabledUser(Boolean shareHideDisabledUser) {
        this.shareHideDisabledUser = shareHideDisabledUser;
        return this;
    }
    public Boolean getShareHideDisabledUser() {
        return this.shareHideDisabledUser;
    }

    public AppConfig setShareLinkDisableDownload(Boolean shareLinkDisableDownload) {
        this.shareLinkDisableDownload = shareLinkDisableDownload;
        return this;
    }
    public Boolean getShareLinkDisableDownload() {
        return this.shareLinkDisableDownload;
    }

    public AppConfig setShareLinkDisableUpload(Boolean shareLinkDisableUpload) {
        this.shareLinkDisableUpload = shareLinkDisableUpload;
        return this;
    }
    public Boolean getShareLinkDisableUpload() {
        return this.shareLinkDisableUpload;
    }

    public AppConfig setShareLinkLoginAccessOnly(Boolean shareLinkLoginAccessOnly) {
        this.shareLinkLoginAccessOnly = shareLinkLoginAccessOnly;
        return this;
    }
    public Boolean getShareLinkLoginAccessOnly() {
        return this.shareLinkLoginAccessOnly;
    }

    public AppConfig setShowCustomizedLoginConfig(Boolean showCustomizedLoginConfig) {
        this.showCustomizedLoginConfig = showCustomizedLoginConfig;
        return this;
    }
    public Boolean getShowCustomizedLoginConfig() {
        return this.showCustomizedLoginConfig;
    }

    public AppConfig setSingleFileUploadSizeLimit(Long singleFileUploadSizeLimit) {
        this.singleFileUploadSizeLimit = singleFileUploadSizeLimit;
        return this;
    }
    public Long getSingleFileUploadSizeLimit() {
        return this.singleFileUploadSizeLimit;
    }

    public AppConfig setSyncAppEnable(Boolean syncAppEnable) {
        this.syncAppEnable = syncAppEnable;
        return this;
    }
    public Boolean getSyncAppEnable() {
        return this.syncAppEnable;
    }

    public AppConfig setUserCanAccessGroupRecycleBin(Boolean userCanAccessGroupRecycleBin) {
        this.userCanAccessGroupRecycleBin = userCanAccessGroupRecycleBin;
        return this;
    }
    public Boolean getUserCanAccessGroupRecycleBin() {
        return this.userCanAccessGroupRecycleBin;
    }

    public AppConfig setVideoPlayEnable(Boolean videoPlayEnable) {
        this.videoPlayEnable = videoPlayEnable;
        return this;
    }
    public Boolean getVideoPlayEnable() {
        return this.videoPlayEnable;
    }

    public AppConfig setWebClientDownloadMode(String webClientDownloadMode) {
        this.webClientDownloadMode = webClientDownloadMode;
        return this;
    }
    public String getWebClientDownloadMode() {
        return this.webClientDownloadMode;
    }

    public AppConfig setWebVersion(String webVersion) {
        this.webVersion = webVersion;
        return this;
    }
    public String getWebVersion() {
        return this.webVersion;
    }

    public AppConfig setWhiteAdminMenuItems(String whiteAdminMenuItems) {
        this.whiteAdminMenuItems = whiteAdminMenuItems;
        return this;
    }
    public String getWhiteAdminMenuItems() {
        return this.whiteAdminMenuItems;
    }

}
