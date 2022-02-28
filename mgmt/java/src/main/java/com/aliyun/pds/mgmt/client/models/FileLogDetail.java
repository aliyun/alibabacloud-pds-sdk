// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class FileLogDetail extends TeaModel {
    // new_name
    @NameInMap("new_name")
    public String newName;

    // parent_path
    @NameInMap("parent_path")
    public String parentPath;

    // to_parent_path
    @NameInMap("to_parent_path")
    public String toParentPath;

    // to_parent_path_type
    @NameInMap("to_parent_path_type")
    public String toParentPathType;

    // type
    @NameInMap("type")
    public String type;

    public static FileLogDetail build(java.util.Map<String, ?> map) throws Exception {
        FileLogDetail self = new FileLogDetail();
        return TeaModel.build(map, self);
    }

    public FileLogDetail setNewName(String newName) {
        this.newName = newName;
        return this;
    }
    public String getNewName() {
        return this.newName;
    }

    public FileLogDetail setParentPath(String parentPath) {
        this.parentPath = parentPath;
        return this;
    }
    public String getParentPath() {
        return this.parentPath;
    }

    public FileLogDetail setToParentPath(String toParentPath) {
        this.toParentPath = toParentPath;
        return this;
    }
    public String getToParentPath() {
        return this.toParentPath;
    }

    public FileLogDetail setToParentPathType(String toParentPathType) {
        this.toParentPathType = toParentPathType;
        return this;
    }
    public String getToParentPathType() {
        return this.toParentPathType;
    }

    public FileLogDetail setType(String type) {
        this.type = type;
        return this;
    }
    public String getType() {
        return this.type;
    }

}
