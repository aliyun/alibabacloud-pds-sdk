// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class CreateSyncMappingModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public CreateSyncMappingResponse body;

    public static CreateSyncMappingModel build(java.util.Map<String, ?> map) throws Exception {
        CreateSyncMappingModel self = new CreateSyncMappingModel();
        return TeaModel.build(map, self);
    }

    public CreateSyncMappingModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public CreateSyncMappingModel setBody(CreateSyncMappingResponse body) {
        this.body = body;
        return this;
    }
    public CreateSyncMappingResponse getBody() {
        return this.body;
    }

}
