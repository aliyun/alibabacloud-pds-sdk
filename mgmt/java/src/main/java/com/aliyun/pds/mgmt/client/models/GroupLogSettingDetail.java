// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class GroupLogSettingDetail extends TeaModel {
    // name
    @NameInMap("name")
    public String name;

    // parent_group_id
    @NameInMap("parent_group_id")
    public String parentGroupId;

    // parent_group_name
    @NameInMap("parent_group_name")
    public String parentGroupName;

    public static GroupLogSettingDetail build(java.util.Map<String, ?> map) throws Exception {
        GroupLogSettingDetail self = new GroupLogSettingDetail();
        return TeaModel.build(map, self);
    }

    public GroupLogSettingDetail setName(String name) {
        this.name = name;
        return this;
    }
    public String getName() {
        return this.name;
    }

    public GroupLogSettingDetail setParentGroupId(String parentGroupId) {
        this.parentGroupId = parentGroupId;
        return this;
    }
    public String getParentGroupId() {
        return this.parentGroupId;
    }

    public GroupLogSettingDetail setParentGroupName(String parentGroupName) {
        this.parentGroupName = parentGroupName;
        return this;
    }
    public String getParentGroupName() {
        return this.parentGroupName;
    }

}
