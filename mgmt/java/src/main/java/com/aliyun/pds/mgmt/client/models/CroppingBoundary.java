// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class CroppingBoundary extends TeaModel {
    @NameInMap("height")
    public Long height;

    @NameInMap("left")
    public Long left;

    @NameInMap("top")
    public Long top;

    @NameInMap("width")
    public Long width;

    public static CroppingBoundary build(java.util.Map<String, ?> map) throws Exception {
        CroppingBoundary self = new CroppingBoundary();
        return TeaModel.build(map, self);
    }

    public CroppingBoundary setHeight(Long height) {
        this.height = height;
        return this;
    }
    public Long getHeight() {
        return this.height;
    }

    public CroppingBoundary setLeft(Long left) {
        this.left = left;
        return this;
    }
    public Long getLeft() {
        return this.left;
    }

    public CroppingBoundary setTop(Long top) {
        this.top = top;
        return this;
    }
    public Long getTop() {
        return this.top;
    }

    public CroppingBoundary setWidth(Long width) {
        this.width = width;
        return this;
    }
    public Long getWidth() {
        return this.width;
    }

}
