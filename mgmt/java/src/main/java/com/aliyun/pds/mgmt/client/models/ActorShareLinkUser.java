// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class ActorShareLinkUser extends TeaModel {
    // Creator
    @NameInMap("creator")
    public String creator;

    // ShareID
    @NameInMap("share_id")
    public String shareId;

    public static ActorShareLinkUser build(java.util.Map<String, ?> map) throws Exception {
        ActorShareLinkUser self = new ActorShareLinkUser();
        return TeaModel.build(map, self);
    }

    public ActorShareLinkUser setCreator(String creator) {
        this.creator = creator;
        return this;
    }
    public String getCreator() {
        return this.creator;
    }

    public ActorShareLinkUser setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

}
