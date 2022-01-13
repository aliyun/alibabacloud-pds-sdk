// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class ListSyncMappingModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public ListSyncMappingResponse body;

    public static ListSyncMappingModel build(java.util.Map<String, ?> map) throws Exception {
        ListSyncMappingModel self = new ListSyncMappingModel();
        return TeaModel.build(map, self);
    }

    public ListSyncMappingModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ListSyncMappingModel setBody(ListSyncMappingResponse body) {
        this.body = body;
        return this;
    }
    public ListSyncMappingResponse getBody() {
        return this.body;
    }

}
