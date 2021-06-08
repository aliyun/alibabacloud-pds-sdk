// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class ListRecyclebinModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public ListFileResponse body;

    public static ListRecyclebinModel build(java.util.Map<String, ?> map) throws Exception {
        ListRecyclebinModel self = new ListRecyclebinModel();
        return TeaModel.build(map, self);
    }

    public ListRecyclebinModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ListRecyclebinModel setBody(ListFileResponse body) {
        this.body = body;
        return this;
    }
    public ListFileResponse getBody() {
        return this.body;
    }

}
