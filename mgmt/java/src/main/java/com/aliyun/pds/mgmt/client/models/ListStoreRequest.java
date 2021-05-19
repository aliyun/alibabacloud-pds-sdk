// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * list storage file
 */
public class ListStoreRequest extends TeaModel {
    // domain_id
    @NameInMap("domain_id")
    public String domainId;

    public static ListStoreRequest build(java.util.Map<String, ?> map) throws Exception {
        ListStoreRequest self = new ListStoreRequest();
        return TeaModel.build(map, self);
    }

    public ListStoreRequest setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

}
