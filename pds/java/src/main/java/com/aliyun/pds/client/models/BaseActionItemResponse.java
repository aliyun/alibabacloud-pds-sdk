// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * action response
 */
public class BaseActionItemResponse extends TeaModel {
    @NameInMap("action")
    public String action;

    public static BaseActionItemResponse build(java.util.Map<String, ?> map) throws Exception {
        BaseActionItemResponse self = new BaseActionItemResponse();
        return TeaModel.build(map, self);
    }

    public BaseActionItemResponse setAction(String action) {
        this.action = action;
        return this;
    }
    public String getAction() {
        return this.action;
    }

}
