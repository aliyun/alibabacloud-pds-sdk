// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class LdapConfig extends TeaModel {
    @NameInMap("admin_dn")
    public String adminDn;

    @NameInMap("admin_password")
    public String adminPassword;

    @NameInMap("base_dn")
    public String baseDn;

    @NameInMap("display_name_key")
    public String displayNameKey;

    @NameInMap("global_uid")
    public String globalUid;

    @NameInMap("host")
    public String host;

    @NameInMap("port")
    public Long port;

    @NameInMap("sync_config")
    public LDAPSyncConfig syncConfig;

    @NameInMap("type")
    public String type;

    @NameInMap("uid")
    public String uid;

    @NameInMap("version")
    public String version;

    public static LdapConfig build(java.util.Map<String, ?> map) throws Exception {
        LdapConfig self = new LdapConfig();
        return TeaModel.build(map, self);
    }

    public LdapConfig setAdminDn(String adminDn) {
        this.adminDn = adminDn;
        return this;
    }
    public String getAdminDn() {
        return this.adminDn;
    }

    public LdapConfig setAdminPassword(String adminPassword) {
        this.adminPassword = adminPassword;
        return this;
    }
    public String getAdminPassword() {
        return this.adminPassword;
    }

    public LdapConfig setBaseDn(String baseDn) {
        this.baseDn = baseDn;
        return this;
    }
    public String getBaseDn() {
        return this.baseDn;
    }

    public LdapConfig setDisplayNameKey(String displayNameKey) {
        this.displayNameKey = displayNameKey;
        return this;
    }
    public String getDisplayNameKey() {
        return this.displayNameKey;
    }

    public LdapConfig setGlobalUid(String globalUid) {
        this.globalUid = globalUid;
        return this;
    }
    public String getGlobalUid() {
        return this.globalUid;
    }

    public LdapConfig setHost(String host) {
        this.host = host;
        return this;
    }
    public String getHost() {
        return this.host;
    }

    public LdapConfig setPort(Long port) {
        this.port = port;
        return this;
    }
    public Long getPort() {
        return this.port;
    }

    public LdapConfig setSyncConfig(LDAPSyncConfig syncConfig) {
        this.syncConfig = syncConfig;
        return this;
    }
    public LDAPSyncConfig getSyncConfig() {
        return this.syncConfig;
    }

    public LdapConfig setType(String type) {
        this.type = type;
        return this;
    }
    public String getType() {
        return this.type;
    }

    public LdapConfig setUid(String uid) {
        this.uid = uid;
        return this;
    }
    public String getUid() {
        return this.uid;
    }

    public LdapConfig setVersion(String version) {
        this.version = version;
        return this;
    }
    public String getVersion() {
        return this.version;
    }

}
