// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * list view files response
 */
public class ListViewFilesResponse extends TeaModel {
    @NameInMap("items")
    public java.util.List<ViewFileItem> items;

    @NameInMap("next_marker")
    public String nextMarker;

    public static ListViewFilesResponse build(java.util.Map<String, ?> map) throws Exception {
        ListViewFilesResponse self = new ListViewFilesResponse();
        return TeaModel.build(map, self);
    }

    public ListViewFilesResponse setItems(java.util.List<ViewFileItem> items) {
        this.items = items;
        return this;
    }
    public java.util.List<ViewFileItem> getItems() {
        return this.items;
    }

    public ListViewFilesResponse setNextMarker(String nextMarker) {
        this.nextMarker = nextMarker;
        return this;
    }
    public String getNextMarker() {
        return this.nextMarker;
    }

}
