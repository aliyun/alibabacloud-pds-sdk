// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class ListUploadedPartsModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public ListUploadedPartResponse body;

    public static ListUploadedPartsModel build(java.util.Map<String, ?> map) throws Exception {
        ListUploadedPartsModel self = new ListUploadedPartsModel();
        return TeaModel.build(map, self);
    }

    public ListUploadedPartsModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ListUploadedPartsModel setBody(ListUploadedPartResponse body) {
        this.body = body;
        return this;
    }
    public ListUploadedPartResponse getBody() {
        return this.body;
    }

}
