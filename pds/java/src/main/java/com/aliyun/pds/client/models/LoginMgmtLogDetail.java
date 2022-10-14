// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 *
 */
public class LoginMgmtLogDetail extends TeaModel {
    // app_id
    @NameInMap("app_id")
    public String appId;

    @NameInMap("ding_sync_config")
    public DingSyncConfig dingSyncConfig;

    // enable
    @NameInMap("enable")
    public Boolean enable;

    @NameInMap("ldap_config")
    public LdapConfig ldapConfig;

    @NameInMap("wechat_sync_config")
    public WeChatSyncConfig wechatSyncConfig;

    public static LoginMgmtLogDetail build(java.util.Map<String, ?> map) throws Exception {
        LoginMgmtLogDetail self = new LoginMgmtLogDetail();
        return TeaModel.build(map, self);
    }

    public LoginMgmtLogDetail setAppId(String appId) {
        this.appId = appId;
        return this;
    }
    public String getAppId() {
        return this.appId;
    }

    public LoginMgmtLogDetail setDingSyncConfig(DingSyncConfig dingSyncConfig) {
        this.dingSyncConfig = dingSyncConfig;
        return this;
    }
    public DingSyncConfig getDingSyncConfig() {
        return this.dingSyncConfig;
    }

    public LoginMgmtLogDetail setEnable(Boolean enable) {
        this.enable = enable;
        return this;
    }
    public Boolean getEnable() {
        return this.enable;
    }

    public LoginMgmtLogDetail setLdapConfig(LdapConfig ldapConfig) {
        this.ldapConfig = ldapConfig;
        return this;
    }
    public LdapConfig getLdapConfig() {
        return this.ldapConfig;
    }

    public LoginMgmtLogDetail setWechatSyncConfig(WeChatSyncConfig wechatSyncConfig) {
        this.wechatSyncConfig = wechatSyncConfig;
        return this;
    }
    public WeChatSyncConfig getWechatSyncConfig() {
        return this.wechatSyncConfig;
    }

}
