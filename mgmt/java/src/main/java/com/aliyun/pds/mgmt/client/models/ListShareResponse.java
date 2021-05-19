// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * List share response
 */
public class ListShareResponse extends TeaModel {
    // items
    @NameInMap("items")
    public java.util.List<BaseShareResponse> items;

    // next_marker
    @NameInMap("next_marker")
    public String nextMarker;

    public static ListShareResponse build(java.util.Map<String, ?> map) throws Exception {
        ListShareResponse self = new ListShareResponse();
        return TeaModel.build(map, self);
    }

    public ListShareResponse setItems(java.util.List<BaseShareResponse> items) {
        this.items = items;
        return this;
    }
    public java.util.List<BaseShareResponse> getItems() {
        return this.items;
    }

    public ListShareResponse setNextMarker(String nextMarker) {
        this.nextMarker = nextMarker;
        return this;
    }
    public String getNextMarker() {
        return this.nextMarker;
    }

}
