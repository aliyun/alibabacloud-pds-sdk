// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class TrashDetail extends TeaModel {
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

    public static TrashDetail build(java.util.Map<String, ?> map) throws Exception {
        TrashDetail self = new TrashDetail();
        return TeaModel.build(map, self);
    }

    public TrashDetail setSrcParentFileId(String srcParentFileId) {
        this.srcParentFileId = srcParentFileId;
        return this;
    }
    public String getSrcParentFileId() {
        return this.srcParentFileId;
    }

    public TrashDetail setTgtParentFileId(String tgtParentFileId) {
        this.tgtParentFileId = tgtParentFileId;
        return this;
    }
    public String getTgtParentFileId() {
        return this.tgtParentFileId;
    }

}
