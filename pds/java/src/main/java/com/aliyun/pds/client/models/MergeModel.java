// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class MergeModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public MergeFaceGroupResponse body;

    public static MergeModel build(java.util.Map<String, ?> map) throws Exception {
        MergeModel self = new MergeModel();
        return TeaModel.build(map, self);
    }

    public MergeModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public MergeModel setBody(MergeFaceGroupResponse body) {
        this.body = body;
        return this;
    }
    public MergeFaceGroupResponse getBody() {
        return this.body;
    }

}
