// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 *
 */
public class TrashDetail extends TeaModel {
    // ParentFileID
    @NameInMap("parent_file_id")
    public String parentFileId;

    public static TrashDetail build(java.util.Map<String, ?> map) throws Exception {
        TrashDetail self = new TrashDetail();
        return TeaModel.build(map, self);
    }

    public TrashDetail setParentFileId(String parentFileId) {
        this.parentFileId = parentFileId;
        return this;
    }
    public String getParentFileId() {
        return this.parentFileId;
    }

}
