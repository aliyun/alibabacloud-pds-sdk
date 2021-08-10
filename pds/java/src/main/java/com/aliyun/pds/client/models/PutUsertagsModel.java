// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class PutUsertagsModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public PutFileUserTagsResponse body;

    public static PutUsertagsModel build(java.util.Map<String, ?> map) throws Exception {
        PutUsertagsModel self = new PutUsertagsModel();
        return TeaModel.build(map, self);
    }

    public PutUsertagsModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public PutUsertagsModel setBody(PutFileUserTagsResponse body) {
        this.body = body;
        return this;
    }
    public PutFileUserTagsResponse getBody() {
        return this.body;
    }

}
