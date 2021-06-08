// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * ArchiveStatusResponse response
 */
public class ArchiveStatusResponse extends TeaModel {
    @NameInMap("file_list")
    public java.util.Map<String, ?> fileList;

    @NameInMap("progress")
    public Long progress;

    @NameInMap("state")
    public String state;

    @NameInMap("task_id")
    public String taskId;

    public static ArchiveStatusResponse build(java.util.Map<String, ?> map) throws Exception {
        ArchiveStatusResponse self = new ArchiveStatusResponse();
        return TeaModel.build(map, self);
    }

    public ArchiveStatusResponse setFileList(java.util.Map<String, ?> fileList) {
        this.fileList = fileList;
        return this;
    }
    public java.util.Map<String, ?> getFileList() {
        return this.fileList;
    }

    public ArchiveStatusResponse setProgress(Long progress) {
        this.progress = progress;
        return this;
    }
    public Long getProgress() {
        return this.progress;
    }

    public ArchiveStatusResponse setState(String state) {
        this.state = state;
        return this;
    }
    public String getState() {
        return this.state;
    }

    public ArchiveStatusResponse setTaskId(String taskId) {
        this.taskId = taskId;
        return this;
    }
    public String getTaskId() {
        return this.taskId;
    }

}
