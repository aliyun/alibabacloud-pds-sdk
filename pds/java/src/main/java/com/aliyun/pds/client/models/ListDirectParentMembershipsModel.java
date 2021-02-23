// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class ListDirectParentMembershipsModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public ListDirectParentMembershipsResponse body;

    public static ListDirectParentMembershipsModel build(java.util.Map<String, ?> map) throws Exception {
        ListDirectParentMembershipsModel self = new ListDirectParentMembershipsModel();
        return TeaModel.build(map, self);
    }

    public ListDirectParentMembershipsModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ListDirectParentMembershipsModel setBody(ListDirectParentMembershipsResponse body) {
        this.body = body;
        return this;
    }
    public ListDirectParentMembershipsResponse getBody() {
        return this.body;
    }

}
