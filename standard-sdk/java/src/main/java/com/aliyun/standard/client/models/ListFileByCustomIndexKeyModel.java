// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.standard.client.models;

import com.aliyun.tea.*;

public class ListFileByCustomIndexKeyModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public ListFileResponse body;

    public static ListFileByCustomIndexKeyModel build(java.util.Map<String, ?> map) throws Exception {
        ListFileByCustomIndexKeyModel self = new ListFileByCustomIndexKeyModel();
        return TeaModel.build(map, self);
    }

    public ListFileByCustomIndexKeyModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ListFileByCustomIndexKeyModel setBody(ListFileResponse body) {
        this.body = body;
        return this;
    }
    public ListFileResponse getBody() {
        return this.body;
    }

}
