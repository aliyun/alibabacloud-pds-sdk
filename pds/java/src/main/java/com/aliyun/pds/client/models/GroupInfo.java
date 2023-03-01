// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class GroupInfo extends TeaModel {
    @NameInMap("group_id")
    public String groupId;

    /**
     * <p>MemberRole 暂不对外，只作保留</p>
     */
    @NameInMap("member_role")
    public String memberRole;

    public static GroupInfo build(java.util.Map<String, ?> map) throws Exception {
        GroupInfo self = new GroupInfo();
        return TeaModel.build(map, self);
    }

    public GroupInfo setGroupId(String groupId) {
        this.groupId = groupId;
        return this;
    }
    public String getGroupId() {
        return this.groupId;
    }

    public GroupInfo setMemberRole(String memberRole) {
        this.memberRole = memberRole;
        return this;
    }
    public String getMemberRole() {
        return this.memberRole;
    }

}
