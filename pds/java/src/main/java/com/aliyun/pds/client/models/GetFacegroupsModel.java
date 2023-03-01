// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class GetFacegroupsModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public ImageFaceGroupsResponse body;

    public static GetFacegroupsModel build(java.util.Map<String, ?> map) throws Exception {
        GetFacegroupsModel self = new GetFacegroupsModel();
        return TeaModel.build(map, self);
    }

    public GetFacegroupsModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetFacegroupsModel setBody(ImageFaceGroupsResponse body) {
        this.body = body;
        return this;
    }
    public ImageFaceGroupsResponse getBody() {
        return this.body;
    }

}
