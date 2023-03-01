// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class GetFacegroupInfoModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public ImageFaceGroupResponse body;

    public static GetFacegroupInfoModel build(java.util.Map<String, ?> map) throws Exception {
        GetFacegroupInfoModel self = new GetFacegroupInfoModel();
        return TeaModel.build(map, self);
    }

    public GetFacegroupInfoModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetFacegroupInfoModel setBody(ImageFaceGroupResponse body) {
        this.body = body;
        return this;
    }
    public ImageFaceGroupResponse getBody() {
        return this.body;
    }

}
