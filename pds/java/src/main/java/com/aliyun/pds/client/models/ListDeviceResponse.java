// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class ListDeviceResponse extends TeaModel {
    /**
     * <p>items</p>
     */
    @NameInMap("items")
    public java.util.List<DeviceItem> items;

    /**
     * <p>marker</p>
     */
    @NameInMap("marker")
    public String marker;

    public static ListDeviceResponse build(java.util.Map<String, ?> map) throws Exception {
        ListDeviceResponse self = new ListDeviceResponse();
        return TeaModel.build(map, self);
    }

    public ListDeviceResponse setItems(java.util.List<DeviceItem> items) {
        this.items = items;
        return this;
    }
    public java.util.List<DeviceItem> getItems() {
        return this.items;
    }

    public ListDeviceResponse setMarker(String marker) {
        this.marker = marker;
        return this;
    }
    public String getMarker() {
        return this.marker;
    }

}
