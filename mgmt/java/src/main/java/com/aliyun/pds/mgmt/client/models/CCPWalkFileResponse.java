// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 列举文件response
 */
public class CCPWalkFileResponse extends TeaModel {
    // items
    @NameInMap("items")
    public java.util.List<BaseCCPFileResponse> items;

    // next_marker
    @NameInMap("next_marker")
    public String nextMarker;

    public static CCPWalkFileResponse build(java.util.Map<String, ?> map) throws Exception {
        CCPWalkFileResponse self = new CCPWalkFileResponse();
        return TeaModel.build(map, self);
    }

    public CCPWalkFileResponse setItems(java.util.List<BaseCCPFileResponse> items) {
        this.items = items;
        return this;
    }
    public java.util.List<BaseCCPFileResponse> getItems() {
        return this.items;
    }

    public CCPWalkFileResponse setNextMarker(String nextMarker) {
        this.nextMarker = nextMarker;
        return this;
    }
    public String getNextMarker() {
        return this.nextMarker;
    }

}
