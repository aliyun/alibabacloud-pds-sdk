// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 转码接口response
 */
public class OSSVideoTranscodeResponse extends TeaModel {
    // definition_list
    @NameInMap("definition_list")
    public java.util.List<String> definitionList;

    // duration
    @NameInMap("duration")
    public Long duration;

    // hls_time
    @NameInMap("hls_time")
    public Long hlsTime;

    public static OSSVideoTranscodeResponse build(java.util.Map<String, ?> map) throws Exception {
        OSSVideoTranscodeResponse self = new OSSVideoTranscodeResponse();
        return TeaModel.build(map, self);
    }

    public OSSVideoTranscodeResponse setDefinitionList(java.util.List<String> definitionList) {
        this.definitionList = definitionList;
        return this;
    }
    public java.util.List<String> getDefinitionList() {
        return this.definitionList;
    }

    public OSSVideoTranscodeResponse setDuration(Long duration) {
        this.duration = duration;
        return this;
    }
    public Long getDuration() {
        return this.duration;
    }

    public OSSVideoTranscodeResponse setHlsTime(Long hlsTime) {
        this.hlsTime = hlsTime;
        return this;
    }
    public Long getHlsTime() {
        return this.hlsTime;
    }

}
