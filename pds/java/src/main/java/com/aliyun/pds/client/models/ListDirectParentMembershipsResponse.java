// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class ListDirectParentMembershipsResponse extends TeaModel {
    // items
    @NameInMap("items")
    public java.util.List<BaseMembershipResponse> items;

    // 翻页标记
    @NameInMap("next_marker")
    public String nextMarker;

    public static ListDirectParentMembershipsResponse build(java.util.Map<String, ?> map) throws Exception {
        ListDirectParentMembershipsResponse self = new ListDirectParentMembershipsResponse();
        return TeaModel.build(map, self);
    }

    public ListDirectParentMembershipsResponse setItems(java.util.List<BaseMembershipResponse> items) {
        this.items = items;
        return this;
    }
    public java.util.List<BaseMembershipResponse> getItems() {
        return this.items;
    }

    public ListDirectParentMembershipsResponse setNextMarker(String nextMarker) {
        this.nextMarker = nextMarker;
        return this;
    }
    public String getNextMarker() {
        return this.nextMarker;
    }

}
