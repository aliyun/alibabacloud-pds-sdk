// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

/**
 * 获取文档预览地址 response
 */
public class GetOfficePreviewUrlResponse extends TeaModel {
    // AccessToken
    @NameInMap("access_token")
    public String accessToken;

    // preview_url
    @NameInMap("preview_url")
    public String previewUrl;

    public static GetOfficePreviewUrlResponse build(java.util.Map<String, ?> map) throws Exception {
        GetOfficePreviewUrlResponse self = new GetOfficePreviewUrlResponse();
        return TeaModel.build(map, self);
    }

    public GetOfficePreviewUrlResponse setAccessToken(String accessToken) {
        this.accessToken = accessToken;
        return this;
    }
    public String getAccessToken() {
        return this.accessToken;
    }

    public GetOfficePreviewUrlResponse setPreviewUrl(String previewUrl) {
        this.previewUrl = previewUrl;
        return this;
    }
    public String getPreviewUrl() {
        return this.previewUrl;
    }

}
