// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.standard.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class AdminListStoresRequest extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    public static AdminListStoresRequest build(java.util.Map<String, ?> map) throws Exception {
        AdminListStoresRequest self = new AdminListStoresRequest();
        return TeaModel.build(map, self);
    }

    public AdminListStoresRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

}
