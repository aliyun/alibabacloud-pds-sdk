// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.hostingmode.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class ImageMediaMetadata extends TeaModel {
    // height
    @NameInMap("height")
    public Long height;

    // width：
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

    public ImageMediaMetadata setWidth(Long width) {
        this.width = width;
        return this;
    }
    public Long getWidth() {
        return this.width;
    }

}
