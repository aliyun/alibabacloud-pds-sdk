// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class BaseGroupRequest extends TeaModel {
    /**
     * <p>描述</p>
     */
    @NameInMap("description")
    public String description;

    /**
     * <p>名称</p>
     */
    @NameInMap("group_name")
    @Validation(required = true)
    public String groupName;

    /**
     * <p>是否是根group</p>
     */
    @NameInMap("is_root")
    public Boolean isRoot;

    public static BaseGroupRequest build(java.util.Map<String, ?> map) throws Exception {
        BaseGroupRequest self = new BaseGroupRequest();
        return TeaModel.build(map, self);
    }

    public BaseGroupRequest setDescription(String description) {
        this.description = description;
        return this;
    }
    public String getDescription() {
        return this.description;
    }

    public BaseGroupRequest setGroupName(String groupName) {
        this.groupName = groupName;
        return this;
    }
    public String getGroupName() {
        return this.groupName;
    }

    public BaseGroupRequest setIsRoot(Boolean isRoot) {
        this.isRoot = isRoot;
        return this;
    }
    public Boolean getIsRoot() {
        return this.isRoot;
    }

}
