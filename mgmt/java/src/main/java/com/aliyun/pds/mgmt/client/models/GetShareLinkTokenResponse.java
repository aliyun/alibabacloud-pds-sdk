// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * get_share_token response
 */
public class GetShareLinkTokenResponse extends TeaModel {
    // expire_time
    @NameInMap("expire_time")
    @Validation(required = true)
    public String expireTime;

    // expires_in
    @NameInMap("expires_in")
    @Validation(required = true)
    public Long expiresIn;

    // share_token
    @NameInMap("share_token")
    @Validation(required = true)
    public String shareToken;

    public static GetShareLinkTokenResponse build(java.util.Map<String, ?> map) throws Exception {
        GetShareLinkTokenResponse self = new GetShareLinkTokenResponse();
        return TeaModel.build(map, self);
    }

    public GetShareLinkTokenResponse setExpireTime(String expireTime) {
        this.expireTime = expireTime;
        return this;
    }
    public String getExpireTime() {
        return this.expireTime;
    }

    public GetShareLinkTokenResponse setExpiresIn(Long expiresIn) {
        this.expiresIn = expiresIn;
        return this;
    }
    public Long getExpiresIn() {
        return this.expiresIn;
    }

    public GetShareLinkTokenResponse setShareToken(String shareToken) {
        this.shareToken = shareToken;
        return this;
    }
    public String getShareToken() {
        return this.shareToken;
    }

}
