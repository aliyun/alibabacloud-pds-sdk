// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class ListSubdomainsResponse extends TeaModel {
    // 分页的 subdomain 数据
    @NameInMap("items")
    @Validation(required = true)
    public java.util.List<BaseSubdomainResponse> items;

    // 分页游标，可以用作下次list的起点
    @NameInMap("next_marker")
    @Validation(required = true)
    public String nextMarker;

    public static ListSubdomainsResponse build(java.util.Map<String, ?> map) throws Exception {
        ListSubdomainsResponse self = new ListSubdomainsResponse();
        return TeaModel.build(map, self);
    }

    public ListSubdomainsResponse setItems(java.util.List<BaseSubdomainResponse> items) {
        this.items = items;
        return this;
    }
    public java.util.List<BaseSubdomainResponse> getItems() {
        return this.items;
    }

    public ListSubdomainsResponse setNextMarker(String nextMarker) {
        this.nextMarker = nextMarker;
        return this;
    }
    public String getNextMarker() {
        return this.nextMarker;
    }

}
