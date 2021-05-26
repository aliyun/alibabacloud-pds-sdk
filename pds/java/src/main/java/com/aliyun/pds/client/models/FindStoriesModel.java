// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class FindStoriesModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public FindStoriesResponse body;

    public static FindStoriesModel build(java.util.Map<String, ?> map) throws Exception {
        FindStoriesModel self = new FindStoriesModel();
        return TeaModel.build(map, self);
    }

    public FindStoriesModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public FindStoriesModel setBody(FindStoriesResponse body) {
        this.body = body;
        return this;
    }
    public FindStoriesResponse getBody() {
        return this.body;
    }

}
