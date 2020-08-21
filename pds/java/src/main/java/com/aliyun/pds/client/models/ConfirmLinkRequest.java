// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class ConfirmLinkRequest extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // 待绑定的临时token，此token只能访问绑定、取消绑定接口
    @NameInMap("temporary_token")
    @Validation(required = true)
    public String temporaryToken;

    public static ConfirmLinkRequest build(java.util.Map<String, ?> map) throws Exception {
        ConfirmLinkRequest self = new ConfirmLinkRequest();
        return TeaModel.build(map, self);
    }

    public ConfirmLinkRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ConfirmLinkRequest setTemporaryToken(String temporaryToken) {
        this.temporaryToken = temporaryToken;
        return this;
    }
    public String getTemporaryToken() {
        return this.temporaryToken;
    }

}
