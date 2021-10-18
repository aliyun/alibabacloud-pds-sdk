// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class ListManageSharingFileModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public ListFileResponse body;

    public static ListManageSharingFileModel build(java.util.Map<String, ?> map) throws Exception {
        ListManageSharingFileModel self = new ListManageSharingFileModel();
        return TeaModel.build(map, self);
    }

    public ListManageSharingFileModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ListManageSharingFileModel setBody(ListFileResponse body) {
        this.body = body;
        return this;
    }
    public ListFileResponse getBody() {
        return this.body;
    }

}
