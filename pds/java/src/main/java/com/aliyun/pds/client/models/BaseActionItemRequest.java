// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * request
 */
public class BaseActionItemRequest extends TeaModel {
    @NameInMap("action")
    public String action;

    public static BaseActionItemRequest build(java.util.Map<String, ?> map) throws Exception {
        BaseActionItemRequest self = new BaseActionItemRequest();
        return TeaModel.build(map, self);
    }

    public BaseActionItemRequest setAction(String action) {
        this.action = action;
        return this;
    }
    public String getAction() {
        return this.action;
    }

}
