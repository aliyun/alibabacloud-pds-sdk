// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

public class ListStoresModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public ListStoresResponse body;

    public static ListStoresModel build(java.util.Map<String, ?> map) throws Exception {
        ListStoresModel self = new ListStoresModel();
        return TeaModel.build(map, self);
    }

    public ListStoresModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ListStoresModel setBody(ListStoresResponse body) {
        this.body = body;
        return this;
    }
    public ListStoresResponse getBody() {
        return this.body;
    }

}
