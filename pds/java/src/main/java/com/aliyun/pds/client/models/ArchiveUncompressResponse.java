// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 解压 response
 */
public class ArchiveUncompressResponse extends TeaModel {
    @NameInMap("state")
    public String state;

    @NameInMap("task_id")
    public String taskId;

    public static ArchiveUncompressResponse build(java.util.Map<String, ?> map) throws Exception {
        ArchiveUncompressResponse self = new ArchiveUncompressResponse();
        return TeaModel.build(map, self);
    }

    public ArchiveUncompressResponse setState(String state) {
        this.state = state;
        return this;
    }
    public String getState() {
        return this.state;
    }

    public ArchiveUncompressResponse setTaskId(String taskId) {
        this.taskId = taskId;
        return this;
    }
    public String getTaskId() {
        return this.taskId;
    }

}
