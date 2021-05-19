// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class VideoPreviewThumbnail extends TeaModel {
    @NameInMap("skip_begin_percent")
    public String skipBeginPercent;

    @NameInMap("skip_begin_sec")
    public Double skipBeginSec;

    public static VideoPreviewThumbnail build(java.util.Map<String, ?> map) throws Exception {
        VideoPreviewThumbnail self = new VideoPreviewThumbnail();
        return TeaModel.build(map, self);
    }

    public VideoPreviewThumbnail setSkipBeginPercent(String skipBeginPercent) {
        this.skipBeginPercent = skipBeginPercent;
        return this;
    }
    public String getSkipBeginPercent() {
        return this.skipBeginPercent;
    }

    public VideoPreviewThumbnail setSkipBeginSec(Double skipBeginSec) {
        this.skipBeginSec = skipBeginSec;
        return this;
    }
    public Double getSkipBeginSec() {
        return this.skipBeginSec;
    }

}
