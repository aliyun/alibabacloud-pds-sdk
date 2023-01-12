// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * GetDriveUsedSizeResponse
 */
public class GetDriveUsedSizeResponse extends TeaModel {
    /**
     * <p>used_size</p>
     */
    @NameInMap("used_size")
    public Long usedSize;

    public static GetDriveUsedSizeResponse build(java.util.Map<String, ?> map) throws Exception {
        GetDriveUsedSizeResponse self = new GetDriveUsedSizeResponse();
        return TeaModel.build(map, self);
    }

    public GetDriveUsedSizeResponse setUsedSize(Long usedSize) {
        this.usedSize = usedSize;
        return this;
    }
    public Long getUsedSize() {
        return this.usedSize;
    }

}
