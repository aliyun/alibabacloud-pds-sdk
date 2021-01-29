// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

/**
 * get_share_link_by_anonymous request
 */
public class GetShareLinkByAnonymousRequest extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // share_id
    @NameInMap("share_id")
    public String shareId;

    public static GetShareLinkByAnonymousRequest build(java.util.Map<String, ?> map) throws Exception {
        GetShareLinkByAnonymousRequest self = new GetShareLinkByAnonymousRequest();
        return TeaModel.build(map, self);
    }

    public GetShareLinkByAnonymousRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetShareLinkByAnonymousRequest setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

}
