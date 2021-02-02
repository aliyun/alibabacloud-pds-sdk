// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.hostingmode.client.models;

import com.aliyun.tea.*;

public class ListStorefileModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public ListStoreFileResponse body;

    public static ListStorefileModel build(java.util.Map<String, ?> map) throws Exception {
        ListStorefileModel self = new ListStorefileModel();
        return TeaModel.build(map, self);
    }

    public ListStorefileModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ListStorefileModel setBody(ListStoreFileResponse body) {
        this.body = body;
        return this;
    }
    public ListStoreFileResponse getBody() {
        return this.body;
    }

}
