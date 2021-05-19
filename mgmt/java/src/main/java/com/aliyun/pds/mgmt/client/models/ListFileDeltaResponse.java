// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * list file op response
 */
public class ListFileDeltaResponse extends TeaModel {
    // cursor
    @NameInMap("cursor")
    public String cursor;

    // has_more
    @NameInMap("has_more")
    public Boolean hasMore;

    // items
    @NameInMap("items")
    public java.util.List<FileDeltaResponse> items;

    public static ListFileDeltaResponse build(java.util.Map<String, ?> map) throws Exception {
        ListFileDeltaResponse self = new ListFileDeltaResponse();
        return TeaModel.build(map, self);
    }

    public ListFileDeltaResponse setCursor(String cursor) {
        this.cursor = cursor;
        return this;
    }
    public String getCursor() {
        return this.cursor;
    }

    public ListFileDeltaResponse setHasMore(Boolean hasMore) {
        this.hasMore = hasMore;
        return this;
    }
    public Boolean getHasMore() {
        return this.hasMore;
    }

    public ListFileDeltaResponse setItems(java.util.List<FileDeltaResponse> items) {
        this.items = items;
        return this;
    }
    public java.util.List<FileDeltaResponse> getItems() {
        return this.items;
    }

}
