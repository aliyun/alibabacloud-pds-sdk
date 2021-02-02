// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

public class CreateAppModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public GetAppResponse body;

    public static CreateAppModel build(java.util.Map<String, ?> map) throws Exception {
        CreateAppModel self = new CreateAppModel();
        return TeaModel.build(map, self);
    }

    public CreateAppModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public CreateAppModel setBody(GetAppResponse body) {
        this.body = body;
        return this;
    }
    public GetAppResponse getBody() {
        return this.body;
    }

}
