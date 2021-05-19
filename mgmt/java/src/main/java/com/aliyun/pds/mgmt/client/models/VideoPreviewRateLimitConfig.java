// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class VideoPreviewRateLimitConfig extends TeaModel {
    @NameInMap("rate_limit")
    public Long rateLimit;

    public static VideoPreviewRateLimitConfig build(java.util.Map<String, ?> map) throws Exception {
        VideoPreviewRateLimitConfig self = new VideoPreviewRateLimitConfig();
        return TeaModel.build(map, self);
    }

    public VideoPreviewRateLimitConfig setRateLimit(Long rateLimit) {
        this.rateLimit = rateLimit;
        return this;
    }
    public Long getRateLimit() {
        return this.rateLimit;
    }

}
