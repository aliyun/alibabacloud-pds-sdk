// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class AppConfig extends TeaModel {
    @NameInMap("audio_play_enable")
    public Boolean audioPlayEnable;

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

    @NameInMap("mount_app_enable")
    public Boolean mountAppEnable;

    @NameInMap("show_customized_login_config")
    public Boolean showCustomizedLoginConfig;

    @NameInMap("sync_app_enable")
    public Boolean syncAppEnable;

    @NameInMap("video_play_enable")
    public Boolean videoPlayEnable;

    @NameInMap("web_version")
    public String webVersion;

    public static AppConfig build(java.util.Map<String, ?> map) throws Exception {
        AppConfig self = new AppConfig();
        return TeaModel.build(map, self);
    }

    public AppConfig setAudioPlayEnable(Boolean audioPlayEnable) {
        this.audioPlayEnable = audioPlayEnable;
        return this;
    }
    public Boolean getAudioPlayEnable() {
        return this.audioPlayEnable;
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

    public AppConfig setMountAppEnable(Boolean mountAppEnable) {
        this.mountAppEnable = mountAppEnable;
        return this;
    }
    public Boolean getMountAppEnable() {
        return this.mountAppEnable;
    }

    public AppConfig setShowCustomizedLoginConfig(Boolean showCustomizedLoginConfig) {
        this.showCustomizedLoginConfig = showCustomizedLoginConfig;
        return this;
    }
    public Boolean getShowCustomizedLoginConfig() {
        return this.showCustomizedLoginConfig;
    }

    public AppConfig setSyncAppEnable(Boolean syncAppEnable) {
        this.syncAppEnable = syncAppEnable;
        return this;
    }
    public Boolean getSyncAppEnable() {
        return this.syncAppEnable;
    }

    public AppConfig setVideoPlayEnable(Boolean videoPlayEnable) {
        this.videoPlayEnable = videoPlayEnable;
        return this;
    }
    public Boolean getVideoPlayEnable() {
        return this.videoPlayEnable;
    }

    public AppConfig setWebVersion(String webVersion) {
        this.webVersion = webVersion;
        return this;
    }
    public String getWebVersion() {
        return this.webVersion;
    }

}
