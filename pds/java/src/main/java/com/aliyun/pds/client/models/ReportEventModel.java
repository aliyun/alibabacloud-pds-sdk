// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class ReportEventModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public ReportEventResponse body;

    public static ReportEventModel build(java.util.Map<String, ?> map) throws Exception {
        ReportEventModel self = new ReportEventModel();
        return TeaModel.build(map, self);
    }

    public ReportEventModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ReportEventModel setBody(ReportEventResponse body) {
        this.body = body;
        return this;
    }
    public ReportEventResponse getBody() {
        return this.body;
    }

}
