// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * delete share request
 */
public class DeleteShareRequest extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // share_id
    @NameInMap("share_id")
    @Validation(required = true)
    public String shareId;

    public static DeleteShareRequest build(java.util.Map<String, ?> map) throws Exception {
        DeleteShareRequest self = new DeleteShareRequest();
        return TeaModel.build(map, self);
    }

    public DeleteShareRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public DeleteShareRequest setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

}
