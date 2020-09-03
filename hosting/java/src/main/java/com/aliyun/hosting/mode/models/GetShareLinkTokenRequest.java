// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

/**
 * get_share_token request
 */
public class GetShareLinkTokenRequest extends TeaModel {
    // share_id
    @NameInMap("share_id")
    public String shareId;

    // share_pwd
    @NameInMap("share_pwd")
    public String sharePwd;

    public static GetShareLinkTokenRequest build(java.util.Map<String, ?> map) throws Exception {
        GetShareLinkTokenRequest self = new GetShareLinkTokenRequest();
        return TeaModel.build(map, self);
    }

    public GetShareLinkTokenRequest setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

    public GetShareLinkTokenRequest setSharePwd(String sharePwd) {
        this.sharePwd = sharePwd;
        return this;
    }
    public String getSharePwd() {
        return this.sharePwd;
    }

}
