// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 展示地点分组集合
 */
public class ListImageAddressGroupsResponse extends TeaModel {
    @NameInMap("items")
    public java.util.List<ImageAddressResponse> items;

    @NameInMap("next_marker")
    public String nextMarker;

    public static ListImageAddressGroupsResponse build(java.util.Map<String, ?> map) throws Exception {
        ListImageAddressGroupsResponse self = new ListImageAddressGroupsResponse();
        return TeaModel.build(map, self);
    }

    public ListImageAddressGroupsResponse setItems(java.util.List<ImageAddressResponse> items) {
        this.items = items;
        return this;
    }
    public java.util.List<ImageAddressResponse> getItems() {
        return this.items;
    }

    public ListImageAddressGroupsResponse setNextMarker(String nextMarker) {
        this.nextMarker = nextMarker;
        return this;
    }
    public String getNextMarker() {
        return this.nextMarker;
    }

}
