// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class MigrateUserToSubdomainModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public MigrateUserToSubdomainResponse body;

    public static MigrateUserToSubdomainModel build(java.util.Map<String, ?> map) throws Exception {
        MigrateUserToSubdomainModel self = new MigrateUserToSubdomainModel();
        return TeaModel.build(map, self);
    }

    public MigrateUserToSubdomainModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public MigrateUserToSubdomainModel setBody(MigrateUserToSubdomainResponse body) {
        this.body = body;
        return this;
    }
    public MigrateUserToSubdomainResponse getBody() {
        return this.body;
    }

}
