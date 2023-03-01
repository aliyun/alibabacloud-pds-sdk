// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class RemoveStoreRequest extends TeaModel {
    /**
     * <p>domain ID</p>
     */
    @NameInMap("domain_id")
    @Validation(required = true)
    public String domainId;

    /**
     * <p>store ID</p>
     */
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
