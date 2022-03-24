// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class UpdateStoryModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public UpdateStoryResponse body;

    public static UpdateStoryModel build(java.util.Map<String, ?> map) throws Exception {
        UpdateStoryModel self = new UpdateStoryModel();
        return TeaModel.build(map, self);
    }

    public UpdateStoryModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public UpdateStoryModel setBody(UpdateStoryResponse body) {
        this.body = body;
        return this;
    }
    public UpdateStoryResponse getBody() {
        return this.body;
    }

}
