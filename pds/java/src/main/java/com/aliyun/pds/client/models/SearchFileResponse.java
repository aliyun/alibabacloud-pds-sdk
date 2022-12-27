// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * search file response
 */
public class SearchFileResponse extends TeaModel {
    /**
     * <p>items</p>
     */
    @NameInMap("items")
    public java.util.List<BaseCCPFileResponse> items;

    /**
     * <p>next_marker</p>
     */
    @NameInMap("next_marker")
    public String nextMarker;

    /**
     * <p>total_count</p>
     */
    @NameInMap("total_count")
    public Long totalCount;

    public static SearchFileResponse build(java.util.Map<String, ?> map) throws Exception {
        SearchFileResponse self = new SearchFileResponse();
        return TeaModel.build(map, self);
    }

    public SearchFileResponse setItems(java.util.List<BaseCCPFileResponse> items) {
        this.items = items;
        return this;
    }
    public java.util.List<BaseCCPFileResponse> getItems() {
        return this.items;
    }

    public SearchFileResponse setNextMarker(String nextMarker) {
        this.nextMarker = nextMarker;
        return this;
    }
    public String getNextMarker() {
        return this.nextMarker;
    }

    public SearchFileResponse setTotalCount(Long totalCount) {
        this.totalCount = totalCount;
        return this;
    }
    public Long getTotalCount() {
        return this.totalCount;
    }

}
