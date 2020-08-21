// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * list domain response
 */
public class ListDomainsResponse extends TeaModel {
    // domain 列表
    @NameInMap("items")
    public java.util.List<BaseDomainResponse> items;

    // 下次分页查询游标
    @NameInMap("next_marker")
    public String nextMarker;

    public static ListDomainsResponse build(java.util.Map<String, ?> map) throws Exception {
        ListDomainsResponse self = new ListDomainsResponse();
        return TeaModel.build(map, self);
    }

    public ListDomainsResponse setItems(java.util.List<BaseDomainResponse> items) {
        this.items = items;
        return this;
    }
    public java.util.List<BaseDomainResponse> getItems() {
        return this.items;
    }

    public ListDomainsResponse setNextMarker(String nextMarker) {
        this.nextMarker = nextMarker;
        return this;
    }
    public String getNextMarker() {
        return this.nextMarker;
    }

}
