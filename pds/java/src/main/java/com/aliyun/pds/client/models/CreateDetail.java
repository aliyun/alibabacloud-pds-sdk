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

    @NameInMap("is_over_write")
    public Boolean isOverWrite;

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

    public CreateDetail setIsOverWrite(Boolean isOverWrite) {
        this.isOverWrite = isOverWrite;
        return this;
    }
    public Boolean getIsOverWrite() {
        return this.isOverWrite;
    }

    public CreateDetail setSrcFileId(String srcFileId) {
        this.srcFileId = srcFileId;
        return this;
    }
    public String getSrcFileId() {
        return this.srcFileId;
    }

}
