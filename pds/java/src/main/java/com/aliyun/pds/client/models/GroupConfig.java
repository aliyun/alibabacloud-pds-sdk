// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 *
 */
public class GroupConfig extends TeaModel {
    @NameInMap("auto_add_root_group_enabled")
    public Boolean autoAddRootGroupEnabled;

    @NameInMap("max_level")
    public Long maxLevel;

    @NameInMap("root_group_id")
    public String rootGroupId;

    public static GroupConfig build(java.util.Map<String, ?> map) throws Exception {
        GroupConfig self = new GroupConfig();
        return TeaModel.build(map, self);
    }

    public GroupConfig setAutoAddRootGroupEnabled(Boolean autoAddRootGroupEnabled) {
        this.autoAddRootGroupEnabled = autoAddRootGroupEnabled;
        return this;
    }
    public Boolean getAutoAddRootGroupEnabled() {
        return this.autoAddRootGroupEnabled;
    }

    public GroupConfig setMaxLevel(Long maxLevel) {
        this.maxLevel = maxLevel;
        return this;
    }
    public Long getMaxLevel() {
        return this.maxLevel;
    }

    public GroupConfig setRootGroupId(String rootGroupId) {
        this.rootGroupId = rootGroupId;
        return this;
    }
    public String getRootGroupId() {
        return this.rootGroupId;
    }

}
