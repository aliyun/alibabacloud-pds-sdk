// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class LoginMgmtLogDetail extends TeaModel {
    // app_id
    @NameInMap("app_id")
    public String appId;

    // enable
    @NameInMap("enable")
    public Boolean enable;

    @NameInMap("ldap_config")
    public LdapConfig ldapConfig;

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

}
