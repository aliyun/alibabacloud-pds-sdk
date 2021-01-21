// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.mgmt.mode.models;

import com.aliyun.tea.*;

public class ListDomainModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public ListDomainsResponse body;

    public static ListDomainModel build(java.util.Map<String, ?> map) throws Exception {
        ListDomainModel self = new ListDomainModel();
        return TeaModel.build(map, self);
    }

    public ListDomainModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ListDomainModel setBody(ListDomainsResponse body) {
        this.body = body;
        return this;
    }
    public ListDomainsResponse getBody() {
        return this.body;
    }

}
