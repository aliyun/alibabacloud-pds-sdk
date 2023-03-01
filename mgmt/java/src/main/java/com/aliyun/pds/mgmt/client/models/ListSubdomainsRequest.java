// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class ListSubdomainsRequest extends TeaModel {
    /**
     * <p>数量，默认为50</p>
     */
    @NameInMap("limit")
    public Integer limit;

    /**
     * <p>分页游标，可从 response 中获取</p>
     */
    @NameInMap("marker")
    public String marker;

    public static ListSubdomainsRequest build(java.util.Map<String, ?> map) throws Exception {
        ListSubdomainsRequest self = new ListSubdomainsRequest();
        return TeaModel.build(map, self);
    }

    public ListSubdomainsRequest setLimit(Integer limit) {
        this.limit = limit;
        return this;
    }
    public Integer getLimit() {
        return this.limit;
    }

    public ListSubdomainsRequest setMarker(String marker) {
        this.marker = marker;
        return this;
    }
    public String getMarker() {
        return this.marker;
    }

}
