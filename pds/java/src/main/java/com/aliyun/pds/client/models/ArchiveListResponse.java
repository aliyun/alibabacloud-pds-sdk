// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 预览压缩包结构 response
 */
public class ArchiveListResponse extends TeaModel {
    @NameInMap("file_list")
    public java.util.Map<String, ?> fileList;

    @NameInMap("state")
    public String state;

    @NameInMap("task_id")
    public String taskId;

    public static ArchiveListResponse build(java.util.Map<String, ?> map) throws Exception {
        ArchiveListResponse self = new ArchiveListResponse();
        return TeaModel.build(map, self);
    }

    public ArchiveListResponse setFileList(java.util.Map<String, ?> fileList) {
        this.fileList = fileList;
        return this;
    }
    public java.util.Map<String, ?> getFileList() {
        return this.fileList;
    }

    public ArchiveListResponse setState(String state) {
        this.state = state;
        return this;
    }
    public String getState() {
        return this.state;
    }

    public ArchiveListResponse setTaskId(String taskId) {
        this.taskId = taskId;
        return this;
    }
    public String getTaskId() {
        return this.taskId;
    }

}
