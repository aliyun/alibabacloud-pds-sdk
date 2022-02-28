// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * WatermarkEnableConfig 功能开关及显示配置
 */
public class WatermarkEnableConfig extends TeaModel {
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

    public static WatermarkEnableConfig build(java.util.Map<String, ?> map) throws Exception {
        WatermarkEnableConfig self = new WatermarkEnableConfig();
        return TeaModel.build(map, self);
    }

    public WatermarkEnableConfig setDisplayAccessUserName(Boolean displayAccessUserName) {
        this.displayAccessUserName = displayAccessUserName;
        return this;
    }
    public Boolean getDisplayAccessUserName() {
        return this.displayAccessUserName;
    }

    public WatermarkEnableConfig setDisplayCustomText(String displayCustomText) {
        this.displayCustomText = displayCustomText;
        return this;
    }
    public String getDisplayCustomText() {
        return this.displayCustomText;
    }

    public WatermarkEnableConfig setDisplayShareLinkCreatorName(Boolean displayShareLinkCreatorName) {
        this.displayShareLinkCreatorName = displayShareLinkCreatorName;
        return this;
    }
    public Boolean getDisplayShareLinkCreatorName() {
        return this.displayShareLinkCreatorName;
    }

    public WatermarkEnableConfig setEnableDocPreview(Boolean enableDocPreview) {
        this.enableDocPreview = enableDocPreview;
        return this;
    }
    public Boolean getEnableDocPreview() {
        return this.enableDocPreview;
    }

    public WatermarkEnableConfig setEnableOnPreview(Boolean enableOnPreview) {
        this.enableOnPreview = enableOnPreview;
        return this;
    }
    public Boolean getEnableOnPreview() {
        return this.enableOnPreview;
    }

}
