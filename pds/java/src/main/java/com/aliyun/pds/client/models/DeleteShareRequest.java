// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * delete share request
 */
public class DeleteShareRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    /**
     * <p>share_id</p>
     */
    @NameInMap("share_id")
    @Validation(required = true)
    public String shareId;

    public static DeleteShareRequest build(java.util.Map<String, ?> map) throws Exception {
        DeleteShareRequest self = new DeleteShareRequest();
        return TeaModel.build(map, self);
    }

    public DeleteShareRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public DeleteShareRequest setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

}
