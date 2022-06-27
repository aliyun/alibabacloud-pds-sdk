// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class ViewSearchFileModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public SearchViewsResponse body;

    public static ViewSearchFileModel build(java.util.Map<String, ?> map) throws Exception {
        ViewSearchFileModel self = new ViewSearchFileModel();
        return TeaModel.build(map, self);
    }

    public ViewSearchFileModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ViewSearchFileModel setBody(SearchViewsResponse body) {
        this.body = body;
        return this;
    }
    public SearchViewsResponse getBody() {
        return this.body;
    }

}
