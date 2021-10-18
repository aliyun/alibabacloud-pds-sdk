// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class SendSmsCodeModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public SendSmsCodeResponse body;

    public static SendSmsCodeModel build(java.util.Map<String, ?> map) throws Exception {
        SendSmsCodeModel self = new SendSmsCodeModel();
        return TeaModel.build(map, self);
    }

    public SendSmsCodeModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public SendSmsCodeModel setBody(SendSmsCodeResponse body) {
        this.body = body;
        return this;
    }
    public SendSmsCodeResponse getBody() {
        return this.body;
    }

}
