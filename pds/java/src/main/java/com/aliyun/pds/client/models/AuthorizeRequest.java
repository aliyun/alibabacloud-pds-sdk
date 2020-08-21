// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class AuthorizeRequest extends TeaModel {
    // Client ID, 此处填写创建App时返回的AppID
    @NameInMap("ClientID")
    @Validation(required = true)
    public String ClientID;

    // 鉴权方式，目前支持ding,ram鉴权
    @NameInMap("LoginType")
    public String LoginType;

    // 回调地址, 此处填写创建App时填写的回调地址
    @NameInMap("RedirectUri")
    @Validation(required = true)
    public String RedirectUri;

    // 返回类型, 只能填写code
    @NameInMap("ResponseType")
    @Validation(required = true)
    public String ResponseType;

    // 申请的权限列表, 默认为所有权限
    @NameInMap("Scope")
    public java.util.List<String> Scope;

    // 用户自定义字段，会在鉴权成功后的callback带回
    @NameInMap("State")
    public String State;

    public static AuthorizeRequest build(java.util.Map<String, ?> map) throws Exception {
        AuthorizeRequest self = new AuthorizeRequest();
        return TeaModel.build(map, self);
    }

    public AuthorizeRequest setClientID(String ClientID) {
        this.ClientID = ClientID;
        return this;
    }
    public String getClientID() {
        return this.ClientID;
    }

    public AuthorizeRequest setLoginType(String LoginType) {
        this.LoginType = LoginType;
        return this;
    }
    public String getLoginType() {
        return this.LoginType;
    }

    public AuthorizeRequest setRedirectUri(String RedirectUri) {
        this.RedirectUri = RedirectUri;
        return this;
    }
    public String getRedirectUri() {
        return this.RedirectUri;
    }

    public AuthorizeRequest setResponseType(String ResponseType) {
        this.ResponseType = ResponseType;
        return this;
    }
    public String getResponseType() {
        return this.ResponseType;
    }

    public AuthorizeRequest setScope(java.util.List<String> Scope) {
        this.Scope = Scope;
        return this;
    }
    public java.util.List<String> getScope() {
        return this.Scope;
    }

    public AuthorizeRequest setState(String State) {
        this.State = State;
        return this;
    }
    public String getState() {
        return this.State;
    }

}
