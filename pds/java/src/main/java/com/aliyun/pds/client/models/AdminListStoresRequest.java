// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 *
 */
public class AdminListStoresRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    public static AdminListStoresRequest build(java.util.Map<String, ?> map) throws Exception {
        AdminListStoresRequest self = new AdminListStoresRequest();
        return TeaModel.build(map, self);
    }

    public AdminListStoresRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

}
