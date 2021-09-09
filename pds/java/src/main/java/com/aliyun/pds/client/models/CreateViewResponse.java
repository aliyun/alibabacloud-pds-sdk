// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 创建逻辑视图
 */
public class CreateViewResponse extends TeaModel {
    @NameInMap("category")
    public String category;

    @NameInMap("owner")
    public String owner;

    @NameInMap("view_id")
    public String viewId;

    public static CreateViewResponse build(java.util.Map<String, ?> map) throws Exception {
        CreateViewResponse self = new CreateViewResponse();
        return TeaModel.build(map, self);
    }

    public CreateViewResponse setCategory(String category) {
        this.category = category;
        return this;
    }
    public String getCategory() {
        return this.category;
    }

    public CreateViewResponse setOwner(String owner) {
        this.owner = owner;
        return this;
    }
    public String getOwner() {
        return this.owner;
    }

    public CreateViewResponse setViewId(String viewId) {
        this.viewId = viewId;
        return this;
    }
    public String getViewId() {
        return this.viewId;
    }

}
