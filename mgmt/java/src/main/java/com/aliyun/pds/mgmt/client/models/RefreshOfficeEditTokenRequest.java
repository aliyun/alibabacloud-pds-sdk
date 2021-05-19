// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 刷新office文档在线编辑凭证
 */
public class RefreshOfficeEditTokenRequest extends TeaModel {
    // addition_data
    @NameInMap("addition_data")
    public java.util.Map<String, ?> additionData;

    // location
    @NameInMap("location")
    public String location;

    // AccessToken
    @NameInMap("office_access_token")
    @Validation(required = true)
    public String officeAccessToken;

    // RefreshToken
    @NameInMap("office_refresh_token")
    @Validation(required = true)
    public String officeRefreshToken;

    public static RefreshOfficeEditTokenRequest build(java.util.Map<String, ?> map) throws Exception {
        RefreshOfficeEditTokenRequest self = new RefreshOfficeEditTokenRequest();
        return TeaModel.build(map, self);
    }

    public RefreshOfficeEditTokenRequest setAdditionData(java.util.Map<String, ?> additionData) {
        this.additionData = additionData;
        return this;
    }
    public java.util.Map<String, ?> getAdditionData() {
        return this.additionData;
    }

    public RefreshOfficeEditTokenRequest setLocation(String location) {
        this.location = location;
        return this;
    }
    public String getLocation() {
        return this.location;
    }

    public RefreshOfficeEditTokenRequest setOfficeAccessToken(String officeAccessToken) {
        this.officeAccessToken = officeAccessToken;
        return this;
    }
    public String getOfficeAccessToken() {
        return this.officeAccessToken;
    }

    public RefreshOfficeEditTokenRequest setOfficeRefreshToken(String officeRefreshToken) {
        this.officeRefreshToken = officeRefreshToken;
        return this;
    }
    public String getOfficeRefreshToken() {
        return this.officeRefreshToken;
    }

}
