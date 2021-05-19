// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * list drive response
 */
public class ListDriveResponse extends TeaModel {
    // Drive 列表
    @NameInMap("items")
    public java.util.List<BaseDriveResponse> items;

    // 翻页标记
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
