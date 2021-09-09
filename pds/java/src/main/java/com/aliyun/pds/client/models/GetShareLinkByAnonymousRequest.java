// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * get_share_link_by_anonymous request
 */
public class GetShareLinkByAnonymousRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    // share_id
    @NameInMap("share_id")
    public String shareId;

    public static GetShareLinkByAnonymousRequest build(java.util.Map<String, ?> map) throws Exception {
        GetShareLinkByAnonymousRequest self = new GetShareLinkByAnonymousRequest();
        return TeaModel.build(map, self);
    }

    public GetShareLinkByAnonymousRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public GetShareLinkByAnonymousRequest setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

}
