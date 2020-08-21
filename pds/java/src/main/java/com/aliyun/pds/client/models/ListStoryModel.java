// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class ListStoryModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public ListStoryResponse body;

    public static ListStoryModel build(java.util.Map<String, ?> map) throws Exception {
        ListStoryModel self = new ListStoryModel();
        return TeaModel.build(map, self);
    }

    public ListStoryModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ListStoryModel setBody(ListStoryResponse body) {
        this.body = body;
        return this;
    }
    public ListStoryResponse getBody() {
        return this.body;
    }

}
