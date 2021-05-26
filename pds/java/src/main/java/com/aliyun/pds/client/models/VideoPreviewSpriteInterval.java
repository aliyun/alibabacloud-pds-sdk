// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 雪碧图抓图间隔配置。如果配置异常，默认以1%抓图
 */
public class VideoPreviewSpriteInterval extends TeaModel {
    @NameInMap("default_interval")
    public String defaultInterval;

    @NameInMap("grab_interval_list")
    public java.util.List<String> grabIntervalList;

    @NameInMap("upper_limit_list")
    public java.util.List<Integer> upperLimitList;

    public static VideoPreviewSpriteInterval build(java.util.Map<String, ?> map) throws Exception {
        VideoPreviewSpriteInterval self = new VideoPreviewSpriteInterval();
        return TeaModel.build(map, self);
    }

    public VideoPreviewSpriteInterval setDefaultInterval(String defaultInterval) {
        this.defaultInterval = defaultInterval;
        return this;
    }
    public String getDefaultInterval() {
        return this.defaultInterval;
    }

    public VideoPreviewSpriteInterval setGrabIntervalList(java.util.List<String> grabIntervalList) {
        this.grabIntervalList = grabIntervalList;
        return this;
    }
    public java.util.List<String> getGrabIntervalList() {
        return this.grabIntervalList;
    }

    public VideoPreviewSpriteInterval setUpperLimitList(java.util.List<Integer> upperLimitList) {
        this.upperLimitList = upperLimitList;
        return this;
    }
    public java.util.List<Integer> getUpperLimitList() {
        return this.upperLimitList;
    }

}
