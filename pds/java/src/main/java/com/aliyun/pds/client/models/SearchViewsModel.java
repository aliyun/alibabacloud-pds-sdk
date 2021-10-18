// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class SearchViewsModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public SearchViewsResponse body;

    public static SearchViewsModel build(java.util.Map<String, ?> map) throws Exception {
        SearchViewsModel self = new SearchViewsModel();
        return TeaModel.build(map, self);
    }

    public SearchViewsModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public SearchViewsModel setBody(SearchViewsResponse body) {
        this.body = body;
        return this;
    }
    public SearchViewsResponse getBody() {
        return this.body;
    }

}
