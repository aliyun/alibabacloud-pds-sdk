// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.standard.client.models;

import com.aliyun.tea.*;

/**
 * list_share_link response
 */
public class ListShareLinkResponse extends TeaModel {
    // items
    @NameInMap("items")
    public java.util.List<BaseShareLinkResponse> items;

    // next_marker
    @NameInMap("next_marker")
    public String nextMarker;

    public static ListShareLinkResponse build(java.util.Map<String, ?> map) throws Exception {
        ListShareLinkResponse self = new ListShareLinkResponse();
        return TeaModel.build(map, self);
    }

    public ListShareLinkResponse setItems(java.util.List<BaseShareLinkResponse> items) {
        this.items = items;
        return this;
    }
    public java.util.List<BaseShareLinkResponse> getItems() {
        return this.items;
    }

    public ListShareLinkResponse setNextMarker(String nextMarker) {
        this.nextMarker = nextMarker;
        return this;
    }
    public String getNextMarker() {
        return this.nextMarker;
    }

}
