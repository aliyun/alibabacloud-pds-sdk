// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 打包下载response
 */
public class CCPArchiveFilesResponse extends TeaModel {
    @NameInMap("async_task_id")
    public String asyncTaskId;

    public static CCPArchiveFilesResponse build(java.util.Map<String, ?> map) throws Exception {
        CCPArchiveFilesResponse self = new CCPArchiveFilesResponse();
        return TeaModel.build(map, self);
    }

    public CCPArchiveFilesResponse setAsyncTaskId(String asyncTaskId) {
        this.asyncTaskId = asyncTaskId;
        return this;
    }
    public String getAsyncTaskId() {
        return this.asyncTaskId;
    }

}
