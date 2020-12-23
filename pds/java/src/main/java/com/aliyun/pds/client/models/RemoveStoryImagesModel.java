// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class RemoveStoryImagesModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public RemoveStoryImagesResponse body;

    public static RemoveStoryImagesModel build(java.util.Map<String, ?> map) throws Exception {
        RemoveStoryImagesModel self = new RemoveStoryImagesModel();
        return TeaModel.build(map, self);
    }

    public RemoveStoryImagesModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public RemoveStoryImagesModel setBody(RemoveStoryImagesResponse body) {
        this.body = body;
        return this;
    }
    public RemoveStoryImagesResponse getBody() {
        return this.body;
    }

}
