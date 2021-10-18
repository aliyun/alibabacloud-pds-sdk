// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class SearchDrivesModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public SearchDriveResponse body;

    public static SearchDrivesModel build(java.util.Map<String, ?> map) throws Exception {
        SearchDrivesModel self = new SearchDrivesModel();
        return TeaModel.build(map, self);
    }

    public SearchDrivesModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public SearchDrivesModel setBody(SearchDriveResponse body) {
        this.body = body;
        return this;
    }
    public SearchDriveResponse getBody() {
        return this.body;
    }

}
