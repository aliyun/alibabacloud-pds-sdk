// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class GetDataProcessTemplateModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public GetDriveDataProcessTemplateResponse body;

    public static GetDataProcessTemplateModel build(java.util.Map<String, ?> map) throws Exception {
        GetDataProcessTemplateModel self = new GetDataProcessTemplateModel();
        return TeaModel.build(map, self);
    }

    public GetDataProcessTemplateModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetDataProcessTemplateModel setBody(GetDriveDataProcessTemplateResponse body) {
        this.body = body;
        return this;
    }
    public GetDriveDataProcessTemplateResponse getBody() {
        return this.body;
    }

}
