// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

public class GetSubdomainBizCnameInfoModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public GetBizCNameInfoResponse body;

    public static GetSubdomainBizCnameInfoModel build(java.util.Map<String, ?> map) throws Exception {
        GetSubdomainBizCnameInfoModel self = new GetSubdomainBizCnameInfoModel();
        return TeaModel.build(map, self);
    }

    public GetSubdomainBizCnameInfoModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetSubdomainBizCnameInfoModel setBody(GetBizCNameInfoResponse body) {
        this.body = body;
        return this;
    }
    public GetBizCNameInfoResponse getBody() {
        return this.body;
    }

}
