// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

/**
 * Get default drive request
 */
public class GetDefaultDriveRequest extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // 用户ID
    @NameInMap("user_id")
    public String userId;

    public static GetDefaultDriveRequest build(java.util.Map<String, ?> map) throws Exception {
        GetDefaultDriveRequest self = new GetDefaultDriveRequest();
        return TeaModel.build(map, self);
    }

    public GetDefaultDriveRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetDefaultDriveRequest setUserId(String userId) {
        this.userId = userId;
        return this;
    }
    public String getUserId() {
        return this.userId;
    }

}
