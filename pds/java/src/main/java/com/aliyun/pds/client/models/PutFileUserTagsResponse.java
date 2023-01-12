// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 更新文件 user tags response
 */
public class PutFileUserTagsResponse extends TeaModel {
    /**
     * <p>file_id</p>
     */
    @NameInMap("file_id")
    @Validation(pattern = "[a-z0-9]{1,50}")
    public String fileId;

    public static PutFileUserTagsResponse build(java.util.Map<String, ?> map) throws Exception {
        PutFileUserTagsResponse self = new PutFileUserTagsResponse();
        return TeaModel.build(map, self);
    }

    public PutFileUserTagsResponse setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

}
