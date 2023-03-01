// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * list store file
 */
public class ListStoreFileRequest extends TeaModel {
    /**
     * <p>limit</p>
     */
    @NameInMap("limit")
    @Validation(maximum = 1000, minimum = 1)
    public Long limit;

    /**
     * <p>marker</p>
     */
    @NameInMap("marker")
    public String marker;

    /**
     * <p>parent_file_path</p>
     */
    @NameInMap("parent_file_path")
    public String parentFilePath;

    /**
     * <p>store_id</p>
     */
    @NameInMap("store_id")
    public String storeId;

    /**
     * <p>type</p>
     */
    @NameInMap("type")
    public String type;

    public static ListStoreFileRequest build(java.util.Map<String, ?> map) throws Exception {
        ListStoreFileRequest self = new ListStoreFileRequest();
        return TeaModel.build(map, self);
    }

    public ListStoreFileRequest setLimit(Long limit) {
        this.limit = limit;
        return this;
    }
    public Long getLimit() {
        return this.limit;
    }

    public ListStoreFileRequest setMarker(String marker) {
        this.marker = marker;
        return this;
    }
    public String getMarker() {
        return this.marker;
    }

    public ListStoreFileRequest setParentFilePath(String parentFilePath) {
        this.parentFilePath = parentFilePath;
        return this;
    }
    public String getParentFilePath() {
        return this.parentFilePath;
    }

    public ListStoreFileRequest setStoreId(String storeId) {
        this.storeId = storeId;
        return this;
    }
    public String getStoreId() {
        return this.storeId;
    }

    public ListStoreFileRequest setType(String type) {
        this.type = type;
        return this;
    }
    public String getType() {
        return this.type;
    }

}
