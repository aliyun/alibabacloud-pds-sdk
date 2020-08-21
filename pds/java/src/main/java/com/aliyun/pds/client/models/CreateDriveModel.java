// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class CreateDriveModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public CreateDriveResponse body;

    public static CreateDriveModel build(java.util.Map<String, ?> map) throws Exception {
        CreateDriveModel self = new CreateDriveModel();
        return TeaModel.build(map, self);
    }

    public CreateDriveModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public CreateDriveModel setBody(CreateDriveResponse body) {
        this.body = body;
        return this;
    }
    public CreateDriveResponse getBody() {
        return this.body;
    }

}
