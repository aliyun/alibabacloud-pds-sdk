// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class ListIdentityRoleModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public BaseRoleMemberResponse body;

    public static ListIdentityRoleModel build(java.util.Map<String, ?> map) throws Exception {
        ListIdentityRoleModel self = new ListIdentityRoleModel();
        return TeaModel.build(map, self);
    }

    public ListIdentityRoleModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ListIdentityRoleModel setBody(BaseRoleMemberResponse body) {
        this.body = body;
        return this;
    }
    public BaseRoleMemberResponse getBody() {
        return this.body;
    }

}
