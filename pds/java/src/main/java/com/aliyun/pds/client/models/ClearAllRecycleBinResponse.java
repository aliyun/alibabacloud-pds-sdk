// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * clear all recycle bin response
 */
public class ClearAllRecycleBinResponse extends TeaModel {
    @NameInMap("items")
    public java.util.List<ClearRecycleBinResponse> items;

    public static ClearAllRecycleBinResponse build(java.util.Map<String, ?> map) throws Exception {
        ClearAllRecycleBinResponse self = new ClearAllRecycleBinResponse();
        return TeaModel.build(map, self);
    }

    public ClearAllRecycleBinResponse setItems(java.util.List<ClearRecycleBinResponse> items) {
        this.items = items;
        return this;
    }
    public java.util.List<ClearRecycleBinResponse> getItems() {
        return this.items;
    }

}
