// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 *
 */
public class SearchGroupResponse extends TeaModel {
    // items
    @NameInMap("items")
    public java.util.List<BaseGroupResponse> items;

    // next_marker
    @NameInMap("next_marker")
    public String nextMarker;

    public static SearchGroupResponse build(java.util.Map<String, ?> map) throws Exception {
        SearchGroupResponse self = new SearchGroupResponse();
        return TeaModel.build(map, self);
    }

    public SearchGroupResponse setItems(java.util.List<BaseGroupResponse> items) {
        this.items = items;
        return this;
    }
    public java.util.List<BaseGroupResponse> getItems() {
        return this.items;
    }

    public SearchGroupResponse setNextMarker(String nextMarker) {
        this.nextMarker = nextMarker;
        return this;
    }
    public String getNextMarker() {
        return this.nextMarker;
    }

}
