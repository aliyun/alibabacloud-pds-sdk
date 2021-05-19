// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class ActorAliUser extends TeaModel {
    // AliUserID
    @NameInMap("ali_user_id")
    public String aliUserId;

    // AliUserType
    @NameInMap("ali_user_type")
    public String aliUserType;

    public static ActorAliUser build(java.util.Map<String, ?> map) throws Exception {
        ActorAliUser self = new ActorAliUser();
        return TeaModel.build(map, self);
    }

    public ActorAliUser setAliUserId(String aliUserId) {
        this.aliUserId = aliUserId;
        return this;
    }
    public String getAliUserId() {
        return this.aliUserId;
    }

    public ActorAliUser setAliUserType(String aliUserType) {
        this.aliUserType = aliUserType;
        return this;
    }
    public String getAliUserType() {
        return this.aliUserType;
    }

}
