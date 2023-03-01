// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class ImageSimpleQueryModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public SimpleQueryResponse body;

    public static ImageSimpleQueryModel build(java.util.Map<String, ?> map) throws Exception {
        ImageSimpleQueryModel self = new ImageSimpleQueryModel();
        return TeaModel.build(map, self);
    }

    public ImageSimpleQueryModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ImageSimpleQueryModel setBody(SimpleQueryResponse body) {
        this.body = body;
        return this;
    }
    public SimpleQueryResponse getBody() {
        return this.body;
    }

}
