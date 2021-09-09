// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * cancel_share_link request
 */
public class CancelShareLinkRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    // share_id
    @NameInMap("share_id")
    public String shareId;

    public static CancelShareLinkRequest build(java.util.Map<String, ?> map) throws Exception {
        CancelShareLinkRequest self = new CancelShareLinkRequest();
        return TeaModel.build(map, self);
    }

    public CancelShareLinkRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public CancelShareLinkRequest setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

}
