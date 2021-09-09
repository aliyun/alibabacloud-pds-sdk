// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class ViewListFileModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public ListViewFilesResponse body;

    public static ViewListFileModel build(java.util.Map<String, ?> map) throws Exception {
        ViewListFileModel self = new ViewListFileModel();
        return TeaModel.build(map, self);
    }

    public ViewListFileModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ViewListFileModel setBody(ListViewFilesResponse body) {
        this.body = body;
        return this;
    }
    public ListViewFilesResponse getBody() {
        return this.body;
    }

}
