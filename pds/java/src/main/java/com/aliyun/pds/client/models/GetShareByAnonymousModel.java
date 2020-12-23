// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class GetShareByAnonymousModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public GetShareLinkByAnonymousResponse body;

    public static GetShareByAnonymousModel build(java.util.Map<String, ?> map) throws Exception {
        GetShareByAnonymousModel self = new GetShareByAnonymousModel();
        return TeaModel.build(map, self);
    }

    public GetShareByAnonymousModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetShareByAnonymousModel setBody(GetShareLinkByAnonymousResponse body) {
        this.body = body;
        return this;
    }
    public GetShareLinkByAnonymousResponse getBody() {
        return this.body;
    }

}
