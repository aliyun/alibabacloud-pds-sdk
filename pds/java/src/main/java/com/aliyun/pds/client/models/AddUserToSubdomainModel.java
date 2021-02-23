// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class AddUserToSubdomainModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    public static AddUserToSubdomainModel build(java.util.Map<String, ?> map) throws Exception {
        AddUserToSubdomainModel self = new AddUserToSubdomainModel();
        return TeaModel.build(map, self);
    }

    public AddUserToSubdomainModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

}
