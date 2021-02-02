// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.hostingmode.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class GetCaptchaRequest extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // App ID, 当前访问的App
    @NameInMap("app_id")
    @Validation(required = true)
    public String appId;

    public static GetCaptchaRequest build(java.util.Map<String, ?> map) throws Exception {
        GetCaptchaRequest self = new GetCaptchaRequest();
        return TeaModel.build(map, self);
    }

    public GetCaptchaRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetCaptchaRequest setAppId(String appId) {
        this.appId = appId;
        return this;
    }
    public String getAppId() {
        return this.appId;
    }

}
