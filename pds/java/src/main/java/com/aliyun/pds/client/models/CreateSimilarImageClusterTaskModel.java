// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class CreateSimilarImageClusterTaskModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public CreateSimilarImageClusterTaskResponse body;

    public static CreateSimilarImageClusterTaskModel build(java.util.Map<String, ?> map) throws Exception {
        CreateSimilarImageClusterTaskModel self = new CreateSimilarImageClusterTaskModel();
        return TeaModel.build(map, self);
    }

    public CreateSimilarImageClusterTaskModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public CreateSimilarImageClusterTaskModel setBody(CreateSimilarImageClusterTaskResponse body) {
        this.body = body;
        return this;
    }
    public CreateSimilarImageClusterTaskResponse getBody() {
        return this.body;
    }

}
