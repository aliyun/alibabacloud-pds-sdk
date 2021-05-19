// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * delete share request
 */
public class DeleteShareRequest extends TeaModel {
    // share_id
    @NameInMap("share_id")
    @Validation(required = true)
    public String shareId;

    public static DeleteShareRequest build(java.util.Map<String, ?> map) throws Exception {
        DeleteShareRequest self = new DeleteShareRequest();
        return TeaModel.build(map, self);
    }

    public DeleteShareRequest setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

}
