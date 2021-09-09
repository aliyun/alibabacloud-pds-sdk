// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class ListFileViewsModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public ListFileViewsResponse body;

    public static ListFileViewsModel build(java.util.Map<String, ?> map) throws Exception {
        ListFileViewsModel self = new ListFileViewsModel();
        return TeaModel.build(map, self);
    }

    public ListFileViewsModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ListFileViewsModel setBody(ListFileViewsResponse body) {
        this.body = body;
        return this;
    }
    public ListFileViewsResponse getBody() {
        return this.body;
    }

}
