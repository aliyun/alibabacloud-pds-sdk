// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

/**
 * list_file_by_anonymous response
 */
public class ListByAnonymousResponse extends TeaModel {
    // items
    @NameInMap("items")
    public java.util.List<BaseFileAnonymousResponse> items;

    // next_marker
    @NameInMap("next_marker")
    public String nextMarker;

    public static ListByAnonymousResponse build(java.util.Map<String, ?> map) throws Exception {
        ListByAnonymousResponse self = new ListByAnonymousResponse();
        return TeaModel.build(map, self);
    }

    public ListByAnonymousResponse setItems(java.util.List<BaseFileAnonymousResponse> items) {
        this.items = items;
        return this;
    }
    public java.util.List<BaseFileAnonymousResponse> getItems() {
        return this.items;
    }

    public ListByAnonymousResponse setNextMarker(String nextMarker) {
        this.nextMarker = nextMarker;
        return this;
    }
    public String getNextMarker() {
        return this.nextMarker;
    }

}
