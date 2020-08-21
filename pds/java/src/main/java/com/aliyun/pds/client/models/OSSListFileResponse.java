// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * List file response
 */
public class OSSListFileResponse extends TeaModel {
    // items
    @NameInMap("items")
    public java.util.List<BaseOSSFileResponse> items;

    // next_marker
    @NameInMap("next_marker")
    public String nextMarker;

    public static OSSListFileResponse build(java.util.Map<String, ?> map) throws Exception {
        OSSListFileResponse self = new OSSListFileResponse();
        return TeaModel.build(map, self);
    }

    public OSSListFileResponse setItems(java.util.List<BaseOSSFileResponse> items) {
        this.items = items;
        return this;
    }
    public java.util.List<BaseOSSFileResponse> getItems() {
        return this.items;
    }

    public OSSListFileResponse setNextMarker(String nextMarker) {
        this.nextMarker = nextMarker;
        return this;
    }
    public String getNextMarker() {
        return this.nextMarker;
    }

}
