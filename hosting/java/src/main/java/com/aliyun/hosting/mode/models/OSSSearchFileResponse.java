// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

/**
 * search file response
 */
public class OSSSearchFileResponse extends TeaModel {
    // items
    @NameInMap("items")
    public java.util.List<BaseOSSFileResponse> items;

    // next_marker
    @NameInMap("next_marker")
    public String nextMarker;

    public static OSSSearchFileResponse build(java.util.Map<String, ?> map) throws Exception {
        OSSSearchFileResponse self = new OSSSearchFileResponse();
        return TeaModel.build(map, self);
    }

    public OSSSearchFileResponse setItems(java.util.List<BaseOSSFileResponse> items) {
        this.items = items;
        return this;
    }
    public java.util.List<BaseOSSFileResponse> getItems() {
        return this.items;
    }

    public OSSSearchFileResponse setNextMarker(String nextMarker) {
        this.nextMarker = nextMarker;
        return this;
    }
    public String getNextMarker() {
        return this.nextMarker;
    }

}
