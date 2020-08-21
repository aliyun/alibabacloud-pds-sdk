// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 展示标签集合
 */
public class ListImageTagsResponse extends TeaModel {
    @NameInMap("tags")
    public java.util.List<ImageTagResponse> tags;

    public static ListImageTagsResponse build(java.util.Map<String, ?> map) throws Exception {
        ListImageTagsResponse self = new ListImageTagsResponse();
        return TeaModel.build(map, self);
    }

    public ListImageTagsResponse setTags(java.util.List<ImageTagResponse> tags) {
        this.tags = tags;
        return this;
    }
    public java.util.List<ImageTagResponse> getTags() {
        return this.tags;
    }

}
