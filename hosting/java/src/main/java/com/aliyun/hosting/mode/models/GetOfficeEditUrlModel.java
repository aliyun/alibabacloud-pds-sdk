// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

public class GetOfficeEditUrlModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public GetOfficeEditUrlResponse body;

    public static GetOfficeEditUrlModel build(java.util.Map<String, ?> map) throws Exception {
        GetOfficeEditUrlModel self = new GetOfficeEditUrlModel();
        return TeaModel.build(map, self);
    }

    public GetOfficeEditUrlModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetOfficeEditUrlModel setBody(GetOfficeEditUrlResponse body) {
        this.body = body;
        return this;
    }
    public GetOfficeEditUrlResponse getBody() {
        return this.body;
    }

}
