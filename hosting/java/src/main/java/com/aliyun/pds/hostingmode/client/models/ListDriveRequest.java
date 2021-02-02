// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.hostingmode.client.models;

import com.aliyun.tea.*;

/**
 * List drive request
 */
public class ListDriveRequest extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // 每页大小限制
    @NameInMap("limit")
    public Integer limit;

    // 翻页标记, 接口返回的标记值
    @NameInMap("marker")
    public String marker;

    // 所属者
    @NameInMap("owner")
    public String owner;

    public static ListDriveRequest build(java.util.Map<String, ?> map) throws Exception {
        ListDriveRequest self = new ListDriveRequest();
        return TeaModel.build(map, self);
    }

    public ListDriveRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ListDriveRequest setLimit(Integer limit) {
        this.limit = limit;
        return this;
    }
    public Integer getLimit() {
        return this.limit;
    }

    public ListDriveRequest setMarker(String marker) {
        this.marker = marker;
        return this;
    }
    public String getMarker() {
        return this.marker;
    }

    public ListDriveRequest setOwner(String owner) {
        this.owner = owner;
        return this;
    }
    public String getOwner() {
        return this.owner;
    }

}
