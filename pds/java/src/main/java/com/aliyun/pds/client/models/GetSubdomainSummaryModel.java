// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class GetSubdomainSummaryModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public SubdomainSummaryResponse body;

    public static GetSubdomainSummaryModel build(java.util.Map<String, ?> map) throws Exception {
        GetSubdomainSummaryModel self = new GetSubdomainSummaryModel();
        return TeaModel.build(map, self);
    }

    public GetSubdomainSummaryModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetSubdomainSummaryModel setBody(SubdomainSummaryResponse body) {
        this.body = body;
        return this;
    }
    public SubdomainSummaryResponse getBody() {
        return this.body;
    }

}
