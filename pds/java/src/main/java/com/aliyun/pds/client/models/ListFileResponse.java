// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * List file response
 */
public class ListFileResponse extends TeaModel {
    /**
     * <p>items</p>
     */
    @NameInMap("items")
    public java.util.List<BaseCCPFileResponse> items;

    /**
     * <p>next_marker</p>
     */
    @NameInMap("next_marker")
    public String nextMarker;

    /**
     * <p>punished_file_count</p>
     */
    @NameInMap("punished_file_count")
    public Long punishedFileCount;

    public static ListFileResponse build(java.util.Map<String, ?> map) throws Exception {
        ListFileResponse self = new ListFileResponse();
        return TeaModel.build(map, self);
    }

    public ListFileResponse setItems(java.util.List<BaseCCPFileResponse> items) {
        this.items = items;
        return this;
    }
    public java.util.List<BaseCCPFileResponse> getItems() {
        return this.items;
    }

    public ListFileResponse setNextMarker(String nextMarker) {
        this.nextMarker = nextMarker;
        return this;
    }
    public String getNextMarker() {
        return this.nextMarker;
    }

    public ListFileResponse setPunishedFileCount(Long punishedFileCount) {
        this.punishedFileCount = punishedFileCount;
        return this;
    }
    public Long getPunishedFileCount() {
        return this.punishedFileCount;
    }

}
