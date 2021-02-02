// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.hostingmode.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class AccountLinkRequest extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // 账号信息
    @NameInMap("detail")
    public String detail;

    // 额外的信息，比如type为mobile时，此字段为国家编号，不填默认86
    @NameInMap("extra")
    public String extra;

    // 唯一身份标识
    @NameInMap("identity")
    @Validation(required = true)
    public String identity;

    // 状态
    @NameInMap("status")
    public String status;

    // 认证类型
    @NameInMap("type")
    @Validation(required = true)
    public String type;

    // 绑定的user_id
    @NameInMap("user_id")
    @Validation(required = true)
    public String userId;

    public static AccountLinkRequest build(java.util.Map<String, ?> map) throws Exception {
        AccountLinkRequest self = new AccountLinkRequest();
        return TeaModel.build(map, self);
    }

    public AccountLinkRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public AccountLinkRequest setDetail(String detail) {
        this.detail = detail;
        return this;
    }
    public String getDetail() {
        return this.detail;
    }

    public AccountLinkRequest setExtra(String extra) {
        this.extra = extra;
        return this;
    }
    public String getExtra() {
        return this.extra;
    }

    public AccountLinkRequest setIdentity(String identity) {
        this.identity = identity;
        return this;
    }
    public String getIdentity() {
        return this.identity;
    }

    public AccountLinkRequest setStatus(String status) {
        this.status = status;
        return this;
    }
    public String getStatus() {
        return this.status;
    }

    public AccountLinkRequest setType(String type) {
        this.type = type;
        return this;
    }
    public String getType() {
        return this.type;
    }

    public AccountLinkRequest setUserId(String userId) {
        this.userId = userId;
        return this;
    }
    public String getUserId() {
        return this.userId;
    }

}
