// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class SearchModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public SearchPermissionResponse body;

    public static SearchModel build(java.util.Map<String, ?> map) throws Exception {
        SearchModel self = new SearchModel();
        return TeaModel.build(map, self);
    }

    public SearchModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public SearchModel setBody(SearchPermissionResponse body) {
        this.body = body;
        return this;
    }
    public SearchPermissionResponse getBody() {
        return this.body;
    }

}
