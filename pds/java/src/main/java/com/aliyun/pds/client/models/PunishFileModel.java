// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class PunishFileModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    public static PunishFileModel build(java.util.Map<String, ?> map) throws Exception {
        PunishFileModel self = new PunishFileModel();
        return TeaModel.build(map, self);
    }

    public PunishFileModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

}
