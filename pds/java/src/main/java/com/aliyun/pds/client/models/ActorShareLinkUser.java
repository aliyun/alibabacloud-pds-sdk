// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class ActorShareLinkUser extends TeaModel {
    /**
     * <p>Creator</p>
     */
    @NameInMap("creator")
    public String creator;

    /**
     * <p>ShareID</p>
     */
    @NameInMap("share_id")
    public String shareId;

    /**
     * <p>UserID</p>
     */
    @NameInMap("user_id")
    public String userId;

    /**
     * <p>UserName</p>
     */
    @NameInMap("user_name")
    public String userName;

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

    public ActorShareLinkUser setUserId(String userId) {
        this.userId = userId;
        return this;
    }
    public String getUserId() {
        return this.userId;
    }

    public ActorShareLinkUser setUserName(String userName) {
        this.userName = userName;
        return this;
    }
    public String getUserName() {
        return this.userName;
    }

}
