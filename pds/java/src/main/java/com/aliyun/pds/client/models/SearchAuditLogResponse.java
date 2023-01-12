// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 查询审计日志response
 */
public class SearchAuditLogResponse extends TeaModel {
    /**
     * <p>items</p>
     */
    @NameInMap("items")
    public java.util.List<BaseAuditLogResponse> items;

    /**
     * <p>next_marker</p>
     */
    @NameInMap("next_marker")
    public String nextMarker;

    public static SearchAuditLogResponse build(java.util.Map<String, ?> map) throws Exception {
        SearchAuditLogResponse self = new SearchAuditLogResponse();
        return TeaModel.build(map, self);
    }

    public SearchAuditLogResponse setItems(java.util.List<BaseAuditLogResponse> items) {
        this.items = items;
        return this;
    }
    public java.util.List<BaseAuditLogResponse> getItems() {
        return this.items;
    }

    public SearchAuditLogResponse setNextMarker(String nextMarker) {
        this.nextMarker = nextMarker;
        return this;
    }
    public String getNextMarker() {
        return this.nextMarker;
    }

}
