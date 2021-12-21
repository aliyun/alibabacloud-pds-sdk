// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

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
