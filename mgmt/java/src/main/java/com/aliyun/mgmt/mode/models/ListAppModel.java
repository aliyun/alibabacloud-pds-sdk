// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.mgmt.mode.models;

import com.aliyun.tea.*;

public class ListAppModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public ListAppsResponse body;

    public static ListAppModel build(java.util.Map<String, ?> map) throws Exception {
        ListAppModel self = new ListAppModel();
        return TeaModel.build(map, self);
    }

    public ListAppModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ListAppModel setBody(ListAppsResponse body) {
        this.body = body;
        return this;
    }
    public ListAppsResponse getBody() {
        return this.body;
    }

}
