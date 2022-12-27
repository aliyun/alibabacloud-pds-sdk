// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class RestoreDetail extends TeaModel {
    // SrcParentFileID
    @NameInMap("src_parent_file_id")
    public String srcParentFileId;

    // TgtParentFileID
    @NameInMap("tgt_parent_file_id")
    public String tgtParentFileId;

    public static RestoreDetail build(java.util.Map<String, ?> map) throws Exception {
        RestoreDetail self = new RestoreDetail();
        return TeaModel.build(map, self);
    }

    public RestoreDetail setSrcParentFileId(String srcParentFileId) {
        this.srcParentFileId = srcParentFileId;
        return this;
    }
    public String getSrcParentFileId() {
        return this.srcParentFileId;
    }

    public RestoreDetail setTgtParentFileId(String tgtParentFileId) {
        this.tgtParentFileId = tgtParentFileId;
        return this;
    }
    public String getTgtParentFileId() {
        return this.tgtParentFileId;
    }

}
