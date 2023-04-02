// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class DeltaExtInfo extends TeaModel {
    @NameInMap("move_type")
    public String moveType;

    @NameInMap("src_name")
    public String srcName;

    @NameInMap("src_parent_file_id")
    public String srcParentFileId;

    public static DeltaExtInfo build(java.util.Map<String, ?> map) throws Exception {
        DeltaExtInfo self = new DeltaExtInfo();
        return TeaModel.build(map, self);
    }

    public DeltaExtInfo setMoveType(String moveType) {
        this.moveType = moveType;
        return this;
    }
    public String getMoveType() {
        return this.moveType;
    }

    public DeltaExtInfo setSrcName(String srcName) {
        this.srcName = srcName;
        return this;
    }
    public String getSrcName() {
        return this.srcName;
    }

    public DeltaExtInfo setSrcParentFileId(String srcParentFileId) {
        this.srcParentFileId = srcParentFileId;
        return this;
    }
    public String getSrcParentFileId() {
        return this.srcParentFileId;
    }

}
