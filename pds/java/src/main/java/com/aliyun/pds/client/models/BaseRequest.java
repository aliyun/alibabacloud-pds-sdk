// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 *
 */
public class BaseRequest extends TeaModel {
    // category
    @NameInMap("category")
    @Validation(required = true)
    public String category;

    // user_id
    @NameInMap("user_id")
    public String userId;

    // view_id
    @NameInMap("view_id")
    @Validation(required = true)
    public String viewId;

    public static BaseRequest build(java.util.Map<String, ?> map) throws Exception {
        BaseRequest self = new BaseRequest();
        return TeaModel.build(map, self);
    }

    public BaseRequest setCategory(String category) {
        this.category = category;
        return this;
    }
    public String getCategory() {
        return this.category;
    }

    public BaseRequest setUserId(String userId) {
        this.userId = userId;
        return this;
    }
    public String getUserId() {
        return this.userId;
    }

    public BaseRequest setViewId(String viewId) {
        this.viewId = viewId;
        return this;
    }
    public String getViewId() {
        return this.viewId;
    }

}
