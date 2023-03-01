// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * search drive response
 */
public class SearchDriveResponse extends TeaModel {
    /**
     * <p>Drive 列表</p>
     */
    @NameInMap("items")
    public java.util.List<BaseDriveResponse> items;

    /**
     * <p>翻页标记</p>
     */
    @NameInMap("next_marker")
    public String nextMarker;

    public static SearchDriveResponse build(java.util.Map<String, ?> map) throws Exception {
        SearchDriveResponse self = new SearchDriveResponse();
        return TeaModel.build(map, self);
    }

    public SearchDriveResponse setItems(java.util.List<BaseDriveResponse> items) {
        this.items = items;
        return this;
    }
    public java.util.List<BaseDriveResponse> getItems() {
        return this.items;
    }

    public SearchDriveResponse setNextMarker(String nextMarker) {
        this.nextMarker = nextMarker;
        return this;
    }
    public String getNextMarker() {
        return this.nextMarker;
    }

}
