// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class ListInheritPermissionModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public FileListInheritPermissionResponse body;

    public static ListInheritPermissionModel build(java.util.Map<String, ?> map) throws Exception {
        ListInheritPermissionModel self = new ListInheritPermissionModel();
        return TeaModel.build(map, self);
    }

    public ListInheritPermissionModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ListInheritPermissionModel setBody(FileListInheritPermissionResponse body) {
        this.body = body;
        return this;
    }
    public FileListInheritPermissionResponse getBody() {
        return this.body;
    }

}
