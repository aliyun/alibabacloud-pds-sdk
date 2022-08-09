// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class ListModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public ListPermissionResponse body;

    public static ListModel build(java.util.Map<String, ?> map) throws Exception {
        ListModel self = new ListModel();
        return TeaModel.build(map, self);
    }

    public ListModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ListModel setBody(ListPermissionResponse body) {
        this.body = body;
        return this;
    }
    public ListPermissionResponse getBody() {
        return this.body;
    }

}
