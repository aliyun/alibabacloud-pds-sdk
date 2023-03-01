// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * search all recycle bin response
 */
public class SearchAllRecycleBinResponse extends TeaModel {
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

    public static SearchAllRecycleBinResponse build(java.util.Map<String, ?> map) throws Exception {
        SearchAllRecycleBinResponse self = new SearchAllRecycleBinResponse();
        return TeaModel.build(map, self);
    }

    public SearchAllRecycleBinResponse setItems(java.util.List<BaseCCPFileResponse> items) {
        this.items = items;
        return this;
    }
    public java.util.List<BaseCCPFileResponse> getItems() {
        return this.items;
    }

    public SearchAllRecycleBinResponse setNextMarker(String nextMarker) {
        this.nextMarker = nextMarker;
        return this;
    }
    public String getNextMarker() {
        return this.nextMarker;
    }

}
