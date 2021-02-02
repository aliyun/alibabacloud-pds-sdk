// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.hostingmode.client.models;

import com.aliyun.tea.*;

/**
 * get_share_link_by_anonymous request
 */
public class GetShareLinkByAnonymousRequest extends TeaModel {
    // share_id
    @NameInMap("share_id")
    public String shareId;

    public static GetShareLinkByAnonymousRequest build(java.util.Map<String, ?> map) throws Exception {
        GetShareLinkByAnonymousRequest self = new GetShareLinkByAnonymousRequest();
        return TeaModel.build(map, self);
    }

    public GetShareLinkByAnonymousRequest setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

}
