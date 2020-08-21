// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class ListFaceGroupsModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public ListImageFaceGroupsResponse body;

    public static ListFaceGroupsModel build(java.util.Map<String, ?> map) throws Exception {
        ListFaceGroupsModel self = new ListFaceGroupsModel();
        return TeaModel.build(map, self);
    }

    public ListFaceGroupsModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ListFaceGroupsModel setBody(ListImageFaceGroupsResponse body) {
        this.body = body;
        return this;
    }
    public ListImageFaceGroupsResponse getBody() {
        return this.body;
    }

}
