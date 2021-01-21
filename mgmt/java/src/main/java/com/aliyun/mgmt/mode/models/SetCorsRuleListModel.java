// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.mgmt.mode.models;

import com.aliyun.tea.*;

public class SetCorsRuleListModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public ListDomainCORSRuleResponse body;

    public static SetCorsRuleListModel build(java.util.Map<String, ?> map) throws Exception {
        SetCorsRuleListModel self = new SetCorsRuleListModel();
        return TeaModel.build(map, self);
    }

    public SetCorsRuleListModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public SetCorsRuleListModel setBody(ListDomainCORSRuleResponse body) {
        this.body = body;
        return this;
    }
    public ListDomainCORSRuleResponse getBody() {
        return this.body;
    }

}
