// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * list drive response
 */
public class ListDriveResponse extends TeaModel {
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

    public static ListDriveResponse build(java.util.Map<String, ?> map) throws Exception {
        ListDriveResponse self = new ListDriveResponse();
        return TeaModel.build(map, self);
    }

    public ListDriveResponse setItems(java.util.List<BaseDriveResponse> items) {
        this.items = items;
        return this;
    }
    public java.util.List<BaseDriveResponse> getItems() {
        return this.items;
    }

    public ListDriveResponse setNextMarker(String nextMarker) {
        this.nextMarker = nextMarker;
        return this;
    }
    public String getNextMarker() {
        return this.nextMarker;
    }

}
