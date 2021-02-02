// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

public class GetDataCnameInfoModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public GetBizCNameInfoResponse body;

    public static GetDataCnameInfoModel build(java.util.Map<String, ?> map) throws Exception {
        GetDataCnameInfoModel self = new GetDataCnameInfoModel();
        return TeaModel.build(map, self);
    }

    public GetDataCnameInfoModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetDataCnameInfoModel setBody(GetBizCNameInfoResponse body) {
        this.body = body;
        return this;
    }
    public GetBizCNameInfoResponse getBody() {
        return this.body;
    }

}
