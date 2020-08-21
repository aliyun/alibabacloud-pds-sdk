// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.standard.client.models;

import com.aliyun.tea.*;

public class AdminListStoresModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public ListStoresResponse body;

    public static AdminListStoresModel build(java.util.Map<String, ?> map) throws Exception {
        AdminListStoresModel self = new AdminListStoresModel();
        return TeaModel.build(map, self);
    }

    public AdminListStoresModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public AdminListStoresModel setBody(ListStoresResponse body) {
        this.body = body;
        return this;
    }
    public ListStoresResponse getBody() {
        return this.body;
    }

}
