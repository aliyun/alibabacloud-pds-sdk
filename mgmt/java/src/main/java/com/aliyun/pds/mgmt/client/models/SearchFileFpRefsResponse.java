// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * search file response
 */
public class SearchFileFpRefsResponse extends TeaModel {
    @NameInMap("items")
    public java.util.List<FpRef> items;

    @NameInMap("next_marker")
    public String nextMarker;

    public static SearchFileFpRefsResponse build(java.util.Map<String, ?> map) throws Exception {
        SearchFileFpRefsResponse self = new SearchFileFpRefsResponse();
        return TeaModel.build(map, self);
    }

    public SearchFileFpRefsResponse setItems(java.util.List<FpRef> items) {
        this.items = items;
        return this;
    }
    public java.util.List<FpRef> getItems() {
        return this.items;
    }

    public SearchFileFpRefsResponse setNextMarker(String nextMarker) {
        this.nextMarker = nextMarker;
        return this;
    }
    public String getNextMarker() {
        return this.nextMarker;
    }

}
