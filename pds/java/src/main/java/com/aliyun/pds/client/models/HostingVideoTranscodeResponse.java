// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 转码接口response
 */
public class HostingVideoTranscodeResponse extends TeaModel {
    /**
     * <p>definition_list</p>
     */
    @NameInMap("definition_list")
    public java.util.List<String> definitionList;

    /**
     * <p>duration</p>
     */
    @NameInMap("duration")
    public Long duration;

    /**
     * <p>hls_time</p>
     */
    @NameInMap("hls_time")
    public Long hlsTime;

    public static HostingVideoTranscodeResponse build(java.util.Map<String, ?> map) throws Exception {
        HostingVideoTranscodeResponse self = new HostingVideoTranscodeResponse();
        return TeaModel.build(map, self);
    }

    public HostingVideoTranscodeResponse setDefinitionList(java.util.List<String> definitionList) {
        this.definitionList = definitionList;
        return this;
    }
    public java.util.List<String> getDefinitionList() {
        return this.definitionList;
    }

    public HostingVideoTranscodeResponse setDuration(Long duration) {
        this.duration = duration;
        return this;
    }
    public Long getDuration() {
        return this.duration;
    }

    public HostingVideoTranscodeResponse setHlsTime(Long hlsTime) {
        this.hlsTime = hlsTime;
        return this;
    }
    public Long getHlsTime() {
        return this.hlsTime;
    }

}
