// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.hostingmode.client.models;

import com.aliyun.tea.*;

/**
 * get share request
 */
public class GetShareRequest extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // share_id
    @NameInMap("share_id")
    public String shareId;

    public static GetShareRequest build(java.util.Map<String, ?> map) throws Exception {
        GetShareRequest self = new GetShareRequest();
        return TeaModel.build(map, self);
    }

    public GetShareRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetShareRequest setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

}
