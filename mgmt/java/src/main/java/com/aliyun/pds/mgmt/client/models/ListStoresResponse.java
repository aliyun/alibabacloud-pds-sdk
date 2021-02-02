// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class ListStoresResponse extends TeaModel {
    // Store 列表
    @NameInMap("items")
    @Validation(required = true)
    public java.util.List<Store> items;

    public static ListStoresResponse build(java.util.Map<String, ?> map) throws Exception {
        ListStoresResponse self = new ListStoresResponse();
        return TeaModel.build(map, self);
    }

    public ListStoresResponse setItems(java.util.List<Store> items) {
        this.items = items;
        return this;
    }
    public java.util.List<Store> getItems() {
        return this.items;
    }

}
