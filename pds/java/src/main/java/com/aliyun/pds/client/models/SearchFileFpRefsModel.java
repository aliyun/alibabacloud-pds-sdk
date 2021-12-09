// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class SearchFileFpRefsModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public SearchFileFpRefsResponse body;

    public static SearchFileFpRefsModel build(java.util.Map<String, ?> map) throws Exception {
        SearchFileFpRefsModel self = new SearchFileFpRefsModel();
        return TeaModel.build(map, self);
    }

    public SearchFileFpRefsModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public SearchFileFpRefsModel setBody(SearchFileFpRefsResponse body) {
        this.body = body;
        return this;
    }
    public SearchFileFpRefsResponse getBody() {
        return this.body;
    }

}
