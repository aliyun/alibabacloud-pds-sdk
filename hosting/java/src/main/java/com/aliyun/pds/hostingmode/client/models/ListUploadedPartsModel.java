// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.hostingmode.client.models;

import com.aliyun.tea.*;

public class ListUploadedPartsModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public HostingListUploadedPartResponse body;

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

    public ListUploadedPartsModel setBody(HostingListUploadedPartResponse body) {
        this.body = body;
        return this;
    }
    public HostingListUploadedPartResponse getBody() {
        return this.body;
    }

}
