// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 *
 */
public class DingSyncConfig extends TeaModel {
    @NameInMap("cron")
    public String cron;

    @NameInMap("enabled")
    public Boolean enabled;

    public static DingSyncConfig build(java.util.Map<String, ?> map) throws Exception {
        DingSyncConfig self = new DingSyncConfig();
        return TeaModel.build(map, self);
    }

    public DingSyncConfig setCron(String cron) {
        this.cron = cron;
        return this;
    }
    public String getCron() {
        return this.cron;
    }

    public DingSyncConfig setEnabled(Boolean enabled) {
        this.enabled = enabled;
        return this;
    }
    public Boolean getEnabled() {
        return this.enabled;
    }

}
