// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 *
 */
public class MemberIDInfo extends TeaModel {
    @NameInMap("member_type")
    public String memberType;

    @NameInMap("sub_group_id")
    public String subGroupId;

    @NameInMap("user_id")
    public String userId;

    public static MemberIDInfo build(java.util.Map<String, ?> map) throws Exception {
        MemberIDInfo self = new MemberIDInfo();
        return TeaModel.build(map, self);
    }

    public MemberIDInfo setMemberType(String memberType) {
        this.memberType = memberType;
        return this;
    }
    public String getMemberType() {
        return this.memberType;
    }

    public MemberIDInfo setSubGroupId(String subGroupId) {
        this.subGroupId = subGroupId;
        return this;
    }
    public String getSubGroupId() {
        return this.subGroupId;
    }

    public MemberIDInfo setUserId(String userId) {
        this.userId = userId;
        return this;
    }
    public String getUserId() {
        return this.userId;
    }

}
