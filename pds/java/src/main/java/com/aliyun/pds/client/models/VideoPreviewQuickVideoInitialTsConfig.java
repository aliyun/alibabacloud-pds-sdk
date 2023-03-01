// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 快速起播配置
 */
public class VideoPreviewQuickVideoInitialTsConfig extends TeaModel {
    @NameInMap("initial_duration")
    public Double initialDuration;

    @NameInMap("initial_ts_list")
    public java.util.List<Integer> initialTsList;

    public static VideoPreviewQuickVideoInitialTsConfig build(java.util.Map<String, ?> map) throws Exception {
        VideoPreviewQuickVideoInitialTsConfig self = new VideoPreviewQuickVideoInitialTsConfig();
        return TeaModel.build(map, self);
    }

    public VideoPreviewQuickVideoInitialTsConfig setInitialDuration(Double initialDuration) {
        this.initialDuration = initialDuration;
        return this;
    }
    public Double getInitialDuration() {
        return this.initialDuration;
    }

    public VideoPreviewQuickVideoInitialTsConfig setInitialTsList(java.util.List<Integer> initialTsList) {
        this.initialTsList = initialTsList;
        return this;
    }
    public java.util.List<Integer> getInitialTsList() {
        return this.initialTsList;
    }

}
