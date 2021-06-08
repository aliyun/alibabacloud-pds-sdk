// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class ArchiveFilesModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public CCPArchiveFilesResponse body;

    public static ArchiveFilesModel build(java.util.Map<String, ?> map) throws Exception {
        ArchiveFilesModel self = new ArchiveFilesModel();
        return TeaModel.build(map, self);
    }

    public ArchiveFilesModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ArchiveFilesModel setBody(CCPArchiveFilesResponse body) {
        this.body = body;
        return this;
    }
    public CCPArchiveFilesResponse getBody() {
        return this.body;
    }

}
