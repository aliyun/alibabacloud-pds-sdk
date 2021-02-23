// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class DeleteSubdomainModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public DeleteSubdomainResponse body;

    public static DeleteSubdomainModel build(java.util.Map<String, ?> map) throws Exception {
        DeleteSubdomainModel self = new DeleteSubdomainModel();
        return TeaModel.build(map, self);
    }

    public DeleteSubdomainModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public DeleteSubdomainModel setBody(DeleteSubdomainResponse body) {
        this.body = body;
        return this;
    }
    public DeleteSubdomainResponse getBody() {
        return this.body;
    }

}
