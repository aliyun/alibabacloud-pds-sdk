// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 获取逻辑视图列表信息
 */
public class SearchViewsResponse extends TeaModel {
    @NameInMap("items")
    public java.util.List<GetViewResponse> items;

    @NameInMap("next_marker")
    public String nextMarker;

    @NameInMap("total_count")
    public Long totalCount;

    public static SearchViewsResponse build(java.util.Map<String, ?> map) throws Exception {
        SearchViewsResponse self = new SearchViewsResponse();
        return TeaModel.build(map, self);
    }

    public SearchViewsResponse setItems(java.util.List<GetViewResponse> items) {
        this.items = items;
        return this;
    }
    public java.util.List<GetViewResponse> getItems() {
        return this.items;
    }

    public SearchViewsResponse setNextMarker(String nextMarker) {
        this.nextMarker = nextMarker;
        return this;
    }
    public String getNextMarker() {
        return this.nextMarker;
    }

    public SearchViewsResponse setTotalCount(Long totalCount) {
        this.totalCount = totalCount;
        return this;
    }
    public Long getTotalCount() {
        return this.totalCount;
    }

}
