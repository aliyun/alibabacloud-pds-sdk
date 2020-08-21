// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.standard.client.models;

import com.aliyun.tea.*;

/**
 * search file response
 */
public class SearchFileResponse extends TeaModel {
    // items
    @NameInMap("items")
    public java.util.List<BaseFileResponse> items;

    // next_marker
    @NameInMap("next_marker")
    public String nextMarker;

    public static SearchFileResponse build(java.util.Map<String, ?> map) throws Exception {
        SearchFileResponse self = new SearchFileResponse();
        return TeaModel.build(map, self);
    }

    public SearchFileResponse setItems(java.util.List<BaseFileResponse> items) {
        this.items = items;
        return this;
    }
    public java.util.List<BaseFileResponse> getItems() {
        return this.items;
    }

    public SearchFileResponse setNextMarker(String nextMarker) {
        this.nextMarker = nextMarker;
        return this;
    }
    public String getNextMarker() {
        return this.nextMarker;
    }

}
