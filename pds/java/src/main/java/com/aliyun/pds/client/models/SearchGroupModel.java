// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class SearchGroupModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public SearchGroupResponse body;

    public static SearchGroupModel build(java.util.Map<String, ?> map) throws Exception {
        SearchGroupModel self = new SearchGroupModel();
        return TeaModel.build(map, self);
    }

    public SearchGroupModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public SearchGroupModel setBody(SearchGroupResponse body) {
        this.body = body;
        return this;
    }
    public SearchGroupResponse getBody() {
        return this.body;
    }

}
