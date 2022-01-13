// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class ListDeviceRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    // limit
    @NameInMap("limit")
    public Integer limit;

    // marker
    @NameInMap("marker")
    public String marker;

    public static ListDeviceRequest build(java.util.Map<String, ?> map) throws Exception {
        ListDeviceRequest self = new ListDeviceRequest();
        return TeaModel.build(map, self);
    }

    public ListDeviceRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public ListDeviceRequest setLimit(Integer limit) {
        this.limit = limit;
        return this;
    }
    public Integer getLimit() {
        return this.limit;
    }

    public ListDeviceRequest setMarker(String marker) {
        this.marker = marker;
        return this;
    }
    public String getMarker() {
        return this.marker;
    }

}
