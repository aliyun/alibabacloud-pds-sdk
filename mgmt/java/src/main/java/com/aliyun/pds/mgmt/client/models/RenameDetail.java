// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class RenameDetail extends TeaModel {
    /**
     * <p>NewName</p>
     */
    @NameInMap("new_name")
    public String newName;

    /**
     * <p>OldName</p>
     */
    @NameInMap("old_name")
    public String oldName;

    public static RenameDetail build(java.util.Map<String, ?> map) throws Exception {
        RenameDetail self = new RenameDetail();
        return TeaModel.build(map, self);
    }

    public RenameDetail setNewName(String newName) {
        this.newName = newName;
        return this;
    }
    public String getNewName() {
        return this.newName;
    }

    public RenameDetail setOldName(String oldName) {
        this.oldName = oldName;
        return this;
    }
    public String getOldName() {
        return this.oldName;
    }

}
