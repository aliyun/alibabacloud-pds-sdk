// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class GetAppDebugCmdModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public GetAppDebugCmdResponse body;

    public static GetAppDebugCmdModel build(java.util.Map<String, ?> map) throws Exception {
        GetAppDebugCmdModel self = new GetAppDebugCmdModel();
        return TeaModel.build(map, self);
    }

    public GetAppDebugCmdModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetAppDebugCmdModel setBody(GetAppDebugCmdResponse body) {
        this.body = body;
        return this;
    }
    public GetAppDebugCmdResponse getBody() {
        return this.body;
    }

}
