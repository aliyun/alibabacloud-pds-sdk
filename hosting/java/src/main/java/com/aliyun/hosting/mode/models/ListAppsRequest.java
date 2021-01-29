// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class ListAppsRequest extends TeaModel {
    // 返回结果数据
    @NameInMap("limit")
    public Integer limit;

    // 下次查询游标
    @NameInMap("marker")
    public String marker;

    public static ListAppsRequest build(java.util.Map<String, ?> map) throws Exception {
        ListAppsRequest self = new ListAppsRequest();
        return TeaModel.build(map, self);
    }

    public ListAppsRequest setLimit(Integer limit) {
        this.limit = limit;
        return this;
    }
    public Integer getLimit() {
        return this.limit;
    }

    public ListAppsRequest setMarker(String marker) {
        this.marker = marker;
        return this;
    }
    public String getMarker() {
        return this.marker;
    }

}
