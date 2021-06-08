// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class ImportUserModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public BaseUserResponse body;

    public static ImportUserModel build(java.util.Map<String, ?> map) throws Exception {
        ImportUserModel self = new ImportUserModel();
        return TeaModel.build(map, self);
    }

    public ImportUserModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ImportUserModel setBody(BaseUserResponse body) {
        this.body = body;
        return this;
    }
    public BaseUserResponse getBody() {
        return this.body;
    }

}
