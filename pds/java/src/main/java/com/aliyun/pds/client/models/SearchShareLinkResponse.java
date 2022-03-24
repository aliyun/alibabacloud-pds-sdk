// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * search_share_link response
 */
public class SearchShareLinkResponse extends TeaModel {
    // items
    @NameInMap("items")
    public java.util.List<BaseShareLinkResponse> items;

    // next_marker
    @NameInMap("next_marker")
    public String nextMarker;

    // total_count
    @NameInMap("total_count")
    public Long totalCount;

    public static SearchShareLinkResponse build(java.util.Map<String, ?> map) throws Exception {
        SearchShareLinkResponse self = new SearchShareLinkResponse();
        return TeaModel.build(map, self);
    }

    public SearchShareLinkResponse setItems(java.util.List<BaseShareLinkResponse> items) {
        this.items = items;
        return this;
    }
    public java.util.List<BaseShareLinkResponse> getItems() {
        return this.items;
    }

    public SearchShareLinkResponse setNextMarker(String nextMarker) {
        this.nextMarker = nextMarker;
        return this;
    }
    public String getNextMarker() {
        return this.nextMarker;
    }

    public SearchShareLinkResponse setTotalCount(Long totalCount) {
        this.totalCount = totalCount;
        return this;
    }
    public Long getTotalCount() {
        return this.totalCount;
    }

}
