// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * request
 */
public class ListPermissionRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    @NameInMap("collection")
    public String collection;

    @NameInMap("limit")
    public Integer limit;

    @NameInMap("marker")
    public String marker;

    public static ListPermissionRequest build(java.util.Map<String, ?> map) throws Exception {
        ListPermissionRequest self = new ListPermissionRequest();
        return TeaModel.build(map, self);
    }

    public ListPermissionRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public ListPermissionRequest setCollection(String collection) {
        this.collection = collection;
        return this;
    }
    public String getCollection() {
        return this.collection;
    }

    public ListPermissionRequest setLimit(Integer limit) {
        this.limit = limit;
        return this;
    }
    public Integer getLimit() {
        return this.limit;
    }

    public ListPermissionRequest setMarker(String marker) {
        this.marker = marker;
        return this;
    }
    public String getMarker() {
        return this.marker;
    }

}
