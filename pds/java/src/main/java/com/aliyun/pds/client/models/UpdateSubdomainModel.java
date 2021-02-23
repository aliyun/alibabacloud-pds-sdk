// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class UpdateSubdomainModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public UpdateSubdomainResponse body;

    public static UpdateSubdomainModel build(java.util.Map<String, ?> map) throws Exception {
        UpdateSubdomainModel self = new UpdateSubdomainModel();
        return TeaModel.build(map, self);
    }

    public UpdateSubdomainModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public UpdateSubdomainModel setBody(UpdateSubdomainResponse body) {
        this.body = body;
        return this;
    }
    public UpdateSubdomainResponse getBody() {
        return this.body;
    }

}
