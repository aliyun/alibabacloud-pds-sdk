// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class ActorUser extends TeaModel {
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

    public static ActorUser build(java.util.Map<String, ?> map) throws Exception {
        ActorUser self = new ActorUser();
        return TeaModel.build(map, self);
    }

    public ActorUser setUserId(String userId) {
        this.userId = userId;
        return this;
    }
    public String getUserId() {
        return this.userId;
    }

    public ActorUser setUserName(String userName) {
        this.userName = userName;
        return this;
    }
    public String getUserName() {
        return this.userName;
    }

}
