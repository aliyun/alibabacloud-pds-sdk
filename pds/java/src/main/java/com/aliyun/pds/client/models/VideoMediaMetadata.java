// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class VideoMediaMetadata extends TeaModel {
    /**
     * <p>Duration</p>
     */
    @NameInMap("duration")
    public String duration;

    /**
     * <p>taken_at</p>
     */
    @NameInMap("taken_at")
    public String takenAt;

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

    public VideoMediaMetadata setTakenAt(String takenAt) {
        this.takenAt = takenAt;
        return this;
    }
    public String getTakenAt() {
        return this.takenAt;
    }

}
