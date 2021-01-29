// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

public class GetOfficePreviewUrlModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public GetOfficePreviewUrlResponse body;

    public static GetOfficePreviewUrlModel build(java.util.Map<String, ?> map) throws Exception {
        GetOfficePreviewUrlModel self = new GetOfficePreviewUrlModel();
        return TeaModel.build(map, self);
    }

    public GetOfficePreviewUrlModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetOfficePreviewUrlModel setBody(GetOfficePreviewUrlResponse body) {
        this.body = body;
        return this;
    }
    public GetOfficePreviewUrlResponse getBody() {
        return this.body;
    }

}
