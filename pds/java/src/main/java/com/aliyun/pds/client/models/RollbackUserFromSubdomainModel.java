// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class RollbackUserFromSubdomainModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public RollbackUserFromSubdomainResponse body;

    public static RollbackUserFromSubdomainModel build(java.util.Map<String, ?> map) throws Exception {
        RollbackUserFromSubdomainModel self = new RollbackUserFromSubdomainModel();
        return TeaModel.build(map, self);
    }

    public RollbackUserFromSubdomainModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public RollbackUserFromSubdomainModel setBody(RollbackUserFromSubdomainResponse body) {
        this.body = body;
        return this;
    }
    public RollbackUserFromSubdomainResponse getBody() {
        return this.body;
    }

}
