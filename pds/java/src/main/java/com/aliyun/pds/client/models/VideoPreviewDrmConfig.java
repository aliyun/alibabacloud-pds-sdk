// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 *
 */
public class VideoPreviewDrmConfig extends TeaModel {
    @NameInMap("region")
    public String region;

    public static VideoPreviewDrmConfig build(java.util.Map<String, ?> map) throws Exception {
        VideoPreviewDrmConfig self = new VideoPreviewDrmConfig();
        return TeaModel.build(map, self);
    }

    public VideoPreviewDrmConfig setRegion(String region) {
        this.region = region;
        return this;
    }
    public String getRegion() {
        return this.region;
    }

}
