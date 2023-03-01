// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * get_share_id response
 */
public class GetShareLinkIDResponse extends TeaModel {
    /**
     * <p>share_id</p>
     */
    @NameInMap("share_id")
    public String shareId;

    /**
     * <p>share_pwd</p>
     */
    @NameInMap("share_pwd")
    public String sharePwd;

    public static GetShareLinkIDResponse build(java.util.Map<String, ?> map) throws Exception {
        GetShareLinkIDResponse self = new GetShareLinkIDResponse();
        return TeaModel.build(map, self);
    }

    public GetShareLinkIDResponse setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

    public GetShareLinkIDResponse setSharePwd(String sharePwd) {
        this.sharePwd = sharePwd;
        return this;
    }
    public String getSharePwd() {
        return this.sharePwd;
    }

}
