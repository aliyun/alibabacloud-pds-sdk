// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

public class ListFileModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public HostingListFileResponse body;

    public static ListFileModel build(java.util.Map<String, ?> map) throws Exception {
        ListFileModel self = new ListFileModel();
        return TeaModel.build(map, self);
    }

    public ListFileModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ListFileModel setBody(HostingListFileResponse body) {
        this.body = body;
        return this;
    }
    public HostingListFileResponse getBody() {
        return this.body;
    }

}
