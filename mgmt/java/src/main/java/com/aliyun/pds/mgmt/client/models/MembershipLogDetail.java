// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class MembershipLogDetail extends TeaModel {
    /**
     * <p>group_id</p>
     */
    @NameInMap("group_id")
    public String groupId;

    /**
     * <p>group_name</p>
     */
    @NameInMap("group_name")
    public String groupName;

    /**
     * <p>member_name</p>
     */
    @NameInMap("member_name")
    public String memberName;

    /**
     * <p>member_type</p>
     */
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
