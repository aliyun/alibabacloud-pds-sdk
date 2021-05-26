// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class FaceBoundary extends TeaModel {
    @NameInMap("height")
    public Long height;

    @NameInMap("left")
    public Long left;

    @NameInMap("top")
    public Long top;

    @NameInMap("width")
    public Long width;

    public static FaceBoundary build(java.util.Map<String, ?> map) throws Exception {
        FaceBoundary self = new FaceBoundary();
        return TeaModel.build(map, self);
    }

    public FaceBoundary setHeight(Long height) {
        this.height = height;
        return this;
    }
    public Long getHeight() {
        return this.height;
    }

    public FaceBoundary setLeft(Long left) {
        this.left = left;
        return this;
    }
    public Long getLeft() {
        return this.left;
    }

    public FaceBoundary setTop(Long top) {
        this.top = top;
        return this;
    }
    public Long getTop() {
        return this.top;
    }

    public FaceBoundary setWidth(Long width) {
        this.width = width;
        return this;
    }
    public Long getWidth() {
        return this.width;
    }

}
