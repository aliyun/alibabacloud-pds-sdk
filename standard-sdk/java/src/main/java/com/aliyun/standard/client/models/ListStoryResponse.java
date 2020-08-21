// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.standard.client.models;

import com.aliyun.tea.*;

/**
 * 故事列表
 */
public class ListStoryResponse extends TeaModel {
    // items
    @NameInMap("items")
    public java.util.List<StoryResponse> items;

    // next_marker
    @NameInMap("next_marker")
    public String nextMarker;

    public static ListStoryResponse build(java.util.Map<String, ?> map) throws Exception {
        ListStoryResponse self = new ListStoryResponse();
        return TeaModel.build(map, self);
    }

    public ListStoryResponse setItems(java.util.List<StoryResponse> items) {
        this.items = items;
        return this;
    }
    public java.util.List<StoryResponse> getItems() {
        return this.items;
    }

    public ListStoryResponse setNextMarker(String nextMarker) {
        this.nextMarker = nextMarker;
        return this;
    }
    public String getNextMarker() {
        return this.nextMarker;
    }

}
