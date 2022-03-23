// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class DeleteSyncMappingModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public DeleteSyncMappingResponse body;

    public static DeleteSyncMappingModel build(java.util.Map<String, ?> map) throws Exception {
        DeleteSyncMappingModel self = new DeleteSyncMappingModel();
        return TeaModel.build(map, self);
    }

    public DeleteSyncMappingModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public DeleteSyncMappingModel setBody(DeleteSyncMappingResponse body) {
        this.body = body;
        return this;
    }
    public DeleteSyncMappingResponse getBody() {
        return this.body;
    }

}
