// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.standard.client.models;

import com.aliyun.tea.*;

/**
 * list store file
 */
public class ListStoreFileRequest extends TeaModel {
    // limit
    @NameInMap("limit")
    public Long limit;

    // marker
    @NameInMap("marker")
    public String marker;

    // parent_file_path
    @NameInMap("parent_file_path")
    public String parentFilePath;

    // store_id
    @NameInMap("store_id")
    public String storeId;

    // type
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
