// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * Get AsyncTask Response
 */
public class AsyncTaskResponse extends TeaModel {
    /**
     * <p>async_task_id</p>
     * <p>type:string</p>
     */
    @NameInMap("async_task_id")
    public String asyncTaskId;

    /**
     * <p>created_at</p>
     */
    @NameInMap("created_at")
    public Long createdAt;

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
     * <p>state</p>
     */
    @NameInMap("state")
    public String state;

    /**
     * <p>type</p>
     */
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

    public AsyncTaskResponse setCreatedAt(Long createdAt) {
        this.createdAt = createdAt;
        return this;
    }
    public Long getCreatedAt() {
        return this.createdAt;
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
