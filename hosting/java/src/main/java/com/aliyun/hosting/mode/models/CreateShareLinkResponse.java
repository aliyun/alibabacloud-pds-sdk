// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

/**
 * create_share_link response
 */
public class CreateShareLinkResponse extends TeaModel {
    // share_id
    @NameInMap("share_id")
    public String shareId;

    // share_msg
    @NameInMap("share_msg")
    public String shareMsg;

    // share_policy
    @NameInMap("share_policy")
    public String sharePolicy;

    // share_pwd
    @NameInMap("share_pwd")
    public String sharePwd;

    // share_url
    @NameInMap("share_url")
    public String shareUrl;

    public static CreateShareLinkResponse build(java.util.Map<String, ?> map) throws Exception {
        CreateShareLinkResponse self = new CreateShareLinkResponse();
        return TeaModel.build(map, self);
    }

    public CreateShareLinkResponse setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

    public CreateShareLinkResponse setShareMsg(String shareMsg) {
        this.shareMsg = shareMsg;
        return this;
    }
    public String getShareMsg() {
        return this.shareMsg;
    }

    public CreateShareLinkResponse setSharePolicy(String sharePolicy) {
        this.sharePolicy = sharePolicy;
        return this;
    }
    public String getSharePolicy() {
        return this.sharePolicy;
    }

    public CreateShareLinkResponse setSharePwd(String sharePwd) {
        this.sharePwd = sharePwd;
        return this;
    }
    public String getSharePwd() {
        return this.sharePwd;
    }

    public CreateShareLinkResponse setShareUrl(String shareUrl) {
        this.shareUrl = shareUrl;
        return this;
    }
    public String getShareUrl() {
        return this.shareUrl;
    }

}
