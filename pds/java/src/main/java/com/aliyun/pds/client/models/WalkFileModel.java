// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class WalkFileModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public CCPWalkFileResponse body;

    public static WalkFileModel build(java.util.Map<String, ?> map) throws Exception {
        WalkFileModel self = new WalkFileModel();
        return TeaModel.build(map, self);
    }

    public WalkFileModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public WalkFileModel setBody(CCPWalkFileResponse body) {
        this.body = body;
        return this;
    }
    public CCPWalkFileResponse getBody() {
        return this.body;
    }

}
