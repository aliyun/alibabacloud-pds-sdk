// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.standard.client.models;

import com.aliyun.tea.*;

public class ListFileByAnonymousModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public ListByAnonymousResponse body;

    public static ListFileByAnonymousModel build(java.util.Map<String, ?> map) throws Exception {
        ListFileByAnonymousModel self = new ListFileByAnonymousModel();
        return TeaModel.build(map, self);
    }

    public ListFileByAnonymousModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ListFileByAnonymousModel setBody(ListByAnonymousResponse body) {
        this.body = body;
        return this;
    }
    public ListByAnonymousResponse getBody() {
        return this.body;
    }

}
