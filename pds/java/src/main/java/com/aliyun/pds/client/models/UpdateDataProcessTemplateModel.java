// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class UpdateDataProcessTemplateModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public UpdateDataProcessTemplateResponse body;

    public static UpdateDataProcessTemplateModel build(java.util.Map<String, ?> map) throws Exception {
        UpdateDataProcessTemplateModel self = new UpdateDataProcessTemplateModel();
        return TeaModel.build(map, self);
    }

    public UpdateDataProcessTemplateModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public UpdateDataProcessTemplateModel setBody(UpdateDataProcessTemplateResponse body) {
        this.body = body;
        return this;
    }
    public UpdateDataProcessTemplateResponse getBody() {
        return this.body;
    }

}
