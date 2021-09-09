// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class ListViewsModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public ListViewsResponse body;

    public static ListViewsModel build(java.util.Map<String, ?> map) throws Exception {
        ListViewsModel self = new ListViewsModel();
        return TeaModel.build(map, self);
    }

    public ListViewsModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ListViewsModel setBody(ListViewsResponse body) {
        this.body = body;
        return this;
    }
    public ListViewsResponse getBody() {
        return this.body;
    }

}
