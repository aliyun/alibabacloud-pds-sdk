// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class GetShareLinkDownloadUrlModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public GetShareLinkDownloadURLResponse body;

    public static GetShareLinkDownloadUrlModel build(java.util.Map<String, ?> map) throws Exception {
        GetShareLinkDownloadUrlModel self = new GetShareLinkDownloadUrlModel();
        return TeaModel.build(map, self);
    }

    public GetShareLinkDownloadUrlModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetShareLinkDownloadUrlModel setBody(GetShareLinkDownloadURLResponse body) {
        this.body = body;
        return this;
    }
    public GetShareLinkDownloadURLResponse getBody() {
        return this.body;
    }

}
