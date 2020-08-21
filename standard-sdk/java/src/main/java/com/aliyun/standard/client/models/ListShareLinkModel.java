// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.standard.client.models;

import com.aliyun.tea.*;

public class ListShareLinkModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public ListShareLinkResponse body;

    public static ListShareLinkModel build(java.util.Map<String, ?> map) throws Exception {
        ListShareLinkModel self = new ListShareLinkModel();
        return TeaModel.build(map, self);
    }

    public ListShareLinkModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ListShareLinkModel setBody(ListShareLinkResponse body) {
        this.body = body;
        return this;
    }
    public ListShareLinkResponse getBody() {
        return this.body;
    }

}
