// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * ListFileInRecycleBinResponse
 */
public class ListFileInRecycleBinResponse extends TeaModel {
    // items
    @NameInMap("items")
    public java.util.List<BaseCCPFileResponse> items;

    // next_marker
    @NameInMap("next_marker")
    public String nextMarker;

    public static ListFileInRecycleBinResponse build(java.util.Map<String, ?> map) throws Exception {
        ListFileInRecycleBinResponse self = new ListFileInRecycleBinResponse();
        return TeaModel.build(map, self);
    }

    public ListFileInRecycleBinResponse setItems(java.util.List<BaseCCPFileResponse> items) {
        this.items = items;
        return this;
    }
    public java.util.List<BaseCCPFileResponse> getItems() {
        return this.items;
    }

    public ListFileInRecycleBinResponse setNextMarker(String nextMarker) {
        this.nextMarker = nextMarker;
        return this;
    }
    public String getNextMarker() {
        return this.nextMarker;
    }

}
