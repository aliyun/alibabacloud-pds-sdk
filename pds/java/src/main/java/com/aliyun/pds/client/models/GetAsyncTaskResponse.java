// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * Get AsyncTask Response
 */
public class GetAsyncTaskResponse extends TeaModel {
    /**
     * <p>async_task_id</p>
     * <p>type:string</p>
     */
    @NameInMap("async_task_id")
    public String asyncTaskId;

    /**
     * <p>consumed_process</p>
     */
    @NameInMap("consumed_process")
    public Long consumedProcess;

    /**
     * <p>err_code</p>
     */
    @NameInMap("err_code")
    public Long errCode;

    /**
     * <p>message</p>
     */
    @NameInMap("message")
    public String message;

    /**
     * <p>punished_file_count</p>
     */
    @NameInMap("punished_file_count")
    public Long punishedFileCount;

    /**
     * <p>state</p>
     */
    @NameInMap("state")
    public String state;

    /**
     * <p>status</p>
     */
    @NameInMap("status")
    public String status;

    /**
     * <p>total_process</p>
     */
    @NameInMap("total_process")
    public Long totalProcess;

    /**
     * <p>download_url</p>
     * <p>example</p>
     */
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

    public GetAsyncTaskResponse setStatus(String status) {
        this.status = status;
        return this;
    }
    public String getStatus() {
        return this.status;
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
