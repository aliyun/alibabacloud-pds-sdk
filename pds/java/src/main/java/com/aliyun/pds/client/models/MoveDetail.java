// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 *
 */
public class MoveDetail extends TeaModel {
    // SrcParentFileID
    @NameInMap("src_parent_file_id")
    public String srcParentFileId;

    // TgtParentFileID
    @NameInMap("tgt_parent_file_id")
    public String tgtParentFileId;

    public static MoveDetail build(java.util.Map<String, ?> map) throws Exception {
        MoveDetail self = new MoveDetail();
        return TeaModel.build(map, self);
    }

    public MoveDetail setSrcParentFileId(String srcParentFileId) {
        this.srcParentFileId = srcParentFileId;
        return this;
    }
    public String getSrcParentFileId() {
        return this.srcParentFileId;
    }

    public MoveDetail setTgtParentFileId(String tgtParentFileId) {
        this.tgtParentFileId = tgtParentFileId;
        return this;
    }
    public String getTgtParentFileId() {
        return this.tgtParentFileId;
    }

}
