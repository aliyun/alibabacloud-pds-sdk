// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * Pre_create_check response
 */
public class PreCreateCheckResponse extends TeaModel {
    @NameInMap("name_check_result")
    public NameCheckResult nameCheckResult;

    // result_code
    @NameInMap("result_code")
    public String resultCode;

    public static PreCreateCheckResponse build(java.util.Map<String, ?> map) throws Exception {
        PreCreateCheckResponse self = new PreCreateCheckResponse();
        return TeaModel.build(map, self);
    }

    public PreCreateCheckResponse setNameCheckResult(NameCheckResult nameCheckResult) {
        this.nameCheckResult = nameCheckResult;
        return this;
    }
    public NameCheckResult getNameCheckResult() {
        return this.nameCheckResult;
    }

    public PreCreateCheckResponse setResultCode(String resultCode) {
        this.resultCode = resultCode;
        return this;
    }
    public String getResultCode() {
        return this.resultCode;
    }

}
