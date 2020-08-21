// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.standard.client.models;

import com.aliyun.tea.*;

/**
 * 展示人脸分组集合
 */
public class ListImageFaceGroupsResponse extends TeaModel {
    @NameInMap("items")
    public java.util.List<ImageFaceGroupResponse> items;

    @NameInMap("next_marker")
    public String nextMarker;

    public static ListImageFaceGroupsResponse build(java.util.Map<String, ?> map) throws Exception {
        ListImageFaceGroupsResponse self = new ListImageFaceGroupsResponse();
        return TeaModel.build(map, self);
    }

    public ListImageFaceGroupsResponse setItems(java.util.List<ImageFaceGroupResponse> items) {
        this.items = items;
        return this;
    }
    public java.util.List<ImageFaceGroupResponse> getItems() {
        return this.items;
    }

    public ListImageFaceGroupsResponse setNextMarker(String nextMarker) {
        this.nextMarker = nextMarker;
        return this;
    }
    public String getNextMarker() {
        return this.nextMarker;
    }

}
