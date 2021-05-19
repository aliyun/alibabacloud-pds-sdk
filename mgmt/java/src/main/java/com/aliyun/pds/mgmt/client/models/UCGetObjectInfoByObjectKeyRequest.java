// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * UCGetObjectInfoByObjectKeyRequest
 */
public class UCGetObjectInfoByObjectKeyRequest extends TeaModel {
    @NameInMap("object_key")
    public String objectKey;

    public static UCGetObjectInfoByObjectKeyRequest build(java.util.Map<String, ?> map) throws Exception {
        UCGetObjectInfoByObjectKeyRequest self = new UCGetObjectInfoByObjectKeyRequest();
        return TeaModel.build(map, self);
    }

    public UCGetObjectInfoByObjectKeyRequest setObjectKey(String objectKey) {
        this.objectKey = objectKey;
        return this;
    }
    public String getObjectKey() {
        return this.objectKey;
    }

}
