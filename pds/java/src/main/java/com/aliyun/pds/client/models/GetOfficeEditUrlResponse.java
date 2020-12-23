// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 获取office文档在线编辑地址 response
 */
public class GetOfficeEditUrlResponse extends TeaModel {
    // EditUrl
    @NameInMap("edit_url")
    public String editUrl;

    // AccessToken
    @NameInMap("office_access_token")
    public String officeAccessToken;

    // RefreshToken
    @NameInMap("office_refresh_token")
    public String officeRefreshToken;

    public static GetOfficeEditUrlResponse build(java.util.Map<String, ?> map) throws Exception {
        GetOfficeEditUrlResponse self = new GetOfficeEditUrlResponse();
        return TeaModel.build(map, self);
    }

    public GetOfficeEditUrlResponse setEditUrl(String editUrl) {
        this.editUrl = editUrl;
        return this;
    }
    public String getEditUrl() {
        return this.editUrl;
    }

    public GetOfficeEditUrlResponse setOfficeAccessToken(String officeAccessToken) {
        this.officeAccessToken = officeAccessToken;
        return this;
    }
    public String getOfficeAccessToken() {
        return this.officeAccessToken;
    }

    public GetOfficeEditUrlResponse setOfficeRefreshToken(String officeRefreshToken) {
        this.officeRefreshToken = officeRefreshToken;
        return this;
    }
    public String getOfficeRefreshToken() {
        return this.officeRefreshToken;
    }

}
