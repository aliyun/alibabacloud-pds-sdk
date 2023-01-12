// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class LinkInfoListResponse extends TeaModel {
    /**
     * <p>items</p>
     */
    @NameInMap("items")
    @Validation(required = true)
    public java.util.List<LinkInfoResponse> items;

    public static LinkInfoListResponse build(java.util.Map<String, ?> map) throws Exception {
        LinkInfoListResponse self = new LinkInfoListResponse();
        return TeaModel.build(map, self);
    }

    public LinkInfoListResponse setItems(java.util.List<LinkInfoResponse> items) {
        this.items = items;
        return this;
    }
    public java.util.List<LinkInfoResponse> getItems() {
        return this.items;
    }

}
