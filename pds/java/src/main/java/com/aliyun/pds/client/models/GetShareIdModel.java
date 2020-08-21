// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class GetShareIdModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public GetShareLinkIDResponse body;

    public static GetShareIdModel build(java.util.Map<String, ?> map) throws Exception {
        GetShareIdModel self = new GetShareIdModel();
        return TeaModel.build(map, self);
    }

    public GetShareIdModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetShareIdModel setBody(GetShareLinkIDResponse body) {
        this.body = body;
        return this;
    }
    public GetShareLinkIDResponse getBody() {
        return this.body;
    }

}
