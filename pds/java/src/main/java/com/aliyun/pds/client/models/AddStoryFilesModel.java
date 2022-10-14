// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class AddStoryFilesModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public AddStoryFilesResponse body;

    public static AddStoryFilesModel build(java.util.Map<String, ?> map) throws Exception {
        AddStoryFilesModel self = new AddStoryFilesModel();
        return TeaModel.build(map, self);
    }

    public AddStoryFilesModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public AddStoryFilesModel setBody(AddStoryFilesResponse body) {
        this.body = body;
        return this;
    }
    public AddStoryFilesResponse getBody() {
        return this.body;
    }

}
