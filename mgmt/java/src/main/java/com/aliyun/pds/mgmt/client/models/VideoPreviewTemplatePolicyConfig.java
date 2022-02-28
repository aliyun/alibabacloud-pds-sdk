// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 转码模板选择策略配置
 */
public class VideoPreviewTemplatePolicyConfig extends TeaModel {
    @NameInMap("aliyundrive_config")
    public VideoPreviewTemplatePolicyAliyundriveConfig aliyundriveConfig;

    @NameInMap("policy")
    public String policy;

    public static VideoPreviewTemplatePolicyConfig build(java.util.Map<String, ?> map) throws Exception {
        VideoPreviewTemplatePolicyConfig self = new VideoPreviewTemplatePolicyConfig();
        return TeaModel.build(map, self);
    }

    public VideoPreviewTemplatePolicyConfig setAliyundriveConfig(VideoPreviewTemplatePolicyAliyundriveConfig aliyundriveConfig) {
        this.aliyundriveConfig = aliyundriveConfig;
        return this;
    }
    public VideoPreviewTemplatePolicyAliyundriveConfig getAliyundriveConfig() {
        return this.aliyundriveConfig;
    }

    public VideoPreviewTemplatePolicyConfig setPolicy(String policy) {
        this.policy = policy;
        return this;
    }
    public String getPolicy() {
        return this.policy;
    }

}
