// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class LDAPSyncConfig extends TeaModel {
    @NameInMap("cron")
    public String cron;

    @NameInMap("enabled")
    public Boolean enabled;

    @NameInMap("group_filter")
    public String groupFilter;

    @NameInMap("group_object_class")
    public String groupObjectClass;

    @NameInMap("user_filter")
    public String userFilter;

    @NameInMap("user_object_class")
    public String userObjectClass;

    public static LDAPSyncConfig build(java.util.Map<String, ?> map) throws Exception {
        LDAPSyncConfig self = new LDAPSyncConfig();
        return TeaModel.build(map, self);
    }

    public LDAPSyncConfig setCron(String cron) {
        this.cron = cron;
        return this;
    }
    public String getCron() {
        return this.cron;
    }

    public LDAPSyncConfig setEnabled(Boolean enabled) {
        this.enabled = enabled;
        return this;
    }
    public Boolean getEnabled() {
        return this.enabled;
    }

    public LDAPSyncConfig setGroupFilter(String groupFilter) {
        this.groupFilter = groupFilter;
        return this;
    }
    public String getGroupFilter() {
        return this.groupFilter;
    }

    public LDAPSyncConfig setGroupObjectClass(String groupObjectClass) {
        this.groupObjectClass = groupObjectClass;
        return this;
    }
    public String getGroupObjectClass() {
        return this.groupObjectClass;
    }

    public LDAPSyncConfig setUserFilter(String userFilter) {
        this.userFilter = userFilter;
        return this;
    }
    public String getUserFilter() {
        return this.userFilter;
    }

    public LDAPSyncConfig setUserObjectClass(String userObjectClass) {
        this.userObjectClass = userObjectClass;
        return this;
    }
    public String getUserObjectClass() {
        return this.userObjectClass;
    }

}
