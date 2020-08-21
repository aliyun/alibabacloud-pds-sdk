// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class GetCaptchaModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public Captcha body;

    public static GetCaptchaModel build(java.util.Map<String, ?> map) throws Exception {
        GetCaptchaModel self = new GetCaptchaModel();
        return TeaModel.build(map, self);
    }

    public GetCaptchaModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetCaptchaModel setBody(Captcha body) {
        this.body = body;
        return this;
    }
    public Captcha getBody() {
        return this.body;
    }

}
