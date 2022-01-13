// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * base watermark config response
 */
public class BaseWatermarkConfigResponse extends TeaModel {
    @NameInMap("bold")
    public Boolean bold;

    @NameInMap("display_access_user_name")
    public Boolean displayAccessUserName;

    @NameInMap("display_custom_text")
    public String displayCustomText;

    @NameInMap("display_shareLink_creator_name")
    public Boolean displayShareLinkCreatorName;

    @NameInMap("enable_doc_preview")
    public Boolean enableDocPreview;

    @NameInMap("enable_on_preview")
    public Boolean enableOnPreview;

    @NameInMap("fill_style")
    public String fillStyle;

    @NameInMap("font")
    public String font;

    @NameInMap("horizontal")
    public Long horizontal;

    @NameInMap("rotate")
    public Long rotate;

    @NameInMap("size")
    public Long size;

    @NameInMap("vertical")
    public Long vertical;

    public static BaseWatermarkConfigResponse build(java.util.Map<String, ?> map) throws Exception {
        BaseWatermarkConfigResponse self = new BaseWatermarkConfigResponse();
        return TeaModel.build(map, self);
    }

    public BaseWatermarkConfigResponse setBold(Boolean bold) {
        this.bold = bold;
        return this;
    }
    public Boolean getBold() {
        return this.bold;
    }

    public BaseWatermarkConfigResponse setDisplayAccessUserName(Boolean displayAccessUserName) {
        this.displayAccessUserName = displayAccessUserName;
        return this;
    }
    public Boolean getDisplayAccessUserName() {
        return this.displayAccessUserName;
    }

    public BaseWatermarkConfigResponse setDisplayCustomText(String displayCustomText) {
        this.displayCustomText = displayCustomText;
        return this;
    }
    public String getDisplayCustomText() {
        return this.displayCustomText;
    }

    public BaseWatermarkConfigResponse setDisplayShareLinkCreatorName(Boolean displayShareLinkCreatorName) {
        this.displayShareLinkCreatorName = displayShareLinkCreatorName;
        return this;
    }
    public Boolean getDisplayShareLinkCreatorName() {
        return this.displayShareLinkCreatorName;
    }

    public BaseWatermarkConfigResponse setEnableDocPreview(Boolean enableDocPreview) {
        this.enableDocPreview = enableDocPreview;
        return this;
    }
    public Boolean getEnableDocPreview() {
        return this.enableDocPreview;
    }

    public BaseWatermarkConfigResponse setEnableOnPreview(Boolean enableOnPreview) {
        this.enableOnPreview = enableOnPreview;
        return this;
    }
    public Boolean getEnableOnPreview() {
        return this.enableOnPreview;
    }

    public BaseWatermarkConfigResponse setFillStyle(String fillStyle) {
        this.fillStyle = fillStyle;
        return this;
    }
    public String getFillStyle() {
        return this.fillStyle;
    }

    public BaseWatermarkConfigResponse setFont(String font) {
        this.font = font;
        return this;
    }
    public String getFont() {
        return this.font;
    }

    public BaseWatermarkConfigResponse setHorizontal(Long horizontal) {
        this.horizontal = horizontal;
        return this;
    }
    public Long getHorizontal() {
        return this.horizontal;
    }

    public BaseWatermarkConfigResponse setRotate(Long rotate) {
        this.rotate = rotate;
        return this;
    }
    public Long getRotate() {
        return this.rotate;
    }

    public BaseWatermarkConfigResponse setSize(Long size) {
        this.size = size;
        return this;
    }
    public Long getSize() {
        return this.size;
    }

    public BaseWatermarkConfigResponse setVertical(Long vertical) {
        this.vertical = vertical;
        return this;
    }
    public Long getVertical() {
        return this.vertical;
    }

}
