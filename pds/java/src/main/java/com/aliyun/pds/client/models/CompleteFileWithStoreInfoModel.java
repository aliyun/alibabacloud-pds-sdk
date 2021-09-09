// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class CompleteFileWithStoreInfoModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public UCCompleteFileResponse body;

    public static CompleteFileWithStoreInfoModel build(java.util.Map<String, ?> map) throws Exception {
        CompleteFileWithStoreInfoModel self = new CompleteFileWithStoreInfoModel();
        return TeaModel.build(map, self);
    }

    public CompleteFileWithStoreInfoModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public CompleteFileWithStoreInfoModel setBody(UCCompleteFileResponse body) {
        this.body = body;
        return this;
    }
    public UCCompleteFileResponse getBody() {
        return this.body;
    }

}
