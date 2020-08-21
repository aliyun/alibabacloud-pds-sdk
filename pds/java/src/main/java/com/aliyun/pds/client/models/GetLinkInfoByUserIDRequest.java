// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class GetLinkInfoByUserIDRequest extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // user ID
    @NameInMap("user_id")
    @Validation(required = true)
    public String userId;

    public static GetLinkInfoByUserIDRequest build(java.util.Map<String, ?> map) throws Exception {
        GetLinkInfoByUserIDRequest self = new GetLinkInfoByUserIDRequest();
        return TeaModel.build(map, self);
    }

    public GetLinkInfoByUserIDRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetLinkInfoByUserIDRequest setUserId(String userId) {
        this.userId = userId;
        return this;
    }
    public String getUserId() {
        return this.userId;
    }

}
