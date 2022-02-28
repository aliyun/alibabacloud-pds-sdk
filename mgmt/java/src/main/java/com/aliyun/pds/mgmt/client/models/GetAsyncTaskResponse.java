// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * Get AsyncTask Response
 */
public class GetAsyncTaskResponse extends TeaModel {
    // async_task_id
    // type:string
    @NameInMap("async_task_id")
    public String asyncTaskId;

    // consumed_process
    @NameInMap("consumed_process")
    public Long consumedProcess;

    // err_code
    @NameInMap("err_code")
    public Long errCode;

    // message
    @NameInMap("message")
    public String message;

    // punished_file_count
    @NameInMap("punished_file_count")
    public Long punishedFileCount;

    // state
    @NameInMap("state")
    public String state;

    // total_process
    @NameInMap("total_process")
    public Long totalProcess;

    // download_url
    // example
    @NameInMap("url")
    public String url;

    public static GetAsyncTaskResponse build(java.util.Map<String, ?> map) throws Exception {
        GetAsyncTaskResponse self = new GetAsyncTaskResponse();
        return TeaModel.build(map, self);
    }

    public GetAsyncTaskResponse setAsyncTaskId(String asyncTaskId) {
        this.asyncTaskId = asyncTaskId;
        return this;
    }
    public String getAsyncTaskId() {
        return this.asyncTaskId;
    }

    public GetAsyncTaskResponse setConsumedProcess(Long consumedProcess) {
        this.consumedProcess = consumedProcess;
        return this;
    }
    public Long getConsumedProcess() {
        return this.consumedProcess;
    }

    public GetAsyncTaskResponse setErrCode(Long errCode) {
        this.errCode = errCode;
        return this;
    }
    public Long getErrCode() {
        return this.errCode;
    }

    public GetAsyncTaskResponse setMessage(String message) {
        this.message = message;
        return this;
    }
    public String getMessage() {
        return this.message;
    }

    public GetAsyncTaskResponse setPunishedFileCount(Long punishedFileCount) {
        this.punishedFileCount = punishedFileCount;
        return this;
    }
    public Long getPunishedFileCount() {
        return this.punishedFileCount;
    }

    public GetAsyncTaskResponse setState(String state) {
        this.state = state;
        return this;
    }
    public String getState() {
        return this.state;
    }

    public GetAsyncTaskResponse setTotalProcess(Long totalProcess) {
        this.totalProcess = totalProcess;
        return this;
    }
    public Long getTotalProcess() {
        return this.totalProcess;
    }

    public GetAsyncTaskResponse setUrl(String url) {
        this.url = url;
        return this;
    }
    public String getUrl() {
        return this.url;
    }

}
