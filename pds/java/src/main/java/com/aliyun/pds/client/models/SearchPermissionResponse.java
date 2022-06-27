// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 列举权限记录 response
 */
public class SearchPermissionResponse extends TeaModel {
    @NameInMap("domain_id")
    public String domainId;

    @NameInMap("items")
    public java.util.List<BasePermissionResponse> items;

    @NameInMap("next_marker")
    public String nextMarker;

    public static SearchPermissionResponse build(java.util.Map<String, ?> map) throws Exception {
        SearchPermissionResponse self = new SearchPermissionResponse();
        return TeaModel.build(map, self);
    }

    public SearchPermissionResponse setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public SearchPermissionResponse setItems(java.util.List<BasePermissionResponse> items) {
        this.items = items;
        return this;
    }
    public java.util.List<BasePermissionResponse> getItems() {
        return this.items;
    }

    public SearchPermissionResponse setNextMarker(String nextMarker) {
        this.nextMarker = nextMarker;
        return this;
    }
    public String getNextMarker() {
        return this.nextMarker;
    }

}
