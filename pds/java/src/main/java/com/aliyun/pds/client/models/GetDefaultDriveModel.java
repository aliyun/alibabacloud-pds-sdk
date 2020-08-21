// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class GetDefaultDriveModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public GetDriveResponse body;

    public static GetDefaultDriveModel build(java.util.Map<String, ?> map) throws Exception {
        GetDefaultDriveModel self = new GetDefaultDriveModel();
        return TeaModel.build(map, self);
    }

    public GetDefaultDriveModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetDefaultDriveModel setBody(GetDriveResponse body) {
        this.body = body;
        return this;
    }
    public GetDriveResponse getBody() {
        return this.body;
    }

}
