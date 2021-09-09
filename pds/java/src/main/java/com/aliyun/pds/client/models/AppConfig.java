// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class AppConfig extends TeaModel {
    @NameInMap("hide_drive_file_entry")
    public Boolean hideDriveFileEntry;

    @NameInMap("hide_share_admin_entry")
    public Boolean hideShareAdminEntry;

    @NameInMap("web_version")
    public String webVersion;

    public static AppConfig build(java.util.Map<String, ?> map) throws Exception {
        AppConfig self = new AppConfig();
        return TeaModel.build(map, self);
    }

    public AppConfig setHideDriveFileEntry(Boolean hideDriveFileEntry) {
        this.hideDriveFileEntry = hideDriveFileEntry;
        return this;
    }
    public Boolean getHideDriveFileEntry() {
        return this.hideDriveFileEntry;
    }

    public AppConfig setHideShareAdminEntry(Boolean hideShareAdminEntry) {
        this.hideShareAdminEntry = hideShareAdminEntry;
        return this;
    }
    public Boolean getHideShareAdminEntry() {
        return this.hideShareAdminEntry;
    }

    public AppConfig setWebVersion(String webVersion) {
        this.webVersion = webVersion;
        return this;
    }
    public String getWebVersion() {
        return this.webVersion;
    }

}
