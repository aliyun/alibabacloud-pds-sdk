// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class ListDirectChildMembershipsResponse extends TeaModel {
    // items
    @NameInMap("items")
    public java.util.List<BaseMembershipResponse> items;

    // 翻页标记
    @NameInMap("next_marker")
    public String nextMarker;

    public static ListDirectChildMembershipsResponse build(java.util.Map<String, ?> map) throws Exception {
        ListDirectChildMembershipsResponse self = new ListDirectChildMembershipsResponse();
        return TeaModel.build(map, self);
    }

    public ListDirectChildMembershipsResponse setItems(java.util.List<BaseMembershipResponse> items) {
        this.items = items;
        return this;
    }
    public java.util.List<BaseMembershipResponse> getItems() {
        return this.items;
    }

    public ListDirectChildMembershipsResponse setNextMarker(String nextMarker) {
        this.nextMarker = nextMarker;
        return this;
    }
    public String getNextMarker() {
        return this.nextMarker;
    }

}
