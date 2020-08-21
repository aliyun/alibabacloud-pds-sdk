// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class VideoMediaMetadata extends TeaModel {
    // Duration
    @NameInMap("duration")
    public String duration;

    public static VideoMediaMetadata build(java.util.Map<String, ?> map) throws Exception {
        VideoMediaMetadata self = new VideoMediaMetadata();
        return TeaModel.build(map, self);
    }

    public VideoMediaMetadata setDuration(String duration) {
        this.duration = duration;
        return this;
    }
    public String getDuration() {
        return this.duration;
    }

}
