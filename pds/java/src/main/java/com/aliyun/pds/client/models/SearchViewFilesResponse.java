// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * search view files response
 */
public class SearchViewFilesResponse extends TeaModel {
    @NameInMap("items")
    public java.util.List<ViewFileItem> items;

    @NameInMap("next_marker")
    public String nextMarker;

    @NameInMap("total_count")
    public Long totalCount;

    public static SearchViewFilesResponse build(java.util.Map<String, ?> map) throws Exception {
        SearchViewFilesResponse self = new SearchViewFilesResponse();
        return TeaModel.build(map, self);
    }

    public SearchViewFilesResponse setItems(java.util.List<ViewFileItem> items) {
        this.items = items;
        return this;
    }
    public java.util.List<ViewFileItem> getItems() {
        return this.items;
    }

    public SearchViewFilesResponse setNextMarker(String nextMarker) {
        this.nextMarker = nextMarker;
        return this;
    }
    public String getNextMarker() {
        return this.nextMarker;
    }

    public SearchViewFilesResponse setTotalCount(Long totalCount) {
        this.totalCount = totalCount;
        return this;
    }
    public Long getTotalCount() {
        return this.totalCount;
    }

}
