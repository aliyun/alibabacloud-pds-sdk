// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * List user response
 */
public class ListUserResponse extends TeaModel {
    @NameInMap("items")
    public java.util.List<BaseUserResponse> items;

    // 翻页标记
    @NameInMap("next_marker")
    public String nextMarker;

    public static ListUserResponse build(java.util.Map<String, ?> map) throws Exception {
        ListUserResponse self = new ListUserResponse();
        return TeaModel.build(map, self);
    }

    public ListUserResponse setItems(java.util.List<BaseUserResponse> items) {
        this.items = items;
        return this;
    }
    public java.util.List<BaseUserResponse> getItems() {
        return this.items;
    }

    public ListUserResponse setNextMarker(String nextMarker) {
        this.nextMarker = nextMarker;
        return this;
    }
    public String getNextMarker() {
        return this.nextMarker;
    }

}
