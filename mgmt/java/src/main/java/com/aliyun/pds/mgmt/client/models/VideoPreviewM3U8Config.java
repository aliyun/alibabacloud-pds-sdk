// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class VideoPreviewM3U8Config extends TeaModel {
    @NameInMap("hls_time")
    public Long hlsTime;

    public static VideoPreviewM3U8Config build(java.util.Map<String, ?> map) throws Exception {
        VideoPreviewM3U8Config self = new VideoPreviewM3U8Config();
        return TeaModel.build(map, self);
    }

    public VideoPreviewM3U8Config setHlsTime(Long hlsTime) {
        this.hlsTime = hlsTime;
        return this;
    }
    public Long getHlsTime() {
        return this.hlsTime;
    }

}
