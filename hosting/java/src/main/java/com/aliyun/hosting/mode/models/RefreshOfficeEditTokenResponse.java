// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

/**
 * 刷新office文档在线编辑凭证 response
 */
public class RefreshOfficeEditTokenResponse extends TeaModel {
    // AccessToken
    @NameInMap("office_access_token")
    public String officeAccessToken;

    // RefreshToken
    @NameInMap("office_refresh_token")
    public String officeRefreshToken;

    public static RefreshOfficeEditTokenResponse build(java.util.Map<String, ?> map) throws Exception {
        RefreshOfficeEditTokenResponse self = new RefreshOfficeEditTokenResponse();
        return TeaModel.build(map, self);
    }

    public RefreshOfficeEditTokenResponse setOfficeAccessToken(String officeAccessToken) {
        this.officeAccessToken = officeAccessToken;
        return this;
    }
    public String getOfficeAccessToken() {
        return this.officeAccessToken;
    }

    public RefreshOfficeEditTokenResponse setOfficeRefreshToken(String officeRefreshToken) {
        this.officeRefreshToken = officeRefreshToken;
        return this;
    }
    public String getOfficeRefreshToken() {
        return this.officeRefreshToken;
    }

}
