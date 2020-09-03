// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

public class ListShareModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public ListShareResponse body;

    public static ListShareModel build(java.util.Map<String, ?> map) throws Exception {
        ListShareModel self = new ListShareModel();
        return TeaModel.build(map, self);
    }

    public ListShareModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ListShareModel setBody(ListShareResponse body) {
        this.body = body;
        return this;
    }
    public ListShareResponse getBody() {
        return this.body;
    }

}
