// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 *
 */
public class AuditLogConfig extends TeaModel {
    @NameInMap("active_log_keep_days")
    public Long activeLogKeepDays;

    @NameInMap("enabled")
    public Boolean enabled;

    @NameInMap("redirect_enabled")
    public Boolean redirectEnabled;

    public static AuditLogConfig build(java.util.Map<String, ?> map) throws Exception {
        AuditLogConfig self = new AuditLogConfig();
        return TeaModel.build(map, self);
    }

    public AuditLogConfig setActiveLogKeepDays(Long activeLogKeepDays) {
        this.activeLogKeepDays = activeLogKeepDays;
        return this;
    }
    public Long getActiveLogKeepDays() {
        return this.activeLogKeepDays;
    }

    public AuditLogConfig setEnabled(Boolean enabled) {
        this.enabled = enabled;
        return this;
    }
    public Boolean getEnabled() {
        return this.enabled;
    }

    public AuditLogConfig setRedirectEnabled(Boolean redirectEnabled) {
        this.redirectEnabled = redirectEnabled;
        return this;
    }
    public Boolean getRedirectEnabled() {
        return this.redirectEnabled;
    }

}
