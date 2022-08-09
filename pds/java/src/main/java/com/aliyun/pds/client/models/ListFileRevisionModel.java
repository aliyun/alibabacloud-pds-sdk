// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class ListFileRevisionModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public ListRevisionResponse body;

    public static ListFileRevisionModel build(java.util.Map<String, ?> map) throws Exception {
        ListFileRevisionModel self = new ListFileRevisionModel();
        return TeaModel.build(map, self);
    }

    public ListFileRevisionModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ListFileRevisionModel setBody(ListRevisionResponse body) {
        this.body = body;
        return this;
    }
    public ListRevisionResponse getBody() {
        return this.body;
    }

}
