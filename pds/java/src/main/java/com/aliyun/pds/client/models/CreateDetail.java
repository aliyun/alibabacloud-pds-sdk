// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 *
 */
public class CreateDetail extends TeaModel {
    // CreateType
    @NameInMap("create_type")
    public String createType;

    // SrcFileID
    @NameInMap("src_file_id")
    public String srcFileId;

    public static CreateDetail build(java.util.Map<String, ?> map) throws Exception {
        CreateDetail self = new CreateDetail();
        return TeaModel.build(map, self);
    }

    public CreateDetail setCreateType(String createType) {
        this.createType = createType;
        return this;
    }
    public String getCreateType() {
        return this.createType;
    }

    public CreateDetail setSrcFileId(String srcFileId) {
        this.srcFileId = srcFileId;
        return this;
    }
    public String getSrcFileId() {
        return this.srcFileId;
    }

}
