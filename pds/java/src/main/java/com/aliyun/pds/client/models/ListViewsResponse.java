// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 获取逻辑视图列表信息
 */
public class ListViewsResponse extends TeaModel {
    @NameInMap("items")
    public java.util.List<GetViewResponse> items;

    @NameInMap("next_marker")
    public String nextMarker;

    public static ListViewsResponse build(java.util.Map<String, ?> map) throws Exception {
        ListViewsResponse self = new ListViewsResponse();
        return TeaModel.build(map, self);
    }

    public ListViewsResponse setItems(java.util.List<GetViewResponse> items) {
        this.items = items;
        return this;
    }
    public java.util.List<GetViewResponse> getItems() {
        return this.items;
    }

    public ListViewsResponse setNextMarker(String nextMarker) {
        this.nextMarker = nextMarker;
        return this;
    }
    public String getNextMarker() {
        return this.nextMarker;
    }

}
