// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.mgmt.mode.models;

import com.aliyun.tea.*;

public class GetBizCnameInfoModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public GetBizCNameInfoResponse body;

    public static GetBizCnameInfoModel build(java.util.Map<String, ?> map) throws Exception {
        GetBizCnameInfoModel self = new GetBizCnameInfoModel();
        return TeaModel.build(map, self);
    }

    public GetBizCnameInfoModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetBizCnameInfoModel setBody(GetBizCNameInfoResponse body) {
        this.body = body;
        return this;
    }
    public GetBizCNameInfoResponse getBody() {
        return this.body;
    }

}
