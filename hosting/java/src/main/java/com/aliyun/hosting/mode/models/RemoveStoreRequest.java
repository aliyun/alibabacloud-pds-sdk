// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class RemoveStoreRequest extends TeaModel {
    // domain ID
    @NameInMap("domain_id")
    @Validation(required = true)
    public String domainId;

    // store ID
    @NameInMap("store_id")
    @Validation(required = true)
    public String storeId;

    public static RemoveStoreRequest build(java.util.Map<String, ?> map) throws Exception {
        RemoveStoreRequest self = new RemoveStoreRequest();
        return TeaModel.build(map, self);
    }

    public RemoveStoreRequest setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public RemoveStoreRequest setStoreId(String storeId) {
        this.storeId = storeId;
        return this;
    }
    public String getStoreId() {
        return this.storeId;
    }

}
