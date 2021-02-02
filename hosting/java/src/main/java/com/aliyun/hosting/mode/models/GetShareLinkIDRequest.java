// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

/**
 * get_share_id request
 */
public class GetShareLinkIDRequest extends TeaModel {
    // share_msg
    @NameInMap("share_msg")
    public String shareMsg;

    public static GetShareLinkIDRequest build(java.util.Map<String, ?> map) throws Exception {
        GetShareLinkIDRequest self = new GetShareLinkIDRequest();
        return TeaModel.build(map, self);
    }

    public GetShareLinkIDRequest setShareMsg(String shareMsg) {
        this.shareMsg = shareMsg;
        return this;
    }
    public String getShareMsg() {
        return this.shareMsg;
    }

}
