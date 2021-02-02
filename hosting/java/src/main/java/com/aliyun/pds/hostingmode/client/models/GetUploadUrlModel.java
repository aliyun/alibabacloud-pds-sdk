// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.hostingmode.client.models;

import com.aliyun.tea.*;

public class GetUploadUrlModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public HostingGetUploadUrlResponse body;

    public static GetUploadUrlModel build(java.util.Map<String, ?> map) throws Exception {
        GetUploadUrlModel self = new GetUploadUrlModel();
        return TeaModel.build(map, self);
    }

    public GetUploadUrlModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetUploadUrlModel setBody(HostingGetUploadUrlResponse body) {
        this.body = body;
        return this;
    }
    public HostingGetUploadUrlResponse getBody() {
        return this.body;
    }

}
