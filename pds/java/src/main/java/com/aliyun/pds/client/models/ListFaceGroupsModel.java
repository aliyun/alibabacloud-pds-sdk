// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class ListFacegroupsModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public ListImageFaceGroupsResponse body;

    public static ListFacegroupsModel build(java.util.Map<String, ?> map) throws Exception {
        ListFacegroupsModel self = new ListFacegroupsModel();
        return TeaModel.build(map, self);
    }

    public ListFacegroupsModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ListFacegroupsModel setBody(ListImageFaceGroupsResponse body) {
        this.body = body;
        return this;
    }
    public ListImageFaceGroupsResponse getBody() {
        return this.body;
    }

}
