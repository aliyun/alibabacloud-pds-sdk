// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 实时转码meta响应
 */
public class LiveTranscodingMetaResponse extends TeaModel {
    // ts_pre_count
    @NameInMap("ts_pre_count")
    public Long tsPreCount;

    // ts_segment
    @NameInMap("ts_segment")
    public Long tsSegment;

    // ts_total_count
    @NameInMap("ts_total_count")
    public Long tsTotalCount;

    public static LiveTranscodingMetaResponse build(java.util.Map<String, ?> map) throws Exception {
        LiveTranscodingMetaResponse self = new LiveTranscodingMetaResponse();
        return TeaModel.build(map, self);
    }

    public LiveTranscodingMetaResponse setTsPreCount(Long tsPreCount) {
        this.tsPreCount = tsPreCount;
        return this;
    }
    public Long getTsPreCount() {
        return this.tsPreCount;
    }

    public LiveTranscodingMetaResponse setTsSegment(Long tsSegment) {
        this.tsSegment = tsSegment;
        return this;
    }
    public Long getTsSegment() {
        return this.tsSegment;
    }

    public LiveTranscodingMetaResponse setTsTotalCount(Long tsTotalCount) {
        this.tsTotalCount = tsTotalCount;
        return this;
    }
    public Long getTsTotalCount() {
        return this.tsTotalCount;
    }

}
