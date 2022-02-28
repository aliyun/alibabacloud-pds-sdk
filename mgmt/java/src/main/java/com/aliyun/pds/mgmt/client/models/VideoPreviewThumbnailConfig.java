// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 截图配置
 */
public class VideoPreviewThumbnailConfig extends TeaModel {
    @NameInMap("skip_begin_percent")
    public String skipBeginPercent;

    @NameInMap("skip_begin_sec")
    public Double skipBeginSec;

    public static VideoPreviewThumbnailConfig build(java.util.Map<String, ?> map) throws Exception {
        VideoPreviewThumbnailConfig self = new VideoPreviewThumbnailConfig();
        return TeaModel.build(map, self);
    }

    public VideoPreviewThumbnailConfig setSkipBeginPercent(String skipBeginPercent) {
        this.skipBeginPercent = skipBeginPercent;
        return this;
    }
    public String getSkipBeginPercent() {
        return this.skipBeginPercent;
    }

    public VideoPreviewThumbnailConfig setSkipBeginSec(Double skipBeginSec) {
        this.skipBeginSec = skipBeginSec;
        return this;
    }
    public Double getSkipBeginSec() {
        return this.skipBeginSec;
    }

}
