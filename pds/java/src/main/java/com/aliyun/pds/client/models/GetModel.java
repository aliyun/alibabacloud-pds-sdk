// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class GetModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public BasePermissionResponse body;

    public static GetModel build(java.util.Map<String, ?> map) throws Exception {
        GetModel self = new GetModel();
        return TeaModel.build(map, self);
    }

    public GetModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetModel setBody(BasePermissionResponse body) {
        this.body = body;
        return this;
    }
    public BasePermissionResponse getBody() {
        return this.body;
    }

}
