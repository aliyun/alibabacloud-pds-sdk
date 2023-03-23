// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class ListGroupResponse extends TeaModel {
    /**
     * <p>items</p>
     */
    @NameInMap("items")
    public java.util.List<GroupExtraItem> items;

    /**
     * <p>翻页标记</p>
     */
    @NameInMap("next_marker")
    public String nextMarker;

    public static ListGroupResponse build(java.util.Map<String, ?> map) throws Exception {
        ListGroupResponse self = new ListGroupResponse();
        return TeaModel.build(map, self);
    }

    public ListGroupResponse setItems(java.util.List<GroupExtraItem> items) {
        this.items = items;
        return this;
    }
    public java.util.List<GroupExtraItem> getItems() {
        return this.items;
    }

    public ListGroupResponse setNextMarker(String nextMarker) {
        this.nextMarker = nextMarker;
        return this;
    }
    public String getNextMarker() {
        return this.nextMarker;
    }

}
