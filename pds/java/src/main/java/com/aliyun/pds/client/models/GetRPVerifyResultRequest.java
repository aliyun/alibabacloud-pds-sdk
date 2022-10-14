// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class GetRPVerifyResultRequest extends TeaModel {
    // During Verify Process, 是否在实人认证流程中调用
    @NameInMap("during_verify_process")
    public Boolean duringVerifyProcess;

    // User ID, 当前访问的用户
    @NameInMap("user_id")
    @Validation(required = true)
    public String userId;

    public static GetRPVerifyResultRequest build(java.util.Map<String, ?> map) throws Exception {
        GetRPVerifyResultRequest self = new GetRPVerifyResultRequest();
        return TeaModel.build(map, self);
    }

    public GetRPVerifyResultRequest setDuringVerifyProcess(Boolean duringVerifyProcess) {
        this.duringVerifyProcess = duringVerifyProcess;
        return this;
    }
    public Boolean getDuringVerifyProcess() {
        return this.duringVerifyProcess;
    }

    public GetRPVerifyResultRequest setUserId(String userId) {
        this.userId = userId;
        return this;
    }
    public String getUserId() {
        return this.userId;
    }

}
