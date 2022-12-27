// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class DeleteDetail extends TeaModel {
    /**
     * <p>SrcParentFileID</p>
     */
    @NameInMap("src_parent_file_id")
    public String srcParentFileId;

    /**
     * <p>TgtParentFileID</p>
     */
    @NameInMap("tgt_parent_file_id")
    public String tgtParentFileId;

    public static DeleteDetail build(java.util.Map<String, ?> map) throws Exception {
        DeleteDetail self = new DeleteDetail();
        return TeaModel.build(map, self);
    }

    public DeleteDetail setSrcParentFileId(String srcParentFileId) {
        this.srcParentFileId = srcParentFileId;
        return this;
    }
    public String getSrcParentFileId() {
        return this.srcParentFileId;
    }

    public DeleteDetail setTgtParentFileId(String tgtParentFileId) {
        this.tgtParentFileId = tgtParentFileId;
        return this;
    }
    public String getTgtParentFileId() {
        return this.tgtParentFileId;
    }

}
