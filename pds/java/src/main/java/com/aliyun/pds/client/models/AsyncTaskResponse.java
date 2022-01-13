// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * Get AsyncTask Response
 */
public class AsyncTaskResponse extends TeaModel {
    // async_task_id
    // type:string
    @NameInMap("async_task_id")
    public String asyncTaskId;

    // err_code
    @NameInMap("err_code")
    public Long errCode;

    // message
    @NameInMap("message")
    public String message;

    // state
    @NameInMap("state")
    public String state;

    // type
    @NameInMap("type")
    public String type;

    public static AsyncTaskResponse build(java.util.Map<String, ?> map) throws Exception {
        AsyncTaskResponse self = new AsyncTaskResponse();
        return TeaModel.build(map, self);
    }

    public AsyncTaskResponse setAsyncTaskId(String asyncTaskId) {
        this.asyncTaskId = asyncTaskId;
        return this;
    }
    public String getAsyncTaskId() {
        return this.asyncTaskId;
    }

    public AsyncTaskResponse setErrCode(Long errCode) {
        this.errCode = errCode;
        return this;
    }
    public Long getErrCode() {
        return this.errCode;
    }

    public AsyncTaskResponse setMessage(String message) {
        this.message = message;
        return this;
    }
    public String getMessage() {
        return this.message;
    }

    public AsyncTaskResponse setState(String state) {
        this.state = state;
        return this;
    }
    public String getState() {
        return this.state;
    }

    public AsyncTaskResponse setType(String type) {
        this.type = type;
        return this;
    }
    public String getType() {
        return this.type;
    }

}
