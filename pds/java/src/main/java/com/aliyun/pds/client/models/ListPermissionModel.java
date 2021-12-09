// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class ListPermissionModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public java.util.List<FilePermissionMember> body;

    public static ListPermissionModel build(java.util.Map<String, ?> map) throws Exception {
        ListPermissionModel self = new ListPermissionModel();
        return TeaModel.build(map, self);
    }

    public ListPermissionModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ListPermissionModel setBody(java.util.List<FilePermissionMember> body) {
        this.body = body;
        return this;
    }
    public java.util.List<FilePermissionMember> getBody() {
        return this.body;
    }

}
