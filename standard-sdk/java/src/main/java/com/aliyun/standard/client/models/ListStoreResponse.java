// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.standard.client.models;

import com.aliyun.tea.*;

/**
 * List storage
 */
public class ListStoreResponse extends TeaModel {
    // items
    @NameInMap("items")
    public java.util.List<StoreItemResponse> items;

    public static ListStoreResponse build(java.util.Map<String, ?> map) throws Exception {
        ListStoreResponse self = new ListStoreResponse();
        return TeaModel.build(map, self);
    }

    public ListStoreResponse setItems(java.util.List<StoreItemResponse> items) {
        this.items = items;
        return this;
    }
    public java.util.List<StoreItemResponse> getItems() {
        return this.items;
    }

}
