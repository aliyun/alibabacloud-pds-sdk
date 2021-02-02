// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.hostingmode.client.models;

import com.aliyun.tea.*;

public class GetDownloadUrlModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public HostingGetDownloadUrlResponse body;

    public static GetDownloadUrlModel build(java.util.Map<String, ?> map) throws Exception {
        GetDownloadUrlModel self = new GetDownloadUrlModel();
        return TeaModel.build(map, self);
    }

    public GetDownloadUrlModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetDownloadUrlModel setBody(HostingGetDownloadUrlResponse body) {
        this.body = body;
        return this;
    }
    public HostingGetDownloadUrlResponse getBody() {
        return this.body;
    }

}
