// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

/**
 * List file response
 */
public class ListFileResponse extends TeaModel {
    // items
    @NameInMap("items")
    public java.util.List<BaseFileResponse> items;

    // next_marker
    @NameInMap("next_marker")
    public String nextMarker;

    public static ListFileResponse build(java.util.Map<String, ?> map) throws Exception {
        ListFileResponse self = new ListFileResponse();
        return TeaModel.build(map, self);
    }

    public ListFileResponse setItems(java.util.List<BaseFileResponse> items) {
        this.items = items;
        return this;
    }
    public java.util.List<BaseFileResponse> getItems() {
        return this.items;
    }

    public ListFileResponse setNextMarker(String nextMarker) {
        this.nextMarker = nextMarker;
        return this;
    }
    public String getNextMarker() {
        return this.nextMarker;
    }

}
