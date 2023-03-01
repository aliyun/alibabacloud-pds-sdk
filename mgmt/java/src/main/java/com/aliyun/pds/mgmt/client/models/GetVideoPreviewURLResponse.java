// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 获取视频文件播放 url response
 */
public class GetVideoPreviewURLResponse extends TeaModel {
    /**
     * <p>preview_url</p>
     */
    @NameInMap("preview_url")
    public String previewUrl;

    public static GetVideoPreviewURLResponse build(java.util.Map<String, ?> map) throws Exception {
        GetVideoPreviewURLResponse self = new GetVideoPreviewURLResponse();
        return TeaModel.build(map, self);
    }

    public GetVideoPreviewURLResponse setPreviewUrl(String previewUrl) {
        this.previewUrl = previewUrl;
        return this;
    }
    public String getPreviewUrl() {
        return this.previewUrl;
    }

}
