// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class GroupLogDetail extends TeaModel {
    // name
    @NameInMap("name")
    public String name;

    // parent_group_id
    @NameInMap("parent_group_id")
    public String parentGroupId;

    // parent_group_name
    @NameInMap("parent_group_name")
    public String parentGroupName;

    @NameInMap("update_to")
    public GroupLogSettingDetail updateTo;

    public static GroupLogDetail build(java.util.Map<String, ?> map) throws Exception {
        GroupLogDetail self = new GroupLogDetail();
        return TeaModel.build(map, self);
    }

    public GroupLogDetail setName(String name) {
        this.name = name;
        return this;
    }
    public String getName() {
        return this.name;
    }

    public GroupLogDetail setParentGroupId(String parentGroupId) {
        this.parentGroupId = parentGroupId;
        return this;
    }
    public String getParentGroupId() {
        return this.parentGroupId;
    }

    public GroupLogDetail setParentGroupName(String parentGroupName) {
        this.parentGroupName = parentGroupName;
        return this;
    }
    public String getParentGroupName() {
        return this.parentGroupName;
    }

    public GroupLogDetail setUpdateTo(GroupLogSettingDetail updateTo) {
        this.updateTo = updateTo;
        return this;
    }
    public GroupLogSettingDetail getUpdateTo() {
        return this.updateTo;
    }

}
