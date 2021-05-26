// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 生成故事
 */
public class FindStoriesResponse extends TeaModel {
    // items
    @NameInMap("items")
    public java.util.List<GetStoryResponse> items;

    // next_marker
    @NameInMap("next_marker")
    public String nextMarker;

    public static FindStoriesResponse build(java.util.Map<String, ?> map) throws Exception {
        FindStoriesResponse self = new FindStoriesResponse();
        return TeaModel.build(map, self);
    }

    public FindStoriesResponse setItems(java.util.List<GetStoryResponse> items) {
        this.items = items;
        return this;
    }
    public java.util.List<GetStoryResponse> getItems() {
        return this.items;
    }

    public FindStoriesResponse setNextMarker(String nextMarker) {
        this.nextMarker = nextMarker;
        return this;
    }
    public String getNextMarker() {
        return this.nextMarker;
    }

}
