// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * Merge face group response
 */
public class MergeFaceGroupResponse extends TeaModel {
    @NameInMap("status")
    public String status;

    @NameInMap("task_id")
    public String taskId;

    public static MergeFaceGroupResponse build(java.util.Map<String, ?> map) throws Exception {
        MergeFaceGroupResponse self = new MergeFaceGroupResponse();
        return TeaModel.build(map, self);
    }

    public MergeFaceGroupResponse setStatus(String status) {
        this.status = status;
        return this;
    }
    public String getStatus() {
        return this.status;
    }

    public MergeFaceGroupResponse setTaskId(String taskId) {
        this.taskId = taskId;
        return this;
    }
    public String getTaskId() {
        return this.taskId;
    }

}
