// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

public class GetDriveModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public GetDriveResponse body;

    public static GetDriveModel build(java.util.Map<String, ?> map) throws Exception {
        GetDriveModel self = new GetDriveModel();
        return TeaModel.build(map, self);
    }

    public GetDriveModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetDriveModel setBody(GetDriveResponse body) {
        this.body = body;
        return this;
    }
    public GetDriveResponse getBody() {
        return this.body;
    }

}
