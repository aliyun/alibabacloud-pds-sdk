// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

public class SearchFileModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public SearchFileResponse body;

    public static SearchFileModel build(java.util.Map<String, ?> map) throws Exception {
        SearchFileModel self = new SearchFileModel();
        return TeaModel.build(map, self);
    }

    public SearchFileModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public SearchFileModel setBody(SearchFileResponse body) {
        this.body = body;
        return this;
    }
    public SearchFileResponse getBody() {
        return this.body;
    }

}
