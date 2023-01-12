// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 获取云照片个数结果
 */
public class GetImageCountResponse extends TeaModel {
    /**
     * <p>image_count</p>
     */
    @NameInMap("image_count")
    public Long imageCount;

    public static GetImageCountResponse build(java.util.Map<String, ?> map) throws Exception {
        GetImageCountResponse self = new GetImageCountResponse();
        return TeaModel.build(map, self);
    }

    public GetImageCountResponse setImageCount(Long imageCount) {
        this.imageCount = imageCount;
        return this;
    }
    public Long getImageCount() {
        return this.imageCount;
    }

}
