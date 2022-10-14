// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 列举版本response
 */
public class ListRevisionResponse extends TeaModel {
    // items
    @NameInMap("items")
    public java.util.List<BaseRevisionResponse> items;

    // next_marker
    @NameInMap("next_marker")
    public String nextMarker;

    public static ListRevisionResponse build(java.util.Map<String, ?> map) throws Exception {
        ListRevisionResponse self = new ListRevisionResponse();
        return TeaModel.build(map, self);
    }

    public ListRevisionResponse setItems(java.util.List<BaseRevisionResponse> items) {
        this.items = items;
        return this;
    }
    public java.util.List<BaseRevisionResponse> getItems() {
        return this.items;
    }

    public ListRevisionResponse setNextMarker(String nextMarker) {
        this.nextMarker = nextMarker;
        return this;
    }
    public String getNextMarker() {
        return this.nextMarker;
    }

}
