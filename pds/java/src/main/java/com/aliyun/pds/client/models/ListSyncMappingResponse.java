// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class ListSyncMappingResponse extends TeaModel {
    // items
    @NameInMap("items")
    public java.util.List<SyncMappingItem> items;

    // marker
    @NameInMap("marker")
    public String marker;

    public static ListSyncMappingResponse build(java.util.Map<String, ?> map) throws Exception {
        ListSyncMappingResponse self = new ListSyncMappingResponse();
        return TeaModel.build(map, self);
    }

    public ListSyncMappingResponse setItems(java.util.List<SyncMappingItem> items) {
        this.items = items;
        return this;
    }
    public java.util.List<SyncMappingItem> getItems() {
        return this.items;
    }

    public ListSyncMappingResponse setMarker(String marker) {
        this.marker = marker;
        return this;
    }
    public String getMarker() {
        return this.marker;
    }

}
