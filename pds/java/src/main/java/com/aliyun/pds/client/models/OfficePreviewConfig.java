// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * OfficePreviewConfig 文档预览配置
 */
public class OfficePreviewConfig extends TeaModel {
    @NameInMap("enabled")
    public Boolean enabled;

    public static OfficePreviewConfig build(java.util.Map<String, ?> map) throws Exception {
        OfficePreviewConfig self = new OfficePreviewConfig();
        return TeaModel.build(map, self);
    }

    public OfficePreviewConfig setEnabled(Boolean enabled) {
        this.enabled = enabled;
        return this;
    }
    public Boolean getEnabled() {
        return this.enabled;
    }

}
