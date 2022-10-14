// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class WeChatSyncConfig extends TeaModel {
    @NameInMap("cron")
    public String cron;

    @NameInMap("enabled")
    public Boolean enabled;

    @NameInMap("tag_id")
    public String tagId;

    public static WeChatSyncConfig build(java.util.Map<String, ?> map) throws Exception {
        WeChatSyncConfig self = new WeChatSyncConfig();
        return TeaModel.build(map, self);
    }

    public WeChatSyncConfig setCron(String cron) {
        this.cron = cron;
        return this;
    }
    public String getCron() {
        return this.cron;
    }

    public WeChatSyncConfig setEnabled(Boolean enabled) {
        this.enabled = enabled;
        return this;
    }
    public Boolean getEnabled() {
        return this.enabled;
    }

    public WeChatSyncConfig setTagId(String tagId) {
        this.tagId = tagId;
        return this;
    }
    public String getTagId() {
        return this.tagId;
    }

}
