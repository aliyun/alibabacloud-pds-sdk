// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class AuthConfig extends TeaModel {
    @NameInMap("app_id")
    public String appId;

    @NameInMap("app_secret")
    public String appSecret;

    @NameInMap("callback_security")
    public Boolean callbackSecurity;

    @NameInMap("enable")
    public Boolean enable;

    @NameInMap("endpoint")
    public String endpoint;

    @NameInMap("enterprise_id")
    public String enterpriseId;

    @NameInMap("ldap_config")
    public LdapConfig ldapConfig;

    @NameInMap("login_page_headers")
    public java.util.Map<String, ?> loginPageHeaders;

    @NameInMap("login_page_template")
    public String loginPageTemplate;

    @NameInMap("login_page_vars")
    public java.util.Map<String, ?> loginPageVars;

    @NameInMap("white_list_config")
    public java.util.Map<String, ?> whiteListConfig;

    @NameInMap("white_list_enable")
    public Boolean whiteListEnable;

    public static AuthConfig build(java.util.Map<String, ?> map) throws Exception {
        AuthConfig self = new AuthConfig();
        return TeaModel.build(map, self);
    }

    public AuthConfig setAppId(String appId) {
        this.appId = appId;
        return this;
    }
    public String getAppId() {
        return this.appId;
    }

    public AuthConfig setAppSecret(String appSecret) {
        this.appSecret = appSecret;
        return this;
    }
    public String getAppSecret() {
        return this.appSecret;
    }

    public AuthConfig setCallbackSecurity(Boolean callbackSecurity) {
        this.callbackSecurity = callbackSecurity;
        return this;
    }
    public Boolean getCallbackSecurity() {
        return this.callbackSecurity;
    }

    public AuthConfig setEnable(Boolean enable) {
        this.enable = enable;
        return this;
    }
    public Boolean getEnable() {
        return this.enable;
    }

    public AuthConfig setEndpoint(String endpoint) {
        this.endpoint = endpoint;
        return this;
    }
    public String getEndpoint() {
        return this.endpoint;
    }

    public AuthConfig setEnterpriseId(String enterpriseId) {
        this.enterpriseId = enterpriseId;
        return this;
    }
    public String getEnterpriseId() {
        return this.enterpriseId;
    }

    public AuthConfig setLdapConfig(LdapConfig ldapConfig) {
        this.ldapConfig = ldapConfig;
        return this;
    }
    public LdapConfig getLdapConfig() {
        return this.ldapConfig;
    }

    public AuthConfig setLoginPageHeaders(java.util.Map<String, ?> loginPageHeaders) {
        this.loginPageHeaders = loginPageHeaders;
        return this;
    }
    public java.util.Map<String, ?> getLoginPageHeaders() {
        return this.loginPageHeaders;
    }

    public AuthConfig setLoginPageTemplate(String loginPageTemplate) {
        this.loginPageTemplate = loginPageTemplate;
        return this;
    }
    public String getLoginPageTemplate() {
        return this.loginPageTemplate;
    }

    public AuthConfig setLoginPageVars(java.util.Map<String, ?> loginPageVars) {
        this.loginPageVars = loginPageVars;
        return this;
    }
    public java.util.Map<String, ?> getLoginPageVars() {
        return this.loginPageVars;
    }

    public AuthConfig setWhiteListConfig(java.util.Map<String, ?> whiteListConfig) {
        this.whiteListConfig = whiteListConfig;
        return this;
    }
    public java.util.Map<String, ?> getWhiteListConfig() {
        return this.whiteListConfig;
    }

    public AuthConfig setWhiteListEnable(Boolean whiteListEnable) {
        this.whiteListEnable = whiteListEnable;
        return this;
    }
    public Boolean getWhiteListEnable() {
        return this.whiteListEnable;
    }

}
