// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * copy view files
 */
public class CopyViewFilesResponse extends TeaModel {
    /**
     * <p>async_task_id</p>
     */
    @NameInMap("async_task_id")
    public String asyncTaskId;

    public static CopyViewFilesResponse build(java.util.Map<String, ?> map) throws Exception {
        CopyViewFilesResponse self = new CopyViewFilesResponse();
        return TeaModel.build(map, self);
    }

    public CopyViewFilesResponse setAsyncTaskId(String asyncTaskId) {
        this.asyncTaskId = asyncTaskId;
        return this;
    }
    public String getAsyncTaskId() {
        return this.asyncTaskId;
    }

}
