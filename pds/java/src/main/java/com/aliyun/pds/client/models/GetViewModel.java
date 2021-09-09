// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class GetViewModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public GetViewResponse body;

    public static GetViewModel build(java.util.Map<String, ?> map) throws Exception {
        GetViewModel self = new GetViewModel();
        return TeaModel.build(map, self);
    }

    public GetViewModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetViewModel setBody(GetViewResponse body) {
        this.body = body;
        return this;
    }
    public GetViewResponse getBody() {
        return this.body;
    }

}
