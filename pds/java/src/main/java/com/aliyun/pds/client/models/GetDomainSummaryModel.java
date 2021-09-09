// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class GetDomainSummaryModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public DomainSummaryResponse body;

    public static GetDomainSummaryModel build(java.util.Map<String, ?> map) throws Exception {
        GetDomainSummaryModel self = new GetDomainSummaryModel();
        return TeaModel.build(map, self);
    }

    public GetDomainSummaryModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetDomainSummaryModel setBody(DomainSummaryResponse body) {
        this.body = body;
        return this;
    }
    public DomainSummaryResponse getBody() {
        return this.body;
    }

}
