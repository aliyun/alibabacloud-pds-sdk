// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * Get view request
 */
public class GetViewRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

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

    public static GetViewRequest build(java.util.Map<String, ?> map) throws Exception {
        GetViewRequest self = new GetViewRequest();
        return TeaModel.build(map, self);
    }

    public GetViewRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public GetViewRequest setCategory(String category) {
        this.category = category;
        return this;
    }
    public String getCategory() {
        return this.category;
    }

    public GetViewRequest setUserId(String userId) {
        this.userId = userId;
        return this;
    }
    public String getUserId() {
        return this.userId;
    }

    public GetViewRequest setViewId(String viewId) {
        this.viewId = viewId;
        return this;
    }
    public String getViewId() {
        return this.viewId;
    }

}
