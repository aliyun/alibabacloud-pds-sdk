// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

/**
 * List my drive request
 */
public class ListMyDriveRequest extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // 每页大小限制
    @NameInMap("limit")
    public Integer limit;

    // 翻页标记, 接口返回的标记值
    @NameInMap("marker")
    public String marker;

    public static ListMyDriveRequest build(java.util.Map<String, ?> map) throws Exception {
        ListMyDriveRequest self = new ListMyDriveRequest();
        return TeaModel.build(map, self);
    }

    public ListMyDriveRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ListMyDriveRequest setLimit(Integer limit) {
        this.limit = limit;
        return this;
    }
    public Integer getLimit() {
        return this.limit;
    }

    public ListMyDriveRequest setMarker(String marker) {
        this.marker = marker;
        return this;
    }
    public String getMarker() {
        return this.marker;
    }

}
