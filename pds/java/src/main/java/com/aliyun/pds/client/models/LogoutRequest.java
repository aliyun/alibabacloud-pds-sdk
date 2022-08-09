// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 *
 */
public class LogoutRequest extends TeaModel {
    // 登出之后的跳转地址，默认跳转到App的域名下
    @NameInMap("BackUrl")
    public String BackUrl;

    // Client ID, 此处填写创建App时返回的AppID
    @NameInMap("ClientID")
    @Validation(required = true)
    public String ClientID;

    // 用户自定义字段，会在鉴权成功后的callback带回
    @NameInMap("LoginType")
    public String LoginType;

    public static LogoutRequest build(java.util.Map<String, ?> map) throws Exception {
        LogoutRequest self = new LogoutRequest();
        return TeaModel.build(map, self);
    }

    public LogoutRequest setBackUrl(String BackUrl) {
        this.BackUrl = BackUrl;
        return this;
    }
    public String getBackUrl() {
        return this.BackUrl;
    }

    public LogoutRequest setClientID(String ClientID) {
        this.ClientID = ClientID;
        return this;
    }
    public String getClientID() {
        return this.ClientID;
    }

    public LogoutRequest setLoginType(String LoginType) {
        this.LoginType = LoginType;
        return this;
    }
    public String getLoginType() {
        return this.LoginType;
    }

}
