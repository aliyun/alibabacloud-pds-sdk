// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class MembershipLogDetail extends TeaModel {
    // group_id
    @NameInMap("group_id")
    public String groupId;

    // group_name
    @NameInMap("group_name")
    public String groupName;

    // member_name
    @NameInMap("member_name")
    public String memberName;

    // member_type
    @NameInMap("member_type")
    public String memberType;

    public static MembershipLogDetail build(java.util.Map<String, ?> map) throws Exception {
        MembershipLogDetail self = new MembershipLogDetail();
        return TeaModel.build(map, self);
    }

    public MembershipLogDetail setGroupId(String groupId) {
        this.groupId = groupId;
        return this;
    }
    public String getGroupId() {
        return this.groupId;
    }

    public MembershipLogDetail setGroupName(String groupName) {
        this.groupName = groupName;
        return this;
    }
    public String getGroupName() {
        return this.groupName;
    }

    public MembershipLogDetail setMemberName(String memberName) {
        this.memberName = memberName;
        return this;
    }
    public String getMemberName() {
        return this.memberName;
    }

    public MembershipLogDetail setMemberType(String memberType) {
        this.memberType = memberType;
        return this;
    }
    public String getMemberType() {
        return this.memberType;
    }

}
