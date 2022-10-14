// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class SearchShareLinkModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public SearchShareLinkResponse body;

    public static SearchShareLinkModel build(java.util.Map<String, ?> map) throws Exception {
        SearchShareLinkModel self = new SearchShareLinkModel();
        return TeaModel.build(map, self);
    }

    public SearchShareLinkModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public SearchShareLinkModel setBody(SearchShareLinkResponse body) {
        this.body = body;
        return this;
    }
    public SearchShareLinkResponse getBody() {
        return this.body;
    }

}
