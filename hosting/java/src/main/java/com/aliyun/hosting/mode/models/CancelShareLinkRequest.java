// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

/**
 * cancel_share_link request
 */
public class CancelShareLinkRequest extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // share_id
    @NameInMap("share_id")
    public String shareId;

    public static CancelShareLinkRequest build(java.util.Map<String, ?> map) throws Exception {
        CancelShareLinkRequest self = new CancelShareLinkRequest();
        return TeaModel.build(map, self);
    }

    public CancelShareLinkRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public CancelShareLinkRequest setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

}
