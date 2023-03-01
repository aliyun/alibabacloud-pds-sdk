// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class FaceBoundary extends TeaModel {
    @NameInMap("Height")
    public Long Height;

    @NameInMap("Left")
    public Long Left;

    @NameInMap("Top")
    public Long Top;

    @NameInMap("Width")
    public Long Width;

    public static FaceBoundary build(java.util.Map<String, ?> map) throws Exception {
        FaceBoundary self = new FaceBoundary();
        return TeaModel.build(map, self);
    }

    public FaceBoundary setHeight(Long Height) {
        this.Height = Height;
        return this;
    }
    public Long getHeight() {
        return this.Height;
    }

    public FaceBoundary setLeft(Long Left) {
        this.Left = Left;
        return this;
    }
    public Long getLeft() {
        return this.Left;
    }

    public FaceBoundary setTop(Long Top) {
        this.Top = Top;
        return this;
    }
    public Long getTop() {
        return this.Top;
    }

    public FaceBoundary setWidth(Long Width) {
        this.Width = Width;
        return this;
    }
    public Long getWidth() {
        return this.Width;
    }

}
