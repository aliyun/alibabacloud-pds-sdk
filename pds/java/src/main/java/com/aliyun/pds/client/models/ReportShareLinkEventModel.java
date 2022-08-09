// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class ReportShareLinkEventModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public ReportEventResponse body;

    public static ReportShareLinkEventModel build(java.util.Map<String, ?> map) throws Exception {
        ReportShareLinkEventModel self = new ReportShareLinkEventModel();
        return TeaModel.build(map, self);
    }

    public ReportShareLinkEventModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ReportShareLinkEventModel setBody(ReportEventResponse body) {
        this.body = body;
        return this;
    }
    public ReportEventResponse getBody() {
        return this.body;
    }

}
