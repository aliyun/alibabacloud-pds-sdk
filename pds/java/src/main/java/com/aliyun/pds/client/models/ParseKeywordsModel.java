// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class ParseKeywordsModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public ParseKeywordsResponse body;

    public static ParseKeywordsModel build(java.util.Map<String, ?> map) throws Exception {
        ParseKeywordsModel self = new ParseKeywordsModel();
        return TeaModel.build(map, self);
    }

    public ParseKeywordsModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ParseKeywordsModel setBody(ParseKeywordsResponse body) {
        this.body = body;
        return this;
    }
    public ParseKeywordsResponse getBody() {
        return this.body;
    }

}
