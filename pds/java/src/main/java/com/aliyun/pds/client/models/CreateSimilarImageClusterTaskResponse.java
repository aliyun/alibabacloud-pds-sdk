// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * create similar image cluster task response
 */
public class CreateSimilarImageClusterTaskResponse extends TeaModel {
    @NameInMap("task_id")
    public String taskId;

    public static CreateSimilarImageClusterTaskResponse build(java.util.Map<String, ?> map) throws Exception {
        CreateSimilarImageClusterTaskResponse self = new CreateSimilarImageClusterTaskResponse();
        return TeaModel.build(map, self);
    }

    public CreateSimilarImageClusterTaskResponse setTaskId(String taskId) {
        this.taskId = taskId;
        return this;
    }
    public String getTaskId() {
        return this.taskId;
    }

}
