// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class ImageMediaMetadata extends TeaModel {
    /**
     * <p>height</p>
     */
    @NameInMap("height")
    public Long height;

    /**
     * <p>taken_at</p>
     */
    @NameInMap("taken_at")
    public String takenAt;

    /**
     * <p>width：</p>
     */
    @NameInMap("width")
    public Long width;

    public static ImageMediaMetadata build(java.util.Map<String, ?> map) throws Exception {
        ImageMediaMetadata self = new ImageMediaMetadata();
        return TeaModel.build(map, self);
    }

    public ImageMediaMetadata setHeight(Long height) {
        this.height = height;
        return this;
    }
    public Long getHeight() {
        return this.height;
    }

    public ImageMediaMetadata setTakenAt(String takenAt) {
        this.takenAt = takenAt;
        return this;
    }
    public String getTakenAt() {
        return this.takenAt;
    }

    public ImageMediaMetadata setWidth(Long width) {
        this.width = width;
        return this;
    }
    public Long getWidth() {
        return this.width;
    }

}
