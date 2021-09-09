// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * GetFileCountResponse
 */
public class GetFileCountResponse extends TeaModel {
    // file_count
    @NameInMap("file_count")
    public Long fileCount;

    public static GetFileCountResponse build(java.util.Map<String, ?> map) throws Exception {
        GetFileCountResponse self = new GetFileCountResponse();
        return TeaModel.build(map, self);
    }

    public GetFileCountResponse setFileCount(Long fileCount) {
        this.fileCount = fileCount;
        return this;
    }
    public Long getFileCount() {
        return this.fileCount;
    }

}
