// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class GetDriveUsedSizeModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public GetDriveUsedSizeResponse body;

    public static GetDriveUsedSizeModel build(java.util.Map<String, ?> map) throws Exception {
        GetDriveUsedSizeModel self = new GetDriveUsedSizeModel();
        return TeaModel.build(map, self);
    }

    public GetDriveUsedSizeModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetDriveUsedSizeModel setBody(GetDriveUsedSizeResponse body) {
        this.body = body;
        return this;
    }
    public GetDriveUsedSizeResponse getBody() {
        return this.body;
    }

}
