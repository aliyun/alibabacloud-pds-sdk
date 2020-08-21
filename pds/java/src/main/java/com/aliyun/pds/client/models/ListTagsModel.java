// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class ListTagsModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public ListImageTagsResponse body;

    public static ListTagsModel build(java.util.Map<String, ?> map) throws Exception {
        ListTagsModel self = new ListTagsModel();
        return TeaModel.build(map, self);
    }

    public ListTagsModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ListTagsModel setBody(ListImageTagsResponse body) {
        this.body = body;
        return this;
    }
    public ListImageTagsResponse getBody() {
        return this.body;
    }

}
