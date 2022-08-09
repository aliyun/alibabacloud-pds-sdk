// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class RemoveStoryFilesModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public RemoveStoryFilesResponse body;

    public static RemoveStoryFilesModel build(java.util.Map<String, ?> map) throws Exception {
        RemoveStoryFilesModel self = new RemoveStoryFilesModel();
        return TeaModel.build(map, self);
    }

    public RemoveStoryFilesModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public RemoveStoryFilesModel setBody(RemoveStoryFilesResponse body) {
        this.body = body;
        return this;
    }
    public RemoveStoryFilesResponse getBody() {
        return this.body;
    }

}
