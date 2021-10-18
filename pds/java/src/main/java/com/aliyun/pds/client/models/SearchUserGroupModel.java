// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class SearchUserGroupModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public SearchUserAndGroupResponse body;

    public static SearchUserGroupModel build(java.util.Map<String, ?> map) throws Exception {
        SearchUserGroupModel self = new SearchUserGroupModel();
        return TeaModel.build(map, self);
    }

    public SearchUserGroupModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public SearchUserGroupModel setBody(SearchUserAndGroupResponse body) {
        this.body = body;
        return this;
    }
    public SearchUserAndGroupResponse getBody() {
        return this.body;
    }

}
