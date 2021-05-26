// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class ListFileActivityModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public ListFileActivityResponse body;

    public static ListFileActivityModel build(java.util.Map<String, ?> map) throws Exception {
        ListFileActivityModel self = new ListFileActivityModel();
        return TeaModel.build(map, self);
    }

    public ListFileActivityModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ListFileActivityModel setBody(ListFileActivityResponse body) {
        this.body = body;
        return this;
    }
    public ListFileActivityResponse getBody() {
        return this.body;
    }

}
