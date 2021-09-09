// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * list file view ids
 */
public class ListFileViewsResponse extends TeaModel {
    @NameInMap("items")
    public java.util.List<GetViewResponse> items;

    public static ListFileViewsResponse build(java.util.Map<String, ?> map) throws Exception {
        ListFileViewsResponse self = new ListFileViewsResponse();
        return TeaModel.build(map, self);
    }

    public ListFileViewsResponse setItems(java.util.List<GetViewResponse> items) {
        this.items = items;
        return this;
    }
    public java.util.List<GetViewResponse> getItems() {
        return this.items;
    }

}
