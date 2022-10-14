// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class ListAppsResponse extends TeaModel {
    // App 列表
    @NameInMap("items")
    @Validation(required = true)
    public java.util.List<GetAppResponse> items;

    // App 分批查询游标
    @NameInMap("next_marker")
    public String nextMarker;

    public static ListAppsResponse build(java.util.Map<String, ?> map) throws Exception {
        ListAppsResponse self = new ListAppsResponse();
        return TeaModel.build(map, self);
    }

    public ListAppsResponse setItems(java.util.List<GetAppResponse> items) {
        this.items = items;
        return this;
    }
    public java.util.List<GetAppResponse> getItems() {
        return this.items;
    }

    public ListAppsResponse setNextMarker(String nextMarker) {
        this.nextMarker = nextMarker;
        return this;
    }
    public String getNextMarker() {
        return this.nextMarker;
    }

}
