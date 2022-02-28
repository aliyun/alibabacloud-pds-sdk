// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 目前只提供一定的参数化即可, 因为太参数化会让整个代码逻辑过于复杂, 容易留下 bug
通过 hotfix 升级后台任务实现定制策略优化
 */
public class VideoPreviewTemplatePolicyAliyundriveConfig extends TeaModel {
    @NameInMap("pre_transcode_begin_duration")
    public Long preTranscodeBeginDuration;

    public static VideoPreviewTemplatePolicyAliyundriveConfig build(java.util.Map<String, ?> map) throws Exception {
        VideoPreviewTemplatePolicyAliyundriveConfig self = new VideoPreviewTemplatePolicyAliyundriveConfig();
        return TeaModel.build(map, self);
    }

    public VideoPreviewTemplatePolicyAliyundriveConfig setPreTranscodeBeginDuration(Long preTranscodeBeginDuration) {
        this.preTranscodeBeginDuration = preTranscodeBeginDuration;
        return this;
    }
    public Long getPreTranscodeBeginDuration() {
        return this.preTranscodeBeginDuration;
    }

}
