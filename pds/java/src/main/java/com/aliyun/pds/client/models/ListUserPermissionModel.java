// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class ListUserPermissionModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public FileListUserPermissionResponse body;

    public static ListUserPermissionModel build(java.util.Map<String, ?> map) throws Exception {
        ListUserPermissionModel self = new ListUserPermissionModel();
        return TeaModel.build(map, self);
    }

    public ListUserPermissionModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ListUserPermissionModel setBody(FileListUserPermissionResponse body) {
        this.body = body;
        return this;
    }
    public FileListUserPermissionResponse getBody() {
        return this.body;
    }

}
