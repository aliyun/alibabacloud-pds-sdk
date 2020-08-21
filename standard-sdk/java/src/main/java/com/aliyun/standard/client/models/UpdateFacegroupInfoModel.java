// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.standard.client.models;

import com.aliyun.tea.*;

public class UpdateFacegroupInfoModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public UpdateFaceGroupInfoResponse body;

    public static UpdateFacegroupInfoModel build(java.util.Map<String, ?> map) throws Exception {
        UpdateFacegroupInfoModel self = new UpdateFacegroupInfoModel();
        return TeaModel.build(map, self);
    }

    public UpdateFacegroupInfoModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public UpdateFacegroupInfoModel setBody(UpdateFaceGroupInfoResponse body) {
        this.body = body;
        return this;
    }
    public UpdateFaceGroupInfoResponse getBody() {
        return this.body;
    }

}
