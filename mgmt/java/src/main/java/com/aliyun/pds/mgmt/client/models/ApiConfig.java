// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class ApiConfig extends TeaModel {
    @NameInMap("blacklist")
    public java.util.List<String> blacklist;

    @NameInMap("enabled")
    public Boolean enabled;

    @NameInMap("grayscale_config")
    public GrayscaleConfig grayscaleConfig;

    @NameInMap("status")
    public String status;

    @NameInMap("whitelist_config")
    public WhitelistConfig whitelistConfig;

    public static ApiConfig build(java.util.Map<String, ?> map) throws Exception {
        ApiConfig self = new ApiConfig();
        return TeaModel.build(map, self);
    }

    public ApiConfig setBlacklist(java.util.List<String> blacklist) {
        this.blacklist = blacklist;
        return this;
    }
    public java.util.List<String> getBlacklist() {
        return this.blacklist;
    }

    public ApiConfig setEnabled(Boolean enabled) {
        this.enabled = enabled;
        return this;
    }
    public Boolean getEnabled() {
        return this.enabled;
    }

    public ApiConfig setGrayscaleConfig(GrayscaleConfig grayscaleConfig) {
        this.grayscaleConfig = grayscaleConfig;
        return this;
    }
    public GrayscaleConfig getGrayscaleConfig() {
        return this.grayscaleConfig;
    }

    public ApiConfig setStatus(String status) {
        this.status = status;
        return this;
    }
    public String getStatus() {
        return this.status;
    }

    public ApiConfig setWhitelistConfig(WhitelistConfig whitelistConfig) {
        this.whitelistConfig = whitelistConfig;
        return this;
    }
    public WhitelistConfig getWhitelistConfig() {
        return this.whitelistConfig;
    }

}
