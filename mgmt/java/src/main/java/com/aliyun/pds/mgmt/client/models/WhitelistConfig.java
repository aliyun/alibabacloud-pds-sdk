// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class WhitelistConfig extends TeaModel {
    @NameInMap("drive_whitelist")
    public java.util.List<String> driveWhitelist;

    @NameInMap("enabled")
    public Boolean enabled;

    @NameInMap("whitelist")
    public java.util.List<String> whitelist;

    public static WhitelistConfig build(java.util.Map<String, ?> map) throws Exception {
        WhitelistConfig self = new WhitelistConfig();
        return TeaModel.build(map, self);
    }

    public WhitelistConfig setDriveWhitelist(java.util.List<String> driveWhitelist) {
        this.driveWhitelist = driveWhitelist;
        return this;
    }
    public java.util.List<String> getDriveWhitelist() {
        return this.driveWhitelist;
    }

    public WhitelistConfig setEnabled(Boolean enabled) {
        this.enabled = enabled;
        return this;
    }
    public Boolean getEnabled() {
        return this.enabled;
    }

    public WhitelistConfig setWhitelist(java.util.List<String> whitelist) {
        this.whitelist = whitelist;
        return this;
    }
    public java.util.List<String> getWhitelist() {
        return this.whitelist;
    }

}
