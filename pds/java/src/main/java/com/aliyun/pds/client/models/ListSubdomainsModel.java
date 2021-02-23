// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class ListSubdomainsModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public ListSubdomainsResponse body;

    public static ListSubdomainsModel build(java.util.Map<String, ?> map) throws Exception {
        ListSubdomainsModel self = new ListSubdomainsModel();
        return TeaModel.build(map, self);
    }

    public ListSubdomainsModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ListSubdomainsModel setBody(ListSubdomainsResponse body) {
        this.body = body;
        return this;
    }
    public ListSubdomainsResponse getBody() {
        return this.body;
    }

}
