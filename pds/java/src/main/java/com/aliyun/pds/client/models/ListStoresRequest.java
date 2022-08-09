// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 *
 */
public class ListStoresRequest extends TeaModel {
    // domain ID
    @NameInMap("domain_id")
    @Validation(required = true)
    public String domainId;

    public static ListStoresRequest build(java.util.Map<String, ?> map) throws Exception {
        ListStoresRequest self = new ListStoresRequest();
        return TeaModel.build(map, self);
    }

    public ListStoresRequest setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

}
