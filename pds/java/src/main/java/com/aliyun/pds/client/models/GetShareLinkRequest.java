// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * get_share request
 */
public class GetShareLinkRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    /**
     * <p>share_id</p>
     */
    @NameInMap("share_id")
    public String shareId;

    public static GetShareLinkRequest build(java.util.Map<String, ?> map) throws Exception {
        GetShareLinkRequest self = new GetShareLinkRequest();
        return TeaModel.build(map, self);
    }

    public GetShareLinkRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public GetShareLinkRequest setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

}
