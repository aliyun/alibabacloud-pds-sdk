// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class ListSyncMappingRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    /**
     * <p>SyncMode</p>
     */
    @NameInMap("SyncMode")
    public String SyncMode;

    /**
     * <p>device_name</p>
     */
    @NameInMap("device_name")
    public String deviceName;

    /**
     * <p>limit</p>
     */
    @NameInMap("limit")
    public Integer limit;

    /**
     * <p>marker</p>
     */
    @NameInMap("marker")
    public String marker;

    public static ListSyncMappingRequest build(java.util.Map<String, ?> map) throws Exception {
        ListSyncMappingRequest self = new ListSyncMappingRequest();
        return TeaModel.build(map, self);
    }

    public ListSyncMappingRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public ListSyncMappingRequest setSyncMode(String SyncMode) {
        this.SyncMode = SyncMode;
        return this;
    }
    public String getSyncMode() {
        return this.SyncMode;
    }

    public ListSyncMappingRequest setDeviceName(String deviceName) {
        this.deviceName = deviceName;
        return this;
    }
    public String getDeviceName() {
        return this.deviceName;
    }

    public ListSyncMappingRequest setLimit(Integer limit) {
        this.limit = limit;
        return this;
    }
    public Integer getLimit() {
        return this.limit;
    }

    public ListSyncMappingRequest setMarker(String marker) {
        this.marker = marker;
        return this;
    }
    public String getMarker() {
        return this.marker;
    }

}
