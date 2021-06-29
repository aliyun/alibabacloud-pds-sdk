// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class DeleteStoryModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public DeleteStoryResponse body;

    public static DeleteStoryModel build(java.util.Map<String, ?> map) throws Exception {
        DeleteStoryModel self = new DeleteStoryModel();
        return TeaModel.build(map, self);
    }

    public DeleteStoryModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public DeleteStoryModel setBody(DeleteStoryResponse body) {
        this.body = body;
        return this;
    }
    public DeleteStoryResponse getBody() {
        return this.body;
    }

}
