// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.mgmt.mode.models;

import com.aliyun.tea.*;

public class GetCorsRuleListModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public ListDomainCORSRuleResponse body;

    public static GetCorsRuleListModel build(java.util.Map<String, ?> map) throws Exception {
        GetCorsRuleListModel self = new GetCorsRuleListModel();
        return TeaModel.build(map, self);
    }

    public GetCorsRuleListModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetCorsRuleListModel setBody(ListDomainCORSRuleResponse body) {
        this.body = body;
        return this;
    }
    public ListDomainCORSRuleResponse getBody() {
        return this.body;
    }

}
